# icrease max limit for recursion function
import sys
sys.setrecursionlimit(50)

# notes holistic flow of the program

# generally, semua proses pengerjaan dilakukan secara looping terhadap database untuk mencegah error dan skip data terutama setelah dilakukan modifikasi data
# contohnya bila user menambahkan index baru dengan nilai yang tidak berkelanjutan dari data awal (ex : index = 100) tanpa looping pencarian akan error dan tidak dapat dilakukan

# proses pengerjaan dlakukan terbalik (membuat frame awal dari menu data (function main_menu) + initial data(data_awal))
# mengimport library datetime untuk digunakan pada function jamsek(), perhitungan expired_date pada dictionary, 
# penentuan status pada dictionary (expired / still good) dengan menggunakan perbandingan antara tanggal sekarang dan tanggal expired
# mengimport class bcolors untuk pewarnaan dan mempermudah warning bagi user
# membuat function sdata(), sdata3() untuk menampilkan data dan function jamsek() untuk mengtahui pagi/siang/malam dan menyapa user
# membuat function sub menu 1 - 5
# menambahkan fitur login dengan menggunakan function registration() dan login()
# mengkompilasi semua function menjadi satu kesatuan dengan menggunakan metode calling other function dan recursive function
# start program dengan menuliskan fungsi Login() yang telah terintegrasi

# additional new feature
# menambahkan function baru untuk lupapass() untuk lupa password dan  gantipass() untuk  mengganti password


# Coloring
#=================================================================================================================================================================
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")


# initial data
#=================================================================================================================================================================
import datetime as dt
Data_Awal = [
    {'Index' : 1,'Item' : 'Delfies',    'Location' : 'Sector1','Qty' : '100',   'Expired_Date' : '27/01/2021','Status' : ''}, 
    {'Index' : 2,'Item' : 'Zennys',     'Location' : 'Sector3','Qty' : '50',    'Expired_Date' : '06/12/2022','Status' : ''}, 
    {'Index' : 3,'Item' : 'Bankai',     'Location' : 'Sector1','Qty' : '70',    'Expired_Date' : '11/05/2023','Status' : ''}]

# blank list used as buffer storage data for iteration therefore, iteration can be print after looping and will not causing multiple format printed
Selection_Data = [] 
Dummy_S2 = []
Dummy_S2a = []
Dummy_S3 = []
Dummy_S4 = []

# Register + Login + Lupapass + Gantipass
#=================================================================================================================================================================
# blank list used as buffer storage data for iteration registration and log in
UserName = [] 
DummyPassword = []
PassWord = [] 
User_Pass = []
Dummy_User_Pass = []
Dummy_Lupa = []
Dummy_GantiU = []
Dummy_GantiP = []


# register new ID and new Pass then store it on list above

def Registration ():
    print (f'''
{'+'*15}{bcolors.OKBLUE} 😊🙋‍♂️ Welcome Visitor! 🙋‍♀️😊 {bcolors.ENDC}{'+'*15}
Before continue, let me identify you by filling registration below :
{bcolors.OKGREEN}{dt.datetime.now().strftime("%A, %d %b %Y %H:%M:%S")}{bcolors.ENDC} 
''')        # used to format time now into days(sunday,monday,etc), (dates) (months) (years) (hours):(minutes):(seconds)
    try :
        NewUser = input('Please input new Username :')
        NewPass = input('Please input new Password:')
        DummyPassword.append(NewPass)
        while True :
            print(f"{bcolors.OKGREEN}'Type exit, if you want to exit'{bcolors.ENDC}")
            ConfirmPass = input('Re-enter new Password :')
            if ConfirmPass == DummyPassword[0] :        # used index 0 as comparsion since the dummy data will be always cleared later
                print ('Password has been verified')
                ConfirmUser = input('Are you sure want to make new UserName (y/n)?'.lower())
                if ConfirmUser == 'y' :
                    try : # must use try because if the index is not in list will causing error and execute to except
                        if UserName.index(NewUser) >= 0 :
                            print (f'{bcolors.WARNING}UserName already registered{bcolors.ENDC}')
                            break
                    except : # NewUser not yet registered thefore the data will be added 
                            UserName.append(NewUser)
                            PassWord.append(ConfirmPass)
                            DummyPassword.clear()
                            print (f"{bcolors.OKBLUE} 😊 Account successfully create 😊 \n{bcolors.ENDC}")
                            User_Pass.append(dict(zip(UserName,PassWord))) # to combine the user password into dictionary and reduce risk of wrong combination between
                            UserName.clear()                               # registered password and username
                            PassWord.clear()
                            return UserName,PassWord,User_Pass,Login() # return value to keep username + password and continue to func Login
                elif ConfirmUser == 'n':
                    DummyPassword.clear()
                    print (f'{bcolors.WARNING}Registration cancelled{bcolors.ENDC}')
                    Login()
                    break
            elif ConfirmPass == 'exit' :
                DummyPassword.clear()
                Login()
                break
            else :
                print(f'{bcolors.WARNING}Verification Failed{bcolors.ENDC}')
    except :
        print (f'{bcolors.WARNING}Sorry, we found some error please re-enter the data{bcolors.ENDC}')
        Login()
        
        
