# Trello card: https://trello.com/c/iCFGS1kC/73-import-definition
from repo_utils import def_from_dir, find_definition


def import_definition(name: str, namespace: str = None):
    """Import a definition based on its name without its path
    Returns the imported function or object, not the module
    namespace should be a directory or path from <repo_root>/src
    If the module name is not found, return None"""
    def_dir = find_definition(name, namespace=namespace)
    if def_dir:
        definition = def_from_dir(def_dir)
        return definition
