## Como exportar archivos de Nessus
  Exportar el reporte de Nessus en CSV, desde la opción "Export" de la esquina superior derecha y luego csv.

## Como usarlo
Los posibles argumentos de ohmyreport son:
-h: Muestra el mensaje de ayuda
-v: Activa el modo verboso
-o [obligatorio]: Nombre del/los archivo/s de salida (sin extención)
    Por defecto se crea el archivo Excel y el archivo Word
    -e: Crear el archivo Excel
    -w: Crear el archivo Word
-l [obligatorio]: Seleccionar el lenguaje de escritura. 
    Opciones: 
    es para Español
    en para Ingles
-c: Agregar el nombre del cliente objetivo. Por defecto: [empresa]
-n: Agregrar la salida del escaneo de puertos realizado en nmap para anexarlo al reporte ejecutivo. El mismo se debe guardar en formato xml con el argumento -oX
NESSUSFILE.csv: archivo csv exportado de Nessus

##Ejemplos
  `ohmyreport NESSUSFILE.csv  -o FILENAME --language en` reporte word y excel en ingles
  `ohmyreport NESSUSFILE.csv  -o FILENAME -w --language en` reporte word ingles
  `ohmyreport NESSUSFILE.csv  -o FILENAME --language es` reporte excel en español
