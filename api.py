import flask
from flask import jsonify
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/movie/list', methods=['GET'])
@cross_origin()
def movie_list():
    return "<p>Returns a list of movies</p>"

@app.route('/movie/detail/<string:movie_id>', methods=['GET'])
@cross_origin()
def movie_detail(movie_id):
    return "<p>Returns a list of movies</p>"

app.run()