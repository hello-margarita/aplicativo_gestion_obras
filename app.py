from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from modelos.trabajador import Obrero, Ingeniero, Arquitecto
from modelos.material import Material
from modelos.obra import Obra

app = Flask(__name__)

# Datos de ejemplo al iniciar la aplicación.
lista_obras = []

def inicializar_datos():
    if lista_obras:
        return

    obra1 = Obra("Edificio Central", "Avenida Principal 123", codigo="OBR-2026-001", presupuesto=500000000, fecha_inicio="01/02/2026", fecha_fin="30/04/2026", porcentaje_avance=45, estado='En ejecución')
    obra1.agregar_trabajador(Arquitecto("Lucía Gómez", "16.567.098", 2800000, fecha_ingreso="12/03/2025", estado_laboral="Activo", cargo="Director de Obra"))
    obra1.agregar_trabajador(Ingeniero("Martín Pérez", "16.567.099", 2600000, fecha_ingreso="02/08/2024", estado_laboral="Activo", cargo="Ingeniero Residente"))
    obra1.agregar_trabajador(Obrero("Ana Torres", "16.567.100", 1350000, fecha_ingreso="20/11/2025", estado_laboral="Activo", cargo="Oficial"))
    obra1.agregar_trabajador(Obrero("Carlos Meza", "16.567.104", 1100000, fecha_ingreso="15/05/2025", estado_laboral="Activo", cargo="Ayudante Práctico"))
    obra1.agregar_material(Material("Cemento", "saco", 25000, 100))
    obra1.agregar_material(Material("Ladrillo", "unidad", 500, 2000))

    obra2 = Obra("Ampliación Hospital", "Calle Salud 456", codigo="OBR-2026-002", presupuesto=350000000, fecha_inicio="15/01/2026", fecha_fin="30/04/2026", porcentaje_avance=72, estado='Liquidada')
    obra2.agregar_trabajador(Arquitecto("Carolina Ruiz", "16.567.101", 2700000, fecha_ingreso="10/01/2024", estado_laboral="Activo", cargo="Arquitecto Residente"))
    obra2.agregar_trabajador(Ingeniero("Diego Sánchez", "16.567.102", 2450000, fecha_ingreso="05/06/2023", estado_laboral="Activo", cargo="SISO"))
    obra2.agregar_trabajador(Obrero("José Díaz", "16.567.103", 1250000, fecha_ingreso="28/02/2022", estado_laboral="Retirado", cargo="Ayudante"))
    obra2.agregar_trabajador(Obrero("Sandra López", "16.567.105", 1400000, fecha_ingreso="18/09/2025", estado_laboral="Activo", cargo="Ayudante Práctico"))
    obra2.agregar_material(Material("Acero", "tonelada", 4500000, 5))
    obra2.agregar_material(Material("Tubería PVC", "metro", 12000, 500))

    obra3 = Obra("Adecuación ascensores bodegas 2 y 6", "Centro Comercial Chipichape, Cali - Valle del Cauca", codigo="OBR-2026-003", presupuesto=217865000, fecha_inicio="10/09/2025", fecha_fin="15/08/2026", porcentaje_avance=65, estado='En ejecución')
    obra3.agregar_trabajador(Arquitecto("Andrés Varón Cisneros", "16.789.234", 3200000, fecha_ingreso="10/09/2025", estado_laboral="Activo", cargo="Director de Obra"))
    obra3.agregar_trabajador(Ingeniero("Margarita Arango Vélez", "31.456.789", 2800000, fecha_ingreso="10/09/2025", estado_laboral="Activo", cargo="Ingeniero Residente"))
    obra3.agregar_trabajador(Ingeniero("Felipe Ríos Morales", "16.234.901", 2500000, fecha_ingreso="15/09/2025", estado_laboral="Activo", cargo="SISO"))
    obra3.agregar_trabajador(Obrero("Luz Marina Castaño", "29.876.543", 1450000, fecha_ingreso="20/09/2025", estado_laboral="Activo", cargo="Oficial"))
    obra3.agregar_trabajador(Obrero("Hernán Ospina Gil", "14.567.890", 1200000, fecha_ingreso="20/09/2025", estado_laboral="Activo", cargo="Ayudante Práctico"))
    obra3.agregar_material(Material("Perfil metálico estructural", "Kg", 8500, 800))
    obra3.agregar_material(Material("Cable de acero 6x19", "Ml", 42000, 85))
    obra3.agregar_material(Material("Contrapeso de concreto prefabricado", "Unidad", 1250000, 2))
    obra3.agregar_material(Material("Tablero eléctrico trifásico", "Unidad", 3800000, 2))
    obra3.agregar_material(Material("Pintura epóxica anticorrosiva", "Kg", 45000, 60))
    obra3.agregar_material(Material("Riel guía de acero T-90", "Ml", 320000, 24))

    obra4 = Obra("Cimentación Edificio Torres Loma", "Calle 23 Norte # 12 - 57, Cali - Valle del Cauca", codigo="OBR-2026-004", presupuesto=945123700, fecha_inicio="03/02/2026", fecha_fin=None, porcentaje_avance=28, estado='En ejecución')
    obra4.agregar_trabajador(Arquitecto("Roberto Solano Parra", "79.456.123", 3500000, fecha_ingreso="03/02/2026", estado_laboral="Activo", cargo="Director de Obra"))
    obra4.agregar_trabajador(Ingeniero("Valentina Cruz Ospina", "52.789.456", 2900000, fecha_ingreso="03/02/2026", estado_laboral="Activo", cargo="Ingeniero Residente"))
    obra4.agregar_trabajador(Ingeniero("Hernán Muñoz Lozano", "16.234.567", 2600000, fecha_ingreso="10/02/2026", estado_laboral="Activo", cargo="SISO"))
    obra4.agregar_trabajador(Obrero("Jorge Palomino Reyes", "14.234.567", 1350000, fecha_ingreso="10/02/2026", estado_laboral="Activo", cargo="Oficial"))
    obra4.agregar_trabajador(Obrero("Pedro Andrade Cano", "16.789.012", 1100000, fecha_ingreso="10/02/2026", estado_laboral="Activo", cargo="Ayudante Práctico"))
    obra4.agregar_trabajador(Obrero("Rosa Moreno Vargas", "31.567.890", 1100000, fecha_ingreso="15/02/2026", estado_laboral="Activo", cargo="Ayudante"))
    obra4.agregar_material(Material("Cemento Portland tipo I", "Bulto", 28000, 1200))
    obra4.agregar_material(Material("Acero corrugado 1/2\"", "Kg", 3200, 18000))
    obra4.agregar_material(Material("Agregado grueso", "M3", 95000, 380))
    obra4.agregar_material(Material("Arena de río lavada", "M3", 65000, 280))
    obra4.agregar_material(Material("Formaleta metálica", "M2", 185000, 620))

    lista_obras.extend([obra1, obra2, obra3, obra4])


