from transformers import pipeline

#crear un pipeline de analisis de sentimiento
clasificador = pipeline('sentiment-analysis')

#analizar una sentenfia
resultado = clasificador("me es indiferente saber utilizar python")
print(resultado)
resultado2 = clasificador("no prefiero madrugar pero a veces si me dan ganas")
print(resultado2)