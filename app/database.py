"""JSON file reading/writing logic"""

import json
import os
from fastapi import HTTPException, status

ARQUIVO_DADOS = "series.json"


def carregar_series():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, IOError):
        return []


def salvar_series(series: list) -> None:
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(series, arquivo, indent=4, ensure_ascii=False)
    except IOError as erro:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao salvar dados no arquivo: {str(erro)}",
        )
