// Pegar o formulário
var formulario = document.getElementById('cadastro');
var listaElement = document.getElementById('lista');

// Usa um array para armazenar os alunos
var alunos = [];

// Função que renderiza a lista de alunos no DOM a partir do array
function renderLista() {
    listaElement.innerHTML = '';
    alunos.forEach(function(aluno) {
        let li = document.createElement('li');
        li.innerHTML = aluno.nome + '<br>' + aluno.email + '<br> ' + aluno.registro + '<br> ' + aluno.telefone + '<br>' + aluno.turma;
        listaElement.appendChild(li);
    });
}

function remover() {
    if (alunos.length > 0) {
        alunos.pop();
        let lista = document.getElementById("lista");
        lista.removeChild(lista.lastChild);
    }}

    formulario.addEventListener('submit', function(evento) {
        evento.preventDefault();

        let nome = document.getElementById('nome').value;
        let email = document.getElementById('email').value;
        let registro = document.getElementById('registro').value;
        let telefone = document.getElementById('telefone').value;
        let turma = document.getElementById('turma').value;

        // Cria um objeto aluno e adiciona ao array
        var aluno = {
            nome: nome,
            email: email,
            registro: registro,
            telefone: telefone,
            turma: turma

        };

    alunos.push(aluno);
    renderLista();
    document.getElementById('aluno').value = '<br>';

});