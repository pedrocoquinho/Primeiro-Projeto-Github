# Classe base
class Veiculo:
    def __init__(self, modelo: str, ano: int, preco: float):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self) -> float:
        return self.preco * 0.10

    def __str__(self):
        return f"{self.modelo} ({self.ano}) - R$ {self.preco:,.2f}"


# Subclasse Carro
class Carro(Veiculo):
    def __init__(self, modelo: str, ano: int, preco: float, marca: str):
        super().__init__(modelo, ano, preco)
        self.marca = marca

    def desconto(self) -> float:
        return self.preco * 0.05

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - R$ {self.preco:,.2f}"


# Subclasse Moto
class Moto(Veiculo):
    def __init__(self, modelo: str, ano: int, preco: float, cilindrada: int):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self) -> float:  # Override do método da classe base
        return self.preco * 0.05

    def __str__(self):
        return f"{self.modelo} {self.cilindrada}cc ({self.ano}) - R$ {self.preco:,.2f}"


# ──────────────────────────────────────────
# Instâncias
# ──────────────────────────────────────────
carro = Carro(modelo="Civic", ano=2023, preco=150_000.00, marca="Honda")
moto  = Moto(modelo="CB 500", ano=2022, preco=35_000.00, cilindrada=500)

# ──────────────────────────────────────────
# Resultados
# ──────────────────────────────────────────
print("=" * 45)
print(f"  Veículo : {carro}")
print(f"  Imposto : R$ {carro.calcular_imposto():,.2f}  (10%)")
print(f"  Desconto: R$ {carro.desconto():,.2f}   (5%)")
print("=" * 45)
print(f"  Veículo : {moto}")
print(f"  Imposto : R$ {moto.calcular_imposto():,.2f}    (5%)")
print("=" * 45)