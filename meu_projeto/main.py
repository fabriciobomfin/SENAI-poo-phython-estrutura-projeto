import os

from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco

os.system ("cls || clear")

# Instanciando Classes.
pessoa_1 = Pessoa("Morgana cheira pó", 666, Sexo.NEUTRO,Endereco("Macumbeira.", 69))

print(pessoa_1)