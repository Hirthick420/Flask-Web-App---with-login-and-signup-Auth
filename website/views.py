#This file has all the url/ this file is blueprint of our project
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Note

from . import db
import json

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST']) 
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note)<1:
            flash('Note is too sort!', category = 'error')

        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    noteId = data.get('noteId')
    
    print(f"Received noteId: {noteId}, Type: {type(noteId)}")  # Debug print
    
    if noteId:
        note_obj = Note.query.get(int(noteId))
        print(f"Found note: {note_obj}")  # Debug print
        
        if note_obj and note_obj.user_id == current_user.id:
            db.session.delete(note_obj)
            db.session.commit()
            print(f"Deleted note {noteId}")  # Debug print
    
    return jsonify({})