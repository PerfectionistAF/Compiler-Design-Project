# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import graphviz
import re
from tkinter import *


# Design
# this is a function to get the user input from the text input box
from graphviz import Digraph


def getInputBoxValue():
	userInput = Enter_string.get()
	return userInput

# click OK to stop entry
def OK_btnClickFunction():
	print('OK clicked')

# click List of Tokens
def Tokens_btnClickFunction():
    print('List of Tokens clicked')
    token_window =Tk()
    token_window.geometry("700x350")
    token_window.title('Tokeniser')
    Label(token_window, text='token[]', bg='#F5F5F5', font=('courier', 9, 'normal')) #print tokens as labels

# click Operations DFA
def DFA_OP_btnClickFunction():
    print('Operations DFA clicked')
    operations_window=Tk()
    operations_window.geometry("700x350")
    operations_window.title('Logical Operators DFA')
    f: Digraph = graphviz.Digraph('DFA', filename='fsm.gv')
    f.view()

# click Accepting String DFA
def DFA_STRING_btnClickFunction():
	print('Accepting String DFA clicked')

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

# main window
root.geometry('500x300')
root.configure(background='#F5F5F5')
root.title('COMPILER')
# labels of title
Label(root, text='Lexical Analyser and Parser', bg='#F5F5F5', font=('courier', 14, 'normal')).place(x=18, y=14)
Label(root, text='Logical Operators', bg='#F5F5F5', font=('courier', 9, 'normal')).place(x=329, y=23)
# text input box
Enter_string=Entry(root)
Enter_string.place(x=19, y=58)
# buttons
Button(root, text='OK', bg='#BEBEBE', font=('helvetica', 10, 'normal'), command=OK_btnClickFunction).place(x=178, y=53)
Button(root, text='List of Tokens', bg='#E6E6FA', font=('helvetica', 12, 'normal'), command=Tokens_btnClickFunction).place(x=32, y=114)
Button(root, text='Operations DFA', bg='#E6E6FA', font=('helvetica', 12, 'normal'), command=DFA_OP_btnClickFunction).place(x=33, y=170)
Button(root, text='Accepting String DFA', bg='#E6E6FA', font=('helvetica', 12, 'normal'), command=DFA_STRING_btnClickFunction).place(x=34, y=227)
Button(root, text='Derivation', bg='#E6E6FA', font=('helvetica', 12, 'normal'), command=DERIVATION_btnClickFunction).place(x=302, y=114)
Button(root, text='String Parse Tree ', bg='#E6E6FA', font=('helvetica', 12, 'normal'), command=PARSE_TREE_btnClickFunction).place(x=303, y=168)
Button(root, text='String Syntax Tree', bg='#E6E6FA', font=('helvetica', 12, 'normal'), command=SYNTAX_TREE_btnClickFunction).place(x=302, y=225)


root.mainloop()

# events handled:STRING ENTRY/ NEW WINDOW WHEN BUTTON CLICKED
# handled by printing tokens and shifting arrows "ACCEPTED"
'''events = []
def handle_OK(event):
    print(event.string)

while True:
    if events == []:
        continue

    event = events[0]
    if event.type == "OK_clicked":
        handle_OK(event)'''

# NUM and ID

IDENTIFIER = re.compile(r"([a-zA-Z]+\Z)")
NUM = re.compile(r"(\d +\Z)")

# OP

EQUAL = re.compile(r"[=]{1}\Z")
LESS_THAN = re.compile(r"[<]{1}\Z")
GREATER_THAN = re.compile(r"[>]{1}\Z")
LESS_THAN_OR_EQUAL = re.compile(r"[<=]{2}\Z")
GREATER_THAN_OR_EQUAL = re.compile(r"[>=]{2}\Z")
OR = re.compile(r"[\|\|]{2}\Z")
AND = re.compile(r"[&&]{2}\Z")
NOT = re.compile(r"[!]{1}\Z")
OPEN_BRACKET = re.compile(r"[\(]{1}\Z")
CLOSE_BRACKET = re.compile(r"[\)]{1}\Z")

#############################################################################################

