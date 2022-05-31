# validar semestres.


pensum = [
{'0123': {'nombre': 'intro a la ing', 'créditos': 2},
'4567': {'nombre': 'inglés', 'créditos': 1}},
{}, {}
]

def modificar_materia(pensum, semestre, materia, nombre, creditos): 
    all_semester=len(pensum)
    if semestre > 0 and semestre < all_semester:
        dic_semestre =pensum[semestre - 1]
        materia_valida = validar_materias(materia,dic_semestre)
        if materia_valida[1] == 0:
            mensaje = "El semestre no tiene materias"
        else:
            if materia_valida[0] == False:
                mensaje = "La materia no existe"
            else:
                for materia_ref in dic_semestre[materia]:
                    if materia_ref == "nombre":
                        dic_semestre[materia][materia_ref] = nombre
                    else:
                        dic_semestre[materia][materia_ref] = creditos
                    mensaje = "Guardado exitoso"
                          

    else:
        mensaje = "Ingrese semestre valido"
    print(mensaje) 
    

def validar_materias(materia,semestre):
        list = [key for key in semestre ]
        if semestre == {}:
            return False,0
        else:    
            for i in list:
                if materia == i:
                    
                    return True,materia
                    break
                else:
                    return False,materia
                    break
                    
modificar_materia(pensum, 1,"0123", "Juan", 2)
print(pensum)


 