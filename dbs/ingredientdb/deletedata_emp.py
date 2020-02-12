import sqlite3

class query(object):

    def query(self):
        conn = sqlite3.connect('ingredient.db')
        cursor = conn.cursor()
        sql = "Delete from items where quantity = 22 "
        cursor.execute(sql)
        conn.commit()
        cursor.close()

def main():
    q = query()
    q.query()

if __name__ == '__main__':
    main()