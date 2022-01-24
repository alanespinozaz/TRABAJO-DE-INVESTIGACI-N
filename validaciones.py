from departamento import Departamento
from cargo import Cargo

class Validar:
    def __init__(self):
        pass

    def validarCedula(dni):
        dig=dni.isdigit()
        if dig==True:
            return True
        else:
            return False

    def buscarcargo(cod):
        car = 0     
        for pos in range(0,len(Cargo.cargos)):
            Carg = Cargo.cargos[pos]
            if Carg["cargo"] == cod:
                car = Carg["cargo"]
                break
        return car 

    def buscardepartamento(cod):
        car = 0     
        for pos in range(0,len(Departamento.departamentos)):
            depar = Departamento.departamentos[pos]
            if depar["departamento"] == cod:
                car = depar["departamento"]
                break
        return car 
    
    def validarSueldo(suel):
        try:
            suel=float(suel)
            return True
        except ValueError:
            return False