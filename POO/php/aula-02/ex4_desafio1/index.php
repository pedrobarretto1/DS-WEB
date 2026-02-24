<?php

abstract class Produto
{
    protected $nome;
    protected $preco;
    protected $estoque;

    public function __construct($nome, $preco, $estoque)
    {
        $this->nome = $nome;
        $this->preco = $preco;
        $this->estoque = $estoque;
    }

    // método abstrato
    abstract public function calcularDesconto();

    public function precoFinal()
    {
        $precoComDesconto = $this->calcularDesconto();

        // desconto extra se estoque baixo
        if ($this->estoque < 5) {
            $precoComDesconto -= $precoComDesconto * 0.10;
        }

        return $precoComDesconto;
    }

    public function mostrarProduto()
    {
        echo $this->nome . " - Preço final: R$ " . $this->precoFinal() . "<br>";
    }
}

class Eletronico extends Produto
{
    public function calcularDesconto()
    {
        return $this->preco - ($this->preco * 0.10);
    }
}

class Roupa extends Produto
{
    public function calcularDesconto()
    {
        return $this->preco - ($this->preco * 0.20);
    }
}

$produto1 = new Eletronico("Notebook", 3000, 3);
$produto2 = new Roupa("Camiseta", 100, 10);
$produto3 = new Roupa("Jaqueta", 250, 2);

$produto1->mostrarProduto();
$produto2->mostrarProduto();
$produto3->mostrarProduto();

?>