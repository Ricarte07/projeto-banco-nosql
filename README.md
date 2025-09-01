# Projeto Banco Virtual com NoSQL

Este projeto é uma aplicação web simples que simula a listagem de clientes de um banco, desenvolvido para uma apresentação sobre bancos de dados não relacionais (NoSQL).

---

### Tecnologias Utilizadas

* **Backend:** Python com Flask
* **Banco de Dados:** MongoDB (NoSQL - Documentos)
* **Ambiente:** Docker
* **Frontend:** HTML e JavaScript

---

### Pré-requisitos

Antes de começar, garanta que você tem as seguintes ferramentas instaladas na sua máquina:
* [Git](https://git-scm.com/downloads)
* [Python 3.10+](https://www.python.org/downloads/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

---

### Como Rodar o Projeto

Siga os passos abaixo para executar a aplicação localmente.

**1. Clonar o Repositório**
Abra seu terminal e clone este repositório para a sua máquina:
```bash
git clone [URL_DO_SEU_REPOSITORIO_AQUI]
```

**2. Acessar a Pasta do Projeto**
```bash
cd nome-da-pasta-do-projeto
```

**3. Criar e Ativar o Ambiente Virtual**
É uma boa prática isolar as dependências do projeto.
```powershell
# Criar o ambiente
python -m venv venv

# Ativar o ambiente (no Windows PowerShell)
.\venv\Scripts\Activate
```

**4. Instalar as Dependências**
Este comando vai ler o arquivo `requirements.txt` e instalar todas as bibliotecas Python necessárias.
```bash
pip install -r requirements.txt
```

**5. Iniciar o Banco de Dados com Docker**
Garanta que o Docker Desktop esteja aberto e rodando em seu computador. Em seguida, execute o comando abaixo para iniciar o container do MongoDB.
```bash
docker run -d --name meu-mongo -p 27017:27017 mongo
```
*Este comando só precisa ser executado uma vez. Se o container já existir, você pode iniciá-lo com `docker start meu-mongo`.*

**6. Executar a Aplicação**
Com o banco de dados rodando, inicie o servidor Flask:
```bash
python app.py
```
O terminal irá indicar que o servidor está rodando no endereço `http://12.0.0.1:5000`.

**7. Acessar no Navegador**
Abra seu navegador de internet e acesse a seguinte URL:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

Você verá a página inicial. Clique no botão "Buscar Clientes" para carregar os dados do banco MongoDB.
