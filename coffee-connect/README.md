# coffee-connect
Aplicación de Gestión de Cartas para cafeterías

## Descripción
Este proyecto es una aplicación web para la gestión de cartas en cafeterías, permitiendo a los usuarios visualizar y administrar las opciones de menú de manera eficiente.

## Estructura del Proyecto
El proyecto está dividido en dos partes principales: el frontend y el backend.

### Frontend
La parte del frontend está construida con React.js y contiene los siguientes archivos y directorios:

- **public/index.html**: Archivo HTML principal que sirve como punto de entrada para la aplicación React.
- **src/components/App.js**: Componente raíz de la aplicación que maneja la estructura y la lógica de enrutamiento.
- **src/pages/Home.js**: Componente que representa la página de inicio de la aplicación.
- **src/services/api.js**: Funciones para realizar llamadas API al backend.
- **src/styles/App.css**: Estilos CSS para la aplicación.
- **src/index.js**: Punto de entrada para la aplicación React que renderiza el componente App.

### Backend
La parte del backend está construida con Python y contiene los siguientes archivos y directorios:

- **app/__init__.py**: Marca el directorio como un paquete de Python y puede contener código de inicialización.
- **app/main.py**: Punto de entrada para la aplicación backend que configura el servidor web.
- **app/models/__init__.py**: Marca el directorio de modelos como un paquete de Python.
- **app/routes/__init__.py**: Marca el directorio de rutas como un paquete de Python.
- **app/utils/__init__.py**: Marca el directorio de utilidades como un paquete de Python.
- **requirements.txt**: Lista de dependencias necesarias para la aplicación backend.
- **.env**: Contiene variables de entorno para la aplicación backend.

## Instalación
Para instalar y ejecutar el proyecto, siga estos pasos:

1. Clonar el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd coffee-connect
   ```

2. Configurar el backend:
   - Navegar al directorio `backend` y crear un entorno virtual:
     ```
     cd backend
     python -m venv venv
     source venv/bin/activate  # En Windows use `venv\Scripts\activate`
     ```
   - Instalar las dependencias:
     ```
     pip install -r requirements.txt
     ```

3. Configurar el frontend:
   - Navegar al directorio `frontend` y instalar las dependencias:
     ```
     cd frontend
     npm install
     ```

4. Ejecutar el backend:
   ```
   python app/main.py
   ```

5. Ejecutar el frontend:
   ```
   npm start
   ```

## Características
- Gestión de cartas de menú para cafeterías.
- Interfaz de usuario intuitiva construida con React.
- API RESTful para la comunicación entre el frontend y el backend.

## Contribuciones
Las contribuciones son bienvenidas. Si desea contribuir, por favor abra un issue o un pull request en el repositorio.