from XCEED import app
from XCEED.models.user import User
from flask import Flask, render_template, redirect, request,session
from XCEED.models.coach import Coach
from XCEED.models.form import Form
from XCEED.models.news import News
from XCEED.models.event import Event
from XCEED.utilities.utilites import  Utilities


@app.route("/")
def main():
    all_event = Event.get_last_two()
    all_news = News.get_last_two()
    session['isAdminLoggedIn'] = False
    return render_template('index.html' , all_event=all_event , all_news=all_news)

@app.route('/sign_up')
def sign_in_user():
    return render_template('sign_up_user_form.html')

@app.route('/more_info_form')
def more_info_form():
    return render_template('more_info_form.html')

@app.route('/more_info_form_action', methods=['POST'])
def more_info_form_action():
    print('******************************************')
    data = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'message': request.form.get('message')
    }

    email_sender = "xceedtraining@gmx.com"
    email_receiver= "xceedtraining@gmx.com"
    subject="Inscription for a new client"
    email_password = "Xceed2023"
    context=f"""
                Client Name : {data['name']}
                Client Email : {data['email']}
                Clent Message : {data['message']}
            """
    Utilities.send_mail(email_sender,email_receiver,subject,context,email_password)

    return redirect('/')


@app.route('/see_one_event/<int:event_id>')
def see_one_event(event_id):
    event_details = Event.show_one_by_id(event_id)
    return render_template('see_one_event.html', event=event_details)

@app.route('/see_one_news/<int:news_id>')
def see_one_news(news_id):
    news_details = News.show_one_by_id(news_id)
    return render_template('see_one_news.html', news=news_details)

@app.route('/login')
def sign_up_user():
    return render_template('log_in_user_form.html')

@app.route('/login_dash_admin')
def coaches_login():
    if(session['isAdminLoggedIn']):
        return render_template('dash_admin.html')
    return redirect('/')

@app.route('/add_coach')
def add_coach_render():
    if(session['isAdminLoggedIn']):
        return render_template('add_coach.html')
    return redirect('/')

@app.route('/add_event')
def add_event_render():
    if(session['isAdminLoggedIn']):
        return render_template('add_event.html')
    return redirect('/')

@app.route('/add_news')
def add_news_render():
    if(session['isAdminLoggedIn']):
        return render_template('add_news.html')
    return redirect('/')

@app.route('/Individuals.html')
def individuals():
    return render_template('Individuals.html')

@app.route('/GYM_Owner.html')
def gym_owner():
    return render_template('GYM_owner.html')

@app.route('/Corporate.html')
def corporate():
    return render_template('Corporate.html')

@app.route('/Events.html')
def events():
    return render_template('Events.html')

@app.route('/store.html')
def store():
    return render_template('store.html')

@app.route('/trainer.html')
def crew():
    all_coaches = Coach.get_all()
    return render_template('trainer.html' , coches=all_coaches)

@app.route('/contact.html')
def resources():
    all_news = News.get_all()
    return render_template('contact.html' , all_news=all_news)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/client/form')
def user_form():
    user = User.get_by_id({'id' : session['user_id']})
    return render_template('client_form.html' , user = user)



