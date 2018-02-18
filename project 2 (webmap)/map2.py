import folium
map = folium.Map([46.731922, -117.154244], zoom_start=6, tiles="Mapbox Bright")
fg= folium.FeatureGroup(name="moji's map")
fg.add_child(folium.Marker(location=[47.678072, -117.414563], popup="Here is Spokane", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("map2.html")
