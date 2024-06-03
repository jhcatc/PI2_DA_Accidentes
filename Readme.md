<p align='center'>
<img src ="statics//caba.png">
<p>

<h1 align='center'>
 <b>PROYECTO INTEGRADOR 2 - DA</b>
</h1>

# [Link para el Deploy del Dashboard en Render] (https://pi2-da-accidentes.onrender.com/)


# Presentación del Problema

## Descripción del Problema

En Buenos Aires, los siniestros viales representan una amenaza significativa para la seguridad pública. Estos accidentes, que involucran vehículos y peatones, resultan en daños materiales y, frecuentemente, en lesiones graves o muertes. En Argentina, con un promedio de 4.000 muertes anuales, los siniestros viales son la principal causa de muertes violentas. Entre 2018 y 2022, se registraron 19.630 fallecimientos, lo que se traduce en 11 víctimas fatales diarias. En 2022, 3.828 personas perdieron la vida en accidentes de tránsito, lo que evidencia la urgencia de abordar esta problemática.

## Contexto

La alta tasa de mortalidad por siniestros viales en Argentina, significativamente mayor que otras causas de muertes violentas, subraya la necesidad de intervenciones efectivas. Estas incluyen la educación vial, el cumplimiento de normas de tráfico, la mejora de la infraestructura vial y la promoción de vehículos más seguros. Un análisis detallado y el seguimiento de estadísticas son fundamentales para entender mejor el problema y formular políticas eficaces.

## Rol a Desarrollar

El Observatorio de Movilidad y Seguridad Vial (OMSV) de la Secretaría de Transporte de Buenos Aires nos ha encargado un proyecto de análisis de datos para ayudar a reducir las víctimas fatales en siniestros viales. Nos han proporcionado un dataset en formato xlsx con datos sobre homicidios en siniestros viales en Buenos Aires entre 2016 y 2021 y datos sobre lesionados en siniestros viales en Buenos Aires entre 2019 y 2021 (estos incluye Lesionados sea o no con homicidios). Este dataset incluye cuatro hojas principales: hechos y víctimas con homicidios y hechos y victimas de lesionados con o sin homicidios, junto con diccionarios de datos para facilitar la comprensión.

## Introducción a los Hallazgos y Conclusiones

#### Hallazgos

El análisis del dataset ha revelado patrones clave en los siniestros viales:

Tipo de Victima: Los accidentes muestran como pareto y con alta frecuencia comparativa donde las victimas son Motorizados o Peatones.
Relacion Lesionados - Homicidios: La tendencia de ocurrencia entre Lesionados y Homicidios se mantiene a lo largo del tiempo.
Factores de Riesgo: Son factores de influencia La edad y el género de las víctimas, donde la mayoria son Hombres en edades 25 - 40 años.
Zonas Críticas: No se Observa una gran influencia de la ubicación geografica, ya que los accidentes ocurren en forma muy distribuida en la ciudad.
Tendencia de los Siniestros: Se observa una completa falta de tendencia, no hay una estabilidad ni en alza ni en baja. 

#### Conclusiones

Basados en estos hallazgos, recomendamos:

Educación y Concientización: Campañas dirigidas a grupos de alto riesgo y durante períodos críticos, haciendo un gran enfasis en el correcto uso de cascos y mantener canal de circulacion para motorizados; como en los Peatones solo cruzar por puntos de cruce peatonal, respetar semaforos, no arriesgar al cruzar pensando que no habria problemas.
Infraestructura Vial: Mejoras en las zonas con alta incidencia de accidentes, como semáforos adicionales y mejor señalización, considerar la necesidad del peaton de coincidir por canales compartidos con vehiculos, garantizar todos los cruces necesarios.
Políticas de Tráfico: Refuerzo del cumplimiento de normas y políticas más estrictas en períodos de alto riesgo, Exigir a Motorizados el correcto uso de indumentaria con proteccion asi como respeto en los canales de circulacion y velocidades limites.
Estas recomendaciones proporcionan a las autoridades locales herramientas basadas en datos para tomar decisiones informadas y reducir significativamente las víctimas fatales en siniestros viales, mejorando la seguridad vial en Buenos Aires.

______

# Distribución del Proyecto

## ETL

Ubicado en el directorio:  code//etl.ipynb

