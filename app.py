"""
Flask app for the 2nd challenge in the CEE pool.
"""
from StringIO import StringIO

import datetime
import pandas as pd
import gspread

from flask import Flask
from flask import render_template
from oauth2client import service_account as sc

from .secret import secret_file

app = Flask(__name__)

def get_alumni():
    """Obtains the formatting object for alumni lists"""
    sht = get_connection()
    alumni = pd.read_csv(StringIO(sht.export()))
    alumni["idx"] = alumni.index + 2
    alumni = alumni.fillna("")
    alumni = alumni.T.to_dict().values()
    return alumni

def get_connection():
    """Get the connection for the google sheet"""
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = sc.ServiceAccountCredentials.from_json_keyfile_name(secret_file, scope)
    googleconnection = gspread.authorize(credentials)
    sht = googleconnection.open("GTC-CEE").sheet1
    return sht

def update_review_date(idx):
    last_review_col = 3
    sht = get_connection()
    sht.update_cell(idx, last_review_col, datetime.date.today())
    return


@app.route("/")
def index():
    """Homepage of the alumni list"""
    alumni = get_alumni()
    return render_template("index.html", alumni=alumni)

@app.route("/update/<int:idx>")
def update(idx):
    """Updates the Last Review date of the idx'th row"""
    update_review_date(idx)
    return "{'status':'success'}"

@app.route("/group/<string:cohort>")
def groups(cohort):
    """Updates the Last Review date of the idx'th row"""
    alumni = get_alumni()
    alumni = [alum for alum in alumni if alum["cohort"].lower() == cohort.lower()]
    return render_template("index.html", alumni=alumni)
