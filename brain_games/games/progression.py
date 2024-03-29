import random

INSTRUCTION = 'What number is missing in the progression?'


def get_task_and_result():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    num_of_elements = random.randint(5, 10)
    progression = list(range(start, start + step * num_of_elements, step))
    index = random.randint(0, len(progression) - 1)
    result = str(progression[index])
    progression[index] = '..'
    progression = ' '.join(list(map(str, progression)))
    return progression, result
