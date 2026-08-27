import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path,file_path))
        #print(f"target_file: {target_file}\n")
        valid_target_path = os.path.commonpath([abs_path,target_file]) == abs_path
        #print(f"valid target path? {valid_target_path}\n")
        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(working_directory, exist_ok=True)
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except FileNotFoundError:
        return (f"Error: The file at {file_path} could not be found.")
    except PermissionError:
        return ("Error: You do not have permissions to access this file.")
    except TypeError:
        return ("Error: Provided path must be a string or bytes-like object.")
            
    