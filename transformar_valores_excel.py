from os.path import isfile
from os import getcwd
from openpyxl import Workbook

def main():

    #Pedimos el nombre el archivo
    nombre_archivo = input("Ingrese el nombre del archivo con terminación .txt: ")
    #Revisamos que el txt existe
    if isfile(r"{}/{}".format(getcwd(), nombre_archivo)):
        archivo = open(r"{}/{}".format(getcwd(), nombre_archivo), "r")

        #Creamos el libro de excel
        libro = Workbook()
        hoja = libro["Sheet"]

        contador_fila = 1
        #Recorremos el archivo
        for linea in archivo:
            valor = ""
            #COntador que se encarga de llevar la columna actual
            contador_columna = 1

            for caracter in linea:
                if caracter == " " or caracter == "\n":
                    
                    #Ubicamos en la fila y columna el valor
                    hoja.cell(row=contador_fila, column=contador_columna, value=valor)
                    valor = ""
                    contador_columna += 1
                else:
                    valor += caracter
            
            contador_fila += 1

        #Guardamos los archivos en datos.xlsx
        libro.save(filename = "datos.xlsx")

        print("Convertido correctamente")
        archivo.close()

    else:
        print("Error, no se encontro el archivo")

main()