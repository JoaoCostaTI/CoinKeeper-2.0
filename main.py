from tkinter import *
from tkinter import Tk, ttk

# Cores
co1 = '#2e2d2b'  # Preta (Ideal para Fundo da Janela)
co2 = '#feffff'  # Branca (Ideal para Texto ou Fundo dos Inputs)
co3 = '#4fa882'  # Verde (Verde água/Suave para detalhes)
co4 = '#38576b'  # Valor (Azul petróleo - bom para textos descritivos)
co5 = '#403d3d'  # Letra (Cinza escuro - para leitura em fundo claro)
co6 = '#e11138'  # - profit (Vermelho para Despesas/Prejuízo)
co7 = '#038cfc'  # Azul (Azul "Link" ou Botão Principal)
co8 = '#2cd43a'  # Verde Neon (Destaque forte)
co9 = '#3b9110'  # + verde (Verde Sólido para Receitas/Lucro)
co10 = '#78c2ad' # + verde (Verde pastel para fundos suaves)

#colors
colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']


#Criando janela Vazia
janela = Tk()
janela.title()
janela.geometry('900x650')
janela.configure(background=co2)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use('clam')

# Criando frames para divisão da tela
frame_cima = Frame(janela, width=1043, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0)

frame_meio = Frame(janela, width=1043, height=361, bg=co1,pady=20, relief='raised')
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=1043, height=300, bg=co1, relief='flat')
frame_baixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)



janela.mainloop()

