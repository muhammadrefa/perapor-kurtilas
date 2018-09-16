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

def saveMapel(mapel, data, aksi):
    to_save = []
    for i in range(0, len(data['p_nokd'])):
        to_save.append([data['p_nokd'][i], 'pengetahuan', data['p_kd'][i]])
    for i in range(0, len(data['k_nokd'])):
        to_save.append([data['k_nokd'][i], 'keterampilan', data['k_kd'][i]])

    conn, c = dbConn()

    if aksi == "ubah" or aksi == "hapus":
        try:
            c.execute("DROP TABLE `" + mapel + "`")
        except:
            pass
    if aksi != "hapus":
        c.execute("CREATE TABLE `" + mapel + "` (`nokd` INTEGER, `jenis` TEXT, `kd` TEXT)")
        c.executemany("INSERT INTO `" + mapel + "` VALUES (?,?,?)", (to_save))

    conn.commit()
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

def saveNilai(data, mapel):
    to_save = []
    kd = ['nipd']
    db_mapel = getMapel(mapel)
    for data_mapel in db_mapel[0]:
        kd.append(str(data_mapel[0]))
    for data_mapel in db_mapel[1]:
        kd.append(str(data_mapel[0]))
    i = 0
    for x in data:
        to_save.append([])
        to_save[i].append(x)
        for y in data[x]:
            to_save[i].append(y)
        i+=1
    mapel = mapel.split('_')[1]
    print("mapel -> " + mapel)
    print(kd)
    print(to_save)

    conn, c = dbConn()
    try:
        c.execute("DROP TABLE `nilai_" + mapel + "`")
    except:
        pass

    statement = ""
    wildcard = ""
    for i in kd:
        statement += "`" + i + "` INTEGER,"
        wildcard += "?,"
    statement = statement[:-1]
    wildcard = wildcard[:-1]
    c.execute("CREATE TABLE `nilai_" + mapel + "` (" + statement + ")")
    c.executemany("INSERT INTO `nilai_" + mapel + "` VALUES (" + wildcard + ")", (to_save))
    conn.commit()
    c.close()
    conn.close()
