from flask import Flask, render_template, request, redirect, abort


app = Flask(__name__)



messages=[]

class Message(object):
    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message


@app.route('/')
def welcome():

    return render_template('index.html', title="hackerspace", messages=messages[:100])


@app.route("/message", methods=['POST', 'GET'])
def message():
    if request.method == "GET":
        return render_template("form.html")
    try:
        message = request.form['message']
        name = request.form.get("name", "dude")
        email = request.form.get("email", "None")
        return request

    except:
        return abort(400)

    if name == "jobs":
        return abort(501)
    elif name == "bill":
        return abort(403)
    messages.insert(0, Message(name, email, message))
    return redirect('/')

@app.route("/forbidden")
def return_forbidden():
    return abort(403)


@app.route("/grid")
def create_grid():
    return render_template("create_grid.html")

@app.route("/not_implemented")
def return_not_implemented():
    return abort(501)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template("405.html"), 405

@app.errorhandler(501)
def all_is_steves_fault(e):
    return render_template("501.html"), 501

@app.errorhandler(403)
def page_is_forbidden(e):
    return render_template("403.html"), 403

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
