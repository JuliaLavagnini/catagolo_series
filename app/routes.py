from sys import prefix
from fastapi import APIRouter, status
from app.schemas import CriarSerie, SerieResposta
from app.database import carregar_series, salvar_series

router = APIRouter(prefix="/series", tags=["Series"])

# Rota GET /series para listar o catalogo completo
@router.get("", response_model=list[CriarSerie], status_code=status.HTTP_200_OK)
def listar_series():
    catalogo = carregar_series()
    return catalogo

# Rota POST /series
@router.post("", response_model=SerieResposta, status_code=status.HTTP_201_CREATED)
def cadastrar_serie(nova_serie: CriarSerie):
    catalogo = carregar_series()
    serie_dict = nova_serie.model_dump()
    catalogo.append(serie_dict)
    salvar_series(catalogo)
    return {"mensagem": "Série cadastrada com sucesso!", "serie": serie_dict}
