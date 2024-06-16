import psutil
from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent(interval=1)
    mem_metric = psutil.virtual_memory().percent
    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
