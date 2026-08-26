import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_directory = os.path.normpath(os.path.join(abs_path,directory))
        valid_target_path = os.path.commonpath([abs_path,target_directory]) == abs_path
        if not valid_target_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'
        #print(f"target directory = {target_directory}\n")
        dir_items = os.listdir(target_directory)
        output_str = ""


        for item in dir_items:
        #    print(f"HEY! {item}\n")
            item_path = os.path.normpath(os.path.join(target_directory,item))
            item_size = os.path.getsize(item_path)
         #   print(f"file size = {item_size}\n")
            isdir = os.path.isdir(item_path)
          #  print(f"is directory? {isdir}")
            output_str+=f"- {item}: file_size={item_size} bytes, is_dir={isdir}\n"
        return output_str
            
    except FileNotFoundError:
        return (f"Error: The file at {target_directory} could not be found.")
    except PermissionError:
        return ("Error: You do not have permissions to access this file.")
    except TypeError:
        return ("Error: Provided path must be a string or bytes-like object.")
    




    


