# Simple Crud

This is a simple django app to show a little bit of my knowledge in Django. 


## Setup

1. Clone this repository
    ```
    $ git clone https://github.com/rencesar/simple-crud-django.git
    ```
1. Create your virtualenv and enter
1. Install the requirements on `requirements.txt`
1. Generate your Django Secret Key
    * Access this [link](https://www.miniwebtool.com/django-secret-key-generator/) and generate your secret key

1. Add environment variables
    * You can add them permanently
        ```
        $ echo 'export SECRET_KEY=[PUT YOUR SECRET KEY HERE WITHOUT THE SQUARED BRACKETS]' >> ~/.bashrc
        ```

    * or temporarily
        ```
        $ export DJANGO_SECRET_KEY=[PUT YOUR SECRET KEY HERE WITHOUT THE SQUARED BRACKETS
        ```
1. Do the same thing for:
  - PG_USER
  - PG_PASSWORD
  - SQL_HOST
  - SQL_PORT
  - FACEBOOK_APP_ID
  - FACEBOOK_API_KEY
  
  (obs.: You can add those env variables on your virtualenv as well a better approach).

1. On facebook you have to create your on project and add your Url to it (even localhost:8000 if that is the case)
