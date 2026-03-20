import csv

# input = arquivo que envia informação
# output = arquivo que recebe informação
# key_words = palavras chaves a serem buscadas
input_file = "Estabelecimento.csv"
output_file = "CondominioFiltro.csv"
key_words = ["CONDOMINIO", "EDIFICIO", "CONDOMÍNIO", "EDIFÍCIO", "COND."]

# configurações de leitura
with open(input_file, "r", encoding="latin-1", newline="") as infile, \
     open(output_file, "w", encoding="utf-8", newline="") as outfile:
    
    reader = csv.reader(infile, delimiter=";")
    writer = csv.writer(outfile, delimiter=";", quoting=csv.QUOTE_ALL)

    # cabeçalho
    writer.writerow(["CNPJ", "NOME", "ENDERECO", "BAIRRO", "UF", "TELEFONE1", "TELEFONE2", "TELEFONE3"])

    print("Copiando arquivos, aguarde um momento...")

    total = 0
    filtrado = 0

    # varredura de dados
    for row in reader:
        total += 1
        nome = row[4].upper()

        if not any(p in nome for p in key_words):
            continue

        cnpj = "".join(x.strip() for x in row[0:3])
        endereco = " ".join(x.strip() for x in row[13:16])
        bairro = row[17].upper()
        uf = row[19].upper()
        tel1 = "".join(x.strip() for x in row[21:23])
        tel2 = "".join(x.strip() for x in row[23:25])
        tel3 = "".join(x.strip() for x in row[25:27])
        
        filtrado += 1
        writer.writerow([cnpj, nome, endereco, bairro, uf, tel1, tel2, tel3])

print("Arquivos copiados com sucesso!")
print(f"Total de linhas: {total}")
print(f"Linhas filtradas: {filtrado}")