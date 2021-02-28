from flask import Flask, render_template, request, redirect, url_for, session, abort
from flask_socketio import SocketIO, send, join_room, leave_room, emit
from RoomForm import RoomForm
from roomGenerator import room_generator
import random
from lyrics import getLyrics
import os
from dotenv import load_dotenv
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from cloudSQL import cloudSQL

load_dotenv()
twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_api_key_sid = os.environ.get('TWILIO_API_KEY_SID')
twilio_api_key_secret = os.environ.get('TWILIO_API_KEY_SECRET')
cloudTool = cloudSQL()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'
socketio = SocketIO(app,cors_allowed_origins="*")

@socketio.on('text', namespace='/chatRoom')
def text(message):
    room = session.get('room', '')
    send(message['msg'], room=room)

@socketio.on('join', namespace='/chatRoom')
def on_join(data):
    name = session.get('name', '')
    room = session.get('room', '')
    join_room(room)
    send(name + ' has entered the room.', room=room, people=cloudTool.listData('testdb', room))

@socketio.on('leave', namespace='/chatRoom')
def on_leave(data):
    name = session.get('name', '')
    room = session.get('room', '')
    leave_room(room)
    send(name + ' has left the room.', room=room)

@socketio.on('lyrics', namespace='/chatRoom')
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

@app.route('/login', methods=['POST'])
def login():
    username = session.get('name', '')
    room = session.get('room', '')
    if not username:
        abort(401)

    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity=username)
    token.add_grant(VideoGrant(room=room))

    return {'token': token.to_jwt().decode()}

if __name__ == '__main__':
    socketio.run(app)