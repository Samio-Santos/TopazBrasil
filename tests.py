import unittest
from unittest.mock import patch, Mock
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

class TestGitHubUserInfo(unittest.TestCase):
    @patch('requests.get')
    def test_get_github_user_info_success(self, mock_get):
        # Simula uma resposta de sucesso da API do GitHub
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "Test User",
            "html_url": "https://github.com/testuser",
            "public_repos": 10,
            "followers": 100,
            "following": 50,
            "repos_url": "https://api.github.com/users/testuser/repos"
        }
        mock_get.return_value = mock_response

        # Chama a função a ser testada
        user_info = get_github_user_info("testuser")

        # Verifica se a função retorna o resultado esperado
        expected_result = {
            "Name": "Test User",
            "Perfil": "https://github.com/testuser",
            "Número de repositórios públicos": 10,
            "Seguidores": 100,
            "Seguindo": 50,
            "lista_repositórios": "https://api.github.com/users/testuser/repos"
        }
        self.assertEqual(user_info, expected_result)

    @patch('requests.get')
    def test_get_github_user_info_failure(self, mock_get):
        # Simula uma resposta de falha da API do GitHub
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Chama a função a ser testada
        user_info = get_github_user_info("nonexistentuser")

        # Verifica se a função retorna None em caso de falha
        self.assertIsNone(user_info)

if __name__ == '__main__':
    unittest.main()
