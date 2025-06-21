# Trabajo-dirigido-clustering
 
## Experimento blob y blob_noisy:
hallazgos: 
DBSCAN: por defecto detectaba demasiadas clases, aumentando EPS bajo el numero manteniendo la deteccion de ruido. Con demasiadas clases DSGD se vuelve menos precisos que los otros metodos (menor accuracy).

las clases de ruido le cuesta más a DSGD encontrar reglas para estas que a los otros clasificadores

Tanto ripper como DT tienden a mostrar reglas para una unica feature ya que es facil de hacer la separación cuando se usa GMM o Kmeans. Mientras que DSGD es capaz de mostrar info para todas las features relevante, si uno baja el threshold podemos observar que la feature con ruido comienza a aparecer, pero con una importancia aproximadamente 4 veces mas bajay con una incertidumbre muy alta