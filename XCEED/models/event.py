from XCEED.config.mysqlconnection import connectToMySQL
from flask import flash
from XCEED import DATABASE

class Event:
    def __init__(self, data):
        self.id  = data['id']
        self.title = data['title']
        self.start_date = data['start_date']
        self.end_date = data['end_date']
        self.location = data['location']
        self.content = data['content']
        self.event_img = data['event_img']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """
                insert into events (title, start_date, end_date, content , event_img , location) values
                (%(title)s, %(start_date)s, %(end_date)s, %(content)s , %(event_img)s , %(location)s)
                """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def remove(cls, data):
        query = """
                delete from events where id = %(id)s
                """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "select * from events"
        results = connectToMySQL(DATABASE).query_db(query)
        all_events_data=[]
        for row in results:
            all_events_data.append(cls(row))
        return all_events_data

    @classmethod
    def update(cls, data):
        query = """
                update events set
                title = %(title)s,
                start_date = %(start_date)s,
                end_date = %(end_date)s,
                content = %(content)s
                event_img = %(event_img)s
                location = %(location)s
                where id = %(id)s
                """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def show_one(cls, data):
        query = "SELECT * FROM events WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None
        

    @classmethod
    def get_last_two(cls):
        query = "SELECT * FROM events ORDER BY created_at DESC LIMIT 2;"
        results = connectToMySQL(DATABASE).query_db(query)
        last_two_events_data = [cls(row) for row in results]
        return last_two_events_data
    
    @classmethod
    def show_one_by_id(cls, events_id):
        query = "SELECT * FROM events WHERE id = %(id)s;"
        data = {'id': events_id}
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None