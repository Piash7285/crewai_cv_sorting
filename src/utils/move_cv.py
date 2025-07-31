def move(path, destination):
    import os
    import shutil

    if not os.path.exists(destination):
        os.makedirs(destination)

    try:
        shutil.move(path, destination)
        print(f"Moved {path} to {destination}")
    except Exception as e:
        print(f"Error moving file: {e}")