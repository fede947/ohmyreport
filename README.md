## Como instalarlo
  Dentro de la carpeta ohmyreport descargada ejecutar `make install`

## Como exportar archivos de Nessus
  Exportar el reporte de Nessus en CSV, desde la opción "Export" de la esquina superior derecha y luego csv.

## Como usarlo
Los posibles argumentos de ohmyreport son:  

NESSUSFILE.csv: archivo csv exportado de Nessus

-h --help: Muestra el mensaje de ayuda  
-v --verbose: Activa el modo verboso  
-o --output: Nombre del/los archivo/s de salida (sin extención)  

    Por defecto se crea el archivo Excel y el Word
    -e --excel: Crear el archivo Excel  
    -w --word: Crear el archivo Word  

-l --language: Seleccionar el lenguaje de escritura.  

    Opciones:  
    es	para Español  
    en	para Ingles  

-c --client: Agregar el nombre del cliente objetivo. Por defecto: [empresa]  
-n --nmap: Agregrar la salida del escaneo de puertos realizado en nmap para anexarlo al reporte ejecutivo. El mismo se debe guardar en formato xml con el argumento -oX  


## Ejemplos  

`ohmyreport NESSUSFILE.csv` reporte word y excel en ingles  
`ohmyreport NESSUSFILE.csv  -o [PATH/]FILENAME --language en` reporte word y excel en ingles  
`ohmyreport NESSUSFILE.csv  -o [PATH/]FILENAME -w --language en` reporte word ingles  
`ohmyreport NESSUSFILE.csv  -o [PATH/]FILENAME -e --language es`reporte excel en español  
`ohmyreport NESSUSFILE.csv  -o [PATH/]FILENAME -c CLIENTNAME -n NMAP_EXIT.xml --language es`reporte word y excel en español agregando el nombre del cliente y el resultado del escaneo de puertos  
