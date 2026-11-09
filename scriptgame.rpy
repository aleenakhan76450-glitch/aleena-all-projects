

init python:
    renpy.music.register_channel("text_voice", mixer="voice", loop=True, tight=True)

    def cartman_talk(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/cartmanv.wav", channel="text_voice", loop=True)
        elif event == "end":
            renpy.sound.stop(channel="text_voice")

    def kyle_talk(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/kylev.ogg", channel="text_voice", loop=True)
        elif event == "end":
            renpy.sound.stop(channel="text_voice")

    def stan_talk(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/stan_voice.mp3", channel="text_voice", loop=True)
        elif event == "end":
            renpy.sound.stop(channel="text_voice")
    
    def kenny_talk(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/kenny_voice.mp3", channel="text_voice", loop=True)
        elif event == "end":
            renpy.sound.stop(channel="text_voice")
    
    def pc_talk(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/pcv.mp3", channel="text_voice", loop=True)
        elif event == "end":
            renpy.sound.stop(channel="text_voice")

    def streibel_talk(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/voice_streibel.wav", channel="text_voice", loop=True)
        elif event == "end":
            renpy.sound.stop(channel="text_voice")

define c = Character('Cartman', color="#FF474C", callback=cartman_talk)
define k = Character('Kyle', color="#379737", callback=kyle_talk)
define s = Character('Stan', color = "#4169E1", callback=stan_talk)
define ke = Character('Kenny', color = "#ed5b25", callback=kenny_talk)
define p = Character('PC Principal', color = "#FFFF00", callback=pc_talk)
define ms = Character('Mrs Streibel', color = "#d747ff", callback=streibel_talk)


image kyle normal = "kylenormal.png"
image kyle happy = "kylehappy.png"
image kyle think = "kylethink.png"
image kyle sad = "kylesad.png"
image kyle angry = "kyleangry.png"
image school = "school.jpg"
image car = "car.jpg"
image busstop = "busstop.png"
image croom = "croom.jpg" 
image pcoffice = "pc.jpg"
image artroom = "artroom.jpg"
image lunchroom = "lunch.jpg"
image cartman placeholder = At("EricCartman.png", Transform(size=(400, 600)))
transform fit_screen:
    xsize config.screen_width
    ysize config.screen_height
transform kyle_position:
    zoom 0.25
    xalign 0.1
    yalign 1.0
transform cartman_position:
    zoom 1.5
    xalign 0.9    
    yalign 1.0
default go = False
default truth = False
default friendship_points = 3
default inventory = []


label start:

    play music "audio/bg.mp3"

    show screen display_stats
    show screen global_inventory_action

    scene school at fit_screen

    show cartman placeholder at cartman_position

    c "Hey Kahl, lemme guess. Coming from calc arent ya? Nerdy Jew."

    show kyle think at kyle_position
    
    k "Shut up fatass..."

    "I can't bring myself to tell him the truth..."

    show kyle normal at kyle_position

    k "Can you give me a ride? Kenny stole my car and I'm sure he wrecked it"

    c "Sure asshole, but remember you totally owe me for this!"

    scene car at fit_screen

    show cartman placeholder at cartman_position

    c "What's with you, got sand up your vag again?"

    show kyle sad at kyle_position

    k "What?"

    c "Well obviously SOMETHING's got your jew panties in a twist, hmm?"

    c "You've been sulking all day! It's no fun to rip on you."

    "How the hell did he figure out? Not even Stan or Kenny realised it"

    show kyle think at kyle_position

    "Should I tell him the truth?"

    menu:

        "Tell Cartman the truth.":
            $ friendship_points += 2
            jump truth

        "Lie and tell him its ok.":
            $ friendship_points -= 1
            jump lie

    label truth:

        $ truth = True

        show kyle sad at kyle_position
        show cartman placeholder at cartman_position

        k "Cartman, there's something that's really been on my mind lately. Something I can't even tell Kenny or Stan."

        jump confess

    label lie:

        $ truth = False

        show kyle normal at kyle_position
        show cartman placeholder at cartman_position

        k "Nothing important. Just senior year jitters I guess."

        jump hide

    label confess:
        show cartman placeholder at cartman_position

        c "Oh? What could you be hiding that is so incriminating, Kahl?"

        c "Did your moral sense of justice finally collapse? Did you finally go full jersey (as if u didn't go full cartman on ur dad and half brother?)"

        show kyle angry at kyle_position

        k "NO YOU IDIOT! GODDAMMIT!"

        c "Relax, Kahl, I was only teasing of course."

        c "So, what is it then? What's got you looking like Stan after Wendy dumped his ass again?"

        show kyle sad at kyle_position

        k "Are we in a game dude?"

        k "Are we like, some 2 old guys' characters that a fangirl used to make a game for?"

        k "Cos that would be like, really freaking stupid, dude."

        c "Did someone hit you on the head, Kyel?"

        show kyle think at kyle_position

        k "Shut up! It just feels weird..."

        k "Almost like I'm.. A character in someone else's story"

        c "Oh I get it. It's that rake bullshit from when we were playing tooth fairy"

        c "Every once in a while, you doubt that you're ALIVE"

        c "There's like, an episode on this or something (tooth fairy's tats 2000 s4 ep1)"

        c "You know, for the valedictorian of the grade or whatever, you're kinda stupid dude."

        show kyle angry at kyle_position

        k "SHUT THE HELL UP FATASS! YOU'RE PROBABLY TOO HEAD EMPTY TO EVEN HAVE THESE THOUGHTS!"

        k "I TRIED TO CONFIDE IN YOU! DO YOU ENJOY THIS? ARE YOU A SADIST ASSHOLE?"

        k "WHO AM I KIDDING? OF COURSE YOU ARE! HOW STUPID WAS I TO THINK YOU WOULD COMFORT ME?"

        c "So Kahl, you feel better now?"

        c "I feel like this plot has been way overused now."

        c "If we really WERE in a game, the programmer wouldn't be this stupid, dude."

        show kyle think at kyle_position

        k "Wait..."

        "Why does he have a point? A programmer for a complex game wouldn't be able to do everything herself without it being straight ass!"

        c "Told ya, if anything YOU'RE the sadist, relieving stress from yelling at others!"

        show kyle normal at kyle_position

        k "You know what? You're a stupid fatass and everything,"

        c "EY, SHUT UP JEW!"

        show kyle happy at kyle_position

        k "But you're not a bad friend"


        if truth:
            jump truth_end  
        else:
            jump lie_end  



    label hide:

        show kyle think at kyle_position

        k "I think I'm just scared dude."

        show cartman placeholder at cartman_position

        c "Scared of what?"

        show kyle sad at kyle_position

        k "To graduate"

        c "Yeah, no one at Nerdston will be able to rip on you like I do"

        show kyle angry at kyle_position

        k "SHUT THE HELL UP!"

        jump lie_end


    label truth_end:

        show cartman placeholder at cartman_position

        c "Well thanks, jew!"

        c "I still hate you though."

        show kyle normal at kyle_position

        k "Feeling is ALWAYS mutual fatass."

        c "Sooo.. wanna come over and play brawl stars with me? I have snacks"

        show kyle happy at kyle_position

        k "Sure, If your ass doesn't EAT all the snacks!"

        c "EY! Be thankful I'm even LETTING you into my house!"

        c "It'll take a team of scientists to remove the Jersey stench from my basement (axl heck = cartman canon?)"
        #this line is a DIRECT reference to what axl says to sue in The Middle someone pls someone get it bro

        show kyle normal at kyle_position

        k "The jersey stench is like a DREAM compared to your fatso smell."

        c "Alright jew, I take back my offer! Now go home and die!"

        k "If you wanted me to die, you woul've done it a LONG TIME AGO FATSO!" 

        k "You aren't fooling anyone!"

        k "And how did you get brawl on xbox anyway? that literally isnt possible!"

        c "Some ninth grade indian chick in Singapore. Posting all this shit on tiktok for the FBI to see too!"
        #the point of this joke is that you phyisically cannot play brawl on xbox, im just showing yall that cartman is not always smart lmao
        #the other point of this joke is that i am stupid and tried to emulate tomodachi on my old ass laptop and expected it to work
        #my laptop crashed. twice.
        k "Oh please, I bet she learned all these tricks from her teacher! Must be some coffee-loving guy for sure."
        #mr ken this is a reference to you please get i hope it was funny

        jump truth_part2

    label lie_end:

        show cartman placeholder at cartman_position

        c "Alright now go back to Jew manor!"

        c "Go relax or something! You already got INTO college dude! Early descision too!(this is overused as hell but its ok shut up)"

        show kyle normal at kyle_position

        k "Thanks fatass... BUT THIS DOES NOT MEAN A TRUCE!"

        c "Of course, jew! Ripping on you is indeed my favorite hobby"

        show kyle happy at kyle_position

        k "Not that you're smart enough to have any others!"

        c "EY! SHUT UP!"

        "I will figure you out someday, Kahl, the only one you can't fool is me..."

        jump lie_part2

    label truth_part2:

        scene croom at fit_screen

        show kyle happy at kyle_position

        k "Your house is a pigsty as usual, dude."

        k "Do you ever clean?"

        show cartman placeholder at cartman_position

        c "Shut up jew, at least I'm letting you in!"

        c "It's only because you would go totally batshit crazy alone with your own thoughts otherwise."

        show kyle angry at kyle_position

        k "You make me sound like I'm some kind of patient!"

        c "Yeah, yeah, whatever. Now stop whining and pass me the controller."

        k "YOU totally started it! I was just defending myself."

        c "Keep wasting time and your bitchy jew mom will totally rip me a new one."

        c "Aren't you supposed to be at some gay prep school anyway?"

        show kyle think at kyle_position

        k "It's CRAM school. And that ended 2 weeks ago!"

        k "At least try to keep track of my whearabouts!"

        c "Oh please jew, I know your schedule by heart."

        c "Do you not remember how I used to record every little thing you said to me when we were younger?"

        show kyle angry at kyle_position

        k "You don't still have that, do you?"

        c "Of course not Kahl, have I ever been sentimental?"

        hide kyle
        hide cartman

        "They played on the XBOX until Liane offered to have Kyle stay over for dinner"

        "That was when Kyle realised he was probably late and that Sheila would not be too happy with him for it."

        "The phone with the recordings sat in Cartman's bedroom drawer, even after all those years he never let it go."

        show kyle normal at kyle_position

        k "Again fatass, thank you for today."

        show kyle happy at kyle_position

        k "I mean it."

        c "Yeah, Yeah, no problem Jew. You're totally insane by the way"

        show kyle normal at kyle_position

        k "You're not any better."

        jump bus_stop


    label lie_part2:

        scene croom at fit_screen

        "Eric lied on his bed, coming up with any plausible theory for his questions."

        "On his desk sat a crap ton of homework and coursework he had due the next morning, but he had his priorities."

        show cartman placeholder at cartman_position

        c "What could Kahl possibly be hiding?"

        c "It can't be his coursework for sure, I know he never paid it too much mind. Even though he is a tryhard."

        c "Could it be his bitchy parents? No. They're too busy hounding the mini jew."

        "Eric then had a theory. A very weird theory. But a theory that finally made some sense."

        c "OH MY GOD"

        c "He must be having a jew crush! That dumbass must be having real HUMAN feelings!"

        #Developer note: I got really stupidly lazy and I have no idea how or what to write anymore."
        #Take this as a parody on those really cliche dating sims or something, i lowkey gave up. its corny but not intentionally"

        "Eric could not be more wrong (is he ever right tbh?)"

        jump bus_stop

    label bus_stop:

        scene busstop at fit_screen

        "Stan and Kenny were chatting idly and the bus stop next morning"
        "As Kyle walks up to the bus stop, he notices some jingling sounds in his pocket"

        menu:

            "Keep Stan's forgotten Hall Pass.":
                $ inventory.append("Hall Pass")
                "Kyle saved up the Hall Pass. Might let him sneak around later."

            "Keep Kenny's leftover dollar bill. (Why does kenny have unspent money to begin with?).":
                $ inventory.append("One Dollar")
                "Kyle saved the crumpled dollar bill. Kenny probably won't live long enough to miss it anyway."

            "Empties his pockets":
                "Why do I have so much crap in here anyway??"

        s "And that's why ninjas ARENT gay, Kenny!"

        ke "Mrphm mrmph prhm (Ok Stan, I never said I disagree...)"

        "It was then where Cartman and Kyle decided to start another argument."

        "About something totally stupid, of course."

        show cartman placeholder at cartman_position

        c "Are you serious Kahl? You already accepted it!"

        c "JERSEY JINGER JEW!"

        show kyle angry at kyle_position

        k "I am NOT a Jersey Jew! You can't even spell ginger! At least get it right!"

        c "Of course you are! You're from jersey, you're a jew and you're literally GOING to jersey for college!"

        menu: 
            "Bribe Kenny to back Kyle up" if "One Dollar" in inventory:
                $ inventory.remove("One Dollar")
                $ friendship_points += 1
                k "Pst, Kenny! I'll give ya a dollar to get cartman to shut up!"
                ke "Mphrm! (Heck yeah, a whole dollar!)"
                ke "Mrpm Prhm prhmp! (At least he's going to college!)"
                "Cartman punches Kenny playfully, but still with some force"
                "Kenny often liked to play dead, if it meant that kyle and cartman would stop fighting sometimes!"
                s "Oh my god, Cartman killed Kenny!"
                k "You bastard!"
                k "No wonder no college accepted a violent idiot like you!"

            "Keep arguing.":
                k "At least i'm going to college!"

        c "EY! It's by CHOICE! Not because I couldn't!"

        k "Oh please! We all know why your dumbass isn't going to college!"

        k "It's because you only game, eat and think up weird scenarios at night instead of doing your work!"

        c "HEY! You're as bad as me! You're only on top of your work cos your mom is always hounding ya!"

        show kyle think at kyle_position

        k "And look where I am now! I'm getting out of this shithole while you stay here forever!"

        "Cartman paused for a second"

        c "Shut the hell up, KAHL!"

        k "You shut up, FATASS!"

        "Stan and Kenny sighed and tuned them out as this was practically the normal for them"

        "They and everyone else in South Park were impervious to the fights Cartman and Kyle would have (Seriously, though, I can name the amount of episodes.)"

        "After the 2 settled down, they all said their goodbyes and headed to class."

        jump after_class

    label after_class:

        scene school at fit_screen

        "Kyle was heading back to his locker."
        "He had forgotten his books and wouldn't have an old, cranky Garrison scream at him for it again"

        show cartman placeholder at cartman_position

        c "Hey jew, wait up."

        show kyle think at kyle_position

        k "Cartman? Don't you know that class starts in 5?"

        c "Yeah whatever. It's not like I care."

        show kyle normal at kyle_position

        k "Fine. Expected from you. What do you want?"

        c "I wanna talk to you about something important. I think it would require more than 5 though."

        show kyle think at kyle_position

        k "You want me to bunk class with you? Are you serious"

        c "Yeah. I am."

        "Cartman has never sounded more serious before, but Garrison would hire hitmen to jump me if I bunk again."
        "Should I go with him? He hasn't been too annoying lately anyway..."


    menu:

        "Bunk with Cartman.":
            $ go = True
            $ friendship_points += 2
            jump go

        "Brush him off and head to class.":
            $ go = False
            $ friendship_points -= 1
            jump stay

        "Show Garrison the Hall Pass to excuse yourself." if "Hall Pass" in inventory:
            "Fine wait, let me show that old hag the pass so I can leave."
            $ inventory.remove("Hall Pass") 
            $ go = True 
            $ friendship_points += 1
            "Kyle showed stan's crumpled hall pass at Mr. Garrison. He rolled his eyes and muttered something cranky, but he let Kyle leave."
            jump go


    label stay:

        show kyle normal at kyle_position

        k "Sorry fatass. I actually want to graduate this year."

        show kyle think at kyle_position

        k "Besides, isn't shop one of the classes you LIKE?"

        show cartman placeholder at cartman_position

        c "It could wait. But since you're so BUSY. I'll just leave."

        hide kyle
        hide cartman

        "He stormed off, but Kyle just brushed it off as regular old Eric Cartman"
        "Behaving like a complete toddler when he didn't get what he wanted"

        "Kyle spent the rest of the class wondering what Eri- er Cartman actually needed so bad"

        show kyle think at kyle_position

        k "Could it have been serious?"

        "He almost missed the bell from stewing in his own thoughts, indicating it was time for lunch."

        "And time to face Eric and get some answers."

        jump backclass




    label go:

        scene car at fit_screen

        "Eric and Kyle headed to the parking lot, seemed like it was quiet there after all."

        show kyle think at kyle_position
        
        k "Okay fatso. There better be a good reason you're making me skip Garrison's lecture."

        show cartman placeholder at cartman_position

        c "I'm doing you a favor. His classes suck ass anyway."

        "He seems a bit sad about something... No jersey comments?"
        #wanted to write "jew comments here" but school appropriations said no

        show kyle normal at kyle_position

        k "So? what's up?"

        if truth:
            jump go_truth_response
        else:
            jump go_lie_response

    label go_truth_response:

        show cartman placeholder at cartman_position

        c "Look. I've been thinking a lot about what you said yesterday. And today."

        show kyle think at kyle_position

        k "What did I say?"

        c "Your whole existensial crisis and the...other thing."

        show kyle normal at kyle_position

        k "Well Yeah, I remember that. You helped me feel somewhat better."

        show kyle think at kyle_position

        k "But what other thing?"

        c "You know, when you said you wanted to leave this shitty town so bad."

        c "Did you mean...us too?"

        k "Us? Who is us?"

        c "You know... me?"

        c "and the hippie and the brokie of course"

        show kyle sad at kyle_position

        k "Of course not, you dirty asshole!"

        show kyle normal at kyle_position

        k "You... You guys are what made this town bearable."

        k "I can't imagine my life without you guys"

        show kyle happy at kyle_position

        k "Or...you."

        c "Really? But don't we like, hate each other?"

        #going completely off character here but leave me alone...

        show kyle normal at kyle_position

        k "Well yeah, but to literally quote you,"

        k "I know we argue all the time and I give you tons of crap," 

        k "But we've also been through a, a lot together, and... maybe that alone doesn't make us friends, but it makes us something."  

        k "I know you totally said that so you could go to casa bonita, but I stand by it. (this is one of my favorite cartman lines let me rip it off ok?)"

        c "You are quite a sentimental jew after all, huh?"

        c "I fully expected you to tell me the opposite, that you hated ME and that you wanted to leave cuz of ME."

        show kyle happy at kyle_position

        k "Again, to literally quote you, I never meant to make you feel like you didn't matter at all to me." 

        show kyle normal at kyle_position

        k "I know its gay as hell to remember this, especially since I'm sure it was a tactic to gain your ticket to casa bonita,"

        k "But I never forgot what you said."

        c "I didn't forget either"

        show kyle happy at kyle_position

        k "I know. You never do."

        hide kyle
        hide cartman

        "They sat on the top of Eric's truck, reminiscing on the days where they had nothing to worry about"

        "It was then when the crossing guard caught them, and told them to go back to class before he narced on them."

        jump backclass

    label go_lie_response:

        show kyle think at kyle_position
        show cartman placeholder at cartman_position

        c "Kahl. Be honest with me here."

        hide kyle
        hide cartman

        "Eric pushed Kyle into the back of his truck, making their faces meet.(it's written like this on purpose leave me alone bro)"
        "They shared an intense glare before Kyle pulled away and yelled out (LMAOOO IMAGINE)"

        show kyle angry at kyle_position

        k "STOP THIS CRAP! BE HONEST ABOUT WHAT?"

        show cartman placeholder at cartman_position

        c "Do you have a crush?" #lets put on our thinking caps cartman

        show kyle happy at kyle_position

        "Kyle burst out into a fit of hysterical laughter"

        "Before that laughter turned into rage"

        show kyle angry at kyle_position

        "And then he punched Eric right in his fat nose. God his nose was fat"
        
        hide kyle
    
        "It bled a color of red Kyle had honestly never even seen before."

        show kyle angry at kyle_position

        k "ARE YOU FREAKING KIDDING ME?"

        k "YOU CALLED ME OUT HERE FOR THIS?"

        k "WHAT DO YOU THINK, CARTMAN?"

        k "THIS ISN'T ELEMENTARY SCHOOL AGAIN!"

        k "I'M AN ADULT WITH RESPONSIBILITIES AND SO ARE YOU!"

        k "IT'S TIME TO START ACTING LIKE IT!"

        c "Okay geez. You could've just said no, jew!"

        c "Why did ya have to punch me?"

        c "How will I show up to shop class now?"

        show kyle sad at kyle_position

        k "You will blend in just like the rest of the idiots who take shop!"

        show kyle angry at kyle_position

        k "NEVER make me bunk class unless it's ACTUALLY important!"

        show kyle think at kyle_position

        k "You seemed almost sad!"

        show kyle sad at kyle_position

        k "I shouldn't have taken pity on your ass."

        c "Fine, fine. I deserve that much."

        c "If I give you a ride will we be even?"

        show kyle normal at kyle_position

        k "I'll think about it. But for now? BE ON YOUR BEST BEHAVIOR AND GO TO CLASS."

        c "Alright, kahl. See you!"

        k "Goddamn you, Eric!"

        #another dev note here, I COULD NOT STOP LAUGHING WHILE WRITING THIS DURING MATH BRO OH MY GOD. REMIND ME TO NEVER WRITE FANFICTION BRUHHH
        #trust me i am building up to something amazing (you're not even halfway thru this bs)

        jump backclass

    label backclass:

        scene school at fit_screen

        "The four went to their regular meetup spot before lunch." 

        scene lunchroom at fit_screen

        "While waiting for everyone else, Kyle had noticed a few things around school"

        show kyle think at kyle_position

        "Cartman had often eaten all his snacks or stolen his stationary. Could any of these be useful?"

        menu:


            "Pick up a bag of Cheesy Poofs someone left behind.":
                $ inventory.append("Cheesy Poofs")
                "Kyle tucked the Cheesy Poofs into his bag. This might come in handy for a certain fatass."
        
            "Pick up a spare pencil from the bench.":
                $ inventory.append("Chewed Pencil")
                "Kyle grabbed the Chewed Pencil. Good for drawing or an arts class. A bit chewed so it might tempt cartman. He could die of lead poisoning!!"
        
            "Don't pick up anything.":
                "Kyle decided to leave the clutter alone. (ok why would you NOT take the free stuff, dude!)"

        hide kyle

        s "Guys, anyone wanna come over after school? I emulated valorant!"

        ke "Mprmh Mrphm rhm rmhp! (How much malware did ya download this time? Butters will have to fix it again. but if there's food involved then sure!)"

        s "Aight bet Kenny! Try not to die again! (mission:impossible)"

        ke "Mrphm prhm... (that is if your bootleg laptop and shitty programming skills don't explode me first...)" #stan is just like me forreal bro

        if go and truth:

            show cartman placeholder at cartman_position

            c "Sup Kyle, hey hippie stan and kinny!"

            show kyle normal at kyle_position

            k "Have you matured? Not calling me Kahl or Kyel anymore?"

            "Cartman paused and realised"

            c "Simple slip up Kyel. Don't let your guard down."

            show kyle happy at kyle_position

            k "As if I would ever. With you around, I'm pretty sure PC principal had to hire another guard at the gate!"

            c "I meant METAPHORICALLY, kyel! And hey! I thought we were having a temporary alliance!"

            show kyle normal at kyle_position

            k "Hmm, fine Cartman. You haven't been as annoying lately. Don't get your hopes up though, I'm not helping you pirate tomodachi life." #ryujinx is a pain please do not try to pirate it

            c "But KAHLLLLL, I just HAVE to get tomodachi life so I can make you fall in love with Brian Boitano!"

            show kyle think at kyle_position

            k "Even worse. All the less reason for me to-"

            "They were interupted by the feedback of the speakers in the hallway."

            jump principal_office1

        elif go:

            show cartman placeholder at cartman_position

            c "Sup Kale, hey hippie stan and kinny!"

            show kyle angry at kyle_position

            k "Kale. Seriously. KALE?"

            c "Well if you hate it so much, I'll go back to kyel or kahl then!"

            k "SHUT UP! You still owe me by the way!"

            c "Yeah, yeah whatever. To be fair, you were acting hella weird!"

            show kyle sad at kyle_position

            k "That's only becaus-"

            "He was interupted by a whining feedback of the speakers in the halls."

            jump principal_office2

        else:

            show cartman placeholder at cartman_position

            c "Hey hippie, Hey Kinny!"

            c "Sup Jew."

            show kyle think at kyle_position

            "Oh god. He was still mad from earlier wasn't he?"

            "The rest of the 3 boys chatted idly, while Kyle was left wondering bout that familiar fatso again." 

            "he was then interupted by his name being brodcast on loud speakers."

            jump principal_office3

    label principal_office1:

            show screen display_stats
            show screen global_inventory_action

            p "Kyle Broflovski, you are to report to my office right away, bro."

            p "And hurry up because Jimmy Kimmel is on!"

            show kyle sad at kyle_position

            k "Oh goddammit!"

            hide kyle

            scene pcoffice at fit_screen

            p "Hey Kyle, quick heads up, bro. You aren't in trouble."

            show kyle think at kyle_position

            k "I'm...not?"

            p "Yeah bro. It's just come to my attention that you aren't taking an arts subject."

            k "Well yeah, to get into Princeton, I needed-"

            p "Up bup bup, gonna cut ya off right there. It is MANDATORY to take one at South Park High!"

            show kyle sad at kyle_position

            k "But-"

            p "No buts bro! Now pick one or I will do it for you! AND HURRY UP! Kimmels on in 5! (practical joke, because I assume PC Principal would either HATE or LOVE kimmel dude.)"

            show kyle think at kyle_position

            "Kyle was stunted for choice. Being a heavy academics student, he barely even had time for his hobbies"
            

            $ user_choice = renpy.input("Type an elective (Visual Arts / Music / Drama):")
            $ user_choice = user_choice.strip().lower()

            "Before he could even suggest taking something like [user_choice], an untimely arrival broke Kyle free from his thoughts."
            show cartman placeholder at cartman_position
            
            c "He can take Visual Arts with me. Our class doesn't have a full capacity and it's more easier for beginners"

            show kyle normal at kyle_position

            "Kyle shot Cartman a confused, but very thankful look. Cartman nodded back in return and made a poor attempt to signal something behind his back. (can he even reach behind his back?)"

            "PC Principal sighed"

            p "I dont know what alliance you boys are having but it seems to be working for now."

            p "Fine. Kyle, collect your adjusted timetable from outside. Now GET OUT BOTH OF YOU, BRO!"

            hide kyle
            hide cartman

            "They left the office and started walking to their next classes."

            scene school at fit_screen

            show kyle normal at kyle_position

            k "Thanks for earlier, dude"

            k "I honestly don't know what I would've done otherwise."

            show kyle happy at kyle_position

            k "That was...really nice of you and I'm very...surprised to see you being this kind to me"

            show cartman placeholder at cartman_position

            c "Its no problem Kyle, after all, its payback since you did bunk class with me and come over to play brawl and shit" #they got hardstuck at gold and cartman tilted kyle's p2 mandy by 200 trophies. also, i hc that cartman mains chester just because.

            show kyle normal at kyle_position

            k "Any reason for being this docile, You've been in a good mood practically all week!"

            show kyle happy at kyle_position

            k "Although, I do have to say that I kinda miss our senseless arguments." #WHO is this cos kyle WOULD NOT say ts

            k "I almost wanna make sure you aren't an imposter or something, dude!" 

            c "Wow, KYEL. That was realy JERSEY of you! But yeah, I do agree I have been less of a pain lately."

            show kyle normal at kyle_position

            c "I just feel kinda bad is all. When you go of to Nerdston there won't be a handsome, buff, smart, cool.."

            show kyle sad at kyle_position

            k "Alright, ALRIGHT! Enough with the self-glaze!"

            c "...funny and awesome asshole to annoy you anymore. I felt bad and wanted your last memories to be nice or something."

            show kyle normal at kyle_position

            k "Oh my god. You're actually capable of real human emotion! You're gonna miss me, aren't ya? (he gonna come in a suit to save him from the smug storm or sum?)"

            c "SHUT UP KAHL! DONT PUT WORDS IN MY MOUTH!"

            c "Maybe a little bit though. I can't get the same kick out of ripping on anyone else."

            show kyle happy at kyle_position

            k "Well hey, since you'll be an unemployed bum anyway, might as well come visit me there sometime?"

            c "EY! I will NOT be UNEMPLOYED! I'll be successful and rich while you keep on studying!"

            c "But since your dumbass has so NICELY asked, then sure. As long as there is food and a place to sleep and a Kahl to rip on I'm down."

            show kyle normal at kyle_position

            k "Alright, alright! But you dont gotta be so nice dude, its freaking everyone out! Enjoy your last moments ripping on me while you can!"

            c "Fine bum. Then let's start right now! Last one to visual arts is an idiot!"

            show kyle happy at kyle_position

            k "Hey! You got a headstart!"

            "They ran down the halls, papers flying and students all staring. Were Eric Cartman and Kyle Broflovski actually getting along?" #they wouldn't but its fun to believe bruh

            jump art_class1

    label principal_office3:

            show screen display_stats
            show screen global_inventory_action

            p "Kyle Broflovski, you are to report to my office right away, bro."

            p "And hurry up because Jimmy Kimmel is on!"

            k "Oh goddammit!"

            scene pcoffice at fit_screen

            p "Hey Kyle, quick heads up, bro. You aren't in trouble."

            show kyle think at kyle_position

            k "I'm...not?"

            p "Yeah bro. It's just come to my attention that you aren't taking an arts subject."

            show kyle sad at kyle_position

            k "Well yeah, to get into Princeton, I needed-"

            p "Up bup bup, gonna cut ya off right there. It is MANDATORY to take one at South Park High!"

            show kyle think at kyle_position

            k "But-"

            p "No buts bro! Now pick one or I will do it for you! AND HURRY UP! Kimmels on in 5!"

            $ user_choice = renpy.input("Type an elective (Visual Arts / Music / Drama):")
            $ user_choice = user_choice.strip().lower()

            if "visual" in user_choice or "art" in user_choice:
                "Kyle looked around until he saw something that caught his eye."
                "He had frequently heard Cartman complain about his art class, and what better way to get answers than to share a boring class together?"
                "After all, if he was forced to take this subject, he might as well have gained something from it!"
                k "What about Visual Arts?"
            else:
                p "[user_choice] is completely full, bro! Look, I'm just gonna stick you in Visual Arts. I don't care!"
                "Kyle blinked. Visual Arts? He had frequently heard Cartman complain about his art class..."
                "He realized what better way to get answers than to share a boring class together? If he was forced to take a subject, he might as well gain something from it."
                k "Fine..."

            p "yeah yeah, cool, whatever bro. Tell the lady outside, get your updated timetable and GET OUTTA HERE! Kimmel is on right now!"

            jump art_class3

    label principal_office2:

            show screen display_stats
            show screen global_inventory_action

            p "Kyle Broflovski, you are to report to my office right away, bro."

            p "And hurry up because Jimmy Kimmel is on!"

            k "Oh goddammit!"

            scene pcoffice at fit_screen

            p "Hey Kyle, quick heads up, bro. You aren't in trouble."

            show kyle think at kyle_position

            k "I'm...not?"

            p "Yeah bro. It's just come to my attention that you aren't taking an arts subject."

            k "Well yeah, to get into Princeton, I needed-"

            p "Up bup bup, gonna cut ya off right there. It is MANDATORY to take one at South Park High!"

            show kyle sad at kyle_position

            k "But-"

            p "No buts bro! Now pick one or I will do it for you! AND HURRY UP! Kimmels on in 5!"

            $ user_choice = renpy.input("Type an elective (Visual Arts / Music / Drama):")
            $ user_choice = user_choice.strip().lower()


            show kyle think at kyle_position
            "Kyle was about to start panicking at the thought of taking [user_choice] when an untimely arrival had screwed up his plan."

            show cartman placeholder at cartman_position

            c "He can take Visual Arts with me. Our class doesn't have a full capacity and it's more easier than the rest."

            "This will also be the perfect time to find out what he's hiding! Can't believe I didn't think of it before!"
            "I am a genuis after all! (dont grind my parents into chilli, but u aren't at all buddy)"


            show kyle normal at kyle_position

            "Kyle shot Cartman a confused, but very thankful look. Cartman nodded back in return."

            "PC Principal sighed"

            p "I dont know what alliance you boys are having but it seems to be working for now."

            p "Fine. Kyle, collect your adjusted timetable from outside. Now GET OUT BOTH OF YOU, BRO!"

            "They left the office and started walking to their next class."

            hide cartman
            hide kyle

            scene school at fit_screen

            show kyle think at kyle_position

            k "Look man, after your...interesting accusation, I was quite pissed."

            show cartman placeholder at cartman_position

            c "Can't argue with that."

            show kyle normal at kyle_position

            k "But I just wanted to say, thanks dude."

            show kyle happy at kyle_position

            k "You saved my ass out there!"

            "And you'll save mine by telling me what you're thinking!" #i felt tuff for coming up with this lowkey

            c "No problem bro, I did owe you one! (not that he would ever follow up on it)"

            show kyle normal at kyle_position

            k "Im still mad and I still hate you though, don't get too cocky fatass!"

            c "Easy there, Jersey! Don't wanna show those colors before you reach your habitat!"

            show kyle angry at kyle_position

            k "SHUT THE HELL UP!"

            jump art_class2



    label art_class1:
            
            show screen display_stats
            show screen global_inventory_action

            scene artroom at fit_screen

            "The bell rang and Cartman and Kyle were.. winded to say the least"

            show kyle happy at kyle_position

            k "Even after you got a headstart I still beat you! How slow can you be?"

            show cartman placeholder at cartman_position

            c "Shut"

            c "Shu"

            "Cartman paused to wheeze again"

            c "Shutup jersey!"

            "Another wheeze"

            c "You have an advantage! I heard people from jersey always run from the cops!"

            show kyle angry at kyle_position

            k "Between the 2 of us, which one has run from the cops more? Me or You!"

            c "Point taken. Now lets go to class, Kyel!"

            show kyle think at kyle_position

            k "What the hell do you mean lets go to class dude, we're already here!"

            "Mrs Streibel sighed when she saw Cartman as usual, but almost had a panick attack when she saw the familiar green hat enter her classroom"

            ms "Er - Hello Kyle, what brings you to the art room?"

            show kyle normal at kyle_position

            k "I've been transferred to your class for the rest of the year."

            ms "THE REST OF THE YEAR? OH DEAR GOD!" #probably mr ken's reaction if he saw me in his classlist next year bro

            c "Don't worry, hag! It wasn't by choice!"

            c "PC A-hole transferred him here cos apparently it's mandatory to take an arts subject!"

            c "And Jersey over here cheated his way out of it! That was until he got caught, of course!"

            ms "Well, uh. Looks like I do not have a choice in the matter here."

            ms "But why would he willingly take a subject YOU take, Eric?"

            c "Don't bother asking questions and just teach! I wanna start drawing already!" #me too

            k "I promise I will not be causing trouble, Ms Streibel. As for him... I'm not too sure."

            c "EY!"

            ms "Fine, as long as you two promise to BEHAVE, not argue and NOT make uh... private parts out of clay! (toilet paper, s7e3)"

            c "Yeah yeah, hag!"

            "Kyle elbowed his side hard"

            c "Okay, Mrs Streibel."

            "Kyle shot him an approving look" #considering adding friendship points here...

            jump choice_art

    label art_class2:
            show screen display_stats
            show screen global_inventory_action
            scene artroom at fit_screen

            "Kyle and Cartman walked towards the art room as the art class was about to begin."

            "Mrs Streibel saw Cartman and sighed, she saw Kyle and then almost had a full scale panick attack."

            ms "Hello Eric... And what is your...friend doing here?"

            show kyle normal at kyle_position

            k "I've been transferred here for the rest of the year, please refer to PC Principal's note."

            ms "Oh dear, well I must ask why he transferred you to ERIC's class?"

            show cartman placeholder at cartman_position

            c "It was willingly, hag!"

            show kyle think at kyle_position

            "Kyle elbowed him hard"

            c "We promise to behave or whatever. Just don't fail us."

            ms "Okay, seeing as the principal has ordered this. As long as you two behave and appriciate the arts, you will be passing"

            show kyle normal at kyle_position

            k "Alright, Thank you Mrs Streibel."

            "As Kyle went to go take a seat, Cartman realised that this was his chance to finally get some answers."

            jump choice_art

    label art_class3:

            show screen display_stats
            show screen global_inventory_action

            scene artroom at fit_screen

            "Kyle walked down the halways until he found the art room"
            "He then spotted a familiar figure in the doorway of the art room. He stopped to eavesdrop."

            ms "Eric, this is a wonderful painting! I've never seen anything quite like it at all!"

            show cartman placeholder at cartman_position

            c "Thank you, Miss. I am quite uhh proud of it!"
            
            "He's being....NICE?"

            ms "I do say Eric, why not try for an art school? You never know where you might end up!"

            c "Miss, you know I don't plan on furthering my studies right?"

            ms "I know, Eric! But it really wouldn't hurt to try!"

            ms "The world deserves to see such uniqueness! I think your work deserves to be shared!"

            c "Cmon, miss! We both know as well as the next person that people would make so much fun of me if they found out!"

            c "The cranky, fatherless little fat kid! Painting as a living! That's just straight bullshit!"

            ms "Art doesn't have a guideline for who can paint, Eric! I think it's time to stop keeping such a secret! You're so talented too!"

            ms "It's such a shame to see it go to waste!"

            c "Fine. I'll think about it if you stop hounding me..."

            "Is this what he was trying to tell me today? Oh my god, I'm so stupid."
            "As Kyle watched Eric go inside, he too followed."
            "He handed the slip PC Principal gave him and Mrs Streibel, although reluctant, welcomed him in."

            c "Oh. Hey. What are you doing here?"

            "I hope that Jersey didn't here what I was saying earlier, after all its not like he would've wanted to listen..."

            show kyle think at kyle_position

            k "I've been transferred here for the rest of the year. Apparently someone narced on my lack of an arts subject to PC Principal and now I'm essentially forced to take it"

            c "Why visual arts, jew?"

            "I can't tell him my real motive for joining this class, so I'll just lie again."

            show kyle normal at kyle_position

            k "The other ones were full already. Besides, theres like 2 months left anyway. It doesn't even matter."

            c "Fine, fine but I hope you know that this is what you get, hm?"

            show kyle sad at kyle_position

            k "What?"

            c "You're really going to enjoy fingerpainting..."

            c "With the kindergardners!"

            "Maybe I can finally tell him now"

            show kyle angry at kyle_position

            k "Be quiet fatso, I know one things for sure, I'm a thousand times better at painting than you!"

            "That's a lie but there isn't a need to boost his ego!"

            c "Shut up Jersey! At least I don't have to be forced to have fun!"

            "Cartman's idea of having fun drawing was sketching in his little red book...(this is referencing tfbw the game ok)"

            show kyle normal at kyle_position

            k "Fine then! Let's do the assignment today and see who does it better!"

            c "You're on!"

            #dev note for the end of this, its a bit of a yap. i really wanted cartman to be an art genuis because im not and i find that concept funny as hell
            # ONLY in this situation do I wanna be cartman bro like give me that talent if u gonna waste it bruh
            #also if u ever did play the fractured but whole game, cartman actually keeps a sketchbook with very...unique drawings in the game! this is lok an easter egg!

            jump choice_art

    label choice_art:

            menu:

                "Behave and do the assignment like asked.":
                    $ friendship_points += 1
                    jump behave
                "Start a paint fight.":
                    $ friendship_points -= 1
                    jump fight

    label behave:

        show screen display_stats
        show screen global_inventory_action

        "Mrs Streibel gave the class a still-life assignment, the class got to work painting a picture of a fruit bowl"

        show cartman placeholder at cartman_position
        
        c "Ah shit! I forgot my pencil. You have one I can borrow, jersey?" #he would not ask this nicely

        menu:
            "Give the pencil to cartman" if "Chewed Pencil" in inventory:
                $ inventory.remove("Chewed Pencil")
                $ friendship_points += 2
                "Kyle rummages through his bag a little and brings out a somewhat chewed on pencil"
                k "Here fatso, use this."
                c "kinda gross, but I appreciate it, jew!"
                "How is he not tempted to eat it! Goddammit."
                c "here, since you're struggling a bit, I'll help ya out."
                "Cartman helps Kyle draw a very lifelike outline of the bowl."
            
            "Make fun of him and continue on":
                k "Be prepared next time, fatty!"
                c "EY! Mine looks better than yours anyway! Besides, i've stolen more than enough pencils from you!"

        show kyle sad at kyle_position
        show cartman placeholder at cartman_position

        k "God, this is so cliche! Do you just do this every lesson? I feel like I'm in an anime right now!"

        c "Its just the type of assignments the hag gives us!"

        show kyle think at kyle_position

        k "Don't call her a hag, Cartman!"

        c "Shut up, Kahl! You also went to tp her house when we were kids you know."

        show kyle sad at kyle_position

        k "Yes, but I actually felt guilty! And you tried to unalive me with a whiffle bat when we did!"

        c "Cmon Kahl, I was going easy on you. I totally would've kill ya if I wanted"

        show kyle normal at kyle_position

        k "Exactly. Now focus and start painting. I know you wanted a nude model but this would have to do."

        c "That isnt the ONLY reason I signed up! I happen to actually like painting!"

        k "I guess it makes sense...you don't actually suck at it!"

        c "Wow, Kahl. A very half-assed compliment-"

        show kyle happy at kyle_position

        k "Still a compliment though, right!"

        c "Fine. What about you. Still stressed and stuff?"

        show kyle normal at kyle_position

        k "Well for now, no actually. This painting stuff isn't too bad!"

        "Kyle was proud that he finally got the outline of the basket correct."
        "Meanwhile, he looked over at Cartman's canvas, only to see a full outline, primed canvas AND base colors"
        "Since when did he Kyle even know these terms!"

        show kyle think at kyle_position

        k "DUDE! How are you so far ahead!"

        c "Because, Kyle. You're a perfectionist. Look closely and see how messy my lines are! I didn't even paint the base layer inside them"

        #NONE of them would use these terms but i wanted to show off my art skills (non existent)
        #btw this entire subplot is just a big reference to the "toilet paper" episode because I find the idea of cartman attempting to kill kyle with a wiffle ball bat funny as hell

        jump after_paint







    

    label fight:
        show screen display_stats
        show screen global_inventory_action

        "Kyle gets a little bored during the lesson, he looks over and sees a focused cartman"

        "He looks so silly right now...it wouldn't hurt to have a little fun right?"

        "Kyle puts some green paint onto his brush, and flicks it onto cartman"

        show cartman placeholder at cartman_position
        show kyle normal at kyle_position

        c "KAHL! I KNOW THAT WAS YOU!"

        ms "BOYS! PLEASE!"

        "Cartman flicks some red paint onto kyle's canvas."

        k "Oh its OVER fatass!"

        show screen fight_qte_button
        $ renpy.pause(3.5, hard=True)


    label kyle_wins_fight:
        hide screen fight_qte_button
        $ friendship_points -= 2
    
        show kyle happy at kyle_position
        k "Nice try, fatass!"
        "The paint is spilled all over the classroom. The students and Mrs Streibel look on in horror."

        show cartman placeholder at cartman_position

        c "EYYY! Screw you guys, I'm going home!"
    
    jump after_fight


    label cartman_wins_fight:
        hide screen fight_qte_button
        $ friendship_points -= 3
    
        show kyle sad at kyle_position
        "POW!"
        "Kyle hesitates. Cartman flicks a wad of paint into Kyles eyes while he isn't looking."
        show cartman placeholder at cartman_position
        c "Ha-ha! Direct hit, Jew!"
    
        jump after_fight


    label after_fight:

        ms "BOYS! YOU PROMISED ME YOU WOULDN'T FIGHT!"

        ms "I'LL HAVE NO CHOICE BUT TO FAIL YOU IF THIS KEEPS UP!"

        ms "AND KYLE! ITS YOUR FIRST CLASS! HOW DID YOU MANAGE TO START SUCH A COMMOTION ALREADY!"

        ms "UNTIL BOTH OF YOU LEARN HOW TO BEHAVE PROPERLY, YOUR GRADES WILL BOTH BE Fs."

        if friendship_points >= 5:

            show kyle sad at kyle_position
            k "I'm sorry cartman, it was all silly banter, didn't mean to start up something stupid."

            show cartman placeholder at cartman_position

            c "Im sorry too, kyle, yes, it was silly banter and I honestly kinda had fun!"

            "They were trying to grin and bear the pain in front of Mrs Streibel, as neither wanted a failing grade."

            ms "Fine, I guess at the end of the day you boys are friends after all..."

            ms "Since it was all in good fun, I have decided to let it slide BUT ONLY FOR NOW OKAY?"

            show kyle happy at kyle_position

            k "Thank you Ms Streibel!"

            c "Yeah, thanks"

            "Kyle and Cartman nodded to each other, grinned and even started laughing when her back was turned"
            "Visual arts was turning out to be quite a fun surprise, Kyle had never expected to have fun in the class? Especially not with Eric Cartman, his mortal enemy"

        else:

            ms "DO YOU BOTH UNDERSTAND?"

            "Kyle and Cartman both nodded."
            "They made eye contact again, awkward but..."

            menu:
                "smile at cartman and gesture something stupid.":
                    $ friendship_points += 2
                    jump end_day
                "glare.":
                    $ friendship_points -= 1
                    c "FUCK YOU KAHL!"
                    jump end_day



    label after_paint:

        "The bell rang and it was finally the end of the lesson"

        show cartman placeholder at cartman_position

        c "Jew, you aren't as bad as I thought you would be! But you still suck of course!"

        k "Thanks, fatty! But I still beg to differ"

        show kyle normal at kyle_position

        c "Wanna come over again? We had fun last time"

        show kyle happy at kyle_position

        k "Sure, but you gotta show me your little red drawing book!"

        c "LIKE HELL I WILL KAHL!"

        jump end_day


    label end_day:

        "Cartman gives Kyle a ride home, and maybe a pass for a sleepover, depending on how high your friendship points are of course."
        "What, confused to see the narrator narrating about the GAME? Grow up dude"
        "But yeah, you've reached the end for now cos I do not have time to code the rest before the deadline (cmon mr ken whyy)"
        "I had an awesome time coding this icl and it was like coding, fanfiction and art all at once, which was a dream and a nightmare for me heh"
        "also the cartman image is a placeholder until I draw, i realised i wasn't getting graded on that so i lost motivation."
        "Bascially, take this as a demo. This is the end for now, please consider replaying to see other options that i broke my back to code!!"

        return 




            








        



        


screen display_stats():
    frame:
        xalign 0.05
        yalign 0.05
        padding (15, 15)
        vbox:
            spacing 5
            text "Game Engine State HUD" size 18 color "#fff" bold True
            text "Cartman Relationship Score: [friendship_points]" size 14 color "#FF474C"
            text "Inventory: [inventory]" size 14 color "#3fb83b"



screen global_inventory_action():
    zorder 100 
    
    if "Cheesy Poofs" in inventory:
        button:
            xalign 0.95
            yalign 0.05
            background "#FF4500"
            padding (10, 10)
            
            
            action [
                RemoveFromSet(inventory, "Cheesy Poofs"),
                IncrementVariable("friendship_points", 5),
                Hide("display_stats"),
                Hide("global_inventory_action"),
                Function(renpy.call_in_new_context, "cartman_snack_attack")
            ]
            
            text "Toss Cartman Cheesy Poofs" size 12 color "#fff" bold True

label cartman_snack_attack:
    
    play sound "audio/cartmanv.wav"
    
    "Out of nowhere, Kyle reaches into his bag and tosses the bag of Cheesy Poofs mid-sentence."

    c "OH MY GOD! CHEESY POOFS?!"

    "Cartman completely drops whatever he was doing, tears open the bag, and begins cramming them into his face."

    c "Kahl... I don't care what we were talking about. You are awesome right now."

    
    show screen display_stats
    show screen global_inventory_action
    
    return
           

screen fight_qte_button():
    zorder 101
    modal True 
    
    default timer_duration = 3.0
    
    vbox:
        xalign 0.5
        yalign 0.45       
        spacing 25        
        
        
        bar:
            value AnimatedValue(0.0, 1.0, delay=timer_duration)
            xmaximum 500   
            ymaximum 25    
            left_bar "#ff3333"  
            right_bar "#842424" 
            xalign 0.5
            
        
        button:
            xalign 0.5
            background "#cc0000"
            hover_background "#ff1111" 
            padding (35, 20)           
            
            action [
                Hide("fight_qte_button"),
                Jump("kyle_wins_fight")
            ]
            
            text " DODGE CARTMAN'S PUNCH! ":
                size 22 
                color "#fff" 
                bold True 
                xalign 0.5 

    timer timer_duration action [
        Hide("fight_qte_button"),
        Jump("cartman_wins_fight")
    ]