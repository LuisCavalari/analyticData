
op=0
while(op!=3):
    op = int(raw_input("Escolha uma opcao \n 1-Celsius para fahreinheint \n 2-fahreinhein para Celius \n 3-sair \n>>>  " ))
    if(op==1):
        fh = float(raw_input("Digite o valor em fahreinheint  \n>>>"))
        c = ((fh-32)/9)*5
        print("O valor em celsius e  %f"%(c))
    elif(op==2):
        cl = float(raw_input("Digite o valor em celsius \n>>> "))
        rfh = ((cl/5)*9)+32
        print("O valor em fahreinhein e  %f"%(rfh))
    elif op==3:
        print "Saindo...."
    else:
        print"Op invalida"
