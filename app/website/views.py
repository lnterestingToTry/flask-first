from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

from . import db
from .models import Notes

import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Notes(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    
    return render_template("home.html", user=current_user)


@views.route('/delete_note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    note_id = data['note_id']
    
    note = Notes.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})