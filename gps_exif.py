def modificar_exif_gps(exif):
    gps_exif_modificado = exif.replace("deg", "º")

    if any(dir in gps_exif_modificado for dir in ['S', 'E', 'N', 'W']):
        segmentos = gps_exif_modificado.split(", ")

        latitud = segmentos[0].strip().split()
        longitud = segmentos[1].strip().split()
        coordenada = f"{latitud[0]}{latitud[1]}{latitud[2].replace('\"', '')}{latitud[3]}{latitud[4]}, {longitud[0]}{longitud[1]}{longitud[2].replace('\"', '')}{longitud[3]}{longitud[4]}"
        return [coordenada]

    else:
        segmentos = gps_exif_modificado.split(", ")

        latitud_base = f"{segmentos[0].strip().replace('\"', '').replace(" ", "")}"
        longitud_base = f"{segmentos[1].strip().replace('\"', '').replace(" ", "")}"

        latitud_orientaciones = ['S', 'N']
        longitud_orientaciones = ['E', 'W']
        alternativas = []

    for lat in latitud_orientaciones:
        for lon in longitud_orientaciones:
            coordenada = f"{latitud_base}{lat}, {longitud_base}{lon}"
            alternativas.append(coordenada)
    return alternativas

texto_inicial = input("Ingresa las coordenadas: ")
resultados = modificar_exif_gps(texto_inicial)

for resultado in resultados:
    print(resultado)
