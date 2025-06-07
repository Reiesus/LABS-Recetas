import datetime
from recetas import *

def test_lee_recetas():
    recetas = lee_recetas("data/recetas.csv")
    print(f"Registros leídos: {len(recetas)}")
    print(f"Los dos primeros: {recetas[:2]}")
    print(f"Los dos últimos: {recetas[-2:]}")

def test_ingredientes_en_unidad():
    recetas = lee_recetas("data/recetas.csv")
    total = ingredientes_en_unidad(recetas, None)
    gr = ingredientes_en_unidad(recetas, "gr")
    cl = ingredientes_en_unidad(recetas, "cl")
    print(f"Hay {total} ingredientes distintos que se miden en None.")
    print(f"Hay {gr} ingredientes distintos que se miden en gr.")
    print(f"Hay {cl} ingredientes distintos que se miden en cl.")

def test_recetas_con_ingredientes():
    recetas = lee_recetas("data/recetas.csv")
    ing1 = {"harina", "azúcar"}
    ing2 = {"pimiento", "tomate", "cebolla"}
    res1 = recetas_con_ingredientes(recetas, ing1)
    res2 = recetas_con_ingredientes(recetas, ing2)
    print(f"Las recetas con alguno de los siguiente ingredientes {ing1} son: {res1}")
    print(f"Las recetas con alguno de los siguiente ingredientes {ing2} son: {res2}")

def test_receta_mas_barata():
    recetas = lee_recetas("data/recetas.csv")
    tipos1 = {"Postre", "Entrante"}
    tipos2 = {"Postre", "Plato principal"}
    mas_barata1 = receta_mas_barata(recetas, tipos1)
    mas_barata2 = receta_mas_barata(recetas, tipos2, n=5)
    print(f"La receta más barata de alguno de los siguientes tipos {tipos1} es:\n {mas_barata1}")
    print(f"La receta más barata de alguno de los siguientes tipos {tipos2} entre las 5 con menos calorías es:\n {mas_barata2}")

def test_recetas_baratas_con_menos_calorias():
    recetas = lee_recetas("data/recetas.csv")
    res3 = recetas_baratas_con_menos_calorias(recetas, 3)
    res5 = recetas_baratas_con_menos_calorias(recetas, 5)
    print(f"Las 3 recetas con menos calorías con precio menor que el promedio son:")
    for r in res3:
        print(f"\t{r}")
    print(f"Las 5 recetas con menos calorías con precio menor que el promedio son:")
    for r in res5:
        print(f"\t{r}")

if __name__ == "__main__":
    print("== Test lee_recetas ==")
    test_lee_recetas()
    print("\n== Test ingredientes_en_unidad ==")
    test_ingredientes_en_unidad()
    print("\n== Test recetas_con_ingredientes ==")
    test_recetas_con_ingredientes()
    print("\n== Test receta_mas_barata ==")
    test_receta_mas_barata()
    print("\n== Test recetas_baratas_con_menos_calorias ==")
    test_recetas_baratas_con_menos_calorias()
