import sys
from os.path import join

from repo_utils import find_definition, pytest_on_path


def test_def(def_name: str, namespace: str = None, test_func: str = None):
    """Given the name of a definition to test_def,
    run the chosen test_def module on it"""
    def_dir = find_definition(def_name, namespace=namespace)
    # In order to specify function, the specific
    # test_def file must be specified, so it
    # will only search within the test_def file named after
    # the definition
    if def_dir:
        return pytest_on_path(join(def_dir), test_func=test_func)
    else:
        print(f"No definition found named {def_name}", file=sys.stderr)
