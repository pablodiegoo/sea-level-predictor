import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    lr = linregress(x, y)
    
    xf = pd.Series(range(1880, 2051))
    yf = linregress(x, df['CSIRO Adjusted Sea Level']).intercept + linregress(x, df['CSIRO Adjusted Sea Level']).slope*xf

    plt.plot(x, lr.intercept + lr.slope*x, 'r', label='fitted line')
    
    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']

    lr2 = linregress(x2, y2)

    x2 = pd.Series(range(2000, 2051))
    y2 = lr2.slope*x2 + lr2.intercept
    plt.plot(x2, y2, 'g', label='fitted line 2000-2050')
    
    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()