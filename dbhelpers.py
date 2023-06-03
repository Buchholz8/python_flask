import mariadb
import dbcreds

def run_pocedures(sql, args):
    try:
        results = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
    except mariadb.IntegrityError:
        print("Sorry, what you entered doesnt exist")
    except Exception as error:
        print('Error' , error)
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.close()
        return results