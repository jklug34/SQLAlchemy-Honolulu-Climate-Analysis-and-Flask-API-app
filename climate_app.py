import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker


from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#session = Session(engine)
session = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/<br/>"
        f"/api/v1.0/start/end/"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Convert the query results to a Dictionary using `date` as the key and `prcp` as the value."""
    # Query Measurement
    results = session.query(Measurement.id, Measurement.station, Measurement.date, Measurement.prcp, Measurement.tobs).all()

    # Create a dictionary from the row data and append to a list of precipitation
    precipitation = []
    for id, station, date, prcp, tobs in results:
        precipitation_dict = {}
        precipitation_dict["id"] = id
        precipitation_dict["station"] = station
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation_dict["tobs"] = tobs
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)



@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all stations"""
    # Query all stations
    results = session.query(Measurement.station).group_by(Measurement.station).all()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    """query for the dates and temperature observations from a year from the last data point."""
    """Return a JSON list of Temperature Observations (tobs) for the previous year."""
    # Query all dates and temp obs over the last year
    last_date = dt.date(2017, 8, 23)
    last12months = last_date - dt.timedelta(days=365)
    sel = [Measurement.station, Measurement.date, Measurement.tobs]
    results = session.query(*sel).filter(Measurement.date >= last12months).order_by(Measurement.date).all()
    
    # Convert list of tuples into normal list
    all_temp_obs_last_year = list(np.ravel(results))

    return jsonify(all_temp_obs_last_year)


@app.route("/api/v1.0/start/<start>")
def min_avg_max_by_start_date(start):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    # Create a dictionary from the row data and append to a list of normals
    normals = []
    for min, avg, max in results:
        normals_dict = {}
        normals_dict[0] = min
        normals_dict[1] = avg
        normals_dict[2] = max
        normals.append(normals_dict)

    return jsonify(normals)

    canonicalized = start.replace(" ", "").lower()
    for result in results:
        search_term = result["start"].replace(" ", "").lower()

        if search_term == canonicalized:
            return jsonify(result)
        
    return jsonify({"error": f"Date with start {start} not found."}), 404


@app.route("/api/v1.0/start/end/<start>/<end>")
def min_avg_max_by_start_end_date(start, end):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Create a dictionary from the row data and append to a list of normals
    normals_start_end = []
    for min, avg, max in results:
        normals_start_end_dict = {}
        normals_start_end_dict[0] = min
        normals_start_end_dict[1] = avg
        normals_start_end_dict[2] = max
        normals_start_end.append(normals_start_end_dict)

    return jsonify(normals_start_end)

    canonicalized = start.replace(" ", "").lower()
    canonicalized = end.replace(" ", "").lower()
    for result in results:
        search_term = result["start"].replace(" ", "").lower()
        search_term = result["end"].replace(" ", "").lower()

        if search_term == canonicalized:
           return jsonify(result)
        
    return jsonify({"error": f"Date with start {start} or end {end} not found."}), 404



if __name__ == '__main__':
    app.run(debug=True)