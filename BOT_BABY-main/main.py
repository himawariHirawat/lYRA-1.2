# import threading


# t1 = threading.Thread(target=nltk_funk)
# t1.start()
# t1.join()

from termcolor import colored
import datetime
import time
import wikipedia
import os
import json
import requests
import pandas as pd
from AppOpener import  open
import webbrowser
from tkinter import Tk
from tkinter.filedialog import askopenfilename




query = 0

queries = pd.read_csv("temp.csv")
con = pd.read_csv("Conversation.csv")
songs = pd.read_csv("spotify_songs.csv")
cuss = pd.read_csv("cuss.csv")

questions = con["question"]
answers = con["answer"]

song_name = songs["track_name"]
artist_name = songs["track_artist"]

cuss_words = cuss["cuss"]

q = queries["queries"]

def takeCommand():
  global query
  query = str(input(colored("You: ", "red")))
  query.lower()

#   Filtering the text
  try:
    query = query.replace("  ", " ")
  except:
      pass
  
  try:
    query = query.replace("   ", " ")
  except:
      pass
  
  try:
    query = query.replace("    ", " ")
  except:
      pass
  
  return query

def wishMe():
    morning = ["Good Morning sir", "Bon Matin sir", "buenos días sir","guten Morgen Sir", "buongiorno sir"]
    afternoon = ["Dobar Dan sir", "Mayad nga apon", "Dobré odpoledne Sir", "Good Afternoon sir", "God eftermiddag Sir"]
    evening = ["Good Evening sir","Boa Noite Sir", "Buenas Tardes Sir", "Bonsoir Sir", "Guten Abend Sir", "Buonasera Sir"]
    
    import random 
    mor = random.choice(morning)
    after = random.choice(afternoon)
    eve = random.choice(evening)

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        printl(mor)

    elif hour >= 12 and hour < 18:
        printl(after)

    else:
        printl(eve)
  
    printl("Please tell me how may I help you")

def countdown(time_sec):
  try:
      while time_sec != 0:
          min = time_sec
          timeformat = '{:02d}:{:02d}'.format(0, time_sec)
          printl(timeformat)
          time.sleep(1)
          time_sec -= 1
  except Exception as e:
              printl("Sorry sir, i am not able to do this task!")

  printl("Sir the time is up!")



def printl(a):
  a = colored("Bot_baby: ", "yellow") + a + '.'
  print(colored(a, "red"))

state = True

for i in con['question']:
    i = i.lower()

else_state = True



