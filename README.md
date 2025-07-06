# Trabajo-dirigido-clustering
 
## Experimento blob y blob_noisy:
hallazgos: 
DBSCAN: por defecto detectaba demasiadas clases, aumentando EPS bajo el numero manteniendo la deteccion de ruido. Con demasiadas clases DSGD se vuelve menos precisos que los otros metodos (menor accuracy).

las clases de ruido le cuesta más a DSGD encontrar reglas para estas que a los otros clasificadores

Tanto ripper como DT tienden a mostrar reglas para una unica feature ya que es facil de hacer la separación cuando se usa GMM o Kmeans. Mientras que DSGD es capaz de mostrar info para todas las features relevante, si uno baja el threshold podemos observar que la feature con ruido comienza a aparecer, pero con una importancia aproximadamente 4 veces mas bajay con una incertidumbre muy alta

## Experimento moon:
hallazgos:
DBSCAN con una buena configuración tiene mejor performance para detectar los cluster a pesar de tener peor silhouete, pero no se puede concluir mucho de la interpretabilidad, principalmente porque en el caso de Kmean y Gaussianlos clusters se cortan en un eje y las reglas tienden a eso.
Con DBSCAN notamos que el arbol de decisión le permite hacer las separaciones ya que puede hacer multiples cortes en el plano.
Ripper por su parte tiene la ventaja que puede generar reglas que hagan cortes en el plano o rectangulos dentro de este.
DSGD por su parte a las zonas en que se puede hacer separaciones lineales les da unos pesos muy grandes y las zonas en que entra en conflicto rapidamente bajan estos pesos


## Experimento Wine:
se dio algo muy curioso DT dio muy buen resultado comparadao con Ripper y DSClustering a pesar  de ser un arbol muy sencillo, probablemente porque puede tomar valores mejores para realizar los cortes


# Idea
Si el foco de clusters es identificar nuevos grupos a uno le gustaría tener la mayor cantidad de información sobre las features con el menor numero de reglas, se podria crear una formula para eso que evaluar el numero de reglas, normalizandolo con las features usadas / el total de features.