from cargo import Cargo
from departamento import Departamento
class Empleado:
    secuencia=1
    empleados= [{"codigo":1,"nombre":"Dan","cedula":"0914192182","cargo":Cargo.cargos[0]["cargo"],"departamento":Departamento.departamentos[0]["departamento"],"sueldo":500.50},]
    
    def __init__(self,nombre,cedula,codCargo,codDepartamento,sueldo):
        Empleado.secuencia+=1
        self.codigo = Empleado.secuencia
        self.nombre = nombre
        self.cedula= cedula
        self.cargo = codCargo
        self.departamento = codDepartamento
        self.sueldo = sueldo

    def  registro(self):
        return {"codigo":self.codigo,"nombre":self.nombre,"cedula":self.cedula,"cargo":self.cargo,"departamento":self.departamento,"sueldo":self.sueldo}
