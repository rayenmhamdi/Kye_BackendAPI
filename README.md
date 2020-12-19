# Kye_BackendAPI
This repository is the backend of the Inventory Management product "Kye". Developed with Django and DRF. 

## Cloning steps
1. Clone this repo to you local dev enviroment.
2. Create a virtual enviroment (virtualenv venv)
3. Activate the venv (venv\Scripts\activate)
4. Install packages (pip install -r requirements.txt)
5. Create the database (python manage.py migrate)
6. Import initial fixture (python manage.py loaddata Fixtures\rayen.json)
7. Run the server and open the documentation to see the apis (http://localhost:8000/apidoc/)

## Adding packages
If you add any package during the dev phase
type (pip freeze > requirements.txt)