from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, send
from RoomForm import RoomForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'
socketio = SocketIO(app)

@socketio.on('text', namespace='/chat')
def text(message):

    send(message['msg'], room=room)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RoomForm(request.form)
    if request.method == 'POST' and form.validate():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('chatRoom'))
    return render_template('index.html', form=form)

@app.route('/chatRoom')
def chatRoom():
    name = session.get('name', '')
    room = session.get('room', '')

    if name == '' or room == '':
        return render_template('index.html')
    
    return render_template('chatRoom.html', name=name, room=room)

if __name__ == '__main__':
    socketio.run(app)