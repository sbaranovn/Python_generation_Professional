# INPUT DATA:

def hide_card(card):
    card = card.replace(' ', '')
    
    return '*' * 8 + card[-4:]
# TEST_1:
card = '1234567890123456'

print(hide_card(card))

# TEST_2:
card = '3456 9012 5678 1234'

print(hide_card(card))

# TEST_3:
card = '905 678123 45612 56'

print(hide_card(card))

# TEST_4:
card = '7 3 9 1 4 0 5 6 5 2 7 8 9 4 3 4'
print(hide_card(card))

# TEST_5:
card = '  103 43948 19446 323  '
print(hide_card(card))

# TEST_6:
print(hide_card('1034 3948 1944 6327'))