def LupaPass () :
    Lupa = input('Please input your registered username to get your password : ')
    for i in range(len(User_Pass)) :    # to check whether have registered user
        if str(User_Pass[i].keys())[12:-3] == Lupa :
            Dummy_Lupa.append(str(User_Pass[i].values())[14:-3])
    if len(Dummy_Lupa) > 0 :
        print(f'\n\n HERE IS YOUR PASSWORD : {bcolors.OKCYAN}{Dummy_Lupa[0]}{bcolors.ENDC}')
        Dummy_Lupa.clear()
        Login()
    else :
        print (f'{bcolors.WARNING}Username not yet registered, please registered first{bcolors.ENDC}')
        Login()
        
def GantiPass ():
    Ganti = input('Please input your registered username: ')
    for i in range(len(User_Pass)) :    # to check whether have registered user
        if str(User_Pass[i].keys())[12:-3] == Ganti :
            Pengganti = User_Pass[i][str(User_Pass[i].keys())[12:-3]]
            Dummy_GantiP.append(str(User_Pass[i].values())[14:-3])
            Dummy_GantiU.append(str(User_Pass[i].keys())[12:-3])
    if len(Dummy_GantiU) > 0 :
        PassLama = input('Please input old password : ')
        if PassLama == Pengganti :
            PassBaru = input('Please input new password : ')
            DummyPassword.append(PassBaru)
            while True :
                print(f"{bcolors.OKGREEN}'Type exit, if you want to exit'{bcolors.ENDC}")
                ConfirmPass = input('Re-enter new Password :')
                if ConfirmPass == DummyPassword[0] :        # used index 0 as comparsion since the dummy data will be always cleared later
                    print ('NEW Password has been verified')
                    ConfirmUser = input('Are you sure want to make new UserName (y/n)?'.lower())
                    if ConfirmUser == 'y' :
                        Pengganti = DummyPassword[0]
                        for i in range(len(User_Pass)) :
                            if str(User_Pass[i].keys())[12:-3] == Ganti :
                                User_Pass[i][str(User_Pass[i].keys())[12:-3]] = DummyPassword[0]
                        DummyPassword.clear()
                        Dummy_GantiU.clear()
                        Dummy_GantiP.clear()
                        print (f"{bcolors.OKBLUE} 😊 Password HAS BEEN CHANGED 😊 \n{bcolors.ENDC}")
                        return User_Pass, Login()
                    elif ConfirmUser == 'n':
                        Dummy_GantiU.clear()
                        Dummy_GantiP.clear()
                        DummyPassword.clear()
                        print (f'{bcolors.WARNING}Password Changes cancelled{bcolors.ENDC}')
                        Login()
                        break
                elif ConfirmPass == 'exit' :
                    DummyPassword.clear()
                    Login()
                    break
        else :
            print (f'{bcolors.WARNING}Old password is wrong{bcolors.ENDC}')
            Dummy_GantiU.clear()
            Dummy_GantiP.clear()
            DummyPassword.clear()
            Login()
    else :
        print (f'{bcolors.WARNING}Username not yet registered, please registered first{bcolors.ENDC}')
        DummyPassword.clear()
        Dummy_GantiU.clear()
        Dummy_GantiP.clear()
        Login()
        
