# TCU-725
Aplicación para facilitar el seguimiento del progreso de proyectos para el CIMPA

# Anotaciones para mejoras

## Diseños faltantes
De momento hace falta completamente el diseño de las siguientes paginas:

* Colegios (El diseño original no tiene especificado aun lo que se espera para esta sección)

* Tutores (Aun faltan muchos datos en la base de datos para realizar esta sección correctamente)

De forma parcial se ha realizado las secciones de:

* Estudiantes (Existe informacion suficiente para crear parcialmente la sección, sin embargo no suficiente para concluirla)

<br>
<br>

## Base de datos:
 Para realizar ciertas tareas es complicado con la arquitectura actual de la base de datos, esto añadido a problemas de ausencia de datos necesarios para realizar ciertas relaciones por lo que se presentan las siguientes sugerencias:

 * Crear una relacion entre las tablas Estudiantes_Colegiales y Colegios_Inscritos.

 * Llevar un registro de los colegios a los que pertenece cada tutor crear una relacion entre las tablas Estudiante_TCU_UCR y Colegios_Inscritos para poder llevar un control de cuantos tutores hay distribuidos por institución y cantidad de estudiantes asignados a cada uno.

 * Opcional al punto anterior sería posible llevar un registro de a que tutor se le asigna cada estudiante a partir de una relación entre Estudiantes_TCU_UCR y Estudiantes_Colegiales.