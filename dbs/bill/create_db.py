import sqlite3
class create(object):

    def create(self):
        conn = sqlite3.connect('Bills.db')
        cursor = conn.cursor()
        sql = '''create table bills(
            orderno text,
            date text,
            time text,
            amount number)'''
        cursor.execute(sql)
        cursor.close()

def main():
    c = create()
    c.create()
if __name__ == '__main__':
    main()