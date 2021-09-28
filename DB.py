import sqlite3


class DB:

    def __init__(self):
        self.con = sqlite3.connect('mydatabase.db')
        self.cursor = self.con.cursor()

    def create_user(self,user_id):
        # добавление пользователя в базу данных по id
        self.cursor.execute(f"SELECT user_id FROM employees WHERE user_id = {str(user_id)}")
        data = self.cursor.fetchone()
        if data is None:
            self.cursor.execute("INSERT INTO employees(user_id) VALUES(?);", [str(user_id)])
            self.con.commit()
        else:
            pass
        self.con.commit()

    def delete_user(self, user_id):
        # удаление пользователя из базы данных по id
        delete = f"DELETE FROM employees WHERE user_id = [str(user_id)]"
        self.cursor.execute(delete)
        self.con.commit()

    def mid_nigth_update(self):
        # смена статуса на FALSE у всех пользователей
        self.cursor.execute("UPDATE employees SET status_evening = FALSE, status_morning = FALSE WHERE status_evening = TRUE AND status_morning = TRUE")
        self.con.commit()

    def get_users(self):
        #получение всех пользователей
        request = self.cursor.execute("SELECT * FROM employees")
        data = request.fetchall()
        return data

    def morning_update(self, user_id):
        # смена статуса при нажатии на кнопку утром
        self.cursor.execute(f"UPDATE employees SET status_morning = TRUE WHERE user_id = {str(user_id)}")
        self.con.commit()

    def evening_update(self, user_id):
        # смена статуса при нажатии на кнопку вечером
        self.cursor.execute(f"UPDATE employees SET status_evening = TRUE WHERE user_id = {str(user_id)}")
        self.con.commit()


#db =DB()
#db.create_user("674868256")