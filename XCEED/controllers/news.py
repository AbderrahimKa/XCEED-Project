from XCEED import app
from flask import Flask, render_template, redirect, request, send_file,session
from XCEED.models.news import News  # Assuming you have a News model
from io import BytesIO

@app.route('/news_create', methods=['POST'])
def add_news():  
    if(session['isAdminLoggedIn']):
        if 'new_img' in request.files:
            photo_file = request.files['new_img']
            photo_data = photo_file.read()
        data = {
            'title': request.form['title'],
            'content': request.form['content'],
            'new_img': photo_data
        }
        News.create(data)
        return redirect('/see_all_news')
    return redirect('/')

@app.route("/see_all_news")
def see_all_news():
    if(session['isAdminLoggedIn']):
        all_news = News.get_all()
        return render_template('see_all_news.html', news=all_news)
    return redirect('/')

@app.route("/news/<int:id>")
def get_news_image(id):
    data = {'id': id}
    news_item = News.show_one(data)
    if news_item:
        photo_data = news_item.new_img
        return send_file(BytesIO(photo_data), mimetype='image/*')

@app.route('/news/delete/<int:id>')
def delete_news(id):    
    News.remove({'id': id})
    return redirect('/see_all_news')
