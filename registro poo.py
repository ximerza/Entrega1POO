

registros_usuarios = {}

def registrar_usuario():
    print("Registro de Usuario")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in registros_usuarios:
        print("El nombre de usuario ya existe. Por favor, elija otro.")
        return
    contraseña = input("Ingrese su contraseña: ")
    registros_usuarios[nombre_usuario] = contraseña
    print("Registro exitoso. Ahora puede iniciar sesión.")

def iniciar_sesion():
    print("Inicio de Sesión")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if nombre_usuario in registros_usuarios and registros_usuarios[nombre_usuario] == contraseña:
        print("Inicio de sesión exitoso. ¡Bienvenido!")
    else:
        print("Credenciales incorrectas. Inicio de sesión fallido.")

while True:
    print("\nOpciones:")
    print("1. Registrar Usuario")
    print("2. Iniciar Sesión")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
