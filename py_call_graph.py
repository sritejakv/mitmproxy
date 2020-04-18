import pytest
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph.config import Config
from pycallgraph.globbing_filter import GlobbingFilter


@pytest.fixture(autouse=True)
def record_call_graph(request):
    import time
    current_millis = int(round(time.time() * 1000))
    total_input_files = set()
    with open("../entry_point_extractor/commonEntryPoints/mitmproxy.txt") as f:
        for line in f:
            temp = line.split("mitmproxy")[-1][1:]
            temp = temp.replace("/", ".")
            temp = temp.replace(".py", ".*")
            temp = temp.replace("\n", "")
            if len(temp) > 0:
                total_input_files.add("mitmproxy." + temp)

    with PyCallGraph(output=GraphvizOutput(dot_file='./dotFiles/%s.dot' % current_millis),
                     config=Config(debug=True,
                                   trace_filter=GlobbingFilter(
                                       include=list(total_input_files),
                                       exclude=['pycallgraph.*', 'test*.*', '*.tests.*', '*test.*']
                                   )
                                   )):
        yield
