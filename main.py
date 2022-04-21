# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import graphviz
import graphviz as gv
import re
from tkinter import *

# Design
# this is a function to get the user input from the text input box
from graphviz import Digraph

# NUM and ID

IDENTIFIER = re.compile(r"^[a-zA-z]+\Z")
NUM = re.compile(r"^[\d]+$\Z")

# OP

EQUAL = re.compile(r"^[=]{1}$\Z")
LESS_THAN = re.compile(r"^[<]{1}$\Z")
GREATER_THAN = re.compile(r"^[>]{1}$\Z")
GREATER_THAN_OR_EQUAL = re.compile(r"^>=$\Z")
LESS_THAN_OR_EQUAL = re.compile(r"^<=$\Z")
OR = re.compile(r"(\|\|){2}\Z")
AND = re.compile(r"(&&){2}\Z")
NOT = re.compile(r"[!]{1}\Z")
OPEN_BRACKET = re.compile(r"[\(]{1}\Z")
CLOSE_BRACKET = re.compile(r"[\)]{1}\Z")


def submit():
    userInput = string.get()
    string.set("")
    Tokens_btnClickFunction(userInput)


# click List of Tokens
def Tokens_btnClickFunction(userInput):
    print('List of Tokens clicked')
    token_window = Tk()
    token_window.geometry("500x300")
    token_window.title('Tokeniser')

    strings = userInput.split()
    token = []  # initialise token list
    for string in strings:
        if re.fullmatch(IDENTIFIER, string):
            print('IDENTIFIER', ',', string)
            token.append(['IDENTIFIER', string])
        elif re.fullmatch(NUM, string):
            print('NUM', ',', string)
            token.append(['NUM', string])
        elif re.fullmatch(EQUAL, string):
            print('EQUAL', ',', string)
            token.append(['EQUAL', string])
        elif re.fullmatch(LESS_THAN, string):
            print('LESS_THAN', ',', string)
            token.append(['LESS_THAN', string])
        elif re.fullmatch(GREATER_THAN, string):
            print('GREATER_THAN', ',', string)
            token.append(['GREATER_THAN', string])
        elif re.fullmatch(GREATER_THAN_OR_EQUAL, string):
            print('GREATER_THAN_OR_EQUAL', ',', string)
            token.append(['GREATER_THAN_OR_EQUAL', string])
        elif re.fullmatch(LESS_THAN_OR_EQUAL, string):
            print('LESS_THAN_OR_EQUAL', ',', string)
            token.append(['LESS_THAN_OR_EQUAL', string])
        elif re.fullmatch(OR, string):
            print('OR', ',', string)
            token.append(['OR', string])
        elif re.fullmatch(AND, string):
            print('AND', ',', string)
            token.append(['AND', string])
        elif re.fullmatch(NOT, string):
            print('NOT', ',', string)
            token.append(['NOT', string])
        elif re.fullmatch(OPEN_BRACKET, string):
            print('OPEN_BRACKET', ',', string)
            token.append(['OPEN_BRACKET', string])
        elif re.fullmatch(CLOSE_BRACKET, string):
            print('CLOSE_BRACKET', ',', string)
            token.append(['CLOSE_BRACKET', string])
        else:
            print('INVALID_TOKEN', ',', string)
            token.append(['INVALID_TOKEN', string])
    for i in range(len(token)):
        exec('Label%d=Label(token_window,text="%s")\nLabel%d.pack()' % (i, token[i], i))


# click Operations DFA
def DFA_OP_btnClickFunction():
    print('Operations DFA clicked')
    f = graphviz.Digraph('DFA', filename='fsm.gv')
    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='doublecircle')
    f.node('Done')

    f.attr('node', shape='circle')
    f.node('Start')
    f.node('open_bracket')
    f.node('close_bracket')
    f.node('NUM')
    f.node('ID')
    f.node('equal')
    f.node('less_than')
    f.node('greater_than')
    f.node('less_than_or_equal')
    f.node('greater_than_or_equal')
    f.node('OR')
    f.node('AND')
    f.node('NOT')
    f.node('Invalid_token')
    f.edge('Start', 'Start', label='whitespace')
    f.edge('Start', 'open_bracket', label='(')
    f.edge('open_bracket', 'Done', label='[other]')
    f.edge('Start', 'close_bracket', label=')')
    f.edge('close_bracket', 'Done', label='[other]')
    f.edge('Start', 'NUM', label='digit')
    f.edge('NUM', 'NUM', label='digit')
    f.edge('NUM', 'Done', label='[other]')
    f.edge('Start', 'ID', label='letter')
    f.edge('ID', 'ID', label='letter')
    f.edge('ID', 'Done', label='[other]')
    f.edge('Start', 'equal', label='=')
    f.edge('equal', 'Done', label='[other]')
    f.edge('Start', 'less_than', label='<')
    f.edge('less_than', 'Done', label='[other]')
    f.edge('Start', 'greater_than', label='>')
    f.edge('greater_than', 'Done', label='[other]')
    f.edge('less_than', 'less_than_or_equal', label='=')
    f.edge('less_than_or_equal', 'Done', label='[other]')
    f.edge('greater_than', 'greater_than_or_equal', label='=')
    f.edge('greater_than_or_equal', 'Done', label='[other]')
    f.edge('Start', 'OR', label='|')
    f.edge('OR', 'Done', label='|')
    f.edge('OR', 'Invalid_token', label='[other]')
    f.edge('Start', 'AND', label='&')
    f.edge('AND', 'Done', label='&')
    f.edge('AND', 'Invalid_token', label='[other]')
    f.edge('Start', 'NOT', label='!')
    f.edge('NOT', 'Invalid_token', label='[other]')
    f.edge('Start', 'Invalid_token', label='else')
    f.edge('Invalid_token', 'Done')

    f.view()
    '''operations_window=Tk()
    operations_window.geometry("700x350")
    operations_window.title('Logical Operators DFA')
    f: Digraph = graphviz.Digraph('DFA', filename='fsm.gv')
    f.view()'''


