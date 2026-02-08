# GPS_EXIF
Script que normaliza la salida del campo `GPS Position` de exiftool y facilita su uso en mapas en línea. Convierte formatos DMS con o sin letras de orientación, genera variantes cuando faltan orientaciones.
## Requisitos:

- Python 3.7+ (no requiere dependencias externas).
## Funcionalidades:

- Reemplaza "deg" por "º" y normaliza el formato.
- Si ya existen letras de orientación (N/S/E/W) devuelve la coordenada única normalizada.
- Si faltan las letras de orientación, genera las 4 combinaciones posibles (N/S × E/W).
- Convierte DMS a coordenadas decimales cuando es posible.
- Acepta entrada interactiva o por pipe desde exiftool.
## Instalación

1. Descargar o clonar el repositorio que contiene `gps_exif.py`.
```bash
git clone https://github.com/Bankroupt/GPS_exif.git
```
   
2. Ejecutar con Python:

```bash
python gps_exif.py
```
## Uso

- Ejecuta el script 

```bash
python gps_exif.py
```

- Escribe o pega la cadena que exiftool muestra en `GPS Position`, entradas soportadas
	- `26 deg 12' 14.76", 28 deg 2' 50.28"`
	- `26 deg 12' 14.76" N, 28 deg 2' 50.28" E`
	- `26º12'14.76", 28º2'50.28"`

Salida del script:

- Coordenada propuesta (o varias propuestas si faltaban orientaciones).
- Coordenadas en formato decimal (si se pudo convertir).
## Beneficios para investigación OSINT

- Automatiza la conversión de coordenadas DMS a decimal, reduciendo errores manuales.
- Soporta formatos inconsistentes de exiftool (con o sin orientación).
- Genera variantes cuando faltan orientaciones, útil en CTFs y análisis de metadatos incompletos.
