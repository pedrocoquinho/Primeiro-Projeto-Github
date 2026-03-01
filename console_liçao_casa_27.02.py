
class Console():
    def __init__(self, marca, cor, modelo):
      self.marca = marca
      self.cor = cor
      self.modelo = modelo
    def acelerar(self):
       return f"o console da {self.marca} é um {self.modelo} e é {self.cor}"
    
console1 = Console("xbox","preto","xbox one")

console2 = Console("playstation","branco", "ps5")

console3 = Console("nintendo","vermelho","switch")
print(console1.acelerar())

print(console2.acelerar())

print(console3.acelerar())