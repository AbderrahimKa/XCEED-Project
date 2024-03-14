from XCEED.config.mysqlconnection import connectToMySQL
from flask import flash
from XCEED import DATABASE

class Coach:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.firstname = data_dict['firstname']
        self.lastname = data_dict['lastname']
        self.email = data_dict['email']
        self.insta_link = data_dict['insta_link']
        self.linkedin_link = data_dict['linkedin_link']
        self.info = data_dict['info']
        self.photo_link = data_dict['photo_link']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create(cls,data_dict):
        query = """
                insert into coachs (firstname, lastname, email, insta_link, linkedin_link, info, photo_link) values
                (%(firstname)s , %(lastname)s , %(email)s , %(insta_link)s , %(linkedin_link)s , %(info)s , %(photo_link)s)
                """
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    @classmethod
    def remove(cls,data):
        query = """
                delete from coachs where id = %(id)s
                """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = """
                update coachs set
                firstname = %(firstname)s,
                lastname = %(lastname)s,
                email = %(email)s,
                insta_link = %(insta_link)s,
                linkedin_link = %(linkedin_link)s,
                info = %(info)s,
                photo_link = %(photo_link)s
                where id = %(id)s
                """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "select * from coachs"
        results = connectToMySQL(DATABASE).query_db(query)
        all_coches_data=[]
        for row in results:
            all_coches_data.append(cls(row))
        return all_coches_data
    
    @classmethod
    def show_one(cls,data):
        query="Select * From coachs Where id=%(id)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        if(result): 
            return cls(result[0])
        else:
            return None
    

    




    
    