# click Accepting String DFA
def DFA_STRING_btnClickFunction():
    print('Accepting String DFA clicked')

    DFA = gv.Digraph('DFA2', filename='fsm2.gv')
    DFA.node('START', 'START')
    DFA.node('ID1', 'ID1')
    DFA.node('NUM1', 'NUM1')
    DFA.node('NOT1', 'NOT1')
    DFA.node('=', '=')
    DFA.node('>', '>')
    DFA.node('<', '<')
    DFA.node('>=', '>=')
    DFA.node('<=', '<=')
    DFA.node('ID2', 'ID2', shape='doublecircle')
    DFA.node('NUM2', 'NUM2', shape='doublecircle')
    DFA.node('AND1', 'AND1')
    DFA.node('OR1', 'OR1')
    DFA.node('AND2', 'AND2')
    DFA.node('OR2', 'OR2')
    DFA.node('NOT2', 'NOT2')
    DFA.node('ANDE1', 'ANDE1')
    DFA.node('ANDE2', 'ANDE2')
    DFA.node('ORE1', 'ORE1')
    DFA.node('ORE2', 'ORE2')
    DFA.node('Invalid_token', 'Invalid_token')
    #############################################
    DFA.edge('START', 'ID1', label=' letter ')
    DFA.edge('START', 'NUM1', label=' digit ')
    DFA.edge('START', 'START', label=' white space ')
    DFA.edge('START', 'NOT1', label=' ! ')
    ##############################################
    DFA.edge('NOT1', 'ID1', label=' letter ')
    DFA.edge('NOT1', 'NUM1', label=' digit ')
    ##########################################
    DFA.edge('ID1', '=', label=' = ')
    DFA.edge('ID1', '>', label=' > ')
    DFA.edge('ID1', '<', label=' < ')
    DFA.edge('ID1', 'ID1', label=' letter ')
    DFA.edge('ID1', 'AND1', label='&')
    DFA.edge('ID1', 'OR1', label=' | ')
    #####################################
    DFA.edge('NUM1', '=', label=' = ')
    DFA.edge('NUM1', '>', label=' > ')
    DFA.edge('NUM1', '<', label=' < ')
    DFA.edge('NUM1', 'NUM1', label=' digit ')
    DFA.edge('NUM1', 'AND1', label=' & ')
    DFA.edge('NUM1', 'OR1', label=' | ')
    #####################################
    DFA.edge('AND1', 'AND2', label=' & ')
    DFA.edge('OR1', 'OR2', label=' | ')
    #########################################
    DFA.edge('>', '>=', label=' = ')
    DFA.edge('<', '<=', label=' = ')
    ####################################
    DFA.edge('=', 'ID2', label=' letter ')
    DFA.edge('>', 'ID2', label=' letter ')
    DFA.edge('<', 'ID2', label=' letter ')
    DFA.edge('>=', 'ID2', label=' letter ')
    DFA.edge('<=', 'ID2', label=' letter ')
    DFA.edge('AND2', 'ID2', label=' letter ')
    DFA.edge('OR2', 'ID2', label=' letter ')
    DFA.edge('ID2', 'ID2', label=' letter ')
    DFA.edge('NOT2', 'ID2', label=' letter ')
    ##########################################
    DFA.edge('=', 'NUM2', label=' digit ')
    DFA.edge('>', 'NUM2', label=' digit ')
    DFA.edge('<', 'NUM2', label=' digit ')
    DFA.edge('>=', 'NUM2', label=' digit ')
    DFA.edge('<=', 'NUM2', label=' digit ')
    DFA.edge('AND2', 'NUM2', label=' digit ')
    DFA.edge('OR2', 'NUM2', label=' digit ')
    DFA.edge('NUM2', 'NUM2', label=' digit ')
    DFA.edge('NOT2', 'NUM2', label=' digit ')
    ############################################
    DFA.edge('=', 'NOT2', label=' ! ')
    DFA.edge('>', 'NOT2', label=' ! ')
    DFA.edge('<', 'NOT2', label=' ! ')
    DFA.edge('>=', 'NOT2', label=' ! ')
    DFA.edge('<=', 'NOT2', label=' ! ')
    DFA.edge('AND2', 'NOT2', label=' ! ')
    DFA.edge('OR2', 'NOT2', label=' ! ')
    ############################################
    DFA.edge('START', 'Invalid_token', label='[other]')
    DFA.edge('ID1', 'Invalid_token', label='[other]')
    DFA.edge('NUM1', 'Invalid_token', label='[other]')
    DFA.edge('NOT1', 'Invalid_token', label='[other]')
    DFA.edge('=', 'Invalid_token', label='[other]')
    DFA.edge('>', 'Invalid_token', label='[other]')
    DFA.edge('<', 'Invalid_token', label='[other]')
    DFA.edge('>=', 'Invalid_token', label='[other]')
    DFA.edge('<=', 'Invalid_token', label='[other]')
    DFA.edge('ID2', 'Invalid_token', label='[other]')
    DFA.edge('NUM2', 'Invalid_token', label='[other]')
    DFA.edge('AND1', 'Invalid_token', label='[other]')
    DFA.edge('OR1', 'Invalid_token', label='[other]')
    DFA.edge('AND2', 'Invalid_token', label='[other]')
    DFA.edge('OR2', 'Invalid_token', label='[other]')
    DFA.edge('NOT2', 'Invalid_token', label='[other]')
    DFA.edge('ANDE1', 'Invalid_token', label='[other]')
    DFA.edge('ANDE2', 'Invalid_token', label='[other]')
    DFA.edge('ORE1', 'Invalid_token', label='[other]')
    DFA.edge('ORE2', 'Invalid_token', label='[other]')
    ############################################
    DFA.edge('ID2', 'ANDE1', label=' & ')
    DFA.edge('NUM2', 'ANDE1', label=' & ')
    DFA.edge('ID2', 'ORE1', label=' | ')
    DFA.edge('NUM2', 'ORE1', label=' | ')
    DFA.edge('NUM2', 'ORE1', label=' | ')
    DFA.edge('ANDE1', 'ANDE2', label=' & ')
    DFA.edge('ORE1', 'ORE2', label=' | ')
    DFA.edge('ANDE2', 'ID1', label=' letter ')
    DFA.edge('ANDE2', 'NUM1', label=' digit ')
    DFA.edge('ORE2', 'ID1', label=' letter ')
    DFA.edge('ORE2', 'NUM1', label=' digit ')
    DFA.render(view=1)


