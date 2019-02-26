### Data visualization by Bokeh:
---

There are three ways we can generate bokeh visualization (3 interfaces): 

1- bokeh.models: low level. mostly designed for developers. You need to write a lot of code.
2- bokeh.plotting: Medium level interface. you have lots of room for customizing, adjusting.
3- bokeh.charts: high level interface.

Plotting interface is the best way to do it. 

- first lets start with bokeh.charts: (deprecated)

we can see the code at the jupyter notebook called scatter_plotting.ipynb. 
p.triangle() can be replaced by p.circle() or square() or other shapes.

for pasing the size of the shapes, we can have different sizes. we should pass a list of sizes for each point.
```
p.triangle([1,2,4], [5,3,2], size=[12,54,2], color='red')
```
Also we can double any value in a list and pass them as the sizes:
```
p.triangle([1,2,4], [5,3,2], size[i*2 for i in [12,54.2]], color='red)
```

In order to add more customization to the chart, instead of passing parameters directly to the p instance, we can call them as attributes. for example:
```
p.title = 'Earthquake'
```
instead of:
```
p.figure(..., title='Earthquake', ....)
```
  
- In order to have Bokeh run faster on the browser, we can download the css, and js CDN of bokeh and reference them locally so that it doesn't pull these files from the server each time the page loads.

Bokeh can do this automatically, when we pass an argument in output_file() like this:
```
output_file("file_name", mode="relative")
``` 
by default mode is CDN. There are other modes such as absolute and inline.

- we can also pass tools="" which removes all the toolbar when the graph runs in the browser.
- also with logo=None we can remove bokeh logo from the chart.

- we can pass the tools we want such as pan, resize, etc. as tool parameter passed in figure.
```
fogure(plot_width-500, plot_height=500, tools='pan, resize', logo=None)
```

#### Time Series:__ 
For times series we use p.line instead of circle or other types.

Then we load data by pandas and pass them into p.

- In order to make the chart responsive, we can pass it to graph()
```
p = figure(..., sizing_mode="scale_both")
```


