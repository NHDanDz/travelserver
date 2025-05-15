from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from apps.api import address, chat, index, prompt, chat_pri
from apps.api.user import user
from apps.base.exceptions import global_exception_handlers
from apps.base.conf import conf
from apps.base.middleware import register_middleware

def create_app():
    app = FastAPI(
        title=conf.title,
        description=conf.description,
        version=conf.VERSION,
        docs_url=conf.DOCS_URL,
        redoc_url=conf.REDOC_URL,
        openapi_url=conf.OPENAPI_URL
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_middleware(app)

    # Mount exception handlers
    for exc, handler in global_exception_handlers.items():
        app.add_exception_handler(exc, handler)

    # Mount static files
    app.mount("/static", StaticFiles(directory="apps/static"), name="static")

    # API routes
    app.include_router(user.route, prefix="/api/v1/user", tags=["User"])
    app.include_router(address.route, prefix="/api/v1/address", tags=["Address"])
    app.include_router(chat.route, prefix="/api/v1/chat", tags=["Chat"])
    app.include_router(prompt.route, prefix="/api/v1/chat/prompt", tags=["Prompt"])
    app.include_router(chat_pri.route, prefix="/api/v1/chat", tags=["Chat-Pri"])
    app.include_router(index.route, tags=["Index"])

    @app.get("/favicon.ico", include_in_schema=False)
    async def favicon():
        return FileResponse("apps/static/favicon.ico")

    return app