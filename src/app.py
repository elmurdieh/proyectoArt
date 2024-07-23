from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from functools import wraps
from datetime import datetime
from datetime import datetime, timezone
import pytz

#aca se hace la conexion a la base de datos
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:Olasoymotopiz777@localhost/proyectoartv1' # usuario/contraseña/localhost dejarlo como esta/nombre de la DB
app.config['SECRET_KEY'] = '78808261'
db = SQLAlchemy(app)

class Trabajador(db.Model):
    __tablename__ = 'trabajador'
    Rut = db.Column(db.String(12), primary_key=True)
    Nombre = db.Column(db.String(300), nullable=False)
    Cargo = db.Column(db.String(50),nullable=False)
    Correo_electronico = db.Column(db.String(300), nullable=False)
    Contraseña = db.Column(db.String(300), nullable=False)

class Supervisor(db.Model):
    __tablename__ = 'supervisor'
    Rut = db.Column(db.String(12), primary_key=True)
    Nombre = db.Column(db.String(300), nullable=False)
    Cargo = db.Column(db.String(50),nullable=False)
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
    Cargo = db.Column(db.String(50),nullable=False)
    Contraseña = db.Column(db.String(255), nullable=False)
    Correo_electronico = db.Column(db.String(255), nullable=False)
    Rol = db.Column(db.String(25), nullable=False)

class Art(db.Model):
    __tablename__ = 'art'
    Art_id = db.Column(db.Integer, primary_key=True)
    Fecha_creacion = db.Column(db.String(30), nullable=False)
    Hora_creacion = db.Column(db.String(30), nullable=False)
    Estado_cierre = db.Column(db.String(100), nullable=True)
    Supervisor_rut = db.Column(db.String(12), nullable=False)


class ArtResSup(db.Model):
    __tablename__ = 'art_res_sup'
    Art_id = db.Column(db.Integer, db.ForeignKey('art.Art_id'), primary_key=True)
    Supervisor_rut = db.Column(db.String(12), nullable=False)
    Sup_asignado = db.Column(db.String(100), nullable=False)
    Gerencia = db.Column(db.String(100), nullable=False)
    Superintendencia = db.Column(db.String(100), nullable=False)
    Trab_realizar = db.Column(db.String(100), nullable=False)
    Lug_esp = db.Column(db.String(100), nullable=False)
    Empresa = db.Column(db.String(100), nullable=False)
    Fecha = db.Column(db.String(30), nullable=False)
    Hora_inicio = db.Column(db.String(15), nullable=False)
    Hora_termino = db.Column(db.String(15), nullable=False)
    Pre_trans_1 = db.Column(db.Boolean, nullable=False)
    Pre_trans_2 = db.Column(db.Boolean, nullable=False)
    Pre_trans_3 = db.Column(db.Boolean, nullable=False)
    Pre_trans_4 = db.Column(db.Boolean, nullable=False)
    Pre_trans_5 = db.Column(db.Boolean, nullable=False)
    Pre_trans_6 = db.Column(db.Boolean, nullable=False)
    Trab_sim_1 = db.Column(db.Boolean, nullable=False)
    Trab_sim_2 = db.Column(db.String(100), nullable=True) # El "nullable=True" evitara errores en caso de que la respuesta de Trab_sim_1 sea false
    Trab_sim_3 = db.Column(db.Boolean, nullable=False)
    Trab_sim_4 = db.Column(db.Boolean, nullable=False)
    Trab_sim_5 = db.Column(db.Boolean, nullable=False)   

class Trabajadores_asignados(db.Model):
    __tablename__ = 'trabajadores_asignados'
    Art_id = db.Column(db.Integer, db.ForeignKey('art.Art_id'), primary_key=True)
    Trabajador_rut = db.Column(db.String(12), db.ForeignKey('trabajador.Rut'), primary_key=True)
    Estado_firma_trabajador = db.Column(db.Boolean, nullable=True)

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
    if user and (user.Contraseña, password):
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

@app.route('/interfaz_trabajador/artTrabajador')
@login_required
@role_required('trabajador')
def art_trabajador_view():
    return render_template('artTrabajador.html')

@app.route('/interfaz_supervisor')
@login_required
@role_required('supervisor')
def interfaz_supervisor():
    user_id = session['user_id']
    user = Supervisor.query.get(user_id)
    return render_template('interfazSupervisor.html',nombre=user.Nombre)


