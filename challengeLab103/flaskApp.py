#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Trivia question and answer
trivia_question = "What is the capital of France?"
correct_answer = "Paris"


@app.route("/", methods=["GET", "POST"])
def landing_page():
    if request.method == "POST":
        user_answer = request.form.get("answer")
        if user_answer == correct_answer:
            return redirect("/correct")
        else:
            return render_template("index.html", question=trivia_question, message="Wrong answer. Try again!")
    return render_template("index.html", question=trivia_question, message="")


@app.route("/correct")
def correct_answer():
    return "Congratulations! Your answer is correct."


if __name__ == "__main__":
    app.run(debug=True)

