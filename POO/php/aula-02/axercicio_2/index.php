<?php
abstract class Animal {
public function fazerSom(){}
}
class Cachorro extends Animal {
public function fazerSom() {
echo "Au Au!";
}
}

class passaro extends Animal {
public function fazerSom() {
echo "piu piu";
}
}

class gato extends Animal {
public function fazerSom() {
echo "Miau Miau!";
}
}
$cachorro = new Cachorro();
echo "<br/>";
$cachorro->fazerSom();
$passaro = new passaro();
echo "<br/>";
$passaro->fazerSom();
$gato = new gato();
echo "<br/>";
$gato->fazerSom();
?>