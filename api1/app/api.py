import os

import requests
from flask import Flask

api2_host = os.getenv("API2_HOST", "api2:8080")
port = os.getenv("PORT", "8080")

app = Flask(__name__)
@app.route("/health")
def health():
    return "Deu certo (api1) :D\n"

@app.route("/outra-api")
def api():
    res = requests.get(f"http://{api2_host}/teste").content
    return f"Bati na url {api2_host}/teste e ela retornou: {res}\n"  

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
