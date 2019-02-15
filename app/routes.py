from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'gema antika hariadi',
            'address': 'pandeyan umbulharjo',
            'age': '21',
            'hobby': 'doing this'}
    post=[
        {
            'author': {'username': 'ennu intan iksan', 'age': '19'},
            'have' : {'title': 'the strongest girl', 'hair': 'slim'}
        },
        {
            'author': {'username': 'susanti auliya'},
            'have' : {'title': 'the beutiful sound', 'hair': 'long'}
        }
    ]
    return render_template('index.html', title='Home', tampilan='cakep bener', user=user, post=post)