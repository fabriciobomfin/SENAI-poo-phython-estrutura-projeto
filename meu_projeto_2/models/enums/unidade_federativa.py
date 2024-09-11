from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    SÃO_PAULO = ("São Paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")
   
    #definindo sigla:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla

'''# Exemplo de uso:
for estado in UnidadeFederativa:
    print(f"Estado: {estado.nome}, Sigla: {estado.sigla}")'''
