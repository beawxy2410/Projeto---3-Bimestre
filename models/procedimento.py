from crud import CRUDGeral

class Procedimento:
    def __init__(self, id, descricao, valor):
        self.id = id
        self.descricao = descricao
        self.valor = valor

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value: str):
        if value:
            self._descricao = value
        else:
            raise ValueError("Informe a descrição do procedimento")

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value: float):
        if value >= 0:
            self._valor = value
        else:
            raise ValueError("O valor deve ser positivo")

    def __str__(self):
        return f"{self.id} - {self.descricao} - R${self.valor:.2f}"


class Procedimentos_CRUD(CRUDGeral):
    nome_arquivo = "procedimentos"

    @classmethod
    def to_dict(cls, obj: Procedimento) -> dict:
        return {
            "id": obj.id,
            "descricao": obj.descricao,
            "valor": obj.valor,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Procedimento:
        return Procedimento(
            data["id"],
            data["descricao"],
            data["valor"],
        )
    

