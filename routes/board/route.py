from flask import jsonify


def run():
    return jsonify({'name': 'blice',
                    'email': 'blice@outlook.com'})