from XCEED import app
from flask import Flask, render_template, redirect, request, send_file,session
from XCEED.models.event import Event  # Assuming you have an Event model
from io import BytesIO

@app.route('/event_create', methods=['POST'])
def add_event():  
    if(session['isAdminLoggedIn']):
        if 'event_img' in request.files:
            photo_file = request.files['event_img']
            photo_data = photo_file.read()
        data = {
            'title': request.form['title'],
            'start_date': request.form['start_date'],
            'end_date': request.form['end_date'],
            'content': request.form['content'],
            'location': request.form['location'],
            'event_img': photo_data
        }
        Event.create(data)
        return redirect('/see_all_events')
    return redirect('/')

@app.route("/see_all_events")
def see_all_events():
    if(session['isAdminLoggedIn']):
        all_events = Event.get_all()
        return render_template('see_all_events.html', events=all_events)
    return redirect('/')

@app.route("/event/<int:id>")
def get_event_image(id):
    data = {'id': id}
    event_item = Event.show_one(data)
    if event_item:
        photo_data = event_item.event_img
        return send_file(BytesIO(photo_data), mimetype='image/*')

@app.route('/event/delete/<int:id>')
def delete_event(id):    
    if(session['isAdminLoggedIn']):
        Event.remove({'id': id})
        return redirect('/see_all_events')
    return redirect('/')
