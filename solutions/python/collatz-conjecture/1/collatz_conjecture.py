def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    result = number
    number_of_steps = 0

    while result > 0:
        if result == 1:
            return number_of_steps
        if result % 2 == 0:
            result = result / 2
            number_of_steps += 1
        else:
            result = (result * 3) + 1
            number_of_steps += 1