from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)

    report_card = hackbright.get_report_card(github)

    html = render_template("student_info.html", first=first, 
                            last=last, 
                            github=github,
                            report_card=report_card)
    return html


@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    """Show form for adding new student."""
    return render_template("student_add.html")


@app.route("/add-confirm", methods=['POST'])    
def add_confirm():
    """Takes info user submitted on /student-add, adds to DB, and displays confirmation"""
    fname = request.form.get("firstname")
    lname = request.form.get("lastname")
    ghub = request.form.get("github")

    hackbright.make_new_student(fname, lname, ghub)

    return render_template("add_confirmation.html", firstname=fname,
                            lastname=lname, github=ghub)



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
