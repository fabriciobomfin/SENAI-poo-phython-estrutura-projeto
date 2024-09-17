import os
os.system("cls" if os.name == "nt" else "clear")
# Executando o comando 'pytest' para iniciar os testes.
if __name__ == "__main__":
    os.system("pytest")









'''import os

from models.enums.unidade_federativa import UnidadeFederativa
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco

# Limpar tela do console
os.system("cls" if os.name == "nt" else "clear")

# Instanciando Classes
pessoa_1 = Pessoa(
    nome = "Morgana Santos",  # Nome adequado
    idade = 30,  # Idade ou outro parâmetro apropriado
    sexo = Sexo.NEUTRO,  
    
    endereco=Endereco(
        local = "Rua das Flores", 
        numero = 69, 
        complemento = "Bairro do Centro", 
        cep = "40028-922",  # CEP como string
        cidade = "Xique-Xique", 
        uf = UnidadeFederativa.BAHIA
    )  # Endereço completo
)

print(pessoa_1)


'''