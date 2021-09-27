import sqlite3


def create_user(user_id):
    #добавление пользователя в базу данных по id
    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()


    cursor.execute(f"SELECT user_id FROM employees WHERE user_id = {str(user_id)}")
    data = cursor.fetchone()
    if data is None:
        cursor.execute("INSERT INTO employees(user_id) VALUES(?);", str(user_id))
        con.commit()
    else:
        pass

    con.commit()


def delete_user(user_id):
    #удаление пользователя из базы данных по id
    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()

    delete = f"DELETE FROM employees WHERE user_id = {str(user_id)}"
    cursor.execute(delete)
    con.commit()


def mid_nigth_update():
    #смена статуса на FALSE у всех пользователей
    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()

    cursor.execute("UPDATE employees SET status_evening = FALSE, status_morning = FALSE WHERE status_evening = TRUE AND status_morning = TRUE")
    con.commit()


def get_users():
    #получить всех пользователей
    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()

    request = cursor.execute("SELECT * FROM employees")
    data = request.fetchall()
    return data


def morning_update(user_id):
    #смена статуса при нажатии на кнопку утром
    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()

    cursor.execute(f"UPDATE employees SET status_morning = TRUE WHERE user_id = {str(user_id)}")

    con.commit()


def evening_update(user_id):
    #смена статуса при нажатии на кнопку вечером
    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()

    cursor.execute(f"UPDATE employees SET status_evening = TRUE WHERE user_id = {str(user_id)}")

    con.commit()

