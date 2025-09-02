# INPUT DATA:

def is_valid(string):
    return all([(4 <= len(string) <= 6),  (string.isdigit())]    )

# TEST_1:
print(is_valid('4367'))

# TEST_2:
print(is_valid('92134'))

# TEST_3:
print(is_valid('89abc1'))

# TEST_4:
print(is_valid('900876'))

# TEST_5:
print(is_valid('49 83'))

# TEST_6:
print(is_valid('467'))

# TEST_7:
print(is_valid('4323423424467'))

# TEST_8:
print(is_valid('3 7 0'))

# TEST_9:
print(is_valid('0000'))

# TEST_10:
print(is_valid(''))

# TEST_11:
print(is_valid('aaaa'))

