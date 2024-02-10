import random

INSTRUCTION = 'What is the result of the expression?'


def get_task_and_result():
    operator = random.choice('+-*')
    number1, number2 = random.randint(1, 10), random.randint(1, 10)
    if operator == '+':
        result = str(number1 + number2)
        expression = f'{number1} + {number2}'
    elif operator == '-':
        result = str(number1 - number2)
        expression = f'{number1} - {number2}'
    else:
        result = str(number1 * number2)
        expression = f'{number1} * {number2}'
    return expression, result
