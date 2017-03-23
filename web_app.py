from flask import Flask
application = Flask(__name__)
from flask import render_template
import films_sf
from films_sf import streetview_link
from films_sf import get_film_list
from films_sf import msg_for_movie



@application.route('/')
def homepage():
    template = 'homepage.html'
    film_list = get_film_list()
    return render_template(template, film_list = film_list)
    #return "Give me a movie name and I will return some information and a map"

@application.route('/<film_name>')
def run_app(film_name):
    link = streetview_link(film_name)
    msg = msg_for_movie(film_name)
    template = 'movie_page.html'
    return render_template(template, film_name= film_name, location_link = link, message = msg)
    #return "hello pt2"

if __name__ == '__main__':
    application.run(debug=True, use_reloader=True)
