import logging

import uvicorn
from api import router as api_router
from core.config import settings
from create_fastapi_app import create_app

logging.basicConfig(
    format=settings.logging.log_format,
)
main_app = create_app(
    create_custom_static_urls=True,
)

main_app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=run.host,
        port=run.port,
        reload=True,
    )
