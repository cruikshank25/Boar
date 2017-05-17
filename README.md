**Boar - Snort IDS Alert Visualization**

![example_dashboard](https://cloud.githubusercontent.com/assets/22418075/26171251/312a9f86-3b3c-11e7-81a5-69123455cab2.png
)
**Architecture:**

![example_architechture](https://cloud.githubusercontent.com/assets/22418075/26170725/57f0dc04-3b3a-11e7-81d9-5c14b4750400.PNG
)
To run the project you mgust have the following dependancies installed:

**Python Software Dependancies:**

elasticsearch==5.3.0 (optional for 'elk_shipper.py')

SQLAlchemy==1.1.5 (for MySQL database connection)

pandas==0.19.2 (for necessary datatypes)

bokeh==0.12.4 (for web server and plot visualizations)

**Intrusion Detection System Server Dependancies:**

Snort==2.9.9.0 (Intrusion detection System)

PulledPork==0.7.2 (Automatically Updating Rulesets)

Barnyard2==2.1.14 (Spooler and Database)

Pytbull==2.1 (optional IDS testing framework)

**Configuration:**

**Useage:**
To execute the software, use the following command from parent directory;

`bokeh serve --show Boar`

**Features:**

- 'Big Data' style visualization for overview of attacks.

- Real-Time capability with updating plots.

- Utilises Bokeh, a modern Python visualization library. 

- Ability to hover over individual alerts in realtime.

![example_hover](https://cloud.githubusercontent.com/assets/22418075/26171305/5b464c20-3b3c-11e7-81d0-da2d770c2151.png)
