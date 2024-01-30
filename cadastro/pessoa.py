from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, name):
        self._nome = name

    @classmethod
    def cadastrar_pessoa(cls, nome, idade):
        return cls(nome, idade)


    @abstractmethod
    def hello(self):pass


class Aluno(Pessoa):
    def hello(self):
        return f'Sou o Aluno {self._nome} e tenho {self._idade}'
    

class Professor(Pessoa):
    def hello(self):
        return f'Sou o Professor {self._nome} e tenho {self._idade}'
    

    

if __name__ == '__main__':
    a = Aluno('Luis', 20)

    p = Professor.cadastrar_pessoa('Diogenis', 30)

    print(a.hello())
    print(p.hello())