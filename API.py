import requests    # Importar biblioteca requests
import json
# #pip install requests

##------------------------------------ GET  PY ----------------------------------##

# URL's de API #
urlPhotos = 'https://vercel-api-mongo-reactgram.vercel.app/api/photos/' # URL da API
urlUsers = 'https://vercel-api-mongo-reactgram.vercel.app/api/users/668520e47aba32f2469bdf45' # URL da API

 

def getRequestAPI(url):
    global urlPhotos
    global urlUsers
    
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2ODUyMGU0N2FiYTMyZjI0NjliZGY0NSIsImlhdCI6MTcyMjI1NTU1MiwiZXhwIjoxNzIyODYwMzUyfQ.q7pKvoL2aABCDjtCnowh75TIl53SzCacKW_GtSeJCSY' # Token da API

    headers = {                            # Definir os headers da requisição
        'Authorization': f'Bearer {token}' # Adicionar o token na requisição
    }

    url = urlPhotos if url == urlPhotos else urlUsers    # Operador Tenário
    
    response = requests.get(url, headers=headers)  # Solicitando a API conforme os dados definidos  

    if response.status_code == 200:                # Verificar o status da resposta
        dados = json.loads(response.text)          # Carregar os dados da requisição
        print('API Executada com sucesso!')        # Imprimir mensagem de sucesso
        todos = json.loads(response.content)
        print(todos[0]["comments"])  # Acessando o array dentro do objeto, e imprimindo o valor.

        # print(todos[0]["comments"][0]["userName"])  # Acessando o array dentro do objeto, e imprimindo o valor.
        
        # for i, item in enumerate(dados):          # looping com enumerate para imprimir os dados e seus indices    
            # print(f"Índice: {i}, Valor capturado : {item['image']}") #exibindo todos os dados
        
        # for item in dados:
        #     print(item["image"])

    else:
        print('Falha na requisição:', response.status_code)

# if __name__ == '__main__':
# getRequestAPI(urlPhotos)



##------------------------------------  REQUISIÇÃO API POST  PY ----------------------------------##

urlLogin = 'https://vercel-api-mongo-reactgram.vercel.app/api/users/login' # URL da API

def postRequestAPI(url):
    global urlLogin

    dados = {'email': 'nra19501@yahoo.com.br','password': '102030'}

    response = requests.post(url, json=dados)

    print(response.status_code)
    print(response.json())

postRequestAPI(urlLogin)