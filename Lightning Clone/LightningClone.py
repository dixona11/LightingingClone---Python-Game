import time,sys,os,random
user_name = ""

def type_w(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)
        if char != "\n":
            time.sleep(0.015)
        else:
            time.sleep(1)

def start_game():
    type_w("\nCN JAMS Copyright(c) Presents: ")
    time.sleep(1)
    print("""           
__________________________________________________________________________________________________________________
         .____    .__       .__     __         .__                    _________ .__                        
         |    |   |__| ____ |  |___/  |_  ____ |__| ____    ____      \_   ___ \|  |   ____   ____   ____  
         |    |   |  |/ ___\|  |  \   __\/    \|  |/    \  / ___\     /    \  \/|  |  /  _ \ /    \_/ __ \ 
         |    |___|  / /_/  >   Y  \  | |   |  \  |   |  \/ /_/  >    \     \___|  |_(  <_> )   |  \  ___/ 
         |_______ \__\___  /|___|  /__| |___|  /__|___|  /\___  /      \______  /____/\____/|___|  /\___  >
                 \/ /_____/      \/          \/        \//_____/              \/                 \/     \/ 

     _   _            _                                      __   _   _           _        ______       _ _   
    | | | |          | |                                    / _| | | | |         (_)       | ___ \     | | |  
    | |_| |__   ___  | | ___  __ _  __ _  ___ _   _    ___ | |_  | | | |___  __ _ _ _ __   | |_/ / ___ | | |_ 
    | __| '_ \ / _ \ | |/ _ \/ _` |/ _` |/ __| | | |  / _ \|  _| | | | / __|/ _` | | '_ \  | ___ \/ _ \| | __|
    | |_| | | |  __/ | |  __/ (_| | (_| | (__| |_| | | (_) | |   | |_| \__ \ (_| | | | | | | |_/ / (_) | | |_ 
     \__|_| |_|\___| |_|\___|\__, |\__,_|\___|\__, |  \___/|_|    \___/|___/\__,_|_|_| |_| \____/ \___/|_|\__|
                              __/ |            __/ |                                                          
                             |___/            |___/                                                           
__________________________________________________________________________________________________________________
        """)
    time.sleep(0.5)
    type_w("Welcome to Lightning Clone!") 
    type_w("\nThank you for choosing to play our game.\n")
    type_w("\nThis is the story of how Usain Bolt's Clone came into life.\n ")
    type_w("\nDo you dare to find out about it? [Y] or [N]")
    reply = input("\n> ")

    if reply.upper() == "YES" or reply.upper() == "Y":
        time.sleep(0.5)
        type_w ("Okay, lets move on with the story then shall we?")
        intro()
    
    elif reply.upper() == "NO" or reply.upper() == "N":
        time.sleep(0.5)
        type_w ("\nIt's sad to see you not play this awesomely coded game.")
        type_w ("\nIf you really want to make us feel bad, you can leave now.")

    else:
        time.sleep(1)
        type_w("\nAll I asked you to do was to press Y or N. We have to restart all over again now.")
        type_w("\nPlease press the correct letter this time.")
        time.sleep(2)
        start_game()
        
def intro():

    type_w("\nThe American team wants to stop Usain Bolt from winning the Olympics this year.")
    type_w("\nThey bring in an American Scientist to help sabotage Usain's chances of winning gold medals.")
    type_w("\nThe scientist then clone Usain so his clone will compete in the Olympic Games.")
    type_w("\nThe scientist keep the real Usain locked up in a room under the stadium.")
    type_w("\nThe Jamaican team has noticed that there's a change to Usain's personality, but still enter him into the Games.\n")
    type_w("\nPress Y to choose from the events.")
    reply = input("\n> ")

    if reply.upper() == "Y" or reply.upper() == "YES":
        time.sleep(1)
        type_w("\nUsain demands to compete in the following competitions, to the displeasure of the Jamaican team, lets see how he gets on!\n")
        events()

    else:
        type_w("\nPlease press Y if you want to move forward next time.\n ")
        time.sleep(1.5)
        intro()

