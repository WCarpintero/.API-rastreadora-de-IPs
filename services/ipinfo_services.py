import requests
from fastapi import HTTPException
from core.config import settings

def obtener_info_ip(ip: str):
    url = f"https://ipinfo.io/{ip}"
    params = {
        "token": settings.IPINFO_TOKEN
    }

    try:
        response = requests.get(url, params=params, timeout=5)
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=503,
            detail="No se pudo conectar con la API externa"
        )

    if response.status_code == 400:
        raise HTTPException(400, "Petición inválida a la API externa")

    if response.status_code == 401:
        raise HTTPException(401, "Token de autenticación inválido o ausente")

    if response.status_code == 403:
        raise HTTPException(403, "Acceso prohibido a la API externa")

    if response.status_code == 404:
        raise HTTPException(404, "Información no encontrada para la IP solicitada")

    if response.status_code == 429:
        raise HTTPException(429, "Se excedió el límite de peticiones a la API externa")

    if response.status_code >= 500:
        raise HTTPException(502, "Error interno en la API externa")

    data = response.json()

    if "ip" not in data:
        raise HTTPException(
            status_code=502,
            detail="Respuesta inválida desde la API externa"
        )

    return {
        "ip": data.get("ip"),
        "ciudad": data.get("city"),
        "region": data.get("region"),
        "pais": data.get("country"),
        "ubicacion": data.get("loc"),
        "proveedor": data.get("org")
    }
