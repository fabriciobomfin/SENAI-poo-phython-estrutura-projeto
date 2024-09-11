
from models.enums.unidade_federativa import UnidadeFederativa


class Endereco:
    def __init__(self, local: str, numero: int, complemento: str, cep: int, cidade: str, uf: UnidadeFederativa) -> None:
        self.local = local
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
        