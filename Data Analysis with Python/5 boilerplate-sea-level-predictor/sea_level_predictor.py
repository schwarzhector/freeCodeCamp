import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

  # Read data from file
  data_df = pd.read_csv('epa-sea-level.csv')
  x= data_df['Year']
  y= data_df['CSIRO Adjusted Sea Level']
  

  # Create scatter plot
  fig, ax1 = plt.subplots()
  plt.scatter(x,y)

  # Create first line of best fit
  regression = linregress(x,y)
  x_prediction = pd.Series([i for i in range(1880,2051) ])
  y_prediction = regression.slope*x_prediction + regression.intercept
  plt.plot(x_prediction, y_prediction, color='green')
  
  # Create second line of best fit
  second_fit = data_df.loc[data_df['Year'] >= 2000]
  second_x = second_fit['Year']
  second_y = second_fit['CSIRO Adjusted Sea Level']
  second_regression = linregress(second_x,second_y)
  x_2_prediction = pd.Series([i for i in range(2000,2051) ])
  y_2_prediction = second_regression.slope*x_2_prediction + second_regression.intercept
  plt.plot(x_2_prediction, y_2_prediction, color='red')

  # Add labels and title
  ax1.set_xlabel('Year')
  ax1.set_ylabel('Sea Level (inches)')
  ax1.set_title('Rise in Sea Level')
    
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()