from fastapi import FastAPI
from app.util.class_object import singleton
from app.api.staging.routes import routers as staging_routers

app = FastAPI()

# @app.get("/")
# def root():
#     return "Hello, FastAPI!"

class Config:
    API = "api"
    PROJECT_NAME: str = "FastAPI Lab"
    STAGING = "/api/staging"

configs = Config()

@singleton
class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title=configs.PROJECT_NAME,
            openapi_url=f"/{configs.API}/openapi.json",
            version="0.0.1",
        )

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

        self.app.include_router(staging_routers, prefix=configs.STAGING)

        self._initialized = True

app_creator = AppCreator()
app = app_creator.app