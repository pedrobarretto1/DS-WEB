<?php

class dono {
    public $nome;
    public $telefone;

    function __construct($nome, $telefone) {
        $this-> nome = $nome;
        $this -> telefone = $telefone;
    }

}

class animal {
    public $nome;
    public $especie;
    public dono $dono;

    function __construct($nome, $especie, $dono) {
        $this -> nome = $nome;
        $this -> especie = $especie;
        $this -> dono = $dono;
    }

}

$dono = new dono("pedro", "11987654321");
$animal = new animal("rex", "cachorro", $dono);
echo "O nome do animal é: " . $animal -> nome . "<br>";
echo "A espécie do animal é: " . $animal -> especie . "<br>";
echo "O dono do animal é: " . $animal -> dono -> nome . "<br>";
echo "O telefone do dono é: " . $animal -> dono -> telefone . "<br>";

?>