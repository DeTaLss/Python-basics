class ComplexNumber:

    def __init__(self, real, unreal):
        self.real = real
        self.unreal = unreal

    def __add__(self, other):
        return f"{self.real + other.real} + {(self.unreal + self.unreal)}"

    def __mul__(self, other):
        return f"{self.real * other.real - self.unreal * other.unreal} " \
               f" + {self.real * other.unreal + other.real * self.unreal}"


a1 = int(input("Введите 'a1' число: "))
a2 = int(input("Введите 'a2' число: "))
a = ComplexNumber(a1, a2)

b1 = int(input("Введите 'b1' число: "))
b2 = int(input("Введите 'b2' число: "))
b = ComplexNumber(b1, b2)

print(f"a + b = {a + b}")
print(f"a * b = {a * b}")
