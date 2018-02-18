import folium
map = folium.Map([46.731922, -117.154244], zoom_start=6, tiles="Mapbox Bright")
fg= folium.FeatureGroup(name="moji's map")
for coordinates in [[47.678072, -117.414563],[47.672333, -117.236556]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Here is Spokane", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("map3.html")
