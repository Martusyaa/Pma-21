from nazarii_bryniarskyi.rest.model import Person
import mysql.connector

class PersonRepo:

    @staticmethod
    def _connect():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="rest"
        )

    @staticmethod
    def findAll():
        connection = PersonRepo._connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM person")
        results = cursor.fetchall()
        connection.close()
        cursor.close()
        return results

    @staticmethod
    def findById(id):
        connection = PersonRepo._connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM person WHERE id = %s", (id,))
        result = cursor.fetchall()
        connection.close()
        cursor.close()
        return result

    @staticmethod
    def save(person):
        connection = PersonRepo._connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO person(name, surname) VALUES(%s, %s)", (person.name, person.surname))
        connection.commit()
        connection.close()
        cursor.close()
        return person.__str__()

    @staticmethod
    def update(id, name=None, surname=None):
        connection = PersonRepo._connect()
        cursor = connection.cursor()

        update_query = "UPDATE person SET"
        update_values = []

        if name is not None:
            update_query += " name = %s,"
            update_values.append(name)

        if surname is not None:
            update_query += " surname = %s,"
            update_values.append(surname)

        update_query = update_query.rstrip(',')

        update_query += " WHERE id = %s"
        update_values.append(id)

        cursor.execute(update_query, tuple(update_values))
        connection.commit()
        connection.close()
        cursor.close()
        return cursor.rowcount > 0

    @staticmethod
    def delete(id):
        connection = PersonRepo._connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM person WHERE id = %s", (id,))
        result = cursor.fetchall()
        cursor.execute("DELETE FROM person WHERE id = %s", (id,))

        connection.commit()
        connection.close()
        cursor.close()

        return result
