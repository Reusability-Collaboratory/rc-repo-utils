import os
from os.path import join

import git


def find_definition(def_name: str, containing_folder: str=None, namespace: str = None):
    """
    Searches among modules directories and
    returns the directory path that matches def_name
    under the specified namespace directory

    Args:
        - containing_folder (str): Search only within this directory path. Current working directory by default.
        - namespace (str): Within containing_folder, find a folder with this name and search only under this folder.
    """
    if containing_folder is None:
        repo = git.Repo(containing_folder, search_parent_directories=True)
        src_root = repo.working_tree_dir
    # src_root = join(repo_root, repo.name) # subfolder with same name
    # level_offset = len(src_root.split(os.sep)) - 1

    if namespace is None:
        for dir_path, dirs, _ in os.walk(src_root):
            if dir_path == "build" or dir_path.endswith(os.sep + "build"):
                continue
            for dir_name in dirs:
                if dir_name == def_name:
                    return join(dir_path, dir_name)
    else:
        for dir_path, dirs, _ in os.walk(src_root):
            for dir_name in dirs:
                if dir_name == "build":
                    continue
                if not namespace or dir_name == namespace:
                    for space_path, space_dirs, space_files in os.walk(
                        join(dir_path, dir_name)
                    ):
                        for def_dir in space_dirs:
                            if def_dir == def_name:
                                return join(space_path, def_dir)
                    if namespace:
                        break
    return None
