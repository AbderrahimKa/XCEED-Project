from XCEED.config.mysqlconnection import connectToMySQL
from flask import flash
from XCEED import DATABASE
import re	

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']



    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users (first_name, last_name, email, password ) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM users WHERE id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return cls(result[0])

    
    @classmethod
    def get_by_email(cls, data_dict):
        query = """SELECT * FROM users WHERE email=%(email)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        if result :
            return cls(result[0])
        return False
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users ORDER BY created_at DESC;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_users_data=[]
        for row in results:
            all_users_data.append(cls(row))
        return all_users_data
    
    @classmethod
    def delete(cls, data):
        query = """
        delete from users where id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def is_form_submitted(cls,data):
        query = """
                SELECT count(*) FROM users u join users_forms uf where u.id = uf.user_id and u.id = %(id)s; 
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result :
            return True
        return False 

    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['first_name'])<2:
            is_valid =False
            flash("First Name not valid", "first_name")
        if len(data_dict['last_name'])<2:
            is_valid =False
            flash("Last name not valid", "last_name")
        if not EMAIL_REGEX.match(data_dict['email']): 
            is_valid = False
            flash("Email not valid", "email")
        elif User.get_by_email({'email': data_dict['email']}):
            is_valid = False
            flash("email already taken ","email")
        if len(data_dict["password"])<7:
            is_valid = False
            flash("Password too short", "password")
        elif data_dict["password"]!= data_dict["confirm_password"]:
            is_valid = False
            flash("Password and confirm password must match", "password")
        return is_valid