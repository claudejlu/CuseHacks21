from wtforms import Form, StringField, validators

class RoomForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=15)])
    room = StringField('Room', [validators.Length(min=6, max=6)])
