class Livro:
    def __init__(self,titulo,autor,paginas,proximo=None):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
        self.proximo=proximo
    
    def info(self):
        
        txt=""
        txt+=f"---------------Livro: {self.titulo}---------------\n"
        txt+=f"Autor:{self.autor} || Número de páginas: {self.paginas}"
        if self.proximo!=None:
            txt+="\n\n"
            txt+=self.proximo.info()
        return txt
       


class Pilha:
    def __init__(self,topo=None,tamanho=0):
        self.topo=topo
        self.tamanho=tamanho
        
        
    
    def add(self,livro):
        if self.tamanho<1:
            self.topo=livro
        else:
            livro.proximo=self.topo
            self.topo=livro
            
        self.tamanho+=1
        print(f"Livro {self.topo.titulo} adicionado")
    
    def remover(self):
        print(f"Livro do topo({self.topo.titulo}) removido")
        self.topo=self.topo.proximo
        
    

    def imprimir(self):
        if self.tamanho<1:
            print("Pilha vazia")
        else:
            print(f"Tamanho: {self.tamanho}")
            r=self.topo.info()
            print(r)
           
            
pilha=Pilha()
novoLivro=Livro("Engenharia","Jefferson Engenho",100)

pilha.add(novoLivro)

novoLivro=Livro("Engenharia Volume 2","Jefferson Engenho",110)

pilha.add(novoLivro)

novoLivro=Livro("Guinness","Hugh",256)

pilha.add(novoLivro)

novoLivro=Livro("Cinema e Efeitos","Castro",192)

pilha.add(novoLivro)

escolha=0
loop=True


while loop:
    escolha=int(input("MENU\n1 - Adicionar novo livro à pilha\n2 - Remover livro do topo da pilha\n3 - Ver pilha de livros\n4 - Parar\n"))

    if (escolha==1):
        novoLivro=Livro(input("Nome do livro: "),input("Autor do livro: "),int(input("Número de páginas: ")))
        pilha.add(novoLivro)
    elif (escolha==2):
        pilha.remover()
    elif(escolha==3):
        #print("Escolhido",escolha)
        pilha.imprimir()
    elif(escolha==4):
        print("Encerrado")
        loop=False