def parse_positivo(valor_str, entero=True):
    try:
        v = int(valor_str.strip()) if entero else float(valor_str.strip())
        return v if v > 0 else None
    except (ValueError, AttributeError):
        return None

def formatear_cedula(cedula):
    cedula_limpia = cedula.replace('.', '').replace(',', '').strip()
    try:
        return f"{int(cedula_limpia):,}".replace(',', '.')
    except:
        return cedula

def formatear_pesos(valor):
    try:
        return f"${valor:,.0f}".replace(",", ".")
    except (TypeError, ValueError):
        return str(valor)

@app.route('/')
def index():
    inicializar_datos()
    total_obras = len(lista_obras)
    obras_en_curso = sum(1 for obra in lista_obras if obra.esta_en_ejecucion())
    total_trabajadores = sum(len(obra.get_trabajadores()) for obra in lista_obras)
    presupuesto_total_num = sum((obra.get_presupuesto() or 0) for obra in lista_obras)
    presupuesto_total = f"${presupuesto_total_num:,.0f}".replace(",", ".")
    gasto_total = sum(obra.calcular_gasto_total() for obra in lista_obras)
    porcentaje_gastado = int((gasto_total / presupuesto_total_num) * 100) if presupuesto_total_num > 0 else 0

    return render_template('index.html', lista_obras=lista_obras, active='dashboard', total_obras=total_obras, obras_en_curso=obras_en_curso, total_trabajadores=total_trabajadores, presupuesto_total=presupuesto_total, gasto_total=gasto_total, porcentaje_gastado=porcentaje_gastado)

