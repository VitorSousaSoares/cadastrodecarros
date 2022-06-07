import sqlite3
from sqlite3 import Error
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import END, PhotoImage, Tk, Label, StringVar, Entry, Button, NO, W

root = Tk()
root.title("Cadastro de veiculos")
root.geometry("700x520")

controle=ttk.Notebook(root)
controle.pack(expand=True)

aba1 = ttk.Frame(controle, width=700, height=520)
aba2 = ttk.Frame(controle, width=700, height=520)
aba3 = ttk.Frame(controle, width=700, height=520)

aba1.pack(fill='both', expand=True)
aba2.pack(fill='both', expand=True)
aba3.pack(fill='both', expand=True)

controle.add(aba1, text="INICIAL")
controle.add(aba2, text="CADASTRO")
controle.add(aba3, text="EDIÇAO")



placa = StringVar()
marca = StringVar()
modelo = StringVar()
ano = StringVar()
cor = StringVar()
km = StringVar()
combustivel = StringVar()




def conecxaoBanco():
    banco = 'bancoAV2.db'
    con=None
    try:
        con=sqlite3.connect(banco)
    except Error as ex:
        print(ex)
    return con

variavelConecxao=conecxaoBanco()

vsqlcriartabela="""CREATE TABLE carros (
            placa VARCHAR(7) NOT NULL PRIMARY KEY,
            marca VARCHAR(15),
            modelo VARCHAR(15),
            ano VARCHAR(4),
            cor VARCHAR(10),
            km VARCHAR(5),
            combustivel VARCHAR(10)
        )"""

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
    except Error as ex:
        print(ex)





def cadastrar():
    if dadoplacacadastro.get() == "" or dadomodelocadastro.get() == "" or dadomarcacadastro.get()== "" or dadoanocadastro.get()=="" or dadocorcadastro.get()=="" or dadokmcadastro.get()== "" or liscadastro.get()=="":
        msb.showwarning('', 'Por favor, digite todos os campos.', icon='warning')
    else:
        vplaca=dadoplacacadastro.get()
        vmarca=dadomarcacadastro.get()
        vmodelo=dadomodelocadastro.get()
        vano=dadoanocadastro.get()
        vcor=dadocorcadastro.get()
        vkm=dadokmcadastro.get()
        vcombustivel=liscadastro.get()

        vsqlinserir = "INSERT INTO carros (placa,marca,modelo,ano,cor,km,combustivel) VALUES ('"+vplaca+"','"+vmarca+"','"+vmodelo+"','"+vano+"','"+vcor+"','"+vkm+"','"+vcombustivel+"')"
        
        def inserirDados(conexao,sql):
            
            try:
                c=conexao.cursor()
                c.execute(sql)
                conexao.commit()
                dadoplacacadastro.delete(0,END)
                dadomarcacadastro.delete(0,END)
                dadomodelocadastro.delete(0,END)
                dadoanocadastro.delete(0,END)
                dadocorcadastro.delete(0,END)
                dadokmcadastro.delete(0,END)
                liscadastro.delete(0,END)
                msb.showwarning('', 'Item cadastrado')
            except Error as ex:
                print(ex)
            
            
        inserirDados(variavelConecxao,vsqlinserir)
        

