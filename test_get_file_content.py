from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print(f"lorem text: {result}")

print(f'{get_file_content("calculator", "main.py")}\n')
print(f'{get_file_content("calculator", "pkg/calculator.py")}\n')
print(f'{get_file_content("calculator", "/bin/cat")}\n') 
print(f'{get_file_content("calculator", "pkg/does_not_exist.py")}\n') 