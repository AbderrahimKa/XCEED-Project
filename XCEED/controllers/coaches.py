from XCEED import app
from flask import Flask, render_template, redirect, request, send_file,session
from XCEED.models.coach import Coach
from io import BytesIO

@app.route('/coach_create', methods=['POST'])
def add_coach():  
    if(session['isAdminLoggedIn']):
        if 'photo_link' in request.files:
            photo_file = request.files['photo_link']
            photo_data = photo_file.read()
        data = {
            'firstname': request.form['first_name'],
            'lastname': request.form['last_name'],
            'email': request.form['email'],
            'insta_link': request.form['insta_link'],
            'linkedin_link': request.form['linkedin_link'],
            'info': request.form['info'],
            'photo_link': photo_data
        }
        Coach.create(data)
        return redirect('/see_all_coaches')
    return redirect('/')

@app.route("/see_all_coaches")
def see_all_coches():
    if(session['isAdminLoggedIn']):
        all_coaches = Coach.get_all()
        return render_template('see_all_coahes.html' , coches=all_coaches)
    return redirect('/')

@app.route("/coach/<int:id>")
def get_image(id):
    data = {'id': id}
    coach = Coach.show_one(data)
    if coach:
        photo_data = coach.photo_link  
        return send_file(BytesIO(photo_data), mimetype='image/*')

        
@app.route('/coach/delete/<int:id>')
def delete_coach(id): 
    if(session['isAdminLoggedIn']):   
        Coach.remove({'id':id})
        return redirect('/see_all_coaches')
    return redirect('/')








