var contadoritem = 0;

function addlist(){
    contadoritem ++

let novoitem = document.createElement("li");
let novatarefa = document.getElementById("novatarefa").value;
novoitem.textContent = contadoritem + " - " + novatarefa;
novoitem.setAttribute ("id", contadoritem);

document.getElementById("lista").appendChild(novoitem);
}

function remover(itemlista){
   console.log(contadoritem);

   let itemremovido = document.getElementById(contadoritem);
        document.getElementById("lista").removeChild(itemremovido);
    }