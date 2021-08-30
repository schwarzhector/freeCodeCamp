import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

from matplotlib import dates as mpl_dates

print("<< Read the CSV File >>")
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Test if it loaded correctly
print(df.head())
print(df.info())
print(df.describe())

# Parse dates
df['date'] = pd.to_datetime(df['date'])

#Set date as index
df.set_index("date", inplace=True)
print(df.head())


print("<<< Clean the Data >>>")
#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
bottom = df['value'] <= df['value'].quantile(0.025)
top = df['value'] >= df['value'].quantile(0.975)
eliminate = (bottom | top)
df = df.drop(index=df[eliminate].index)
# Test clean DF
print(df.info())


def draw_line_plot():
    print("<<< Draw Line Plot >>>")
    df_line = df.copy()
    # Create a `draw_line_plot` function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png".
    fig, ax = plt.subplots()
    fig.set_figheight(9)
    fig.set_figwidth(12)

    ax.plot_date(df.index, df_line['value'], marker=None, linestyle='solid', color='Red' )

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel('Date')
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    print("<<< Draw Bar Plot >>>")
    # Copy and modify data for monthly bar plot
    # Create a `draw_bar_plot` function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of "Months". On the chart, the label on the x axis should be "Years" and the label on the y axis should be "Average Page Views".
    list_month=['January','February','March','April','May','June','July','August','September','October','November','December']
    df_bar = df.copy()

    df_bar['year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.strftime('%B')
    df_new = df_bar.groupby(['year', 'Month']) 

    df_new['value'].apply(lambda x : x.mean())

    # Draw bar plot
    sns.set_style('ticks')
    sns_style = sns.catplot(x='year', kind='bar', y='value', hue='Month', data=df_bar, hue_order = list_month, ci=None, legend=False)

    fig = sns_style.fig
    ax = sns_style.ax

    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    plt.legend(loc='upper left', title='Month')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    print("<<< Draw Box Plot >>>")
    #* Create a `draw_box_plot` function that uses Searborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of the second chart should be "Month-wise Box Plot (Seasonality)". Make sure the month labels on bottom start at "Jan" and the x and x axis are labeled correctly.

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize=(9,12), dpi=70)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax[0]).set(xlabel='year', ylabel='Page Views', title='Year-wise Box Plot (trending')

    sns.boxplot(x='month', y='value', data=df_box.loc[~df_box.year.isin([2016, 2019]), :]).set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (season)')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
