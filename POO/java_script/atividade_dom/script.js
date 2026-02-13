//exercicio 1
document.getElementById("changeColorBtn").addEventListener("click", function() {
    var container = document.getElementById("container");
    container.innerText = "O fundo mudou de cor!";
    container.style.backgroundColor = "lightblue";
});

//exercicio 2
document.getElementById("changeImage1Btn").addEventListener("click", function() {
    var image = document.getElementById("image");
    image.setAttribute("src", "imagem1.jpg");
});

document.getElementById("changeImage2Btn").addEventListener("click", function() {
    var image = document.getElementById("image");
    image.setAttribute("src", "imagem2.jpg");
});
document.getElementById("showImageSrcBtn").addEventListener("click", function() {
    var image = document.getElementById("image");
    var src = image.getAttribute("src");
    console.log("Valor do atributo src: " + src);
});

//Exercício 3 - Mudar a cor da página ao clicar para 3 cores diferentes com 3 botoes diferentes e adicionar um título correspondente à cor escolhida.
document.getElementById("vermelho").addEventListener("click", function() {
    document.body.style.backgroundColor = "red";
    document.title = "Vermelho";
});

document.getElementById("verde").addEventListener("click", function() {
    document.body.style.backgroundColor = "green";
    document.title = "Verde";
});
document.getElementById("azul").addEventListener("click", function() {
    document.body.style.backgroundColor = "blue";
    document.title = "Azul";
});