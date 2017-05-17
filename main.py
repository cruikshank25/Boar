from sqlalchemy import create_engine
from bokeh.io import curdoc
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool, LinearColorMapper
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.layouts import *
from bokeh.charts import Histogram, Bar
from bokeh.palettes import *
from config import *
import pandas as pd


#TODO: research potential other connection options within 'sqlalchemy'
class sql_connect:

    engine = create_engine(mysql['connection'], pool_size=20, max_overflow=0)


#TODO: optimize sql queries, get plots to only retrive data from 'source'
class data_fetch:

    df = pd.read_sql_query('SELECT * FROM event LEFT JOIN signature ON event.signature=signature.sig_id '
                           'LEFT JOIN sig_class ON signature.sig_class_id=sig_class.sig_class_id;',
                           sql_connect.engine).drop('sig_class_id', axis=1)

    df2 = pd.read_sql_query('SELECT ip_src,ip_dst FROM iphdr;', sql_connect.engine)

    df3 = pd.read_sql_query('SELECT tcp_sport, tcp_dport FROM tcphdr;', sql_connect.engine)

    df4 = pd.concat([df, df2, df3], axis=1, verify_integrity=True).dropna()

    source = ColumnDataSource(data={'cid': [],
                                    'ip_dst': [],
                                    'ip_src': [],
                                    'sid': [],
                                    'sig_class_name': [],
                                    'sig_gid': [],
                                    'sig_id': [],
                                    'sig_name': [],
                                    'sig_priority': [],
                                    'sig_rev': [],
                                    'sig_sid': [],
                                    'signature': [],
                                    'tcp_dport': [],
                                    'tcp_sport': [],
                                    'timestamp': []})

    source2 = ColumnDataSource(df4)

    def update():

        df = pd.read_sql_query('SELECT * FROM event LEFT JOIN signature ON event.signature=signature.sig_id '
                               'LEFT JOIN sig_class ON signature.sig_class_id=sig_class.sig_class_id;',
                               sql_connect.engine).drop('sig_class_id', axis=1)

        df2 = pd.read_sql_query('SELECT ip_src,ip_dst FROM iphdr;', sql_connect.engine)

        df3 = pd.read_sql_query('SELECT tcp_sport, tcp_dport FROM tcphdr;', sql_connect.engine)

        df4 = pd.concat([df, df2, df3], axis=1, verify_integrity=True).dropna()

        df5 = df4.to_dict(orient='list')

        data_fetch.source.stream(df5, 500)


class themes:

    palette = small_palettes['Spectral'][10]
    palette2 = small_palettes['Spectral'][4]


#TODO: Check colours for 'colormapper'
class timeseriesplot:

    timeseries = figure(title='Alerts by Datetime', x_axis_type='datetime', plot_height=500, plot_width=1100,
                        x_axis_label='Datetime', y_axis_label='Port', toolbar_location='left',
                        toolbar_sticky=False, logo=None)

    timeseries.line(x='timestamp', y='tcp_dport', alpha=0.9, line_width=1, color='deepskyblue', line_dash='dotdash',
                    source=data_fetch.source)

    timeseries.toolbar.logo = None
    timeseries.xgrid.grid_line_alpha = 0.9
    timeseries.ygrid.grid_line_alpha = 0.9

    mapper = LinearColorMapper(palette=['blue', 'yellow', 'orange'])

    timeseries.circle(x='timestamp', y='tcp_dport', fill_color={'field': 'sig_priority', 'transform': mapper},
                      source=data_fetch.source, size=5)

    hover = HoverTool(tooltips=[("Priority", "@sig_priority"), ("Signature", "@sig_name"),
                                ('Classification', '@sig_class_name'), ('Source IP', '@ip_src'),
                                ('Source Port', '@tcp_sport'), ('Destination IP', '@ip_dst'),
                                ('Destination Port', '@tcp_dport'), ('Timestamp', '@timestamp')])

    timeseries.add_tools(hover)


#TODO: get data from 'data_fetch.source' instead
class histogramplot:

    signatures = Histogram(data_fetch.df4, values='cid', color='signature', legend='top_right',
                           xlabel='Event No. (cid)',
                           ylabel='Event Count. (cid)', plot_height=400, plot_width=800,
                           title='Signatures by Event Number',
                           palette=themes.palette, toolbar_location='left', toolbar_sticky=False)

    signatures.toolbar.logo = None

    signatures.ygrid.grid_line_alpha = 0.9


#TODO: get data from 'data_fetch.source' instead
class barplot:

    classifications = Bar(data_fetch.df4, 'sig_class_name', values='cid', legend='top_right', color='sig_class_name',
                          title='Classification Count', ylabel='Event Count. (cid)',
                          xlabel='Classification (sig_class_name)',
                          palette=themes.palette2, toolbar_location='left', toolbar_sticky=False, plot_height=450)

    classifications.toolbar.logo = None

    classifications.ygrid.grid_line_alpha = 0.9


#TODO: get data from 'data_fetch.source' instead
class datatableplot:

    datatable = DataTable(source=data_fetch.source2,
                          fit_columns=True,
                          width=950,
                          height=350,
                          columns=[TableColumn(field='cid', title='Event No.'),
                                   # TableColumn(field='ip_dst', title='Destination'),
                                   TableColumn(field='ip_src', title='Source'),
                                   # TableColumn(field='sid', title='sid'),
                                   TableColumn(field='sig_class_name', title='Classification'),
                                   TableColumn(field='sig_gid', title='Generator'),
                                   TableColumn(field='sig_id', title='Sig ID.'),
                                   TableColumn(field='sig_name', title='Signature'),
                                   TableColumn(field='sig_priority', title='Priority'),
                                   TableColumn(field='sig_rev', title='Revision'),
                                   # TableColumn(field='sig_sid', title='sig_sid'),
                                   # TableColumn(field='signature', title='sig_num'),
                                   TableColumn(field='tcp_dport', title='Destination Port'),
                                   # TableColumn(field='tcp_sport', title='src_port'),
                                   TableColumn(field='timestamp', title='Timestamp')])

class layout:

    layout1 = row(timeseriesplot.timeseries, barplot.classifications)
    layout2 = row(histogramplot.signatures, datatableplot.datatable)


#TODO: find optimal method of sending data to browser
class html_push:

    curdoc().add_periodic_callback(data_fetch.update, 1000)
    curdoc().add_root(layout.layout1)
    curdoc().add_root(layout.layout2)
    curdoc().title = "Snort Alerts"


