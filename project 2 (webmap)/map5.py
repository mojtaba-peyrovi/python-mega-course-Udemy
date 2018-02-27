import folium
import pandas
data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map([46.731922, -117.154244], zoom_start=6, tiles="Mapbox Bright")
fg= folium.FeatureGroup(name="moji's map")

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+ " m", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("map5.html")
