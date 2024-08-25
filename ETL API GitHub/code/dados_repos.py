import requests
import pandas as pd

# Essa classe envolve extração e transformação dos dados
class DadosRepositorios:
    
    # CONSTRUTOR , onde os atributos da classe estão (inicialização dos atributos do objeto durante a criação)
    def __init__(self, owner, nome_arquivo):
        self.owner = owner # nome dono da conta do github que se quer extrair os dados
        self.api_base_url = 'https://api.github.com'
        self.acess_token = <YOUR OWN TOKEN>
        self.headers = {'Authorization':'Bearer ' + self.acess_token , 
           'X-GitHub-Api-Version': '2022-11-28'}
        self.nome_arquivo = nome_arquivo
        
    # metódos da classe
    # EXTRAÇÃO
    def lista_repositorios(self):
        # extração dos dados dos repositorios de uma determinada conta do github
        repos_list = []

        # definindo a quantidade máxima de páginas
        resp = requests.get(f'{self.api_base_url}/users/{self.owner}')
        # resp.json()['public_repos'] => pega a quantidade máxima de repositórios que a página tem
        from math import ceil
        max = ceil(resp.json()['public_repos']/30)

        # PAGINAÇÃO
        for page_num in range(1,max + 1):
            try:
                # onde se é possível extrair os dados de cada página => page={page_num}
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url , headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        
        return repos_list
    
    # TRANSFORMAÇÃO
    # Seleção dos nomes dos repositórios
    def nomes_repos(self, repos_list):
        repos_name = []

        for pagina in range (len(repos_list)): # ou for page in repos_list
            for repos in range (len(repos_list[pagina])): # for repo in page
                    try:
                        repos_name.append(repos_list[pagina][repos]['name']) # repos_name.append(repo['name'])
                    except:
                         pass

        
        return repos_name
    
    def nomes_linguagens(self, repos_list):
        repos_language = []

        for page in repos_list:
            for repo in page:
                    try:
                        repos_language.append(repo['language']) 
                    except:
                         pass
                    
        return repos_language
    
    # metódo que chama os outros metodos para criar um dataframe para cada conta do github
    def cria_df_linguagens(self):
        
         repositorios = self.lista_repositorios()
         nomes = self.nomes_repos(repositorios)
         linguagens = self.nomes_linguagens(repositorios)

         dados = pd.DataFrame()
         dados['repositoriy_name'] = nomes
         dados['language'] = linguagens

         return dados
    
    def salvandoCSV(self):
        dados = self.cria_df_linguagens()
        dados.to_csv(f'dados/{self.nome_arquivo}.csv', index=False)

'''
# from dados_repos import DadosRepositorios
# Instanciando um objeto para teste
amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()
#print(ling_mais_usadas_amzn)

netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

# Salvando os dados 

ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv')
ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv')
ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')C
'''

netflix = DadosRepositorios('spotify', 'linguagens_spotify').salvandoCSV()