@app.route('/obras')
def obras():
    inicializar_datos()
    return render_template('obras.html', lista_obras=lista_obras, active='obras')

@app.route('/obras/<int:id>')
@app.route('/obra/<int:obra_id>')
def detalle_obra(id=None, obra_id=None):
    inicializar_datos()
    obra_index = id if id is not None else obra_id
    if obra_index is None or obra_index < 0 or obra_index >= len(lista_obras):
        return redirect(url_for('index'))
    obra = lista_obras[obra_index]
    return render_template('detalle_obra.html', obra=obra, obra_id=obra_index, active='obras')


@app.route('/trabajadores')
def trabajadores():
    inicializar_datos()
    lista = []
    for obra_id, obra in enumerate(lista_obras):
        for emp_id, t in enumerate(obra.get_trabajadores()):
            lista.append({
                'trabajador': t,
                'obra': obra,
                'obra_id': obra_id,
                'emp_id': emp_id,
                'cargo': t.get_cargo(),
            })
    obras = list(enumerate(lista_obras))
    return render_template('trabajadores.html', trabajadores=lista, obras=obras, active='trabajadores')


@app.route('/materiales')
def materiales():
    inicializar_datos()
    lista = []
    costo_total = 0
    for obra_id, obra in enumerate(lista_obras):
        for mat_id, m in enumerate(obra.get_materiales()):
            costo = m.calcular_costo()
            costo_total += costo
            lista.append({
                'material': m,
                'obra': obra,
                'obra_id': obra_id,
                'mat_id': mat_id,
                'precio_unitario_formateado': formatear_pesos(m.get_precio_unitario()),
                'costo_total_formateado': formatear_pesos(costo),
            })

    costo_total_materiales = formatear_pesos(costo_total)
    obras = list(enumerate(lista_obras))
    return render_template('materiales.html', materiales=lista, obras=obras, active='materiales', costo_total_materiales=costo_total_materiales)

@app.route('/crear_obra', methods=['POST'])
def crear_obra():
    nombre = request.form.get('nombre', '').strip()
    ubicacion = request.form.get('ubicacion', '').strip()
    if not nombre or not ubicacion:
        return redirect('/?error=campos_vacios')
    codigo = request.form.get('codigo', '').strip()
    fecha_raw = request.form.get('fecha_inicio', '')
    try:
        fecha_inicio = datetime.strptime(fecha_raw, '%Y-%m-%d').strftime('%d/%m/%Y')
    except ValueError:
        fecha_inicio = None
    fecha_fin_raw = request.form.get('fecha_fin', '')
    try:
        fecha_fin = datetime.strptime(fecha_fin_raw, '%Y-%m-%d').strftime('%d/%m/%Y')
    except ValueError:
        fecha_fin = None
    presupuesto = parse_positivo(request.form.get('presupuesto', ''))
    if presupuesto is None:
        return redirect('/?error=campos_vacios')
    if fecha_inicio and fecha_fin:
        di = datetime.strptime(fecha_inicio, '%d/%m/%Y')
        df = datetime.strptime(fecha_fin, '%d/%m/%Y')
        if di > df:
            return redirect('/?error=fechas_invalidas')
    nueva = Obra(nombre, ubicacion, codigo=codigo, presupuesto=presupuesto)
    if fecha_inicio:
        nueva.set_fecha_inicio(fecha_inicio)
    if fecha_fin:
        nueva.set_fecha_fin(fecha_fin)
    lista_obras.append(nueva)
    return redirect('/')

CARGO_CLASE = {
    'Director de Obra': Arquitecto,
    'Arquitecto Residente': Arquitecto,
    'Ingeniero Residente': Ingeniero,
    'SISO': Ingeniero,
    'Oficial': Obrero,
    'Ayudante Práctico': Obrero,
    'Ayudante': Obrero,
}

