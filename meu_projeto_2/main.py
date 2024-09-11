import os

from models.enums.unidade_federativa import UnidadeFederativa
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco

# Limpar tela do console
os.system("cls" if os.name == "nt" else "clear")

# Instanciando Classes
pessoa_1 = Pessoa(
    "Morgana Santos",  # Nome adequado
    666,  # ID ou outro parâmetro (verificar no modelo)
    Sexo.FLUIDO,  # Valor do enum Sexo
    Endereco(
        "Rua das Flores", 69, "Bairro do Centro", 40028922, "Xique-Xique", UnidadeFederativa.RIO_DE_JANEIRO
    )  # Endereço completo
)

print(pessoa_1)
