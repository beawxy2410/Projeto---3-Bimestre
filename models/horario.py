import json
from datetime import datetime
from typing import Union


# Modelo
class Horario:
    def __init__(self, id, data, confirmado, id_cliente, id_servico):
        self.__id = id
        self.__data = datetime.now()
        self.__confirmado = False
        self.__id_cliente = 0
        self.__id_servico = 0

        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(confirmado)
        self.set_id_cliente(id_cliente)
        self.set_id_servico(id_servico)

    def __str__(self):
        return f"{self.__id} - {self.__data}"

    def to_json(self):
        dic = {}
        dic["id"] = self.__id
        dic["data"] = self.__data.strftime("%d/%m/%Y %H:%M")
        dic["confirmado"] = self.__confirmado
        dic["id_cliente"] = self.__id_cliente
        dic["id_servico"] = self.__id_servico
        return dic

    def set_id(self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError("O ID não pode ser um número negativo.")

    def get_id(self):
        return self.__id

    def set_data(self, data):
        if data:
            self.__data = data
        else:
            raise ValueError("Determine a data.")

    def get_data(self):
        return self.__data

    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado

    def get_confirmado(self):
        return self.__confirmado

    def set_id_cliente(self, id_cliente):
        if id_cliente is None or id_cliente >= 0:
            self.__id_cliente = id_cliente
        else:
            raise ValueError("O ID não pode ser um número negativo.")
        self.__id_cliente = id_cliente

    def get_id_cliente(self):
        return self.__id_cliente

    def set_id_servico(self, id_servico):
        if id_servico is None or id_servico >= 0:
            self.__id_servico = id_servico
        else:
            raise ValueError("O ID não pode ser um número negativo.")
        self.__id_servico = id_servico

    def get_id_servico(self):
        return self.__id_servico


# Persistência
class Horarios:
    objetos = []

    @classmethod
    def inserir(cls, obj) -> None:
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.get_id() > m:
                m = c.get_id()
        obj.set_id(m + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[Horario]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_disponiveis(cls) -> list[Horario]:
        cls.abrir()
        horarios = []
        for horario in cls.objetos:
            if not horario.get_confirmado():
                horarios.append(horario)
        return horarios

    @classmethod
    def listar_confirmados(cls) -> list[Horario]:
        cls.abrir()
        horarios = []
        for horario in cls.objetos:
            if horario.get_confirmado():
                horarios.append(horario)
        return horarios

    @classmethod
    def listar_id(cls, id: int) -> Union[Horario, None]:
        cls.abrir()
        for obj in cls.objetos:
            if id == obj.get_id():
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: Horario) -> None:
        c = cls.listar_id(obj.get_id())
        if c is not None:
            c.set_confirmado(obj.get_confirmado())
            c.set_id_cliente(obj.get_id_cliente())
            c.set_id_servico(obj.get_id_servico())
        cls.salvar()

    @classmethod
    def excluir(cls, id: int) -> None:
        c = cls.listar_id(id)
        if c is not None:
            cls.objetos.remove(c)
        cls.salvar()

    @classmethod
    def salvar(cls) -> None:
        data = []
        for obj in cls.objetos:
            data.append(obj.to_json())
        with open("horarios.json", mode="w") as arquivo:
            json.dump(data, arquivo)

    @classmethod
    def abrir(cls) -> None:
        cls.objetos = []
        try:
            with open("horarios.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Horario(
                        obj["id"],
                        datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"),
                        obj["confirmado"],
                        obj["id_cliente"],
                        obj["id_servico"],
                    )
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
