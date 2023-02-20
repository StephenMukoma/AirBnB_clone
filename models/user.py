#!/usr/bin/python3
"""Defines class User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Initializes user attributes """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
