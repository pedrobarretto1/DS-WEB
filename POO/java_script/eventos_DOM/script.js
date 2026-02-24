//=========eventos do mouse=========

var area = document.getElementById("area");
var mensagem = document.getElementById("mensagem");
var posicao = document.getElementById("posicao");

area.addEventListener("mouseenter", function () {
    area.style.backgroundColor = "red";
    if (mensagem) mensagem.textContent = "O mouse entrou na área!";
});
area.addEventListener("click", function () {
    area.style.backgroundColor = "green";
});

area.addEventListener("dblclick", function () {
    area.style.backgroundColor = "blue";
});

area.addEventListener("mouseleave", function () {
    if (area.style.backgroundColor == "red") {
        area.style.backgroundColor = "white";
    } else {
        area.style.backgroundColor = "white";
    }
});

area.addEventListener("contextmenu", function(event){
event.preventDefault();
alert("Botão direito clicado!");
});

//========eventos do teclado=========
document.addEventListener("keydown", function(event){
var campo = document.getElementById("resultado");
campo.textContent = "Tecla pressionada: " + event.key;
console.log("Tecla pressionada: " + event.key);

//teclas e cores
var cores = {
    "0": "black",
    "1": "darkred",
    "2": "darkgreen",
    "3": "darkblue",
    "4": "darkorange",
    "5": "darkviolet",
    "6": "darkcyan",
    "7": "darkgoldenrod",
    "8": "darkmagenta",
    "9": "darkolivegreen",
    "a": "red",
    "e": "blue",
    "q": "green",
    "w":"yellow",
    "s":"purple",
    "d":"orange",
    "f":"cyan"
};

if (cores[event.key]) {
    area.style.backgroundColor = cores[event.key];
} else {
    area.style.backgroundColor = "lightblue";
}
});

if (click in area) {
    
}

    