import sqlite3

class query(object):

    def query(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        sql = "select * from users"
        results = cursor.execute(sql)
        users = results.fetchall()
        for user in users:
            print(user)

def main():
    q = query()
    q.query()

if __name__ == '__main__':
    main()