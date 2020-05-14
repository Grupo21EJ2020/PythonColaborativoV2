from clases_thomas import Carro, Motocicleta, Pantalon, Persona
from clase_tenis import Tenis
from clase_videojuego import Videojuego
from clase_estudiante import Estudiante

Auto = Carro("Ford", "Mustang", 2020 )
Auto.imprimirInfo()

Moto = Motocicleta("Honda", "Navi", 2019 )
Moto.imprimirInfo()

pantalon = Pantalon("Levi's", "Azul", "mezclilla" )
pantalon.imprimirInfo()

juego = Videojuego("Resident Evil 2", "PS4 y Xbox one", "digital" )
juego.imprimirInfo()

alguien = Persona("Thomas", 19, "mexicano" )
alguien.imprimirInfo()

zapato = Tenis("Nike", "Blanco", 8 )
zapato.imprimirInfo()

alumno = Estudiante("Thomas", 1842782, 96)
alumno.imprimirInfo()