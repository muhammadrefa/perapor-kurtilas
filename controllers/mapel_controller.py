from flask import Blueprint, render_template, request
from models import kurtilas_db

mapel = Blueprint("mapel", __name__)

def postDataParser(form):
    data = {}
    key = []
    for item in request.form.keys():
        key.append(item)
    for par in key:
        data[par] = form.getlist(par)
    return data

@mapel.route('/mapel')
def mapel_index():
    data = kurtilas_db.getMapel()
    return render_template("kurtilas/mapel/index.html", mapel=data)

@mapel.route('/mapel/lihat/<mapel>')
def mapel_lihat(mapel):
    data = kurtilas_db.getMapel(mapel=mapel)
    return render_template("kurtilas/mapel/lihat.html", mapel=mapel, data_mapel=data)

@mapel.route('/mapel/ubah/<mapel>')
def mapel_ubah(mapel):
    data = kurtilas_db.getMapel(mapel=mapel)
    return render_template("kurtilas/mapel/ubah.html", mapel=mapel, data_mapel=data)

@mapel.route('/mapel/tambah')
def mapel_tambah():
    # data = kurtilas_db.getMapel(mapel=mapel)
    return render_template("kurtilas/mapel/ubah.html", mapel="mapel_", data_mapel=None)

@mapel.route('/mapel/simpan', methods=['GET', 'POST'])
def siswa_simpan():
    data = []
    if request.method == 'POST':
        data = postDataParser(request.form)
    kurtilas_db.saveMapel(data['data'])
    return "OK"