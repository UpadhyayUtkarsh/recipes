from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import RecipesModel
from resources.v1.schemas.schemas import RecipeCreateSchema, RecipeUpdateSchema , RecipeResponseSchema , RecipesListResponseSchema , RecipeUpdateResponseSchema, RecipeCreateResponseSchema

blp = Blueprint("Recipes", "recipes", description="recipes")

@blp.route("/recipes/<string:id>")
class Recipes(MethodView):
    @blp.response(200, RecipeResponseSchema)
    def get(self, id):
        item = RecipesModel.query.get(id)
        if item == None: 
                abort(400, messages =  "No recipe found"  )
        return { "message" : "Recipe details by id", "recipe": [item]}

    @blp.arguments(RecipeUpdateSchema)
    @blp.response(200, RecipeUpdateResponseSchema)
    def patch(self, recipe, id):
        try:
            existingRecipe = RecipesModel.query.get(id)


            existingRecipe.title = recipe["title"]
            existingRecipe.making_time = recipe["making_time"]
            existingRecipe.serves = recipe["serves"]
            existingRecipe.ingredients = recipe["ingredients"]
            existingRecipe.cost = recipe["cost"]

            db.session.add(existingRecipe)
            db.session.commit()
        except SQLAlchemyError: 
            abort(200, { "message": "Recipe updation failed!" })
        

        return {"message": "Recipe successfully updated!", "recipe": [existingRecipe]}
    
    def delete(self, id):
        try: 
            item = RecipesModel.query.get(id)
            if item == None: 
                abort(400, messages =  "No recipe found"  )

            db.session.delete(item)
            db.session.commit()
        except SQLAlchemyError: 
            abort(200, { "message": "Recipe deletion failed!" })
        
        return {  "message": "Recipe successfully removed!" }
    
    @blp.errorhandler(400)
    def bad_request(error):
        response = {
                     "message": error.data.get('messages'),
                    }
        return response , 200


@blp.route("/recipes")
class RecipesList(MethodView):
    @blp.response(200, RecipesListResponseSchema())
    def get(self):
        return {"recipes" : RecipesModel.query.all()}
    
    @blp.arguments(RecipeCreateSchema)
    @blp.response(200, RecipeCreateResponseSchema)
    def post(self, recipe):
        try:
            item = RecipesModel(**recipe)
       
            db.session.add(item)
            db.session.commit()

        except ValidationError as err:
            abort(422, err)

        except SQLAlchemyError:
            abort(200, {
                    "message": "Recipe creation failed!",
                    "required": "title, making_time, serves, ingredients, cost"
                    })
        

        return {"message": "Recipe successfully created!", "recipe": [item]}
    
    @blp.errorhandler(422)
    def handle_unprocessable_entity(error):
        response = {
                    "message": "Recipe creation failed!",
                    "required": "title, making_time, serves, ingredients, cost"
                    }
        return response , 200
    
