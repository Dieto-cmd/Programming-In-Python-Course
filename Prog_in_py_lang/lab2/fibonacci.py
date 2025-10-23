class Fibonacci:
    def __init__(self, steps):
        self.steps = steps  # ile liczb generować
        self.index = 0      # aktualna pozycja w iteracji
        self.a = 0          # pierwsza liczba Fibonacciego
        self.b = 1          # druga liczba Fibonacciego

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.steps:
            raise StopIteration  # koniec iteracji
        if self.index == 0:
            self.index += 1
            return self.a
        elif self.index == 1:
            self.index += 1
            return self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            self.index += 1
            return self.b

# Przykład użycia:
fib = Fibonacci(10)
for num in fib:
    print(num)