def events():
    type_w("\n1. Swimming")
    type_w("\n2. Floor Gymnastics")
    type_w("\n3. Karate")
    type_w("\n4. 100m")
    type_w("\n5. 200m\n")
    type_w("\nChoose one of the events above. Select 1, 2, 3, 4 or 5")
    reply = input("\n> ")
    if reply == "1":
        type_w("\nUsain's team was really concerned at this bizarre request as Usain was known to be the only guy on the team that is not a good swimmer.")
        type_w("\nBut the final decision is still his.\n")
        type_w("\nWhat do you want to do?\n")
        swimming_event()

    elif reply == "2":
        gymnastics_event()

    elif reply == "3":
        karate_event()

    elif reply == "4":
        hundred_meter_event()

    elif reply == "5":
        two_hundred_meter_event()

    else:
        type_w("\nYou entered an invalid character. Please enter the correct character and try again.\n")
        time.sleep(1.5)
        events()

def swimming_event():
    time.sleep(0.5)
    type_w("\n1. I want to compete in the event.")
    type_w("\n2. I want to listen to my team and choose a different event.")
    type_w("\n3. I want to protect this temple of a body with my Onesie.\n")
    type_w("\nSelect 1, 2 or 3.")
    reply = input("\n> ")
    if reply == "1":
        time.sleep (1)
        type_w("\nDespite all the disagreemetnt with the team Usain still decides to enter the swimming event.")
        type_w("\nUsain came to his lane wearing the biggest swimming trunks anyone has ever seen and taunts all the other competitors.")
        type_w("\nWhen the countdown struct 2, Usain got to his usual running position confusing everyone in the arena and began to run on top of the water like a cartoon character, he failed miserably and was disqualified as he started early and used an unusual style.\n")
        time.sleep(1)
        events()

    elif reply == "2":
        time.sleep(1)
        type_w("\nListen to the team and go back to look at the events.\n")
        time.sleep(3.5)
        events()

    elif reply == "3":
        time.sleep(1)
        type_w("\nUsain enters the race and lines up dressed in what seems to be a onesie alongside the rest of the swimmers who are all in their pre match tracksuits.")
        type_w("\nOne of the swimmers looks at Usain from head to toe and smirks and asks 'What is that?'")
        type_w("\nUsain looks back at him and says 'You’ll see.'")
        type_w("\nCompetitors all take off their tracksuits and start doing their pre match rituals.")
        type_w("\nThe officials call everyone to the starting block.")
        time.sleep(1)
        event_begins()

    else:
         type_w("You've entered an invalid character. Please enter the correct character and try again\n") 
         time.sleep(2.5)
         swimming_event()

def event_begins():
        type_w("\nPress Y to see what happens next.")
        reply = input("\n> ")
        
        if reply.upper() == "Y" or reply.upper() == "YES":
            type_w("\nUsain waits for the rest of his rivals to be in position.")
            type_w("\nHowever, Usain doesn't take off his onesie.")
            type_w("\nHe steps up to the starting block and, to the astonishment of the crowd, athletes, and officials, Usain points to himself and shouts out, 'I’ve got to protect this temple of a body!'.")
            type_w("\nUsain jumps into the pool and uses a doggy paddle. Which seemed initially to be working, till his onsie starts filling up with water.")
            type_w("\nUsain then sinks to the bottom of the pool. The Life Guard has to jump in and save him.\n")
            time.sleep(1)
            type_w("\nUsain then decides to try his luck at a different event as he realises swimming is not for him.")
            time.sleep(1)
            events()

        else:
            type_w("You've entered an invalid character. Please enter the correct character and try again\n") 
            time.sleep(2.5)
            event_begins()
        

def gymnastics_event():
    time.sleep(0.5)
    type_w("\nThe music starts playing the stadium is holding their breath in anticipation for Usain Bolts's debut routine.\n")
    type_w("\nI'm a Barbie girl by Aqua, comes blaring out of the speakers.")
    type_w("\nUsain runs out as quick as lighting from behind the curtain wearing a pink tutu over his team tracksuit and he starts displaying a number of rubbish forward rolls on the mat.")
    type_w("\nThe judges are captured in a trance of amazement, Usain ends his routine with a wave to the crowd and a curtsy.")
    type_w("\nUsain is awarded with a bunch of flowers and a medal for trying something new.\n")
    type_w("\nThe Jamaican team is furious at Usain for embarrassing them and enters him into the 200 meters.\n")
    time.sleep(1)
    two_hundred_meter_event()

