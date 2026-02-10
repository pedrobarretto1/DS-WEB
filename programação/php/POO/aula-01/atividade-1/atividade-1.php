<?php

class Console {
    public $geracao;
    public $potencial;
    public $cor;
    public $tamanho;
    public $marca;

    public function entretenimento(){
        echo "Entretenimento garantido com seu console da marca: " . $this->marca . "<br>";
    }

    public function jogar(){
        echo "Jogando num console de " . $this->geracao . " com potencial " . $this->potencial . "<br>";
    }

    public function assistir(){

        echo "Assistindo filme no console de cor " . $this->cor . "<br>";
    } 
}

class Caneta {
    public $cor;
    public $tamanho;
    public $tinta;
    public $marca;
    public $recarregavel;

    public function escrever(){
        echo "Escrevendo um texto na cor " . $this->cor . "<br>";
    }

    public function pintar(){
        echo "Pintando com a caneta " . $this->marca . " que usa tinta " . $this->tinta . "<br>";
    }

    public function brincar(){

        echo "Girando a caneta de tamanho " . $this->tamanho . " entre os dedos.<br>";
    }
}

class Caneca {
    public $tamanho;
    public $material;
    public $ml;
    public $cor;
    public $utilidade;

    public function tomar(){
        echo "Hora de " . $this->utilidade . " na caneca de " . $this->material . "<br>";
    }

    public function medir(){
        echo "Esta caneca comporta exatamente " . $this->ml . " ml.<br>";
    }

    public function usar(){
        echo "Usando a caneca " . $this->cor . " para decoração.<br>";
    }
}

class CaixaDeSom {
    public $tamanho;
    public $potencia;
    public $marca;
    public $cor;
    public $comOuSemFio;

    public function tocarMusica(){ 
        echo "Tocando música na potência " . $this->potencia . "!<br>";
    }

    public function divertir(){
        echo "A caixa da " . $this->marca . " está animando a festa.<br>";
    }

    public function entretenimento(){
        echo "Entretenimento " . $this->comOuSemFio . " na cor " . $this->cor . "<br>";
    }
}

class Janela {
    public $tamanho;
    public $enfeites;
    public $fixa;
    public $fabricante;
    public $local;

    public function abrir(){
        echo "Abrindo a janela que fica na " . $this->local . "<br>";
    }

    public function bloquearVento(){
        echo "Bloqueando vento na janela de tamanho " . $this->tamanho . " (Fixa: " . $this->fixa . ")<br>";
    }

    public function proteger(){
        echo "Janela feita por " . $this->fabricante . " com enfeites: " . $this->enfeites . "<br>";
    }
}

$canecaazul = new Caneca();
$canecaazul->tamanho = "Médio";
$canecaazul->material = "ceramica";

$canetapreta = new Caneta();
$canetapreta-> cor = "preta";
$canetapreta->tinta = "azul";

$consoleps5 = new Console();
$consoleps5->geracao = "9 geração";
$consoleps5->potencial = "alto";

$caixadesom = new CaixaDeSom();
$caixadesom->marca = "JBL";
$caixadesom->potencia = "50W";

$janela = new Janela();
$janela->local = "sala de estar";
$janela->tamanho = "grande";



?>