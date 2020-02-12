import sqlite3
class adding(object):

    def add(self):
        conn = sqlite3.connect('ingredient.db')
        cursor = conn.cursor()
        print("Let's Input some Ingredients!")
        while True:
            type = input("ingredient's name:")
            quantity = input("Quantity :")
            sql = '''insert into items
                        (type,quantity)
                        values
                        (:us_type, :us_qty)'''
            cursor.execute(sql,{'us_type':type,'us_qty':quantity})
            conn.commit()
            cont = input("Another Ingredient?")
            if cont[0].lower() == 'n':
                break
        cursor.close()

def main():
    a = adding()
    a.add()

if __name__ == '__main__':
    main()