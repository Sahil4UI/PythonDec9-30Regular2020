from datetime import datetime
import webbrowser
import os,glob,random
chat=True
while chat==True:
    msg=input("Enter message : ")
    
    if msg=='hello' or msg=='hi' or msg=='hey':
        print("Hello Sir...")
    
    elif msg=="bye":
        print("Bye Sir...")
        # chat=False
        break
    
    elif msg.startswith('open'):
        url = msg.split()[-1]+".com"
        webbrowser.open(url)
        
    elif msg=="date":
        dt=datetime.now()
        print(dt.strftime("%d/%m/%y,%a"))
        
    elif msg=="music" or msg=="song":
        path=r"C:\Users\sahil\Downloads"
        os.chdir(path)        
        music = glob.glob("*.mp3")
        song=random.choice(music)
        os.startfile(song)
        
    elif msg=="date":
        dt=datetime.now()
        print(dt.strftime("%d/%m/%y,%a"))
    
    else:
        print("Invalid Message")
