# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


import plotly.graph_objects as go
import pandas as pd
from datetime import date

df = pd.DataFrame({
    "Primary volunteer": ["Viktor", "Viktor", "Julia"],
    "Secondary volunteer": ["Julia", 'Julia', 'Viktor'],
    "Country": ["Poland", "Poland", "Germany"],
    "Language": ["PL", "ENG", 'GER'],
    "Group category": ["Yoga", "Spirituality", "Yoga"],
    "Group name": ["Group 1", "Group 2", "group 3"],
    "Group url": ['https://facebook.com/group/1', 'https://facebook.com/group/2', 'https://facebook.com/group/3'],
    "Allows ads": ["Yes", "No", "Yes"],
    'Group size': [201, 25000, 100000],
    "Week": [1, 1, 2],
    "Content type": ["YT", "Blog", "YT"],
    "Content category": ["Yoga", "Spirituality", "IEO Ad"],
    "Content name": ["What is yoga", "Another video", "Inner engineering"],
    "Content url": ["https://isha.sadhguru.org/yoga/new-to-yoga/what-is-yoga/",
                    "https://www.youtube.com/watch?v=ZCe0mNsLGus", "https://www.youtube.com/watch?v=goQNpV5LqR4"],
    "Bitly url": ["bit.ly/34CUM6a", "bit.ly/3lop96r", "bit.ly/3lrnNYL"],
    "Bitly generation timestamp": [date.today(), date.today(), date.today()],
    "Link to fb post": ['https://facebook.com/post/1', 'https://facebook.com/post/2', 'https://facebook.com/post/3'],
    "Date commented": [date.today(), date.today(), date.today()],
    "Clicks": [15, 60, 46]
})
df['Impressions'] = df['Group size'] * 0.025
df['Impressions'] = df['Impressions'].round(0)

countries_list = df['Country'].unique()
languages_list = df['Language'].unique()
group_categories_list = df['Group category'].unique()
weeks_list = df['Week'].unique()

group_info_columns = ['Week', 'Country', 'Language', 'Group category', 'Group name', 'Group url',
                      'Allows ads', 'Group size', 'Clicks', 'Impressions']

last_week = df['Week'].max

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import plotly.express as px
from dash.dependencies import Output, Input

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


app.layout = html.Div([
    html.H1('Share&Nurture Dashboard'),

    html.Div([
        dcc.Graph(id="main-dashboard"),

        html.Div([
            html.Label('Select country:'),

            dcc.Dropdown(
                id="main-dashboard-country-dropdown",
                options=[{'label': i, 'value': i} for i in countries_list],
                value=countries_list,
                multi=True)
        ], style={'width': '25%'}),


        html.Div([
            html.Label('Select group category:'),

            dcc.Dropdown(
                id="main-dashboard-group-category-dropdown",
                options=[{'label': i, 'value': i} for i in group_categories_list],
                value=group_categories_list,
                multi=True)
        ], style={'width': '25%'}),

        html.Div([
            html.Label('Select weeks:'),

            dcc.Dropdown(
                id="main-dashboard-week-dropdown",
                options=[{'label': i, 'value': i} for i in weeks_list],
                value=weeks_list,
                multi=True)
        ], style={'width': '25%'})
    ]),

    html.Br(),
    html.Br(),

    html.H4('Group data:'),

    html.Div([
        dt.DataTable(
            id='group-data',
            columns=[{"name": i, "id": i} for i in group_info_columns]),
    ], style={"width": "95%"}),

    html.Div([
        html.Div([
            html.Label('Select country:'),

            dcc.Dropdown(
                id="group-data-country-dropdown",
                options=[{'label': i, 'value': i} for i in countries_list],
                value=countries_list,
                multi=True)
        ], style={"width": "25%"}),

        html.Div([
            html.Label('Select language:'),

            dcc.Dropdown(
                id="group-data-group-language-dropdown",
                options=[{'label': i, 'value': i} for i in languages_list],
                value=languages_list,
                multi=True)
        ], style={"width": "25%"}),

        html.Div([
            html.Label('Select group category:'),

            dcc.Dropdown(
                id="group-data-group-category-dropdown",
                options=[{'label': i, 'value': i} for i in group_categories_list],
                value=group_categories_list,
                multi=True)
        ], style={"width": "25%"}),

        html.Div([
            html.Label('Select weeks:'),

            dcc.Dropdown(
                id="group-data-weeks-dropdown",
                options=[{'label': i, 'value': i} for i in weeks_list],
                value=weeks_list,
                multi=True)
        ], style={"width": "25%"}),
    ]),

    html.Div([
        dcc.Graph(
            id='country-graph')
    ], style={"width": "95%"}),

    html.Div([
        html.Label('Select country:'),

        dcc.Dropdown(
            id="country-graph-country-dropdown",
            options=[{'label': i, 'value': i} for i in countries_list],
            value=countries_list,
            multi=True)
    ], style={"width": "25%"}),

    html.Div([
        html.Label('Select language:'),

        dcc.Dropdown(
            id="language-dropdown",
            options=[{'label': i, 'value': i} for i in languages_list],
            value=languages_list,
            multi=True)
    ], style={"width": "25%"}),

    html.Br(),
    html.Br(),

    html.Div([
        dcc.Graph(
            id='content-graph')
    ], style={"width": "95%"}),

    html.Div([
        html.Label('Select order:'),
        dcc.RadioItems(
            id="order-radio",
            options=[{'label': i, 'value': i} for i in ['ascending', 'descending']],
            value='descending')
    ], style={"width": "25%"}),

    html.Div([
        dcc.Graph(
            id='category-graph')
    ], style={"width": "95%"}),

    html.Div([
        dcc.Dropdown(
            id="category-graph-country-dropdown",
            options=[{'label': i, 'value': i} for i in countries_list],
            value=countries_list,
            multi=True)
    ], style={'width': '25%'})
])