# initial function to start the program        
def Login () :
        print(f'''
{'+'*15}{bcolors.OKBLUE} 😊🙋‍♂️ Welcome Visitor! 🙋‍♀️😊 {bcolors.ENDC}{'+'*15}
{bcolors.OKCYAN}Please type 1 to login or
Please type 2 to register or
Please type 3 to {bcolors.WARNING}'forget password' (already registered only){bcolors.ENDC} or
{bcolors.OKCYAN}Please type 4 to {bcolors.WARNING}'change password' (already registered only){bcolors.ENDC}
Type {bcolors.WARNING}'exit' to end your session{bcolors.ENDC}
''')
        # try :   # prevent error to if below wheh  user type alphabetical input
        try :
            LorR = input('Your choice is : ')
            if LorR.lower() == 'exit':
                print (f'{bcolors.OKGREEN}😁 😁 Closing the program, c\'ya 😁 😁{bcolors.ENDC}')
            elif int(LorR) == 1 :
                global InputUser    #to be used on other function
                print(f"\n{'='*15}Log In Menu{'='*15}")
                InputUser = input('Please input Username :')
                InputPass = input('Please input Password:')
                for i in range(len(User_Pass)) :
                    # print(str(User_Pass[i].keys())[12:-3])        # keys from function keys extracted from dicionary will cause error and need to be sliced by convert to string first
                    # print(str(User_Pass[i].values())[14:-3])      # values from function keys extracted from dicionary will cause error and need to be sliced by convert to string first
                    if InputUser == str(User_Pass[i].keys())[12:-3] and InputPass == str(User_Pass[i].values())[14:-3]:
                        Dummy_User_Pass.append(1)
                if len (Dummy_User_Pass) > 0 :
                    JamSek(InputUser)
                    Dummy_User_Pass.clear()
                    return Main_Menu()
                else :
                    print('wrong input')
                    Login()
            elif int(LorR) == 2:
                Registration()
            elif int(LorR) == 3:
                LupaPass()
            elif int(LorR) == 4:
                GantiPass()
        except : 
            print('wrong input')
            Login()

# Date + hour counting
#=================================================================================================================================================================
Today = dt.date.today()
Header = [i for i in Data_Awal[0].keys()]
Sekarang = dt.datetime.now().hour # used to welcome the user later when login


# date counting for expired goods
def SData ():
    print(f'{bcolors.UNDERLINE}{Header[0]:<8}{Header[1]:<13}{Header[2]:<13}{Header[3]:<5}{Header[4]:<13}{Header[5]:<13}{bcolors.ENDC}') #for header
    for i in range(len(Data_Awal)): #looping to print data
        if Today >= (dt.datetime.strptime(Data_Awal[i]['Expired_Date'], "%d/%m/%Y").date()) : # for formatting expired_date on databased into dateandtime type data
            Data_Awal[i]['Status'] = f'{bcolors.WARNING}Expired{bcolors.ENDC}'                # therefore it could be compared with variable 'sekarang' and will fill 
        else :                                                                                # conditional formatting, oherwise error
            Data_Awal[i]['Status'] = f'{bcolors.OKCYAN}Still Good{bcolors.ENDC}'
        print(f"{Data_Awal[i]['Index']:<8}{Data_Awal[i]['Item']:<13}{Data_Awal[i]['Location']:<13}{Data_Awal[i]['Qty']:<5}{Data_Awal[i]['Expired_Date']:<13}{Data_Awal[i]['Status']:<13}")
    return Data_Awal

