from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def current_datetime():
    now = datetime.now()
    return f"<html><body>Obecna data i godzina: {now}</body></html>"

if __name__ == '__main__':
    app.run(debug=True)