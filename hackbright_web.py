"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, flash

import hackbright

app = Flask(__name__)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    grades_list = hackbright.get_grades_by_github(github)

    # return "{acct} is the GitHub account for {first} {last}".format(
    #     acct=github, first=first, last=last)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades_list=grades_list)

    return html

@app.route("/project")
def display_project:
   
    project_info = request.args.get('title')


@app.route("/new-student")
def new_student_form():
    """add new student"""

    return render_template("new_student.html")

@app.route("/new-student-display")
def new_student_displayed():
    """display new student """

    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)
    return render_template("display_student.html")

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
