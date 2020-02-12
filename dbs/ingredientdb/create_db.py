import sqlite3
class create(object):

    def create(self):
        conn = sqlite3.connect('ingredient.db')
        cursor = conn.cursor()
        sql = '''create table items(
            type text,
            quantity number
            )'''
        cursor.execute(sql)
        cursor.close()

def main():
    c = create()
    c.create()
if __name__ == '__main__':
    main()