
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models.widgets import Dropdown
from bokeh.io import curdoc
from bokeh.layouts import column

from bokeh.models import BooleanFilter, CDSView, Select, Range1d, HoverTool
from bokeh.palettes import Category20
from bokeh.models.formatters import NumeralTickFormatter


import tickerHist

# Read data into a pandas object


def get_symbol_df(symbol=None, data=None):
    '''
    parameters: ticker symbol as string, candle data
    returns a pandas dataframe object with the data
    '''
    # df = pd.DataFrame(pd.read_csv(symbol + 'ticker.csv'))
    df = pd.DataFrame(data)
    df.reset_index(inplace=True)
    # print(df[:4])
    return df


# plot basic stock prices


def plot_stock_price(stock):
    p = figure(plot_width=W_PLOT, plot_height=H_PLOT, tools=TOOLS,
               title="Stock price", toolbar_location='above')

    inc = stock.data['close'] > stock.data['open']
    dec = stock.data['open'] > stock.data['close']
    view_inc = CDSView(source=stock, filters=[BooleanFilter(inc)])
    view_dec = CDSView(source=stock, filters=[BooleanFilter(dec)])

    # p.segment(x0='index', x1='index', y0='Low', y1='High',
    #           color=RED, source=stock, view=view_inc)
    # p.segment(x0='index', x1='index', y0='Low', y1='High',
    #           color=GREEN, source=stock, view=view_dec)

    p.vbar(x='index', width=VBAR_WIDTH, top='open', bottom='close', fill_color=BLUE, line_color=BLUE,
           source=stock, view=view_inc, name="price")
    p.vbar(x='index', width=VBAR_WIDTH, top='open', bottom='close', fill_color=RED, line_color=RED,
           source=stock, view=view_dec, name="price")

    p.legend.location = "top_left"
    p.legend.border_line_alpha = 0
    p.legend.background_fill_alpha = 0
    p.legend.click_policy = "mute"

    return p


# Define constants
W_PLOT = 1500
H_PLOT = 600
TOOLS = 'pan,wheel_zoom,reset'

VBAR_WIDTH = 0.2
RED = Category20[7][6]
GREEN = Category20[5][4]

BLUE = Category20[3][0]
BLUE_LIGHT = Category20[3][1]

ORANGE = Category20[3][2]
PURPLE = Category20[9][8]
BROWN = Category20[11][10]

# create bokeh column object
stock = ColumnDataSource(
    data=dict(datetime=[], open=[], close=[]))

symbol = 'GLD'
# fetch symbol candle data form thinkorswim API:
symbol_candle_data = tickerHist.create_ticker_candles_dict(symbol)
# store data into a pandas dataframe object:
df = get_symbol_df(symbol, symbol_candle_data)
# create bokeh column object with data
stock.data = stock.from_df(df)
elements = list()

# update_plot()
p_stock = plot_stock_price(stock)

elements.append(p_stock)

curdoc().add_root(column(elements))
curdoc().title = 'Bokeh stocks historical prices'
