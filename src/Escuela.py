clase  Alumno ():
    def  __init__ ( self , nombre , apellidop , edad , grado ):
        auto . nombre  =  nombre
        auto . apelliop  =  apellidop
        auto . edad  =  edad
        auto . grado  =  grado
    
    def  alumnoinformacion ( self ):
        print ( f "Nombre: { self . nombre }, Apellido paterno: { self . apellidop }, Edad: { self . edad } y Grado escolar: { self . grado } " )

clase  Maestro ():
    def  __init__ ( self , nombre , materia , salon ):
        auto . nombre  =  nombre
        auto . materia  =  materia
        auto . salon  =  salon

    def  maestroinformacion ( self ):
        print ( f "Nombre: { self . nombre }, Materia: { self . materia } y Salón: { self . salon } " )
        
clase  director ():
    def  __init__ ( self , nombre , suapellido , experiencia ):
        auto . nombre  =  nombre
        auto . suapellido  =  suapellido
        auto . experiencia  =  experiencia

    def  directorinformacion ( self ):
        print ( f "Nombre: { self . nombre } Apellido paterno: { self . suapellido } y Experiencia laboral: { self . experiencia } " )