from flask import Flask, jsonify
import routes

app = Flask(__name__)


@app.route('/questions', methods=['GET'])
def questions():
    return routes.question()


@app.route('/boards', methods=['GET'])
def board():
    return routes.board()


if __name__ == '__main__':
    app.run()
