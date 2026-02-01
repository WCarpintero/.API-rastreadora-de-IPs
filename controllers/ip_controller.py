from fastapi import APIRouter, HTTPException
import ipaddress
from services.ipinfo_services import obtener_info_ip as service_obtener_info_ip

router = APIRouter(
    prefix = "/ip",
    tags = ["IP Info"]
)

@router.get("/")
def obtener_info_ip(ip: str):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="La IP proporcionada no es válida"
        )

    return service_obtener_info_ip(ip)