def tudo():

    tree.delete(*tree.get_children())
    conn = sqlite3.connect('bancoAV2.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carros ")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=data)

    cursor.close()
    conn.close()


def listar():
    if dadoplacaedit.get() == "":
        msb.showwarning('', 'Por favor, digite a placa.', icon='warning')

    else:
        vplaca = dadoplacaedit.get()
        vsqlConsulta = "Select * FROM carros WHERE placa='"+vplaca+"'"

        def consultaBanco(conexao,sql):
            try:
                c=conexao.cursor()
                c.execute(sql)
                resultado=c.fetchall()
                return resultado
            except Error as ex:
                print(ex)

            
        res=consultaBanco(variavelConecxao,vsqlConsulta)
        

        for r in res:
            r
        marca.set(r[1])
        modelo.set(r[2])
        ano.set(r[3])
        cor.set(r[4])
        km.set(r[5])
        combustivel.set(r[6])

def alterar():
    if dadoplacaedit.get() == "":
        msb.showwarning('', 'Por favor, digite a placa.', icon='warning')

    else:
        vplaca=dadoplacaedit.get()
        vmarca=dadomarcaedit.get()
        vmodelo=dadomodeloedit.get()
        vano=dadoanoedit.get()
        vcor=dadocoredit.get()
        vkm=dadokmedit.get()
        vcombustivel=lisedit.get()

        vsqlAlualizar="UPDATE carros SET marca='"+vmarca+"',modelo='"+vmodelo+"',ano='"+vano+"', cor='"+vcor+"',km='"+vkm+"',combustivel='"+vcombustivel+"' WHERE placa='"+vplaca+"' "

        def ataualizar(conecxao, sql):
            resultado = msb.askquestion('', 'Tem certeza que deseja alterar o veidulo?')
            if resultado == 'yes':
                try:
                    c=conecxao.cursor()
                    c.execute(sql)
                    conecxao.commit()

                except Error as ex:
                    msb.showwarning('', 'Erro ao auterar o item.', icon='warning')
                finally:
                    dadoplacaedit.delete(0,END)
                    dadomarcaedit.delete(0,END)
                    dadomodeloedit.delete(0,END)
                    dadoanoedit.delete(0,END)
                    dadocoredit.delete(0,END)
                    dadokmedit.delete(0,END)
                    lisedit.delete(0,END)
                    msb.showwarning('', 'Item editado')
        ataualizar(variavelConecxao,vsqlAlualizar)


def apagar():
    if dadoplacaedit.get() == "":
        msb.showwarning('', 'Por favor, digite a placa.', icon='warning')

    else:

        vplaca=dadoplacaedit.get()

        vsqlDeletar ="DELETE FROM carros WHERE placa='"+vplaca+"'"
        def deletarDados(conexao,sql):
            resultado = msb.askquestion('', 'Tem certeza que deseja excluir o veidulo?')
            if resultado == 'yes':
                try:
                    c=conexao.cursor()
                    c.execute(sql)
                    conexao.commit()
                except Error as ex:
                    msb.showwarning('', 'Erro ao apagar o item.', icon='warning')
                finally:
                    dadoplacaedit.delete(0,END)
                    dadomarcaedit.delete(0,END)
                    dadomodeloedit.delete(0,END)
                    dadoanoedit.delete(0,END)
                    dadocoredit.delete(0,END)
                    dadokmedit.delete(0,END)
                    lisedit.delete(0,END)
                    msb.showwarning('', 'Item apagado')
        deletarDados(variavelConecxao,vsqlDeletar)


photo = PhotoImage(file='capa.png')
image_label = ttk.Label(aba1,image=photo,padding=5)
image_label.pack()

legcadastroplaca = Label(aba2, text='placa', font=('arial', 12))
legcadastroplaca.place(x=10, y=10)
legcadastromarca = Label(aba2, text='marca', font=('arial', 12))
legcadastromarca.place(x=10,y=40)
legcadastromodelo = Label(aba2, text='modelo', font=('arial', 12))
legcadastromodelo.place(x=10,y=70)
legcadastroano = Label(aba2, text='ano', font=('arial', 12))
legcadastroano.place(x=10,y=100)
legcadastrocor = Label(aba2, text='cor', font=('arial', 12))
legcadastrocor.place(x=10,y=130)
legcadastrokm = Label(aba2, text='km', font=('arial', 12))
legcadastrokm.place(x=10,y=160)
legcadastrocombustivel = Label(aba2, text='combustivel', font=('arial', 12))
legcadastrocombustivel.place(x=10,y=190)

dadoplacacadastro = Entry(aba2, textvariable=placa,width=93)
dadoplacacadastro.place(x=120,y=10)
dadomarcacadastro = Entry(aba2, textvariable=marca,width=93)
dadomarcacadastro.place(x=120,y=40)
dadomodelocadastro = Entry(aba2, textvariable=modelo,width=93)
dadomodelocadastro.place(x=120,y=70)
dadoanocadastro = Entry(aba2, textvariable=ano,width=93)
dadoanocadastro.place(x=120,y=100)
dadocorcadastro = Entry(aba2, textvariable=cor,width=93)
dadocorcadastro.place(x=120,y=130)
dadokmcadastro = Entry(aba2, textvariable=km,width=93)
dadokmcadastro.place(x=120,y=160)
liscadastro=ttk.Combobox(aba2,textvariable=combustivel, values=('Gasolina','Alcool','Flex','Gas'),width=90)
liscadastro.set("Selecione o combustivel")
liscadastro.place(x=120,y=190)

btncadastro = Button(aba2,text="CADASTRO", width=45, command=cadastrar)
btncadastro.place(x=10,y=220)

btncadastro = Button(aba2,text="MOSTRA ITENS", width=45, command=tudo)
btncadastro.place(x=368,y=220)

tree = ttk.Treeview(aba2, columns=('Placa', 'Marca', 'Modelo', 'Ano', 'Cor', 'KM', 'Combustivel'), show='headings')
tree.heading('Placa', text='Placa', anchor=W)
tree.heading('Marca', text='Marca', anchor=W)
tree.heading('Modelo', text='Modelo', anchor=W)
tree.heading('Ano', text='Ano', anchor=W)
tree.heading('Cor', text='Cor', anchor=W)
tree.heading('KM', text='KM', anchor=W)
tree.heading('Combustivel', text='Combustivel', anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=20)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=80)
tree.place(x=10,y=260)