@app.route('/obra/<int:obra_id>/trabajador', methods=['POST'])
def agregar_trabajador(obra_id):
    if obra_id < 0 or obra_id >= len(lista_obras):
        return redirect(url_for('index'))
    cargo = request.form.get('cargo', 'Ayudante')
    nombre = request.form.get('nombre')
    cedula = request.form.get('cedula')
    fecha_raw = request.form.get('fecha_ingreso', '')
    try:
        fecha_ingreso = datetime.strptime(fecha_raw, '%Y-%m-%d').strftime('%d/%m/%Y')
    except ValueError:
        fecha_ingreso = fecha_raw
    salario = request.form.get('salario', '')
    salario_valor = parse_positivo(salario)
    if nombre and cedula and salario_valor is not None:
        cedula_normalizada = cedula.replace('.', '').replace(',', '').strip()
        cedula_duplicada = any(
            t.get_cedula().replace('.', '').replace(',', '').strip() == cedula_normalizada
            for t in lista_obras[obra_id].get_trabajadores()
        )
        if cedula_duplicada:
            return redirect(f'/obras/{obra_id}?error=cedula_duplicada')
        cedula = formatear_cedula(cedula)
        clase = CARGO_CLASE.get(cargo, Obrero)
        trabajador = clase(nombre, cedula, salario_valor, fecha_ingreso=fecha_ingreso, cargo=cargo)
        lista_obras[obra_id].agregar_trabajador(trabajador)

    return redirect(url_for('detalle_obra', obra_id=obra_id))

@app.route('/trabajadores/nuevo', methods=['POST'])
def nuevo_empleado():
    inicializar_datos()
    try:
        obra_id = int(request.form.get('obra_id', -1))
    except ValueError:
        return redirect('/trabajadores')
    if obra_id < 0 or obra_id >= len(lista_obras):
        return redirect('/trabajadores')
    cargo = request.form.get('cargo', 'Ayudante')
    nombre = request.form.get('nombre', '').strip()
    cedula = request.form.get('cedula', '').strip()
    fecha_raw = request.form.get('fecha_ingreso', '')
    salario = request.form.get('salario', '').strip()
    if not nombre or not cedula or not salario:
        return redirect('/trabajadores?error=campos_vacios')
    try:
        fecha_ingreso = datetime.strptime(fecha_raw, '%Y-%m-%d').strftime('%d/%m/%Y')
    except ValueError:
        fecha_ingreso = ''
    cedula_normalizada = cedula.replace('.', '').replace(',', '').strip()
    if any(t.get_cedula().replace('.', '').replace(',', '').strip() == cedula_normalizada
           for t in lista_obras[obra_id].get_trabajadores()):
        return redirect('/trabajadores?error=cedula_duplicada')
    salario_valor = parse_positivo(salario)
    if salario_valor is None:
        return redirect('/trabajadores?error=campos_vacios')
    cedula = formatear_cedula(cedula)
    clase = CARGO_CLASE.get(cargo, Obrero)
    lista_obras[obra_id].agregar_trabajador(
        clase(nombre, cedula, salario_valor, fecha_ingreso=fecha_ingreso, cargo=cargo)
    )
    return redirect('/trabajadores')

@app.route('/obras/<int:id>/editar', methods=['POST'])
def editar_obra(id):
    if id < 0 or id >= len(lista_obras):
        return redirect('/obras')
    obra = lista_obras[id]
    nombre = request.form.get('nombre', '').strip()
    ubicacion = request.form.get('ubicacion', '').strip()
    if nombre:
        obra.set_nombre(nombre)
    if ubicacion:
        obra.set_ubicacion(ubicacion)
    obra.set_codigo(request.form.get('codigo', '').strip())
    for campo, setter in [('fecha_inicio', obra.set_fecha_inicio), ('fecha_fin', obra.set_fecha_fin)]:
        raw = request.form.get(campo, '')
        try:
            setter(datetime.strptime(raw, '%Y-%m-%d').strftime('%d/%m/%Y'))
        except ValueError:
            pass
    try:
        p = parse_positivo(request.form.get('presupuesto', ''))
        if p is not None:
            obra.set_presupuesto(p)
    except ValueError:
        pass
    estado = request.form.get('estado', '').strip()
    if estado:
        obra.set_estado(estado)
    try:
        obra.set_porcentaje_avance(int(request.form.get('porcentaje_avance', 0)))
    except ValueError:
        pass
    return redirect('/obras')

@app.route('/obras/<int:id>/eliminar', methods=['POST'])
def eliminar_obra(id):
    if 0 <= id < len(lista_obras):
        lista_obras.pop(id)
    return redirect('/obras')

