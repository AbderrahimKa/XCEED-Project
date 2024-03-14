from XCEED.config.mysqlconnection import connectToMySQL
from flask import flash
from XCEED import DATABASE

class Form:
    def init(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']
        self.full_name = data_dict['full_name']
        self.email = data_dict['email']
        self.date_of_birth = data_dict['date_of_birth']
        self.gender = data_dict['gender']
        self.country=data_dict['country']
        self.phone_number=data_dict['phone_number']
        self.goal=data_dict['goal']
        self.motivation=data_dict['motivation']
        self.goal_details=data_dict['goal_details']
        self.coaching_type=data_dict['coaching_type']
        self.weight=data_dict['weight']
        self.height=data_dict['height']
        self.activity_level=data_dict['activity_level']
        self.hours_of_sleep=data_dict['hours_of_sleep']
        self.default_workout_time=data_dict['default_workout_time']
        self.meals_per_day=data_dict['meals_per_day']
        self.forbidden_food=data_dict['forbidden_food']
        self.training_experience=data_dict['training_experience']
        self.default_activity=data_dict['default_activity']
        self.previous_medical_history=data_dict['previous_medical_history']
        self.default_health_concerns=data_dict['default_health_concerns']
        self.about_yourself=data_dict['about_yourself']
        self.from_where=data_dict['from_where']
        self.additional_question=data_dict['additional_question']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']


    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users_forms 
                (user_id, full_name, email, date_of_birth, 
                gender, country, phone_number, goal, motivition, 
                goal_details, coaching_type, weight, height, activity_level, 
                hours_of_sleep, default_workout_time, meals_per_day, forbidden_food, 
                training_experience, default_activity, previous_medical_history, 
                default_health_concerns, about_yourself, from_where, additional_question) 
                VALUES 
                (%(user_id)s, %(full_name)s, %(email)s, %(date_of_birth)s, 
                %(gender)s, %(country)s, %(phone_number)s, %(goal)s, %(motivition)s, 
                %(goal_details)s, %(coaching_type)s, %(weight)s, %(height)s, %(activity_level)s, 
                %(hours_of_sleep)s, %(default_workout_time)s, %(meals_per_day)s, %(forbidden_food)s, 
                %(training_experience)s, %(default_activity)s, %(previous_medical_history)s, 
                %(default_health_concerns)s, %(about_yourself)s, %(from_where)s, %(additional_question)s);
                """
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    @classmethod
    def get_all(cls):
        query = """
                select * from users_forms    
                """
        results = connectToMySQL(DATABASE).query_db(query)
        all_users_data=[]
        for row in results:
            all_users_data.append(cls(row))
        return all_users_data
    
    @classmethod
    def get_by_id(cls,data):
        query = """ 
                select * from users_form where id = %(id)s
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        if (result):
            return cls(result[0])
        else:
            return None
        
    @classmethod
    def get_user_form(cls,data):
        query = """
                SELECT f.* FROM users u LEFT JOIN users_forms f ON u.id = f.user_id WHERE f.user_id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result[0]
    

    
    


    