Aca recibimos el Dataset en extension .xlsx y lo guardamos como .csv para comodidad de trabajo.
Hacemos cambios de los tipos de Datos, eliminando filas sin data 'SD' que no afectan la integridad de los datos.
Cambiamos los nombres de las columnas para facilitar el manejo, y quedarnos solo con las columnas que nos interesan.
Normalizamos y capitalizamos todos los textos de las columnas.
Para los faltantes de las columnas de 'DIRECCION', 'DIRECCION_NORMALIZADA' y 'XY_CABA', realizamos un crece de todas estas, apoyandonos en librerias de geolocalizacion y asi completamos estos faltantes.

## EDA

Ubicado en el directorio:  code//eda.ipynb

Iniciamos el proceso de EDA con cinco Dataframes.
df_homicidiosHechos - El cual contiene la Data de los hechos de siniestros Viales con Homicidios en un lapso temporal del año 2016 al 2021.
df_homicidiosVictimas - El cual contiene la Data de las victimas de siniestros Viales con Homicidios en un lapso temporal del año 2016 al 2021.
df_lesionadosHechos - El cual contiene la Data de los hechos de siniestros Viales con y sin Homicidios en un lapso temporal del año 2019 al 2021 (incluye lesionados lastimados que no llegan a Homicidios).
df_lesionadosVictimas - El cual contiene la Data de las victimas de siniestros Viales con y sin Homicidios en un lapso temporal del año 2019 al 2021 (incluye lesionados lastimados que no llegan a Homicidios).
df_poblacion_CABA - Data del total de la poblacion de la Comunidad Autónoma de Buenos Aires en un lapso temporal del año 2016 al 2021.

Revisemos las Tendencias y Distribuciones comparativas de los Hechos/Homicidios y Hechos/Lesionados.

Revisemos la localizacion geografica de los casos de Homicidios - Lesionados.

Revisemos la incidencia del tipo de Vehiculo (Victima) en el Accidente tanto en Homicidios como en Lesionados.

Evaluemos la incidencia de la Hora de ocurrencia del Accidente.

Evaluemos comparativamente Sexo y Edad de Accidentes que involucra Homicidios y solo Lesionados.

Evaluemos la relacion en la frecuencia de ocurrencia de Lesiones y Homicidios para cada mes del año.

Evaluemos la dispersion de las Ubicaciones respecto a las Victimas para Homicidios.

Evaluemos el TOP 10 de Ubicaciones para Lesionados y Homicidios.

Evaluemos los KPIs considerados para el analisis de este estudio.

## KPIs

Ubicado en el directorio:  code//eda.ipynb - Dentro del proceso del EDA.

** Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior.
Los valores Positivos en la columna 'REDUCCION' nos indica una reduccion respecto al semestre anterior, por su lado valores negativos indica un aumento. es conveniente evaluar que se ha hecho y dejado de hacer, ya que no existe ningun tipo de tendencia en la reduccion de Homicidios.
Si se ha hecho algun plan de accion este no ha surtido efecto buscado, aunque la falta de tendencia muestra posiblemente que no se ha trabajado ningun plan de accion atacando causas raices.

** Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior.
Valores positivos en la columna 'EVOLUCION_ANUAL' indica reduccion porcentual respecto al año anterior, por su lado valores negativos indica aumento porcentual respecto al año anterior.
De manera inmediata podemos repetir parte de las conclusiones en el KPI anterior.
Si se ha hecho algun plan de accion este no ha surtido efecto buscado, aunque la falta de tendencia muestra posiblemente que no se ha trabajado ningun plan de accion atacando causas raices.
En analisis anteriores vimos que Motos y Peatones eran la mayor proporcion de Victimas Mortales de Accidentes de Transito.
Si bien hay años donde la reduccion ha estado muy por encima de las metas propuestas en la medicion del KPI, lo que seria muy positivo, tambien vemos que este reduccion se pierde muy facilmente al llegar otro año.

** Aumentar la proporción de lesionados por cada homicidio en un 10% anual, respecto al año anterior.
Este KPI se centra en medir y gestionar la relación entre lesionados y homicidios, buscando que cada año se requiera un 10% más de lesionados para que ocurra un homicidio, en comparación con el año anterior. Aunque el objetivo no es incrementar el número de lesionados, en caso de que los incidentes ocurran, queremos asegurarnos de que la tasa de lesionados por homicidio aumente, reflejando una posible mejora en la capacidad de prevención de homicidios.
Nuestra META es la reduccion en un 10% del valor de PROPORCION respecto al AÑO anterior.
Podemos intuir lo visto en analisis anteriores de KPIs.
Si se ha hecho algun plan de accion este no ha surtido efecto buscado, aunque la falta de tendencia muestra posiblemente que no se ha trabajado ningun plan de accion atacando causas raices.
Si bien en ultimo año en estudio (2021) existe una considerable reduccion ha PROPORCION no alcanza a la meta propuestas en la medicion del KPI, lo que seria muy positivo si fuera repetitivo, tambien vemos que este reduccion viene de un aumento mucho mayor en la relacion en par de años anteriores.

