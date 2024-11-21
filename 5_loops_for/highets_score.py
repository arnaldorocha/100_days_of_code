students_scores = [123,511,31,412,31,41]

soma = sum(students_scores)
print(soma)

maximo = max(students_scores)
minimo = min(students_scores)

print(f'Valor maior da lista {maximo}')
print(f'Valor menor da lista {minimo}')
print(f'Soma do valor maior e do menor {maximo + minimo}')

for score in students_scores:
    print(score)

max_score = 0

for socore in students_scores:
    if score > max_score:   # parou quando atingiu a condição que é o valor maior da lista
        max_score = score
        print(max_score)   

    

