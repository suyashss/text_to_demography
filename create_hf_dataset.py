from argparse import ArgumentParser
import pandas as pd
import glob
import os
from datasets import Dataset

def main():
    parser = ArgumentParser("Take in a directory with paired yaml files and description, and save to a HF dataset")
    parser.add_argument("inputdir")
    parser.add_argument("hf_dataset")

    args = parser.parse_args()

    inputdir = args.inputdir
    hf_dataset = args.hf_dataset

    yamls = glob.glob(inputdir+"/*.yaml")
    descriptions = [x.replace(".yaml",".description") for x in yamls]

    entries = []
    for yaml_fn,description_fn in zip(yamls,descriptions):
        if not os.path.exists(description_fn):
            print(f'File {description_fn} not found, skipping {yaml_fn}')
            continue
        yaml_str = open(yaml_fn,'r').read().strip()
        description_str = open(description_fn,'r').read().strip()
        entries.append([description_str,yaml_str])

    entry_df = pd.DataFrame.from_records(entries,columns=['Description','YAML'])
    print(entry_df.shape)

    print(f"Loading {hf_dataset}")
    dataset = Dataset.from_pandas(entry_df)
    dataset.push_to_hub(hf_dataset)
    print(f"Completed push to {hf_dataset}")

if __name__ == "__main__":
    main()

