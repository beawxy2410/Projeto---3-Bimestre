# Lista de Clientes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json
from typing import Union


# Modelo
class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.__id = 0
        self.__nome = ""
        self.__email = ""
        self.__fone = ""
        self.__senha = ""

        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def __str__(self):
        return f"{self.__nome} - {self.__email} - {self.__fone}"

    def set_id(self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError("O ID não pode ser um número negativo.")

    def get_id(self):
        return self.__id

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            raise ValueError("Nome não pode ser vazio.")

    def get_nome(self):
        return self.__nome

    def set_email(self, email):
        if email != "":
            self.__email = email.lower()
        else:
            raise ValueError("O e-mail não pode ser vazio.")

    def get_email(self):
        return self.__email

    def set_fone(self, fone):
        if fone != "":
            self.__fone = fone
        else:
            raise ValueError("Fone não pode ser vazio.")

    def get_fone(self):
        return self.__fone

    def set_senha(self, senha):
        if senha != "":
            self.__senha = senha
        else:
            raise ValueError("O e-mail não pode ser vazio.")

    def get_senha(self):
        return self.__senha


# Persistência
class Clientes:
    objetos: list[Cliente] = []

    @classmethod
    def inserir(cls, obj: Cliente) -> None:
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.get_id() > m:
                m = c.get_id()
        obj.set_id(m + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[Cliente]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int) -> Union[Cliente, None]:
        cls.abrir()
        for obj in cls.objetos:
            if id == obj.get_id():
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: Cliente) -> None:
        c = cls.listar_id(obj.get_id())
        if c is not None:
            c.set_nome(obj.get_nome())
            c.set_email(obj.get_email())
            c.set_fone(obj.get_fone())
            c.set_senha(obj.get_senha())
        cls.salvar()

    @classmethod
    def excluir(cls, id: int) -> None:
        c = cls.listar_id(id)
        if c is not None:
            cls.objetos.remove(c)
        cls.salvar()

    @classmethod
    def abrir(cls) -> None:
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Cliente(
                        obj["id"],
                        obj["nome"],
                        obj["email"],
                        obj["fone"],
                        obj["senha"],
                    )
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls) -> None:
        data = []
        for obj in cls.objetos:
            data.append(
                {
                    "id": obj.get_id(),
                    "nome": obj.get_nome(),
                    "email": obj.get_email(),
                    "fone": obj.get_fone(),
                    "senha": obj.get_senha(),
                }
            )
        with open("clientes.json", mode="w") as arquivo:
            json.dump(data, arquivo)
