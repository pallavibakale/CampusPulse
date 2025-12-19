import base64
from io import BytesIO

from pandas import DataFrame
import matplotlib
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator

matplotlib.use('agg')

def create_plot(df, plot_func, xlabel, title, ylabel: str|None=None, y_major_locator: int|None=None, only_six=True)-> str:
    # If there are more than 6 unique values in the DataFrame, group all but the top 5 into 'Others'
    if only_six and df[xlabel].nunique() > 6:
        # Get the top 5 categories
        top_categories = df[xlabel].value_counts().index[:5]
        # Replace all other categories with 'Others'
        df.loc[~df[xlabel].isin(top_categories), xlabel] = 'Others'

    fig = Figure()
    ax = fig.subplots()
    
    if ylabel:
        plot_func(x=xlabel, data=df, y=ylabel, ax=ax, color="#cfb991")
    else:
        plot_func(x=xlabel, data=df, ax=ax, color="#cfb991")
    
    if y_major_locator:
        ax.yaxis.set_major_locator(MultipleLocator(y_major_locator))
    
    ax.set_title(title)
    buffer = BytesIO()
    fig.savefig(buffer, format="png")
    data = base64.b64encode(buffer.getbuffer()).decode("utf-8")
    return data

def count_plot(queryset, xlabel: str, title: str, y_major_locator: int|None=None)-> str:
    df = DataFrame(queryset, columns=[xlabel])
    return create_plot(df=df, plot_func=sns.countplot, xlabel=xlabel, title=title, y_major_locator=y_major_locator)

def hist_plot(queryset, xlabel: str, title: str):
    df = DataFrame(queryset, columns=[xlabel])
    return create_plot(df=df, plot_func=sns.histplot, xlabel=xlabel, title=title, only_six=False)

def bar_plot(queryset, xlabel: str, title: str, y_major_locator: int|None=None)-> str:
    df = DataFrame(queryset)
    return create_plot(df=df, plot_func=sns.barplot, xlabel=xlabel, title=title, ylabel="Total Points", y_major_locator=y_major_locator)