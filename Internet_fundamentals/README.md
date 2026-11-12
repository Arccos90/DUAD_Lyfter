# Fundamentos de Internet 

## 1. Del Cliente al Servidor
    El cliente ingresa al navegador y coloca la dirección web "www.youtube.com". Esto es un REQUEST para el servidor de DNS. El el servidor de DNS traduce esta información en la dirección IP pública del servidor de youtube. El RESPONSE llega al navegador, Luego el navedador envía un nuevo REQUEST al servidor de youtube con la busqueda o requerimiento especifico del usuario.
    El DNS (Domain Name System), es la manera en que se traducen los dominios de las diferentes paginas web (.com, .net, .org) a el formato de dominio IP público. Esta es la manera en que el navegador sabe a que servidor enviar el REQUEST. Entiendo que YouTube no maneja una dirección IP publica fija, si no que varia con el tiempo de manera dinámica.
    El REQUEST se realiza utilizando el protocolo HTTP o HTTPS, esta segundo protocolo maneja toda la información de manera cifrada. Es protocolo establece el PATH, QUERY_PARAMETERS, METHODS y STATUS CODES.

## 2. Frontend y Backend en acción:
    El frontend se encargaría de realizar toda la parte visual y estética de la pagina, asi como todo los elementos con los que interactua el usuario, por ejemplo construye un calendario visual con los diferentes espacios de agenda durante la semana, los espacios disponibles se ven en verde y los ocupados en gris. El backend, se encarga de realizar todo el trabajo tras bambalinas así como las persistencia de los datos, trabaja con las API que conectan las diferentes funcionalidades, por ejemplo, trabaja en las consultas a la base de datos en donde se encuentran la información de la citas ya confirmadas y que se generen los RESPONSE de manera adecuada sin errores.
    Tecnologías disponibles:
    Frontend: HTML (estructura), CSS / Tailwind (estilos) y JavaScript con React (interactividad).   
    Backend: Python (con FastAPI o Django), Node.js (con Express) o C#, conectados a una base de datos como PostgreSQL. 

    Siguiendo con el ejemplo, cuando el usuario ingresa a la pagina y preciona la opcion ver calendario, esto seria unando el protocolo HTTP y una ruta o PATH www.sumedicodeconfianza.com/inicio/citas. Está enviando un REQUEST al servidor donde esta la base de datos de la agenda, posiblemente usando el método GET para obtener información de los espacios disponibles . El servidor devolverá el RESPONSE con la información de los espacios disponibles. Cuando el cliente elige un espacio en un día especifico, enviará otro REQUEST posiblemente usando el método PUT, modificando el status del elemento o el bloque de tiempo en el calendario de disponible a ocupado, o agregando informacions adicional en el BODY como por ejemplo el nombre del paciente. El servidor guarda el cambio y responde con un código 201 Created o 200 OK confirmando la reserva.
    El JSON se vería asi:
    {
  "doctor_id": 42,
  "nombre_doctor": "Dra. Sofía Mora",
  "especialidad": "Medicina General",
  "fecha": "2026-11-15",
  "horarios": [
    {
      "bloque_id": 101,
      "hora_inicio": "09:00",
      "hora_fin": "09:30",
      "estado": "disponible"
    },
    {
      "bloque_id": 102,
      "hora_inicio": "09:30",
      "hora_fin": "10:00",
      "estado": "ocupado"
    },
    {
      "bloque_id": 103,
      "hora_inicio": "10:00",
      "hora_fin": "10:30",
      "estado": "disponible"
    }
  ]
}

## 3. REST vs SOAP vs GraphQL


| Tipo de API |Formato de datos usado |Nivel de flexibilidad |Dificultad de implementación |Uso actual (Alta / Media / Baja) |
|-------------|-----------------------|----------------------|-----------------------------|-----------------------------------|
| REST        | JSON/ XML, texto plano| Media Alto           |  Baja/Fácil                 | Alta
| SOAP        | XML                   | Baja                 |  Alta/Compleja              | Baja
| GraphQL     | JSON                  | Alta                 |  Media - Alta               | Media - Alta

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**

REST es la opción más apropiada para iniciar (con GraphQL como alternativa solo si el producto escala a múltiples clientes con requerimientos de datos muy complejos).

¿Por qué?

-Velocidad de desarrollo: En una startup moderna la prioridad es lanzar rápido y validar el modelo de negocio. REST aprovecha directamente las características estándar de HTTP (rutas, métodos GET, POST, DELETE, status codes), lo que ofrece la curva de aprendizaje más baja y agiliza la construcción del MVP.

-Ecosistema maduro y bajo costo de mantenimiento: La gran mayoría de desarrolladores frontend y backend dominan el consumo y creación de APIs REST con JSON, y existen herramientas estándar listas para usar (como Postman, Swagger/OpenAPI, FastAPI o Express).

