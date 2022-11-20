import time
import pytube
import colorama

from tqdm import tqdm
from pytube import YouTube, Playlist

colorama.init(True)
green = colorama.Fore.LIGHTGREEN_EX
white = colorama.Fore.WHITE
cyan = colorama.Fore.CYAN
red = colorama.Fore.RED
grey = colorama.Fore.LIGHTBLACK_EX

print("\n - Utilize 'cancelar' em qualquer momento para fechar -\n")
time.sleep(1)
download = ""
while download != "cancelar":
    resposta = input(f"{cyan} Digite o link do vídeo ou playlist: {white}")
    print("")

    if resposta.lower() == "cancelar":
        break

    if resposta.__contains__("playlist"):
        try:
            resposta = Playlist(resposta)
            resposta.title
        except Exception as erro:
            print(f" {red}-=- {white}Playlist não encontrada, tente novamente! {red}-=-\n")
            continue

        print(f" Baixando a playlist: \"{resposta.title}\"\n" +
        f" Quantidade de videos: \"{len(resposta.video_urls)}\"\n" +
        f" Autor: \"{resposta.owner}\"\n")
        
        i = 0
        for video in resposta.videos:
            video.streams.get_highest_resolution().download("./Downloads")
            i = i + 1
            print(f"{grey} {i} - Download concluído: \"{video.title}\"{white} - {video.author}")
        
        print(f"\n {green}-=- {white}Todos downloads foram concluídos com sucesso! {green}-=-\n")
    else:
        try:
            resposta = YouTube(resposta)
            resposta.streams.all
            resposta.streams.get_highest_resolution().download('./Downloads')
            for i in tqdm(range(50)):
                time.sleep(0.05)
            print(f"\n{white} Download concluído: {grey}\"{resposta.title}\" - {white}{resposta.author}\n")
        except pytube.exceptions.PytubeError:
            print(f" {red}-=- {white}Video não encontrado, tente novamente! {red}-=-\n")

print(f"{green} - Obrigado por utilizar! -\n")
time.sleep(30)
print(" (O aplicativo será fechado automaticamente em 10 segundos...)")
time.sleep(10)