def is_armstrong_number(number):
    array_of_numbers = str(number)
    sum_of_numbers = 0

    for item in array_of_numbers:
        sum_of_numbers += int(item) ** len(array_of_numbers)

    return sum_of_numbers == number

        
        