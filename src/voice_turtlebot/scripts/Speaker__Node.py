import websocket
import json
import speech_recognition

server_port="ws://localhost:9090"



def sending_command(ws,command):

    msg={
        "op":"publish",
        "topic":"/voice_commands",
        "msg":{"data":command}
    }

    ws.send(json.dumps(msg))
    print(f"Sent command: {command}")

def recognize(ws):

    recognizer = speech_recognition.Recognizer()
    mic= speech_recognition.Microphone()

    while True: 

        with mic as a:
            print("Say a command:")
            recognizer.adjust_for_ambient_noise(a)
            audio= recognizer.listen(a)

        try:
            cmd= recognizer.recognize_google(audio).lower()
            print(f"recognized: {cmd}")

            sending_command(ws, cmd)

        except speech_recognition.UnknownValueError:
            print("Could not understand audio")
        
        except speech_recognition.RequestError:
            print("Speech Recognition service is unavailable")



if __name__=='__main__':
     
     hrik= websocket.create_connection(server_port)

     try:
         recognize(hrik)
     finally:
         hrik.close()
         print("WebSocket connection closed.")