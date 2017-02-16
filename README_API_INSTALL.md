# README for API Installation

[Back to root README](README.md)

[Read about working with WeVoteServer](README_WORKING_WITH_WE_VOTE_SERVER.md)

[Installation Troubleshooting](README_INSTALLATION_TROUBLESHOOTING.md)

NOTE: We are running Django version 1.8

NOTE: WeVoteServer is built for Python 3.4. It currently still works with Python version 2.7.6.
(tests still have issues with Python 3.4, but everything else works)

## Clone WeVoteServer from github

Create a place to put all of the code from Github:

    $ mkdir /Users/<YOUR NAME HERE>/PythonProjects/

Retrieve “WeVoteServer” into that folder:

1. Create a fork of wevote/WeVoteServer.git. You can do this from https://github.com/wevote/WeVoteServer with the "Fork" button  
(upper right of screen)

1. Change into your local WeVoteServer repository folder, and set up a remote for upstream:  
`$ git remote add upstream git@github.com:wevote/WeVoteServer.git`  


## Installing Python 3 on Mac (See below for Ubuntu)

Mac instructions (Based on [this](http://joebergantine.com/blog/2015/apr/30/installing-python-2-and-python-3-alongside-each-ot/))

Install the latest Python 3.x from package: https://www.python.org/downloads/ 
This allows you to run python3 and pip3. 
(Software gets installed into /Library/Frameworks/Python.framework/Versions/3.5/bin/.)

    $ pip3 install --user virtualenv
    $ vim ~/.bash_profile

Add the following to .bash_profile, save and quit:

    alias virtualenv3='~/Library/Python/3.5/bin/virtualenv'

Update the current Terminal window to use the alias you just saved:

    $ source ~/.bash_profile

Create a place for the virtual environment to live on your hard drive. We recommend installing it 
outside of "PythonProjects" folder:

    $ mkdir /Users/<YOUR NAME HERE>/PythonEnvironments/
    $ cd /Users/<YOUR NAME HERE>/PythonEnvironments/
    $ virtualenv3 WeVoteServer3.5

Now activate this new virtual environment for WeVoteServer:

    $ cd /Users/<YOUR NAME HERE>/PythonProjects/WeVoteServer/
    $ source /Users/<YOUR NAME HERE>/PythonEnvironments/WeVoteServer3.5/bin/activate
    $ export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"
    
## Installing Python 3 on Ubuntu

Taken from here:
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-16-04#install-through-pip-in-a-virtualenv
    
Perhaps the most flexible way to install Django on your system is with the virtualenv tool. This tool allows you to create virtual Python environments where you can install any Python packages you want without affecting the rest of the system. This allows you to select Python packages on a per-project basis regardless of conflicts with other project's requirements.

We will begin by installing pip from the Ubuntu repositories. Refresh your local package index before starting:

    sudo apt-get update
    
If you plan on using version 2 of Python, you can install pip by typing:

    sudo apt-get install python-pip

If, instead, you plan on using version 3 of Python, you can install pip by typing:

    sudo apt-get install python3-pip
    
Once pip is installed, you can use it to install the virtualenv package. If you installed the Python 2 pip, you can type:

    sudo pip install virtualenv

If you installed the Python 3 version of pip, you should type this instead:

    sudo pip3 install virtualenv

Now, whenever you start a new project, you can create a virtual environment for it. Start by creating and moving into a new project directory:

    mkdir ~/newproject
    cd ~/newproject

Now, create a virtual environment within the project directory by typing:

    virtualenv newenv

## Installing Python on Windows
Install the Python 3.4 from package: https://www.python.org/downloads/ This allows you to run python3 and pip3.
Note: Installing Python 3.6 ran into some issues with usaddress package from requirements.txt file.

    $ pip3 install --user virtualenv
    $ vim ~/.bash_profile

Add the following to .bash_profile, save and quit:

    alias virtualenv3='<Python Installation Directory, default is C:\Python3.4>/Scripts/virtualenv.exe'

Update the current Terminal window to use the alias you just saved:

    $ source ~/.bash_profile

Create a place for the virtual environment to live on your hard drive. We recommend installing it
outside of "PythonProjects" folder:

    $ mkdir /Users/<YOUR NAME HERE>/PythonEnvironments/
    $ cd /Users/<YOUR NAME HERE>/PythonEnvironments/
    $ virtualenv3 WeVoteServer3.5

Now activate this new virtual environment for WeVoteServer:

    $ cd /Users/<YOUR NAME HERE>/PythonProjects/WeVoteServer/
    $ source /Users/<YOUR NAME HERE>/PythonEnvironments/WeVoteServer3.5/bin/activate
    $ export PATH="<Postgres Installation Path:default is C:\Program Files\Postgres>/<version-number>/bin:$PATH"

## Installing Postgres
    
Install the latest version of Postgres for your machine (see instructions further down on this page as well):
 
MAC: Download and install the DMG from [http://postgresapp.com/](http://postgresapp.com/)
 
OTHER: Go to [https://www.postgresql.org/download/](https://www.postgresql.org/download/).

Install PGAdmin4. Go to [https://www.pgadmin.org/download/](https://www.pgadmin.org/download/).

Then run these comments from your virtual environment for WeVoteServer:
    
    $ pip install -r requirements.txt
    $ python manage.py runserver

[Having troubles? See Installation Troubleshooting](README_INSTALLATION_TROUBLESHOOTING.md)


### Running Linux?
If you are installing on a Linux environment, we recommend the following steps within your virtual environment. If you
are installing on a Mac or Windows machine, you can skip these steps.

DO:

    sudo apt-get install python-psycopg2 
    sudo apt-get install python-dev
    pip install psycopg2 

THEN:

    pip install django-toolbelt
    pip install --upgrade pip
    pip install -r requirements.txt

## Setup - Install the Postgres database

### METHOD 1 (Mac)
For Mac, download and install the DMG from [http://postgresapp.com/](http://postgresapp.com/)

Run this on your command line:

    export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin

Start up the command line for postgres (there is an 'open psql' button/navigation item if you installed postgresapp.
Run these commands:

    create role postgres;
    alter role postgres with login;

### METHOD 2 (Windows)

Install Postgres and pgAdmin 4 from https://www.postgresql.org/download/windows/. Choose the first option, Interactive installer by EnterpriseDB

After installing Postgres, edit requirements.txt file under WeVoteServer directory with following changes:
psycopg2==2.6 change to psycopg2==2.6.2
py3dns==3.1.0 change to py3dns==3.1.1.a0

Save the changes and execute below commands:
    $ pip install -r requirements.txt
    $ python manage.py runserver

## Setup - pgAdmin 4
In Windows, pgAdmin 4 is installed along with Postgres. From the Start Menu, search for pgAdmin 4 application and click to open it.

In pgadmin add a server - WeVoteServer

PGAdmin 4 issues:
pgAdmin 4 will ask for password when you open it post installation or when you try to add a new server. Windows installation of Postgres does not ask to setup user "postgres". A workaround for this issue is mentioned on this link: http://serverfault.com/questions/110154/whats-the-default-superuser-username-password-for-postgres-after-a-new-install
Editing the file file <PostgreSQL PATH>\data\pg_hba.conf temporarily is recommended.

### METHOD 3 (linux Ubuntu)

Follow [these instructions](https://help.ubuntu.com/community/PostgreSQL)

## Setup - Install pgAdmin 4

We recommend installing pgAdmin 4 as a WYSIWYG database administration tool.
NOTE: You may need to turn off the restriction in "Security & Privacy" on "unidentified developers"
to allow this tool to be installed.
See: http://blog.tcs.de/program-cant-be-opened-because-it-is-from-an-unidentified-developer/

In pgadmin add a server. You can use your sign in name as the server name.


## Setup - Environment Variables Configuration - config/environment_variables.json

NOTE: IMPORTANT STEP

Copy "config/environment_variables-template.json" to "config/environment_variables.json". 
You will configure many variables for your local environment in this file. 

New variables needed by WeVoteServer will be added to
"environment_variables-template.json" from time to time, so please check for updates by comparing your local version
with the template file.

### LOG_FILE
Create a file on your computer to match the one expected in the environment_variables.json file:

    sudo mkdir /var/log/wevote/
    sudo touch /var/log/wevote/wevoteserver.log
    sudo chmod -R 0777 /var/log/wevote/

As configured in github, only errors get written to the log.
Logging has five levels: CRITICAL, ERROR, INFO, WARN, DEBUG.
It works as a hierarchy (i.e. INFO picks up all messages logged as INFO, ERROR and CRITICAL), and when logging we
specify the level assigned to each message. You can change this to info items by changing this:

    LOG_FILE_LEVEL = logging.INFO

## Set up GeoIP

###  Install the C library

Start by changing directories into your WeVoteServer folder:

    $ cd /Users/<YOUR NAME HERE>/PythonProjects/WeVoteServer/
    $ git clone https://github.com/maxmind/geoip-api-c.git
    $ cd geoip-api-c
    $ ./bootstrap
    
If you have problems with ./bootstrap command, try this. On OS X 10.10.5 I got an error 
(autoreconf: command not found), and had to do this first. For directions on installing "brew" see
[http://brew.sh/](http://brew.sh/):
    
    $ brew install automake
    $ brew install libtool

If you had to install "brew", try this again.

    $ ./bootstrap
    $ ./configure
    $ make
    
In the "make check" step, you may see some errors like "make[2]: * [install-libLTLIBRARIES] Error 1". 
These errors won't prevent geoip from working.
    
    $ make check
    $ make install
    $ cd ..

### Windows installation
In Windows, on trying to execute bootstrap command, you may get error such as "autoreconf not found"
You will need to install a Unix/POSIX environment on Windows like Cygwin, Msys or Mingw. Mingw does not have POSIX compatibility support for sockets.
Note: The compilation of geo-ip C library did not go through for me. Ran into POSIX socket related compilation issues when I tried to use mingw library.

    
#### “libGeoIP.so.1: cannot open..."
On Amazon Linux (Fedora), if you get a “libGeoIP.so.1: cannot open shared object No such file or directory” error 
when you run WeVoteServer:

    $ sudo vi /etc/ld.so.conf
    
Add on a new line:

    /usr/local/lib
     
Then run:

    $ sudo ldconfig


###  Run the command that downloads the GeoLite database from the WeVoteServer root folder (Where this README lives)

    $ ./manage.py update_geoip_data
    
### On Amazon Web Services - NOT for local install

Buy the latest database ("GEO-133	GeoIP Legacy City with DMA/Area Codes") at http://www.maxmind.com

Find and copy the GZIP download link from this page https://www.maxmind.com/en/download_files which will look like:

    https://download.maxmind.com/app/geoip_download?edition_id=133&date=20160517&suffix=tar.gz&license_key=KEYHERE

Transfer it to the live API server:
    
    $ cd /home/wevote/WeVoteServer/geoip/import_data/
    $ wget "https://download.maxmind.com/app/geoip_download? (FILL IN ACTUAL LINK FROM THEIR DOWNLOADS PAGE)"
    $ mv geoip_download\?edition_id\=133\&date\=20160202 GeoIP-133_DATE_HERE.tar.gz
    $ chmod 0777 GeoIP-133_DATE_HERE.tar.gz
    $ tar zxvf GeoIP-133_DATE_HERE.tar.gz
    $ cp GeoIP-133_20160202/GeoIPCity.dat .
    $ chmod 0777 *.*

## Setup - Database Creation

If you would like to match the local database settings from the "config/environment_variables.json" file,
(Search for "DATABASES"):

    $ createdb WeVoteServerDB

Populate your database with the latest database tables:

    $ python manage.py makemigrations
    $ python manage.py migrate

Create the initial database:

    $ python manage.py syncdb

When prompted for a super user, enter your email address and a simple password. This admin account is only used in development.

If you are not prompted to create a superuser, run the following command:

    python manage.py createsuperuser
    
## Test that WeVoteServer is running

Start up the webserver:

    $ cd /Users/<YOUR NAME HERE>/PythonProjects/WeVoteServer/
    $ source /Users/<YOUR NAME HERE>/PythonEnvironments/WeVoteServer3.4/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py runserver

[Having troubles? See Installation Troubleshooting](README_INSTALLATION_TROUBLESHOOTING.md)

## Grant yourself Admin rights

Find admin tools here:

    http://localhost:8000/admin
    
Now you will need to authenticate as an admin. For now, this will require that you log in with your Twitter account. 
Please contact Dale.McGrew@WeVoteUSA.org for configuration settings you can add to your local 
config/environment_variables.json file.

    Click "Sign in with Twitter" and use your Twitter credentials to Sign-In. 
    
After you have signed in, you will see an error message in red that states "You must sign in with account that has
Verified Volunteer rights to see that page." Just below the error message, there will be a field "we_vote_id" with a 
text string like "wv01voter1234" next to it, note the we_vote_id number.

### Give yourself Admin rights via PGAdmin

Open pgAdmin 4 and navigate to:

    Server Groups > Servers > WeVoteServerDB 

Double click on WeVoteServerDB (there may be a red x thru it). It will prompt you for a password; leave it blank and click
OK. You may see an additional warning screen about saving passwords, if so, click ok. Once you are connected, navigate to:

    WeVoteServerDB > Schemas > public > Tables > voter_voter

Then, right click, and in the menu that appears, select:

    View Data > View Top 100 rows

In the new window that opens, scroll down and find the we_vote_id number, noted above. Scroll to the right to locate the box
"is_admin" click on it once, and a box will appear, click it and change it to TRUE. Then, go back to your browser, 
and click on:

    Back to Admin Home
    
### Give yourself Admin rights via command line

Run this command from your Postgres command line. Replace WE_VOTE_ID_HERE with the actual we_vote_id found above:

    UPDATE voter_voter SET is_admin=true WHERE we_vote_id='WE_VOTE_ID_HERE';

## Test your access

Now, you should be able to access the admin tools. 

Find documentation for all of the APIs here:

    http://localhost:8000/apis/v1/docs

## Sample data
Sample data is provided. Go here:

    http://localhost:8000/admin
    
Find the "Sync Data with Master We Vote Servers" link, and click it: http://localhost:8000/admin/sync_dashboard/

Choose 1) an upcoming election from the drop down, and 2) your local state, and then run all scripts from top to bottom.
 
### Google Civic
In order to retrieve fresh ballot data, you will need to sign up for a Google Civic API key:

  - Go here:  https://console.developers.google.com/projectselector/apis/credentials?pli=1
  - Create a new project
  - Click Credentials -> New credentials -> API Key -> Browser Key
  - Check to make sure the "Google Civic Information API" is enabled here: https://console.developers.google.com/apis/enabled?project=atomic-router-681
  - If you don't see it, go here and search for "Google Civic": https://console.developers.google.com/apis/library?project=atomic-router-681
  - When you find it, click the "Enable API" button.
  - Copy your newly generated key and paste it into config/environment_variables.json as the value for GOOGLE_CIVIC_API_KEY
  
### Vote Smart
We also have a paid subscription with Vote Smart. You can sign up for a 
[Vote Smart developer key](http://votesmart.org/share/api/register#.VrIx4VMrJhE), or reach out to 
Dale.McGrew@WeVoteUSA.org to discuss using our organizational account.

  - Copy your Vote Smart key and paste it into config/environment_variables.json as the value for VOTE_SMART_API_KEY
  
### Twitter
Instructions coming soon.
    
[Working with WeVoteServer day-to-day](README_WORKING_WITH_WE_VOTE_SERVER.md)

[Back to root README](README.md)
