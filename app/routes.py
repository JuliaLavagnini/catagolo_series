from typing import List
from fastapi import APIRouter, status, HTTPException
from app.schemas import CriarSerie, SerieResposta
from app.database import (
    buscar_por_titulo,
    inserir_serie,
    listar_todas_series,
    delete_serie_por_titulo,
)

router = APIRouter(prefix="/series", tags=["Series"])


# Rota GET /series para listar o catalogo completo
@router.get("", response_model=list[CriarSerie], status_code=status.HTTP_200_OK)
def listar_series():
    return listar_todas_series()


# Rota POST /series
@router.post("", response_model=SerieResposta, status_code=status.HTTP_201_CREATED)
def cadastrar_serie(nova_serie: CriarSerie):
    return inserir_serie(nova_serie.model_dump())


@router.get("/{titulo}", response_model=CriarSerie, status_code=status.HTTP_200_OK)
def obter_serie(titulo: str):
    # Busca exata
    serie = buscar_por_titulo(titulo)

    # Caso nao encontre e a URL tenha hifens, tenta substituir por espaco
    if not serie and "-" in titulo:
        serie = buscar_por_titulo(titulo.replace("-", " "))

    if not serie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Série não encontrada"
        )
    return serie


@router.delete("/{titulo}", status_code=status.HTTP_200_OK)
def deletar_serie(titulo: str):
    removida = delete_serie_por_titulo(titulo)

    if not removida:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Série não encontrada"
        )
    return {"mensagem": "Série '{titulo}' removida com sucesso!"}
