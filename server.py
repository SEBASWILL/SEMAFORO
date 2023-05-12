import socket


def renderizar_pagina():
    # Esta función devuelve el contenido HTML de la página
    contenido = """
<!DOCTYPE html>
<html>
  <link
      rel="stylesheet"
      href="https://unpkg.com/tailwindcss@2.2.19/dist/tailwind.min.css"
    />
  </head>
 <body
    class="font-sans antialiased text-gray-900 leading-normal tracking-wider bg-cover"
    style="background-image: url('https://source.unsplash.com/1L71sPT5XKc')"
  >
    <div
      class="max-w-4xl flex items-center h-auto lg:h-screen flex-wrap mx-auto my-32 lg:my-0"
    >
      <!--Main Col-->
      <div
        id="profile"
        class="w-full lg:w-3/5 rounded-lg lg:rounded-l-lg lg:rounded-r-none shadow-2xl bg-white opacity-75 mx-6 lg:mx-0"
      >
        <div class="p-4 md:p-12 text-center lg:text-left">
          <!-- Image for mobile view-->
          <div
            class="block lg:hidden rounded-full shadow-xl mx-auto -mt-16 h-48 w-48 bg-cover bg-center"
            style="
              background-image: url('https://www.segurmaniazurekin.eus/a/2021/03/segurmania_semaforo_aniversario_destacada-320x240.jpg');
            "
          ></div>

          <h1 class="text-3xl font-bold pt-8 lg:pt-0">Semaforo</h1>
          <div
            class="mx-auto lg:mx-0 w-4/5 pt-3 border-b-2 border-green-500 opacity-25"
          ></div>
          <p
            class="pt-4 text-base font-bold flex items-center justify-center lg:justify-start"
          >
            <svg
              class="h-4 fill-current text-green-700 pr-4"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
            >
              <path
                d="M9 12H1v6a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6h-8v2H9v-2zm0-1H0V5c0-1.1.9-2 2-2h4V2a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v1h4a2 2 0 0 1 2 2v6h-9V9H9v2zm3-8V2H8v1h4z"
              />
            </svg>
            Sebastian Wilches Olarte
          </p> <p
            class="pt-4 text-base font-bold flex items-center justify-center lg:justify-start"
          >
            <svg
              class="h-4 fill-current text-green-700 pr-4"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
            >
              <path
                d="M9 12H1v6a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6h-8v2H9v-2zm0-1H0V5c0-1.1.9-2 2-2h4V2a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v1h4a2 2 0 0 1 2 2v6h-9V9H9v2zm3-8V2H8v1h4z"
              />
            </svg>
            Ailen Beltran Montealegre
           </p>
          <p
            class="pt-2 text-gray-600 text-xs lg:text-sm flex items-center justify-center lg:justify-start"
          >
            <svg
              class="h-4 fill-current text-green-700 pr-4"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
            >
              <path
                d="M10 20a10 10 0 1 1 0-20 10 10 0 0 1 0 20zm7.75-8a8.01 8.01 0 0 0 0-4h-3.82a28.81 28.81 0 0 1 0 4h3.82zm-.82 2h-3.22a14.44 14.44 0 0 1-.95 3.51A8.03 8.03 0 0 0 16.93 14zm-8.85-2h3.84a24.61 24.61 0 0 0 0-4H8.08a24.61 24.61 0 0 0 0 4zm.25 2c.41 2.4 1.13 4 1.67 4s1.26-1.6 1.67-4H8.33zm-6.08-2h3.82a28.81 28.81 0 0 1 0-4H2.25a8.01 8.01 0 0 0 0 4zm.82 2a8.03 8.03 0 0 0 4.17 3.51c-.42-.96-.74-2.16-.95-3.51H3.07zm13.86-8a8.03 8.03 0 0 0-4.17-3.51c.42.96.74 2.16.95 3.51h3.22zm-8.6 0h3.34c-.41-2.4-1.13-4-1.67-4S8.74 3.6 8.33 6zM3.07 6h3.22c.2-1.35.53-2.55.95-3.51A8.03 8.03 0 0 0 3.07 6z"
              />
            </svg>
            Funciona a partir de sockets y conecciones tcp 
          </p>
          <p class="pt-8 text-sm">
            Recuende una sola persona a la ves 
          </p>
          <div class="flex gap-1">
            <div class="pt-12 pb-8">
              <button
              id="boton3"
                class="bg-blue-700 hover:bg-blue-900 text-white font-bold py-2 px-4 rounded-full"
              >
                Automatico
              </button>
            </div>
            <div class="pt-12 pb-8">
              <button
              id="boton2"
                class="bg-red-700 hover:bg-red-900 text-white font-bold py-2 px-4 rounded-full"
              >
                rojo
              </button>
            </div>
            <div class="pt-12 pb-8">
              <button
              id="boton1"
                class="bg-green-700 hover:bg-green-900 text-white font-bold py-2 px-4 rounded-full"
              >
                Verde
              </button>
            </div>
          </div>
        </div>
      </div>

      <!--Img Col-->
      <div class="w-full lg:w-2/5">
        <!-- Big profile image for side bar (desktop) -->
        <img
          src="https://res.cloudinary.com/dhoyilan2/image/upload/v1683771784/semaforo/semaforo.jpg"
          class="rounded-none lg:rounded-lg shadow-2xl hidden lg:block"
        />
        <!-- Image from: http://unsplash.com/photos/MP0IUfwrn0A -->
      </div>

      <!-- Pin to top right corner -->
      <div class="absolute top-0 right-0 h-12 w-18 p-4">
        <button   class="js-change-theme focus:outline-none">🌙</button>
      </div>
    </div>

    <script src="https://unpkg.com/popper.js@1/dist/umd/popper.min.js"></script>
    <script src="https://unpkg.com/tippy.js@4"></script>
    <script>
      //Init tooltips
      tippy(".link", {
        placement: "bottom",
      });

      //Toggle mode
      const toggle = document.querySelector(".js-change-theme");
      const body = document.querySelector("body");
      const profile = document.getElementById("profile");

      toggle.addEventListener("click", () => {
        if (body.classList.contains("text-gray-900")) {
          toggle.innerHTML = "☀️";
          body.classList.remove("text-gray-900");
          body.classList.add("text-gray-100");
          profile.classList.remove("bg-white");
          profile.classList.add("bg-gray-900");
        } else {
          toggle.innerHTML = "🌙";
          body.classList.remove("text-gray-100");
          body.classList.add("text-gray-900");
          profile.classList.remove("bg-gray-900");
          profile.classList.add("bg-white");
        }
      });
    </script>

    <script>
        // Función para enviar el dato al servidor
        function enviarDato(valor) {
            var xhr = new XMLHttpRequest();
            var url = "http://192.168.4.2:8050";
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
            enviarDato("verde");
        });

        boton2.addEventListener("click", function () {
            enviarDato("rojo");
        });

        boton3.addEventListener("click", function () {
            enviarDato("auto");
        });
    </script>
</body>
</html>
    """
    return contenido


