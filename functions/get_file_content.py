import os
from functions.config import MAX_CHARS
def get_file_content(working_directory: str, file_path: str) -> str:
    print(f"working directory: {working_directory}\n")
    print(f"file path: {file_path}\n")
    try:
        abs_path = os.path.abspath(working_directory)
        print(f"abs path: {abs_path}\n")
        target_file = os.path.normpath(os.path.join(abs_path,file_path))
        print(f"target_file: {target_file}\n")
        valid_target_path = os.path.commonpath([abs_path,target_file]) == abs_path
        print(f"valid target path? {valid_target_path}\n")
        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        print(f"is file? {os.path.isfile(target_file)}" )

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        #MAX_CHARS = 10000
        file_content_string = ""
        print(f"MAX CHARS: {MAX_CHARS}/n")
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)        
            if f.read(1):
                file_content_string+=f' [...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except FileNotFoundError:
            return (f"Error: The file at {file_path} could not be found.")
    except PermissionError:
            return ("Error: You do not have permissions to access this file.")
    except TypeError:
            return ("Error: Provided path must be a string or bytes-like object.")
        

