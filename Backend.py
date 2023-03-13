from app import *

# DEFININDO FUNÇÃO

caminho_download = ''

def diretorio_download():
    global caminho_download

    caminho_download = filedialog.askdirectory(title='Save file')
    path_link.delete(0, 'end')
    path_link.insert(0, caminho_download)

    caminho_download = str(caminho_download)

def download_V():  
    def download_vv():
        url = link.get()
        if url == '':
            messagebox.showwarning(title='Link' , message= 'Insira um link               ')


        elif caminho_download == '':
            messagebox.showwarning(title='Diretório' , message= 'Selecione o diretório               ')

        else:
            status.config(text='Status: Downloading...')
            yt = YouTube(url, on_complete_callback= finalizado)

            yt.streams.filter(progressive= TRUE,file_extension= 'mp4')

            stream = yt.streams.get_highest_resolution()

            stream.download(output_path= caminho_download)

    thread3 = threading.Thread(target=download_vv)
    thread4 = threading.Thread(target=download_vv)

    lista_v = [0]

    if lista_v[0] == 3:
        del lista_v[0]
        lista_v.append(4)
        thread3.start()
    else:
        del lista_v[0]
        lista_v.append(3)
        thread4.start()
 
def download_A():
    def download():
        url = link.get()

        if url == '':
            messagebox.showwarning(title='Link' , message= 'Insira um link               ')

        elif caminho_download == '':
            messagebox.showwarning(title='Diretório' , message= 'Selecione o diretório               ')
        
        else:
            status.config(text='Status: Downloading...')
            yt = YouTube(url, on_complete_callback= finalizado)
            yt.streams.filter(progressive= TRUE, file_extension= 'mp3')


            stream = yt.streams.get_audio_only()

            stream.download(output_path= caminho_download)

    thread1 = threading.Thread(target=download)
    thread2 = threading.Thread(target=download)

    lista = [0]

    if lista[0] == 1:
        del lista[0]
        lista.append(2)
        thread1.start()
    else:
        del lista[0]
        lista.append(1)
        thread2.start()
        
def finalizado(stream=None,chunk=None, file_handle=None, remaining=None ):
    status.config(text='Status: Complete')


# CRIANDO BOTÃO .. Não estava dando certo em criar no arquivo app

btn_D_video = Button(janela, text= 'Download video', width= 15, relief= RAISED, overrelief= RIDGE, font= 'Arial 13', command=  download_V)
btn_D_video.place(x= 410, y= 225, height= 30)

btn_Audio = Button(janela, text= 'Download áudio', width= 15, relief= RAISED, overrelief= RIDGE, font= 'Arial 13', command= download_A)
btn_Audio.place(x= 220, y= 225, height= 30)

btn_Direc = Button(janela, text= 'Brownse', width= 8,command=diretorio_download)
btn_Direc.place(x= 630, y= 160, height= 30)

# Criando status bar

status = Label(janela, text='Status: Ready', font= 'Calibre 12 italic', fg='black', bg='white', anchor='w')
status.place(rely=1, anchor='sw', relwidth= 1)

janela.mainloop()