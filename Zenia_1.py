
# Welcome message for the user:

print('''Hello and welcome to ZEN Wellness Centre of our University. 
      
I am Zenia your assistant to help you navigate through our services and treatments.

Our services and treatments catalogue includes all the colors of the rainbow:
          red, orange, yellow, green, blue, indigo, and violet. 

Please enter your details below to start our journey. 
      ''')

def print_services(user_fav_clr):                                  # This function is a placeholder for printing out the Wellness services based on user's favourite colour.
  
  if user_fav_clr == "red":                                        # Colour coded services fed to the user based in their input.
    print("""
        I see your favorite rainbow colour is red! 
        Please see below the available treatments and services:""")
       
    print(""" 
      1. Hot yoga session, Mondays at 6:00pm at RED Studio Room 1: Join us to burn all of those 
          toxins and purify yourself! Amanda is your yoga tutor. 
          Bring a towel and plenty of water, things will get steamy!!!
            
      2. Hot Stone Massage treatment, RED Therapy Room 3 Tuesdays & Thursdays between 10:00am - 6:00pm:
         A 45 minute therapy, that is used to help you relax and ease tense muscles as well as 
         damaged soft tissues throughout your body. Attention: Please inform in advance your therapist
         of any potential injuries or traumas.)       
             
      3. Join our "Courageous" talking therapy session on Wednesdays, RED Therapy Room 6, 5:00pm - 6:00pm:
         Paul is a Psychology Professor and holds these meetings to discuss vulnerability, courage, anxiety, depression,
         with anyone who attends. He provides a path to achieve your breakthroughs to a calmer and stronger YOU!
             
      4. "Rojo Bailar" latin and ball room dance studio on Fridays 4:00pm - 5:00pm, RED Studio Room 1:
          Antonio and Melissa will be your dance tutors, please inform them for any injury's you might have.
          A journey to learn classic latin dance such as Argentinian Tango, Salsa. Also Ball Room Dance such as Waltz, Quickstep etc.
         """)  
    
  elif user_fav_clr == "orange":
    print ("""I see your favorite rainbow colour is orange! 
        Please see below the available treatments and services: """)
     
    print("""
      1. Deep Cleansing Facial 40 minute treatment session, Mondays  between 11:00am - 6:00pm, ORANGE Therapy Room 2: 
         It will improve your skin health remove blackheads and close your pores. 
         Selene will be your therapist and will use our Citrus and Honey skin series for all skin types.
         Please feel free to ask for samples of the skin treatment you received. ) 

      2. Fragrant Apothecary, ORANGE Studio Room 5, Tuesdays & Thursdays 11:00am - 1:00pm: 
         Learn how to make your own holistic ointments, serums and lotions.
         Sergio will teach you how to use a series of organically produced oils, and tinctures in order to make
         your one cosmetic products for your face and body, customised to your own skin needs.
           
      3. Aromatherapy Swedish Massage 45 min, ORANGE Therapy Room 2, Monday - Friday 10:30am - 5:30pm:
         George and Mary are running these treatments, please join us and enjoy a massage treatments customised to your needs.
           
      4. Urban Legend Dance Studio, ORANGE Studio 5, Fridays 10:00am - 11:00am and 4:00pm - 5:00pm.
         Deborah and Quincy will show you the moves!! Come and join us to this all immersive street dance experience.
         Please wear comfortable clothing, have a pair of gym trainers that you are comfortable dancing in and do not forget 
         to let your tutors know of any injuries you might have. 
         """)
    
  elif user_fav_clr == "yellow":
    print ("""I see your favorite rainbow colour is yellow! 
        Please see below the available treatments and services: """)
       
    print (""" 
      1. Rise & Shine Yoga session, Monday - Friday 6:00am - 7:00am, YELLOW Studio Room 2:
         Join us in an morning session practicing our Sun salutations! An invigorating yoga session that aims to 
         get you ready for the day. Sarah will be your yoga tutor, please inform her in advance of any injuries. 
         Complimentary smoothie given at the end of the session made with organically produced fruits and vegetables 
         from our kitchen garden! Let the sunshine in to lead your day! ) 
              
      2. Solaris tanning sessions, Wednesdays 9:00am - 4:00pm, YELLOW Studio 7: 
         5min - 12min standing up booths. Boost your vitamin D, help your immune system,  your bones and mental health.
         Our team will help you to get ready, your appointments include a consultation where 
         we can customise the time of exposure based to your needs. 
              
      3. Volley sessions, Thursdays 10:00am - 12:00pm & 2:00pm 4:00pm, capacity 24 places per hour:
         Anna and Jenny will be your coaches, two volley courts, 24 players and let the games begin!
              
         4. Join our "Leaders" talking therapy session on Fridays, YELLOW Therapy Room 6, 10:00am - 11:00am:
            Paul is a Psychology Professor and holds these meetings to discuss anxiety and time-management, 
            procrastination, and panic attacks with anyone who attends and provides a path to achieve your breakthroughs 
            to a calmer and stronger YOU! 
            """)
       
  elif user_fav_clr == "green":
    print("""  I see your favorite rainbow colour is orange! 
        Please see below the available treatments and services: """)
       
    print(""" 
       1. Aerial Yoga session, Mondays 11:15am - 12:15pm, GREEN Studio 4:
          Amanda will be your yoga tutor. A combination of traditional yoga poses with the use of hammocks and ropes.
          A liberating experience that provides an amazing cardio-exercise and tones all of muscles in your body.
             
      2. Shiatsu massage treatment, Tuesdays 1:30pm - 2:30pm, GREEN Therapy Room 3:
         25 minutes sessions with Mizuki (therapist), please book your appointments at the reception.   
         Release tension throughout your body, let the Qi (chee) flow freely and get your energy back up!

      3. "Samba de Roda" Capoeira dance sessions, Wednesdays & Fridays 5:00pm - 6:00pm, GREEN Studio 2:
          A blend of traditional dance and fight moves, often seen as a martial art. Come on let get new skills and delve into brazilian dnace
          moves. Paulo will be your instructor. Please come with comfortable clothes.
             
      4. Arts & Crafts "Healing Crystals Jewelry", GREEN Room 1, Thursday 3:00pm - 4:00pm:
         Please join us to connect with your creative side, lets make some jewelry with gemstones.
         Gemstones have been traditionally used since ancient times to help with healing and balance your energy.
         Also, improving and helping yoga and meditation practices and of course energy cleansing.
         Come with us and express yourself through your creativity and help your body and recharge.
         """)
    
  elif user_fav_clr == "blue": 
    print("""  I see your favorite rainbow colour is blue! 
         Please see below the available treatments and services: """)

    print(""" 
         1. "Restore" pilates session, Mondays 9:00am - 10:00am, BLUE Studio 5:
            Jake will be your pilates instructor for the session. Please let your instructor
            know of any previous injuries. This session will tone your body, strengthen your core. 
               
         2. Craniosacral Massage treatment 35min, Tuesdays 11:30 - 12:30, BLUE Therapy Room 2:
            It is a gentle, hands-on massaging technique. It uses a light touch to release tension around your body's 
            connective tissue network called the fascia. It promotes pain relief from headaches and neck pain.
               
         3. Aqua Aerobics, Wednesday & Friday 4:30pm - 5:30pm, BLUE AREA: Pool Ground Floor:
            Jenny and George will be your instructors. Low impact exercise for our joints and ligaments
            and great cardio.
               
         4. Arts & Crafts, Thursday 11:00am - 12:30pm, BLUE Studio 7:
            Join Amelia to explore painting and free hand drawing. A way to come closer with 
            the creative side of yourself.
            """)
         
  elif user_fav_clr == "indigo":
    print("""  I see your favorite rainbow colour is indigo! 
        Please see below the available treatments and services: """) 

    print("""
        1. Vinyasa Yoga, Monday 8:30am - 9:30am, INDIGO Studio 2:
           Vinyasa is a style of yoga characterized by stringing postures together so that you move 
           from one to another, seamlessly, using breath. Fernando will be your instructor so please inform him
           of any previous injuries you might have. Lets's connect with our breath!

        2. Reiki sessions Tuesday & Thursday 11:00am 12:00pm, INDIGO Treatment Room 4:
           Sonia will be your therapist for the above sessions. Reiki is a Japanese technique for stress reduction 
           and relaxation that also promotes healing.

        3. Rowing sessions Wednesday 2:30pm - 3:30pm INDIGO Studio 3:
           Capacity 15 rowing machines, Harry will be your instructor for those sessions.
           Ready, steady GO! this amazing session will tone and strengthen all your body! 

        4. Meditation sessions Friday 1:30pm - 2:30pm INDIGO Room 1:
           Sami will be guiding through those meditations, please join us and learn how to 
           reach nirvana! 
           """)
        
  elif user_fav_clr == "violet":
    print("""  I see your favorite rainbow colour is violet! 
         Please see below the available treatments and services: """) 

    print("""
         1. Kundalini Yoga, Monday 5:30pm - 6:30pm, VIOLET Studio 4:
            Kundalini is a style of yoga that focuses on the energy that lies within our bodies.
            You will learn to connect deeply with your body, activate this energy and re-energise your chakras,
            lower your cortisol levels and improve your sleep!

         2. Meditation sessions Tuesday 1:30pm - 2:30pm VIOLET Room 1:
            Sami will be guiding through those meditations, please join us and learn how to 
            reach nirvana! 

         3. Aerobic sessions Wednesday 3:30pm - 4:30pm VIOLET Studio 3:
            Susie will be your Aerobics instructor. Ready, steady GO! this amazing session 
            will tone and strengthen all your body! 

         4. Arts & Crafts sessions, Friday 1:30pm - 2:30pm VIOLET Room 2:
            Sonia will be showing you how to make scented candles based on key aromatherapy 
            essential oils.  Make your own scented candle infused with the essential oils that are 
            relevant to your healing needs. 
            """)

