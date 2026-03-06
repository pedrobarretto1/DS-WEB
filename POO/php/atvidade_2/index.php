<?php

class artista {
    public $nome;
    public $genero;

function __construct($nome, $genero) {
    $this -> nome = $nome;
    $this -> genero = $genero;
    }
}   

class musica {
    public $titulo;
    public $dura;
    public artista $artista;

    function __construct($titulo, $dura, $artista) {
        $this -> titulo = $titulo;
        $this -> dura = $dura;
        $this -> artista = $artista;

        }
}

$artista = new artista("michael jackson", "pop");
$musica = new musica("thriller", "5:57", $artista);
echo "O título da música é: " . $musica -> titulo . "<br>";
echo "A duração da música é: " . $musica -> dura . "<br>";
echo "O artista da música é: " . $musica -> artista -> nome . "<br>";
echo "O gênero do artista é: " . $musica -> artista -> genero . "<br>";

?>