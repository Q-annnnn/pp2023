import sqlite3


def add(account, name, manufacturer, model, serial_num, firmware_vers, calibration, usage_count):
    """Add all the information of the 3D printer"""
    con = sqlite3.connect('3d_printer_machine_management.db')
    cur = con.cursor()
    cur.execute(f"""
CREATE TABLE IF NOT EXISTS printerFor_{account}(id INTEGER PRIMARY KEY,
                                  name TEXT,
                                  manufacturer TEXT,
                                  model TEXT,
                                  serial_num TEXT,
                                  firmware_vers TEXT,
                                  calibration TEXT,
                                  usage_count TEXT)""")
    cur.execute(f"""
INSERT INTO printerFor_{account}(name, manufacturer, model, serial_num, firmware_vers, calibration, usage_count)
VALUES (?, ?, ?, ?, ?, ?, ?);""", (str(name), str(manufacturer), str(model), str(serial_num), str(firmware_vers), str(calibration), str(usage_count)))
    con.commit()
    con.close()

def display(account):
    """Display all the data of the user"""
    con = sqlite3.connect('3d_printer_machine_management.db')
    cur = con.cursor()
    cur.execute(f"""
SELECT * FROM printerFor_{account}""")
    data = cur.fetchall()
    con.commit()
    con.close()
    return data

def update(account, id, name, manufacturer, model, serial_num, firmware_vers, calibration, usage_count):
    """To update information in database

    Args:
        id: id of the printer
        account: account of the users
        name: name of a printer
        manufacturer: manufacturer of a printer
        serial_num: serial number of a printer
        firmware_vers: firmware version of a printer
        calibration: calibration of a printer
        usage_count: number of usages of a printer
    """
    con = sqlite3.connect('3d_printer_machine_management.db')
    cur = con.cursor()
    cur.execute(f"""
UPDATE printerFor_{account}
SET name = ?,
    manufacturer = ?,
    model = ?,
    serial_num = ?,
    firmware_vers = ?,
    calibration = ?
    usage_count = ?
WHERE id = {id};""", (name, manufacturer, model, serial_num, firmware_vers, calibration, usage_count))
    con.commit()
    con.close()

def delete(account, id):
    """Delete specific data based on the id of printer"""
    con = sqlite3.connect('3d_printer_machine_management.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM printerFOR_{account} WHERE id = {id}")
    con.commit()
    con.close()

def delete_all(account):
    """Delete all the data"""
    con = sqlite3.connect('3d_printer_machine_management.db')
    cur = con.cursor()
    cur.execute(f"DROP TABLE IF EXISTS printerFor_{account}")
    cur.execute(f"""
CREATE TABLE IF NOT EXISTS printerFor_{account}(id INTEGER PRIMARY KEY,
                                 name TEXT,
                                 manufacturer TEXT,
                                 model TEXT,
                                 serial_num TEXT,
                                 firmware_vers TEXT,
                                 calibration TEXT
                                 usage_count TEXT)""")
    con.commit()
    con.close()

def search(account, type_of_search, search):
    """
    Args:
        account (_type_): account of the user
        type_of_search (_type_): choose the attribute you want to search
        search (_type_): search the content of that attribute
    
    Returns:
        data: return the data you want to search
    """

    con = sqlite3.connect('3d_printer_machine_management.db')
    cur = con.cursor()
    search_command = f"SELECT * FROM printerFOR_{account} WHERE {type_of_search} LIKE '%{search}'"
    cur.execute(search_command)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data




