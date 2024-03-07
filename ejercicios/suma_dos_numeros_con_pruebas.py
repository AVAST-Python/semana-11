
def suma(a,b):
    return a+b


nombre = "suma de positivos"
res = suma(1,2)
expected = 3

if(res != expected):
    print(f'Test {nombre} fallido')

nombre = "suma con cero"
res = suma(0,2)
expected = 2

if(res != expected):
    print(f'Test {nombre} fallido')


nombre = "suma negativo y positivo"
res = suma(-1,2)
expected = 1

if(res != expected):
    print(f'Test {nombre} fallido')


nombre = "suma de negativos"
res = suma(-1,-2)
expected = -3

if(res != expected):
    print(f'Test {nombre} fallido')
