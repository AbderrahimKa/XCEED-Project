from flask import render_template, request, redirect, session, flash, jsonify
from XCEED import app
from flask_bcrypt import Bcrypt
from XCEED.models.user import User
from XCEED.models.form import Form
from XCEED.utilities.utilites import Utilities
bcrypt = Bcrypt(app)

@app.route('/users/create', methods=['POST'])
def register():
    if(User.validate(request.form)):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form,'password':pw_hash
        }
        if (request.form['user_type'] == 'individual'):
            user_id = User.create(data)
            session['user_id'] = user_id
            return redirect('/client/form')
        if (request.form['user_type'] == 'gym_owner'):
            return redirect('/more_info_form')
        if (request.form['user_type'] == 'corporate'):
            return redirect('/more_info_form')
    return redirect('/sign_up')


@app.route("/user/login", methods=["POST"])
def login12():
    if ((request.form["email"] == 'xceed@admin.com') and (request.form['password'] == '123456789')) :
        session['isAdminLoggedIn'] = True
        return redirect('/login_dash_admin')
    user = User.get_by_email({"email": request.form["email"]})
    if not user:
        flash("Please check your email", "login_email")
        return redirect("/login")
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Please check your password", "login_pwd")
        return redirect("/login")
    session['user_id'] = user.id
    return redirect('/')

# Your route to handle form submission
@app.route('/user/form', methods=["POST"])
def user_form_submit():
    if 'user_id' in session:
        data = {**request.form, "user_id": session['user_id']}
        newForm = Form.create(data)
        # ----------------------
        email_sender = "xceedtraining@gmx.com"
        email_receiver= "hammakammounis@gmail.com"
        subject="Inscription for a new client"
        email_password = "Xceed2023"
        context=f"""
            Full Name: {data['full_name']}

            Email: {data['email']}
            
            Date of Birth: {data['date_of_birth']}
            
            Country: {data['country']}
            
            Phone Number: {data['phone_number']}
            
            Goal: {data['goal']}
            
            Motivation: {data['motivition']}
            
            Goal Details: {data['goal_details']}
            
            Coaching Type: {data['coaching_type']}
            
            Weight: {data['weight']}
            
            Height: {data['height']}
            
            Activity Level: {data['activity_level']}
            
            Hours of Sleep: {data['hours_of_sleep']}
            
            Default Workout Time: {data['default_workout_time']}
            
            Meals per Day: {data['meals_per_day']}
            
            Forbidden Food: {data['forbidden_food']}
            
            Training Experience: {data['training_experience']}
            
            Default Activity: {data['default_activity']}
            
            Previous Medical History: {data['previous_medical_history']}
            
            Default Health Concerns: {data['default_health_concerns']}
            
            About Yourself: {data['about_yourself']}
            
            From Where: {data['from_where']}
            
            Additional Question: {data['additional_question']}
            """
        Utilities.send_mail(email_sender,email_receiver,subject,context,email_password)
        # ----------------------
        return redirect('/')

@app.route('/see_all_users')
def users_dash_admin():
    if(session['isAdminLoggedIn']):
        data = User.get_all()
        return render_template('all_users.html' , data=data)
    return redirect('/')
    
@app.route('/see_all_users/<int:id>')
def users_dash_admin_one(id):
    if(session['isAdminLoggedIn']):
        user_id = {'id': id}
        data = Form.get_user_form(user_id)
        return render_template('one_user_form.html' , data=data)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')