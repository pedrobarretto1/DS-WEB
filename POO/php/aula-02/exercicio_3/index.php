<?php


class Veiculo {
    public $marca;
    public $modelo;
    private $velocidade;

    public function __construct($marca, $modelo) {
        $this->marca = $marca;
        $this->modelo = $modelo;
        $this->velocidade = 0;
    }
    public function setVelocidade($velocidade) {
        $this->velocidade = $velocidade;
    }

    public function getVelocidade() {
        return $this->velocidade;
    }
}

class Carro extends Veiculo {
    public function acelerar() {
        $this->setVelocidade($this->getVelocidade() + 10);
        return "O carro acelerou para " . $this->getVelocidade() . " km/h";
    }
}

class Moto extends Veiculo {
    public function acelerar() {
        $this->setVelocidade($this->getVelocidade() + 20);
        return "A moto acelerou para " . $this->getVelocidade() . " km/h";
    }
}


// Instanciando objetos e exibindo comportamentos
$carro = new Carro("Toyota", "Corolla");
$moto = new Moto("Honda", "CBR");

echo "Carro: " . $carro->marca . " " . $carro->modelo . "<br>";
echo $carro->acelerar() . "<br>";
echo $carro->acelerar() . "<br>";

echo "Moto: " . $moto->marca . " " . $moto->modelo . "<br>";
echo $moto->acelerar() . "<br>";
echo $moto->acelerar() . "<br>";

?>