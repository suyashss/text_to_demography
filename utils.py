import demes

def validate_filled_description(description: str):
    assert description.find("{") == -1, f"Unfilled variable in description: {description}"
    return True

def validate_filled_yaml(filled_yaml: str):
    try:
        ob = demes.loads(filled_yaml)
    except KeyError as k:
        print(k)
        return False
    except Exception as e:
        print(f'Error loading {filled_yaml}')
        return False
    return True

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
        graph1 = demes.loads(str1)
    except KeyError as k:
        print(k)
        return False
    except Exception as e:
        print(f'Error loading {str1}')
        return False
    try:
        graph2 = demes.loads(str2)
    except KeyError as k:
        print(k)
        return False
    except Exception as e:
        print(f'Error loading {str2}')
        return False
    return graph1.isclose(graph2)