# click Derivation
def DERIVATION_btnClickFunction():
    print('Derivation clicked')


# click String Parse Tree
def PARSE_TREE_btnClickFunction():
    print('String Parse Tree clicked')


# click String Syntax Tree
def SYNTAX_TREE_btnClickFunction():
    print('String Syntax Tree clicked')


root = Tk()

string = StringVar()

# main window
root.geometry('500x300')
root.configure(background='#F5F5F5')
root.title('COMPILER')
# labels of title
Label(root, text='Lexical Analyser and Parser', bg='#F5F5F5', font=('courier', 14, 'normal')).place(x=18, y=14)
Label(root, text='Logical Operators', bg='#F5F5F5', font=('courier', 9, 'normal')).place(x=329, y=23)
# text input box
input_entry = Entry(root, textvariable=string)
input_entry.place(x=19, y=58)
# buttons
sub_btn= Button(root,text = 'Ok', command = submit)
sub_btn.place(x=178, y=53)
Button(root, text='List of Tokens', bg='#E6E6FA', font=('helvetica', 12, 'normal'),
       command=Tokens_btnClickFunction).place(x=33, y=114)
Button(root, text='Operations DFA', bg='#E6E6FA', font=('helvetica', 12, 'normal'), command=DFA_OP_btnClickFunction).place(x=33, y=170)
Button(root, text='Accepting String DFA', bg='#E6E6FA', font=('helvetica', 12, 'normal'),
       command=DFA_STRING_btnClickFunction).place(x=33, y=227)
Button(root, text='Derivation', bg='#E6E6FA', font=('helvetica', 12, 'normal'),
       command=DERIVATION_btnClickFunction).place(x=302, y=114)
Button(root, text='String Parse Tree', bg='#E6E6FA', font=('helvetica', 12, 'normal'),
       command=PARSE_TREE_btnClickFunction).place(x=302, y=168)
Button(root, text='String Syntax Tree', bg='#E6E6FA', font=('helvetica', 12, 'normal'),
       command=SYNTAX_TREE_btnClickFunction).place(x=302, y=225)

root.mainloop()

# events handled:STRING ENTRY/ NEW WINDOW WHEN BUTTON CLICKED
# handled by printing tokens and shifting arrows "ACCEPTED"



#############################################################################################
# strings = input('Enter String: ')

