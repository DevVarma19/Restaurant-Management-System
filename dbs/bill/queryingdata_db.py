import sqlite3

class query(object):

    def query(self):
        conn = sqlite3.connect('Bills.db')
        cursor = conn.cursor()
        sql = "select * from bills"
        results = cursor.execute(sql)
        users = results.fetchall()
        print(users)

def main():
    q = query()
    q.query()

if __name__ == '__main__':
    main()