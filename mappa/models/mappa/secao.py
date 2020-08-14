from base_model import BaseModel


class SecaoModel(BaseModel):
    codigo: int
    nome: str
    codigoTipoSecao: int
    codigoGrupo: int
    codigoRegiao: str

    @property
    def tipo_secao_str(self):
        if isinstance(self.codigoTipoSecao, int) and 0 < self.codigoTipoSecao < 5:
            return [
                'Alcatéia',
                'Tropa Escoteira',
                'Tropa Sênior',
                'Clã Pioneiro'
            ][self.codigoTipoSecao-1]

        return f"Seção inválida [{self.codigoTipoSecao}]"
