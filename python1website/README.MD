<h1>Welcome to the McKurz Capital financial charts app.</h1>

<h3>Prerequisites are installation of python and pip. These directions were used on an Ubuntu 18.04 installation.</h3>

<h3>Steps to clone our repo and start the app</h3>

<h3>Step 1: Make directory and cd into it.</h3>

      mkdir finpython
      cd finpython

<h3>Step 2: Create git repository and clone repository.</h3>

      git init
      git clone https://github.com/georgemac510/python1website.git
      cd python1website

<h3>Step 3: Creating python virtual machine instance using virtualenv.</h3>

      pip install virtualenv
      python -m virtualenv virtual
      cd virtual

<h3>Step 4: Install dependencies using pip.</h3>

      pip install flask
      pip install bokeh
      pip install pandas
      pip install pandas_datareader

If errors,

      python -m pip install --upgrade pip

then try to install the "error" dependency again.

<h3>Step 5: Start app and explore</h3>

      cd ..
      python script1.py

<h3>This will start your virtual instance. Navigate to http://127.0.0.1:5000/ and the app
will open in your browser. On the top right on the navigation bar click on Plot. If all is well,
you should see a stock chart of the company Rio Tinto during the first half of 2020.</h3>

<h3>You can see the app at https://python1website.herokuapp.com.</h3>

<h3>More improvements to come. Stay tuned!</h3>

<h3>Visit us at https://mckurzcapital.com to see our other projects.</h3>
