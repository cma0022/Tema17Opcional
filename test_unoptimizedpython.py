from unoptimizedpython import optimizar_opcional

# Método para testear la introducción de n números aleatorios en un array
# En este caso le he indicado que introduzca 10 números y compruebo que el tamaño del array es de 10
def test_aleatorios_array():
    op = optimizar_opcional([])
    op.aleatorios_array(10)
    assert len(op.numbers) == 10

# Método para testear el cálculo del mayor, menor número, la suma total y la media de los números que forman el array
# Inicializo un objeto op introduciendole varios valores al array y comprobando su correcto funcionamiento
def test_calcular_maximo_minimo_total_media():
    op = optimizar_opcional([21, 4, -20, 72, -5, 102, 89, -1])
    maxi, mini, tot, med = op.calcular_maximo_minimo_total_media()
    assert maxi == 102 and mini == -20 and tot == 262 and med == 32.75

# Método para testear el cálculo del mayor, menor número, la suma total y la media de los números que forman el array
# En este caso, al crear un objeto op con el array vacío, debe devolver todos los valores 0
def test_calcular_maximo_minimo_total_media_array_vacio():
    op = optimizar_opcional([])
    maxi, mini, tot, med = op.calcular_maximo_minimo_total_media()
    assert maxi == 0 and mini == 0 and tot == 0 and med == 0

# Método para testear el funcionamiento de la impresión de 4 prints de todo el array, el mayor y menor número y la media
# Inicializo un objeto op introduciendole varios valores al array y comprobando su correcto funcionamiento
def test_imprimir_numeros():
    op = optimizar_opcional([1, 2, 3, 4, 5])
    assert op.imprimir_numeros() == f"Numbers:{op.numbers} Minimun number:1 Maximun number:5 Average number:3.0"
