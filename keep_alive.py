from flask import Flask, render_template, redirect
from threading import Thread
import random

app = Flask('')

@app.route('/')
def main():
    #return render_template("root.html")
    return "i use arch btw", 200

def getrnd():
    rnd = random.randint(1000,9999)
    if rnd == 6969:
        rnd = random.randint(1000, 9999)
    return rnd

def run():
    try:
        app.run(host="0.0.0.0", port=6969)
    except OSError:
        app.run(host="0.0.0.0", port=getrnd())

def keep_alive():
    server = Thread(target=run)
    server.start()
