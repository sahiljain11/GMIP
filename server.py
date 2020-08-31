import Flask, jsonify, request, render_template, abort, session, send_from_directory, url_for, send_file
from flask_session import Session
import flask
import os
import json
import random
import time
import base64
import random
import string

@app.route("/demos", methods=['GET'])
def demos():
    return render_template('demos.html')

@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/", methods=['GET'])
def home_page():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()