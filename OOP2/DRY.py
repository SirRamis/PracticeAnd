'''
Если есть повторяющийся код или функционал, его нужно вынести в отдельную функцию,
 класс или модуль, чтобы избежать дублирования и упростить обслуживание кода.
'''

def print_basic_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

def print_user_info(name, age):
    print_basic_info(name, age)

def print_employee_info(name, age, position):
    print_basic_info(name, age)
    print(f"Position: {position}")

print_user_info("Alice", 25)
print_employee_info("Bob", 30, "Manager")
