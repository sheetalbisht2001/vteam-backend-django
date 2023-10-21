# Install Dependencies

```bash
pip install virtualenv
virtualenv venv
source venv\bin\activate 
pip freeze > requirements.txt
pip install -r requirements.txt
```


# Start Server

```bash
python manage.py runserver
```

# turn models into tables (migration)

```bash
python manage.py makemigrations
python manage.py migrate
```


## After setup, to start a server
```bash
1. Go to the folder where the virtual env folder is present
2. Run command: source vteam-venv/bin/activate
3. Now go the folder where the backend server is
4. Go inside the root folder
5. Run command: python manage.py runserver

```


## TO run the data extraction script from website
```bash
1. Create the upline manually
2. Take the cookie from website
3. python manage.py data_extraction
```


## TODO
>>Frontend 
1. Add a dashboard to the web app - Neelesh
2. Create a module for plottin graphs on points view in vwebiste

>>Backend
1. Add json field to distributor table - Sheetal
2. get api for dashboard - Sheetal
4. add current cumulative PV column in table - Sheetal

3. Explore timescaledb for time series data of distributo (Move changing column to this timescale db)
4. script to read dashbarod from vwebsite
5. script to read points from vwebsite
6. Api to read timeseries data of a particular distribtor over a perid of time
7. Automate login of vwebsite and create a uuid of person if not there and read the cookie, s that we can automate whole script of reading data from website
8. 


## to start influx db 
1. In terminal run `influxd`


# BELOW ARE THE COMMANDS TO ACTIVATE VENV

<!-- sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~$ cd Desktop/
sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop$ ls
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop$ cd code
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop/code$ ls
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop/code$ cd ~/Downloads/


(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Downloads$ ls

(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Downloads$ cd vteam-backend-django/
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Downloads/vteam-backend-django$ ls

(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Downloads/vteam-backend-django$ python manage.py runserver



