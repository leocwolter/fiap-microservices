import os

from flask import Flask

port = os.getenv("PORT", "8080")

app = Flask(__name__)
@app.route("/health")
def health():
    return "Deu certo (api2) :D\n"

@app.route("/teste")
def api():
    return "Resposta do api2"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
