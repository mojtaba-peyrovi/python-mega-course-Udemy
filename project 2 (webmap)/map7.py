import folium
import pandas
data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
def colorChange(elevation):
    if elevation < 1000:
        return '#00cc00'
    elif 1000 <= elevation < 1500:
        return '#ff6600'
    else:
        return '#ff3300'

map = folium.Map([46.731922, -117.154244], zoom_start=6, tiles="Mapbox Bright")
fg= folium.FeatureGroup(name="moji's map")
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], numberpopup=str(el)+ " m", radius=10 , color='grey', fill=True, fill_color=colorChange(el), fill_opacity = 0.9))


map.add_child(fg)
map.save("map7.html")
