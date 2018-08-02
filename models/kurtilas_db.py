import sqlite3

def dbConn():
    conn = sqlite3.connect('data/kurtilas.db')
    c = conn.cursor()
    return conn, c

def getMapel(mapel=None, jenis=None):
    data_mapel = []
    conn, c = dbConn()
    if mapel == None:
        for item in c.execute(
                "SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name LIKE 'mapel_%'"):
            data_mapel.append(item)
    else:
        if jenis==None:
            data_mapel.append([])
            for item in c.execute(
                "SELECT * FROM " + mapel + " WHERE jenis='pengetahuan'"):
                data_mapel[0].append(item)
            data_mapel.append([])
            for item in c.execute(
                "SELECT * FROM " + mapel + " WHERE jenis='keterampilan'"):
                data_mapel[1].append(item)
        else:
            for item in c.execute(
                "SELECT * FROM " + mapel + " WHERE jenis='" + jenis + "'"):
                data_mapel.append(item)
    c.close()
    conn.close()
    return data_mapel

def saveMapel():
    # TODO : Dikerjakan
    conn, c = dbConn()
    c.close()
    conn.close()
    return True

def getSiswa(nipd=None):
    data_siswa = []
    conn, c = dbConn()
    if nipd==None:
        for item in c.execute("SELECT * FROM siswa"):
            data_siswa.append(item)
    else:
        for item in c.execute("SELECT * FROM siswa WHERE nipd='" + str(nipd) + "'"):
            data_siswa.append(item)
    return data_siswa

def saveSiswa(data, aksi):
    if aksi != "hapus":
        if len(data) != 20:
            return False
        # Swap data
        data[0], data[1], data[2] = data[1], data[2], data[0]
        nipd = data[0]
    else:
        nipd = data
    conn, c = dbConn()
    if aksi == "ubah" or aksi == "hapus":
        c.execute("DELETE FROM siswa WHERE nipd = ?", (nipd,))
    if aksi != "hapus":
        c.execute("INSERT INTO siswa VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
    conn.commit()
    c.close()
    conn.close()
    return True
