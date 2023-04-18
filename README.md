# Henry_lab_Daumian_Ruiz

## *info*
Este proyecto es un analisis de los datasets de "Amazon" "Netflix" "Disney" y "Hulu"

La limpieza de datos se hizo en deepnote y puedes acceder a ella en cualquier momento en el siguiente enlace
https://deepnote.com/workspace/daumian-ruiz-ceed-0677a995-df7e-45a8-9540-809a03138f79/project/HenryLabs-55a4c961-dc01-48e3-be55-1482ae5a9cce/notebook/DamianRuizLabs-065483e34ddc4a9db6cc70f17e08ea57

# *Limpieza*

Generar campo id: Cada id se compone de la primera letra del nombre de la plataforma,
ejemplo títulos el titulo "s123" de "Amazon" pasaria a llamarse "as123"

Los valores nulos del campo rating deberán reemplazarse por el string “G” 

Las fechas tienen el formato AAAA-mm-dd

Los campos de texto estan en minúsculas, sin excepciones

El campo duration debe convertirse en dos campos: duration_int y duration_type.
El primero es un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)


# *Fast API*

Se creo una Api con fastApi 
con los siguientes paths

*Home, contiene info*
@app.get("/")

*Cuantas Peliculas hay en esta plataforma*
@app.get("/get_count_platform/{plataforma}")\n\n

*Pelicula mas larga en determinado año y plataforma*
@app.get("/get_max_duration/{year}/{plataforma}")

*Cantidad de peliculas con un score superior al dado*
@app.get("/get_score_count/{platform}/{scored}/{year}")

*Cantidad de contenido total con un score superior*
@app.get("/get_contents/{rating}")
