from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from functools import wraps
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:Olasoymotopiz777@localhost/proyectoartv1'
app.config['SECRET_KEY'] = '78808261'
db = SQLAlchemy(app)

class Trabajador(db.Model):
    __tablename__ = 'trabajador'
    Rut = db.Column(db.String(12), primary_key=True)
    Nombre = db.Column(db.String(300), nullable=False)
    Correo_electronico = db.Column(db.String(300), nullable=False)
    Contraseña = db.Column(db.String(300), nullable=False)

class Supervisor(db.Model):
    __tablename__ = 'supervisor'
    Rut = db.Column(db.String(12), primary_key=True)
    Nombre = db.Column(db.String(300), nullable=False)
    Correo_electronico = db.Column(db.String(300), nullable=False)
    Contraseña = db.Column(db.String(300), nullable=False)

class Gerente(db.Model):
    __tablename__ = 'gerente'
    Rut = db.Column(db.String(12), primary_key=True)
    Nombre = db.Column(db.String(300), nullable=False)
    Correo_electronico = db.Column(db.String(300), nullable=False)
    Contraseña = db.Column(db.String(300), nullable=False)

class USinConfirmar(db.Model):
    __tablename__ = 'u_sinconfirmar'
    Rut = db.Column(db.String(12), primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Contraseña = db.Column(db.String(255), nullable=False)
    Correo_electronico = db.Column(db.String(255), nullable=False)
    Rol = db.Column(db.String(25), nullable=False)

class Art(db.Model):
    __tablename__ = 'art'
    id = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)

