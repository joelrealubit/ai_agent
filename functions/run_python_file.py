import os

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path,file_path))
        #print(f"target_file: {target_file}\n")
        valid_target_path = os.path.commonpath([abs_path,target_file]) == abs_path
        #print(f"valid target path? {valid_target_path}\n")
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: {file_path} does not exist or is not a regular file'
        root, extension = os.path.splitext(file_path)
        if not extension == '.py':
            return f'Error: "{file_path}" is not a Python file'
        
    except FileNotFoundError:
        return (f"Error: The file at {file_path} could not be found.")
    except PermissionError:
        return ("Error: You do not have permissions to access this file.")
    except TypeError:
        return ("Error: Provided path must be a string or bytes-like object.")
                
        