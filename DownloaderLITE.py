import time
import pytube

from pytube import YouTube, Playlist

print("\n - Utilize 'cancelar' em qualquer momento para fechar -\n")
time.sleep(1)
download = ""
while download != "cancelar":
    resposta = input(" Digite o link do vídeo ou playlist: ")
    print("")

    if resposta.lower() == "cancelar":
        break

    if resposta.__contains__("playlist"):
        try:
            resposta = Playlist(resposta)
            resposta.title
        except Exception as erro:
            print(" -=- Playlist não encontrada, tente novamente! -=-\n")
            continue

        print(f" Baixando a playlist: \"{resposta.title}\"\n" +
        f" Quantidade de videos: \"{len(resposta.video_urls)}\"\n" +
        f" Autor: \"{resposta.owner}\"\n")
        
        i = 0
        for video in resposta.videos:
            video.streams.get_highest_resolution().download("./Downloads")
            i = i + 1
            print(f" {i} - Download concluído: \"{video.title}\" - {video.author}")
        
        print(f"\n -=- Todos downloads foram concluídos com sucesso! -=-\n")
    else:
        try:
            resposta = YouTube(resposta)
            resposta.streams.all
            resposta.streams.get_highest_resolution().download('./Downloads')
            print(f" Download concluído: \"{resposta.title}\" - {resposta.author}\n")
        except pytube.exceptions.PytubeError:
            print(f" -=- Video não encontrado, tente novamente! -=-\n")

print(" - Obrigado por utilizar! -\n")
time.sleep(30)
print(" (O aplicativo será fechado automaticamente em 10 segundos...)")
time.sleep(10)