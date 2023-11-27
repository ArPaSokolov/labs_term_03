import random

def generate_input_file(file_name, num_elements):
    with open(file_name, 'w') as file:
        numbers = [random.randint(1, 1000) for _ in range(num_elements)]
        numbers_str = ' '.join(map(str, numbers))
        file.write(numbers_str)

generate_input_file('input.txt', 1000)