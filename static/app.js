let connected = false;
const username = document.getElementById('myName').getAttribute('value');
const button = document.getElementById('leave_room');
const container = document.getElementById('container');
let room;


function addLocalVideo() {
    Twilio.Video.createLocalVideoTrack().then(track => {
        let video = document.getElementById('local').firstChild;
        video.appendChild(track.attach());
    });
};

function disconnectButtonHandler(event) {
    event.preventDefault();
    disconnect();
    connected = false;
};

function connect(username) {
    let promise = new Promise((resolve, reject) => {
        fetch('/login', {
            method: 'POST',
            body: JSON.stringify({'username': username})
        }).then(res => res.json()).then(data => {
            return Twilio.Video.connect(data.token);
        }).then(_room => {
            room = _room;
            room.participants.forEach(participantConnected);
            room.on('participantConnected', participantConnected);
            room.on('participantDisconnected', participantDisconnected);
            connected = true;
            resolve();
        }).catch(() => {
            reject();
        });
    });
    return promise;
};

function participantConnected(participant) {
    let participantDiv = document.createElement('div');
    participantDiv.setAttribute('id', participant.sid);
    participantDiv.setAttribute('class', 'participant');

    let tracksDiv = document.createElement('div');
    participantDiv.appendChild(tracksDiv);

    let labelDiv = document.createElement('div');
    labelDiv.innerHTML = participant.identity;
    participantDiv.appendChild(labelDiv);

    container.appendChild(participantDiv);

    participant.tracks.forEach(publication => {
        if (publication.isSubscribed)
            trackSubscribed(tracksDiv, publication.track);
    });
    participant.on('trackSubscribed', track => trackSubscribed(tracksDiv, track));
    participant.on('trackUnsubscribed', trackUnsubscribed);
};

function participantDisconnected(participant) {
    document.getElementById(participant.sid).remove();
};

function trackSubscribed(div, track) {
    div.appendChild(track.attach());
};

function trackUnsubscribed(track) {
    track.detach().forEach(element => element.remove());
};

function disconnect() {
    room.disconnect();
    while (container.lastChild.id != 'local')
        container.removeChild(container.lastChild);
    connected = false;
    window.location.href = 'http://localhost:5000/';
};

addLocalVideo();
connect(username).then(() => {alert("You are connected!")}).catch(() => {alert("Sorry, we could not connect you")})
button.addEventListener('click', disconnectButtonHandler);