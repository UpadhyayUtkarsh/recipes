
# Reciepes REST API sample 

This repository:

Consists of REST APIs for adding, updating, fetching and deleting recipes. Sqlite is used for persistent data storage.

#### Tech Stack:

 - **Web framework:** Flask
 - **ORM:** SQLAlchemy
 - **Database:** sqlite (Local) , postgres(deployed version)
 - **Containerization:** Docker
 - **Documentation:** Swagger-UI. 

#### Features:

* Containerized Docker build for APIs and DB. 
* Separate environments and configs for Development, Testing, and Production can be created by 
  separating env variables.
* RESTful API documentation via Swagger and visualization with Swagger UI.
* Easy to write different API versions (if needed in future).
* Validation via Marshmallows schema.
* Database entities integrated with SQLAlchemy.

## Contents

* [Get Started](#get-started)
* [Salient points](#salient-points)
* [RESTful endpoints](#restful-endpoints)
* [Documentation](#Documentation)


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


#### To run in docker locally

* Build the docker images and run cotainers locally. 
     >  docker compose up. 

#### Database

* Models folder contains the schema for recipe table. 
* If Database_Url is not provided in env file application works with SQLite and data.db will be created under instance directory in your root folder when you run the program. 
* If postgres Database_Url is provided in env file application works with postgres.


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

## Documentation

* After running applicaton locally API specification can be viewed at -  http://127.0.0.1:5000/recipes-api-specification