if __name__ == "__main__":
  wishMe()
  
  temp_state = False
  conv = True

  else_state = False
  # countdown(5)
  while True:
    query = takeCommand().lower()


    for i in cuss_words:
        if i in query:
            printl("Please mind your language.")
            else_state = False
            conv = False
            break
            
        else:
            conv = True
            continue
        

    sum = ["sum", "add", "total", "increased by", "added to", "plus", "+"]


    if conv == True:
        for i in sum:
            if i in query:
                try: 
                    if '+' in query:
                        query.replace('+', " + ")
                    a= list(query.split(" "))
                    numbers = []
                    for i in a:
                        try:
                            int(i)
                            numbers.append(i)
                        except Exception as e:
                            continue

                    sum = 0
                    for i in numbers:
                        sum+=int(i)
                    
                    resp = "The sum is " + colored(sum, "blue")
                    printl(resp)
                    state = True
                    break
                except Exception as e:
                    printl("Sorry sir I am not able to perform this calculation.")
            else:
                else_state = True

    multi = ["multiply", "product", "*", " X ", " x "]

    if conv == True:
        for i in multi:
            if i in query:
                try: 
                    if 'x' in query:
                        query.replace('x', " x ")
                    a= list(query.split(" "))
                    numbers = []
                    for i in a:
                        try:
                            int(i)
                            numbers.append(i)
                        except Exception as e:
                            continue
                    product = 1
                    for i in numbers:
                        product = product * int(i)
                    
                    resp = "The product is " + colored(product, "blue")
                    printl(resp)
                    state = True
                    break
                except Exception as e:
                    printl("Sorry sir I am not able to perform this calculation.")
            else:
                else_state = True
    if conv == True:
        try:

            for i in con["question"]:
                    if i in query:
                        response = con.loc[con['question'] == i, 'answer'].values[0].replace(';', ',')
                        a = response.replace("'", "")
                        printl(a)
                        # If an roast battle
                        if "roast battle" in i:
                            roast = takeCommand()
                            if "mom" in roast:
                                printl("Oh please, your mom is so technologically challenged, she thinks Bluetooth is a dental condition. I heard she tried to download a workout app and her phone just burst into flames.")
                            elif "dad" in roast or "father" in roast or "daddy" in roast or "pop" in roast or "papa" in roast:
                                printl("Your dad is so bad at telling jokes, even Siri refuses to respond when he asks, 'Hey Siri, tell me a joke.' I heard he once told a dad joke so cheesy that the crickets started a slow clap out of pity.")
                            printl("Now i am tired of these silly jokes. Let's end this battle. I accept my defeat.")
                        
                        
                        # else_state = False
                        state = True
                        temp_state = False
                        else_state = False

                        break
        except Exception as e:
            else_state = True
            temp_state = True
            continue

    if else_state == True:
        print(else_state)
        if 'quit' in query:
            printl("Thank you sir!")
            os.system(quit())

        elif 'the time' in query:
                try:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    printl(f"Sir, the time is {strTime}")
                except Exception as e:
                    printl("Sorry sir, i am not able to do this task!")
        elif 'the date' in query:
            try:
                strdate = datetime.datetime.now().strftime("%D")
                printl(f"Sir, the date is {strdate}")
                # queries.append(query)
            except Exception as e:
                printl("Sorry sir, i am not able to do this task!")
        elif 'change name of a file' in query:
            try:
                printl("Which file?")
                window = Tk()
                window.wm_attributes('-topmost', 1)
                window.withdraw() 
                k = askopenfilename(parent=window)
                k.replace('/', "\\")
                printl("What's the new name")
                d = str(takeCommand())
                a = k
                a = list(a.split("/"))
                file_name = a[-1]
                # Extension bug fixed
                dot_split = list(file_name.split("."))
                extension = dot_split[-1]
                extension = "." + extension
                new_path = k.replace(file_name, d) + extension
                # Main renaming algorithm
                os.renames(k, new_path)
                printl("Successfully renamed!")
                # queries.append(query)
            except Exception as e:
                printl(e)
                printl("Sorry sir, i am not able to do this task!")
        elif 'the year' in query:
            try:
                strYear = datetime.datetime.now().strftime("%Y")
                print(f" {strYear}")
                printl(f"Sir, the year is {strYear}")
                # queries.append(query)
            except Exception as e:
                printl("Sorry sir, i am not able to do this task!")
        elif 'quote' in query or 'pickup line' in query or 'thought' in query or 'motivate' in query:
                import urllib3
                http = urllib3.PoolManager(num_pools=50)
                response = requests.get("https://zenquotes.io/api/random")
                json_data = json.loads(response.text)
                quote = json_data[0]['q']
                printl(quote)
        elif 'song' in query and 'suggest' in query:
            import random
            no = random.randint(0, 29999)
            printl(f"You can listen to {song_name[no]} composed by {artist_name[no]}")
            try:
                open("spotify")
            except Exception as e:
                continue
        elif "open" in query:
            a = query
            a = list(a.split(" "))
            ind = a.index('open')
            try:
                try:
                    webbrowser.open(str(a[ind+1])  + ".com", 2)
                    open(str(a[ind+1]), match_closest=True)
                    if "NOT" in a:
                        print("aquhyigy")
                        try:
                            webbrowser.open(str(a[ind+1]) + ".com", 2)
                        except Exception as e:
                            print(e)
                            try:
                                open(str(a[ind+1])+" "+str(a[ind+2]), match_closest=True)
                            except Exception as e:
                                open(str(a[ind+1])+" "+str(a[ind+2]) + " "+str(a[ind+3]), match_closest=True)
                except Exception as e: 
                    try:
                        webbrowser.open(str(a[ind+1]) + ".com", 2)
                    except Exception as e:
                        try:
                            open(str(a[ind+1])+" "+str(a[ind+2]))
                        except Exception as e:
                            open(str(a[ind+1])+" "+str(a[ind+2]) + " "+str(a[ind+3]))
                if("NOT FOUND" in open(str(a[ind+1]))):
                    try:
                        webbrowser.open(str(a[ind+1]) + ".com", 2)
                    except Exception as e:
                        try:
                            open(str(a[ind+1])+" "+str(a[ind+2]))
                        except Exception as e:
                            open(str(a[ind+1])+" "+str(a[ind+2]) + " "+str(a[ind+3]))
            except Exception as e:
                printl("I am sorry sir! I have encountered with a error")
        elif 'set' in query and 'timer' in query:
            try:
                a = list(query.split(" "))
                for i in a:
                    try:
                        int(i)
                        temp = i
                        break
                    except Exception as e:
                        continue
                counter = int(temp)
                countdown(counter)
            except Exception as e:
                try:
                    printl("For how many seconds")
                    h = int(takeCommand())
                    countdown(h)
                    # queries.append(query)
                except Exception as e:
                    printl("Sorry sir, i am not able to do this task!")

        elif "start log" in query:
            printl("Please press q for stoping the recording.")
            import cv2
            import os
            import datetime

            output_dir = "chatbot"

            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            video_writer = None
            current_video_path = None
            is_recording = False

            def start_recording():
                global video_writer, current_video_path, is_recording

                if not is_recording:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    video_filename = f"video_{timestamp}.avi"
                    current_video_path = os.path.join(output_dir, video_filename)

                    video_writer = cv2.VideoWriter(
                        current_video_path,
                        cv2.VideoWriter_fourcc(*"XVID"),
                        30.0,
                        (640, 480),
                    )

                    is_recording = True
                    print(f"Recording started: {current_video_path}")

            def stop_recording():
                global video_writer, current_video_path, is_recording

                if is_recording:
                    video_writer.release()
                    is_recording = False
                    print(f"Recording stopped: {current_video_path}")

            def record_frame(frame):
                global video_writer, is_recording

                if is_recording:
                    video_writer.write(frame)

            if __name__ == "__main__":
                cap = cv2.VideoCapture(0)

                while True:
                    ret, frame = cap.read()

                    cv2.imshow("Frame", frame)

                    record_frame(frame)
                    start_recording()

                    key = cv2.waitKey(1)
            
                    if key == ord("q"):
                        stop_recording()
                        break

                cap.release()
                cv2.destroyAllWindows()

        
        else:

            if query not in q:
                try:
                    results = wikipedia.summary(query, sentences=2)
                    printl("According to Wikipedia")
                    printl(results)
                    state = True
                except Exception as e:
                            printl("Sorry sir, I am not able to do this task!")
                    