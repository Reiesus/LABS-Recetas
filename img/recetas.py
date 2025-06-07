import csv
from typing import NamedTuple,List,Set,Optional,Tuple
from datetime import *

Ingrediente = NamedTuple("Ingrediente",
					[("nombre",str),
					 ("cantidad",float),
					 ("unidad",str)])
						 
Receta = NamedTuple("Receta", 
                    [("denominacion", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", List[Ingrediente]),
                     ("tiempo", int),
                     ("calorias", int),
                     ("fecha", date),
                     ("precio", float)])


def lee_recetas(ruta:str)->List[Receta]:
    res=list()
    with open(ruta, encoding='utf-8') as f:
        lector=csv.reader(f,delimiter=';')
        next(lector)
        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha,precio_estimado in lector:
            res.append(Receta(denominacion,tipo,dificultad,parsea_ingredientes(ingredientes),int(tiempo),
                              int(calorias),datetime.strptime(fecha, "%d/%m/%Y"),float(precio_estimado.replace(',', '.'))))
    return res

def parsea_ingredientes(cadena: str) -> List[Ingrediente]:
    partes = cadena.strip().split(",")
    return [parsea_ingrediente(p.strip()) for p in partes if p.strip()]

def parsea_ingrediente(texto: str) -> Ingrediente:
    nombre, cantidad, unidad = texto.split("-")
    return Ingrediente(nombre.strip(), float(cantidad), unidad.strip())


def ingredientes_en_unidad(recetas:List[Receta],unidad:Optional[str])->int:
    contador=set()
    for r in recetas:
        for i in r.ingredientes:
            if i.unidad==unidad or unidad is None :
                contador.add(i.nombre)      
    return len(contador)

def recetas_con_ingredientes(recetas:List[Receta], ingredientes:Set[str])->List[Tuple]:
    res=list()
    for r in recetas:
        for i in r.ingredientes:
            if i.nombre in ingredientes:
                res.append((r.denominacion,r.calorias,r.precio))
                break
    return res

def receta_mas_barata(recetas: List[Receta], tipos: Set[str], n: Optional[int] = None) -> Receta:
    filtradas = [r for r in recetas if r.tipo in tipos]
    if n is not None:
        filtradas = sorted(filtradas, key=lambda r: r.calorias)[:n]    
    if not filtradas:
        return None 
    return  min(filtradas, key=lambda r: r.precio)


def recetas_baratas_con_menos_calorias(recetas: List[Receta], n: int) -> List[Tuple[str, int]]:
    precio_medio = sum(r.precio for r in recetas) / len(recetas)
    baratas = [r for r in recetas if r.precio <= precio_medio]

    seleccionadas = sorted(baratas, key=lambda r: r.calorias)[:n]
    
    res = [(r.denominacion, r.calorias) for r in seleccionadas]
    
    return res
