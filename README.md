# ricardo-sandbox 

## App 1 - Southern Ocean Wave-buoy data:
  
  Develop an App that displays the Southern Ocean Wave Buoy timeseries for Significant Wave Height and Maximum Wave Height in the same plot, Peak Wave Period on a second axis, in the same plot as well. The Wave buoy data can be aquired from [Oceanum.io] Datamesh, requires signup and you can use the [oceanum-python](https://github.com/oceanum-io/oceanum-python) library to fetch the data.
  The graphs must be well formatted, with Time in UTC in the X-axis and variables in the Y-axis. In the Axis title or at the graph legends must be displayed the variable units (Wave height in meters and Wave Period in seconds).

The concepts explored in this exercice are:

1. Fetching data from a remote API
2. Streamlit App development
3. Data inspection and XArray/CF-Convention format
4. Plotting timeseries data
5. (bonus) Plot all the buoy's position in a map as dots where the position are represented by a coloured circle and the circle's colour is the maximum wave height.



