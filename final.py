import tkinter as tk
import tkinter.messagebox #i can also use it to create events
from PIL import ImageTk, Image 
from pygame import mixer 
import random 

#pack(): top-bottom
#pack(side=LEFT): left-right 

mixer.init()

class Start:
    def __init__(self,master):
        mixer.music.load("background.mp3")
        mixer.music.play(-1)
        self.master = master
        self.topFrame = tk.Frame(self.master)
        self.topFrame.pack(fill = tk.Y)
        self.bottomFrame = tk.Frame(self.master)
        self.bottomFrame.pack(side=tk.BOTTOM, fill = tk.Y)
        self.deadFrame = tk.Frame(self.master)
        self.deadFrame.pack(side=tk.BOTTOM, fill = tk.Y)
        gameDesc = tk.Label(self.topFrame,text = "For some reasons, you are cursed. \nYou wake up, finding yourself in a 2D world. \nA bloody dead men is lying in front of you. \nHe was murdered. \nBy only finding the true murderer and killing them, you can break the curse, get the key, open the locked door, and return home. \nIf you do not kill the murder, you will be punished, never being able to get out of the 2D world.\n\nPictures from Detective Conan #915 & The Silence of The Lambs\nMusic by Mr.Ravel & Mr.Beethoven\nEverything else: L\n╮(╯▽╰)╭ ",fg = "black")
        gameDesc.pack(side = tk.LEFT, fill = tk.Y) #fill the window! 
        startButton = tk.Button(self.bottomFrame, text = "Start",fg = "black", width = 13, height = 3,command = self.createWorld)
        startButton.pack(side = tk.LEFT)
        img = Image.open("dead.png") 
        img = ImageTk.PhotoImage(img) 
        image = tk.Label(self.deadFrame, image = img)
        image.image = img 
        btn = tk.Button(self.deadFrame, image = img)
        btn.grid(row=0)


    def createWorld(self):
        self.deadFrame.destroy()
        self.topFrame.destroy()
        self.bottomFrame.destroy()
        self.logic = 10
        self.insight = 10
        self.sympathy = 10
        self.eventList = [self.event1, self.event2, self.event3]
        self.statusFrame = tk.Frame(self.master)
        self.statusFrame.pack(side=tk.BOTTOM, fill = tk.X)
        status = tk.Label(self.statusFrame, text = "logic: " + str(self.logic) + " insight: " + str(self.insight) + " sympathy: " + str(self.sympathy), bd = 1, relief = tk.SUNKEN, anchor = tk.W)
        status.pack(side=tk.BOTTOM, fill = tk.X)
        self.itemsCarrying = ""
        toolbar = tk.Frame(self.master, bg = "black")
        help = tk.Button(toolbar, text = "help?", command = self.help)
        help.grid(row=0, padx = 3, pady = 3)
        bag = tk.Button(toolbar, text = "bag", command = self.bag)
        bag.grid(row=0, column = 2, padx = 3, pady = 3)
        event = tk.Button(toolbar, text = "explore", command = self.event)
        event.grid(row=0,column = 4, padx = 3, pady = 3)
        answer = tk.Button(toolbar, text = "I decide to kill...", command = self.answer)
        answer.grid(row=0,column = 6,padx = 3, pady = 3)
        toolbar.pack(side = tk.TOP, fill=tk.X)
        topFrameRoom = tk.Frame(self.master)
        topFrameRoom.pack()
        room1 = tk.Button(topFrameRoom, text = "Hallway", fg = "black", command = self.room1)
        room1.grid(row=0)
        room2 = tk.Button(topFrameRoom, text = "Living Room", fg = "black", command = self.room2)
        room2.grid(row=0,column=1)
        room3 = tk.Button(topFrameRoom, text = "The Wig Store", fg = "black", command = self.room3)
        room3.grid(row=0,column=2)
        room4 = tk.Button(topFrameRoom, text = "Bedroom", fg = "black", command = self.room4)
        room4.grid(row=0,column=3)
        room5 = tk.Button(topFrameRoom, text = "The Locked Door", fg = "black", command = self.lockedDoor)
        room5.grid(row=0,column=4)
        self.createTwoFrame()
        startDesc = tk.Label(self.middleFrameDesc, text = "Please enter a room", fg = "black")
        startDesc.pack()
    
    def status(self):
        self.statusFrame.destroy()
        self.statusFrame = tk.Frame(self.master)
        self.statusFrame.pack(side=tk.BOTTOM, fill = tk.X)
        status = tk.Label(self.statusFrame, text = "logic: " + str(self.logic) + " insight: " + str(self.insight) + " sympathy: " + str(self.sympathy), bd = 1, relief = tk.SUNKEN, anchor = tk.W)
        status.pack(side=tk.BOTTOM, fill = tk.X)
        

    def createTwoFrame(self):
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        self.bottomFrameButton = tk.Frame(self.master)
        self.bottomFrameButton.pack()

    def destroyTwoFrame(self):
        self.middleFrameDesc.destroy()
        self.bottomFrameButton.destroy()

    def showimage(self, fileName, command, column):
        img = Image.open(fileName) 
        img = ImageTk.PhotoImage(img) 
        image = tk.Label(self.bottomFrameButton, image = img)
        image.image = img 
        btn = tk.Button(self.bottomFrameButton, image = img, command = command)
        btn.grid(row=0, column=column)

    def room1(self):
        self.destroyTwoFrame()
        self.createTwoFrame()
        room1Desc = tk.Label(self.middleFrameDesc, text = "A strong man stands in the corner of the room.\nHis face hides in shadow.\nYou vaguely see a serious look on his face—so serious that even seems to be a little too indifferent for the current situation.\nHe is the bodyguard of the dead man, K, and was hired by K two weeks ago.\nHe is the one who found K’s body and called the police.\nMaybe he is feeling guilty for failing his job.\nBut…the look on his face…does it look like being regretful?\nOn the floor, you find a piece of paper and a black bloodstained stick.\nThe stick must be the murder weapon. ", fg = "black")
        room1Desc.pack()
        self.showimage("room1.png", self.character1, 0)
        self.showimage("item1.png", self.item1, 1)
        self.showimage("item2.png", self.item2, 2)
        
    def room2(self):
        self.destroyTwoFrame()
        self.createTwoFrame()
        room1Desc = tk.Label(self.middleFrameDesc, text = "A woman with long beautiful dark-blue hair sits in the sofa, trembling all over.\nShe is E, the fiancee of K and also a well-known model.\nHer face is as pale as a ghost’s, and exaggeratedly twisted.\nSuddenly, she bursts into hysterical laughter.\nIt does not sound like a human voice at all.\nThis women is almost crazy… Indeed, you heard they are about to get married in one month. It is just hard for anyone not to go crazy given the cruel death...\nBut as she looked at you, you seem to catch something more than desperation in her look. It looks like…intense hatred?\nA cop points at a thermometer on the wall and shows you a picture of a train station board.", fg = "black")
        room1Desc.pack()
        self.showimage("room2.png", self.character2, 0)
        self.showimage("item3.png", self.item3, 1)
        self.showimage("item4.png", self.item4, 2)

    def room3(self):
        self.destroyTwoFrame()
        self.createTwoFrame()
        room1Desc = tk.Label(self.middleFrameDesc, text = "This is the largest local wig store. And the owner, Mr. Sunwood, is an old friend of K.\nHe seems to be an honest man. Medium height, nothing worth to describe. Actually, he is so ordinary that it is even hard to believe he owns such a famous wig store.\nHe tells us some history of K. How they went to high school together in Germany and how K got a JD. and became a lawyer, and how himself started this wig store on his own.\nHe especially noted K is kind of a playboy back then. And if it turns out Miss E killed him out of jealousy, he won’t be too surprised.\nThen he shows you around the store. ", fg = "black")
        room1Desc.pack()
        self.showimage("room3.png", self.character3, 0)
        self.showimage("item5.png", self.item5, 1)
        self.showimage("item6.png", self.item6, 2)

    def room4(self):
        self.destroyTwoFrame()
        self.createTwoFrame()
        room1Desc = tk.Label(self.middleFrameDesc, text = "A young man is mourning Mr. K. He is pretty good-looking.\nHe has been K’s personal doctor for five years. He tells you Mr. K hired him just after he graduated from Medical school so he has always being grateful for his trust.\nNothing suspicious about him.\nYou find an old photo and a pair of earrings on the bed.", fg = "black")
        room1Desc.pack()
        self.showimage("room4.png", self.character4, 0)
        self.showimage("item7.png", self.item7, 1)
        self.showimage("item8.png", self.item8, 2)

    def lockedDoor(self):
        self.destroyTwoFrame()
        self.createTwoFrame()
        room1Desc = tk.Label(self.middleFrameDesc, text = "A lokced door connecting 2D and 3D world.\nYou can only open it by killing the murderer(s) of Mr.K", fg = "black")
        room1Desc.pack()
        self.showimage("door.png", self.door, 0)

    def help(self):
        tkinter.messagebox.showinfo("help", "---click images and buttons to navigate---\n---click 'explore' to explore events. The choice you make changes the value of attribute---\n---when you know the killer, click'I decide to kill...' and chose the killer---\n---when you get the key, click the locked door to escape---")

    def bag(self):
        tkinter.messagebox.showinfo("my bag", self.itemsCarrying)

    def character1(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "'My job is, as assigned by Miss E, patrolling around the house for 24 hours and keeping an eye on anything suspicious.\nYesterday at 10 pm, I was about to report the daily passing-by-persons list to Mr. K.\nI knocked the door. No one answered. But the light was on.\nI broke the door and rushed into the living room.\nHe was lying on the floor, dead, just as what you see right now. I called the police immediately.'", fg="black")
        character1Story.pack()
    
    def character2(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "‘…I was out of town to pick up my custom wedding dress yesterday at 10 am and came back at 8 pm. I then went to a cafe and stayed there until a police called me and I…’ She couldn’t speak, starting to sob. ", fg="black")
        character1Story.pack()

    def character3(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "‘I was at home, watching TV with my neighbor all night.’", fg="black")
        character1Story.pack()

    def character4(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "‘I was at my office with my assistant.’", fg="black")
        character1Story.pack()

    def door(self):
        if "key" not in self.itemsCarrying:
            self.middleFrameDesc.destroy()
            self.middleFrameDesc = tk.Frame(self.master)
            self.middleFrameDesc.pack()
            tk.Label(self.middleFrameDesc, text = "You can't open it without a key", fg="black").pack()
        else:
            endWindow = tk.Toplevel(self.master)
            mixer.music.load("end.mp3")
            mixer.music.play(-1)
            tk.Label(endWindow, text = "You open the door and find out Hannibal is staring at you straightly in the 3D world...\nWell, good luck and have a fantastic life.", fg = "black").pack()
            img = Image.open("end.png") 
            img = ImageTk.PhotoImage(img) 
            image = tk.Label(endWindow, image = img)
            image.image = img 
            image.pack()
            tk.Button(endWindow, text = "What the heck!??", fg = "black", command = self.quit).pack()
    
    def item1(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "You pick up the piece of paper on the floor.\nThere are few hand-written words, 'Movie night at 6—old movie from high school—S.'\nIt seems to be a man's handwriting.", fg="black")
        character1Story.pack()

    def item2(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "Just a stick. You put it into your bag(click the 'bag' button to see the items you are carrying)", fg="black")
        character1Story.pack()
        if "t" not in self.itemsCarrying:
            self.itemsCarrying = self.itemsCarrying + " a stick\n"


    def item3(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "The cop tells you when they arrived at the house. It was deadly cold and the thermometer reads -30℃.\nWell...this is beyond weird ", fg="black")
        character1Story.pack()

    def item4(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "The station board shows the train K’s fiancee was in arrived at 8 pm so part of her testimony is confirmed.", fg="black")
        character1Story.pack()

    def item5(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "All of a sudden, a huge beast, as quick as a flash of black lightning, jumps on you. His white, sharp teeth is about to cut your throat…\nAll at once, he stops. He sniffs at your hair, and glimpse his master — Mr. Sunwood — with a frightening look, and then quickly ran away.\nYou are petrified. Mr. Sunwood, embarrassed, apologizes to you forever. You observe this seemingly average man in silence, reconsidering every words he said. ", fg="black")
        character1Story.pack()

    def item6(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "Mr.Sunwood says the reason why his wigs could make such a grand success is just simply setting a high standard of quality— no one can distinguish his wigs from real hair.", fg="black")
        character1Story.pack()

    def item7(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "An old photo of K in high school. Looking at the background, it seems to be taken in Japan.\nInteresting…isn't this incompatible with someone’s words? ", fg="black")
        character1Story.pack()

    def item8(self):
        self.middleFrameDesc.destroy()
        self.middleFrameDesc = tk.Frame(self.master)
        self.middleFrameDesc.pack()
        character1Story = tk.Label(self.middleFrameDesc, text = "A pair of earrings. You put them into the bag, planning to ask Miss E whether she is the owner.", fg="black")
        character1Story.pack()
        if "p" not in self.itemsCarrying:
            self.itemsCarrying = self.itemsCarrying + " a pair of earrings\n"

    def event(self):
        chosen = random.choice(self.eventList)
        chosen()
        self.eventList.remove(chosen)



    def answer(self):
        self.answerWindow = tk.Toplevel(self.master)
        tk.Button(self.answerWindow, text = "The bodyguard", fg = "black", command = self.wrong).pack()
        tk.Button(self.answerWindow, text = "Miss E", fg = "black", command = self.right).pack()
        tk.Button(self.answerWindow, text = "Mr. Sunwood", fg = "black", command = self.wrong).pack()
        tk.Button(self.answerWindow, text = "The doctor", fg = "black", command = self.wrong).pack()
    
    def wrong(self):
        loseWindow = tk.Toplevel(self.answerWindow)
        tk.Label(loseWindow, text = "Unfortunately, you are wrong. You will be stuck in this crazy world forever(maybe this is not too bad as the 3D world is only crazier).", fg = "black").pack()
        tk.Button(loseWindow, text = "quit", fg = "black", command = self.quit).pack()

    def right(self):
        self.winWindow = tk.Toplevel(self.answerWindow)
        tk.Label(self.winWindow, text = "Congrats! You are right! Now you will get the key of the locked door.", fg = "black").pack()
        tk.Button(self.winWindow, text = "Get the key!", fg = "black", command = self.key).pack()

    def quit(self):
        self.master.quit()
    
    def key(self):
        self.itemsCarrying += "the key\n"
        self.winWindow.destroy()
        self.answerWindow.destroy()

    def eventCalled(self):
        self.eventWindow = tk.Toplevel(self.master)
        self.eventDes = tk.Frame(self.eventWindow)
        self.eventDes.pack(fill = tk.X)
        self.eventChoice = tk.Frame(self.eventWindow)
        self.eventChoice.pack(fill = tk.X)
    
    def eventUpdate(self):
        self.eventDes.destroy()
        self.eventDes = tk.Frame(self.eventWindow)
        self.eventDes.pack(fill = tk.X)
        self.eventChoice.destroy()
        self.eventChoice = tk.Frame(self.eventWindow)
        self.eventChoice.pack(fill = tk.X)

    def logicUp(self):
        self.logic += 10 
        self.status()
        self.eventWindow.destroy()
        if self.logic == 20:
            logicHelp = tk.Toplevel(self.master)
            tk.Label(logicHelp, text = "1.Why would K hire a bodyguard just two weeks ago?").pack()
        if self.logic == 30:
            logicHelp = tk.Toplevel(self.master)
            tk.Label(logicHelp, text = "1.After arriving at town, Miss E does not go back home immediately but went to a cafe. Who would have coffee alone at night? Especially when she was carrying her wedding dress.Doesn't it look like she was waiting for the call?.\n2.Because the room temperature when the body was discovered was extremely low, it is hard to tell when K was killed according to the appearance of the body.\n3.The note you found on the floor. Noted 'high school' and 'S'. Mr. Sunwood went to high school with K and 'S' is his initial. If it was Mr.Sunwood, would he be that stupid to leave such evidence at the scene?").pack()
        if self.logic == 40:
            logicHelp = tk.Toplevel(self.master)
            tk.Label(logicHelp,text = "1.Noted 'hair' and 'woman' plays an important part in the whole story. The wig store, the beautiful hair of Miss E. The woman's earrings, and the dog's weird behavior.\n2.Why would K trust an inexperience med school graduate for no reason? Is it possible it is because he wanted the young man to keep a secrete for him?").pack()
    def insightUp(self):
        self.insight += 10
        self.status()
        self.eventWindow.destroy()
        if self.insight == 20:
            insightHelp = tk.Toplevel(self.master)
            tk.Label(insightHelp, text = "Mr. Sunwood and Miss E are hiding something. And they obviously hate each other.")
        if self.insight == 30 and self.logic == 20:
            insightHelp = tk.Toplevel(self.master)
            tk.Label(insightHelp, text = "Mr. Sunwood is a dark, terrible man. But sometimes a good person would kill and a bad person might be innocent.").pack()
        if self.insight == 40:
            insightHelp = tk.Toplevel(self.master)
            tk.Label(insightHelp, text = "Miss E hates and loves K at the same time. And such feelings sometimes cause killing.")

    def sympathyUp(self):
        self.sympathy += 10
        self.status()
        self.eventWindow.destroy()
        if self.sympathy == 40:
            sympathyHelp = tk.Toplevel(self.master)
            tk.Label(sympathyHelp, text = "Miss E finds you and starts to talk:'You are a good man. Please kill me so you can escape form this world. Yes, I killed K, my beloved fiancé. Because he is a psycho! A true murderer!\nSir, please let me tell you my story.\n I met K one year ago and fall in love with him immediately. He was sweet and charming. I loved him so much that I accepted his proposal without knowing much about him.\nHe seldom talked about his past and only said his parents died from a car accident and he left Japan to Germany.\nSunwood is his only old friend. I trusted them very much and believed every words they told me.\n Three weeks ago, I found an old photo of K in high school when cleanning the house. It looked like in Japan. I was shocked because K and Sunwood told me K went to high school in Germany.\nI asked K and K said this is the first day in high school and he moved to Germany the next day. But I felt something strange. The clothes K wore looked old and there was something strange about the look on K’s face.\nI called Sunwood and he confirmed K’s words, as he always did.\nSo I decided to trust them -- I am so stupid-- until I found a pair of earrings in the sink, and the earrings are not mine…\nI was terrified. I thought K was cheating on me.\nBut on the other hand, K behaved as usual, and even better, as the wedding is getting closer…\nI suddenly realized I knew nothing about K’s past other than what K and Sunwood told me.\nI just trusted them so much that I never questioned a word of them…\nThe other day K and I were invited by Sunwood to his store. A dog jumped up and was about to bite me. But when he smelled my hair, he walked away.\n I was desperate about the idea that K was cheating on me but I had no one to turn to.\nI found the doctor of K, Dr. Kim, planning to talk to him, but Kim told me K had some sort of mental disease and he’d like to hide. K was fond of women’s hair.\nDr. Kim miscalled me as another lady’s name. K’s ex girlfriend. And Kim apologized, saying we looked similar, especially we both have great hair and he never saw that girl for a while.\nSuddenly, a terrible idea appeared to me: the wigs are not fake hair but real hair, real women hair!!\nThis explains everything: the dog did not bite me because he was trained to eat up bodies w/o hair,\nSunwood used real hair to make wigs so people can’t distinguish his wigs from real hair,\nK did not lost his parents but his parents sent him to a mental hospital when he was young but he escaped,\nK was attractive so he was responsible for attracting women, when he got her, he and Sunwood would kill hertogether and cut her hair off, feeding the dog the body remains,\nand the earrings...they belong to one of the poor woman...\nI decided to kill K and imputed Sunwood. This was the only way I could escape my own death.\nI made K believed someone wanted to kill him so K hired a bodyguard.\nAnd then I left a note with words, trying to impute Sunwood.\nI used a stick to kill K when he was sleeping. After turning the room temperature cold, I left the house and told the bodyguard to protect K while I was away to get my wedding dress.\nI was unable to return to the house alone so after getting off the train, I went to a caffe and waited for the call.").pack()

    def event1(self):
        self.eventCalled()
        tk.Label(self.eventDes, text = "Night falls, people in the house start to take off.\nYou stay there for a bit longer, reflecting the crazy experience in the morning.\nYou are about to leave. But something catches your eyes — Miss E is still sitting on the sofa, but the look on her face changes.\nIt’s now full of sorrow, fragility, loneliness, and fears.\nTears roll down her face. She is like a sitting abyss, bearing something unbearable.\nAll silence. ", fg = "black").pack()
        tk.Button(self.eventChoice, text = "You don't want feelings to interfere with your judgement, so you quickly leave.", command = self.logicUp).grid(row = 0)
        tk.Button(self.eventChoice, text = "You stare at her for few seconds, trying to connect her with the maniac you saw in the morning.", command = self.insightUp).grid(row=1)
        tk.Button(self.eventChoice, text = "You walk up to her, hand her a handkerchief, and sit next to her silently.", command = self.event1Continue).grid(row=2)

    def event1Continue(self):
        self.eventUpdate()
        tk.Label(self.eventDes, text = "Both of you keep silent for a while. You take the earrings from your bag, hand it to her.\nAs she sees the earrings, she seems to recall something awful, subconsciously flinches back.\n The earrings drop down on the floor.\nShe apologizes.\n'Oh thank you, they are not mine...'\nYou two just sit here.\nWhen you are about to leave, she abruptly said, 'You know how much I loved and trusted K...but...Do you think my hair is beautiful? I hate my hair.I hate myself...'", fg = "black").pack()
        tk.Button(self.eventChoice, text = "You confuse, but still say goodbye to her politely.", command = self.sympathyUp).pack()

    def event2(self):
        self.eventCalled()
        tk.Label(self.eventDes, text = "You go to the wig store. Mr.Sunwood welcome you warmly.\n You ask him if it's ok to visit his wig factory. He hesitates for a while and then says yes.\nSo you are on Mr.Sunwood's car. He drives.\nSuddenly, he stops the car and says he thinks of something urgent and needs to go back.", fg = "black").pack()
        tk.Button(self.eventChoice, text = "'Ok, no worries! Your business comes first.'\nHe seems delighted, and starts to tell you stories about K back in high school. They are all wild, bizarre deeds.",command = self.logicUp).pack()
        tk.Button(self.eventChoice, text = "You keep silent, staring at him. He becomes nervous, behaving differently as he met you for the first time.", command = self.insightUp).pack()
        tk.Button(self.eventChoice, text = "You feel suspicious but nod.\nWhen you come back, you visit Miss E' to check if she is better now. You can't forget this lonely and poor woman.", command = self.sympathyUp).pack()

    def event3(self):
        self.eventCalled()
        tk.Label(self.eventDes, text = "The doctor finds you. He says he needs to tell you something.\n'You know...Mr.K is a great man...but great men always have something strange. Maybe it is eccentricity that makes them great.\nI just think this information might be helpful for finding the killer. But I can't say more. I need to be responsible for Mr.K's reputation.", fg = "black").pack() 
        tk.Button(self.eventChoice, text = "You thank him and ask him to look after Miss E.",command = self.sympathyUp).pack()
        tk.Button(self.eventChoice, text = "You lost in thoughts, forget to reply him.", command = self.logicUp).pack()
        tk.Button(self.eventChoice, text = "'It seems that Mr. K is not a simple man...', you think.", command = self.insightUp).pack()

root = tk.Tk()
start = Start(root)
root.mainloop()