from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, send, join_room, leave_room, emit
from RoomForm import RoomForm
from roomGenerator import room_generator
import random
from lyrics import getLyrics

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'
socketio = SocketIO(app)

@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room', '')
    send(message['msg'], room=room)

@socketio.on('join', namespace='/chat')
def on_join(data):
    name = session.get('name', '')
    room = session.get('room', '')
    join_room(room)
    send(name + ' has entered the room.', room=room)

@socketio.on('leave', namespace='/chat')
def on_leave(data):
    name = session.get('name', '')
    room = session.get('room', '')
    leave_room(room)
    send(name + ' has left the room.', room=room)

@socketio.on('lyrics', namespace='/chat')
def lyrics(data):
    songs = data['songs']
    room = session.get('room', '')
    lyrics = ''

    while ("Verse" not in lyrics):
        try:
            index = random.randint(0, len(songs) - 1)
            lyrics = getLyrics(songs[index])
        except:
            pass
    
    emit('showLyrics', lyrics, room=room)



@app.route('/', methods=['GET', 'POST'])
def index():
    form = RoomForm(request.form)
    if request.method == 'POST' and form.validate():
        session['name'] = form.name.data
        if len(form.room.data) == 0:
            room_id = room_generator()
            session['room'] = room_id
        elif len(form.room.data) == 6:
            session['room'] = form.room.data
        else:
            return render_template('index.html')
        return redirect(url_for('chatRoom'))
    return render_template('index.html', form=form)

@app.route('/chatRoom')
def chatRoom():
    name = session.get('name', '')
    room = session.get('room', '')

    if name == '' or room == '':
        return redirect(url_for('/'))
    
    return render_template('chatRoom.html', name=name, room=room)

if __name__ == '__main__':
    socketio.run(app)