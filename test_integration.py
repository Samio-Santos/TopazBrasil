import unittest
import requests

def get_github_user_info(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        data_json = response.json()
        return {
            "Name": data_json['name'],
            "Perfil": data_json['html_url'],
            "Número de repositórios públicos": data_json['public_repos'],
            "Seguidores": data_json['followers'],
            "Seguindo": data_json['following'],
            "lista_repositórios": data_json['repos_url']
        }
    else:
        return None

class TestGitHubUserInfoIntegration(unittest.TestCase):

    def test_get_github_user_info_integration_success(self):
        # Chama a função a ser testada com um usuário real do GitHub
        user_info = get_github_user_info("samio-santos")

        # Verifica se a função retornou um resultado não vazio
        self.assertIsNotNone(user_info)

        # Verifica se algumas chaves esperadas estão presentes no resultado
        self.assertIn("Name", user_info)
        self.assertIn("Perfil", user_info)
        self.assertIn("Número de repositórios públicos", user_info)
        self.assertIn("Seguidores", user_info)
        self.assertIn("Seguindo", user_info)
        self.assertIn("lista_repositórios", user_info)

    def test_get_github_user_info_integration_failure(self):
        # Chama a função a ser testada com um usuário que provavelmente não existe
        user_info = get_github_user_info("nonexistent_github_username")

        # Verifica se a função retornou None, indicando falha na solicitação
        self.assertIsNone(user_info)

if __name__ == '__main__':
    unittest.main()
