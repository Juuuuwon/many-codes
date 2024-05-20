from flask import Flask, render_template, request, jsonify
from models import SessionLocal, User

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(name=data['name'], email=data['email'])
    with SessionLocal() as session:
        session.add(new_user)
        session.commit()
    return jsonify({"message": "User added successfully"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    with SessionLocal() as session:
        session = SessionLocal()
        users = session.query(User).all()
    
    user_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify(user_list), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    with SessionLocal() as session:
        user = session.query(User).get(user_id)
        if user is None:
            return jsonify({"message": "User not found"}), 404
        session.delete(user)
        session.commit()
    
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