ScrollbarY = ttk.Scrollbar(aba2, orient='vertical', command=tree.yview)
ScrollbarY.place(x=683,y=260, height=230) 
tree['yscrollcommand']=ScrollbarY.set


legeditplaca = Label(aba3, text='placa', font=('arial', 12))
legeditplaca.place(x=10, y=10)
dadoplacaedit = Entry(aba3, textvariable=placa,width=93)
dadoplacaedit.place(x=120,y=10)

btnpesquisa = Button(aba3,text="PESQUISA", width=95, command=listar)
btnpesquisa.place(x=10,y=40)

legeditmarca = Label(aba3, text='marca', font=('arial', 12))
legeditmarca.place(x=10,y=70)
legeditmodelo = Label(aba3, text='modelo', font=('arial', 12))
legeditmodelo.place(x=10,y=100)
legeditano = Label(aba3, text='ano', font=('arial', 12))
legeditano.place(x=10,y=130)
legeditcor = Label(aba3, text='cor', font=('arial', 12))
legeditcor.place(x=10,y=160)
legeditkm = Label(aba3, text='km', font=('arial', 12))
legeditkm.place(x=10,y=190)
legeditcombustivel = Label(aba3, text='combustivel', font=('arial', 12))
legeditcombustivel.place(x=10,y=220)

dadomarcaedit = Entry(aba3, textvariable=marca,width=93)
dadomarcaedit.place(x=120,y=70)
dadomodeloedit = Entry(aba3, textvariable=modelo,width=93)
dadomodeloedit.place(x=120,y=100)
dadoanoedit = Entry(aba3, textvariable=ano,width=93)
dadoanoedit.place(x=120,y=130)
dadocoredit = Entry(aba3, textvariable=cor,width=93)
dadocoredit.place(x=120,y=160)
dadokmedit = Entry(aba3, textvariable=km,width=93)
dadokmedit.place(x=120,y=190)
lisedit=ttk.Combobox(aba3,textvariable=combustivel, values=('Gasolina','Alcool','Flex','Gas'),width=90)
lisedit.set("Selecione o combustivel")
lisedit.place(x=120,y=220)

btneditar = Button(aba3,text="EDITAR", width=45, command=alterar)
btneditar.place(x=10,y=250)

btneditar = Button(aba3,text="EXCLUIR", width=45, command=apagar)
btneditar.place(x=360,y=250)

# variavelConecxao.close()
criarTabela(variavelConecxao,vsqlcriartabela)
root.mainloop()