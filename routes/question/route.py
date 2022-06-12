from flask import jsonify


def run():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})