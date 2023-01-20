# PI_01_Data06
PROYECTO INDIVIDUAL Nº1


Data Engineering


![image](https://user-images.githubusercontent.com/43472426/213601305-9b7e29de-4454-46cf-97b4-85fe8d0a207b.png)


Descripción del problema (Contexto y rol a desarrollar)
Contexto
Application Programming Interface es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles que permiten por ejemplo, crear pipelines facilitando mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy en día contamos con FastAPI, un web framework moderno y de alto rendimiento para construir APIs con Python.

Rol a desarrollar
Como parte del equipo de data de una empresa, el área de análisis de datos le solicita al área de Data Engineering (usted) ciertos requerimientos para el óptimo desarrollo de sus actividades. Usted deberá elaborar las transformaciones requeridas y disponibilizar los datos mediante la elaboración y ejecución de una API.

Propuesta de trabajo (requerimientos de aprobación)
Transformaciones: El analista de datos requiere estas, y solo estas, transformaciones para sus datos:

Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

De haber fechas, deberán tener el formato AAAA-mm-dd

Los campos de texto deberán estar en minúsculas, sin excepciones

El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)


Desarrollo API: Para disponibilizar los datos la empresa usa el framework FastAPI. El analista de datos requiere consultar:

Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

Película que más duró según año, plataforma y tipo de duración

Cantidad de series y películas por rating


Deployment: La empresa suele usar Deta (no necesita dockerizacion) para realizar el deploy de sus aplicaciones. Sin embargo, también puede usar Railway y Render (necesitan dockerizacion).

