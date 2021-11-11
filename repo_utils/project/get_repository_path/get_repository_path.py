import git


def get_repository_path():
    """Return the path of the root directory of this repository"""
    repo = git.Repo(__file__, search_parent_directories=True)
    repo_root = repo.working_tree_dir
    return repo_root
