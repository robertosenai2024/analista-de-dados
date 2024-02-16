"""
   17  git status
   18  git add importandoarquivoCSV.py
   19  git commit -m "Importando arquivos com csv - Primeiro commit com python"
   20  git push
   21  git fetch
   22  git push
   23  git push --set-upstream origin Csv-Json
   24  git status
   25  git pull
   26  git push origin
"""

import csv

with open("arquivo.csv","r") as arquivo:
    arquivo_csv= csv.reader(arquivo, delimiter=",")
    n = 0
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("REGIAO: " + str(linha))
        else:
            print("ID: "+ str(linha))