class ArtResSup(db.Model):
    __tablename__ = 'art_res_sup'
    id = db.Column(db.Integer, primary_key=True)
    art_id = db.Column(db.Integer, db.ForeignKey('art.id'), nullable=False)
    sup_asignado = db.Column(db.String(100), nullable=False)
    empresa = db.Column(db.String(100), nullable=False)
    gerencia = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    superintendencia_direccion = db.Column(db.String(100), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    trabajo_realizar = db.Column(db.String(100), nullable=False)
    hora_termino = db.Column(db.Time, nullable=False)
    lugar_especifico = db.Column(db.String(100), nullable=False)
    art = db.relationship('Art', backref=db.backref('art_res_sup', lazy=True))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            print('Debes iniciar sesión para acceder a esta página.', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get('role') != role:
                print('No tienes permisos para acceder a esta página.', 'error')
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    rut = request.form['rut']
    password = request.form['password']
    
    user = Trabajador.query.filter_by(Rut=rut).first()
    if user and check_password_hash(user.Contraseña, password):
        session['user_id'] = user.Rut
        session['role'] = 'trabajador'
        return redirect(url_for('interfaz_trabajador'))
    
    user = Supervisor.query.filter_by(Rut=rut).first()
    if user and check_password_hash(user.Contraseña, password):
        session['user_id'] = user.Rut
        session['role'] = 'supervisor'
        return redirect(url_for('interfaz_supervisor'))
    
    user = Gerente.query.filter_by(Rut=rut).first()
    if user and check_password_hash(user.Contraseña, password):
        session['user_id'] = user.Rut
        session['role'] = 'gerente'
        return redirect(url_for('interfaz_gerente'))
    
    print('RUT o contraseña incorrectos', 'error')
    return redirect(url_for('index'))

def identificador():
    pass

@app.route('/interfaz_trabajador')
@login_required
@role_required('trabajador')
def interfaz_trabajador():
    user_id = session['user_id']
    user = Trabajador.query.get(user_id)
    return render_template('interfazTrabajador.html',nombre=user.Nombre)

@app.route('/interfaz_supervisor')
@login_required
@role_required('supervisor')
def interfaz_supervisor():
    user_id = session['user_id']
    user = Supervisor.query.get(user_id)
    return render_template('interfazSupervisor.html',nombre=user.Nombre)

@app.route('/interfaz_supervisor/artSupervisor')
@login_required
@role_required('supervisor')
def art_supervisor_view():
    return render_template('artSupervisor.html')

@app.route('/interfaz_gerente')
@login_required
@role_required('gerente')
def interfaz_gerente():
    user_id = session['user_id']
    user = Gerente.query.get(user_id)
    return render_template('gerenteInterfaz.html',nombre=user.Nombre)


@app.route('/register', methods=['POST'])



@app.route('/register', methods=['POST'])
def register():
    nombre = request.form['nombre']
    rut = request.form['rut']
    correo = request.form['correo']
    password = request.form['password']
    rol = request.form['rol']

    if Trabajador.query.filter_by(Rut=rut).first() or Supervisor.query.filter_by(Rut=rut).first() or Gerente.query.filter_by(Rut=rut).first() or USinConfirmar.query.filter_by(Rut=rut).first():
        print('El RUT ya está registrado', 'error')
        return redirect(url_for('index'))

    nuevo_usuario = USinConfirmar(
        Nombre=nombre,
        Rut=rut,
        Correo_electronico=correo,
        Contraseña=generate_password_hash(password),
        Rol=rol
    )

    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        print('Registro exitoso. Espere la confirmación del administrador.', 'success')
    except Exception as e:
        db.session.rollback()
        print('Error en el registro. Por favor, intente de nuevo.', 'error')
        print(str(e)) 

    return redirect(url_for('index'))

@app.route('/get_unconfirmed_users')
def get_unconfirmed_users():
    users = USinConfirmar.query.all()
    return jsonify([
        {
            'Nombre': user.Nombre,
            'Rut': user.Rut,
            'Correo_electronico': user.Correo_electronico,
            'Rol': user.Rol
        } for user in users
    ])

@app.route('/approve_user', methods=['POST'])
def approve_user():
    data = request.json
    rut = data.get('rut')
    
    print(f"Attempting to approve user with RUT: {rut}")
    
    user = USinConfirmar.query.get(rut)
    if not user:
        print(f"User with RUT {rut} not found")
        return jsonify({'error': 'Usuario no encontrado'}), 404

    print(f"User found: {user.Nombre}, Role: {user.Rol}")

    if user.Rol == 'supervisor':
        new_user = Supervisor(
            Rut=user.Rut,
            Nombre=user.Nombre,
            Correo_electronico=user.Correo_electronico,
            Contraseña=user.Contraseña
        )
    elif user.Rol == 'trabajador':
        new_user = Trabajador(
            Rut=user.Rut,
            Nombre=user.Nombre,
            Correo_electronico=user.Correo_electronico,
            Contraseña=user.Contraseña
        )
    else:
        print(f"Invalid role: {user.Rol}")
        return jsonify({'error': 'Rol no válido'}), 400

    try:
        db.session.add(new_user)
        db.session.delete(user)
        db.session.commit()
        print(f"User {user.Nombre} approved successfully")
        return jsonify({'message': 'Usuario aprobado con éxito'}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error approving user: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/guardar_encuesta', methods=['POST'])
@login_required
@role_required('supervisor')
def guardar_encuesta():
    sup_asignado = request.form['sup_asignado']
    empresa = request.form['empresa']
    gerencia = request.form['gerencia']
    fecha = request.form['fecha']
    superintendencia_direccion = request.form['superintendencia_direccion']
    hora_inicio = request.form['hora_inicio']
    trabajo_realizar = request.form['trabajo_realizar']
    hora_termino = request.form['hora_termino']
    lugar_especifico = request.form['lugar_especifico']

    nuevo_art = Art(nombre=trabajo_realizar, fecha_creacion=datetime.utcnow())
    db.session.add(nuevo_art)
    db.session.commit()

    nuevo_art_res_sup = ArtResSup(
        art_id=nuevo_art.id,
        sup_asignado=sup_asignado,
        empresa=empresa,
        gerencia=gerencia,
        fecha=fecha,
        superintendencia_direccion=superintendencia_direccion,
        hora_inicio=hora_inicio,
        trabajo_realizar=trabajo_realizar,
        hora_termino=hora_termino,
        lugar_especifico=lugar_especifico
    )
    db.session.add(nuevo_art_res_sup)
    db.session.commit()

    return redirect(url_for('art_supervisor_view'))


if __name__ == '__main__':
    app.run(debug=True)