import logging
from flask import Flask, request, jsonify, render_template, redirect
from flask.helpers import url_for
from flask.wrappers import Response
from data.plotting import create_plot
from Camera.implementation import hsv_camera_feed
PATH_TO_INDEX_PAGE = "../client"
app = Flask(__name__,
            static_url_path="",
            static_folder=PATH_TO_INDEX_PAGE+"/static",
            template_folder=PATH_TO_INDEX_PAGE)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

configuration_settings = [{"hueLow": 0, "hueHigh": 179,
                           "saturationLow": 0, "saturationHigh": 255,
                           "valueLow": 0, "valueHigh": 255}]


@app.route("/")
def start_page():
    return redirect(url_for("index_page"))


@app.route("/app/index")
def index_page():
    return render_template("index.html")


@app.route("/app/dashboard")
def dashboard_page():
    bar = create_plot()
    return render_template("Dashboard.html", plot=bar)


@app.route("/app/configuration")
def configuration_page():
    return render_template("Configuration.html")


@app.route("/api")
def index_API():
    return jsonify("Success")


@app.route("/video/mask")
def mask_video():
    return Response(hsv_camera_feed(configuration_settings),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/api/data", methods=['GET', 'POST'])
def data_API():
    feature = request.args['selected']
    graphJSON = create_plot(feature)
    return graphJSON


@app.route("/api/configuration")
def configuration_API():
    for arg in request.args:
        configuration_settings[0][arg] = int(request.args.get(arg))
    return jsonify(configuration_settings[0])
