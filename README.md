**Boar - Snort IDS Alert Visualization**

This project visualizes Snort IDS alert data from the barnyard2 MySQL database in real-time using modern Python data analytics.

**Features:**

- 'Big Data' style visualization for overview of attacks.

- Real-Time capability with updating plots.

- Utilises Bokeh, a modern Python visualization library. 

- Ability to hover over individual alerts in realtime.

**Example Dashboard:**

![example_dashboard](https://cloud.githubusercontent.com/assets/22418075/26171251/312a9f86-3b3c-11e7-81a5-69123455cab2.png
)


**Architecture:**

![example_architechture](https://cloud.githubusercontent.com/assets/22418075/26170725/57f0dc04-3b3a-11e7-81d9-5c14b4750400.PNG
)

**Python Software Dependancies:**

SQLAlchemy==1.1.5

pandas==0.19.2 

bokeh==0.12.4 

Flask=0.12.1

mysqlclient=1.3.9

**Intrusion Detection System Server Dependancies:**

Snort==2.9.9.0 (Intrusion detection System)

PulledPork==0.7.2 (Automatically Updating Rulesets)

Barnyard2==2.1.14 (Spooler and Database)

**Configuration:**

Before executing the software, a configuration file (config.py) must be created.
 
This will allow connection of the visualization software to your database. 

This file should be saved in the Boar main foldler with information of your 

barnyard2 MySQL database like so;

![example_file_structure](https://cloud.githubusercontent.com/assets/22418075/26200756/9baf7a80-3bc7-11e7-9cbc-bb3dccc4c441.png)

**config.py line 1 - mysql = {'connection': 'mysql://root:toor@127.0.0.1:3306/snort'}**

Remember to change the database username, password and address to your specific system.

**Useage:**
To execute the software, use the following command from parent directory;

`bokeh serve --show Boar`
