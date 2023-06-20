import mysql.connector

class LoginManager:
    def __init__(self):
        self.logged_in = False
        self.db = mysql.connector.connect(
            host="localhost",
            user="user",  # Replace with your actual username
            password="ADMIN",  # Replace with your actual password
            database="users",
            port="3306"
        )

    def login(self, username, password):
        cursor = self.db.cursor()
        select_query = "SELECT * FROM `users` WHERE `username` = %s AND `password` = %s"
        values = (username, password)
        cursor.execute(select_query, values)
        result = cursor.fetchone()

        if result:
            self.logged_in = True
        else:
            self.logged_in = False

    def logout(self):
        self.logged_in = False

login_manager = LoginManager()
