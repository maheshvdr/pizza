
presetup to run project:
    * Setup Python 2.7.17 locally 
    * install python by clicking on python-2.7.17.amd64.msi file. Follow the steps to complete the installation
    * Install pip 
    * Install virtual environment using the following command 
        pip install virtualenv


1) clone the repository through below command.
	git clone https://github.com/maheshvdr/pizza.git

2) Go to project repository that is pizza

3) cd pizza_config

4). Create a Python 2.7.17 virtualenv like below
    
    virtualenv venv

5). Activate the virtualenv:
    
    In windows:
      
      venv/Scripts/actiavte
    
    In Ubuntu:
      
      source venv/bin/activate


6). Install dependencies::

    pip install -r requirements.txt

   Alternatively use the make task::

    make install

    Note: Try to install all libraries.


7). Create tables:

    python manage.py makemigrations pizza_app
    python manage.py migrate
    python manage.py migrate pizza_app

    or
    
    ./manage.py makemigrations pizza_app
    ./manage.py migrate
    ./manage.py migrate pizza_app

    
8). To run management command, run below command in terminal under pizza_config directory
    
    python manage.py insert_pizza_data

9). Finally run the server::

    python manage.py runserver


10) To run the test cases 
    
    python manage.py test



Supported browsers
------------------

The goal of the site is to target various levels of browsers, depending on
their ability to use the technologies in use on the site, such as HTML5, CSS3,
SVG, webfonts.

We're following `Mozilla's example <https://wiki.mozilla.org/Support/Browser_Support>`_
when it comes to categorize browser support.

- Desktop browsers, except as noted below, are **A grade**, meaning that
  everything needs to work.

- IE < 11 is **not supported** (based on Microsoft's support).

- Mobile browsers should be considered **B grade** as well.
  Mobile Safari, Firefox on Android and the Android Browser should support
  the responsive styles as much as possible but some degredation can't be
  prevented due to the limited screen size and other platform restrictions.