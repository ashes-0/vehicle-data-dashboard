# vehicle-data-dashboard
# Panel de control de datos de anuncios de coches

Este proyecto es un panel de control web interactivo diseñado para visualizar y analizar datos de anuncios de venta de coches. La aplicación fue desarrollada como parte de un proyecto de ingeniería de software para practicar la creación de entornos virtuales, el desarrollo de aplicaciones web y el despliegue en un servicio en la nube.

---

## Funcionalidad de la aplicación

El panel de control permite a los usuarios:

-   Ver un **histograma** que muestra la distribución de los odómetros de los vehículos.
-   Explorar la **relación entre el odómetro y el precio** a través de un gráfico de dispersión.

Los gráficos son interactivos, permitiendo a los usuarios hacer zoom y moverlos para un mejor análisis.

---

## Cómo ejecutar la aplicación

Para ejecutar la aplicación en tu entorno local, sigue estos pasos:

1.  Asegúrate de que tienes Git y un entorno de Python con Conda instalados.
2.  Clona el repositorio:
    `git clone https://github.com/ashes-0/vehicle-data-dashboard.git`
3.  Navega al directorio del proyecto:
    `cd vehicle-data-dashboard`
4.  Activa el entorno virtual (si ya lo tienes) o créalo con los paquetes del archivo `requirements.txt`:
    `conda create --name vehicles_env --file requirements.txt`
    `conda activate vehicles_env`
5.  Ejecuta la aplicación:
    `streamlit run app.py`

---

## Despliegue en la nube

Este panel de control está desplegado en Render y puede ser accedido a través del siguiente enlace:
-   [Enlace a la aplicación desplegada](https://vehicle-data-dashboard-app.onrender.com)