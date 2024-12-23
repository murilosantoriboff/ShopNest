// Capturar os paremetros da url de registro e trata-las de forma correta

// Pega a URL atual
const urlParams = new URLSearchParams(window.location.search);

// Pega o valor do parâmetro 'nome'
const error_value = urlParams.get('erro');

if (error_value == "user_exists") {
    window.alert("Usuário ja existe!")
} else if (error_value == "different_passawords") {
    window.alert("Senhas não conferem")
} else if (error_value == "short_password") {
    window.alert("Senha muito curta")
} else if (error_value == "erro_unknown") {
    window.alert(error_value == "Erro desconhecido")
}