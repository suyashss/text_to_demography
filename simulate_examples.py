import demes
import numpy as np 
from numpy import random
import pandas as pd
from utils import validate_filled_description, validate_filled_yaml
import example_defs
from datasets import Dataset

np.random.seed(42)
desc_entries = []
yaml_entries = []
num_examples_base = 10000

def generate_example_from_class(class_name,yamlstr,description_list,num_examples=1000):
    current_desc_entries = []
    current_yaml_entries = []
    if hasattr(example_defs, class_name):
        class_ref = getattr(example_defs, class_name)
        field_names = class_ref.__fields__.keys()
        num_fields = len([x for x in field_names if 'description' not in x and 'change' not in x])
    else:
        raise ValueError(f"Class {class_name} not found!")
    for i in range(num_examples * num_fields):
        example = class_ref.generate_example()
        filled_yaml = yamlstr.format(**dict(example)) 
        description = random.choice(description_list)
        filled_description = description.format(**dict(example)) 
        if not validate_filled_description(filled_description):
            continue
        if not validate_filled_yaml(filled_yaml):
            continue
        current_desc_entries.append(filled_description)
        current_yaml_entries.append(filled_yaml)
    return current_desc_entries,current_yaml_entries

for i in range(1,10):
    print(i)
    class_name = f"Example{i}"
    yamlstr = open(f"training_set_manual/example{i}.yaml").read().strip()
    description_list = [open(f"training_set_manual/example{i}.description").read().strip()] + \
        [x.strip().strip('"') for x in open(f"training_set_manual/example{i}.description.alts").readlines()]
    curr_desc_entries, curr_yaml_entries = generate_example_from_class(class_name, yamlstr, 
                                                                       description_list,num_examples_base)
    print([class_name,len(curr_desc_entries)])
    desc_entries += curr_desc_entries
    yaml_entries += curr_yaml_entries

example_dict = {'instruction':desc_entries,
                'output':yaml_entries}    
example_df = pd.DataFrame(example_dict)
print(example_df.head())
print(example_df.tail())
print(example_df.shape)
print(np.sum(['{' in x for x in example_df['instruction']]))

indices = np.arange(len(example_df))
random.shuffle(indices)
train_fraction = 0.9
valid_fraction = 0.05
train_max_index = int(len(example_df)*train_fraction)
valid_max_index = train_max_index + int(len(example_df)*valid_fraction)

train_df = example_df.iloc[indices[:train_max_index]]
valid_df = example_df.iloc[indices[train_max_index:valid_max_index]]
test_df = example_df.iloc[indices[valid_max_index:]]

print(f"Sizes of train/valid/test df are:{len(train_df)},{len(valid_df)},{len(test_df)}")

hf_dataset = "suyashss/synthetic_demography_multipop" 
print(f"Loading {hf_dataset}")

train_dataset = Dataset.from_pandas(train_df)
train_dataset.push_to_hub(hf_dataset,split='train')#,private=True)

valid_dataset = Dataset.from_pandas(valid_df)
valid_dataset.push_to_hub(hf_dataset,split='valid')

test_dataset = Dataset.from_pandas(test_df)
test_dataset.push_to_hub(hf_dataset,split='test')

print(f"Completed push to {hf_dataset}")

outprefix = hf_dataset.split("/")[1]
filename = f'{outprefix}.jsonl'
train_dataset.to_json(filename,lines=True)