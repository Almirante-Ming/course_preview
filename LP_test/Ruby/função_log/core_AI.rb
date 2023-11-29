require 'asciicharts'

data = [[1, 2], [2, 3], [3, 1], [4, 2], [5, 3]]

# Create a Cartesian chart with the data
chart = AsciiCharts::Cartesian.new(data, type: :scatter)

# Draw the chart
puts chart.draw
