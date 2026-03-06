<?php
class pessoa {
    public $nome;
    public $idade;

    public function __construct( $novonome, $novaidade ) {
        $this ->nome = $novonome;
        $this->idade = $novaidade;

    }

    public function exibirdados() {
        return "o nome da pessoa é: " . $this->nome . " e a idade é: " . $this->idade;
    }
}
$pedro = new pessoa("pedro", 18);
echo $pedro ->exibirdados();



?>