from cmath import inf
import secrets

class optimizar_opcional:

    # Declaramos las variables
    numbers = []

    # Constructor con los parámetros
    def __init__(self, numbers) -> None:
        self.numbers = numbers

    # Método para introducir n números aleatorios al array
    def aleatorios_array(self, n) -> None:
        for _ in range(n):
            self.numbers.append(secrets.randbelow(100))

    # Método para calcular el num_max, el num_min, el total y la media de los números del array
    def calcular_maximo_minimo_total_media(self):
        total:int = 0
        max_number:int = -inf
        min_number:int = inf
        media:float = 0

        if len(self.numbers) == 0:
            max_number = 0
            min_number = 0
            media = 0
        else:    
            for i in self.numbers:
                total = total + i
                if i > max_number:
                    max_number = i
                if i < min_number:
                    min_number = i
            media = total / len(self.numbers)
        return (max_number, min_number, total, media)

    # Imprimir el array, el número mínimo, el número máximo y la media
    def imprimir_numeros(self) -> str:
        maxi, mini, tot, med = self.calcular_maximo_minimo_total_media()
        print("Numbers:", self.numbers)
        print("Minimum number:", mini)
        print("Maximum number:", maxi)
        print("Average number:", med)
        return f"Numbers:{self.numbers} Minimun number:{mini} Maximun number:{maxi} Average number:{med}"