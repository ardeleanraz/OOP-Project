def odd_num(number):
    numbers = []
    for num in number:
        if num % 2 == 1:
            numbers.append(2*num)
    return set(numbers)


print(odd_num([2,4,5,17]))