def enviar_dato_servidor(dato, host, port):
    # Crea un socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(5)  # Establece un tiempo máximo de espera de 5 segundos

    try:
        # Conéctate al servidor remoto
        client_socket.connect((host, port))

        # Envía el dato al servidor
        client_socket.sendall(dato.encode("utf-8"))

        # Espera la respuesta del servidor
        response = client_socket.recv(1024).decode("utf-8")

        # Imprime la respuesta recibida del servidor
        print("Respuesta del servidor:", response)
    except socket.timeout:
        print("Tiempo de espera agotado. No se recibió respuesta del servidor.")
    except ConnectionRefusedError:
        print("No se pudo establecer la conexión con el servidor remoto.")
    finally:
        # Cierra la conexión del socket
        client_socket.close()


def procesar_peticion(data):
    # Esta función procesa los datos enviados desde el formulario
    import re
    import urllib.parse

    parsed_data = urllib.parse.unquote(data)
    match = re.search(r"dato=(.*)", parsed_data)
    if match:
        dato = match.group(1)
        # Aquí puedes realizar acciones con el dato recibido
        print("-------------------------")
        print("Dato recibido:", dato)
        print("-------------------------")
        # revisar
        enviar_dato_servidor(dato=dato, host="192.168.4.1", port=3000)


def iniciar_servidor():
    host = "192.168.4.2"  # Dirección IP del servidor
    port = 8050  # Puerto del servidor

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Servidor TCP esperando conexiones...")

    while True:
        client_socket, addr = server_socket.accept()
        print("Cliente conectado:", addr)

        data = client_socket.recv(1024).decode("utf-8")
        print("Datos recibidos:", data)

        # Verifica si la solicitud es para el formulario o la página principal
        if "GET / " in data:
            # Renderiza la página principal
            content = renderizar_pagina()
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + content
            client_socket.sendall(response.encode("utf-8"))
        elif "POST /" in data:
            # Procesa los datos del formulario
            procesar_peticion(data)
            # Envía una respuesta al cliente
            content = "¡Formulario recibido correctamente!"
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + content
            client_socket.sendall(response.encode("utf-8"))

        client_socket.close()


iniciar_servidor()
