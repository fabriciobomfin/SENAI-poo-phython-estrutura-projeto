import pytest
from ..models.pessoa import Pessoa #caminho retativo
from meu_projeto.models.endereco import Endereco #caminho absoluto
from models.enums.sexo import Sexo
from models.enums.unidade_federativa import UnidadeFederativa

#modelo
@pytest.fixture
def criar_pessoa():
    pessoa_1 = Pessoa("Marta",22,Sexo.FEMININO,Endereco("RUA A.", 35, UnidadeFederativa.BAHIA))

    return pessoa_1

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Marta"
    
    
    
def test_pessoa_atributo_idade(criar_pessoa):
    assert criar_pessoa.idade == 22