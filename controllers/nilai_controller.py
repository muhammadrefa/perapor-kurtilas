from flask import Blueprint, render_template, request
from models import kurtilas_db

nilai = Blueprint("nilai", __name__)

def postDataParser(form):
    data = {}
    key = []
    for item in request.form.keys():
        key.append(item)
    for par in key:
        data[par] = form.getlist(par)
    return data

@nilai.route('/nilai')
def nilai_index():
    data = kurtilas_db.getMapel()
    return render_template("kurtilas/nilai/index.html", mapel=data)

@nilai.route('/nilai/<mapel>')
def nilai_lihat(mapel):
    pass

@nilai.route('/nilai/<mapel>/ubah')
def nilai_penilaian(mapel):
    data_mapel = kurtilas_db.getMapel(mapel=mapel)
    siswa = kurtilas_db.getSiswa()
    return render_template("kurtilas/nilai/ubah.html", siswa=siswa, mapel=mapel.split('_')[1], data_mapel=data_mapel)

@nilai.route('/nilai/<mapel>/simpan', methods=['GET', 'POST'])
def nilai_penilaian_simpan(mapel):
    if request.method == 'POST':
        data = postDataParser(request.form)
        # print(data)
        kurtilas_db.saveNilai(data, mapel)
    return "Check console"
