import random
import sys


def mostrar_menu():
	print('\nMenu:')
	print('    * (1) Criar Lista')
	print('    * (2) Ler Lista')
	print('    * (3) Soma')
	print('    * (4) Média')
	print('    * (5) Maior')
	print('    * (6) Menor')
	print('    * (7) estaOrdenada por ordem crescente')
	print('    * (8) estaOrdenada por ordem decrescente')
	print('    * (9) Procura um elemento')
	print('    * (0) Sair')


def criar_lista_aleatoria(tamanho=10, minimo=1, maximo=100):
	return [random.randint(minimo, maximo) for _ in range(tamanho)]


def ler_lista_do_utilizador():
	print('Introduza números separados por espaços (ou linha vazia para cancelar):')
	linha = input('> ').strip()
	if linha == '':
		print('Leitura cancelada.')
		return None
	parts = linha.split()
	lista = []
	for p in parts:
		try:
			n = float(p) if ('.' in p) else int(p)
			lista.append(n)
		except ValueError:
			print(f'Ignorado: "{p}" não é um número válido.')
	return lista


def soma_lista(lst):
	return sum(lst)


def media_lista(lst):
	return sum(lst) / len(lst) if lst else None


def maior_lista(lst):
	return max(lst) if lst else None


def menor_lista(lst):
	return min(lst) if lst else None


def esta_ordenada_crescente(lst):
	return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))


def esta_ordenada_decrescente(lst):
	return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))


def procura_elemento(lst, elemento):
	try:
		idx = lst.index(elemento)
		return idx
	except ValueError:
		return -1


def solicitar_int(prompt, minimo=None, maximo=None):
	while True:
		val = input(prompt).strip()
		try:
			n = int(val)
			if minimo is not None and n < minimo:
				print(f'Valor deve ser >= {minimo}.')
				continue
			if maximo is not None and n > maximo:
				print(f'Valor deve ser <= {maximo}.')
				continue
			return n
		except ValueError:
			print('Por favor introduza um inteiro válido.')


def main():
	lista_interna = []
	while True:
		mostrar_menu()
		opc = input('Escolha uma opção: ').strip()

		if opc == '1':
			tamanho = solicitar_int('Tamanho da lista a criar (int positivo, por defeito 10): ')
			if tamanho <= 0:
				print('Tamanho deve ser positivo. A usar 10 por defeito.')
				tamanho = 10
			lista_interna = criar_lista_aleatoria(tamanho)
			print('Lista aleatória criada:')
			print(lista_interna)

		elif opc == '2':
			nova = ler_lista_do_utilizador()
			if nova is not None:
				lista_interna = nova
				print('Lista guardada:')
				print(lista_interna)

		elif opc == '3':
			if not lista_interna:
				print('A lista está vazia. Nada a somar.')
			else:
				print('Soma:', soma_lista(lista_interna))

		elif opc == '4':
			if not lista_interna:
				print('A lista está vazia. Média indisponível.')
			else:
				print('Média:', media_lista(lista_interna))

		elif opc == '5':
			if not lista_interna:
				print('A lista está vazia. Maior indisponível.')
			else:
				print('Maior:', maior_lista(lista_interna))

		elif opc == '6':
			if not lista_interna:
				print('A lista está vazia. Menor indisponível.')
			else:
				print('Menor:', menor_lista(lista_interna))

		elif opc == '7':
			if not lista_interna:
				print('A lista está vazia. Considere que está ordenada: Sim')
			else:
				print('Sim' if esta_ordenada_crescente(lista_interna) else 'Não')

		elif opc == '8':
			if not lista_interna:
				print('A lista está vazia. Considere que está ordenada: Sim')
			else:
				print('Sim' if esta_ordenada_decrescente(lista_interna) else 'Não')

		elif opc == '9':
			if not lista_interna:
				print('A lista está vazia. Nada a procurar.')
			else:
				termo = input('Elemento a procurar (int/float): ').strip()
				try:
					elem = float(termo) if ('.' in termo) else int(termo)
				except ValueError:
					print('Entrada inválida.')
					continue
				pos = procura_elemento(lista_interna, elem)
				print('Posição:' , pos)

		elif opc == '0':
			print('\nA terminar. Lista atual:')
			print(lista_interna)
			print('Até breve!')
			break

		else:
			print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print('\nExecução terminada pelo utilizador.')
		sys.exit(0)

