import ldde

lista = ldde.Ldde()


lista.inserirInicio('4')
lista.inserirInicio('3')
lista.inserirInicio('2')


print("#####################################")
print("############### L D D E #############")

lista.imprimir()

print("#####################################")
print("Imprimindo lista reversa: ")
lista.imprimirReverso()

print("#####################################")
print("Inserindo o 1 no inicio: ")
lista.inserirInicio('1')
lista.imprimir()

print("#####################################")
print("Inserindo o 5 no final: ")
lista.inserirFim('5')
lista.imprimir()

print("#####################################")
print("Removendo o inicio: ")
lista.removerInicio()
lista.imprimir()

print("#####################################")
print("Removendo o Fim: ")
lista.removerFim()
lista.imprimir()
