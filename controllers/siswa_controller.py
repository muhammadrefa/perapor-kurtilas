from flask import Blueprint, render_template, request
from models import kurtilas_db

siswa = Blueprint("siswa", __name__)

def postDataParser(form):
    data = {}
    key = []
    for item in request.form.keys():
        key.append(item)
    for par in key:
        data[par] = form.getlist(par)
    return data

@siswa.route('/siswa')
@siswa.route('/siswa/lihat')
def siswa_index():
    siswa = kurtilas_db.getSiswa()
    return render_template("kurtilas/siswa/index.html", data_siswa=siswa)

@siswa.route('/siswa/tambah')
def siswa_tambah():
    data = [[]]
    for i in range(0,20): data[0].append(None)
    return render_template("kurtilas/siswa/ubah.html", data=data)

@siswa.route('/siswa/ubah/<nipd>')
def siswa_ubah(nipd):
    data = kurtilas_db.getSiswa(nipd=nipd)
    return render_template("kurtilas/siswa/ubah.html", data=data, ubah=True)

@siswa.route('/siswa/simpan', methods=['GET', 'POST'])
def siswa_simpan():
    data = []
    if request.method == 'POST':
        data = postDataParser(request.form)
    res = kurtilas_db.saveSiswa(data['data'], data['aksi'][0])
    if res:
        return "OK"
    else:
        return "NOK"

@siswa.route('/siswa/lihat/<nipd>')
def siswa_lihat(nipd):
    siswa = kurtilas_db.getSiswa(nipd=nipd)
    return render_template("kurtilas/siswa/lihat.html", data_siswa=siswa)

@siswa.route('/siswa/hapus/<nipd>')
def siswa_hapus(nipd):
    res = kurtilas_db.saveSiswa(data=nipd, aksi="hapus")
    if res:
        return "OK"
    else:
        return "NOK"
