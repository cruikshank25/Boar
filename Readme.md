
To run the project you must have the following dependancies installed:

python3 + following libraries:
elasticsearch==5.3.0 (optional for 'elk_shipper.py')
SQLAlchemy==1.1.5 (for MySQL database connection)
pandas==0.19.2 (for necessary datatypes)
bokeh==0.12.4 (for web server and plot visualizations)

Snort / PulledPork / Barnyard2 / Pytbull:
Snort==2.9.9.0 (Intrusion detection System)
PulledPork==0.7.2 (Automatically Updating Rulesets)
Barnyard2==2.1.14 (Spooler and Database)
Pytbull==2.1 (optional IDS testing framework)


Useage:
To run this project the following command should be used in projects parent directory.

'bokeh serve --show Boar'