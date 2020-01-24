import pytest
import py_call_graph


if __name__ == '__main__':
    pytest.main(['--maxfail=10', './test/'], plugins=[py_call_graph])
