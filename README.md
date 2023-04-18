


# Henry_lab_Daumian_Ruiz

# *info*
Este proyecto es un analisis de los datasets de "Amazon" "Netflix" "Disney" y "Hulu"

La limpieza de datos se hizo en deepnote y puedes acceder a ella en cualquier momento en el siguiente enlace
https://deepnote.com/workspace/daumian-ruiz-ceed-0677a995-df7e-45a8-9540-809a03138f79/project/HenryLabs-55a4c961-dc01-48e3-be55-1482ae5a9cce/notebook/DamianRuizLabs-065483e34ddc4a9db6cc70f17e08ea57

# *Limpieza*

Durante la limpieza de los datos, se llevaron a cabo los siguientes procesos:

-Generación del campo ID: cada ID se compone de la primera letra del nombre de la plataforma. Por ejemplo, el título "s123" de "Amazon" pasó a llamarse "as123".

-Reemplazo de los valores nulos del campo rating por el string “G”.

-Formato de fechas: AAAA-mm-dd.

-Los campos de texto están en minúsculas, sin excepciones.

-Conversión del campo duration en dos campos: duration_int y duration_type. El primero es un integer y el segundo es un string que indica la unidad de medición de duración: min (minutos) o season (temporadas).

# *Fast API*

Este proyecto también incluye una API con FastAPI que cuenta con los siguientes endpoints:

## *Home: contiene información general del proyecto. Se accede a través de la ruta*

@app.get("/")

## *Cantidad de películas en una plataforma determinada. Se accede a través de la ruta* 

@app.get("/get_count_platform/{plataforma}")\n\n

## *Película más larga en un año y plataforma determinados. Se accede a través de la ruta* 

@app.get("/get_max_duration/{year}/{plataforma}")

## *Cantidad de películas con una puntuación superior a la dada en una plataforma y año determinados. Se accede a través de la ruta* 

@app.get("/get_score_count/{platform}/{scored}/{year}")

## *Cantidad total de contenido con una puntuación superior a la dada. Se accede a través de la ruta* 

@app.get("/get_contents/{rating}")

# *Contenido Adicional*

Puedes ver un video con la informacion en
https://www.youtube.com/watch?v=DLzylLGxy7M

# ¡Espero que esta propuesta te haya sido útil! Si tienes alguna duda o necesitas alguna ayuda adicional, no dudes en preguntar.
