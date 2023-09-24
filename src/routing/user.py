import requests
from flask import Blueprint, request

from src.authorization.auth import token_required
from src.db import db
from src.exception.generic_exception import (
    BadRequestEception,
    MissingJsonValueException,
    MissingQueryParameterException,
)
from src.model.user import User
from src.repository.user import UserRepository

user_bp = Blueprint("user", __name__)


@user_bp.get("")
def get_users():
    response = UserRepository.get_all_user()
    return response


@user_bp.get("/fetch")
def fetch_user_data():
    page = request.args.get("page")
    if page is None or page == "":
        raise MissingQueryParameterException(query_parameter="page")

    try:
        page = int(page)
    except ValueError as e:
        raise BadRequestEception(f"page '{page}' is not a number")

    url = f"https://reqres.in/api/users?page={page}"

    response = requests.get(url=url)
    datas = response.json().get("data")
    for data in datas:
        UserRepository.add_user(User(**data), db=db)
    return response.json()


@user_bp.get("/<int:user_id>")
def get_specific_user(user_id: int):
    response = UserRepository.get_user_by_id(id=user_id)
    return response


@user_bp.post("")
def post_users():
    data = request.get_json()
    new_user = User(**data)
    response = UserRepository.add_user(user=new_user, db=db)
    return response


@user_bp.put("")
def put_users():
    data = request.get_json()
    if data.get("id") is None:
        raise MissingJsonValueException("no id provided")
    new_user = User(**data)
    response = UserRepository.edit_user(id=new_user.id, new_user=new_user, db=db)
    return response


@user_bp.delete("")
@token_required
def delete_users():
    data = request.get_json()
    if data.get("id") is None:
        raise MissingJsonValueException("no id provided")
    new_user = User(**data)
    response = UserRepository.soft_delete_user(id=new_user.id, db=db)
    return response
