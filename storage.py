import sqlite3

def get_users():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("select * from users")
    result = cursor.fetchall()
    cursor.close()
    return result

def get_user(id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("select * from users where id=?",(id,))
    result = cursor.fetchall()
    cursor.close()
    return result[0]

def update_status(id, value):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("update users set status=? where id=?",(value, id))
    connection.commit()
    cursor.close()

def create_user(f_name, myemail, msg):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("insert into users (f_name, myemail, msg) values (?,?,?)", (f_name, myemail, msg))
    id = cursor.lastrowid
    connection.commit()
    cursor.close()
    return id

def update_user(id, updated_f_name, updated_myemail, updated_msg):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("update users set f_name=?, myemail=?, msg=? where id=?", (updated_f_name, updated_myemail, updated_msg, id))
    connection.commit()
    cursor.close()

def delete_user(id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("delete from users where id=?", (id,))
    connection.commit()
    cursor.close()

def test_get_users():
    print("testing get_users")
    results = get_users()
    assert type(results) is list
    assert len(results) > 0
    for user in results:
        assert type(user) is tuple
    id, f_name, myemail, msg = results[0]
    assert type(id) is int
    assert type(f_name) is str
    assert type(myemail) is str
    assert type(msg) is int
    assert msg in [0,1]

def test_get_user():
    print("testing get_user(id)")
    results = get_users()
    assert len(results) > 0
    id, f_name, myemail, msg = results[0]
    result = get_user(id)
    assert type(result) is tuple
    id2, f_name2, myemail2, msg2 = result
    assert id2 == id
    assert f_name2 == f_name
    assert myemail2 == myemail
    assert msg2 == msg

if __name__ == "__main__":
    # test_get_users()
    test_get_user()
    print("done.")
