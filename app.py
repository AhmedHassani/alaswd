from flask import Flask, render_template, request, redirect, url_for, flash
from model.model import *

app = Flask(__name__)
app.secret_key = "Secret Key"

lng = "en"


@app.route('/')
def index():
    if lng=="en":
        return render_template("home.html",
                               header=header_en,
                               hero=hero_en,
                               lng=lng,
                               footer=footer_en,
                               service=service_en,
                               prodcuts=prodcuts_en,
                               team=team_en,
                               about=about_en
                               )
    else:
        return render_template("home.html",
                               header=header_ar,
                               hero=hero_ar,
                               lng=lng,
                               footer=footer_ar,
                               service=service_ar,
                               prodcuts=prodcuts_ar,
                               team=team_ar,
                               about=about_ar
                               )



@app.route('/projects')
def projects():
    if lng=="en":
        return render_template("projects_view.html",
                               header=header_en,
                               hero=hero_en,
                               lng=lng,
                               footer=footer_en,
                               service=service_en,
                               prodcuts=prodcuts_en,
                               team=team_en,
                               about=about_en
                               )
    else:
        return render_template("projects_view.html",
                               header=header_ar,
                               hero=hero_ar,
                               lng=lng,
                               footer=footer_ar,
                               service=service_ar,
                               prodcuts=prodcuts_ar,
                               team=team_ar,
                               about=about_ar
                               )
@app.route('/booking')
def booking():
    if lng=="en":
        return render_template("booking_view.html",
                               header=header_en,
                               hero=hero_en,
                               lng=lng,
                               footer=footer_en,
                               service=service_en,
                               prodcuts=prodcuts_en,
                               team=team_en,
                               about=about_en,
                               consultation=consultation_en
                               )
    else:
        return render_template("booking_view.html",
                               header=header_ar,
                               hero=hero_ar,
                               lng=lng,
                               footer=footer_ar,
                               service=service_ar,
                               prodcuts=prodcuts_ar,
                               team=team_ar,
                               about=about_ar,
                               consultation=consultation_ar
                               )
@app.route('/jobs')
def jobs():
    if lng=="en":
        return render_template("jobs_view.html",
                               header=header_en,
                               hero=hero_en,
                               lng=lng,
                               footer=footer_en,
                               service=service_en,
                               prodcuts=prodcuts_en,
                               team=team_en,
                               about=about_en
                               )
    else:
        return render_template("jobs_view.html",
                               header=header_ar,
                               hero=hero_ar,
                               lng=lng,
                               footer=footer_ar,
                               service=service_ar,
                               prodcuts=prodcuts_ar,
                               team=team_ar,
                               about=about_ar
                               )



@app.route('/change/<lang>')
def change_language(lang):
    global lng
    if lang=='en':
        lng = 'en'
    else:
        lng = 'ar'
    return redirect("/")



if __name__ == "__main__":
    app.run(debug = True)

