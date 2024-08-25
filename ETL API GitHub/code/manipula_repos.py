import requests
import base64

class ManipulaRepositorios:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.acess_token = <YOUR OWN TOKEN>
        self.headers = {'Authorization':'Bearer ' + self.acess_token , 
           'X-GitHub-Api-Version': '2022-11-28'}

    # criação de um novo repositorio        
    def cria_repo(self , nome_repo):
        data = {
        'name' : nome_repo,
        'description' : 'Dados do repositório de algumas empresas',
        'private' : True
        }

        response = requests.post(f'{self.api_base_url}/user/repos' , json=data , headers=self.headers)
        print(f'status code criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        with open(caminho_arquivo, 'rb') as file:
            file_content = file.read()

        encoded_content = base64.b64encode(file_content)

        #upload do arquivo com o PUT
        url = f'{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}'

        # definir o dicionario para fazer a atualização do arquivo
        data = {
            'message' : 'Adicionando um novo arquivo', # mensagem de commit 
            'content' : encoded_content.decode('utf-8') # passa o arquivo codificado em base64
        }

        response = requests.put(url, json=data , headers=self.headers)
        print(f'status code upload do arquivo: {response.status_code}')


#instanciando um objeto
novo_repo = ManipulaRepositorios('beabritoliveira')

#criando o repositório
nome_repo = 'linguagens-repositorio-empresas'
novo_repo.cria_repo(nome_repo)

#adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguas_rep_Amazon.csv' , '/home/bia/projeto_Requests/dados/linguas_rep_Amazon.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv' , '/home/bia/projeto_Requests/dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv' , '/home/bia/projeto_Requests/dados/linguagens_spotify.csv')

'''
#para deletar um repositório
owner = 'seu_username'
repo = 'linguagens-utilizadas'
url = f'https://api.github.com/repos/{owner}/{repo}'

response = requests.delete(url, headers=headers)
print(f"{response.status_code}")
'''
