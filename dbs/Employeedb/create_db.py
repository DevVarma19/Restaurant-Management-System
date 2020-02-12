import sqlite3
class create(object):

    def create(self):
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        sql = '''create table employees(
            name text,
            age number,
            design text
            )'''
        cursor.execute(sql)
        cursor.close()

def main():
    c = create()
    c.create()
if __name__ == '__main__':
    main()