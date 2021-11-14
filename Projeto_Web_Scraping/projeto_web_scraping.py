from web_scraping import web_scraping
from importar_csv import csv_conteudo, listas_menores
from tqdm import tqdm
from threading import Thread

# listas de CNPJ's dos CSV's
Lista_CNPJ = csv_conteudo()

divisao = (int(len(Lista_CNPJ) / 4) +1)
lista_dividida = list(listas_menores(Lista_CNPJ, divisao))

# threads/linhas/filas de Web_Scraping's simultâneos
fila_01 = Thread(target=web_scraping,args=(tqdm(lista_dividida[0]),))
fila_02 = Thread(target=web_scraping,args=(tqdm(lista_dividida[1]),))
fila_03 = Thread(target=web_scraping,args=(tqdm(lista_dividida[2]),))
fila_04 = Thread(target=web_scraping,args=(tqdm(lista_dividida[3]),))

fila_01.start()
fila_02.start()
fila_03.start()
fila_04.start()