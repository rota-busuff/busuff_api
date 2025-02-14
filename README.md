# API para Rota BusUFF

## 📋 Requisitos  
- Python Flask  
    ```bash
    pip install flask
    ```
- Flask Restx  
    ```bash
    pip install flask-restx
    ```
- SQLAlchemy  
    ```bash
    pip install flask-sqlalchemy
    ```
- Marshmallow  
    ```bash
    pip install marshmallow-sqlalchemy
    ```

## ▶️ Executando a aplicação  

### ⚙️ Deploy Local  
Para realizar o deploy local, basta:  
1. Executar o arquivo `main.py`
2. Acessar, em um navegador, a URL:  
    ```
    http://localhost:5000
    ```
    A documentação SwaggerUI da API estará disponível em:  
    ```
    http://localhost:5000/docs
    ```

💡 **Dica:** Para encerrar a aplicação, basta pressionar `CTRL+C` no terminal em execução.  

---

### 🌐 Deploy Externo com Ngrok  
Para realizar um deploy temporário, para que tenha acesso externo, basta:  
1. Criar uma conta no [Ngrok](https://ngrok.com/)  
2. Baixar o Ngrok e configurar a autenticação (token)  
3. Realizar o deploy local (veja a seção anterior)  
4. Em outro terminal, executar o comando:  
    ```bash
    ngrok http <port>
    ```
    🚀 **Substitua** `<port>` pela porta local onde a aplicação foi hospedada, geralmente `5000`.  

Após isso, você verá um link gerado pelo Ngrok, algo como: 
`https://<subdomínio>.ngrok-free.app`