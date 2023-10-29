D_curso=1.5
D_curso_lento=7
D_curso_promedio=4
D_curso_otros=2.5
Cc=3.5
ccpromedio=5
#diferencia porcentual con respecto al curso actual
dif_otros=(D_curso_otros-D_curso)/D_curso
dif_lento=(D_curso_lento-D_curso)/D_curso
dif_promedio=(D_curso_promedio-D_curso)/D_curso
print("diferencia otros al curso :",dif_otros)
print("diferencia maxima al curso :",dif_lento)
print("diferencia promedio al curso :",dif_promedio)
#%material inservible
Mat_inserv_C=(Cc-D_curso)/D_curso
mat_inserv_promedio=(ccpromedio-D_curso_promedio)/D_curso_promedio
print("material inserv curso :",Mat_inserv_C)
print("material inserv promedio :",mat_inserv_promedio)
#10 horas de este curso
proy_curso=10*D_curso
proy_max=10*D_curso_lento
proy_prom=10*D_curso_promedio
print("proyeccion del curso :",proy_curso)
print("proyeccion maxima del curso :",proy_max)
print("proyeccion promedio del curso :",proy_prom)