def two_hundred_meter_event():
    time.sleep(0.5)
    type_w("\nIt's time for the 200m event. Let's see what happens next\n")
    type_w("\nUsain is all geared up to run the competition!")
    type_w("\nThe Jamaican team is standing at the track side with big smiles on their faces as they know Usain is the one to beat.")
    type_w("\nHowever Usain is very confused and unsure of what he should wear on his feet.")
    type_w("\nTo the left of him are wellington boots and to the right of him are somee flip flops.")
    type_w("\nHelp him decide what to wear.\n")
    
    time.sleep(0.5)
    type_w("\nFor Wellington Boots type 'Left' \nFor Flip Flops type 'Right'\n")
    left_or_right = input ("\n> ")

    if left_or_right.upper =="L" or left_or_right.upper()=="LEFT":
        left_path()

    elif left_or_right.upper == "R" or left_or_right.upper()=="RIGHT":
        right_path()
    else:
        type_w("Invalid input try again.")
        two_hundred_meter_event()

def left_path():
    time.sleep(0.5)
    type_w("\nUsain and all the runners are in position waiting for the command to run, the gun fires and Usain refuses to run, sits down on the track and starts to cry because he has a stone in his Wellington boot.")
    type_w("\nHis team pull him off the tracks and shout at him for not running which causes him to cry even more, the team manages to speak to the official to get them to reset the race.\n")
    time.sleep(0.5)
    type_w("\nPress 'Y' to Return to the Race")
    reply = input("\n> ")

    if reply.upper() == "Y" or reply.upper() == "YES":
        time.sleep(1)
        two_hundred_meter_event()

    else:
        type_w("Invalid input try again.")
        two_hundred_meter_event()

def right_path():
    time.sleep(0.5)
    type_w("\nUsain is all set to run the race and is feeling extremely happy with how his feet feel so fresh and airey in his flip flops and he his laughing to himself to why his competitors would want to wear those awful hot sticky trainers..\n")
    type_w("\nThe gun is fired and Usain is off the first one out of the blocks, he gets past the bend and is leading on the home stretch, Justin Gatlin is hot on Usain's heels, then Gatlin's stash of testosterone pills start spilling out onto the track.\n")
    type_w("\nUsain's flop flops get caught up in the spillage and Usain loses his balance and lands before the finishing line.")
    type_w("\nHe lies flat on his back and lands before the finishing line.")
    type_w("Usain's team had to carry him off the track. \nLets see Usain try another event.")
    type_w("\nPress 'Y' to return to the events")
    reply = input("\n> ")

    if reply.upper() == "Y" or reply.upper() == "YES":
        time.sleep(1)
        events()

    else:
        type_w("Invalid input try again.")
        right_path()

def karate_event():

    global user_name

    type_w("\nBolt decides that its time for him to try and conquer the fighting world by entering a Karate match.")
    type_w("\nSince nobody knew what he was capable of, everyone was afraid to have a fight with him.")
    type_w("\nBut then he realises the perfect person to challenge for his karate debut is the person who's playing this game right now.\n")
    type_w("\nSo then tell us what your name is?")
    user_name = input("\n> ")
    type_w("\nWell..well..well.. looks like we have a worthy opponent.\nSo {}, do you actually think you have a chance against Bolt?".format(user_name.capitalize()))
    type_w("\nType Yes or No")
    reply = input("\n> ")
    if reply.upper() == "Y" or reply.upper() == "YES" or reply.upper() == "YEAH":
        type_w("\nThere is no way on earth you can win against bolt.")
        type_w("\nSince this match is one in a million, the olympic committee decided to make it the main event.")
        type_w("\n{} vs Usain Bolt. Amateur Rookie vs Professional Rookie. Who will come out victorious?\n".format(user_name.capitalize()))
        type_w("\nDING! DING! DING!")
        type_w("\nThe long awaited match begins.")
        type_w("\nYou really want to get the upper hand early on by going first. What are you going to do?")
        fighting_choices()

    elif reply.upper() == "N" or reply.upper() == "NO" or reply.upper() == "NOPE":
        type_w("\nYeah, thats what we thought.")
        type_w("\nOh well, can't blame you anyway.")
        time.sleep(0.6)
        type_w("\nPlease go back and pick another event for bolt because you chickened out.")
        events()
    else:
        type_w("\nIt's just a normal YES or NO question. How hard is it to type that?\nBack you go.\n")
        time.sleep(1)
        karate_event()

