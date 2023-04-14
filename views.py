from typing import Union, Tuple

from flask import request, jsonify, Blueprint, Response
from marshmallow import ValidationError

from convector import configur
from models import BatchRequestSchema
from db import db

bp_pars = Blueprint('main', __name__, url_prefix='/perform_query')


@bp_pars.route('/', methods=['POST'])
def post() -> Union[Response, Tuple[Response, int]]:
    req = request.json
    try:
        val_data = BatchRequestSchema().load(req)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None
    for query in val_data['queries']:
        result = configur(
            cmd=query['cmd'],
            value=query['value'],
            file_name=val_data['file_name'],
            data=result
        )
    return jsonify(result)


@bp_pars.route('/', methods=['GET'])
def get():
    return 'eeeeeeeeeeeeeeeeeeeeeeeee'


@bp_pars.route("/test_db", methods=['GET'])
def test_db():
    result = db.session.execute(
        """
        SELECT 1;
        """
    ).scalar()
    return jsonify({"result": result})