def SData3 ():
    print(f'{bcolors.UNDERLINE}{Header[0]:<8}{Header[1]:<13}{Header[2]:<13}{Header[3]:<5}{Header[4]:<13}{Header[5]:<13}{bcolors.ENDC}') # for header
    for i in range(len(Dummy_S3)): #looping to print data
        if Today >= (dt.datetime.strptime(Dummy_S3[i]['Expired_Date'], "%d/%m/%Y").date()) :
            Dummy_S3[i]['Status'] = f'{bcolors.WARNING}Expired{bcolors.ENDC}'
        else :
            Dummy_S3[i]['Status'] = f'{bcolors.OKCYAN}Still Good{bcolors.ENDC}'
        print(f"{Dummy_S3[i]['Index']:<8}{Dummy_S3[i]['Item']:<13}{Dummy_S3[i]['Location']:<13}{Dummy_S3[i]['Qty']:<5}{Dummy_S3[i]['Expired_Date']:<13}{Dummy_S3[i]['Status']:<13}")

# hour counting for morning, afternoon and evening
def JamSek(InputUser) :    
    if Sekarang > 5 and Sekarang < 11 :
        print (f'{bcolors.OKGREEN}おはよう \nGood morning 😇🌞,{bcolors.OKCYAN}{InputUser}{bcolors.ENDC}')
    elif Sekarang >= 11 and Sekarang <= 18 :
        print (f'{bcolors.OKGREEN}こんにちは, 今日は \nGood afternoon 😇🌥️,{bcolors.OKCYAN}{InputUser}{bcolors.ENDC}')
    else :
        print (f'{bcolors.OKGREEN}こんばんは, 今日は \nGood evening 😇🌙,{bcolors.OKCYAN}{InputUser}{bcolors.ENDC}')

            
#func find index
#=================================================================================================================================================================
def FIndex() :    
    for a in range(len(Data_Awal)) :
        if Data_Awal[a]['Index'] == Find_Index :
            print(f'{bcolors.UNDERLINE}{Header[0]:<8}{Header[1]:<13}{Header[2]:<13}{Header[3]:<5}{Header[4]:<13}{Header[5]:<13}{bcolors.ENDC}') #for header
            if Today >= (dt.datetime.strptime(Data_Awal[a]['Expired_Date'], "%d/%m/%Y").date()) :
                Data_Awal[a]['Status'] = f'{bcolors.WARNING}Expired{bcolors.ENDC}'
            else :
                Data_Awal[a]['Status'] = f'{bcolors.OKCYAN}Still Good{bcolors.ENDC}'
            print(f"{Data_Awal[a]['Index']:<8}{Data_Awal[a]['Item']:<13}{Data_Awal[a]['Location']:<13}{Data_Awal[a]['Qty']:<5}{Data_Awal[a]['Expired_Date']:<13}{Data_Awal[a]['Status']:<13}")
            Selection_Data.append(Data_Awal[a])
    if len(Selection_Data) == 0 :
        print(f'{bcolors.WARNING}Data not found{bcolors.ENDC}')
    return Selection_Data

        
def FItem() :    
    for a in range(len(Data_Awal)) :
        if Data_Awal[a]['Item'] == Find_item :
            print(f'{bcolors.UNDERLINE}{Header[0]:<8}{Header[1]:<13}{Header[2]:<13}{Header[3]:<5}{Header[4]:<13}{Header[5]:<13}{bcolors.ENDC}') #for header
            if Today >= (dt.datetime.strptime(Data_Awal[a]['Expired_Date'], "%d/%m/%Y").date()) :
                Data_Awal[a]['Status'] = f'{bcolors.WARNING}Expired{bcolors.ENDC}'
            else :
                Data_Awal[a]['Status'] = f'{bcolors.OKCYAN}Still Good{bcolors.ENDC}'
            print(f"{Data_Awal[a]['Index']:<8}{Data_Awal[a]['Item']:<13}{Data_Awal[a]['Location']:<13}{Data_Awal[a]['Qty']:<5}{Data_Awal[a]['Expired_Date']:<13}{Data_Awal[a]['Status']:<13}")
            Selection_Data.append(Data_Awal[a])
    if len(Selection_Data) == 0 :
        print(f'{bcolors.WARNING}Data not found{bcolors.ENDC}')
    return Selection_Data
    
