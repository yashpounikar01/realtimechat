# Real-Time-Group-Chat-Web-Application-using-Python

This is a simple real-time chat application built using Flask and Socket.IO. It allows users to log in, send messages, and log out in real-time.

## Features

- **User Authentication**: Users can log in with their username and password.
- **Real-time Messaging**: Messages are delivered instantly to all connected clients using Socket.IO.
- **Logout Functionality**: Users can log out at any time, which will end their session.

## Technologies Used

- **Flask**: A micro web framework written in Python.
- **Socket.IO**: A JavaScript library for real-time web applications. It enables real-time bidirectional event-based communication.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.x)
- Flask (`pip install flask`)
- Flask-SocketIO (`pip install flask-socketio`)
- Socket.IO client library (included via CDN in the provided HTML)

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Flask application by executing `python app.py`.
4. Visit `http://localhost:5000` in your web browser to access the application.

## Usage

1. **Login**: Enter your username and password on the login page and click the "Login" button.
2. **Chat**: Once logged in, you can send messages in the chat box at the bottom of the page.
3. **Logout**: To log out, click the "Logout" button at the bottom of the chat box.

## File Structure

- `app.py`: Contains the Flask application logic, including routes and Socket.IO event handlers.
- `index.html`: HTML template for the login page.
- `chat.html`: HTML template for the chat page.
- `README.md`: Documentation file (you're reading it!).

## Notes

- This application uses a simple dictionary to store username-password pairs for demonstration purposes. In a real-world scenario, you would use a more secure method, such as a database.
- For production use, you should deploy this application on a secure web server with proper security configurations.

## Author

This application was created by Yash Pounikar.

---
