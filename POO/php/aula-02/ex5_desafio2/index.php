<?php

class Documento {

    private $numero;

    public function setNumero($n) {
        $this->numero = $n;
    }

    public function getNumero() {
        return $this->numero;
    }

}

class CPF extends Documento {

    public function validar() {

        $cpf = $this->getNumero();

        $soma = 0;

        for ($i = 0; $i < 9; $i++) {
            $soma = $soma + ($cpf[$i] * (10 - $i));
        }

        $d1 = ($soma * 10) % 11;
        if ($d1 == 10) {
            $d1 = 0;
        }

        $soma = 0;

        for ($i = 0; $i < 10; $i++) {
            $soma = $soma + ($cpf[$i] * (11 - $i));
        }

        $d2 = ($soma * 10) % 11;
        if ($d2 == 10) {
            $d2 = 0;
        }

        if ($cpf[9] == $d1 && $cpf[10] == $d2) {
            return true;
        } else {
            return false;
        }

    }

}

$cpf = new CPF();

$cpf->setNumero("52998224725");

if ($cpf->validar()) {
    echo "CPF valido";
} else {
    echo "CPF invalido";
}

?>