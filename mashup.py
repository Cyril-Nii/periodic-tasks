# Program to mimic MTN's Mashup from *567#

def home():
    input1 = input(f"""
Welcome to MTN Pulse. Please select an option
1. Proceed to buy bundle(No 4G bonus)
2. Go to myMTN app (Free 500MB for new users and 50% 4G bonus) [Currently Not Available]
Input : """)

    if(input1 == '1'):
        mashup_page()
    elif(input1 == '2'):
        not_available()
    else:
        print("Invalid Option")
        inv = input("\n1.Try Again\n2.Exit\nInput : ")
        if(inv == '1'):
            home()
        else:
            print("Exited")
        

def not_available():
    print("\nNot Available at the moment")        
        
def request_input():
    i = input("\nInput : ")
    i = int(i)
    return i

def flexi(amt):
    print()   

def payment_option():
    print(f"""
Payment Option
1. Airtime
2. Mobile Money""")
    opt1 = request_input()

    if(opt1==1):
        print("You have successfully purchased....")
    elif(opt1==2):
        print("Invoice will be sent soon...")

def mashup_page():
    print(f"""
Welcome to MTN Pulse.
1. MashUp For Self
2. Mashup For Others
3. Convert Minutes to Data
4. Pulse Loyalty
5. Check Promo Points
99. More
0. Back""")
    opt1 = request_input()
    
    if(opt1 == 0):
        home()
    elif(opt1==99):
        mashup_page_extended()
    elif(opt1==1):
        mashup_for_self()
    elif(opt1==2):
        mashup_for_others()
    elif(opt1==3):
        convert_minutes_to_data()    
    elif(opt1==4):
        pulse_loyalty() 
    elif(opt1==1):
        check_promo_points()
          

def mashup_page_extended():
    print(f"""
6. Download App
7. Check Balance""")
    opt1 = request_input()
    
    if(opt1==6):
        print("\nPlease confirm request:\n1.Yes\n0.Back")
        opt2 = request_input()
        if(opt2==1):
            print("Dowload link not available at the moment") # Will write code for Dowloading the app
        elif(opt2==0):
            mashup_page()
    

def mashup_for_self():
    print(f"""
MashUp Offers
1. MashUp GHC 1
2. MashUp GHC 5
3. MashUp GHC 10
4. MashUp GHC 30
0. Back""")
    
    opt1 = request_input()
    
    if(opt1==0):
        mashup_page()
    elif(opt1==1):
        GHC1Mashup()
    elif(opt1==2):
        GHC5Mashup()
    elif(opt1==3):
        GHC10Mashup()
    elif(opt1==4):
        GHC30Mashup()
        
        
    
def mashup_for_others():
    
    print()
    
def convert_minutes_to_data():
    print()
    
def pulse_loyalty():
    not_available()
    
def check_promo_points():
    not_available()
    
def GHC1Mashup():
    print(f"""
Select one of the following:
1. GHC 1
2. Enter amount GHC (GHC 0.07 - 4.99)
0. Back""")
    
    opt1 = request_input()
    
    if(opt1==0):
        mashup_for_self()
    elif(opt1==1):
        print() # implement regular
    elif(opt1==2):
        print()# implement flexi
    
def GHC1_regular():
    payment_option()
    

def GHC1_flexi(amt):
    flexi(amt)

def GHC5Mashup():
    print(f"""
Select one of the following:
1. GHC 5
2. Enter amount GHC (GHC 0.07 - 9.99)
0. Back""")
    
    opt1 = request_input()
    
    if(opt1==0):
        mashup_for_self()
    elif(opt1==1):
        print() # implement regular
    elif(opt1==2):
        print()# implement flexi
    
def GHC10Mashup():
    print(f"""
Select one of the following:
1. GHC 10
2. Enter amount GHC (GHC 0.07 - 29.99)
0. Back""")
    
    opt1 = request_input()
    
    if(opt1==0):
        mashup_for_self()
    elif(opt1==1):
        print() # implement regular
    elif(opt1==2):
        print()# implement flexi
    
def GHC30Mashup():
    print(f"""
Select one of the following:
1. GHC 30
2. Enter amount GHC (GHC 0.07 - 4.99)
0. Back""")
    
    opt1 = request_input()
    
    if(opt1==0):
        mashup_for_self()
    elif(opt1==1):
        print() # implement regular
    elif(opt1==2):
        print()# implement flexi
        
    
home()