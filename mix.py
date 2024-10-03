from pydub import AudioSegment
from tqdm import tqdm  # Importar tqdm

# Cargar los archivos de audio
audio_files = [
    {"file": "C:/Users/acer/Documents/Workspace/audio_prjc_salo/pantera_rosa.mp3", "start": 0, "end": 39},  # Archivo 1
    {"file": "C:/Users/acer/Documents/Workspace/audio_prjc_salo/abusadamente.mp3", "start": 23, "end": 42},  # Archivo 2
    {"file": "C:/Users/acer/Documents/Workspace/audio_prjc_salo/calimenio.mp3", "start": 0, "end": 54},  # Archivo 3
    {"file": "C:/Users/acer/Documents/Workspace/audio_prjc_salo/ta_ok.mp3", "start": 17, "end": 74},  # Archivo 4 corregido
    {"file": "C:/Users/acer/Documents/Workspace/audio_prjc_salo/abusadora.mp3", "start": 73, "end": 90},  # Archivo 5 corregido
    {"file": "C:/Users/acer/Documents/Workspace/audio_prjc_salo/la_espeluca.mp3", "start": 55, "end": 86},  # Archivo 6 corregido
    {"file": "C:/Users/acer/Documents/Workspace/audio_prjc_salo/tambores_de_mi_tierra.mp3", "start": 60, "end": 91},  # Archivo 7
]

# Crear una lista para almacenar los audios procesados (con cortes, fades y silencio entre audios)
audios_procesados = []

# Duración del fade out en milisegundos (2 segundos)
fade_duration = 2000

# Duración del silencio entre audios (2 segundos)
silencio_duracion = 2000  # en milisegundos

# Procesar cada archivo: cortar el intervalo, aplicar fade out, y añadir silencio entre audios
for audio_data in tqdm(audio_files, desc="Procesando archivos de audio"):
    file = audio_data["file"]
    start_time = audio_data["start"] * 1000  # Convertir segundos a milisegundos
    end_time = audio_data["end"] * 1000  # Convertir segundos a milisegundos
    
    # Cargar el archivo de audio
    audio = AudioSegment.from_file(file, format="mp3")
    
    # Recortar el archivo desde start_time hasta end_time
    audio_recortado = audio[start_time:end_time]
    
    # Aplicar fade out al archivo recortado
    audio_con_fade = audio_recortado.fade_out(fade_duration)
    
    # Añadir el audio procesado a la lista
    audios_procesados.append(audio_con_fade)

# Inicializar el primer archivo en el audio final
audio_final = audios_procesados[0]

# Generar un segmento de silencio de 2 segundos
silencio = AudioSegment.silent(duration=silencio_duracion)

# Unir el resto de archivos procesados con el silencio de 2 segundos entre cada uno
for audio in tqdm(audios_procesados[1:], desc="Uniendo audios"):
    audio_final += silencio + audio  # Añadir silencio antes de concatenar el siguiente audio

# Exportar el archivo final con los fades y los cortes de silencio
ruta_guardado = "C:/Users/acer/Documents/Workspace/audio_prjc_salo/audio_final_con_cortes_fade_silencio.mp3"
audio_final.export(ruta_guardado, format="mp3")

print("¡Unión completada con éxito y guardada como 'audio_final_con_cortes_fade_silencio.mp3'! en " + ruta_guardado)
