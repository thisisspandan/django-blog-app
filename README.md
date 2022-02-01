# django-blog-app


## Setup

 - Clone the repository
 ```sh
 git clone https://github.com/thisisspandan/django-blog-app
 ```
 - Navigate into the repository 
 - Create a Python virtual environment with python 3.6+ version 
 ```sh
 python3.6 -m venv venv
 ```
 - Activate the virtual environemnt
 ```sh
 source venv/bin/activate
 ```
 - Install required packages
 ```sh
 pip install -r requirements.txt
 ```
 - Run migrations
 ```sh 
 python manage.py migrate
 ```
 - Create SuperUser 
 ```sh
 python manage.py createsuperuser 
 ```
 - Start server 
 ```sh
 python manage.py runserver
 ```
 - Access the application at the specifed port ( http://localhost:8000 )
