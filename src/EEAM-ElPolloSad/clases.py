clase  laptop ():
    def  _init_ ( self , color , marca , ):
        self . color =  color
        self . marca=  marca  
        

    def  imprimirinfo ( self ):
        print ( f "Color: { self . color } \ n Marca: { self . marca}" )


clase Maestro ():
    def  _init_ ( self , matricula , nombre , materia ):
        self . matricula  =  matricula
        self . nombre  =  nombre
        self . materia  =  materia

    def  imprimirinfo ( self ):
        print ( f "Matricula: { self . matricula } \ n Nombre: { self . nombre } \ n Carrera: { self . materia } " )


clase  Serie ():
    def  _init_ ( self , titulo , genero , episodios ):
        self . titulo  =  titulo
        self . genero  =  genero
        self . episodios  =  episodios


    def  imprimirinfo ( self ):
        print ( f "Titulo: { self . titulo } \ n Genero: { self . genero } \ n episodios: { self . episodios } " )

clase  Tablet ():
    def  _init_ ( self , Marca , Precio , Modelo ):
        self . Marca =  Marca
        self . Precio =  Precio
        self . Modelo  =  Modelo


    def  imprimirinfo ( self ):
        print ( f "Marca: { self . Marca} \ n Precio: { self . Precio } \ n Modelo: { self . Modelo } " )
    
    clase  Ropa ():
    def  _init_ ( self , Marca , Precio , Talla):
        self . Marca =  Marca
        self . Precio =  Precio
        self . Talla  =  Talla


    def  imprimirinfo ( self ):
        print ( f "Marca: { self . Marca} \ n Precio: { self . Precio } \ n Talla: { self . Talla} " )
        
    clase  Beisbol ():
    def  _init_ ( self , Nombre , Campeonatos , Jugador):
        self . Nombre =  Nombre
        self . Campeonatos =  Campeonatos
        self . Jugadores =  Jugador


    def  imprimirinfo ( self ):
        print ( f "Nombre: { self . Nombre} \ n Campeonatos: { self . Campeonatos} \ n Jugador: { self . Jugador } " )