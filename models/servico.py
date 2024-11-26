import json
from typing import Union

# Modelo
class Servico:
    def __init__(self, id, descricao, valor, duracao):
      self.__id = 0
      self.__descricao = ""
      self.__valor = 0
      self.__duracao = 0

      self.set_id(id)
      self.set_descricao(descricao)
      self.set_valor(valor)
      self.set_duracao(duracao)


    def __str__(self):
      return f"ID: {self.__id} Descrição: {self.__descricao} Valor: {self.__valor} Duração: {self.__duracao}"

    def set_id(self, id):
      if id >= 0:
        self.__id = id
      else:
        raise ValueError("O ID não pode ser um número negativo.")

    def get_id(self):
      return self.__id

    def set_descricao(self, descricao):
      if descricao != "":
        self.__descricao = descricao
      else:
        raise ValueError("A descrição não pode ser vazio.")

    def get_descricao(self):
      return self.__descricao

    def set_valor(self, valor):
      if valor > 0:
        self.__valor = valor
      else:
        raise ValueError("O valor não pode ser um número negativo.")

    def get_valor(self):
      return self.__valor

    def set_duracao(self, duracao):
      if duracao > 0:
        self.__duracao = duracao
      else:
        raise ValueError("A duração não pode ser negativa.")

    def get_duracao(self):
      return self.__duracao


# Persistência
class Servicos:
    objetos: list[Servico] = []

    @classmethod
    def inserir(cls, obj: Servico) -> None:
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.get_id() > m:
                m = c.get_id()
        obj.set_id(m + 1)

        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[Servico]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int) -> Union[Servico, None]:
        cls.abrir()
        for obj in cls.objetos:
            if id == obj.get_id():
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: Servico) -> None:
        c = cls.listar_id(obj.get_id())
        if c is not None:
            c.set_descricao(obj.get_descricao())
            c.set_valor(obj.get_valor())
            c.set_duracao(obj.get_duracao())
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
            with open("servicos.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Servico(
                        obj["id"],
                        obj["descricao"],
                        obj["valor"],
                        obj["duracao"],
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
                    "descricao": obj.get_descricao(),
                    "valor": obj.get_valor(),
                    "duracao": obj.get_duracao(),
                }
            )
        with open("servicos.json", mode="w") as arquivo:
            json.dump(data, arquivo)  