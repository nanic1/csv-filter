# CSV Filter

Este projeto consiste em um Scrap via **csv**, onde a partir de uma base, um código em **Python** busca por informações específicas com base em palavras chaves. O app também diz quantas linhas foram lidas na base e quantas dessas linhas foram filtradas no novo arquivo.

O objetivo desse projetos é praticar habilidades em Scrap básico utilizando csv para evoluir minhas habilidades nesse tema.

---

## Tecnologias usadas

* Python
* CSV
* Excel (visualização do projeto)

---

## Como executar o projeto
### 1- Clone este repositorio no seu computador. Escolha um ambiente onde consiga acessar a pasta com facilidade.
No seu terminal, execute:
```
git clone https://github.com/nanic1/csv-filter-apsa
cd csv-filter-apsa
```

### 2- Configurar ambiente
Na raiz do projeto, defina a base que quer filtrar as informações como **"Estabelecimento.csv"**. O filtro será feito no arquivo **"Condominiofiltro.csv"**

### 3- Execução do projeto
Após todas as etapas, finalmente podemos executar e filtrar as informações da base.
Dentro do projeto, execute este comando:
```
python column-read.py
```

Se não houver nenhum erro, seu terminal deve exibir:
```
Copiando arquivos, aguarde um momento...
```

Após a filtragem dos dados, o arquivo **"Condominiofiltro.csv"** terá seus dados filtrados de acordo com as palavras chaves definidas.

---

## Autor
Pedro Kurtz
