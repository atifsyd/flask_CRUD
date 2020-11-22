from movies import *


@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'Movies': Movie.get_all_movies()})


@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id():
    response = Movie.get_movie(id)
    return jsonify(response)


@app.route('/movies', methods=['POST'])
def add_movie():
    new_movie = request.get_json()
    Movie.add_movie(new_movie['title'], new_movie['year'], new_movie['genre'])
    return Response('Movie added', 201, mimetype='application/json')


@app.route('/movies/<int:_id>', methods=['PUT'])
def update_movie(_id):
    new_movie = request.get_json()
    Movie.update_movie(_id, new_movie['title'], new_movie['year'], new_movie['genre'])
    return Response('Movie updated', status=200, mimetype='application/json')


@app.route('/movies/<int:_id>', methods=['DELETE'])
def remove_movie(_id):
    Movie.delete_movie(_id)
    return Response('Movie deleted', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(port=8090, debug=True)
