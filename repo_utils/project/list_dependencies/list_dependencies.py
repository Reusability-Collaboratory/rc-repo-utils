import os
import re
from os.path import join

from repo_utils import find_definition, get_repository_path


def list_dependencies(path_or_def: str, package_name: str = None):
    """
    Determine dependencies within a repository or package.

    Args:
        - path_or_def (str): If a string with no /, locate the definition with find_definition
            and identify all dependencies by imports recursively.
            If a directory path, search for imports among all files at that path recursively in subfolders.
        - package_name (str): The package name used when importing (only these imports will be listed).
            If not provided, will use the path set at __meta__.py at the repository root (TODO).

    Returns:
        - dependencies (list): List of unique dependent definitions.
    """
    # if package_name is None:
    # exec(read("TODO/__meta__.py"), meta)
    filenames_to_search = []
    dependencies = []
    if os.sep not in path_or_def:
        # path_or_def is a definition name.
        def_path = join(find_definition(path_or_def), f"{path_or_def}.py")
        file_dependencies = list_file_dependencies(def_path, package_name)
        dependencies.extend(file_dependencies)
        for dependency in dependencies:
            dependencies
    else:
        # path_or_def is a folder path.
        for dirpath, dirs, files in os.walk(path_or_def):
            for filename in files:
                if not filename.endswith(".py"):
                    continue
                filepath = join(dirpath, filename)
                file_dependencies = list_file_dependencies(filepath, package_name)
                dependencies.extend(file_dependencies)
    return list(set(dependencies))


def list_file_dependencies(filepath, package_name):
    """
    Given a filepath, return a list of dependencies based on imports in just that file.

    Returns:
        - dependencies (list): List of dependent definitions in the order in which they were found.

    Implementation:
        1. Include the filename as a dependency if it's the same name as the containing folder.
    """
    dependencies = []
    split_filepath = filepath.split(os.sep)
    # 1. Include the filename as a dependency if it's the same name as the containing folder.
    if len(split_filepath) > 1:
        def_name = split_filepath[-1].strip().split(".")[0]
        if def_name == split_filepath[-2]:
            dependencies.append(split_filepath[-2])
    with open(filepath, "r") as file:
        for line in file.readlines():
            line = line.strip()
            if not line.startswith("from"):
                continue
            line = line[4:].strip()  # Remove from.
            if line.startswith(package_name):
                split_line = line.split("import")
                if len(split_line) > 1:
                    imported = split_line[1]
                    split_imported = imported.split(",")
                    for imported in split_imported:
                        imported = imported.strip()
                        if imported:
                            dependencies.append(imported)
    return dependencies
