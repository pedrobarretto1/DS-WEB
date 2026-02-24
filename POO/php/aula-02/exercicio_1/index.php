<?php

class Pessoa {
    public $nome = "Pedro";
    protected $idade = 18;
}

class Funcionario extends Pessoa {
    protected $salario = 1500;

    public function calcularBonus() {
        return 0;
    }

    public function salarioTotal() {
        return $this->salario + $this->calcularBonus();
    }
}

class Gerente extends Funcionario {
    public $funcao = "gerente de vendas";
    protected $salario = 3000;

    public function calcularBonus() {
        return $this->salario * 0.20;
    }
}

class Desenvolvedor extends Funcionario {
    public $habilidades = "php, java, python";
    protected $salario = 2500;

    public function calcularBonus() {
        return $this->salario * 0.10;
    }
}

$g = new Gerente();
$d = new Desenvolvedor();

echo "Salário + bônus gerente: " . $g->salarioTotal() . "<br>";
echo "Salário + bônus dev: " . $d->salarioTotal();

?>