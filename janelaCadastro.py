import pandas as pd
import openpyxl as xlsx
from tkinter import messagebox, ttk
import datetime as dt
import tkinter as tk
from maskedentry import MaskedWidget, Calendar
from dateutil import parser


# --------------------------------------VALIDA DATA-----------------------------------------------------------
def validaData(entry_nascimento):
    format = "%d-%m-%y"
    res = True
    try:
        res = bool(parser.parse(entry_nascimento))
    except ValueError:
        res = False


# --------------------------------------JANELA CADASTRO-----------------------------------------------------------
def abrir_cadastro(lista_tipos, salvarContato, book):
    janelaCadastro = tk.Toplevel()
    janelaCadastro.grab_set()
    janelaCadastro.title('Cadastrar Doador')
    altura = 660
    largura = 350
    largura_tela = janelaCadastro.winfo_screenwidth()
    altura_tela = janelaCadastro.winfo_screenheight()
    posx = largura_tela / 2 - largura / 2
    posy = altura_tela / 2 - altura / 2
    janelaCadastro.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
    funcCheck = janelaCadastro.register(validaData)
    label_nome = tk.Label(janelaCadastro, text="Nome do doador")
    label_nome.grid(row=1, column=0, padx=10, pady=10,
                    sticky='nswe', columnspan=4)

    entry_nome = tk.Entry(janelaCadastro)
    entry_nome.grid(row=2, column=0, padx=10, pady=10,
                    sticky='nswe', columnspan=4)

    label_cpf = tk.Label(janelaCadastro, text="CPF do doador")
    label_cpf.grid(row=3, column=0, padx=10, pady=10,
                   sticky='nswe', columnspan=4)

    entry_cpf = MaskedWidget(janelaCadastro, 'fixed', mask='999.999.999-99')
    entry_cpf.grid(row=4, column=0, padx=10, pady=10,
                   sticky='nswe', columnspan=4)

    label_nascimento = tk.Label(
        janelaCadastro, text="Data de nascimento do doador")
    label_nascimento.grid(row=5, column=0, padx=10,
                          pady=10, sticky='nswe', columnspan=4)

    entry_nascimento = MaskedWidget(janelaCadastro, 'fixed', mask='99/99')
    entry_nascimento.grid(row=6, column=0, padx=10,
                          pady=10, sticky='nswe', columnspan=4)

    label_numero = tk.Label(janelaCadastro, text="Número do doador")
    label_numero.grid(row=7, column=0, padx=10, pady=10,
                      sticky='nswe', columnspan=4)

    entry_numero = MaskedWidget(janelaCadastro, 'fixed', mask='+5599999999999')
    entry_numero.grid(row=8, column=0, padx=10, pady=10,
                      sticky='nswe', columnspan=4)

    label_valor = tk.Label(janelaCadastro, text="Valor a ser doado")
    label_valor.grid(row=9, column=0, padx=10, pady=10,
                     sticky='nswe', columnspan=4)

    entry_valor = MaskedWidget(
        janelaCadastro, 'numeric', dec_sep=",", tho_sep='.', symbol="R$")
    entry_valor.grid(row=10, column=0, padx=10, pady=10,
                     sticky='nswe', columnspan=4)

    label_tipoPagamento = tk.Label(janelaCadastro, text="Tipo de pagamento")
    label_tipoPagamento.grid(row=11, column=0, padx=10,
                             pady=10, sticky='nswe', columnspan=2)

    combobox_selecionarTipo = ttk.Combobox(janelaCadastro, values=lista_tipos)
    combobox_selecionarTipo.grid(
        row=11, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_diaPagamento = tk.Label(janelaCadastro, text="Dia do pagamento")
    label_diaPagamento.grid(row=12, column=0, padx=10,
                            pady=10, sticky='nswe', columnspan=4)

    entry_diaPagamento = MaskedWidget(
        janelaCadastro, 'fixed', mask='99/99/9999')
    entry_diaPagamento.grid(row=13, column=0, padx=10,
                            pady=10, sticky='nswe', columnspan=4)

    label_Pago = tk.Label(janelaCadastro, text="Pago ? S/N")
    label_Pago.grid(row=14, column=0, padx=10, pady=10,
                    sticky='nswe', columnspan=4)

    entry_Pago = tk.Entry(janelaCadastro)
    entry_Pago.grid(row=15, column=0, padx=10, pady=10,
                    sticky='nswe', columnspan=4)

    botao_cadastrarDoador = tk.Button(janelaCadastro, text="Salvar",
                                      command=lambda: salvarContato(book, entry_nome, entry_cpf, entry_nascimento,
                                                                    entry_numero, entry_valor, combobox_selecionarTipo,
                                                                    entry_diaPagamento, entry_Pago))
    botao_cadastrarDoador.grid(
        row=16, column=1, padx=10, pady=10, sticky='nswe', columnspan=4)

    botaoVoltar = tk.Button(
        janelaCadastro, text='Voltar ao Menu de Opções', command=janelaCadastro.destroy)
    botaoVoltar.grid(row=16, column=0, padx=10, pady=5)


# --------------------------------------JANELA ANIVERSARIANTE-----------------------------------------------------------
def janela_Aniversariantes(verificarAniversario, enviarMensagemAniversario):
    janelaAniversariante = tk.Toplevel()
    janelaAniversariante.grab_set()
    janelaAniversariante.title('Aniversariantes')
    aniversariantes = verificarAniversario()
    aniversariantes = '\n'.join(aniversariantes)
    label_Aniversariantes = tk.Label(
        janelaAniversariante, text=f"{aniversariantes}")
    label_Aniversariantes.grid(
        row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
    botaoEnviarParabens = tk.Button(janelaAniversariante, text="Enviar mensagem aos aniversariantes",
                                    command=enviarMensagemAniversario)
    botaoEnviarParabens.grid(row=2, column=0, padx=10,
                             pady=5, sticky='nswe', columnspan=4)


# --------------------------------------JANELA VENCIMENTO-----------------------------------------------------------
def janela_Vencimentos(vencimento3Dias, enviarMensagemVencidos):
    janelaVencimento = tk.Toplevel()
    janelaVencimento.grab_set()
    janelaVencimento.title('Pagamentos Vencidos')
    vencidos = vencimento3Dias()
    vencidos = '\n'.join(vencidos)
    label_Vencimentos = tk.Label(janelaVencimento, text=f"{vencidos}")
    label_Vencimentos.grid(row=0, column=0, padx=10,
                           pady=10, sticky='nswe', columnspan=4)
    botaoEnviarCobranca = tk.Button(janelaVencimento, text="Enviar mensagem aos que passaram a validade",
                                    command=enviarMensagemVencidos)
    botaoEnviarCobranca.grid(row=3, column=0, padx=10,
                             pady=5, sticky='nswe', columnspan=4)


# --------------------------------------JANELA VENCIMENTO 7 DIAS-----------------------------------------------------------
def janela_Vencimentos7Dias(vencimentos7Dias, enviarMensagemVencidos7Dias):
    janela3Dias = tk.Toplevel()
    janela3Dias.grab_set()
    janela3Dias.title('Pagamentos Vencidos')
    vencidos = vencimentos7Dias()
    vencidos = '\n'.join(vencidos)
    label_Vencimentos = tk.Label(janela3Dias, text=f"{vencidos}")
    label_Vencimentos.grid(row=0, column=0, padx=10,
                           pady=10, sticky='nswe', columnspan=4)
    botaoEnviarCobranca = tk.Button(janela3Dias, text="Enviar mensagem aos que passaram a validade",
                                    command=enviarMensagemVencidos7Dias)
    botaoEnviarCobranca.grid(row=3, column=0, padx=10,
                             pady=5, sticky='nswe', columnspan=4)
