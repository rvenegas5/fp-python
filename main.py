from funciones import *

paisesXContinente = obtenerDicPaises()

def crearDiccionario(nombreArchivo,paises):
  resultado = {}
  archivo = open(nombreArchivo, 'r')
  archivo.readline()
  for linea in archivo.readlines():
    vuelo = linea.split(',')
    idPax = vuelo[1]
    pais = vuelo[2]
    continente = ''
    for conti,country in paises.items():
      if pais in country:
        continente = conti
    claveMyDic = (idPax, continente)
    if claveMyDic not in resultado:
      resultado[claveMyDic] = set()
    
    resultado[claveMyDic].add(pais)
  archivo.close()
  return resultado

def reporte(dic,nombreArchivo):
  reporte = open(nombreArchivo, 'w')
  reporte.write('idPax,paisesVisitados\n')
  dicReporte = {}
  for clave,paises in dic.items():
    if clave[0] not in dicReporte:
      dicReporte[clave[0]] = []
    dicReporte[clave[0]] += list(paises)
  for idPax, paises in dicReporte.items():
    if len(paises) > 5:
      cadenaPaises = ','.join(paises)
      reporte.write(idPax + ',' + cadenaPaises + '\n')
  reporte.close()

def menosVisitados(dic, paises, continente):
  paisesNoVisitados = []
  paisesContinente = paises[continente]
  paisesVisitados = []
  for clave, paisesDic in dic.items():
    if clave[1] == continente:
      paisesVisitados += list(paisesDic) 
  unicoPaisesVisitados = set(paisesVisitados)
  for pais in paisesContinente:
    if pais not in list(unicoPaisesVisitados):
      paisesNoVisitados.append(pais)
  return paisesNoVisitados

print('*'*10)
print("PROGRAMA PRINCIPAL")
archivo = 'informacion.txt'
report = 'reporte.txt'
resultado = crearDiccionario(archivo, paisesXContinente)
reporte(resultado, report)
continente = 'EUROPA'
print('Paises no visitados de: ' + continente)
paisesSinvisitar = menosVisitados(resultado, paisesXContinente, continente)
for i in range(len(paisesSinvisitar)):
  print(str(i + 1) + ")" + paisesSinvisitar[i])