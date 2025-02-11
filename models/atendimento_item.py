from crud import CRUDGeral

class AtendimentoItem:
    def __init__(self, id, id_atendimento, id_procedimento):
        self.id = id
        self.id_atendimento = id_atendimento
        self.id_procedimento = id_procedimento

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def id_atendimento(self):
        return self._id_atendimento

    @id_atendimento.setter
    def id_atendimento(self, value: int):
        self._id_atendimento = value

    @property
    def id_procedimento(self):
        return self._id_procedimento

    @id_procedimento.setter
    def id_procedimento(self, value: int):
        self._id_procedimento = value

    def __str__(self):
        return f"{self.id} - Atendimento: {self.id_atendimento}, Procedimento: {self.id_procedimento}"


class AtendimentoItens_CRUD(CRUDGeral):
    nome_arquivo = "atendimento_itens"

    @classmethod
    def to_dict(cls, obj: AtendimentoItem) -> dict:
        return {
            "id": obj.id,
            "id_atendimento": obj.id_atendimento,
            "id_procedimento": obj.id_procedimento,
        }

    @classmethod
    def from_dict(cls, data: dict) -> AtendimentoItem:
        return AtendimentoItem(
            data["id"],
            data["id_atendimento"],
            data["id_procedimento"],
        )


if __name__ == "__main__":
    # Criando alguns itens de atendimentos
    item1 = AtendimentoItem(None, 1, 101)
    item2 = AtendimentoItem(None, 1, 102)
    item3 = AtendimentoItem(None, 2, 103)

    # Inserindo os itens de atendimentos
    AtendimentoItens_CRUD.inserir(item1)
    AtendimentoItens_CRUD.inserir(item2)
    AtendimentoItens_CRUD.inserir(item3)

    # Listando todos os itens de atendimentos
    print("Lista de itens de atendimento:")
    for item in AtendimentoItens_CRUD.listar():
        print(item)

    # Atualizando um item de um atendimento 
    item1.id_procedimento = 105
    AtendimentoItens_CRUD.atualizar(item1)

    # Listando itens dos atendimentos após atualização
    print("\nLista de itens de atendimento após atualização:")
    for item in AtendimentoItens_CRUD.listar():
        print(item)

    # Excluindo um item de um atendimento
    AtendimentoItens_CRUD.excluir(item2.id)

    # Listando itens de atendimento após exclusão
    print("\nLista de itens de atendimento após exclusão:")
    for item in AtendimentoItens_CRUD.listar():
        print(item)

