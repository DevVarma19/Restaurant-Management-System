import sqlite3
class create(object):

    def create(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        sql = '''create table users(
            name text,
            username text,
            password text)'''
        cursor.execute(sql)
        cursor.close()

def main():
    c = create()
    c.create()
if __name__ == '__main__':
    main()