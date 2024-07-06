from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#  {
#   "message": "Recipe successfully created!",
#   "recipe": [
#     {
#       "id": "3",
#       "title": "Tomato Soup",
#       "making_time": "15 min",
#       "serves": "5 people",
#       "ingredients": "onion, tomato, seasoning, water",
#       "cost": "450",
#       "created_at": "2016-01-12 14:10:12",
#       "updated_at": "2016-01-12 14:10:12"           
#     }
#   ]
# }

#   {
#     "recipes": [
#       {
#         "id": 1,
#         "title": "Chicken Curry",
#         "making_time": "45 min",
#         "serves": "4 people",
#         "ingredients": "onion, chicken, seasoning",
#         "cost": "1000"
#       },
#       {
#         "id": 2,
#         "title": "Rice Omelette",
#         "making_time": "30 min",
#         "serves": "2 people",
#         "ingredients": "onion, egg, seasoning, soy sauce",
#         "cost": "700"
#       },
#       {
#         "id": 3,
#         "title": "Tomato Soup",
#         "making_time": "15 min",
#         "serves": "5 people",
#         "ingredients": "onion, tomato, seasoning, water",
#         "cost": "450"
#       }
#     ]
#   }
#   {
#     "message": "Recipe successfully updated!",
#     "recipe": [
#       {
#         "title": "Tomato Soup",
#         "making_time": "15 min",
#         "serves": "5 people",
#         "ingredients": "onion, tomato, seasoning, water",
#         "cost": "450"
#       }
#     ]
#   }

# {
#   "message": "Recipe details by id",
#   "recipe": [
#     {
#       "id": 1,
#       "title": "Chicken Curry",
#       "making_time": "45 min",
#       "serves": "4 people",
#       "ingredients": "onion, chicken, seasoning",
#       "cost": "1000"
#     }
#   ]
# }