#=================================================================================================================================================================

def Main_Menu() :
    # while True :
        try :
            print (f'''
    {'='*15}{bcolors.OKBLUE} Warehouse Stocks Management {bcolors.ENDC}{'='*15}
    😊 Welcome {bcolors.OKCYAN}{InputUser.capitalize()}{bcolors.ENDC}! 😊
    {bcolors.OKGREEN}{dt.datetime.now().strftime("%A, %d %b %Y %H:%M:%S")}{bcolors.ENDC}
    {bcolors.UNDERLINE}Main Menu :{bcolors.ENDC}
    1. Query Database
    2. Register / Add New Items
    3. Update data
    4. Delete data
    5. Exit program''')
            Opsi_Menu = int(input('Please input menu number to run the program : '))
            if Opsi_Menu == 1 :
                Sub_Menu_1()
            elif Opsi_Menu == 2 :
                Sub_Menu_2()
            elif Opsi_Menu == 3 :
                Sub_Menu_3()
            elif Opsi_Menu == 4 :
                Sub_Menu_4()
            elif Opsi_Menu == 5 :
                print (f'{bcolors.OKGREEN}😁 😁 Closing the program, c\'ya 😁 😁{bcolors.ENDC}')
                return Data_Awal
            else :
                print(f'{bcolors.WARNING}INPUT MUST BE NUMBERS 1-5{bcolors.ENDC}')
                Main_Menu()
        except :
            print(f'{bcolors.WARNING}ONLY NUMBERS 1-5 ALLOWED FOR INPUT{bcolors.ENDC}')
            Main_Menu()

#func sub menu
#=================================================================================================================================================================
def Sub_Menu_1 () :        
    global Find_Index
    global Find_item
    # while True :
    while True :
        try :
            print (f'''
                
    {JamSek(InputUser)}
    {bcolors.UNDERLINE}Sub Menu 1 (QUERY) :{bcolors.ENDC}
    1. Query all data
    2. Query specified data (can input index or items)
    3. Back to main menu''')
            Sub_Menu_1 = int(input('Please input menu number to run \'Sub Menu 1\' :'))
            if Sub_Menu_1 == 1 :
                if len(Data_Awal) != 0 :
                    SData()
                else :
                    print(f'{bcolors.WARNING}Data not found{bcolors.ENDC}')
            elif Sub_Menu_1 == 2 :
                if len(Data_Awal) != 0 :
                    MFind = int(input (f'{bcolors.OKCYAN}>> Which one you prefer for query?\n Please input{bcolors.ENDC}\n1 for index \n2 for item\n'))
                    try :
                        if MFind == 1 :
                            Find_Index = int(input('Please input the Index for query : '))
                            FIndex()
                            Selection_Data.clear()
                        elif MFind == 2 :
                            Find_item = input('Please input the Item for query : ').capitalize()
                            FItem()
                            Selection_Data.clear()
                        else :    
                            print(f'{bcolors.WARNING}Please enter number 1-2{bcolors.ENDC}')
                        pass
                    except :
                        print(f'{bcolors.WARNING}Please enter correctly{bcolors.ENDC}')
                else :
                    print(f'{bcolors.WARNING}Data not found{bcolors.ENDC}')
                
            elif Sub_Menu_1 == 3 :
                    print(f'{bcolors.OKCYAN}Heading to main menu🐾🐾🐾{bcolors.ENDC}')
                    Selection_Data.clear()
                    return Main_Menu()
            else :
                pass
        except :
            print (f'{bcolors.WARNING}Please enter number 1-3{bcolors.ENDC}')
    
