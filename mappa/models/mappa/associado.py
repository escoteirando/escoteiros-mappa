from base_model.base_model import BaseModel
from datetime import datetime

FMT = '%a %b %d %Y %H:%M:%S'  # "Tue Mar 26 2013 00:00:00 GMT+0000 (UTC)"


class AssociadoModel(BaseModel):
    codigo: int
    nome: str
    codigoFoto: int
    codigoEquipe: int
    username: int
    numeroDigito: int
    dataNascimento: datetime
    dataValidade: datetime
    nomeAbreviado: str
    sexo: str
    codigoRamo: int
    codigoCategoria: int
    codigoSegundaCategoria: int
    codigoTerceiraCategoria: int
    linhaFormacao: str
    codigoRamoAdulto: int
    dataAcompanhamento: datetime

    def __init__(self, from_object: dict = None):
        if not from_object:
            super().__init__(from_object)
            return
        self.codigo = from_object.get('codigo')
        self.nome = from_object.get('nome')
        self.codigoFoto = from_object.get('codigoFoto')
        self.codigoEquipe = from_object.get('codigoEquipe')
        self.username = from_object.get('username')
        self.numeroDigito = from_object.get('numeroDigito')
        self.dataNascimento = str_todatetime(
            from_object.get('dataNascimento'))
        self.dataValidade = str_todatetime(from_object.get('dataValidade'))
        self.nomeAbreviado = from_object.get('nomeAbreviado')
        self.sexo = from_object.get('sexo')
        self.codigoRamo = from_object.get('codigoRamo')
        self.codigoCategoria = from_object.get('codigoCategoria')
        self.codigoSegundaCategoria = from_object.get('codigoSegundaCategoria')
        self.codigoTerceiraCategoria = from_object.get(
            'codigoTerceiraCategoria')
        self.linhaFormacao = from_object.get('linhaFormacao')
        self.codigoRamoAdulto = from_object.get('codigoRamoAdulto')
        self.dataAcompanhamento = str_todatetime(
            from_object.get('dataAcompanhamento'))


def str_todatetime(s: str) -> datetime:
    r = datetime.min
    if isinstance(s, str) and len(s) > 24:
        try:
            r = datetime.strptime(s[:24], FMT)
        except:
            ...

    return r
