// Pega a URL atual
const urlParams = new URLSearchParams(window.location.search);

// Pega o valor do parâmetro 'nome'
const error_value = urlParams.get('error');

if (error_value == "login_error") {
    window.alert("Erro de Login")
}