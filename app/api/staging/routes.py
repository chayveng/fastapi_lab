from fastapi import APIRouter
from app.api.staging.endpoints.todo import router as todo_router


routers = APIRouter()
router_list = [todo_router]

for router in router_list:
    # router.tags = router.tags.append()
    routers.include_router(router)