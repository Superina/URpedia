"""This program makes tables with random data"""



import csv 
import random

littlealpha = "abcdefghijklmnopqrstuvwxyz"
bigalpha = littlealpha.upper()
otherchar = "!$@#%*&^"
charlist = [bigalpha, littlealpha, otherchar]
fieldlist = ["Mathematics", "Physics", "Data Science",
             "Chemistry", "Computer Science", "Analysis", "Complex Analysis",
             "Real Analysis", "Algebra", "Theoretical Physics",
             "Database Systems", "Unspecified"]
def subfieldof(arg):
    if arg == "Real Analysis":
        return "Analysis"
    if arg == "Complex Analysis":
        return "Analysis"
    if arg == "Analysis":
        return "Mathematics"
    if arg == "Algebra":
        return "Mathematics"
    if arg == "Theoretical Physics":
        return "Physics"
    if arg == "Database Systems":
        return "Computer Science"
    else:
        return ""

  
# this is for creating random password
# password length range from 8 to 30


"""
def makepass():
    ListOfNumbers=[]
    adigit=random.randint(8,30)
    for i in range(adigit):
        ListOfNumbers.append(random.randint(0,9))
        temp=map(str,ListOfNumbers)
        password=''.join(temp)
    #print(password)
    return password 

"""
  
""" User(Password:varchar(25) NOT NULL, Username: varchar(25), Registration_Date: date NOT NULL, Num_of_Art_Edited: int DEFAULT 0,
    First_Name:varchar(20) NOT NULL,  Last_Name:varchar(20) NOT NULL, Salt:varchar(20) NOT NULL)"""

def makeusername():
    namelen = random.randint(4, 30)
    namestr = ''
    for i in range(namelen):
        #print(charlist)
        whichchar = charlist[random.randint(0,len(charlist)-1)]
        namestr = namestr + whichchar[random.randint(0,len(whichchar)-1)]
    return namestr

def makepassword():
    namelen = random.randint(8, 30)
    passstr = ''
    for i in range(namelen):
        #print(charlist)
        whichchar = charlist[random.randint(0,len(charlist)-1)]
        passstr = passstr + whichchar[random.randint(0,len(whichchar)-1)]
    return passstr

def makeregistration_date():
    daymonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = random.randint(1, 12)
    dayrange = daymonth[month -1]
    day = random.randint(1, dayrange)
    daystr = str(day)
    if len(daystr) == 1:
        daystr = "0" + daystr
    year = random.randint(1950, 1999)
    monthstr = str(month)
    if len(monthstr) == 1:
        monthstr = "0" + monthstr
    return  str(year) + "-" + monthstr + "-" + daystr 
    

def makenum_of_art_edited():
    valuelist = [0, min([random.randint(0,200), random.randint(0,200)]),
                 min([random.randint(0,200), random.randint(0,200)]),
                 min([random.randint(0,200), random.randint(0,200)]),
                 min([random.randint(0,200), random.randint(0,200)])]
    return valuelist[random.randint(0,4)]

def makefirst_name():
    namestr = bigalpha[random.randint(0,25)]
    namelen = random.randint(5,14)
    for i in range(namelen):
        namestr = namestr + littlealpha[random.randrange(0,25)]
    return namestr
    
def makelast_name():
    namestr = bigalpha[random.randint(0,25)]
    namelen = random.randint(5,14)
    for i in range(namelen):
        namestr = namestr + littlealpha[random.randrange(0,25)]
    return namestr

def makesalt():     #Time of registration
    hour = random.randint(0,23)
    minute = random.randrange(0,59)
    second = random.randint(0,59)
    timesalt = str(hour) + ":" + str(minute) + ":" + str(second)
    return timesalt

def makelevel():
    return str(random.randint(1,4))

def admintype():
    typelist = []
    superstatus = ["1", "0"]
    issuper = random.randint(0,3)
    if issuper > 0:
        typelist.append(superstatus[0])
    else:
        typelist.append(superstatus[1])
    hasfield = random.randint(0,2)
    if hasfield == 0 and typelist[0] == "1":
        typelist.append("")
    else:
        typelist.append(fieldlist[random.randint(0, len(fieldlist)-1) ] )
    return typelist

