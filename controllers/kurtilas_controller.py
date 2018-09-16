from flask import Blueprint, render_template, request
from models import kurtilas_db

kurtilas = Blueprint("kurtilas", __name__)

def postDataParser(form):
    data = {}
    key = []
    for item in request.form.keys():
        key.append(item)
    for par in key:
        data[par] = form.getlist(par)
    return data

@kurtilas.route('/')
def kurtilas_index():
    return render_template("kurtilas/index.html")

@kurtilas.route('/kompetensi/<kompetensi>')
def kurtilas_kompetensi(kompetensi):
    # TODO : Diperbaiki
    siswa = [
        ["4822","Demitri Saklitunov"],
        ["4826","Virgiawan Listanto"],
        ["4843","Sanny Aura Syahrani"],
        ["4839","Daniswara Zaidan Abhinaya"],
        ["4840","Devina Joelian Salsadillah"]
    ]
    return render_template("kurtilas/kompetensi.html", siswa=siswa, kompetensi=kompetensi)

@kurtilas.route('/nilai/<mapel>/ubah')
def kurtilas_penilaian(mapel):
    data_mapel = kurtilas_db.getMapel(mapel=mapel)
    siswa = kurtilas_db.getSiswa()
    return render_template("kurtilas/nilai/ubah.html", siswa=siswa, mapel=mapel.split('_')[1], data_mapel=data_mapel)

@kurtilas.route('/nilai/<mapel>/simpan', methods=['GET', 'POST'])
def kurtilas_penilaian_simpan(mapel):
    if request.method == 'POST':
        data = postDataParser(request.form)
        # print(data)
        kurtilas_db.saveNilai(data, mapel)
    return "Check console"