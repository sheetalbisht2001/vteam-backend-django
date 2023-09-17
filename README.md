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





<!-- sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~$ cd Desktop/
sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop$ ls
 46                    'nandi 1.zip'  'New folder (2)'
 789                    nandi1.zip    'New folder (3)'
 code                  'nandi 2.zip'  'New folder (5).zip'
 DOCUMENTS             'nandi 3.zip'   Private.zip
 jdk-20_linux-x64_bin  'nandi 4.zip'   SBG.zip
'k Camera.zip'         'nandi 5.zip'   tanuja.zip
'k New folder.zip'      nandi.zip      virtual-envs
'nandi 1 (2).zip'      'New folder'
sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop$ cd virtual-envs/
sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop/virtual-envs$ ls
vteam-venv
sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop/virtual-envs$ ls
vteam-venv
sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop/virtual-envs$ source vteam-venv/bin/activate
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop/virtual-envs$ cd ..
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop$ ls
 46                    'nandi 1.zip'  'New folder (2)'
 789                    nandi1.zip    'New folder (3)'
 code                  'nandi 2.zip'  'New folder (5).zip'
 DOCUMENTS             'nandi 3.zip'   Private.zip
 jdk-20_linux-x64_bin  'nandi 4.zip'   SBG.zip
'k Camera.zip'         'nandi 5.zip'   tanuja.zip
'k New folder.zip'      nandi.zip      virtual-envs
'nandi 1 (2).zip'      'New folder'
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop$ cd code
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop/code$ ls
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Desktop/code$ cd ~/Downloads/
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Downloads$ lsd

Command 'lsd' not found, but can be installed with:

sudo snap install lsd

(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Downloads$ ls
 Affirmations.docx                  OpenJDK17U-jdk_x64_linux_hotspot_17.0.8_7.tar.gz
 api.zip                            pryog30.pdf
 blog_sheetalbiisht-main.zip        Python-3.11.5
 chrome-linux64.zip                 Python-3.11.5.tar.xz
 cmder                              readme.txt
 cmder.zip                          remix-backup-at-22h6min-2023-9-14.zip
 code_1.81.0-1690980880_amd64.deb   rtw88-master
'Daily Activity Tracker.docx'      'Screenshot 2023-09-16 at 7.45.58 PM.png'
 dbeaver-ce_23.1.4_amd64.deb        sheetalbisht2001.github.io-master.zip
 Frontend                          'Sheetal_Bisht_Resume (1).pdf'
 hydejack-master.zip                Sheetal_Bisht_Resume.pdf
 ideaIU-2023.2                      solidity_0.8.20
 ideaIU-2023.2.tar.gz               solidity_0.8.20.tar.gz
 IP_260723_MMS_DL_ENG.pdf          'Trade Ledger- Calendar Spread Strategy (1).xlsx'
'Mindset Assignment 01.docx'       'Trade Ledger- Calendar Spread Strategy.xlsx'
'Mindset Assignment 02.docx'        vteam-backend-django
'new pdf 123 (1).pdf'               vteam-backend-django.zip
'new pdf 123.pdf'
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Downloads$ cd vteam-backend-django/
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Downloads/vteam-backend-django$ ls
ascripts  db_migrations  Pipfile       README.md         settings
conf      manage.py      Pipfile.lock  requirements.txt  stractor
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Downloads/vteam-backend-django$ ls
ascripts  db_migrations  Pipfile       README.md         settings
conf      manage.py      Pipfile.lock  requirements.txt  stractor
(vteam-venv) sheetal@sheetal-VivoBook-ASUSLaptop-X515EA-X515EA:~/Downloads/vteam-backend-django$ python manage.py runserver
Performing system checks...


