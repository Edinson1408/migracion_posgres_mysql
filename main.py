from datetime import datetime
# import lib.mscSemanal as klibS
import lib.mscDiario as klibD
# import os


# proceso = os.environ.get('proceso')
#0 todo
#1 Diario
#2 Semana


print("Inicio "+str(datetime.now()))
print(f"Ejecución proceso:  #1 Diario")
# if proceso=="0":
#     klibS.INSERT_PROGRAMACION_SEMANAL()
klibD.INSERT_PROGRAMACION_DIARIA()
# elif proceso=="1":
#     klibD.INSERT_PROGRAMACION_DIARIA()
# elif proceso=="2":
#     klibS.INSERT_PROGRAMACION_SEMANAL()

print("Fin "+str(datetime.now()))


