# from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter
# , Depends

# router = APIRouter(prefix="/user", tags=["user"], dependencies=[Depends(JWTBearer())])

router = APIRouter(prefix="/todo", tags=["Todo"])

@router.get("/")
def greeting():
    return "hello, todo"

# @router.get("", response_model=)
# @inject
# async def get_user_list(
#     find_query: FindUser = Depends(),
#     service: UserService = Depends(Provide[Container.user_service]),
#     current_user: User = Depends(get_current_super_user),
# ):
#     return service.get_list(find_query)