@app.route('/interfazSupervisor/artSupervisor')
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
    def calcular_digito_verificador(rut_sin_dv):
        rut_reverso = list(map(int, reversed(rut_sin_dv)))
        multiplicadores = [2, 3, 4, 5, 6, 7]
        suma = sum(d * multiplicadores[i % len(multiplicadores)] for i, d in enumerate(rut_reverso))
        resto = suma % 11
        dv = 11 - resto
        if dv == 11:
            return '0'
        elif dv == 10:
            return 'K'
        else:
            return str(dv)
    def verificar_rut(rut_completo):
        try:
            rut_numero, rut_dv = rut_completo.strip().upper().split('-')
        except ValueError:
            return False
        if not rut_numero.isdigit():
            return False
        dv_calculado = calcular_digito_verificador(rut_numero)

        return dv_calculado == rut_dv
    
    nombre = request.form['nombre']
    rut = request.form['rut']
    correo = request.form['correo']
    cargo = request.form['cargo']
    password = request.form['password']
    rol = request.form['rol']
    
    if verificar_rut(rut):
        print(f"El RUT {rut} es válido.")
    else:
        print(f"El RUT {rut} no es válido.")
        return redirect(url_for('index'))


    if Trabajador.query.filter_by(Rut=rut).first() or Supervisor.query.filter_by(Rut=rut).first() or Gerente.query.filter_by(Rut=rut).first() or USinConfirmar.query.filter_by(Rut=rut).first():
        print('El RUT ya está registrado', 'error')
        return redirect(url_for('index'))

    nuevo_usuario = USinConfirmar(
        Nombre=nombre,
        Rut=rut,
        Correo_electronico=correo,
        Cargo=cargo,
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

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Elimina el ID del usuario de la sesión
    return redirect(url_for('index'))  # Redirige a la página de inicio de sesión o a otra página adecuada

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
@app.route('/get_arts_supervisor')
@login_required
@role_required('supervisor')
def get_arts_supervisor():
    user_rut = session['user_id']
    arts = Art.query.filter_by(Supervisor_rut=user_rut).all()
    
    results = []
    for art in arts:
        # Obtener los trabajadores asignados al Art
        trabajadores_asignados = Trabajadores_asignados.query.filter_by(Art_id=art.Art_id).all()
        trabajadores_nombres = [
            Trabajador.query.get(trabajador.Trabajador_rut).Nombre for trabajador in trabajadores_asignados
        ]
        
        results.append({
            'Art_id': art.Art_id,
            'Fecha_creacion': art.Fecha_creacion,
            'Trabajadores_asignados': trabajadores_nombres,
            'Estado_cierre': art.Estado_cierre
        })
    
    return jsonify(results)
@app.route('/get_arts_trabajador')
@login_required
@role_required('trabajador')
def get_arts_trabajador():
    user_rut = session['user_id']
    
    # Obtener los arts donde el trabajador está asignado
    arts_trabajador = Trabajadores_asignados.query.filter_by(Trabajador_rut=user_rut).all()
    
    results = []
    for art_trabajador in arts_trabajador:
        art = Art.query.get(art_trabajador.Art_id)
        art_res_sup = ArtResSup.query.get(art_trabajador.Art_id)
        
        # Obtener los trabajadores asignados al Art
        trabajadores_asignados = Trabajadores_asignados.query.filter_by(Art_id=art.Art_id).all()
        trabajadores_nombres = [
            Trabajador.query.get(trabajador.Trabajador_rut).Nombre for trabajador in trabajadores_asignados
        ]
        
        results.append({
            'Art_id': art.Art_id,
            'Fecha_creacion': art.Fecha_creacion,
            'Lug_esp': art_res_sup.Lug_esp,
            'Trabajadores_asignados': trabajadores_nombres,
            'Estado_cierre': art.Estado_cierre
        })
    
    return jsonify(results)

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
            Cargo = user.Cargo,
            Correo_electronico=user.Correo_electronico,
            Contraseña=user.Contraseña
        )
    elif user.Rol == 'trabajador':
        new_user = Trabajador(
            Rut=user.Rut,
            Nombre=user.Nombre,
            Cargo = user.Cargo,
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

@app.route('/get_workers')
@login_required
@role_required('supervisor')
def get_workers():
    user_rut = session['user_id']
    trabajadores = Trabajador.query.all()
    # Puedes devolver los datos en el formato que prefieras, por ejemplo, como JSON
    return jsonify([
        {
            'Nombre': trabajador.Nombre,
            'Rut' : trabajador.Rut
        } for trabajador in trabajadores
    ])
@app.route('/guardar_trabajadores', methods=['POST'])
def guardar_trabajadores():
    data = request.json
    trabajadores = data.get('trabajadores', [])

    if not trabajadores:
        return jsonify({'error': 'No se enviaron trabajadores'}), 400

    session['trabajadores'] = trabajadores
    return jsonify({'message': 'Trabajadores almacenados en la sesión'})
#aca se guardan las respuestas en la db 

@app.route('/guardar_encuesta_trabajador', methods=['POST'])
@login_required
@role_required('trabajador')
def guardar_encuesta_supervisor():
    pass

@app.route('/guardar_encuesta', methods=['POST'])
@login_required
@role_required('supervisor')

#se toman las respuestas del html segun el nombre
def guardar_encuesta():
    supervisor_rut = session['user_id']
    supervisor_asignado = request.form.get('sup_asignado')
    empresa = request.form.get('empresa')
    gerencia = request.form.get('gerencia')
    fecha = request.form.get('fecha')
    superintendencia_direccion = request.form.get('superintendencia_direccion')
    hora_inicio = request.form.get('hora_inicio')
    trabajo_realizar = request.form.get('trabajo_realizar')
    hora_termino = request.form.get('hora_termino')
    lugar_especifico = request.form.get('lugar_especifico')
    pretrans1 = int(request.form.get('grupo2-1'))
    pretrans2 = int(request.form.get('grupo2-2'))
    pretrans3 = int(request.form.get('grupo2-3'))
    pretrans4 = int(request.form.get('grupo2-4'))
    pretrans5 = int(request.form.get('grupo2-5'))
    pretrans6 = int(request.form.get('grupo2-6'))
    trabsim1 = int(request.form.get('grupo4-1-1'))
    trabsim2 = request.form.get('tra-sim')
    trabsim3 = int(request.form.get('grupo4-2-1'))
    trabsim4 = int(request.form.get('grupo4-3-1'))
    trabsim5 = int(request.form.get('grupo4-4-1'))

    # Definir la zona horaria de Chile
    chile_tz = pytz.timezone('Chile/Continental')
    now_chile = datetime.now(chile_tz)

    # Crear una instancia del modelo Art con los atributos correctos
    nuevo_art = Art(
        Fecha_creacion=now_chile.strftime('%Y-%m-%d'),
        Hora_creacion=now_chile.strftime('%H:%M:%S'),
        Estado_cierre=None,  # (Aun sin implementar) El estado cierre se tiene sera True cuando todos los trabajadores hayan firmador(aun sin implementar)
        Supervisor_rut=supervisor_rut
    )

    try:
        db.session.add(nuevo_art)
        db.session.commit()  # Commit para obtener el Art_id generado
        db.session.refresh(nuevo_art)  # Refrescar para obtener el Art_id asignado
        
        # Crear una instancia del modelo ArtResSup con el Art_id generado
        nuevo_art_res_sup = ArtResSup(
            Art_id=nuevo_art.Art_id,  # Asignar el Art_id generado
            Supervisor_rut=supervisor_rut,
            Sup_asignado=supervisor_asignado,
            Gerencia=gerencia,
            Superintendencia=superintendencia_direccion,
            Trab_realizar=trabajo_realizar,
            Lug_esp=lugar_especifico,
            Empresa=empresa,
            Fecha=fecha,
            Hora_inicio=hora_inicio,
            Hora_termino=hora_termino,
            Pre_trans_1 = pretrans1,
            Pre_trans_2 = pretrans2,
            Pre_trans_3 = pretrans3,
            Pre_trans_4 = pretrans4,
            Pre_trans_5 = pretrans5,
            Pre_trans_6 = pretrans6,
            Trab_sim_1 = trabsim1,
            Trab_sim_2 = trabsim2,
            Trab_sim_3 = trabsim3,
            Trab_sim_4 = trabsim4,
            Trab_sim_5 = trabsim5 
        )

        db.session.add(nuevo_art_res_sup)

        trabajadores = session.get('trabajadores', [])
        for trabajador in trabajadores:
            nuevo_art_trabajadores = Trabajadores_asignados(
                Art_id=nuevo_art.Art_id,
                Trabajador_rut=trabajador
            )
            db.session.add(nuevo_art_trabajadores)

        db.session.commit()
        print('ART y ART Res Sup creados exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        print('Error al crear el ART. Por favor, intente de nuevo.', 'error')
        print(str(e))

    return redirect(url_for('art_supervisor_view'))



if __name__ == '__main__':
    app.run(debug=True)