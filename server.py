import socket

def renderizar_pagina():
    # Esta función devuelve el contenido HTML de la página
    contenido = '''
<!DOCTYPE html>
<html>
<head>
    <title>Formulario con Botones</title>
</head>
<body>
    <h1>Formulario con Botones</h1>
    <button id="boton1">Botón 1</button>
    <button id="boton2">Botón 2</button>
    <button id="boton3">Botón 3</button>

    <script>
        // Función para enviar el dato al servidor
        function enviarDato(valor) {
            var xhr = new XMLHttpRequest();
            var url = "http://192.168.1.12:8050";
            var params = "dato=" + valor;

            xhr.open("POST", url, true);
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    console.log("Dato enviado correctamente al servidor");
                }
            };

            xhr.send(params);
        }

        // Capturar eventos de clic de los botones
        var boton1 = document.getElementById("boton1");
        var boton2 = document.getElementById("boton2");
        var boton3 = document.getElementById("boton3");

        boton1.addEventListener("click", function () {
            enviarDato("valor1");
        });

        boton2.addEventListener("click", function () {
            enviarDato("valor2");
        });

        boton3.addEventListener("click", function () {
            enviarDato("valor3");
        });
    </script>
</body>
</html>
    '''
    return contenido

def enviar_dato_servidor(dato, host, port):
    # Crea un socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conéctate al servidor remoto
        client_socket.connect((host, port))

        # Envía el dato al servidor
        client_socket.sendall(dato.encode('utf-8'))

        # Espera la respuesta del servidor
        response = client_socket.recv(1024).decode('utf-8')

        # Imprime la respuesta recibida del servidor
        print('Respuesta del servidor:', response)
    finally:
        # Cierra la conexión del socket
        client_socket.close()



def procesar_peticion(data):
    # Esta función procesa los datos enviados desde el formulario
    import re
    import urllib.parse

    parsed_data = urllib.parse.unquote(data)
    match = re.search(r'dato=(.*)', parsed_data)
    if match:
        dato = match.group(1)
        # Aquí puedes realizar acciones con el dato recibido
        print('-------------------------')
        print('Dato recibido:', dato)
        print('-------------------------')
        # revisar 
        enviar_dato_servidor(dato=dato , host='192.168.4.1' , port=3000)


def iniciar_servidor():
    host = '192.168.1.12'  # Dirección IP del servidor
    port = 8050  # Puerto del servidor

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print('Servidor TCP esperando conexiones...')

    while True:
        client_socket, addr = server_socket.accept()
        print('Cliente conectado:', addr)

        data = client_socket.recv(1024).decode('utf-8')
        print('Datos recibidos:', data)

        # Verifica si la solicitud es para el formulario o la página principal
        if 'GET / ' in data:
            # Renderiza la página principal
            content = renderizar_pagina()
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + content
            client_socket.sendall(response.encode('utf-8'))
        elif 'POST /' in data:
            # Procesa los datos del formulario
            procesar_peticion(data)
            # Envía una respuesta al cliente
            content = '¡Formulario recibido correctamente!'
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + content
            client_socket.sendall(response.encode('utf-8'))

        client_socket.close()

iniciar_servidor()
