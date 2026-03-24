import csv
from datetime import datetime

# input_file = arquivo que envia informação
# output_file = arquivo que recebe informação
# key_words = palavras chaves a serem buscadas
def filtrar_arquivo(input_file, output_file, key_words):
    
    # configurações de leitura
    with open(input_file, "r", encoding="latin-1", newline="") as infile, \
        open(output_file, "w", encoding="utf-8", newline="") as outfile:
        
        # delimitadores por ";"
        # reader = comando para ler arquivo
        # writer = comando para escrever em arquivo
        # QUOTE_ALL = coloca tudo entre aspas (força a celula a se tornar string)
        reader = csv.reader(infile, delimiter=";")
        writer = csv.writer(outfile, delimiter=";", quoting=csv.QUOTE_ALL)

        # escreve cabeçalho no novo arquivo
        writer.writerow([
            "CNPJ", "MATRIZ", "NOME", "SITUAÇÃO CADASTRAL", "DATA SITUAÇÃO CADASTRAL", 
            "NOME FANTASIA", "DATA DE INÍCIO DE ATIVIDADE", "CNAE PRINCIPAL", "CNAE SECUNDÁRIO", 
            "ENDERECO", "BAIRRO", "CEP", "UF", "CÓDIGO MUNICÍPIO", 
            "TELEFONE1", "TELEFONE2", "FAX", "EMAIL"
            ]) #18

        total = 0
        filtrado = 0

        # varredura de dados
        for row in reader:
            total += 1
            cnpj = "".join(x.strip() for x in row[0:3])
            nome = row[4].upper()

            # se o nome que foi lido NÃO corresponde as palavras chaves escritas = não faça nada
            if not any((p in nome) or (p in cnpj) for p in key_words):
                continue
            
            # caso nome corresponda as palavras chaves = siga os comandos abaixo
            # variaveis para organizar as informações uteis e que sejam de acordo com o cabeçalho delimitado
            matriz = row[3]
            situ_cadastral = row[5]
            try:
                data_situ_cadatral = datetime.strptime(row[6], "%Y%m%d")
                data_situ_cadatral_formatada = data_situ_cadatral.strftime("%d/%m/%Y")
            except:
                continue
            nome_fantasia = row[8].upper()
            try:
                data_abertura = datetime.strptime(row[10], "%Y%m%d")
                data_abertura_formatada = data_abertura.strftime("%d/%m/%Y")
            except:
                continue
            cnae1 = row[11]
            cnae2 = row[12]
            endereco = " ".join(x.strip() for x in row[13:17]).upper()
            bairro = row[17].upper()
            cep = row[18]
            uf = row[19].upper()
            municipioIBGE = row[20]
            tel1 = " ".join(x.strip() for x in row[21:23])
            tel2 = " ".join(x.strip() for x in row[23:25])
            fax = " ".join(x.strip() for x in row[25:27])
            email = row[27].lower()
            #18
            
            filtrado += 1

            # escrever dados abaixo do cabeçalho na ordem informada
            writer.writerow([
                cnpj, matriz, nome, situ_cadastral, data_situ_cadatral_formatada, nome_fantasia, data_abertura_formatada, 
                cnae1, cnae2, endereco, bairro, cep, uf, municipioIBGE, tel1, tel2, fax, email
            ]) #18
    
    return total, filtrado