## 4. Explorando APIs con Postman

### 4.1 Selección de la API
- **Nombre de la API:**
JSONPlaceholder
- **Descripción:**
JSONPlaceholder is a free online REST API that you can use whenever you need some fake data: in documentation and tutorials, in code examples, in a quick prototype, or simply to test things locally.

### 4.2 Configuración en Postman
- **Exercise_4.postman.collection.json:**
- **Solicitudes agregadas:**
  - GET - GET_posts
  - POST - POST_Newpost
  - PUT/PATCH/DELETE - PATCH_Added_"Hola_Pura_Vida"

### 4.3 Ejecución y análisis

| Solicitud                     | Método| Endpoint                                                 | Código de estado  | Notas |
|-------------------------------|-------|----------------------------------------------------------|-------------------|-------|
|Obtener el post id 50          | GET   |https://jsonplaceholder.typicode.com/comments/50          |      200          |       |
|Modificar el parametro "body"  | PUT   |https://jsonplaceholder.typicode.com/comments/50?Body=hola|      200
|Crear un nuevo post            | POST  |https://jsonplaceholder.typicode.com/posts                |      201

### 4.4 Explicación técnica

#### 4.4.1 Obtener el post id 50    
- **Método HTTP:GET
- **Endpoint:https://jsonplaceholder.typicode.com/comments/50   
- **Parámetros / body:
{
    "postId": 10,
    "id": 50,
    "name": "dolorum soluta quidem ex quae occaecati dicta aut doloribus",
    "email": "Kiana_Predovic@yasmin.io",
    "body": "eum accusamus aut delectus\narchitecto blanditiis quia sunt\nrerum harum sit quos quia aspernatur vel corrupti inventore\nanimi dicta vel corporis"
}
- **Descripción de la respuesta:
Muestra el PostId, id, nombre, correo y el cuerpo del post. Es una base de datos de comentarios random.

#### 4.4.2 Modificar el parametro "body"
- **Método HTTP:PUT
- **Endpoint:https://jsonplaceholder.typicode.com/comments/50?Body=hola  
- **Parámetros / body:
{
    "postId": 10,
    "id": 50,
    "name": "dolorum soluta quidem ex quae occaecati dicta aut doloribus",
    "email": "Kiana_Predovic@yasmin.io",
    "body": "Hola Pura Vida"
}
- **Descripción de la respuesta:
La idea era modificar el parametro "body" con el texto "Hola Pura Vida"

#### 4.4.3 Modificar el parametro "body"
- **Método HTTP:POST
- **Endpoint:https://jsonplaceholder.typicode.com/posts 
- **Parámetros / body:
{
    "postId": 55,
    "id": 505,
    "name": "Costarricans Usser",
    "email": "Puravida@CR.com",
    "body": "Hola",
    "phone_zone": 506
}
- **Descripción de la respuesta:
Se creo un post totalmente nuevo y se agregó un parametro más "phone_zone"

**¿Qué aprendiste del proceso?**
Al inicio no estaba logrando ejecutar los método de modificación de información (PUT o POST), luego intenté usarlo modificando el BODY y usando el parametro RAW, y luego modificaba todo usando el formato del JSON.

### 4.5 Reflexión final

¿Qué aprendiste sobre el funcionamiento de las APIs?
Al inicio me confundí un poco por que tenia el concepto de API, más relacionado a API para comunicar programas con diferentes lenguajes, pero luego fuí captando un poco más el rol para paginas web, me gustaría empezar a interactuar y experimentar como programa el ejemplo de las agendas. Por que me queda claro que se envía un REQUEST y se recibe un RESPONSE con la información, pero como se convierte eso en algo visual en un calendario me parece interesante.
¿Cómo te ayudó Postman a entender la comunicación entre cliente y servidor?
Postman me ayudo a comprender el funcionamiento de la API para web, de hecho de ahí surge mi inquietud en como se transforma el RESPONSE:
   {
  "doctor_id": 42,
  "nombre_doctor": "Dra. Sofía Mora",
  "especialidad": "Medicina General",
  "fecha": "2026-11-15",
  "horarios": [
    {
      "bloque_id": 101,
      "hora_inicio": "09:00",
      "hora_fin": "09:30",
      "estado": "disponible"
    },
    {
      "bloque_id": 102,
      "hora_inicio": "09:30",
      "hora_fin": "10:00",
      "estado": "ocupado"
    },
    {
      "bloque_id": 103,
      "hora_inicio": "10:00",
      "hora_fin": "10:30",
      "estado": "disponible"
    }
  ]
}
En algo visual como lo es un calendario de citas, y como lo que esta ocupado ahora se ve gris y lo que esta disponible se ve verde.