## DATA

Ubicado en el directorio:  data. tenemos ocho archivos .csv que integran toda la Data manejada, Transformada y Guardada para y de todos los analisis.  <br />

** data//homicidios_hechos_etl.csv - Toda la Data de los hechos de siniestros Viales con Homicidios en un lapso temporal del año 2016 al 2021. <br />

** data//homicidios_lesionados.csv - Toda la Data cruzada de los Homicidios y Lesionados en un lapso temporal del año 2019 al 2021, usada para el KPI 3. <br />

** data//homicidios_victimas_etl.csv - Toda la Data de las victimas de siniestros Viales con Homicidios en un lapso temporal del año 2016 al 2021. <br />

** data//homicidiosHechos_Moto.csv - Toda la Data cruzada de los Homicidios ocurridos con Motociclistas como victima, en un lapso temporal del año 2016 al 2021, usada para el KPI 2. <br />

** data//homicidiosHechos_Semestre.csv - Toda la Data cruzada de los Homicidios ocurridos por Semestre, considerando la reduccion respecto al Semestre anterior, en un lapso  temporal del año 2016 al 2021, usada para el KPI 1. <br />

** data//lesiones_hechos_etl.csv - Toda la Data de los hechos de siniestros Viales con Lesionados (con o sin Homicidios) en un lapso temporal del año 2019 al 2021. <br />

** data//lesiones_victimas_etl.csv - Toda la Data de las victimas de siniestros Viales con Lesionados (con o sin Homicidios) en un lapso temporal del año 2019 al 2021. <br />

** data//poblacion_CABA.csv - Toda la Data de la poblacion de la Comunidad Autonoma de Buenos Aires en un lapso temporal de 2016 al 2021. <br />

___________

# Despliegue del Proyecto

## Streamlit

<p align='center'>
<img src ="statics//deploy.png">
<p>

Se realiza despliegue del Proyecto con la libreria de python Streamlit. <br />
La página consta de cinco links para explorar el analisis en general. <br />
** Introducción - breve descriccion y resumen del proyecto. <br />
** KPIs - Presentacion de los tres KPI, y graficas de los mismos. <br />
** Visualizaciones - Visualizaciones filtradas por AÑO, donde cada grafico puede ser ampliado para detallar mejor. <br />
Dispercion de Direcciones de sinisestros respecto a Victimas de Homicidios o de solo Lesiones. <br />
Proporcion de Homicidios y/o Lesiones respecto al Sexo de la vcitima. <br />
Frecuencia de Homicidios segun la edad de la victima. <br />
Frecuencia de Homicidios vs frecuencia de Lesionados por cada un Homicidio. <br />
Frecuencia de Homicidios respecto a la hora de ocurrencia. <br />
Frecuencia de Homicidios por cada Mes del Año. <br />
** Mapa Sinisestro - Mapa con la ocurrecio de Homicidios y Lesionados en CABA, filtrado por Lesionados o por Homicidios <br />
** Dataframe - Presentacion de los cuatro principales conjuntos de datos, interactivos que permite filtrar, ordenar y buscar por cada columna. <br />

## Repositorio

Introduccion.py - Ubicada en el directorio raiz de la aplicación. <br />
pages//01_📌_KPIs.py - Página de los KPIs. <br />
pages//02_📊_Visualizaciones.py - Página de las Visualizaciones. <br />
pages//03_🗺_Mapa_Siniestros.py - Página del mapa de los siniestros. <br />
pages//04_📇_Dataframes.py - Página con la presentacion de los Dataframe. <br />
code//mapa.html - Mapa en .html realizados con la libreria 'folium' de python, donde se representa los Homicidios y Lesionados en CABA, que luego es desplegado con su respectiva página.  <br />

## Base de Datos MySQL

En el directorio data_mysql - Tenemos la integracion de toda la Data lista para trabajar en MySQL

data//pi2_da.sql - Base de Datos donde incluimos los ocho Dataframe <br />
data//Tablas_Data.mwb - El archivo guardado de la modificacion y configuracion en Workbench, cambio de tipos de datos, relaciones de las tablas. <br />

Esta Data no es directamente usada en el proyecto expuesto (ya que estaremos trabajando con librerias de Python, Streamlit), pero se guardo listo para usar en caso que sea  <br />necesario para trabajar en MySQL o algun cambio de Visualizacion en otra aplicacion tipo PowerBI. <br />



__________