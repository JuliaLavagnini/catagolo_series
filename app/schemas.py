from pydantic import BaseModel, Field

class CriarSerie(BaseModel):
    titulo: str = Field(..., min_length=1, description="Título da série")
    genero: str = Field(..., min_length=1, description="Gênero da série")
    ano_lancamento: int = Field(..., gt=1900, description="Ano de lançamento (maior que 1900)")
    temporadas: int = Field(..., gt=0, description="Número de temporadas da série")

    def SerieResposta(BaseModel):
        mensagem: str
        serie: CriarSerie