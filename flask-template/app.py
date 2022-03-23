# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from model import show_results
# from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/results', methods = ['POST', 'GET'])
def result():
    if request.method== "GET":
        return "You haven't finished the quiz"
    else:
        new_york = request.form['New York']
        california = request.form['California']
        georgia = request.form['Georgia']
        washington = request.form['Washington']
        south_dakota = request.form['South Dakota']
        input_values = {'New York': new_york, 'California': california,'Georgia': georgia, 'Washington': washington,'South Dakota': south_dakota}
        return render_template('result.html', results=show_results(input_values).items())
        


