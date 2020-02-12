import sqlite3

class query(object):

    def query(self):
        conn = sqlite3.connect('Bills.db')
        cursor = conn.cursor()
        sql = "Delete from bills where orderno = "
        cursor.execute(sql)
        conn.commit()
        cursor.close()

def main():
    q = query()
    q.query()

if __name__ == '__main__':
    main()