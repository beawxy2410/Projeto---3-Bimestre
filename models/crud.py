import json
from abc import ABC, abstractmethod


class CRUDGeral(ABC):
    objetos: list = []  
    nome_arquivo: str = "dados"  

    @classmethod
    def salvar(cls) -> None:
        dados: list[dict] = []
        for obj in cls.objetos:
            dados.append(cls.to_dict(obj))  
        with open(f"{cls.nome_arquivo}.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

    @classmethod
    def abrir(cls) -> None:
        try:
            with open(f"{cls.nome_arquivo}.json", "r") as arquivo:
                dados = json.load(arquivo)
            cls.limpar()
            for obj in dados:
                cls.objetos.append(cls.from_dict(obj))
        except FileNotFoundError:
            pass

    @classmethod
    def limpar(cls) -> None:
        cls.objetos = []

    @classmethod
    def inserir(cls, obj) -> None:
        if obj.id is None:
            ids = [0]

            for o in cls.objetos:
                ids.append(o.id)

            obj.id = max(ids) + 1

        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list:
        return cls.objetos


    @classmethod 
    def listar_id(cls, id_obj: int):
        for o in cls.objetos:
            if o.id == id_obj:
                return cls.objetos
                

    @classmethod
    def atualizar(cls, obj) -> None:
        for o in cls.objetos:
            if o.id == obj.id:

                cls.objetos[cls.objetos.index(o)] = obj
                break
            
        cls.salvar()  

    @classmethod
    def excluir(cls, id_obj: int) -> None:
        for o in cls.objetos:
            if o.id == id_obj:
                del cls.objetos[cls.objetos.index(o)]
                break
        cls.salvar()

    @classmethod
    @abstractmethod
    def to_dict(cls, obj) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, dados: dict):
        pass