def makearticle_title():
    namestr = bigalpha[random.randint(0,25)]
    namelen = random.randint(5,14)
    for i in range(namelen):
        namestr = namestr + littlealpha[random.randrange(0,25)]
    return namestr

def makelast_edited():
    daymonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = random.randint(1, 12)
    dayrange = daymonth[month -1]
    day = random.randint(1, dayrange)
    daystr = str(day)
    if len(daystr) == 1:
        daystr = "0" + daystr
    year = random.randint(2010, 2017)
    monthstr = str(month)
    if len(monthstr) == 1:
        monthstr = "0" + monthstr
    return  str(year) + "-" + monthstr + "-" + daystr 

def makefield():
    whichfield = random.randint(0, len(fieldlist) -1)
    return fieldlist[whichfield]
    

    
def main():
    usernamelist = []
    regdatelist = []
    
    f = open("user.csv", "wt")
    try:  
        writer = csv.writer(f)
        #writer.writerow( ["Username", "Password", "Registration_Date", "Num_of_Art_Edited",
        #"First_Name", "Last_Name", "Salt"] )
        for i in range(1000):
            username = makeusername() 
            if not (username in usernamelist): # check if username already exists
                usernamelist.append(username)
                writer.writerow( [username, makepassword(),
                                  makeregistration_date(), makenum_of_art_edited(),
                                  makefirst_name(), makelast_name(), makesalt()] )
        usernamelist.append("DELETED")
        writer.writerow( ["DELETED", "DELETED",
                                  "0000-00-00", "0",
                                  "DELETED", "DELEDTED", "00:00:00"] )
                
          
    finally:
        f.close()

    
    
    f = open("field.csv", "wt")
    try:  
        writer = csv.writer(f)
        #writer.writerow( ["Field", "Subfield_Of"] )
        for i in fieldlist:
            writer.writerow( [i, subfieldof(i)] )
          
    finally:
        f.close()
    

    f = open("admin.csv", "wt")
    try:
        adminlist = []
        adminfieldlist = []
        writer = csv.writer(f)
        #writer.writerow( ["AdminID", "Genre", "SuperAdmin"] )
        for i in range(0, len(usernamelist), 20 ):
            admintypelist = admintype()
            is_super = admintypelist[0]
            adminfield = admintypelist[1]
            adminlist.append(usernamelist[i])
            adminfieldlist.append(adminfield)
            writer.writerow( [usernamelist[i], adminfield, is_super ] )
          
    finally:
        f.close()

    f = open("has_experience.csv", "wt")
    try:        
        writer = csv.writer(f)
        #writer.writerow( ["Username", "Field", "Level"] )
        for i in range(0, len(usernamelist), 6 ):
            if usernamelist[i] in adminlist:
                continue
            else:              
                writer.writerow( [usernamelist[i],
                                  fieldlist[random.randint(0, len(fieldlist)-1)]
                                  , str(random.randint(1, 4)) ] )
        for i in range(0, len(adminlist)):
            if len(adminfieldlist[i]) > 1:
                writer.writerow( [adminlist[i],
                                  adminfieldlist[i]
                                  , str(random.randint(1, 4)) ] )
          
    finally:
        f.close()

    f = open("article.csv", "wt")
    try:        
        writer = csv.writer(f)
        #writer.writerow( ["Article_ID", "Article_Title", "Last_Edited",
                          #"Editing_Level", "Creator", "Belongs_To"] )
        art_id = 1
        for i in range(0,1500):
            art_idstr = "0"*(12-len(str(art_id)))+ str(art_id)
            writer.writerow( [art_idstr, makearticle_title(), makelast_edited(),
                              makelevel(),
                              usernamelist[random.randint(0, len(usernamelist)-1)],
                              makefield()] )
            art_id = art_id + 1
            #print(art_idstr)
          
    finally:
        f.close()

    
main()

  
