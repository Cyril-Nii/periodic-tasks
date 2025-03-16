# Functions for MTN Mashup from *567#

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

def payment_option(amt):
    print(f"""
Payment Option
1. Airtime
2. Mobile Money""")
    
    opt1 = request_input()
    
    if(opt1==1):
        print("\nCongratulations! You have successfully purchased GHC" + str(amt) + " Mashup")
        
    elif(opt1==2):
        print("\nYou will recieve Mobile Money prompt soon")

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
    
    if(opt1==0):
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
7. Check Balance
0. Back""")
    
    opt1 = request_input()
    
    if(opt1==6):
        print("\nPlease confirm request:\n1.Yes\n0.Back")
        
        opt2 = request_input()
        
        if(opt2==1):
            print("\nDownload link not available at the moment") # For Dowloading the app
            
        elif(opt2==0):
            mashup_page_extended()
            
    elif(opt1==7):
        print("Checking balance...")
        
    elif(opt1==0):
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
    phone = input(f"""
Enter Phone Number
Input : """)
    
    confirm_phone = input(f"""
Confirm Phone Number
Input : """)
    
    if(confirm_phone==phone):
        mashup_for_self()
        
    else:
        print("\nEntered phone number does not match")
        mashup_for_others()
        
def convert_minutes_to_data():
    not_available()
    
def pulse_loyalty():
    not_available()
    
def check_promo_points():
    not_available()
    
    
def GHC1Mashup():
    print(f"""
Select one of the following:
1. GHC 1
2. Enter amount GHC (Between 0.07 - 4.99)
0. Back""")
    
    opt1 = request_input()
    
    if(opt1==0):
        mashup_for_self()
        
    elif(opt1==1):
        regular(1)
        
    elif(opt1==2):
        flexi()
    
def GHC5Mashup():
    print(f"""
Select one of the following:
1. GHC 5
2. Enter amount GHC (Between 5 - 9.99)
0. Back""")
    
    opt1 = request_input()
    
    if(opt1==0):
        mashup_for_self()
        
    elif(opt1==1):
        regular(5)
        
    elif(opt1==2):
        flexi()
    
def GHC10Mashup():
    print(f"""
Select one of the following:
1. GHC 10
2. Enter amount GHC (Between 10 - 29.99)
0. Back""")
    
    opt1 = request_input()
    
    if(opt1==0):
        mashup_for_self()
        
    elif(opt1==1):
        regular(10)
        
    elif(opt1==2):
        flexi()
    
def GHC30Mashup():
    display_packages(30)
    
    opt1 = request_input()
    
    if(opt1==1):
        payment_option(30)
        
    else:
        exit

      
def regular(amt):
    display_packages(amt)
    
    opt = request_input()
    
    if(opt ==1):
        print("\nAvailable only on the myMTN app")
        
    elif(opt in range(2,5)):
        payment_option(amt)

def flexi():
    input("\nFlexi Packages Unavailable at the moment")

def display_packages(amt):
    if(amt==1):
        print(f"""
1. 13.1MB and 15.42Mins(available on mymtn app only)
2. 21.83MB and 11.02Mins
3. 26.2MB and 8.82Mins
4. 30.57MB and 6.6Mins
5. 43.67MB only""")
        
    elif(amt==5):
        print(f"""
1. 73.93MB and 82.17Mins(available on myMTN app only)
2. 123.21MB and 58.68Mins
3. 147.86MB and 46.95Mins
4. 172.5MB and 35.22Mins
5. 246.43MB only""")
        
    elif(amt==10):
        print(f"""
1. 155.12MB and 171.15Mins(available on mymtn app only)
2. 258.53MB and 122.25Mins
3. 310.24MB and 97.8Mins
4. 361.94MB and 73.35Mins
5. 517.06MB only""")
        
    elif(amt==30):
        print(f"""
Y'ello! the MashUp GHC30 Bundle gives you 2690.58MB. This bundle does not expire.
1. Buy""")
