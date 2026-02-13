var contadoritem = 0;

function addlist(){
    contadoritem ++;
    console.log(contadoritem);

let novoitem = document.createElement("li");
novoitem.textContent = contadoritem + " - " + prompt("digite o nome do item");
novoitem.setAttribute ("id", contadoritem);
//teste de botão remover
let botaoremover = document.createElement("button");
botaoremover.textContent = "remover";
botaoremover.setAttribute("onclick", 'remover(${contadoritem})');



novoitem.appendChild(botaoremover);
document.getElementById("lista").appendChild(novoitem);


document.getElementById("lista").appendChild(novoitem);
}

function remover(itemlista){
//   console.log(contadoritem);
 //       let itemremovido = document.getElementById(prompt("qual item deseja remover?"));
 //       document.getElementById("lista").removeChild(itemremovido);
 //       if (itemremovido in [lista]) {
 //          alert("item não encontrado");
 //       } else {
 //          alert("item removido com sucesso");
  //      }
  var item = document.getElementById(itemlista)
  document.getElementById("lista").removeChild(item);
    }