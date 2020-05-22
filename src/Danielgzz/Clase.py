clase  Computadora ():
    def  __init__ ( self , color , marca , SO ):
        self . color =  color
        self . marca=  marca
        self . SO =  SO
        

    def  imprimirinfo ( self ):
        print ( f "Color: { self . color } \ n Marca: { self . marca} \ n Sistema O: { self . SO } " )


clase  Alumno ():
    def  __init__ ( self , matricula , nombre , carrera ):
        self . matricula  =  matricula
        self . nombre  =  nombre
        self . carrera  =  carrera

    def  imprimirinfo ( self ):
        print ( f "Matricula: { self . matricula } \ n Nombre: { self . nombre } \ n Carrera: { self . carrera } " )


clase  Pelicula ():
    def  __init__ ( self , titulo , genero , duracion ):
        self . titulo  =  titulo
        self . genero  =  genero
        self . duracion  =  duracion


    def  imprimirinfo ( self ):
        print ( f "Titulo: { self . titulo } \ n Genero: { self . genero } \ n Duracion: { self . duracion } " )

clase  Celular ():
    def  __init__ ( self , Marca , Precio , Clase ):
        self . Marca =  Marca
        self . Precio =  Precio
        self . Clase  =  Clase


    def  imprimirinfo ( self ):
        print ( f "Marca: { self . Marca} \ n Precio: { self . Precio } \ n Clase: { self . Clase } " )
    
    clase  Tenis ():
    def  __init__ ( self , Marca , Precio , Tamaño):
        self . Marca =  Marca
        self . Precio =  Precio
        self . Tamaño  =  Tamaño


    def  imprimirinfo ( self ):
        print ( f "Marca: { self . Marca} \ n Precio: { self . Precio } \ n Tamaño: { self . Tamaño} " )
        
    clase  EquipoFut ():
    def  __init__ ( self , Nombre , Estrellas , Jugador):
        self . Nombre =  Nombre
        self . Estrellas =  Estrellas
        self . Jugadores =  Jugador


    def  imprimirinfo ( self ):
        print ( f "Nombre: { self . Nombre} \ n Estrellas: { self . Estrellas} \ n Jugador: { self . Jugador } " )
        