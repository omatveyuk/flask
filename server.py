from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

jobs = { "1": {"title": "Software Engineer", "checked": True}, 
         "2": {"title": "QA Engineer", "checked": False},
         "3": {"title": "Product Manager", "checked": False},
       }
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def start_here():
    """Home page."""

    return render_template("index.html")

@app.route("/application-form")
def show_application_form():
    """Present a user application from"""

    return render_template("application-form.html", jobs=jobs)

@app.route("/application-success", methods=["POST"])
def accept_form_data():
    """Accept data from application form"""

    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    if request.form["salary"]:
        try:
            salary = "{0:,.2f}".format(float(request.form["salary"]))
        except:
            flash("Salary must be a number")
            return redirect("/application-form")
    else:
        salary = 0
    jobid = request.form["job"]

    return render_template("application-response.html",
                           firstname=firstname,
                           lastname=lastname,
                           salary=salary,
                           jobtitle=jobs[jobid]["title"])



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
