import os, sys, glob
import json
import xarray as xr
import pandas as pd
from flask import Flask, request, render_template
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
from datetime import datetime

# URL http://127.0.0.1:5003/board?question=anw 
app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/board2')
def board2():
    return "그냥 보드"

@app.route("/board")
def board_list():
    return f"question 변수의 값은 {request.args.get('question')}"

@app.route("/input")
def input():
    #fn = 'A2082800.nc'
    #ds = xr.open_dataset(fn)
    #varList = list(ds.keys())
    varList = ['backscatter', 'software_level', 'message_number', 'message_subclass', 
               'vertical_visibility', 'cbh_1', 'cbh_2', 'cbh_3', 
               'highest_signal', 'status_alarm', 'status_warning', 
               'status_internal', 'vertical_resolution', 'sky_detection_status', 
               'pulse_energy', 'laser_temperature', 'window_transmission', 
               'tilt_angle', 'background_light', 'pulse_count',                 
               'backscatter_sum', 'layer_height', 'layer_cloud_amount']
    today = datetime.now()
    today = "%s-%s-%s" % (today.year, today.month, today.day)
    return render_template("input.html",varList=varList, today=today)

@app.route("/search", methods=["POST"])
def search():
    date = request.form.get("date") 
    vars = request.form.get("vars")
    cdate = pd.to_datetime(date)
    yr = cdate.strftime("%Y")
    mo = cdate.strftime("%m")
    dy = cdate.strftime("%d")
    y1 = yr[0:1]
    fn = "A%s%s%s00.nc" % (y1,mo,dy)
    fn = "A2082800.nc"
    pid = random.randint(0, 1000)
    gn = os.path.join(app.config['UPLOAD_FOLDER'], '%s.png' % pid)
    #flist = glob.glob(os.path.join(app.config['UPLOAD_FOLDER'],'*'))
    #if len(flist) > 10: 
    #    os.remove(os.path.join(app.config['UPLOAD_FOLDER'],'*'))
    ds = xr.open_dataset(fn)
    fig, ax = plt.subplots(figsize=(12,6))
    cvar = ds[vars]
    cvar = cvar.T
    cvar.plot(ax=ax)
    plt.savefig(gn)
    plt.close()
    
    return render_template("display.html", form=gn)
    #return render_template("test.html", flist=flist)

app.run(host="localhost",port=5003, debug=True)
