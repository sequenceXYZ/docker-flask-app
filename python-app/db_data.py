import db_connect as db


def get_all_people():
    with db.create_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, field, country FROM famous_people")
            people = [{'name': name, 'field': field, 'country': country} for name, field, country in cursor.fetchall()]
    return people


def add_new_person(person):
    with db.create_connection() as connection:
        with connection.cursor() as cursor:
            query = "SELECT COUNT(*) FROM famous_people WHERE name = %s"
            cursor.execute(query, (person['name'],))
            count = cursor.fetchone()[0]

            if count > 0:
                return False

            query = "INSERT INTO famous_people (name, field, country) VALUES (%s, %s, %s);"
            values = (person['name'], person['field'], person['country'])
            cursor.execute(query, values)
            connection.commit()

            return True



def get_one_person(name):
    with db.create_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, field, country FROM famous_people WHERE name = %s", (name,))
            people = []
            for person in cursor.fetchall():
                people.append({'name': person[0], 'field': person[1], 'country': person[2]})
            return people or None


def delete_person(name):
    with db.create_connection() as connection:
        with connection.cursor() as cursor:
            delete_query = "DELETE FROM famous_people WHERE name= %s"
            cursor.execute(delete_query, (name,))
            connection.commit()
            return cursor.rowcount


def update_person(name, person):
    with db.create_connection() as connection:
        with connection.cursor() as cursor:
            update_query = "UPDATE famous_people SET field = %s, country = %s where name = %s"
            values = (person['field'], person['country'], name)
            cursor.execute(update_query, values)
            connection.commit()
        return person
