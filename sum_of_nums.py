def sum(number, to_find):
    array = {}

    for i, value in enumerate(number):
        remaining = to_find - value

        if remaining in array:
            return [array[remaining], i]

        array[value] = i

    return []

list = [2, 7, 11, 15]
find_value = 9

print(sum(list, find_value))