class LoggerInstance(object):
    def __new__(cls):
        from application.main.utility.logger.custom_logging import LogHandler
        return LogHandler()


class IncludeAPIRouter(object):
    def __new__(cls):
        from application.main.routers.routs import router as router_hello_world
        from fastapi.routing import APIRouter
        router = APIRouter()
        router.include_router(router_hello_world, prefix='/api/v1', tags=['hello_world'])
        return router



# instance creation
logger_instance = LoggerInstance()
