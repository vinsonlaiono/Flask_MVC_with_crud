# If you want to import from MySQL database, Import here
from models.db import connectToMySQL

class Hobby:
    """Product Model"""

    def retrieveAllHobbies(app):
    	first = {} 
    	first["id"] = 1
    	first["hobby"] = 'Play Basketball'
    	second = {} 
    	second["id"] = 2
    	second["hobby"] = 'Running'
    	third = {} 
    	third["id"] = 3
    	third["hobby"] = 'Cooking'
    	return [first,second,third]

class User:
	"""User Model"""
	users = []

	def retrieveAllUsers(app):
		mysql = connectToMySQL('flask_mvc')
		query = "SELECT * FROM users"
		users = mysql.query_db(query)

		return users
	def add(app, user):
		print("In models", user, "*"*80)

		mysql = connectToMySQL('flask_mvc')
		query = "INSERT INTO users (first_name, last_name) VALUES (%(fname)s, %(lname)s)"
		data = {
			'fname': user['first_name'],
			'lname': user['last_name'],
		}
		id = mysql.query_db(query, data)

		return None

	def delete(app, id):
		mysql = connectToMySQL('flask_mvc')
		query = "DELETE FROM users WHERE id = "+id
		mysql.query_db(query)
		return None



