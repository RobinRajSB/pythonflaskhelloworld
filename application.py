from flask import Flask,render_template,redirect, url_for, request
import tensorflow as tf

from oauth2client.service_account import ServiceAccountCredentials
app = Flask(__name__)

@app.route("/")
def hello():
    z = tf.constant(5.2, name="x", dtype=tf.float32)

    return "Hello World!"
