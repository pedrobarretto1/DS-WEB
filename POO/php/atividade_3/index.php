<?php

class fabricante {
    public $nome;
    public $pais;

    function __construct($nome, $pais) {
        $this -> nome = $nome;
        $this -> pais = $pais;
    }
}
class motor {
    public $potencia;
    public $combustivel;

    function __construct($potencia, $combustivel) {
        $this -> potencia = $potencia;
        $this -> combustivel = $combustivel;
    }
}

class carro {
    public $modelo;
    public $ano;
    public fabricante $fabricante;
    public motor $motor;

    function __construct($modelo, $ano, $fabricante, $motor) {
        $this -> modelo = $modelo;
        $this -> ano = $ano;
        $this -> fabricante = $fabricante;
        $this -> motor = $motor;
    }

    function exibirFicha() {
        echo "modelo: " . $this -> modelo . "<br>";
        echo "ano: " . $this -> ano . "<br>";
        echo "fabricante: " . $this -> fabricante -> nome . "<br>";
        echo "potência: " . $this -> motor -> potencia . "<br>";
        echo "combustível: " . $this -> motor -> combustivel . "<br>";
    }
}

$fabricante = new fabricante("ford", "estados unidos");
$motor = new motor("150 cavalos", "gasolina");
$carro = new carro("mustang", "2020", $fabricante, $motor);
$carro -> exibirFicha();
?>