def fighting_choices():
        
        type_w("\n1. High Kick")
        type_w("\n2. High Punch")
        type_w("\n3. Flying Roundhouse Kick")
        type_w("\n4. Groin Kick")
        type_w("\n5. One inch Punch\n")
        type_w("\nSelect how you want to attack.")
        reply = input("\n> ")

        if reply == "1" or reply.upper() == "HIGH KICK":
            high_kick()

        elif reply == "2" or reply.upper() == "HIGH PUNCH":
            high_punch()
        
        elif reply == "3" or reply.upper() == "FLYING ROUNDHOUSE KICK":
            flying_kick()

        elif reply == "4" or reply.upper() == "GROIN KICK":
            groin_kick()

        elif reply == "5" or reply.upper() == "ONE INCH PUNCH":
            one_inch_punch()

        else:
            type_w("\nInvalid characted entered. Choose the correct number from the list and enter next time.")
            time.sleep(1)
            fighting_choices()
        

def high_kick():
    outcomes = ["\nIt misses and you lost your balance.", 
    "\nIt hit him right in the face. Very effective and Usain is feeling dizzy already.",
    "\nIt barely hit him, and now Usain has the upper hand."]

    response = random.choice(outcomes)
    type_w(response)

    if response == outcomes[0]:
        type_w("\nYou're almost about to fall and Bolt take advantage of this and kicks you right in the face.")
        type_w("\nYou get knocked the hell out. You're floored and the crowd goes off.")
        type_w("\nBolt have one leg up on your body and does his famous Lightning pose.\n")
        time.sleep(2)
        type_w("\nYou wake up 5 days later and you have no memory of anything.")
        type_w("\nYou don't even remember playing this game.")
        type_w("\nAnd you're wondering why you're still seeing these messages...\n")
        time.sleep(3)
        forget_option()

    elif response == outcomes[1]:
        type_w("\nBolt is having a hard time finding his balance.")
        type_w("\nYou then take it to your advantage and do a sweep kick.")
        type_w("\nBolt collapses on the floor and the crowd goes completely silent.")
        type_w("\nAfter about 10 seconds. The crowd went {}.. {}.. {}!!".format(user_name.upper(),user_name.upper(),user_name.upper()))
        type_w("\nYou win an award for showing excellent sportmanship and for beating Usain Bolt.\n")
        time.sleep(2)
        print("""
                                      ___________
                                 .---'::'        `---.
                                (::::::'              )
                                |`-----._______.-----'|
                                |              :::::::|
                               .|               ::::::!-.
                               \|               :::::/|/
                                |                :::::|
                                |    Special Award :::|
                                |  for Beating Bolt ::|
                                |               ::::::|
                                |              .::::::|
                                J              :::::::F
                                 \            :::::::/
                                  `.        .:::::::'
                                    `-._  .::::::-'
    ____________________________________|  '''|''_________________________________________
                                        |  :::|
                                        F   ::J
                                       /     ::\                                        
                                  __.-'      :::`-.__
                                 (_           ::::::_)
                                   `'''---------''''
            """)
        time.sleep(3)
        forget_option()

    else:
        type_w("\nUsain throws a right jab at you. You dodge it.")
        type_w("\nAnd then you hit him with a right uppercut and he dodges it as well.")
        type_w("\nThe fight goes evenly matched for about 2 hours.")
        type_w("\nBolt's clone powers started to wear off and slow him down.")
        type_w("\nYou immedietely take advantage of it, and kicks him right in his chest.")
        type_w("\nHe goes flying outside the ring. And you collapse right after that.\n")
        time.sleep(2)
        type_w("\nYou wake up the next day in a hospital, and you see your name on the news.")
        type_w("\nIt said the entire match is a world record for the longest karate match in history.")
        type_w("\nAnd a special video made just for you.")
        type_w("\nOverwhelmed by all this. You look to your right, you see the award presented to you after the game and decides to close your eyes with a smile.")
        time.sleep(1)
        type_w("\nYou wake up the next day and realises that everything was a dream and how your life is still a disappointment.")
        time.sleep(3)
        end_scene()

