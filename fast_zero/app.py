from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserDB, UserPublicSchema, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Ola asdasd'}


@app.post(
    '/user/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserSchema):
    user_whith_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_whith_id)

    return user_whith_id
