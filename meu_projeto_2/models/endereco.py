from models.enums.unidade_federativa import UnidadeFederativa

class Endereco:
    def __init__(self, local: str, numero: int, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.local = local
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return (f"{self.local}, {self.numero}, {self.complemento}, {self.cep} - {self.cidade}/{self.uf.value}")
