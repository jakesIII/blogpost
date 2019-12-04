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

@main.route('/blog_comments/<int:blog_id>', methods=['GET'])
def view_comments(blog_id):

    comments=Comments.query.filter_by(blog_id=blog_id).all()

    return render_template('view_comment.html', comments = comments)

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.avatar= path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):

    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio=form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)

@main.route('/blog/<int:id>/update_blog', methods = ["POST", "GET"])
@login_required
def update_blog(id):
    blog=Blog.query.filter_by(id=Blog.id).first()
    # if blog is None:
    #     abort(404)
    form=UpdateBlogForm()
    if form.validate_on_submit():
        blog.content=form.content.data
        blog.title=form.title.data

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('main.index',id = id))
    return render_template('update_blog.html', UpdateBlogForm = form)

    return render_template('view_comment.html', comments = comments)


# delete a whole blog
@main.route('/blog/delete/<int:id>')
@login_required
def delete(id):
    blog=Blog.query.filter_by(id=Blog.id).first()
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('main.index'))
    # return render_template('index.html')

# delete comment
@main.route('/comments/delete/<int:id>')
@login_required
def delete_comment(id):
    comment=Comments.query.filter_by(id=Comments.id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('main.index'))
    # return render_template('index.html')
