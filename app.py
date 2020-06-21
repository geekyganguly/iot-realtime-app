import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_auth

# BootStrap CSS
import dash_bootstrap_components as dbc

import data

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'test@123'
}

app = dash.Dash(__name__,
                external_stylesheets = [dbc.themes.BOOTSTRAP],
                meta_tags=[
                    {
                        'name': 'viewport',
                        'content': 'width=device-width, initial-scale=1, shrink-to-fit=no',
                        'charset':'utf-8'
                    }
                ]
)

server = app.server
app.title = "IoT Realtime"

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
	dcc.Interval(
        id='interval-component',
        interval=3*1000, # in milliseconds
        n_intervals=0
    ),
	
	dbc.CardColumns([
		dbc.Card([
			dbc.CardHeader([
				dbc.Row([
                    dbc.Col(html.Img(src='/assets/favicon.ico', width='60px', className='img-fluid')),
                    dbc.Col(html.P("NMDC Limited", className="h2 text-light pt-2"), width=9),
                ], no_gutters=True),
			], className=' bg-danger'),
			dbc.CardBody([
				html.H5("Project by - Saurav Ganguly", className='text-danger')
			]),
		],color="danger", outline=True, className='text-center'),

		dbc.Card([
			dbc.CardHeader("Temperature", className='h4 text-light bg-danger'),
			dbc.CardBody([
				daq.Thermometer(
					id='thermometer',
					min=95,
					max=105,
					showCurrentValue=True,
					units="C",
					color="#FF5E5E",
					className='pt-2'
				)
			]),
		],color="danger", outline=True, className='text-center'),
    	
    	dbc.Card([
			dbc.CardHeader("Battery", className='h4 text-light bg-danger'),
			dbc.CardBody([
				daq.GraduatedBar(
  					id='graduatedbar',
  					showCurrentValue=True,
  					step=2,
  					max=100,
  					color="#FF5E5E",
  					className='pt-3 pb-3'
				)  
			]),
		],color="danger", outline=True, className='text-center'),

    	dbc.Card([
			dbc.CardHeader("Speed", className='h4 text-light bg-danger'),
			dbc.CardBody([
				daq.Gauge(
					id='gauge',
					showCurrentValue=True,
   					units="MPH",
					min=0,
					max=100,
					color="#FF5E5E",
					className='pt-4'
				),  
			]),
		],color="danger", outline=True, className='text-center'),
    
		dbc.Card([
			dbc.CardHeader("Counter", className='h4 text-light bg-danger'),
			dbc.CardBody([
				daq.LEDDisplay(
					id='leddisplay',
					size=60,
					color="#FF5E5E",
					className='pt-3 pb-4'
				)  
			]),
		],color="danger", outline=True, className='text-center'),
    	
    	dbc.Card([
			dbc.CardHeader("Fuel", className='h4 text-light bg-danger'),
			dbc.CardBody([
				daq.Tank(
					id='tank',
					min=0,
        			max=10,
					showCurrentValue=True,
					units='gallons',
					color="#FF5E5E",
					style={'margin-left': '100px'},
					className='pt-4 pb-4'
				) 
			]),
		],color="danger", outline=True, className='text-center'),
   ])
],className='container-md mt-3')


@app.callback(
	[Output('thermometer', 'value'),
	Output('gauge', 'value'),
	Output('graduatedbar', 'value'),
	Output('leddisplay', 'value'),
	Output('tank', 'value')],
    [Input('interval-component', 'n_intervals')])
def update(value):
	thermometer_value, gauge_value, graduatedbar_value, leddisplay_value, tank_value = data.get_data()
	return thermometer_value, gauge_value, graduatedbar_value, leddisplay_value, tank_value

if __name__ == '__main__':
    app.run_server(debug=True)
