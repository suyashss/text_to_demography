import demes
import numpy as np 
from numpy import random
import pandas as pd
#from example_defs import Example1, Example2, Example3
from utils import validate_filled_description, validate_filled_yaml
import example_defs
from datasets import Dataset

np.random.seed(42)
desc_entries = []
yaml_entries = []
num_examples = 10000

def generate_example_from_class(class_name,yamlstr,description_list):
    current_desc_entries = []
    current_yaml_entries = []
    if hasattr(example_defs, class_name):
        class_ref = getattr(example_defs, class_name)
    else:
        raise ValueError(f"Class {class_name} not found!")
    for i in range(num_examples):
        example = class_ref.generate_example()
        filled_yaml = yamlstr.format(**dict(example)) 
        description = random.choice(description_list)
        filled_description = description.format(**dict(example)) 
        validate_filled_description(filled_description)
        validate_filled_yaml(filled_yaml)
        #ob = demes.loads(filled_yaml)
        current_desc_entries.append(filled_description)
        current_yaml_entries.append(filled_yaml)
    return current_desc_entries,current_yaml_entries

for i in range(1,10):
    print(i)
    class_name = f"Example{i}"
    yamlstr = open(f"training_set_manual/example{i}.yaml").read().strip()
    description_list = [open(f"training_set_manual/example{i}.description").read().strip()] + \
        [x.strip().strip('"') for x in open(f"training_set_manual/example{i}.description.alts").readlines()]
    curr_desc_entries, curr_yaml_entries = generate_example_from_class(class_name, yamlstr, description_list)
    desc_entries += curr_desc_entries
    yaml_entries += curr_yaml_entries

""" yamlstr = open("training_set_manual/example2.yaml").read().strip()
description_list = [open("training_set_manual/example2.description").read().strip()] + \
    [x.strip().strip('"') for x in open("training_set_manual/example2.description.alts").readlines()]

print("Simulating Example2")
for i in range(num_examples):
    example = Example2.generate_example()
    filled_yaml = yamlstr.format(**dict(example)) 
    description = random.choice(description_list)
    filled_description = description.format(**dict(example)) 
    ob = demes.loads(filled_yaml)
    desc_entries.append(filled_description)
    yaml_entries.append(filled_yaml)

yamlstr = open("training_set_manual/example3.yaml").read().strip()
description_list = [open("training_set_manual/example3.description").read().strip()] + \
    [x.strip().strip('"') for x in open("training_set_manual/example3.description.alts").readlines()]

print("Simulating Example3")
for i in range(num_examples):
    example = Example3.generate_example()
    filled_yaml = yamlstr.format(**dict(example)) 
    description = random.choice(description_list)
    filled_description = description.format(**dict(example)) 
    ob = demes.loads(filled_yaml)
    desc_entries.append(filled_description)
    yaml_entries.append(filled_yaml)
 """
example_dict = {'Description':desc_entries,
                'YAML':yaml_entries}    
example_df = pd.DataFrame(example_dict)
print(example_df.head())
print(example_df.tail())
print(example_df.shape)
print(np.sum(['{' in x for x in example_df['Description']]))

indices = np.arange(len(example_df))
random.shuffle(indices)
train_fraction = 0.9
valid_fraction = 0.05
train_max_index = int(len(example_df)*train_fraction)
valid_max_index = train_max_index + int(len(example_df)*valid_fraction)

train_df = example_df.iloc[:train_max_index]
valid_df = example_df.iloc[train_max_index:valid_max_index]
test_df = example_df.iloc[valid_max_index:]

print(f"Sizes of train/valid/test df are:{len(train_df)},{len(valid_df)},{len(test_df)}")

""" hf_dataset = "suyashss/synthetic_demography"
print(f"Loading {hf_dataset}")

train_dataset = Dataset.from_pandas(train_df)
train_dataset.push_to_hub(hf_dataset,split='train')

valid_dataset = Dataset.from_pandas(valid_df)
valid_dataset.push_to_hub(hf_dataset,split='valid')

test_dataset = Dataset.from_pandas(test_df)
test_dataset.push_to_hub(hf_dataset,split='test')

print(f"Completed push to {hf_dataset}")
 """