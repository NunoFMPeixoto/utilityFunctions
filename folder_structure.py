import os

# Function to create directories
def create_directories(base_path, structure):
    for folder, subfolders in structure.items():
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        for subfolder in subfolders:
            os.makedirs(os.path.join(path, subfolder), exist_ok=True)


def create_ml_folders():
    # Define the folder structure to create
    folder_structure = {
        "data": ["processed", "raw"],
        "docs": [],
        "models": [],
        "notebooks": [],
        "reports": [],
        "scripts": [],
        "src": ["data", "features", "models", "visualization"],
        "tests": []
    }

    # Base path to create the folders in
    base_path = './'

    # Create the directory structure
    create_directories(base_path, folder_structure)

    # # List the created directories to verify
    # created_directories = []
    # for root, dirs, files in os.walk(base_path):
    #     for dir in dirs:
    #         created_directories.append(os.path.relpath(os.path.join(root, dir), base_path))

