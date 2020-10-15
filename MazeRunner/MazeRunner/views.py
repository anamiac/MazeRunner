"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MazeRunner import app



@app.route('/')
@app.route('/meteor')
def meteor():
    """Renders the Meteor page."""
    return render_template(
        'MeteorRunner.html',
        title='Meteor',
        xDimension=10,
        yDimension=8
    )


@app.route('/fractal')
def fractal():
    """Renders the Meteor page."""
    return render_template(
        'FractalRunner.html',
        title='Fractal',
        xDimension=16,
        yDimension=16
    )
