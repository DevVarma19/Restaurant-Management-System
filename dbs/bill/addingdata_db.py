import sqlite3
class adding(object):

    def add(self):
        conn = sqlite3.connect('Bills.db')
        cursor = conn.cursor()
        print("Let's Input some users!")
        while True:
            name = input("Users's date:")
            username = input("Users's time:")
            password = input("Users's bill:")
            sql = '''insert into bills
                        (date,time,amount)
                        values
                        (:us_name, :us_username, :pass)'''
            cursor.execute(sql,{'us_name':name,'us_username':username,'pass':password})
            conn.commit()
            cont = input("Another input?")
            if cont[0].lower() == 'n':
                break
        cursor.close()

def main():
    a = adding()
    a.add()

if __name__ == '__main__':
    main()