def high_punch():

    outcomes = ["\nYou panicked and hit Bolt with a Left Jab.", 
    "\nYou feel like you've worked your whole life for this and hit Bolt with the hardest Right Jab you ever could.",
    "\nRight when you're about to hit him with with a high punch, Bolt hits you right in your face before you could even react."]

    response = random.choice(outcomes)
    type_w(response)

    if response == outcomes[0]:
        type_w("\nAs you're Righty, your Left Jab lacks power. Bolt recovers from it very easily.")
        type_w("\nBolt comes running in lightning fast and hits you with a Flying Roundhouse Kick.")
        type_w("\nYou get knocked back to last week. Bolt becomes the victor and goes back to try some other events.\n")
        time.sleep(2)
        events()
    
    elif response == outcomes[1]:
        type_w("\nBolt falls down like a tree.")
        type_w("\nBolt doesn't seem like he's going to get up anytime soon.\nThe Referee counts down to 10.")
        type_w("\nThe crowd goes insane seeing your strength and capabilities.\n")
        type_w("\nYou were then presented with an award.\n")
        time.sleep(1)
        print("""
              (_v_)                   
               _|_                    
               | |                    
          |-----+-----|                
          |  SPECIAL  |               
          |   PRIZE   |                
           '---------'                   
            \       /                  
             '.   .'                   
               | |                     
              .' '.               
             _|___|_                  
            [#######]             
        """)
        time.sleep(1.5)
        forget_option()

    else:
        type_w("\nYou get knocked out immedietely and it becomes the shortest match in the history of Karate.")
        type_w("\nBolt then decides that he is the Best Karate Champion in the world and decides to give other events a try.\n")
        time.sleep(2)
        events()

def groin_kick():
    type_w("\nKicking people in the groin is un-ethical and illegal in professional matches. You should know better than that.")
    type_w("\nGo back and change your answer, you dirty fighter.\n")
    time.sleep(1)
    fighting_choices()

def one_inch_punch():
    type_w("\nYou decided to use Bruce Lee's Ultimate ONE-INCH-PUNCH on Bolt hoping that would impress the crowd.")
    type_w("\nBut you accidentally put too much power in and punch him way hard that he flys across the arena.")
    type_w("\nYou could almost see flying birds on top of his head and he is knocked out for good.")
    type_w("\nCrowd began to chant {}...{}...{}!!!".format(user_name.upper(),user_name.upper(),user_name.upper()))
    type_w("\nBut you were disqualified for using too much power.")
    type_w("\nNobody should be allowed to be that good.\n")
    type_w("\nGo back to the events so that we can forget about this whole thing and actually let Bolt do his thing.\n")
    time.sleep(0.5)
    events()

def flying_kick():
    outcomes = ["\nYou go for the high kick and Usain dodges it perfectly.",
    "\nDo you actually think your lousy fly kick would have any effect on this 6ft 5in behemoth of a man?",
    "\nYou chicken out at the last second and decides to go for a high kick instead."]

    response = random.choice(outcomes)
    type_w(response)

    if response == outcomes[0]:
        type_w("\nYou lose your balance when you hit the ground, falls down and knock yourself out.")
        type_w("\nUsain Bolt becomes the only victor in the history of Karate matches to win a match without ever having to lift a finger.")
        type_w("\nBolt then goes on to try other events.\n")
        time.sleep(2)
        events()

    elif response == outcomes[1]:
        type_w("\nI mean come on, you're better than this.")
        type_w("\nPlease don't embarass yourself in front of millions and millions of people.")
        type_w("\nGo back and please make better life decisions!")
        time.sleep(2)
        fighting_choices()

    else:
        high_kick()