@app.route('/obras/<int:obra_id>/empleados/<int:emp_id>/reactivar', methods=['POST'])
def reactivar_empleado(obra_id, emp_id):
    obra = lista_obras[obra_id]
    trabajadores = obra.get_trabajadores()
    if 0 <= emp_id < len(trabajadores):
        trabajadores[emp_id].set_estado_laboral('Activo')
    return_to = request.form.get('return_to', '/trabajadores')
    return redirect(return_to)

@app.route('/obras/<int:obra_id>/empleados/<int:emp_id>/retirar', methods=['POST'])
def retirar_empleado(obra_id, emp_id):
    obra = lista_obras[obra_id]
    trabajadores = obra.get_trabajadores()
    if 0 <= emp_id < len(trabajadores):
        trabajadores[emp_id].set_estado_laboral('Retirado')
    return_to = request.form.get('return_to', '/trabajadores')
    return redirect(return_to)

@app.route('/obras/<int:obra_id>/empleados/<int:emp_id>/eliminar', methods=['POST'])
def eliminar_empleado(obra_id, emp_id):
    obra = lista_obras[obra_id]
    trabajadores = obra.get_trabajadores()
    if 0 <= emp_id < len(trabajadores):
        trabajadores.pop(emp_id)
    return_to = request.form.get('return_to', f'/obras/{obra_id}')
    return redirect(return_to)

@app.route('/obras/<int:obra_id>/materiales/<int:mat_id>/eliminar', methods=['POST'])
def eliminar_material(obra_id, mat_id):
    obra = lista_obras[obra_id]
    materiales = obra.get_materiales()
    if 0 <= mat_id < len(materiales):
        materiales.pop(mat_id)
    return_to = request.form.get('return_to', f'/obras/{obra_id}')
    return redirect(return_to)

@app.route('/obras/<int:obra_id>/materiales/<int:mat_id>/editar', methods=['POST'])
def editar_material(obra_id, mat_id):
    if obra_id < 0 or obra_id >= len(lista_obras):
        return redirect('/materiales')
    materiales = lista_obras[obra_id].get_materiales()
    if mat_id < 0 or mat_id >= len(materiales):
        return redirect('/materiales')
    m = materiales[mat_id]
    nombre = request.form.get('nombre', '').strip()
    unidad = request.form.get('unidad', '').strip()
    precio = parse_positivo(request.form.get('precio_unitario', ''))
    cantidad = parse_positivo(request.form.get('cantidad', ''))
    if nombre: m.set_nombre(nombre)
    if unidad: m.set_unidad(unidad)
    if precio is not None: m.set_precio_unitario(precio)
    if cantidad is not None: m.set_cantidad(cantidad)
    return_to = request.form.get('return_to', f'/obras/{obra_id}')
    return redirect(return_to)

@app.route('/materiales/nuevo', methods=['POST'])
def nueva_compra():
    inicializar_datos()
    try:
        obra_id = int(request.form.get('obra_id', -1))
    except (ValueError, TypeError):
        return redirect('/materiales')
    if obra_id < 0 or obra_id >= len(lista_obras):
        return redirect('/materiales')
    nombre   = request.form.get('nombre', '').strip()
    unidad   = request.form.get('unidad', '').strip()
    try:
        precio   = float(request.form.get('precio_unitario', '').strip())
        cantidad = float(request.form.get('cantidad', '').strip())
    except (ValueError, TypeError):
        return redirect('/materiales')
    if nombre and unidad and precio > 0 and cantidad > 0:
        lista_obras[obra_id].agregar_material(Material(nombre, unidad, precio, cantidad))
    return redirect('/materiales')

@app.route('/obra/<int:obra_id>/material', methods=['POST'])
def agregar_material(obra_id):
    if obra_id < 0 or obra_id >= len(lista_obras):
        return redirect(url_for('index'))
    nombre = request.form.get('nombre', '').strip()
    unidad = request.form.get('unidad', '').strip()
    precio_valor = parse_positivo(request.form.get('precio_unitario', ''))
    cantidad_valor = parse_positivo(request.form.get('cantidad', ''))
    if nombre and unidad and precio_valor is not None and cantidad_valor is not None:
        material = Material(nombre, unidad, precio_valor, cantidad_valor)
        lista_obras[obra_id].agregar_material(material)

    return redirect(url_for('detalle_obra', obra_id=obra_id))

if __name__ == '__main__':
    app.run(debug=True)
