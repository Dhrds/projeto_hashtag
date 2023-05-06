from ds import database, app
from ds.models import Usuario, Foto

with app.app_context():
    database.create_all()