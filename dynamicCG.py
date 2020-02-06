import sys
import pytest
import py_call_graph


if __name__ == '__main__':
    if len(sys.argv) > 1:
        tc_file = sys.argv[1]
        tc_to_run = ['-x']
        with open(tc_file) as f:
            for line in f:
                tc_to_run.append(str(line.replace("\n", "")))
        pytest.main(tc_to_run, plugins=[py_call_graph])
    else:
        pytest.main(['--maxfail=10', './test/'], plugins=[py_call_graph])
