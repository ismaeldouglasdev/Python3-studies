def teste(b):
    global c
    a = 8
    b += 4
    c = 2
    print(f'A (local) dentro vale {a}')
    print(f'B (local) dentro vale {b}')
    print(f'C (local) dentro vale {c}')


a = 5
c = 9
teste(a)

print(f'A (global) fora vale {a}')
print(f'C (global) fora vale {c}')

