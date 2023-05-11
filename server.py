# import http.server
# import socketserver

# PORT = 8000

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"Serving at port {PORT}")
#     httpd.serve_forever()



import socket

def renderizar_pagina():
    # Esta función devuelve el contenido HTML de la página
    contenido = '''
    <html>
    <head>
        <title>Formulario</title>
    </head>
    <body>
        <h1>Formulario</h1>
        <form method="POST" action="http://direccion_ip_del_servidor:puerto">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
            <br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <br>
            <input type="submit" value="Enviar">
        </form>
    </body>
    </html>
    '''
    return contenido

def procesar_peticion(data):
    # Esta función procesa los datos enviados desde el formulario
    import re
    match = re.search(r'nombre=(.*)&email=(.*)', data)
    if match:
        nombre = match.group(1)
        email = match.group(2)
        print(nombre , email)

        # Aquí puedes realizar acciones con los datos recibidos

def iniciar_servidor():
    host = '192.16.1.1'  # Dirección IP del servidor
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
