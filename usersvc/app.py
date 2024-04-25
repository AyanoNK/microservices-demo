from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def add_user():
    """Add a user to the database

    Returns:
        dict: the user id
    """
    data = request.get_json()
    name = data['name']
    email = data['email']
    conn = psycopg2.connect(
        database="blogs", user="postgres", password="postgres", host="db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", (name, email))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': user_id}), 201


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get the data of a user

    Args:
        user_id (int): the user id

    Returns:
        dict: data of the user
    """
    conn = psycopg2.connect(
        database="blogs", user="postgres", password="postgres", host="db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'id': user[0], 'name': user[1], 'email': user[2]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
