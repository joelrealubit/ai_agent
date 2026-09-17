from functions.run_python_file import run_python_file
run_python_file("calculator", "main.py")
print(f'{run_python_file("calculator", "main.py")}\n')
print(f'{run_python_file("calculator", "main.py",["3 + 5"])}\n')
print(f'{run_python_file("calculator", "tests.py")}\n')
print(f'{run_python_file("calculator", "../main.py")}\n')
print(f'{run_python_file("calculator", "nonexistent.py")}\n')
print(f'{run_python_file("calculator", "lorem.txt")}\n')

