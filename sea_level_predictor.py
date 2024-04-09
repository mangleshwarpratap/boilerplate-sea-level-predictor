import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level', color='blue')

    slope, intercept, _ , _ , _ = linregress( df['Year'], df['CSIRO Adjusted Sea Level'] )
    # Create first line of best fit

    # y = mx + c      # the straight line equation
    plt.plot(df['Year'], slope * df['Year'] + intercept, color='red', label='Line of Best Fit')


    predicted_sea_level_2050 = slope * 2050 + intercept
    plt.plot([df['Year'].min(), 2050], [intercept, predicted_sea_level_2050], '--', color='green', label='Prediction for 2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (mm)')
    plt.title('Sea Level Rise Over Time')
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

    # Create second line of best fit
    df_filtered = df[df['Year'] >= 2000]

    # Perform linear regression on filtered data
    slope, intercept, _, _, _ = linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])

    # Predict sea level rise in 2050
    predicted_sea_level_2050 = slope * 2050 + intercept

    # Plot scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Sea Level Data')

    # Plot new line of best fit from year 2000 to 2050
    plt.plot([2000, 2050], [slope * 2000 + intercept, predicted_sea_level_2050], color='red', label='Line of Best Fit (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (mm)')
    plt.title('Sea Level Rise Over Time')
    plt.legend()

    # Show plot
    plt.grid(True)
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()