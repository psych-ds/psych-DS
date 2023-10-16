import argparse
import yaml
import os
import json

def construct_dict(subdir):
    subdirs = [name for name in os.listdir(subdir) if os.path.isdir(os.path.join(subdir, name)) and 'DS' not in name]
    yamls = [name for name in os.listdir(subdir) if not os.path.isdir(os.path.join(subdir, name)) and 'DS' not in name]
    
    this_dict = {}

    for sub in subdirs:
        this_dict[sub] = construct_dict(os.path.join(subdir,sub))
    
    for yaml_file in yamls:
        with open(os.path.join(subdir,yaml_file)) as f:
            yaml_data = yaml.load(f, Loader=yaml.FullLoader)
            this_dict[yaml_file.split('.')[0]] = yaml_data
    
    return this_dict

def main(input_dir):
    subdirs = [name for name in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, name)) and 'DS' not in name]

    master_dict = {}

    for subdir in subdirs:
        master_dict[subdir] = construct_dict(os.path.join(input_dir, subdir))
    
    with open('schema.json','w') as f:
        json.dump(master_dict,f,indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir',type=str,help="Input directory")
    args = parser.parse_args()

    # Validate input directory
    if not os.path.isdir(args.input_dir):
        raise ValueError(f'Invalid directory: {args.input_dir}')  

    main(args.input_dir)