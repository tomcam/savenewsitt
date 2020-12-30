from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated

# TODO: Doesn't work for some reason
# from py4web.utils.form import FormStyleBootstrap4

from py4web.utils.form import Form, FormStyleBulma

@unauthenticated()
@action("index")
@action.uses('index.html')
#@action.uses(auth, "index.html")
def index():
    query=db(db.post).select()
    return dict(query=query)

@action("new",method=['GET','POST'])    
@action.uses('new.html')
def new():
    form=Form(db.post,formstyle=FormStyleBulma)
    #form=Form(db.post)
    if form.accepted:
        redirect(URL('index'))
    return dict(form=form)

@action("post/<id>")
@action.uses('post.html')
def post(id):
    post=db.post(id)
    form=Form(db.post,post)
    return dict(post=post,form=form)