

def ajouter(conn,add_values_nom,add_values_num,add_values_mail):
    cursor = conn.cursor()
    add = "INSERT INTO repertoire (name,phone_number,email) VALUES (%s,%s,%s)"
    add_values = (add_values_nom,add_values_num,add_values_mail)
    cursor.execute(add,add_values)
    conn.commit()
    cursor.close()

        
def lists(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM repertoire")
    affiche = cur.fetchall()
    cur.close()
    
    return affiche


def search_one(conn,name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM repertoire WHERE name = %s",(name,))
    affichage = cursor.fetchall()
    cursor.close()
    return affichage
    
def search_num(conn,search_num):
    cur = conn.cursor()
    cur.execute("SELECT * FROM repertoire WHERE phone_number = %s",(search_num,))
    search = cur.fetchall()
    cur.close()
    return search

def update_contact(conn,nom,numero,mail,nameMj):
    cur = conn.cursor()
    cur.execute("UPDATE repertoire SET name = %s, phone_number = %s, email = %s WHERE name = %s",(nom, numero, mail, nameMj))
    conn.commit()
    cur.close()


def delete_contact(conn,name_del):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM repertoire WHERE name = %s",(name_del,))
    conn.commit()
    cursor.close()

