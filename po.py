# Pontuações manualmente usando range
pontuacoes = ''.join(chr(i) for i in range(33, 48)) + \
             ''.join(chr(i) for i in range(58, 65)) + \
             ''.join(chr(i) for i in range(91, 97)) + \
             ''.join(chr(i) for i in range(123, 127))

print("Pontuações:", pontuacoes)
