# ANT-TP3 - MICROSERVICIO

DJANGO REST FRAMEWORK

Es una herramienta estandarizada para la creacion de API's.
Tiene 3 componentes los serializadores, las vistas y los routers.

-Los routers son una herramienta que nos permiten definir las urls de nuestro API de una manera sencilla y ordenada.
-Las views no son más que extensiones de las class-view de django, pero de alguna forma vitaminadas para simplificarnos el enganche con los routers, los serializadores y los modelos y en lugar de renderizar un html como respuesta devolver de forma sencilla un json, xml u otra estructura de datos que nos interese que devuelva nuestra API.
-Los serializadores nos permiten definir al detalle cómo serán las respuestas que devolverá nuestro API y cómo procesaremos el contenido de las peticiones que nos lleguen.

Conclusión
DRF es una herramienta muy potente, completa y madura, que nos permite construir APIs de una manera rápida y sencilla. Antepone la convención sobre la configuración, pero las opciones de configuración son muy extensas y bien documentadas.

Primero se inicializo un virtualenv, donde instalamos Django y se configuro(models, admin, urls, settings, views). Se modifico el archivoo models con una tabla llamada 'Cupones' junto con sus respectivos atributos. Para poder cumplir con la consigna se instalo Rest Framework para trabajar con los metoodos POST y GET mejor, se configuro sus archivos correspondientes para poder trabajar con Rest Framework. La consigna era crear una API con el fin de hacer un microservicio en el cual se puedan agregar cupones, para apartir de este poder conectarlo  a un microservicio de planes.



