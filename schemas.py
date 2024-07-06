from marshmallow import Schema, fields
from datetime import datetime

class CustomDateTime(fields.DateTime):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return value.strftime("%Y-%m-%d %H:%M:%S")
    
class RecipeCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    making_time = fields.Str(required=True)
    serves = fields.Str(required=True)
    ingredients = fields.Str(required=True)
    cost = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# class RecipeSchema(Schema):
#     id = fields.Int(dump_only=True)
#     title = fields.Str(required=True)
#     making_time = fields.Str(required=True)
#     serves = fields.Str(required=True)
#     ingredients = fields.Str(required=True)
#     cost = fields.Int(required=True)

class RecipeCreateResponseSchema(Schema):
    message = fields.Str()
    recipe = fields.List(fields.Nested(lambda: RecipeCreateResponseSchema.RecipeSchema()), required=True)

    class RecipeSchema(Schema):
        id = fields.Str(required=True)
        title = fields.Str(required=True)
        making_time = fields.Str(required=True)
        serves = fields.Str(required=True)
        ingredients = fields.Str(required=True)
        cost = fields.Str(required=True)
        created_at = CustomDateTime(required=True)
        updated_at = CustomDateTime(required=True)

class RecipeResponseSchema(Schema):
    message = fields.Str()
    recipe = fields.List(fields.Nested(lambda: RecipeResponseSchema.RecipeSchema()), required=True)
    class RecipeSchema(Schema):
        id = fields.Int(required=True)
        title = fields.Str(required=True)
        making_time = fields.Str(required=True)
        serves = fields.Str(required=True)
        ingredients = fields.Str(required=True)
        cost = fields.Str(required=True)
        created_at = CustomDateTime()
        updated_at = CustomDateTime()


class RecipesListResponseSchema(Schema):
    recipes = fields.List(fields.Nested(lambda: RecipesListResponseSchema.RecipeSchema()), required=True)

    class RecipeSchema(Schema):
        id = fields.Int(required=True)
        title = fields.Str()
        making_time = fields.Str()
        serves = fields.Str()
        ingredients = fields.Str()
        cost = fields.Str()
        

class RecipeUpdateSchema(Schema):
    title = fields.Str()
    making_time = fields.Str()
    serves = fields.Str()
    ingredients = fields.Str()
    cost = fields.Int()

class RecipeUpdateResponseSchema(Schema):
    message = fields.Str(required=True)
    recipe = fields.List(fields.Nested(lambda: RecipeUpdateResponseSchema.RecipeSchema()), required=True)

    class RecipeSchema(Schema):
        title = fields.Str(required=True)
        making_time = fields.Str(required=True)
        serves = fields.Str(required=True)
        ingredients = fields.Str(required=True)
        cost = fields.Str(required=True)


