from XCEED.config.mysqlconnection import connectToMySQL
from flask import flash
from XCEED import DATABASE

class News:
    def __init__(self, data):
        self.id  = data['id']
        self.title = data['title']
        self.content = data['content']
        self.new_img = data['new_img']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """
                insert into news (title, content , new_img) values
                (%(title)s, %(content)s ,%(new_img)s)
                """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def remove(cls, data):
        query = """
                delete from news where id = %(id)s
                """
        return connectToMySQL(DATABASE).query_db(query, data)
    

    @classmethod
    def get_all(cls):
        query = "select * from news"
        results = connectToMySQL(DATABASE).query_db(query)
        all_news_data=[]
        for row in results:
            all_news_data.append(cls(row))
        return all_news_data

    @classmethod
    def update(cls, data):
        query = """
                update news set
                title = %(title)s,
                content = %(content)s,
                new_img = %(new_img)s
                where id = %(id)s
                """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def show_one(cls, data):
        query = "SELECT * FROM news WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None
        
    @classmethod
    def get_last_two(cls):
        query = "SELECT * FROM news ORDER BY created_at DESC LIMIT 2;"
        results = connectToMySQL(DATABASE).query_db(query)
        last_two_news = [cls(row) for row in results]
        return last_two_news
    
    @classmethod
    def show_one_by_id(cls, news_id):
        query = "SELECT * FROM news WHERE id = %(id)s;"
        data = {'id': news_id}
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None