def Sub_Menu_2 () :        
    while True :
        try :
            print (f'''
            
    {JamSek(InputUser)}
    {bcolors.UNDERLINE}Sub Menu 2 (ADD DATA):{bcolors.ENDC}
    1. Create new entry
    2. Back to main menu''')
            Sub_Menu_2 = int(input('Please input menu number to run \'Sub Menu 2\' :'))
            if Sub_Menu_2 == 1 :
                try :
                    Index =int(input (f'Please input the new {Header[0]} : '))
                    check = len(Data_Awal)
                    for q in range(len(Data_Awal)) :
                        if Index != Data_Awal[q]['Index'] :
                            Dummy_S2a.append(Index)
                    if len(Dummy_S2a) == check :
                        Item        =input (f'\nPlease input the new {Header[1]}\t:').capitalize()
                        Location    =input (f'Please input the new {Header[2]}\t:').capitalize()
                        Qty         =input (f'Please input the new {Header[3]}\t:')
                        Expired_Date=input (f'Please input the new {Header[4]} \n{bcolors.WARNING}Please input correctly based on format on date \nor it will causing error (ex:"27/01/2021" or "dd/mm/yyyy) {bcolors.ENDC}: ')
                        Dummy_S2a.clear()
                        Dummy_S2.append({
                            'Index' : Index,
                            'Item' : Item,
                            'Location' : Location,
                            'Qty' : Qty,
                            'Expired_Date' : Expired_Date,
                            'Status' : ''
                            })
                        print (f"{'='*15} Addtitional Data {'='*15}")
                        print (f'{bcolors.UNDERLINE}{Header[0]:<8}{Header[1]:<13}{Header[2]:<13}{Header[3]:<5}{Header[4]:<13}{Header[5]:<13}{bcolors.ENDC}')
                        for o in range (len(Dummy_S2)) :
                            if Today >= (dt.datetime.strptime(Dummy_S2[o]['Expired_Date'], "%d/%m/%Y").date()) :
                                Dummy_S2[o]['Status'] = f'{bcolors.WARNING}Expired{bcolors.ENDC}'
                            else :
                                Dummy_S2[o]['Status'] = f'{bcolors.OKCYAN}Still Good{bcolors.ENDC}'
                            print(f"{Dummy_S2[o]['Index']:<8}{Dummy_S2[o]['Item']:<13}{Dummy_S2[o]['Location']:<13}{Dummy_S2[o]['Qty']:<5}{Dummy_S2[o]['Expired_Date']:<13}{Dummy_S2[o]['Status']:<13}")
                        while True :
                            Saved_Data = input('Do you want to save the changes (y/n)? ').lower()
                            if Saved_Data == 'y' :
                                Data_Awal.extend(Dummy_S2)
                                print (f'{bcolors.OKCYAN}😀 Data has been added successfuly 😀{bcolors.ENDC}')
                                print (f"{'='*15} {bcolors.OKBLUE}NEW Data Result {bcolors.ENDC}{'='*15}")
                                Dummy_S2.clear()
                                SData()
                                break
                            elif Saved_Data == 'n':
                                print (f'{bcolors.WARNING}😢 Data HAS NOT BEEN ADDED as your request 😢{bcolors.ENDC}')
                                Dummy_S2.clear()
                                break
                            else :
                                print (f'{bcolors.WARNING}Please enter only y/n{bcolors.ENDC}')
                    elif len(Dummy_S2a) < check :
                        print(f'{bcolors.WARNING}Data already exist{bcolors.ENDC}')
                        Dummy_S2a.clear()
                except :
                    print (f'{bcolors.WARNING}Please enter correctly{bcolors.ENDC}')
                    Dummy_S2.clear()
            elif Sub_Menu_2 == 2 :
                print(f'{bcolors.OKCYAN}Heading to main menu🐾🐾🐾{bcolors.ENDC}')
                return Main_Menu()
            else :
                print (f'{bcolors.WARNING}Please enter number 1-2{bcolors.ENDC}')
        except :
            print (f'{bcolors.WARNING}Please enter correctly{bcolors.ENDC}')
    
