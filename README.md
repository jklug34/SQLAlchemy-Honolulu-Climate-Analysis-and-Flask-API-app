# SQLAlchemy-Honolulu-Climate-Analysis-and-Flask-API-app
Analysis of  Honolulu, Hawaii climate in  SQLAlchemy/Python along with the creation of a flexible trip date Flask API weather app



- Total Precipitation in Honolulu, Hawaii (08/23/2016 - 08/23/2017).
![Total_Precip_Hawaii_year](https://user-images.githubusercontent.com/48166327/60390825-23ebbd00-9a94-11e9-8e30-a0b42b252fd9.png)



- Histogram of Temperatures in Honolulu, Hawaii (08/18/2016 - 08/18/2017). Most common temperature is 75 F with a range of 60 to 85 F. 

![temperature_histogram](https://user-images.githubusercontent.com/48166327/60390828-28b07100-9a94-11e9-9548-dbcf6ef8fc5d.png)



- Average 14 Day Trip Temperature (01/01/2016 - 01/14/2016) (Error bars represent min-max ranges).

![Trip_Avg_Temp](https://user-images.githubusercontent.com/48166327/60390830-2b12cb00-9a94-11e9-97ba-d56aabf52562.png)



- Trip Temperature Normals (Minimum, Average, Maximum) Area Plot from 01-01-2016 to 01-14-2016.

![Area_plot_temp_normals_over_vacation](https://user-images.githubusercontent.com/48166327/60390831-2f3ee880-9a94-11e9-9525-16d43888bccd.png)





Climate.py Flask API

Use google chrome. Output json libraries.

Endpoints
Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/start/(input date trip start date here, e.g. "2017-01-01")
        /api/v1.0/start/end/(input date trip start date here, e.g. "2017-01-01")/(input date trip end date here, e.g. "2017-01-14")

