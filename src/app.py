from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:Olasoymotopiz777@localhost/proyectoartv1'
app.config['SECRET_KEY'] = 'Olasoymotopiz777'
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/artSupervisor.html')
def art_supervisor():
    return render_template('artSupervisor.html')



@app.route('/login', methods=['POST'])
def login():
    rut = request.form['rut']
    password = request.form['password']
    
    user = Trabajador.query.filter_by(Rut=rut).first()
    if user and check_password_hash(user.Contraseña, password):
        return redirect(url_for('interfaz_trabajador'))
    
    user = Supervisor.query.filter_by(Rut=rut).first()
    if user and check_password_hash(user.Contraseña, password):
        return redirect(url_for('interfaz_supervisor'))
    
    user = Gerente.query.filter_by(Rut=rut).first()
    if user and (user.Contraseña, password):
        return redirect(url_for('interfaz_gerente'))
    
    flash('RUT o contraseña incorrectos', 'error')
    return redirect(url_for('index'))

@app.route('/interfaz_trabajador')
def interfaz_trabajador():
    return render_template('interfazTrabajador.html')

@app.route('/interfaz_supervisor')
def interfaz_supervisor():
    return render_template('interfazSupervisor.html')

@app.route('/interfaz_gerente')
def interfaz_gerente():
    return render_template('gerenteInterfaz.html')
@app.route('/register', methods=['POST'])



@app.route('/register', methods=['POST'])
def register():
    nombre = request.form['nombre']
    rut = request.form['rut']
    correo = request.form['correo']
    password = request.form['password']
    rol = request.form['rol']

    if Trabajador.query.filter_by(Rut=rut).first() or Supervisor.query.filter_by(Rut=rut).first() or Gerente.query.filter_by(Rut=rut).first() or USinConfirmar.query.filter_by(Rut=rut).first():
        flash('El RUT ya está registrado', 'error')
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
        flash('Registro exitoso. Espere la confirmación del administrador.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error en el registro. Por favor, intente de nuevo.', 'error')
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

if __name__ == '__main__':
    app.run(debug=True)