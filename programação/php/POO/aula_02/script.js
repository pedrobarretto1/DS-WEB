//maniulando o DOM

function byid(id) {
    return document.getElementById(id);
}

function seta() {
    return Document.setAttribute
}

const conteudo = byid("conteudo");

conteudo.innerHTML = "<p>Olá, mundo!</p>";
console.log(conteudo.innerHTML);



function mudatamanho() {
    conteudo.style.backgroundColor = "red";
    conteudo.innerHTML = "opa";
    console.log(conteudo.innerHTML);
}

//mudar de cor e o texto aleatoriamente sempre que aperta o botão
function mudatamanho() {
    const cores = ["red", "blue", "green", "yellow"];
    const textos = ["opa", "olá", "tudo bem?", "como vai?"];
}
