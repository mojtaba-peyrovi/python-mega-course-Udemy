import folium
import pandas
data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
map = folium.Map([46.731922, -117.154244], zoom_start=6, tiles="Mapbox Bright")
fg= folium.FeatureGroup(name="moji's map")

for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="Here is Spokane", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("map4.html")
