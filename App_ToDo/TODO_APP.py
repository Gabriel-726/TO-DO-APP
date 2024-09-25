import tkinter as tk
from tkinter import ttk, font, messagebox, PhotoImage
#Importanto o tkinter e algumas funções específicas.

#Criando janela principal atribuida á variável "Janela_principal"
janela_principal = tk.Tk()

#Título da janela(nome)
janela_principal.title("APP DE TAREFAS")

#Definindo geometria da tela(Tamanho)
janela_principal.geometry("500x600")

#Desativando o resize do app
janela_principal.resizable(False, False)

#Criando frame para edição
frame_edicao = None


#Declarando função adicionar tarefas
def AdicionarTarefa():
    global frame_edicao

    tarefa = entry_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_edicao = None
        else:
            adicionar_item(tarefa)
            entry_tarefa.delete(0, tk.END)
    else: 
        messagebox.showwarning("Entrada Invalida", "Insira uma tarefa")


#Função adicionar item

def adicionar_item(tarefa):
    frame_lista_tarefas = tk.Frame(forma_interior, bg="white", bd=1, relief=tk.SOLID)

    lbl_tarefa = tk.Label(frame_lista_tarefas, text=tarefa, font=Fonte_tarefa, bg = "white", width=25, height=2, anchor="w")

    lbl_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady = 5)


    #Botão de edição
    btn_editar = tk.Button(frame_lista_tarefas, image=icon_editar, command=lambda f=frame_lista_tarefas, l=lbl_tarefa: preparar_edit(f,l), bg ="white", relief= tk.FLAT)

    btn_editar.pack(side = tk.RIGHT, padx = 5)

    #botão de excluir
    btn_excluir = tk.Button(frame_lista_tarefas, image=icon_excluir, command=lambda f=frame_lista_tarefas: delete_task(f), bg ="white", relief= tk.FLAT)

    btn_excluir.pack(side = tk.RIGHT, padx = 5)
    
    #Posicionando o frame tarefa
    frame_lista_tarefas.pack(fill=tk.X, padx = 5, pady = 5)

    #criando botão para checar tarefa (concluir)
    btn_check= ttk.Checkbutton(frame_lista_tarefas, command = lambda label = lbl_tarefa: tarefa_concluida(label))

    btn_check.pack(side = tk.RIGHT, padx=5)

    forma_interior.update_idletasks()
    forma.config(scrollregion=forma.bbox("all"))
    
#Função editar tarefa
def preparar_edit(frame_lista_tarefas, lbl_tarefa):
    global frame_edicao 
    frame_edicao = frame_lista_tarefas
    entry_tarefa.delete(0, tk.END)
    entry_tarefa.insert(0, lbl_tarefa.cget("text"))

#Função para aplicar a atualização feita na edição
def atualizar_tarefa(nova_tarefa):
    global frame_edicao
    for widget in frame_edicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.configure(text=nova_tarefa)
    entry_tarefa.delete(0, tk.END)
#Problema: caso o usuário aperte o botão de editar tarefa, e não a atualizar e apaga-la. O programa para de funcionar.

#Função Delete tarefa
def delete_task(frame_lista_tarefas):
    global frame_edicao
    #Verifica se a tarefa que está sendo deletada é a mesma que esta sendo editada
    if frame_lista_tarefas == frame_edicao:
        frame_edicao = None #"Apaga" a instância do frame edição
        entry_tarefa.delete(0, tk.END) #Apaga o texto que estava sendo editado
    frame_lista_tarefas.destroy()
    forma_interior.update_idletasks()
    forma.config(scrollregion=forma.bbox("all"))

#Função para concluir tarefa
def tarefa_concluida(label):
    # Cria uma nova instância de fonte baseada na fonte atual do label
    # A cada execução desta função uma "nova fonte" única desta tarefa é criada pelo código abaixo
    fonte_atual = font.Font(font=label.cget("font"))  

    if fonte_atual.cget("overstrike") == 0:
        fonte_atual.config(overstrike=1) #Ativa
    else:
        fonte_atual.config(overstrike=0)  # Desativa

    # Aplica a nova fonte ao label
    label.config(font=fonte_atual)

#definindo os icones do aplicativo
icon_editar = PhotoImage(file="App_ToDo\icon_editar.png").subsample(2,2)
icon_excluir = PhotoImage(file="App_ToDo\icon_excluir.png").subsample(2,2)

#Definindo cor de fundo da janela
janela_principal.config(bg="#fffdd0")

#Variavel que define a fonte do texto utilizado no "cabeçalho" do app
Fonte_cabecalho = font.Font(family = "Garamond", size=24, weight="bold")

#Criando fonte para tarefa
Fonte_tarefa = font.Font(family="Segoe UI", size= 18)

#Criando label(bg = background color, fg=Cor da letra, pack = posicionamento da label na janela, pady = posição altura, padx = "posicao esquerda para direita"(em pixels))
lbl_cabecalho = tk.Label(janela_principal, text="TAREFAS", font=Fonte_cabecalho, bg="#fffdd0", fg="#333").pack(pady=20, padx=0)

#Area das tarefas
#------------------------

#criando um frame
frame_janela_principal= tk.Frame(janela_principal,bg="#fffdd0")
frame_janela_principal.pack(pady=10)

#criando um campo dentro do frame
entry_tarefa = tk.Entry(frame_janela_principal, font=("Garamond", 15), relief = tk.FLAT, bg="white",fg ="black", width=30)      

#posicionando a entry no frame
entry_tarefa.pack(side=tk.LEFT, padx= 10)

#criando botão
btn_add_tarefa = tk.Button(frame_janela_principal, command=AdicionarTarefa, text="Adicionar Tarefa", relief=tk.FLAT, bg = "#4CAF50", fg="white", height=1, width= 15, font=("Roboto", 11)) 

#posicionando o botão no frame
btn_add_tarefa.pack(side=tk.LEFT, padx=10)

#Criando frame para lista de tarefas com rolagem.
frame_lista_tarefas = tk.Frame(janela_principal, bg ="#fafcd4")
frame_lista_tarefas.pack(fill = tk.BOTH, expand=True, padx = 10, pady = 10)

#criando canvas para formas pesonalizadas
forma = tk.Canvas(frame_lista_tarefas, bg ="white")

#posicionando canvas
forma.pack(side = tk.LEFT, fill=tk.BOTH, expand= True)

#criando scrollbar
scrollbar = ttk.Scrollbar(frame_lista_tarefas, orient="vertical", command=forma.yview)

#posicionando scrollbar
scrollbar.pack(side=tk.RIGHT, fill = tk.Y)

#definindo canvas(colocando scrollbar)
forma.configure(yscrollcommand=scrollbar.set)

#definindo forma do canvas
forma_interior = tk.Frame(forma, bg="white")
forma.create_window((0, 0), window=forma_interior, anchor="nw")
forma_interior.bind("<Configure>", lambda e: forma.configure(scrollregion=forma.bbox("all")))

#------------------------
#Criando o main loop da janela
janela_principal.mainloop()

#Criar um BD para este aplicativo