def Sub_Menu_3 () :        
    while True :
        Copy_Data = Data_Awal.copy() # need to be copy since dollection data is a reference when it is assign, if not copy changes will directly changes data_awal
        try :                        # even when the values is not yet confirmed to be saved
            global Header
            print (f'''

    {JamSek(InputUser)}
    {bcolors.UNDERLINE}Sub Menu 3 (UPDATE DATA):{bcolors.ENDC}
    1. Update data
    2. Back to main menu''')
            Sub_Menu_3 = int(input('Please input menu number to run \'Sub Menu 3\' :'))
            if Sub_Menu_3 == 1 :
                try :
                    SData()
                    Index =int(input (f'Please input the {Header[0]} you wish to update : '))
                    for q in range(len(Copy_Data)) :
                        if Index == Copy_Data[q]['Index'] :
                            Dummy_S3.append(Copy_Data[q].copy()) # need to be copy since dollection data is a reference when it is assign, if not copy changes will directly changes data_awal
                    if len(Dummy_S3) > 0 :                       # even when the values is not yet confirmed to be saved
                        while True :
                            print(f'''
    Please input the data needs to be updated
    1. 'I' for {Header[1]} to update {Header[1]}
    2. 'L' for {Header[2]} to update {Header[2]}
    3. 'Q' for {Header[3]} to update {Header[3]}
    4. 'E' for {Header[4]} to update {Header[4]}
    5. 'Save' to keep the updates
    6. 'Exit' go to  previous Sub Menu 3''')
                            Confirmation = input(f'Please input initial alphabet (ex:"L","Q") / "save" / "exit" to update: ')
                            Confirmation = Confirmation.lower()

                            if Confirmation == 'i' or Confirmation == 'item' :                    
                                Item        =input (f'Please input the update {Header[1]} name :')
                                Dummy_S3[0][Header[1]] = Item.capitalize()
                                SData3()
                            elif Confirmation == 'l' or Confirmation == 'location' :                    
                                Location    =input (f'Please input the update {Header[2]} stored :')
                                Dummy_S3[0][Header[2]] = Location.capitalize()
                                SData3()
                            elif Confirmation == 'q' or Confirmation == 'qty' :                    
                                Qty         =(input (f'Please input the update {Header[3]} :'))
                                Dummy_S3[0][Header[3]] = Qty
                                SData3()
                            elif Confirmation == 'e' or Confirmation =='expired_date' :                    
                                Expired_Date=input (f'{bcolors.WARNING}Please input the update {Header[4]} correctly based on format on date \nor it will causing error (ex:"27/01/2021" or "dd/mm/yyyy) {bcolors.ENDC}: ')
                                Dummy_S3[0][Header[4]] = Expired_Date
                                SData3()
                            elif Confirmation == 'exit' :
                                Dummy_S3.clear()
                                break                    
                            elif Confirmation == 'save' :
                                while True :
                                    Save_Data = input ('Do you want save it (y/n)? ').lower()
                                    if Save_Data == 'y' or Save_Data =='yes' :
                                        for aa in range(len(Data_Awal)) :
                                            if Dummy_S3[0][Header[0]] == Data_Awal[aa][Header[0]] :
                                                Data_Awal[aa][Header[1]] = Dummy_S3[0][Header[1]]
                                                Data_Awal[aa][Header[2]] = Dummy_S3[0][Header[2]]
                                                Data_Awal[aa][Header[3]] = Dummy_S3[0][Header[3]]
                                                Data_Awal[aa][Header[4]] = Dummy_S3[0][Header[4]]
                                        print (f"{bcolors.OKCYAN}😀Data has been updated 😀{bcolors.ENDC}")
                                        print (f"{'='*15} {bcolors.OKBLUE}Update Data Result {bcolors.ENDC}{'='*15}")
                                        Dummy_S3.clear()
                                        SData()
                                        break
                                    elif Save_Data == 'n' or Save_Data =='no' :
                                        print (f"{bcolors.WARNING}😢 Data HAS BEEN NOT UPDATE as your request 😢{bcolors.ENDC}")
                                        Dummy_S3.clear()
                                        SData()
                                        break
                                    else :
                                        print (f'{bcolors.WARNING}Please only input y/n{bcolors.ENDC}')
                            else :
                                print(f'{bcolors.WARNING}Please input the correct menu (I/L/Q/E/S/"exit"/"save"){bcolors.ENDC}')        
                                Dummy_S3.clear() 
                    else :
                        print(f'{bcolors.WARNING}Data not found{bcolors.ENDC}')
                        Dummy_S3.clear()
                except :
                    print (f'{bcolors.WARNING}Please only input number{bcolors.ENDC}')
                    Dummy_S3.clear()
            elif Sub_Menu_3 == 2 :
                print(f'{bcolors.OKCYAN}Heading to main menu🐾🐾🐾{bcolors.ENDC}')
                Dummy_S3.clear()
                return Main_Menu()

            else :
                print (f'{bcolors.WARNING}Please enter number correctly{bcolors.ENDC}')
                Dummy_S3.clear()
        except :
            print (f'{bcolors.WARNING}Please enter number correctly{bcolors.ENDC}')
            Dummy_S3.clear()
    
