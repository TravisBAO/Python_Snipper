import pandas
import plotly.express as px


def line_chart_by_name():
    df = pandas.read_csv('BrawlStars.csv')
    fig = px.line(df, x="Date", y="Trophies", color='Name', title='Hero Trophies Trend',
                  hover_data=['Name'])
    fig.show()

