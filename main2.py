from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for demonstration
users = {}
messages = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    if not username or username in users:
        return jsonify({'error': 'Invalid or duplicate username'}), 400
    users[username] = {'username': username}
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    sender = data.get('sender')
    receiver = data.get('receiver')
    text = data.get('text')
    if sender not in users or receiver not in users:
        return jsonify({'error': 'Sender or receiver not found'}), 404
    message = {
        'sender': sender,
        'receiver': receiver,
        'text': text,
        'timestamp': datetime.utcnow().isoformat()
    }
    messages.append(message)
    return jsonify({'message': 'Message sent'}), 200

@app.route('/messages/<username>', methods=['GET'])
def get_messages(username):
    if username not in users:
        return jsonify({'error': 'User not found'}), 404
    user_messages = [m for m in messages if m['receiver'] == username or m['sender'] == username]
    return jsonify({'messages': user_messages}), 200

if __name__ == '__main__':
    app.run(debug=True)