#Sistemas de acceso

usuario = input('Ingresa el nombre de usuario:')
rol = input('Ingresa el rol:').lower()
estado = input('Estado (activo/inactivo):').lower()

'''
Reglas:
-Cuentas inactivas no pueden logearse.
-Si las cuentas estan activas:
    admin - control total
    tecnico - control sobre usuarios
    usuario - acceso  limitado
    otro rol - no reconocido
'''    
if estado == 'inactivo':
    print('Acceso denegado')
    print('Solicite acceso al administrador')
elif rol == 'Administrador':
    print('Bienvenido',usuario)
    print('Acceso concedido')
    print('Rol:',rol)
    print('Permisos: Acceso total')
elif rol == 'Tecnico':
    print('Bienvenido',usuario)
    print('Acceso concedido')
    print('Rol:',rol)
    print('Permisos: \n mantenimiento del sistema, acceso a usuarios')
elif rol == 'usuario':
    print('Bienvenido',usuario)
    print('Acceso concedido')
    print('Rol:',rol)
    print('Permisos: Acceso limitado')
else:
    print('Acceso denegado')
    print('Rol desconocido')
