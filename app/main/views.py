from flask import render_template, request, redirect, url_for,abort
from . import main
from ..models import User, Quote
from ..requests import get_quotes
from flask_login import login_required

@main.route('/', methods=['GET'])
def index():
    quote=get_quotes()
    title='Thy Blog Post'
    return render_template('index.html', quote=quote, title=title)

@main.route('/new_blog', methods=['GET', 'POST'])
@login_required
def new_blogs():
    form=NewBlogForm()
    if form.validate_on_submit():
        new_blog=Blog(title=form.title.data, content=form.content.data, author=form.author.data)
        new_blog,save_blog()
        return redirect(url_for('main.index'))
    return render_template('new_blog.html', NewBlogForm=form)
