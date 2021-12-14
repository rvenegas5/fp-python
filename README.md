En el archivo **informacion.txt** se guarda el historial de los viajes a diferentes países por diferentes personas, además se guarda el número de millas que un cliente ha ganado en ese viaje en específico. 

*Consultar el archivo para ver más detalles sobre los datos.*

Se cuenta además con el diccionario países que contiene todos los continentes con su respectiva lista de países. 

Implemente las siguientes funciones: 

1. **crearDiccionario(nombreArchivo,paises)** recibe el nombre del archivo y un diccionario. La función retorna un diccionario con la siguiente estructura. 

```
dic = { (idPax,continente): {paises visitados} } }
```

Ejemplo: 

```
 dic = {
   ('0136408941','EUROPA'): {'ESLOVENIA', 'BELGICA'..},
   ('0136408941','AFRICA'): {'TANZANIA', 'ZIMBABWE', 'SENEGAL'}, 
   ('0136408941','OCEANIA'): {'TUVALU', 'VANUATU'}, 
   ('0136408941','ASIA'): {'PALESTINA', 'HONG KONG', 'YEMEN'}, 
   ('0136408941','AMERICA'): {'BRASIL', 'CANADA'}},

   ('0615214233','AMERICA'): {'ANTIGUA Y BARBUDA'}, 
   ('0615214233','AFRICA'): {'ETIOPIA', 'COMORES', 'MALAWI', 'BENIN'}, 
   ... 
   }

```


2. **reporte(dic,nombreArchivo)** recibe el diccionario de la función anterior y crea en un reporte con el nombre del archivo recibido que contenga el id y la lista de paises visitados, de todos los pasajeros que han viajado a más de 5 países.

El encabezado del archivo del siguiente. 
 ```
 idPax,paisesVisitados
 ```

 Ejemplo:

 ```
idPax,paises
0615214233,UCRANIA,MALAWI,KAZAJSTAN,...
1326500321,ETIOPIA,KENIA,ECUADOR,...
.
.
.
 ```
*Nota: de ser necesario considere crear otra estructura resumen (lista, diccionario, etc. ) antes de escribir en el archivo.*

3. **menosVisitados(dic, paises, continente) ** recibe ambos diccionarios y un *continente* y retorna la lista de los países de ese continente que no han sido visitados ni una sola vez por los clientes que se encuentran registrados.


4. Escriba un programa principal que llame a las funciones correspondientes, cree el reporte de la función 2, y muestre por pantalla los paises de EUROPA que no han sido visitados. 