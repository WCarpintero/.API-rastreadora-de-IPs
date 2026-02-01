# IP Information API – Documentación del Contrato de API

## Descripción General

### ¿Qué hace la API?
Esta aplicación consume la API pública de **IPInfo (ipinfo.io)** para obtener información detallada asociada a una dirección IP.
La aplicación funciona como un **servicio intermediario** que encapsula, valida y estructura los datos recibidos desde la API externa.

### ¿Qué información devuelve?
- Dirección IP consultada
- Ciudad
- Región o estado
- País (código ISO)
- Organización / proveedor de red (ISP / ASN)
- Coordenadas geográficas aproximadas
- Zona horaria (si está disponible)

### ¿Para qué sirve?
- Analizar el origen geográfico de una IP
- Obtener información básica de localización
- Integrar datos de IPs en aplicaciones backend
- Aplicar buenas prácticas en el consumo de APIs externas

---

## Endpoints Utilizados (API Externa)

La aplicación utiliza el siguiente endpoint oficial de **IPInfo**:

### 1. IP Details API

| Campo | Descripción |
|------|------------|
| URL del endpoint | https://ipinfo.io/{ip} |
| Método HTTP | GET |
| Documentación oficial | https://ipinfo.io/developers |

### Parámetros Requeridos

| Parámetro | Tipo | Requerido | Descripción |
|----------|------|-----------|-------------|
| ip | string | ✅ Sí | Dirección IP a consultar (IPv4 o IPv6) |
| token | string | ✅ Sí | Token de autenticación de IPInfo |

### Ejemplo de Petición

```http
GET https://ipinfo.io/8.8.8.8?token=TU_API_TOKEN
```

### Ejemplo de Respuesta Exitosa (JSON)

```json
{
  "ip": "8.8.8.8",
  "city": "Mountain View",
  "region": "California",
  "country": "US",
  "loc": "37.4056,-122.0775",
  "org": "AS15169 Google LLC",
  "timezone": "America/Los_Angeles"
}
```

### Descripción de Campos

| Campo | Tipo | Descripción |
|------|------|-------------|
| ip | string | Dirección IP consultada |
| city | string | Ciudad asociada a la IP |
| region | string | Región o estado |
| country | string | Código de país ISO 3166 |
| loc | string | Coordenadas geográficas (latitud,longitud) |
| org | string | Organización o proveedor de red |
| timezone | string | Zona horaria aproximada |

---

## Manejo de Errores

### Códigos de Error Posibles

| Código HTTP | Significado | Causa Común |
|------------|------------|-------------|
| 400 | Bad Request | IP inválida o mal formada |
| 401 | Unauthorized | Token inválido o no enviado |
| 403 | Forbidden | Acceso denegado |
| 404 | Not Found | IP no encontrada |
| 429 | Too Many Requests | Límite de peticiones excedido |
| 500 | Internal Server Error | Error interno del servicio |
| 503 | Service Unavailable | Servicio no disponible |

### Ejemplo de Error – IP inválida

```json
{
  "detail": "La IP proporcionada no es válida."
}
```

### Ejemplo de Error – Token inválido

```json
{
  "detail": "Token de IPInfo inválido o no autorizado."
}
```

### Ejemplo de Error – Límite de peticiones

```json
{
  "detail": "Límite de peticiones excedido. Intente más tarde."
}
```

---

## Endpoint de la Aplicación Local

### Obtener Información de una IP

| Campo | Descripción |
|------|------------|
| URL | http://localhost:8000/ip/{ip} |
| Método HTTP | GET |

### Ejemplo de Petición

```http
GET http://localhost:8000/ip/8.8.8.8
```

### Ejemplo de Respuesta Exitosa

```json
{
  "ip": "8.8.8.8",
  "ciudad": "Mountain View",
  "region": "California",
  "pais": "US",
  "proveedor": "AS15169 Google LLC",
  "ubicacion": "37.4056,-122.0775"
}
```

### Campos de Respuesta

| Campo | Tipo | Descripción |
|------|------|-------------|
| ip | string | Dirección IP consultada |
| ciudad | string | Ciudad |
| region | string | Región |
| pais | string | Código del país |
| proveedor | string | Organización / ISP |
| ubicacion | string | Coordenadas geográficas |

---

## Configuración Requerida

### Variables de Entorno (.env)

```env
IPINFO_TOKEN=tu_api_token_aqui
```

### Obtener API Token
1. Registrarse en https://ipinfo.io
2. Acceder al Dashboard
3. Generar un API Token
4. Configurarlo en el archivo `.env`

---

## Recursos Adicionales

- Documentación oficial: https://ipinfo.io/developers
- Planes y límites: https://ipinfo.io/pricing
- Ejemplos de respuestas: https://ipinfo.io/developers/responses

---

## 👤 Autor

**Nombre:** Wil Carpintero  
**Fecha:** Enero 2026
