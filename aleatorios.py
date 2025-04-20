"""
Este fichero contiene dos implementaciones de generadores de numeros aleatorios. 
Estos se generan mediante el metodo LGC.
Se implementa este tipo de generadores en una clase y en una función.
"""

class Aleat:
    """
    Clase Aleat, que genera numeros aleatorios usando el metodo LGC

    >>> rand = Aleat(m= 32, a=9, c=13, x0=11)
    >>> for _ in rance(4):
    ...     print(next(rand))
    ...

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    """

    def __init__(self, *, m=2147483647, a=1103515245, c=12345, x0=1212121):
        """
        Inicializa el generador de numeros aleatorios
        """

        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __next__(self):
        """
        Genera y devuelve el siguiente numero de la secuencia
        """

        self.x = (self.a * self.x + self.c) % self.m
        return self.x
    
    def __call__(self, x0):
        """
        Reinicia la secuencia con la semilla x0 indicada
        """

        self.x = x0

if __name__ == "__main__":
    import doctest
    doctest.testmod()


def aleat(m=2147483647, a=1103515245, c=12345, x0=1212121):
    """
    Funcion generadora de numeros aleatorios mediante el metodo LGC

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...

    """

    x = x0
    while True:
        yield x
        x = (a * x + c) % m

        try:
            x = yield
        except GeneratorExit:
            break