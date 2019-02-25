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
    