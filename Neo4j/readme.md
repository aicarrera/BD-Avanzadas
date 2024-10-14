# Instrucciones para Usar el Archivo `docker-compose.yml`

## Pasos para usar este archivo

1. **Crear el archivo**: Copia el contenido anterior en un archivo llamado `docker-compose.yml`.

2. **Estructura de directorios**:
   - Crea una carpeta llamada `import` en el mismo directorio donde guardaste el archivo `docker-compose.yml`.
   - Dentro de la carpeta `import`, puedes colocar tus archivos CSV que desees cargar.

3. **Ejecutar Docker Compose**: Abre una terminal en el directorio donde está tu `docker-compose.yml` y ejecuta el siguiente comando para levantar el contenedor:

   ```bash
   docker-compose up -d
Acceder a Neo4j: Abre tu navegador y ve a http://localhost:7474. Inicia sesión con el usuario neo4j y la contraseña test.
