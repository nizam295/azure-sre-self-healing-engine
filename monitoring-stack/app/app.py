from flask import Flask
import time

app = Flask(__name__)
request_counter = 0

@app.route('/')
def home():
    global request_counter
    request_counter += 1
    return f"<h1>SRE Target Node Online</h1><p>Total page clicks: {request_counter}</p><p>Visit /fault to test alerts.</p>"

@app.route('/metrics')
def metrics():
    global request_counter
    return f"# HELP flask_http_request_total Total request count\n# TYPE flask_http_request_total counter\nflask_http_request_total {request_counter}\n"

@app.route('/fault')
def fault():
    time.sleep(5)
    return "<h1>504 Gateway Timeout</h1>", 504

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
