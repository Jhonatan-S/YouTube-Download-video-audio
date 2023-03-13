from Backend import *
from module import *
import threading

cor_0 = '#4682B4'

janela = Tk()
janela.title('Baixar vídeo do Youtube')
janela.maxsize(800, 300)
janela.minsize(800, 300)
janela['bg'] = cor_0

janela.update_idletasks()  # Update "requested size" from geometry manager

# DEFINIR DIMENSSÃO DA JANELA
width = janela.winfo_width()
frm_width = janela.winfo_rootx() - janela.winfo_x()
janela_width = width + 2 * frm_width

height = janela.winfo_height()
titlebar_height = janela.winfo_rooty() - janela.winfo_y()
janela_height = height + titlebar_height + frm_width

# Get the window position from the top dynamically as well as position from left or right as follows
x = janela.winfo_screenwidth() // 2 - janela_width // 2
y = janela.winfo_screenheight() // 2 - janela_height // 2

# this is the line that will center your window
janela.geometry('800x300+{}+{}'.format( x, y))

# CRIANDO LABELS

label_Jhon = Label(janela, text= "Jhonatan's downloader Software", font= 'Times 20 bold', bg= cor_0)
label_Y = Label(janela, text= 'Download YouTube video', font= 'Arial 15', bg= cor_0, fg= 'white')
label_Jhon.place(x= 200, y=30)
label_Y.place(x= 270, y= 70)

#criando label do entry

label_Entry_link = Label(janela, text= "YouTube link", font= 'Times 12 bold', bg= cor_0)
label_Entry_link.place(x= 33, y= 112)


#Criando label do entry do diretório

label_Folder = Label(janela, text= "Download folder", font= 'Times 12 bold', bg= cor_0)
label_Folder.place(x= 33, y= 162)

# CRIANDO INPUTS

link = Entry(janela, width=64, justify= LEFT, font= 'Arial 10')
link.place(x= 165, y= 110, height= 30)

path_link = Entry(janela, width=64, justify= LEFT, font= 'Arial 10')
path_link.place(x= 165, y= 160, height= 30)



