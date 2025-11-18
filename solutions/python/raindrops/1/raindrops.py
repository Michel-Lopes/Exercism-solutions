def convert(number):
    Result = ""

    if number % 3 == 0:
        Result += "Pling"
    if number % 5 == 0:
        Result += "Plang"
    if number % 7 == 0:
        Result += "Plong"

    return Result if Result else str(number)
