from typing import List

from base_model import BaseModel

from mappa.models.mappa.associado import AssociadoModel


class SubSecaoModel(BaseModel):

    codigo: int
    nome: str
    codigoSecao: int
    codigoLider: int
    codigoViceLider: int
    associados: List[AssociadoModel]
