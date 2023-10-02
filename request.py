import requests

def get_github_user_info(username):
    # URL para a qual você deseja fazer a solicitação GET
    url = f'https://api.github.com/users/{username}'

    # Faz a solicitação GET
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        data_json = response.json()
        # Retorna as informações do usuário como um dicionário
        return {
            "Name": data_json['name'],
            "Perfil": data_json['html_url'],
            "Número de repositórios públicos": data_json['public_repos'],
            "Seguidores": data_json['followers'],
            "Seguindo": data_json['following'],
            "lista_repositórios": data_json['repos_url']
        }
    else:
        # Retorna None se a solicitação falhar
        return None

# Solicita o nome de usuário ao usuário
user = input('Digite o nome do usuário do GitHub: ')

# Obtém as informações do usuário
user_info = get_github_user_info(user)

if user_info:    
    # Salva as informações em um arquivo de texto
    with open(f'{user}_github_info.txt', 'w', encoding='utf-8') as file:
        for key, value in user_info.items():
            file.write(f"{key}: {value}\n")
    print(f"As informações foram salvas em {user}_github_info.txt")

else:
    print("A solicitação falhou. Verifique o nome de usuário.")
