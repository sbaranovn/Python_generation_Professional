# INPUT DATA:

def same_parity(numbers):
    return [ el for el in numbers if el % 2 == numbers[0] % 2]

# TEST_1:
print(same_parity([]))

# TEST_2:
print(same_parity([6, 0, 67, -7, 10, -20]))

# TEST_3:
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))

# TEST_4:
print(same_parity([2]))

# TEST_5:
print(same_parity([2, 2, 2, 2, 3, 0, 2, 3]))

# TEST_6:
print(same_parity([-1, 1248234832443, 8]))

# TEST_7:
print(same_parity([1, 2, 4, 6, 8]))

# TEST_8:
print(same_parity([1, 3, 5, 7, 9]))

