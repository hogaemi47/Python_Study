# Concatenation
x = 'Sam'
last_letters = x[1:]
concatentated_letters = 'P' + last_letters

print(concatentated_letters)

# String copying not using for
y = 'Hun is God '
god_word = y[7:]
loop_sentence = y + (god_word * 10)

print(loop_sentence)

# Using method
z = 'hun is god, '
w = 'ho is stupid '

hun_god = z.upper()
ho_stupid = w.upper()

result = hun_god + ho_stupid
result_1 = result.split()

print(result)
print(result_1)