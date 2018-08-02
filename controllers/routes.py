from app import app

from controllers.konfigurasi_controller import konfigurasi
from controllers.terminal_controller import terminal

app.register_blueprint(konfigurasi)
app.register_blueprint(terminal)
