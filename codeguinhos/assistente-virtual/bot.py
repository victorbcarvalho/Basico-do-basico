import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Inicialize o objeto de síntese de fala
engine = pyttsx3.init()

# Obtenha todas as vozes disponíveis no sistema
voices = engine.getProperty('voices')

# Verifique se a lista de vozes não está vazia
if len(voices) > 0:
    # Loop através das vozes disponíveis
    for voice in voices:
        # Verifique se a voz é para o idioma "pt-br"
        if voice.name=='Microsoft Maria Desktop - Portuguese(Brazil)':
            # Se a voz for para o idioma "pt-br", defina-a como a voz padrão
            engine.setProperty('voice', voice.id)
            break
else:
    # Se a lista de vozes estiver vazia, exiba uma mensagem de erro
    print("Não foi possível encontrar vozes disponíveis no sistema.")

# Defina a função de reconhecimento de fala
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='pt-BR')
        print("Você disse: {}".format(text))
        return text
    except:
        print("Desculpe, não entendi o que você disse.")
        return ""

# Defina a função para sintetizar fala
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()
    
# função para abrir um aplicativo
def abrir_aplicativo(aplicativo):
    os.system(f'start {aplicativo}.exe')

# função para realizar uma pesquisa na web
def pesquisar(texto):
    url = f'https://www.google.com/search?q={texto}'
    webbrowser.open(url)

# Loop principal do bot
while True:
    # Ouça o que o usuário tem a dizer
    comando = speech_to_text()

    # Se o usuário não disse nada, continue ouvindo
    if not comando:
        continue

    # Responda ao usuário
    if 'Oi' in comando:
        text_to_speech('Olá! Como posso ajudá-lo?')
    elif 'tchau' in comando:
        text_to_speech('Até logo!')
        break
    # verifica se o comando é para realizar uma pesquisa
    elif 'pesquisar por' in comando:
        termo = comando.replace('pesquisar por', '').strip()
        text_to_speech(f'Pesquisando por {comando[13:]}')
        pesquisar(termo)
    
    # verifica se o comando é para abrir um aplicativo
    elif 'Abrir' in comando:
        aplicativo = comando.replace('Abrir', '').strip()
        print(aplicativo)
        text_to_speech(f'Abrindo {comando[5:]}')
        abrir_aplicativo(aplicativo)
    else:
        text_to_speech('Desculpe, não entendi o que você disse.')
