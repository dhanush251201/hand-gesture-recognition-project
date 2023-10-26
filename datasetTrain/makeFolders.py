import os
import json

TRAIN_PATH="/Users/dhanush/Documents/D/college/sem7/project/MSASL_train.json"

def create_folder(path, folder_name):
    # Combine the path and folder name to create the full directory path
    directory = os.path.join(path, folder_name)

    try:
        # Create the directory if it doesn't exist
        os.makedirs(directory)
        print(f"Folder '{folder_name}' created at {path}")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists at {path}")

# Example usage:
folder_name = "my_new_folder"
path = "/Users/dhanush/Documents/D/college/sem7/project/datasetTrain"



with open(TRAIN_PATH, "r") as json_file:
    json_string = json_file.read()
    data = json.loads(json_string)
for i in data:
    create_folder(path, dict(i)['clean_text'])


create_folder(path, folder_name)
