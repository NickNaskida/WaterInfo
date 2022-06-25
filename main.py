from flask import Flask, render_template

import folium
from folium.plugins import LocateControl

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/map')
def water_map():
    folium_map = folium.Map()
    LocateControl(True).add_to(folium_map)
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