rainbow_cls = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]    # The list contains the valid entries of colours my program accepts to show the services.

while True:
    try:
        user_age = int(input("Please enter your age: "))                        
        
        if user_age < 18:                                                        # Error handling regarding age restrictions for the provided services.
            print("Our services are available to adults only. Thank you for your interest.")     # Prints out a message for the user entry.
            break
        
        user_name = input("Please enter your name: ").capitalize()
        user_fav_clr = input("Please enter your favorite color of the rainbow: ").lower()

        if user_name.isdigit() or user_fav_clr.isdigit() or user_fav_clr not in rainbow_cls:    # Error handling to check the user inputs regarding name and colour using alphabetic characters.
            print("This is not a valid entry. Please only enter alphabetic characters.")        # Prints out a message for the user entry.
            continue

        if user_fav_clr in rainbow_cls:                                           # If the entered color is not in the list, it prints an error message, and the loop goes back to the beginning.
            print_services(user_fav_clr)
        else:
            print("I'm not sure if that was a color you have entered, please try again.")

        another_enquiry = input("\nDo you want to plan another visit? (yes/no): ").lower()  
        if another_enquiry != "yes":                          # Handling a new enquiry if the user wants to make one or it prints out a farewell message and breaks out of the loop.
            print("Goodbye! Have a great day!")
            break

    except ValueError:
        print("You have not entered a valid age. Please try again.")
