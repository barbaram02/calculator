# Importando a biblioteca tkinter
from tkinter import *
from tkinter import ttk 

# Cores do programa:
Preto = "#090412"
Roxo = "#591ac7"
Cinza = "#757378" 
Branca = "#f3f2f5"
lilas = "#d8c2ff"
cinza_escuro = "#7d7c80"
lilas_claro = "#ddc9f0"

# Janela é a parte de fundo da calculadora, como se fosse a base da calculadora. Frame_(tela) é a tela da calculadora e Frame_corpo é onde fica os botões da calculadora.
#O nome da interface para a calculadora será janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("410x448") #Aqui está sendo definido a largura e comprimento da janela/interface da calculadora
janela.config(bg=Cinza) #colocando cor na parte de fundo dos botões



#Aqui está sendo feita a divisória do visor (onde fica o número/resultado da operação) e da
# parte dos teclados/digitos.

# Frame é uma extensão em HTML que permite a divisão da janela na intwerface
frame_tela = Frame(janela, width=410, height=100, bg=lilas)
frame_tela.grid(row=0, column=0)


#Onde fica os botões
frame_corpo = Frame(janela, width=410, height=430)
frame_corpo.grid(row=1, column=0)

# Variavel todos os valores

todos_valores = ''

#Criando label (É A LETRA QUE FICA DENTRO DA TELINHA COM OS NÚMEROS DA EQUAÇÃO)
valor_texto = StringVar()


#Função para jogar todos os valores que forem clicados na tela
    #eval() é usada para avaliar uma expressão matemática ou um código Python contido em uma string. 
    
def entrar_valores(event):
    
    global todos_valores
    
    todos_valores = todos_valores + str(event) #Ao clicar mais de uma vez, irá ser adcionada no visor
    
    
    # passando o valor para a tela
    valor_texto.set(todos_valores)

# Função para calcular
def calculo():
    global todos_valores
    resultado = eval(todos_valores)
    print (resultado)
    
    valor_texto.set(str(resultado)) #Fazendo o resultado aparecer no visor
    
# Função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""  # Esses são os valores dos digitos do botão
    valor_texto.set("") # Valores que estão aparecendo no visor.






#Criando label (É A LETRA QUE FICA DENTRO DA TELINHA COM OS NÚMEROS DA EQUAÇÃO)
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=20, height=3, padx= 8, relief=FLAT, anchor="e", justify= RIGHT, font=('Cambria 28'), bg=lilas)
app_label.place(x=0, y=0) # O método .place() permite posicionar esses widgets/letras em uma janela ou em outro widget, especificando as coordenadas (x, y) onde o widget será colocado.

#textvariable() serve para caso a variavel que está recebendo o valor da equação for alterado, através desse método irá ser alterado na parte gráfica também.





#Criando os botões: b = botões
b1 = Button(frame_corpo, command = limpar_tela, text="C", width=22, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE) #bold é para colocr letra em negrito
b1.place(x=0, y=0) # X e Y é a localização do botão na tela. X é a horizontal e Y é a parte vertical.
b2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE) # overrelief é um efeito de relevo colocado no botão e é acionado ao passar o mouse.
b2.place(x=200, y=0)
b3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="/", width=12, height=3, bg=Roxo, font=('Cambria 12 bold'),overrelief=RIDGE)
b3.place(x=300, y=0)

#Botões da linha de baixo
b4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b4.place(x=0, y=66)
b5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b5.place(x= 100, y=66)
b6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b6.place(x=200, y=66)
b7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text="*", width=12, height=3, bg=Roxo, font=('Cambria 12 bold'),overrelief=RIDGE)
b7.place(x=300, y=66)

#Botões da linha de baixo
b8 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b8.place(x=0, y=136)
b9 = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b9.place(x= 100, y=136)
b10 = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b10.place(x=200, y=136)
b11 = Button(frame_corpo, command = lambda: entrar_valores('-'), text="-", width=12, height=3, bg=Roxo, font=('Cambria 12 bold'),overrelief=RIDGE)
b11.place(x=300, y=136)

#Botões da linha de baixo
b12 = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b12.place(x=0, y=206)
b13 = Button(frame_corpo, command = lambda: entrar_valores('2'), text="2", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b13.place(x= 100, y=206)
b14 = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b14.place(x=200, y=206)
b15 = Button(frame_corpo, command = lambda: entrar_valores('+'), text="+", width=12, height=3, bg=Roxo, font=('Cambria 12 bold'),overrelief=RIDGE)
b15.place(x=300, y=206)

#Botões da linha de baixo
b16 = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=22, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b16.place(x=0, y=276) # X e Y é a localização do botão na tela. X é a horizontal e Y é a parte vertical.
b17 = Button(frame_corpo, command = lambda: entrar_valores('.'), text=".", width=11, height=3, bg=cinza_escuro, font=('Cambria 12 bold'),overrelief=RIDGE)
b17.place(x=200, y=276)
b18 = Button(frame_corpo, command = calculo, text="=", width=12, height=3, bg=Roxo, font=('Cambria 12 bold'),overrelief=RIDGE)
b18.place(x=300, y=276)

#Serve para mostrar a interface janela no monitor 
janela.mainloop()

