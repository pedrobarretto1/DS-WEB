// Pegar o formulário
var formulario = document.getElementById('cadastro');

formulario.addEventListener('submit', function(evento) {
    evento.preventDefault();

    var nome = document.getElementById('nome').value;
    var email = document.getElementById('email').value;
    var registro = document.getElementById('registro').value;
    var telefone = document.getElementById('telefone').value;
    var turma = document.getElementById('turma').value;

    var novoAluno = document.createElement('li');

    novoAluno.textContent = nome + ' - ' + email + ' - ' + registro + ' - ' + telefone + ' - ' + turma;

    document.getElementById('lista').appendChild(novoAluno);

    document.getElementById('nome').value = '';
    document.getElementById('email').value = '';
    document.getElementById('registro').value = '';
    document.getElementById('telefone').value = '';
    document.getElementById('turma').value = '';

    document.getElementById('nome').focus();
});