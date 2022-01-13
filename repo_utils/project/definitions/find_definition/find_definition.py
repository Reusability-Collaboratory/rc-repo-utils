import os
from os.path import join

import git


def find_definition(def_name: str, namespace: str = None):
    """
    Searches among modules directories and
    returns the directory path that matches def_name
    under the specified namespace directory
    """
    repo = git.Repo(os.getcwd(), search_parent_directories=True)
    src_root = repo.working_tree_dir
    # src_root = join(repo_root, repo.name) # subfolder with same name
    level_offset = len(src_root.split(os.sep)) - 1

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
