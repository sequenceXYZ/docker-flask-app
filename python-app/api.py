import db_data as db
from http import HTTPStatus
from flask import make_response


def read_all():
    return db.get_all_people(), HTTPStatus.OK


def create_data_row(person):
    added = db.add_new_person(person)
    if added:
        return person, HTTPStatus.CREATED
    else:
        return make_response("Failed to add a person, it already exists", HTTPStatus.INTERNAL_SERVER_ERROR)


def read_one_row(name):
    return db.get_one_person(name), HTTPStatus.OK


def delete_row(name):
    rows_affected = db.delete_person(name)

    if rows_affected > 0:
        return make_response(f"{name} successfully deleted", HTTPStatus.OK)
    else:
        return make_response(f"{name} wasn't found", HTTPStatus.NOT_FOUND)


def update_row(name, person):
    return db.update_person(name, person), HTTPStatus.OK
