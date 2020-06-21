# iot-realtime-app
Python Dash web app for Realtime IoT application.<br>
Preview app [here](https://iot-realtime-app.herokuapp.com/)
Login id - admin 
Password - test@123

Install requirements packages using pip<br>
`
pip install -r requirements.txt
`

Run app using<br>
`
python app.py
`

Navigate to [http://127.0.0.1:8050/](http://127.0.0.1:8050/)

Note- 
* App shows random generated data to use realtime sensor data you can change it in daya.py file in get_data function.
* You can change update time interval in app.py at line 27
  ```
  dcc.Interval(
        id='interval-component',
        interval=3*1000, # in milliseconds
        n_intervals=0
  ),
   ```
* You can change authentication credentials in app.py at line 15
  ```
  # Keep this out of source code repository - save in a file or a database
  VALID_USERNAME_PASSWORD_PAIRS = {
      'admin': 'test@123'
  }
  ```
References - 
* [https://dash.plotly.com/layout](https://dash.plotly.com/layout)
* [https://dash.plotly.com/basic-callbacks](https://dash.plotly.com/basic-callbacks)
* [https://dash.plotly.com/dash-daq](https://dash.plotly.com/dash-daq)
* [https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/)
* [https://dash.plotly.com/authentication](https://dash.plotly.com/authentication)
