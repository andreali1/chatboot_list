from  chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Rocio")
#chatbot.storage.drop()
frases = ["hola","buen dia, en que puedo ayudarte", "saludos","vete a la mierda ",
          "como estas? como te encuentras? que tal tu dia ?", "bien",
    "mandar un mensaje de texto whatsapp, nota",
    " perfecto escribamos el mensaje ", "¿Puedo hacerle una pregunta?",
  "Por supuesto, para eso estoy"]

trainer = ListTrainer(chatbot)
trainer.train(frases)
while True:
    palabra = input("empieza la conversacion ")
    respuestas = chatbot.get_response(palabra)
    print( "virtual --> {}".format(respuestas))