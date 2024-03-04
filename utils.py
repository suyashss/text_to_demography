import demes

def check_equal_yaml_files(fname1,fname2):
    graph1 = demes.load(fname1)
    graph2 = demes.load(fname2)
    return graph1.isclose(graph2)

def check_equal_yaml_strings(str1,str2):
    graph1 = demes.loads(str1)
    graph2 = demes.loads(str2)
    return graph1.isclose(graph2)
