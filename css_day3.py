# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Line plot
Line plots are suitable for showing trends over time or a sequence. They help visualize patterns and changes in a variable over a continuous interval. They are useful for time series data or data with a natural ordering.
1. Matplotlib
2. plotly
"""


### Using matplotlib

"""import matplotlib.pyplot as plt

react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200,220, 240, 260]

plt.plot(temp,react_conv)
plt.xlabel("temperature")
plt.ylabel("reaction conversion")
plt.title("chemical experiment")

plt.show()


import plotly.express as px
react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200,220, 240, 260]

fig = px.line(x=temp, y=react_conv, labels={'x': 'temperature', 'y': 'reaction conversion'}, title='chemical experiment')
fig.write_html("plot.html")
###chech it under the file project(plot)
"""
# import matplotlib.pyplot as plt
# day1_attendees = [70, 20, 64, 90, 80]
# day1_names = ["blessing", "mali", "pangi", "tafi", "shini"] 
# plt.bar(day1_names, day1_attendees)
# plt.show()


"""
import matplotlib.pyplot as plt

x_line = [1, 2, 3, 4, 5];
y_line = [2, 4, 6, 8, 10];


plt.plot(x_line, y_line, '-o')
plt.xlabel("x_line")
plt.ylabel("y_line")

plt.title('Line Plot')
plt.show()


##plotly
import plotly.express as px

x_line = [1, 2, 3, 4, 5]
y_line = [2, 4, 6, 8, 10]

fig = px.line(x=x_line, y=y_line, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Line Plot')
fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")

##############################################
# """
# Bar Plot
# Bar charts are effective for visualizing the distribution of categorical variables. They help compare the frequencies or proportions of different categories. They are useful for exploring the distribution of a categorical variable, such as the count of observations in different groups.

# 1. Matplotlib
# 2.plotly
# """
"""
import matplotlib.pyplot as plt

x_bar = ['A', 'B', 'C', 'D']
y_bar = [1, 2, 3, 4]

plt.bar(x_bar, y_bar)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
plt.show()



import plotly.express as px

x_bar = ['A', 'B', 'C', 'D']
y_bar = [1, 2, 3, 4]
fig = px.bar(x=x_bar, y=y_bar, labels={'x': 'Categories', 'y': 'Values'}, title='Bar Plot')
fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")

##############################
"""
# Scatter plot
# Scatter plots visualize the relationship between two numerical variables. They help identify patterns, correlations, and potential outliers. They are useful for exploring the correlation between variables and identifying trends or clusters.

# import matplotlib.pyplot as plt

# x_scatter = [1, 2, 3, 4, 5]
# y_scatter = [2, 4, 6, 8, 10]

# plt.scatter(x_scatter, y_scatter)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Scatter Plot Example')
# plt.show()


"""
import plotly.express as px

x_scatter = [1, 2, 3, 4, 5]
y_scatter = [2, 4, 6, 8, 10]

fig = px.scatter(x=x_scatter, y=y_scatter, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Scatter Plot')
fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")


######################
"""
# Histogram Plot
# Histograms provide a visual representation of the distribution of a single variable. They help in understanding the central tendency, spread, and shape of the data. They are useful for exploring the distribution of numerical variables, such as age, income, or any continuous variable.



# import matplotlib.pyplot as plt

# x_histogram = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# plt.hist(x_histogram, bins=range(min(x_histogram), max(x_histogram) + 1), edgecolor='black')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram Example')
# plt.show()


# import plotly.express as px

# x_histogram = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# fig = px.histogram(x=x_histogram, labels={'x': 'Values'}, title='Histogram')
# fig.write_html("plot.html")

# # This is used to automatically open up a browser of your plot
# import webbrowser
# webbrowser.open("plot.html")

"""
#####################
"""
# Maps
# Map plots are visualizations that use geographical maps to represent data spatially. These plots are particularly useful when dealing with data that has a geographic component, such as regional sales, population distribution, or any information tied to specific locations.
"""
data = px.data.gapminder()

# Create a choropleth world map
fig = px.choropleth(
    data_frame=data,
    locations="iso_alpha",
    color="gdpPercap",
    hover_name="country",
    animation_frame="year",
    title="World Map Choropleth",
    color_continuous_scale=px.colors.sequential.Plasma,
    projection="natural earth"
)

"""

#################
"""
Combining codes
"""

import plotly.express as px
import webbrowser

df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x="year", y="lifeExp", color='country')
fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
webbrowser.open("plot.html")

# import pandas

# file = pandas.read_csv('country_data.csv')

# print(file)

# print(file.info())

# print(file.describe())


















