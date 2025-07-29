# Toy Logger Demo

Небольшое FastAPI‑приложение, показывающее централизованный сбор
структурированных логов в стек Fluent Bit → Loki → Grafana.

## Запуск

```bash
# собрать и запустить всё
docker compose up --build -d

# проверить API
curl http://localhost:8000/ping
curl http://localhost:8000/error
