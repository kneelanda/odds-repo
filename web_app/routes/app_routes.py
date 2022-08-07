# web_app/routes/app_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.odds_script import money_lines

app_routes = Blueprint("app_routes", __name__)

@app_routes.route("/app/form")
def app_form():
    print("INPUT FORM...")
    return render_template("app_form.html")

@app_routes.route("/app/result", methods=["POST"])
def app_result():
    print("APP RESULT...")

    request_data = dict(request.form)
    print("FORM DATA:", request_data)

    sport = request_data.get("sport") or "americanfootball_nfl"

    results = money_lines(sport=sport)

    with open('output.txt', 'r') as f:
        return render_template("app_result.html",text=f.read())
