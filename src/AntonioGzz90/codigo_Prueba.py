from clases_orientado_objeto import Saludo
from clases_orientado_objeto import Preferencia
from clases_orientado_objeto import MiembrosdeFamilia

#CODIGO DEL PROGRAMA FINAL
print("***** Bienvenido al programa para sobrellevar la pandemia **** \n ** Ya que no deberias de salir, espero te entretengas un rato ** ")

print("** En esta cuarentena todos tenemos que tener sana distancia ** \n ** Son dias complicados, asi que manda un mensaje para un ser querido ** ")
persona = input(("-- Dime cual es el nombre de la persona-- : "))
saludo = input(("-- Dime algo que le quieres decir a alguna persona en especial-- : "))
nostalgia = Saludo(persona,saludo)
nostalgia.imprimirSaludo()

print("** Despues de haber desahogado, es hora de conocerte un poco mas a ti **")
primera = input("-- Dime que te gusta hacer --: ")
segunda = input("-- Dime otra cosa que te llene el corazon-- : ")
tercera = input("-- Dime por ultimo, algo que sea de tu agrado-- : ")

persona = Preferencia(primera, segunda, tercera)
persona.imprimirPreferencias()

print("** Ya para concluir, gracias a la pandemia haz podido conocer mas a tu familia ** \n ** Ahora dime cuales son sus nombres** \n !!!!! Si no tienes algunos de ellos, solo escribe 'No tengo' !!!!! ")
madre = input("-- ¿Cual es el nombre de tu madre? --: ")
padre = input("-- ¿Cual es el nombre de tu padre? --: ")
hermano = input("-- ¿Cual es el nombre de tu hermano? --: ")
hermana = input("-- ¿Cual es el nombre de tu hermana? --: ")

groveStreet = MiembrosdeFamilia(madre,padre,hermano,hermana)
groveStreet.imprimirFamily()

print("**** Espero que tengas un buen dia! ****")