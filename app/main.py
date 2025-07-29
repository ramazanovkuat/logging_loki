from fastapi import FastAPI
from .config import logger

app = FastAPI(title="Toy Logger Demo")

@app.get("/ping")
async def ping():
    logger.info("pong requested", extra={"endpoint": "/ping"})
    return {"msg": "pong"}

@app.get("/error")
async def error():
    try:
        1 / 0
    except ZeroDivisionError as exc:
        logger.error("division by zero!", exc_info=exc)
        return {"error": "division by zero"}
