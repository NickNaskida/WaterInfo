from flask import Flask, render_template, redirect, url_for

import folium
from folium.plugins import LocateControl
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import ValidationError

from services import get_cords
from forms import SourceForm


app = Flask(__name__)
app.config['SECRET_KEY'] = "i32utohmc328m&*5m(M)#%m0g23m29083mgs"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Models
class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))

    def __repr__(self):
        return f'{self.info}'


# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    form = SourceForm()

    if form.validate_on_submit():
        address = form.address.data
        info = form.info.data
        try:
            cords = get_cords(address)
            new_marker = Marker(
                info=info,
                latitude=cords[0],
                longitude=cords[1]
            )
            db.session.add(new_marker)
            db.session.commit()
            return redirect(url_for('water_map'))
        except:
            raise ValidationError(f"Address - {address} does not exist.")

    return render_template('index.html', form=form)


@app.route('/map')
def water_map():
    markers = Marker.query.all()
    folium_map = folium.Map()
    LocateControl(True).add_to(folium_map)

    for i in markers:
        folium.CircleMarker(
            location=[i.latitude, i.longitude],
            radius=20,
            popup=i.info,
            color="#0084FF",
            fill=True,
            fill_color="#0084FF",
        ).add_to(folium_map)

    return folium_map._repr_html_()


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=False)
