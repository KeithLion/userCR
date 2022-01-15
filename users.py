from mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'select * from users;'
        results = connectToMySQL('new_schema1').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = 'insert into users (first_name, last_name,email,created_at,updated_at) values ( %(fname)s ,  %(lname)s  %(ema)s, NOW(), NOW());'
        return connectToMySQL('new_schema1').query_db(query, data)
