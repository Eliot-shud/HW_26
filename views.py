from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from db import db
from processing import get_resault
from model import RequestSchema

query_blueprint = Blueprint('main', __name__)

FILE_NAME = 'data/apache_logs.txt'


@query_blueprint.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json
    try:
        check_data = RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    cmd = check_data.get('cmd1')
    value = check_data.get('value1')
    file_name = check_data.get('file_name')
    data = get_resault(cmd, value, file_name, None)

    cmd = check_data.get('cmd2')
    value = check_data.get('value2')
    file_name = check_data.get('file_name')
    result = get_resault(cmd, value, file_name, data)

    return jsonify(result)


@query_blueprint.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@query_blueprint.route('/test_db', methods=['GET'])
def test_db():
    result = db.session.execute(
        '''
        SELECT 1;
        '''
    ).scalar()
    return jsonify({'result': result})


