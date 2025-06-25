from flask import Flask, render_template, request, session
from chatbot import get_response  # This should be your chatbot logic function
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for using session

@app.route('/', methods=['GET', 'POST'])
def home():
    # Initialize chat history in session if not present
    if 'chat_history' not in session:
        session['chat_history'] = []

    # Handle form submission
    if request.method == 'POST':
        user_msg = request.form['message']
        bot_reply = get_response(user_msg)

        # Add user and bot messages to chat history
        session['chat_history'].append(('user', user_msg))
        session['chat_history'].append(('bot', bot_reply))
        session.modified = True  # Important to let Flask know session was changed

    return render_template('index.html', chat_history=session.get('chat_history', []))

# Optional: Route to clear chat history
@app.route('/clear')
def clear_chat():
    session.pop('chat_history', None)
    return render_template('index.html', chat_history=[])

if __name__ == '__main__':
    app.run(debug=True)
