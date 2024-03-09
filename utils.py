import demes

def check_equal_yaml_files(fname1,fname2):
    try:
        graph1 = demes.load(fname1)
    except Exception as e:
        print(f'Error loading {fname1}')
        return False
    try:
        graph2 = demes.load(fname2)
    except Exception as e:
        print(f'Error loading {fname2}')
        return False
    return graph1.isclose(graph2)

def check_equal_yaml_strings(str1,str2):
    try:
        graph1 = demes.load(str1)
    except Exception as e:
        print(f'Error loading {str1}')
        return False
    try:
        graph2 = demes.load(str2)
    except Exception as e:
        print(f'Error loading {str2}')
        return False
    return graph1.isclose(graph2)
