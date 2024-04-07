from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Simple dictionary to store username-password pairs (for demonstration purposes)
users = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('chat'))
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('chat'))
    else:
        return render_template('index.html', error='Invalid username or password.')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/chat')
def chat():
    if 'username' in session:
        return render_template('chat.html')
    else:
        return redirect(url_for('index'))

@socketio.on('message')
def handle_message(message):
    if 'username' in session:
        print('Received message from {}: {}'.format(session['username'], message['message']))
        emit('message', {'message': message['message'], 'username': session['username']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000) 
    print("Starting server...")
    print("Server started.")
