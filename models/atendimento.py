import json
from datetime import datetime
from typing import Union
from crud import CRUDGeral

class Atendimento:
    def __init__(self, id, id_paciente, id_medico):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def id_paciente(self):
        return self._id_paciente

    @id_paciente.setter
    def id_paciente(self, value: int):
        self._id_paciente = value

    @property
    def id_medico(self):
        return self._id_medico

    @id_medico.setter
    def id_medico(self, value: int):
        self._id_medico = value

    def __str__(self):
        return f"{self.id} - Paciente: {self.id_paciente}, Médico: {self.id_medico}"


class Atendimentos_CRUD(CRUDGeral):
    nome_arquivo = "atendimentos"

    @classmethod
    def to_dict(cls, obj: Atendimento) -> dict:
        return {
            "id": obj.id,
            "id_paciente": obj.id_paciente,
            "id_medico": obj.id_medico,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Atendimento:
        return Atendimento(
            data["id"],
            data["id_paciente"],
            data["id_medico"],
        )