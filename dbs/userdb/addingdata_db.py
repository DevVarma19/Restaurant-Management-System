import sqlite3
class adding(object):

    def add(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        print("Let's Input some users!")
        while True:
            name = input("Users's name:")
            username = input("Users's username:")
            password = input("Users's password:")
            sql = '''insert into users
                        (name,username,password)
                        values
                        (:us_name, :us_username, :pass)'''
            cursor.execute(sql,{'us_name':name,'us_username':username,'pass':password})
            conn.commit()
            cont = input("Another User?")
            if cont[0].lower() == 'n':
                break
        cursor.close()

def main():
    a = adding()
    a.add()

if __name__ == '__main__':
    main()