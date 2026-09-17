import os
import subprocess

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
            return f'Error: "{file_path}" does not exist or is not a regular file'
        root, extension = os.path.splitext(file_path)
        if not extension == '.py':
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        command.extend(args)
        completed_proc = subprocess.run(command, capture_output=True, text=True, timeout=30000)
        ret_str =""
        if completed_proc.returncode != 0:
            ret_str+=f"Process Exited with code {completed_proc.returncode}\n"
        if completed_proc.stdout == None and completed_proc.stderr == None:
            retstr+=f"No output produced\n"
        ret_str+=f"STDOUT: {completed_proc.stdout}\n"
        ret_str+=f"STDERR: {completed_proc.stderr}\n"
        return ret_str

        
    except FileNotFoundError:
        return (f"Error: The file at {file_path} could not be found.")
    except PermissionError:
        return ("Error: You do not have permissions to access this file.")
    except TypeError:
        return ("Error: Provided path must be a string or bytes-like object.")
    except Exception as e:
        return f"Error: executing Python file: {e}"
                
        