strings = input('Enter String: ')  ##create label
strings = strings.split(' ')
token = []   ##store token list
##initiate graph for DFA_OP
f = graphviz.Digraph('DFA', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')
f.attr('node', shape='doublecircle')
f.node('Done')
f.attr('node', shape='circle')
f.node('Start')
f.edge('Start', 'Start', label='whitespace')
f.view()
for string in strings:
    if re.search(IDENTIFIER, string):
        print('IDENTIFIER', ',', string)
        token.append(['IDENTIFIER', string])
        f.node('ID')
        f.edge('Start', 'ID', label='letter')
        f.edge('ID', 'ID', label='letter')
        f.edge('ID', 'Done', label='[other]')
        f.view()
    if re.search(NUM, string):
        print('NUM', ',', string)
        token.append(['NUM', string])
        f.node('NUM')
        f.edge('Start', 'NUM', label='digit')
        f.edge('NUM', 'NUM', label='digit')
        f.edge('NUM', 'Done', label='[other]')
        f.view()

    if re.search(EQUAL, string):
        print('EQUAL', ',', string)
        token.append(['EQUAL', string])
        f.node('equal')
        f.edge('Start', 'equal', label='=')
        f.edge('equal', 'Done', label='[other]')
        f.view()
    elif re.search(LESS_THAN, string):
        print('LESS_THAN', ',', string)
        token.append(['LESS_THAN', string])
        f.node('less_than')
        f.edge('Start', 'less_than', label='<')
        f.edge('less_than', 'Done', label='[other]')
        f.view()
    elif re.search(GREATER_THAN, string):
        print('GREATER_THAN', ',', string)
        token.append(['GREATER_THAN', string])
        f.node('greater_than')
        f.edge('Start', 'greater_than', label='>')
        f.edge('greater_than', 'Done', label='[other]')
        f.view()
    elif re.search(GREATER_THAN_OR_EQUAL, string):
        print('GREATER_THAN_OR_EQUAL', ',', string)
        token.append(['GREATER_THAN_OR_EQUAL', string])
        f.node('greater_than_or_equal')
        f.edge('greater_than', 'greater_than_or_equal', label='=')
        f.edge('greater_than_or_equal', 'Done', label='[other]')
        f.view()
    elif re.search(LESS_THAN_OR_EQUAL, string):
        print('LESS_THAN_OR_EQUAL', ',', string)
        token.append(['LESS_THAN_OR_EQUAL', string])
        f.node('less_than_or_equal')
        f.edge('less_than', 'less_than_or_equal', label='=')
        f.edge('less_than_or_equal', 'Done', label='[other]')
        f.view()
    elif re.search(OR, string):
        print('OR', ',', string)
        token.append(['OR', string])
        f.node('OR')
        f.edge('Start', 'OR', label='|')
        f.edge('OR', 'Done', label='|')
        f.edge('OR', 'Stuck', label='[other]')
        f.view()
    elif re.search(AND, string):
        print('AND', ',', string)
        token.append(['AND', string])
        f.node('AND')
        f.edge('Start', 'AND', label='&')
        f.edge('AND', 'Done', label='&')
        f.edge('AND', 'Stuck', label='[other]')
        f.view()
    elif re.search(NOT, string):
        print('NOT', ',', string)
        token.append(['NOT', string])
        f.node('NOT')
        f.edge('Start', 'NOT', label='!')
        f.edge('NOT', 'Stuck', label='[other]')
        f.view()
    elif re.search(OPEN_BRACKET, string):
        print('OPEN_BRACKET', ',', string)
        token.append(['OPEN_BRACKET', string])
        f.node('open_bracket')
        f.edge('Start', 'open_bracket', label='(')
        f.edge('open_bracket', 'Done', label='[other]')
        f.view()
    elif re.search(CLOSE_BRACKET, string):
        print('CLOSE_BRACKET', ',', string)
        token.append(['CLOSE_BRACKET', string])
        f.node('close_bracket')
        f.edge('Start', 'close_bracket', label=')')
        f.edge('close_bracket', 'Done', label='[other]')
        f.view()
    else:
        print('Stuck', ',', string)
        token.append(['Stuck', string])
        f.node('Stuck')
        f.edge('Start', 'Stuck', label='else')
        f.view()

f.view()
