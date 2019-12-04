from flask import render_template, request, redirect, url_for,abort
from . import main
from ..models import User, Blog, Comments, Quote
from ..requests import get_quotes
from flask_login import login_required
from .forms import UpdateProfile, NewBlogForm, UpdateBlogForm, CommentForm
from .. import db

@main.route('/', methods=['GET'])
def index():
    blogs=Blog.get_blog()
    quote=get_quotes()
    title='Thy Blog Post'
    return render_template('index.html', quote=quote, title=title, blogs=blogs)

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user=user)

@main.route('/new_blog', methods=['GET', 'POST'])
@login_required
def new_blogs():
    form=NewBlogForm()
    if form.validate_on_submit():
        new_blog=Blog(title=form.title.data, content=form.content.data, author=form.author.data)
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    return render_template('new_blog.html', NewBlogForm=form)

@main.route('/blog/new_comment/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def new_comment(blog_id):
    form=CommentForm()
    if form.validate_on_submit():
        new_comment=Comments(comment=form.comment.data, user=form.user.data, blog_id=blog_id)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    return render_template('comments.html', CommentForm=form)
