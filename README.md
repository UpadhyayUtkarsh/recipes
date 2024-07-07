
# Reciepes REST API sample 

This repository:

Consists of REST APIs for adding, updating, fetching and deleting recipes. Sqlite is used for persistent data storage.

#### Tech Stack:

 - **Web framework:** Flask
 - **ORM:** SQLAlchemy
 - **Database:** sqlite
 - **Containerization:** Docker
 - **Documentation:** Swagger-UI

#### Features:

* Containerized Docker build
* Separate environments and configs for Development, Testing, and Production.
* RESTful API documentation via Swagger and visualization with Swagger UI.
* Easy to write different API versions (if needed in future).
* Validation via Marshmallows schema.
* Database entities integrated with SQLAlchemy.

## Contents

* [Get Started](#get-started)
* [Salient points](#salient-points)
* [RESTful endpoints](#restful-endpoints)

## Get Started

#### Requirements

* Docker
* Other dependencies are listed in `requirements.txt`.

Get docker: https://docs.docker.com/get-docker/

#### To run locally

* It is recommended to create a virtual environment. 
     > python3 -m venv .venv  
* Install other dependencies using below command in the root.
    >  pip install -r requirements.txt
* Run the program on local machine 
    > flask run
    > Access APIs at - http://127.0.0.1:5000 


#### To run in docker

* Build the docker image and tag it. 
     >  docker build -t recipes-image .  
* You might face TLS issues while running locally. If that happens you can trust python host however its a bad practice to do it. 
* To run the container locally and map it to your working directory use below command - 
    >  docker run -d -p 5000:5000 -w /app -v "$(pwd):/app" recipes-image

#### Database

* Models folder contains the recipe table. 
* Data.db is automatically created under instance directory in your root program when you run the program. 

## Salient points
* Schema for all endpoints are written in Scheams.py file. 

## RESTful endpoints
* GET /recipes/<string:id> - Returns a recipe for a given ID. 
* PATCH /recipes/<string:id> - Updates a recipe. 
* DELETE /recipes/<string:id> - Deletes a recipe. 
* GET /recipes - Returns list of recipes. 
* POST /recipes - Creates a recipe for a valid payload. 


#### Authentication
* All APIs are public and no authentication is implemented as per requirement. 

