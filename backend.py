__author__ = 'Bogdan'
# encoding=utf-8
from flask import Flask, render_template, redirect, request
import codecs
import re
from random import choice


app = Flask(__name__)

@app.route('/')
def index():
    word = ''
    day_words = []
    ya_words = codecs.open('ya_words.txt', 'r', 'utf8')
    day_word = re.findall(u'\w+;(.*?)\r\n', ya_words.read(), flags=re.U)
    for _ in xrange(8):
        day_words.append('<p>' + choice(day_word) + '</p><br/>')
    ya_words.close()

    return render_template('workshop.html', word=word, day_words=day_words)

app.run(debug=True)