def Sub_Menu_4 () :       
    while True : 
        try :
            print (f'''

    {JamSek(InputUser)}
    {bcolors.UNDERLINE}Sub Menu 4 (TERMINATE DATA):{bcolors.ENDC}
    1. Terminate data
    2. Back to main menu''')
            Sub_Menu_4 = int(input('Please input menu number to run \'Sub Menu 4\' :'))
            while True :
                if Sub_Menu_4 == 1 :
                    if len (Data_Awal) == 0 :
                        print(f'{bcolors.WARNING}Data not found{bcolors.ENDC}')
                        break
                    elif len (Data_Awal) > 0:
                        try :
                            SData()
                            Index =int(input (f'Please input {Header[0]} you wish to delete : '))
                            for q in range(len(Data_Awal)) :
                                if Index == Data_Awal[q]['Index'] :
                                    IndexHapus = q
                                    Dummy_S4.append(Data_Awal[q])
                            if len (Dummy_S4) > 0 :
                                print (f'{bcolors.UNDERLINE}{Header[0]:<8}{Header[1]:<13}{Header[2]:<13}{Header[3]:<5}{Header[4]:<13}{Header[5]:<13}{bcolors.ENDC}')
                                print(f"{Dummy_S4[0]['Index']:<8}{Dummy_S4[0]['Item']:<13}{Dummy_S4[0]['Location']:<13}{Dummy_S4[0]['Qty']:<5}{Dummy_S4[0]['Expired_Date']:<13}{Dummy_S4[0]['Status']:<13}")                    
                                Confirmation = input ('Are you sure you want to delete the data (y/n)? ').lower()
                                if Confirmation == 'y' or Confirmation =='yes' :
                                    del Data_Awal[IndexHapus]
                                    print (f"{bcolors.OKCYAN}😀 Data has been deleted 😀{bcolors.ENDC}")
                                    print (f"{'='*15} {bcolors.OKBLUE}Deleted Data Result{bcolors.ENDC} {'='*15}")
                                    SData()
                                    Dummy_S4.clear()
                                    break
                                elif Confirmation == 'n' or Confirmation =='no' :
                                    print (f"{bcolors.WARNING}😢 Data HAS NOT been deleted as your request 😢{bcolors.ENDC}")
                                    Dummy_S4.clear()
                                    break
                                else :
                                    print (f'{bcolors.WARNING}Please only input y/n{bcolors.ENDC}') 
                            else : 
                                print (f'{bcolors.WARNING}DATA NOT FOUND{bcolors.ENDC}')
                                Dummy_S4.clear()
                                break             
                        except :
                            print (f'{bcolors.WARNING}Please only input number{bcolors.ENDC}')
                            Dummy_S4.clear()
                            break
                elif Sub_Menu_4 == 2 :
                    print(f'{bcolors.OKCYAN}Heading to main menu🐾🐾🐾{bcolors.ENDC}')
                    return  Data_Awal,Main_Menu()
                else :
                    break
        except :
            print (f'{bcolors.WARNING}Please enter number correctly{bcolors.ENDC}')
                

Login()
