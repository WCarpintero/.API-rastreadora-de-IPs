from fastapi import FastAPI
from controllers.ip_controller import router as ip_router

app = FastAPI(
    title = "IP Tracker API",
    description = "API que consume ipinfo.io para rastrear informaciòn de IPs",
    versiom = "1.0.0"
)

app.include_router(ip_router)