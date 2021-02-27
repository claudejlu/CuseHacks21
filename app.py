from flask import Flask, render_template, request
from flask_socketio import SocketIO
from RoomForm import RoomForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RoomForm(request.form)
    if request.method == 'POST' and form.validate():
        return "Your form has been validated"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    socketio.run(app)