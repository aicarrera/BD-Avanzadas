# Instrucciones para Usar el Archivo `docker-compose.yml`

## Pasos para usar este archivo

1. **Crear el archivo**: Copia el contenido anterior en un archivo llamado `docker-compose.yml`.

2. **Estructura de directorios**:
   - Crea una carpeta llamada `import` en el mismo directorio donde guardaste el archivo `docker-compose.yml`.
   - Dentro de la carpeta `import`, puedes colocar tus archivos CSV que desees cargar.

3. **Ejecutar Docker Compose**: Abre una terminal en el directorio donde está tu `docker-compose.yml` y ejecuta el siguiente comando para levantar el contenedor:

   ```bash
   docker-compose up -d
Acceder a Neo4j: Abre tu navegador y ve a http://localhost:7474. Inicia sesión con el usuario neo4j y la contraseña .

1. Cargar la base de datos de prueba "Movies" en Neo4j
Una vez que tienes Neo4j corriendo en un contenedor Docker, puedes usar la interfaz web o el cliente para cargar la base de datos de ejemplo.

Opción A: Desde la interfaz web de Neo4j
Abre tu navegador y ve a la interfaz web de Neo4j en http://localhost:7474.

Inicia sesión con el usuario y contraseña que configuraste (en este caso neo4j y test).

En la ventana de consultas Cypher, ejecuta el siguiente comando para cargar la base de datos de prueba Movies:

Copiar código
  ```bash
:play movies

Esto abrirá una pequeña ventana interactiva que te guiará a través de la carga de los datos de películas. Solo tienes que hacer clic en "Run" en los scripts que te aparecen, y Neo4j insertará los nodos y relaciones correspondientes.