def hundred_meter_event():
    time.sleep(0.5)
    type_w("\nThe 100m final is about to begin and Usain is favourite to win yet another Gold.")
    type_w("\nBut just as the event is about to start, the Jamaican team hears a cry for help from the American Team’s Dressing room.")
    type_w("\nWhat are they are going to do?\n")
    type_w("\n1. The Jamaican team tell the Official Olympic Security.")
    type_w("\n2. The team goes and check it themselves.\n")
    type_w("\nSelect 1 or 2 from above.\n")
    reply = input("\n> ")

    if reply == "1":
        ending_one()

    elif reply == "2":
        time.sleep(0.5)
        type_w("\nThey were not allowed to enter another teams dressing room and were denied entrance to check it out.")
        ending_two()

    else:
        type_w("\nYou entered an invalid character. Please enter the correct character and try again.\n")
        time.sleep(3.5)
        hundred_meter_event()

def ending_one():
    time.sleep(1)
    type_w("\nThe Jamaican team warns the Official Olympic Security about it and they pass it on to the relevant authorities.")
    type_w("\nThe officials then decide to disqualify the entire American team.")
    type_w("\nBut since the Cloned Usain bolt was a good sport and due to the crowd’s extreme overreaction to seeing two Usain Bolt’s at the same time, they decide to have a 1 on 1 race, Usain Bolt vs Cloned usain bolt.")
    type_w("\nUsain Bolt himself was in a shock to see an exact replica of himself and decides to take on the challenge to the see whos the better version.")
    type_w("\nAs the cloned bolt is only an experimental clone and still not up to par with actual humans, his bolt powers were extremely limited.")
    type_w("\nDuring the middle of the race, the clone ran out of his powers and collapsed on the ground making the real Usain bolt the victor.\n")
    time.sleep(1)
    print("""
         _______________
        |@@@@|     |####|
        |@@@@|     |####|
        |@@@@|     |####|
        \@@@@|     |####/
         \@@@|     |###/
          `@@|_____|##'
               (O)
            .-'''''-.
          .'  * * *  `.
         :  *       *  :
        : ~  G O L D ~  :
        : ~ M E D A L ~ :
         :  *       *  :
          `.  * * *  .'
            `-.....-'
    """)

    end_scene()

def ending_two():
    time.sleep(0.5)
    type_w("\nThe 100m event starts as its supposed to. The clone participates and wins as he was intended to.")
    type_w("\nThe team did not bring up the situation about the cry for help thereafter.")
    type_w("\nAfter the event ended, they went back home with the cloned Usain and replaced the real Usain forever.\n")
    end_scene()
    

def end_credits():
    time.sleep(1)
    type_w("\n  This game was created by: \n")
    type_w("""
    ...*Andrew...
    ...*John...
    ...*Sharmaine...
    ...*Malith...
    """)

def new_game():
    time.sleep(1)
    type_w("\nHope you find a different ending this time.")
    type_w("\nYou're new game will start in 3 seconds...")
    time.sleep(3)
    start_game()

def end_scene():
    type_w("\nTHE END!")
    type_w("\nThank you for playing our game.")
    type_w("\nWould you like to stop here or play again?")
    type_w("\n1. Stop here.")
    type_w("\n2. Play Again.\n")
    type_w("\nSelect 1 or 2.")
    reply = input("\n> ")

    if reply == "1":
        end_credits()

    elif reply == "2":
        new_game()

    else:
        time.sleep(1)
        type_w("\nYou messed it up again. I thought you would have learnt by now. PLEASE SELECT 1 OR 2 LIKE A NORMAL HUMAN BEING.")
        time.sleep(3)
        ending_two()

def forget_option():
    type_w("\nDo you want to forget everything that happened till now in Karate, go back and choose a different option?")
    type_w("\nSelect Yes or NO.")
    reply = input("\n> ")

    if reply.upper() == "Y" or reply.upper() == "YES":
        type_w("\nWe thought you might choose it.")
        type_w("\nNow go back and change your destiny.\n")
        time.sleep(1)
        fighting_choices()

    elif reply.upper() == "N" or reply.upper() == "NO":
        type_w("\nI know nobody wants to go through that ever again.")
        time.sleep(1)
        end_scene()

    else:
        type_w("\nInvalid characted entered. Choose the correct number from the list and enter next time.")
        time.sleep(1)
        forget_option()

start_game()