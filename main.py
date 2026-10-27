import pyttsx3
import time

engine = pyttsx3.init()

pontos = 0
erros = 0

print("Responda so com o segundo nome, exemplo: Itoshi Rin, responda apenas com Rin.")
time.sleep(3)

engine.say("Bem-vindo ao quiz de Blue Lock!")
time.sleep(1)
engine.say("Vamos começar com a primeira pergunta.")
time.sleep(1)
engine.say("Qual é o melhor jogador do mundo em Blue Lock?")
engine.runAndWait()
time.sleep(6)
World_Class = input("Digite sua resposta: ").strip().lower()

if World_Class == "noa":
    mensagem = "Parabéns, você acertou!"
    pontos += 1
else:
    mensagem = "Resposta incorreta!"
    erros += 1

print(mensagem)
engine.say(mensagem)
engine.runAndWait()

time.sleep(2)
engine.say("Segunda pergunta.")
time.sleep(1)
engine.say("Qual o nome do new gen do japão?")
engine.runAndWait()
time.sleep(6)
New_Gen = input("Digite sua resposta: ").strip().lower()

if New_Gen == "sae":
    mensagem = "Parabéns, você acertou!"
    pontos += 1
else:
    mensagem = "Resposta incorreta!"
    erros += 1

print(mensagem)
engine.say(mensagem)
engine.runAndWait()

time.sleep(2)
engine.say("Terceira pergunta.")
time.sleep(1)
engine.say("Qual o nome do protagonista de blue lock?")
engine.runAndWait()
time.sleep(6)
Protagonista = input("Digite sua resposta: ").strip().lower()

if Protagonista == "isagi":
    mensagem = "Parabéns, você acertou!"
    pontos += 1
else:
    mensagem = "Resposta incorreta!"
    erros += 1

print(mensagem)
engine.say(mensagem)
engine.runAndWait()

time.sleep(2)
engine.say("Quarta pergunta.")
time.sleep(1)
engine.say("Qual o nome do imperador de blue lock?")
engine.runAndWait()
time.sleep(6)
Empereor = input("Digite sua resposta: ").strip().lower()

if Empereor == "kaiser":
    mensagem = "Parabéns, você acertou!"
    pontos += 1
else:
    mensagem = "Resposta incorreta!"
    erros += 1

print(mensagem)
engine.say(mensagem)
engine.runAndWait()

time.sleep(1)
print("Quiz finalizado!")
print("Você acertou", pontos, "perguntas.")
print("Você errou", erros, "perguntas.")
print("Pontuação final:", pontos, "/ 4")

engine.say("Quiz finalizado!")
engine.say(f"Você acertou {pontos} perguntas.")
engine.say(f"Você errou {erros} perguntas.")
engine.runAndWait()

engine.stop()
