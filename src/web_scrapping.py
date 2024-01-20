# importar el modulo request para extrar una pagina web
import requests
# importar del modulo bs4 la libreria BeautifulSoup para transformar el codigo en html
from bs4 import BeautifulSoup
from datetime import datetime
# import pandas as pd
# import matplotlib.pyplot as plt

# Definimos la función webscrapping que depende de los argumentos url_scrapping
# página web a hacer el scrapping y la categoría que queremos extraer, categoria_scrapping.
# Al especificar "todas" nos saca todas las categorías de noticias
def webscraping(url_scraping,categoria_scraping='todas'):
    # Creamos una variable global para la URL
    url = url_scraping

    # Realizar la petición
    try:
        respuesta = requests.get(url) # Creamos el objeto respuesta
        #print(respuesta)
        #print(respuesta.text)
        # Verificar si la petición fue exitosa (código 200)
        if respuesta.status_code == 200:
            try:
                with open('../data/noticias.csv', 'w') as f: # Generamos archivo csv
                    f.write('titulo,url,categoria,fecha'+'\n') # Esto sería el encabezado del archivo
                # Analizar el contenido con BeautifulSoup
            except:
                print("ERROR: no se pudo crear el archivo noticias.csv")
            try:
                soup = BeautifulSoup(respuesta.text, 'html.parser')
                #print(soup)
                # Aquí puedes realizar operaciones de Web Scraping
                # ...
                try:
                    noticias = soup.find_all('article', class_='card-news')
                    if noticias:
                        #print(noticias)
                        lista_categorias = []
                        for articulo in noticias:
                            #print(articulo)
                            try:
                                titulo = articulo.find('a', class_='oop-link').text.strip() # text.strip saca la parte de texto de la clase, el titulo
                                url_noticia = articulo.find('a', class_='opp-link')['href'] # Con href sacamos la url de dentro de la clase
                                #print(url_noticia)
                                lista_url_noticia = url_noticia.split('/')
                                if lista_url_noticia[1] != '':
                                    categoria = lista_url_noticia[1] # Coge la posición 1 de la url donde se encuentra la categoria, en algunos casos puede estar vacía o no corresponder
                                    # y encontrarse en la posición 3
                                else:
                                    categoria = lista_url_noticia[3]
                                lista_categorias.append(categoria)
                                lista_fecha = url_noticia.split('--')  # obtenemos la fecha
                                fecha_caracteres = lista_fecha[1].replace('.html', '')
                                # print(fecha_caracteres)
                                # print(fecha_caracteres[0:4])
                                # print(fecha_caracteres[4:6])
                                # print(fecha_caracteres[6:8])
                                # print(fecha_caracteres[8:10])
                                # print(fecha_caracteres[10:12])
                                # print(fecha_caracteres[12:14])
                                fecha = datetime(int(fecha_caracteres[0:4]), int(fecha_caracteres[4:6]),
                                                 int(fecha_caracteres[6:8])) # Creación de la variable fecha a partir de una cadena de caracteres
                                fecha = fecha.strftime("%Y/%m/%d") # formato de la fecha Año, mes, día
                                titulo = titulo.replace('\'','').replace('"','').replace(',','')
                                if categoria_scraping == 'todas':
                                    try:
                                        with open('../data/noticias.csv', 'a') as f:
                                            f.write(titulo+','+url_noticia+','+categoria+','+str(fecha)+'\n')
                                        # Analizar el contenido con BeautifulSoup
                                    except:
                                        print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")
                                else:
                                    if categoria == categoria_scraping:
                                        try:
                                            with open('../data/noticias_'+categoria_scraping+'.csv', 'a') as f:
                                                f.write(titulo + ',' + url_noticia + ',' + categoria + ',' + str(
                                                    fecha) + '\n')
                                            # Analizar el contenido con BeautifulSoup
                                        except:
                                            print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")
                            except:
                                try:
                                    titulo = articulo.find('a', class_='lnk').text.strip()
                                    url_noticia = articulo.find('a', class_='lnk')['href']
                                    lista_url_noticia = url_noticia.split('/')
                                    if lista_url_noticia[1] != '':
                                        categoria = lista_url_noticia[1]
                                    else:
                                        categoria = lista_url_noticia[3]
                                    lista_categorias.append(categoria)
                                    lista_fecha = url_noticia.split('--')
                                    fecha_caracteres = lista_fecha[1].replace('.html', '')
                                    #print(fecha_caracteres)
                                    #print(fecha_caracteres[0:4])
                                    #print(fecha_caracteres[4:6])
                                    #print(fecha_caracteres[6:8])
                                    #print(fecha_caracteres[8:10])
                                    #print(fecha_caracteres[10:12])
                                    #print(fecha_caracteres[12:14])
                                    fecha = datetime(int(fecha_caracteres[0:4]), int(fecha_caracteres[4:6]), int(fecha_caracteres[6:8]))
                                    fecha = fecha.strftime("%Y/%m/%d")
                                    titulo = titulo.replace('\'', '').replace('"', '').replace(',', '')
                                    if categoria_scraping == 'todas':
                                        try:
                                            with open('../data/noticias.csv', 'a') as f:
                                                f.write(titulo + ',' + url_noticia + ',' + categoria + ',' + str(
                                                    fecha) + '\n')
                                            # Analizar el contenido con BeautifulSoup
                                        except:
                                            print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")
                                    else:
                                        if categoria == categoria_scraping:
                                            try:
                                                with open('../data/noticias_' + categoria_scraping + '.csv', 'a') as f:
                                                    f.write(titulo + ',' + url_noticia + ',' + categoria + ',' + str(
                                                        fecha) + '\n')
                                                # Analizar el contenido con BeautifulSoup
                                            except:
                                                print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")
                                except:
                                    pass
                        #print(lista_categorias)
                        conjunto_categorias = set(lista_categorias) # Convertimos la lista en un conjunto para que no saque duplicados
                        #print(conjunto_categorias)
                    else:
                        print(f"Error La pagina {url} no contiene noticias")
                except:
                        print(f"ERROR: No se pudo encontrar articulos en el codigo html")
            except:
                print(f"ERROR: no se pudo convertir la pagina a codigo html")
        else:
            print(f"Error al obtener la página web. Código de estado: {respuesta.status_code}")
    except:
        print(f"ERROR: No se puede abrir la web pagina {url} o existe un error al procesarla")
    return conjunto_categorias


listado_categorias = webscraping('https://www.telemadrid.es/','todas')
seleccion = 'x'
while seleccion != '0': # Para seleccionar 1 categoría determinada de la web creeamos el siguiente menú
    print("Lista de categorias: ")
    i = 1
    for opcion in listado_categorias:
        print(f"{i}.- {opcion}")
        i = i + 1
    print("0.- Salir")
    seleccion = input("Por favor seleccione una opcion indicando un numero:")
    categorias_listas = list(listado_categorias)
    categoria_seleccionada = categorias_listas[int(seleccion)-1]
    webscraping('https://www.telemadrid.es/', categoria_seleccionada) # función que definimos antes y
    # realiza webscrapping de la página indicada, telemadrid, de la categoría que seleccione el usuario (categoría_seleccionada)

