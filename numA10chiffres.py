

import tkinter as tk
from tkinter import font



#fonctions
def operation():
    op=enter_var.get()
    if  op[1]=="1" or op[1]=="2" or op[1]=="3":
        ope_var.set("MOOV")
        pre_var.set("01")
        num10_var.set("01"+op)
    elif   op[1]=="4" or op[1]=="5" or op[1]=="6":
        ope_var.set("MTN")
        pre_var.set("05")
        num10_var.set("05"+op)
    elif  op[1]=="7" or op[1]=="8" or op[1]=="9":
        ope_var.set("ORANGE")
        pre_var.set("07")
        num10_var.set("07"+op)



#création et parametrage de la fenetre
projet = tk.Tk ()
projet.title("Indicatif téléphonique CIV")
screen_x = int (projet.winfo_screenwidth ())
screen_y = int (projet.winfo_screenheight())
win_x = 800
win_y = 600
posx = (screen_x // 2) - (win_x // 2)
posy = (screen_y // 2) - (win_y // 2)
geo =  "{}x{}+{}+{}".format(win_x, win_y, posx, posy)
projet.geometry(geo)
projet.resizable(0,0)

#widget
intro= tk.Frame(projet, height=100, width=800, background="orange")
intro_texte=tk.Label(intro, text="MISE A JOUR DES NUMEROS DE TELEPHONE CIV", fg="white", font=(22), background="orange")
num8=tk.Label(projet, text="Numéro à 8 chiffres:", font=(20), fg="green")
f=font.Font(num8, num8.cget("font"))
f.configure(underline=True)
num8.configure(font=f)
enter_var= tk.StringVar()
entrez_num = tk.Entry(projet, width= 30, textvariable=enter_var, )
mise_a_jour = tk.Button(projet, text= "Mise à Jour", width="100", background="blue", command=operation)
operateur=tk.Label(projet, text="OPERATEUR:", fg="green", font=(23), background="white")
f=font.Font(operateur, operateur.cget("font"))
f.configure(underline=True)
operateur.configure(font=f)
ope_var=tk.StringVar()
ope=tk.Label(projet, background="white", width=30, textvariable=ope_var)
prefixe=tk.Label(projet, text="PREFIXE:", fg="green", background="white", font=(23))
f=font.Font(prefixe, prefixe.cget("font"))
f.configure(underline=True)
prefixe.configure(font=f)
pre_var=tk.StringVar()
pre=tk.Label(projet, background="white", width=30, textvariable=pre_var)
num10=tk.Label(projet,text="NUMERO A 10 CHIFFRES", fg="green", font=(24), background="white")
f=font.Font(num10, num10.cget("font"))
f.configure(underline=True)
num10.configure(font=f)
num10_var=tk.StringVar()
affiche_num10= tk.Label(projet, textvariable=num10_var, width=30, background="white", font=(2))
fin=tk.Frame(projet, background="orange", height=100, width=800)

#Positionnement des widgets
intro.grid()
intro_texte.place(x=150, y=30)
num8.grid(padx=90, pady=50, sticky="w",row=1)
entrez_num.grid(row=1, sticky="e",padx=60)
mise_a_jour.grid()

operateur.grid(sticky="w", padx= 110, pady=50, row=10)
ope.grid(sticky="e", row=10, padx=60)
prefixe.grid(sticky="w", row=11, padx=110)
pre.grid(row=11, sticky="e", padx=60)
num10.grid(row=12, sticky="w", padx=110,pady=50)
affiche_num10.grid(sticky="e", row=12, padx=60)
fin.grid(sticky="s")
#boucle principale

projet.mainloop()
   