@app.callback(
    Output("main-dashboard", 'figure'),
    Input("main-dashboard-country-dropdown", 'value'),
    Input("main-dashboard-group-category-dropdown", 'value'),
    Input("main-dashboard-week-dropdown", 'value'))
def update_main_dashboard(countries, group_categories, weeks):
    if not countries:
        return {}

    dff = df[df['Country'].isin(countries)]
    dff = dff[dff['Group category'].isin(group_categories)]
    dff = dff[dff['Week'].isin(weeks)]
    if dff.empty:
        return {}


    main_dashboard = go.Figure()

    main_dashboard.add_trace(go.Indicator(
        title="total bitlinks posted",
        mode="number",
        value=dff.copy()["Bitly url"].count(),
        domain={'row': 0, 'column': 0}))

    main_dashboard.add_trace(go.Indicator(
        title="total clicks on bitlinks",
        mode="number",
        value=dff.copy().get('Clicks').sum(),
        domain={'row': 1, 'column': 0}))

    main_dashboard.add_trace(go.Indicator(
        title="average clicks per bitlink",
        mode="number",
        value=dff.copy().get('Clicks').mean(),
        domain={'row': 0, 'column': 1}))

    main_dashboard.add_trace(go.Indicator(
        title="total IEO Ad clicks",
        mode="number",
        value=dff.copy()[dff["Content category"] == 'IEO Ad']['Clicks'].sum(),
        domain={'row': 1, 'column': 1}))

    main_dashboard.add_trace(go.Indicator(
        title="total impressions",
        mode="number",
        value=dff.copy()["Impressions"].sum(),
        domain={'row': 1, 'column': 2}))

    # main_dashboard.add_trace(go.Indicator(
    #     title="total IEO Ads posted",
    #     mode="number",
    #     value=dff.copy()[dff["Content category"] == 'IEO Ad']['Content category'].count(),
    #     domain={'row': 0, 'column': 2}))







    main_dashboard.update_layout(
        grid={'rows': 2, 'columns': 3, 'pattern': "independent"})

    return main_dashboard


@app.callback(
    Output('group-data', 'data'),
    Input('group-data-country-dropdown', 'value'),
    Input('group-data-group-language-dropdown', 'value'),
    Input('group-data-group-category-dropdown', 'value'),
    Input('group-data-weeks-dropdown', 'value'),
)
def update_group_data(countries, group_languages, group_categories, weeks):
    if not countries or not group_languages or not group_categories or not weeks:
        return None

    dff = df[df['Country'].isin(countries)]
    dff = dff[dff['Language'].isin(group_languages)]
    dff = dff[dff['Group category'].isin(group_categories)]
    dff = dff[dff['Week'].isin(weeks)]

    if dff.empty:
        return None

    return dff.to_dict('records')


@app.callback(
    Output('country-graph', 'figure'),
    Input('country-graph-country-dropdown', 'value'),
    Input('language-dropdown', 'value'))
def update_country_graph(countries, category_languages):
    if not countries or not category_languages:
        return {}

    dff = df[df['Country'].isin(countries)]
    dff = dff[dff['Language'].isin(category_languages)]
    countries = dff.groupby('Country').sum().reset_index()

    if countries.empty:
        return {}

    fig = px.bar(countries, title="Sum of clicks for country", x="Country", y="Clicks",
                 color="Country", hover_name="Clicks", opacity=0.5)

    return fig


@app.callback(
    Output('content-graph', 'figure'),
    Input('order-radio', 'value'))
def update_content_graph(order):
    fig = px.bar(df, title="Sum of clicks for content", x="Content name", y="Clicks",
                 color="Country", hover_name="Clicks", opacity=0.5)

    if order == 'ascending':
        fig.update_layout(xaxis={'categoryorder': 'total ascending'})
    else:
        fig.update_layout(xaxis={'categoryorder': 'total descending'})
    return fig


@app.callback(
    Output('category-graph', 'figure'),
    Input('category-graph-country-dropdown', 'value'))
def update_content_graph(countries):
    if not countries:
        return {}

    dff = df[df['Country'].isin(countries)]
    if dff.empty:  # needed?
        return {}

    fig = px.bar(dff.groupby('Group category').mean().reset_index(),
                 title="Average clicks for group category", x="Group category", y="Clicks",
                 color="Group category", hover_name="Clicks", opacity=0.5)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
