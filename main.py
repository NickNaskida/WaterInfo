from flask import Flask, render_template, redirect, url_for, request

import folium
from folium.plugins import LocateControl
from flask_sqlalchemy import SQLAlchemy


from forms import SourceForm, LackForm


app = Flask(__name__)
app.config['SECRET_KEY'] = "i32utohmc328m&*5m(M)#%m0g23m29083mgs"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Models
class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    info = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))

    def __repr__(self):
        return f'{self.info}'


# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    lack_form = LackForm()
    source_form = SourceForm()

    if lack_form.validate_on_submit() and 'lack_form' in request.form:
        info = lack_form.info.data
        latitude = lack_form.latitude.data
        longitude = lack_form.longitude.data

        try:
            new_marker = Marker(
                type="lack",
                info=info,
                latitude=latitude,
                longitude=longitude
            )
            db.session.add(new_marker)
            db.session.commit()
            return redirect(url_for('water_map'))
        except Exception as e:
            print(e)
            return redirect(url_for('water_map'))

    if source_form.validate_on_submit() and 'source_form' in request.form:
        info = source_form.info.data
        latitude = source_form.latitude.data
        longitude = source_form.longitude.data

        try:
            new_marker = Marker(
                type="source",
                info=info,
                latitude=latitude,
                longitude=longitude
            )
            db.session.add(new_marker)
            db.session.commit()
            return redirect(url_for('water_map'))
        except Exception as e:
            print(e)
            return redirect(url_for('water_map'))

    return render_template('index.html', lack_form=lack_form, source_form=source_form)


@app.route('/map')
def water_map():
    source_markers = Marker.query.filter(Marker.type == "source")
    lack_markers = Marker.query.filter(Marker.type == "lack")
    folium_map = folium.Map()
    LocateControl(True).add_to(folium_map)

    for i in source_markers:
        folium.CircleMarker(
            location=[i.latitude, i.longitude],
            radius=10,
            popup=i.info,
            color="#0084FF",
            fill=True,
            fill_color="#0084FF",
        ).add_to(folium_map)

    for i in lack_markers:
        folium.CircleMarker(
            location=[i.latitude, i.longitude],
            radius=10,
            popup=i.info,
            color="crimson",
            fill=True,
            fill_color="crimson",
        ).add_to(folium_map)

    return folium_map._repr_html_()


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=False)
