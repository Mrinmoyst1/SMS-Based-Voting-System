import serial
import time

#For postgreSQL Database
import psycopg2

#For twilio messaging
from twilio.rest import Client

#For thingspeak
import urllib.request
import requests
import threading
import json
import random
def thingspeak_post(x,y,z):
    threading.Timer(15,thingspeak_post).start()
    
    URl='https://api.thingspeak.com/update?api_key='
    KEY='7F235N7O3*****'
    HEADER='&field1={}&field2={}&field3={}'.format(x,y,z)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)



cnt=0
nid = 0
phn = 0
w = 0
vot = 0
vote = ""
stat = "DONE"

A = 0
B = 0
C = 0

ser = serial.Serial('COM3',baudrate = 115200, timeout=1)

account_sid = 'AC1ec064cdf4480fc5826b8******'
auth_token = '2d7bcf34b93b21ad3b916*******'
client = Client(account_sid, auth_token)




try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "*****",
                                  host = "localhost",
                                  port = "****",
                                  database = "Vot4u")
                                                           
   
    cursor = connection.cursor()
       
    
          
    postgreSQL_select_Query = "select * from Voters"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    Vote = cursor.fetchall()


    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)



while 1:
    arduinoData = ser.readline().decode('ascii')
    arduinoData = arduinoData.replace("\r","")
    arduinoData = arduinoData.replace("\n","")
    if arduinoData:
       cnt+=1
       if cnt==1:
           a=arduinoData.split('\"')
           print(a)
           a[1]=str(a[1])
           
           for row in Vote:
               
               if (row[2]==a[1]):
                   phn+=1
                   row_count = cursor.rowcount
                   
                   
       
       elif cnt==2:
           b=arduinoData.split()
           b[0]=int(b[0])
           vote = str(b[1])
           for row in Vote:
               
               if (row[0]==b[0]):
                  np = "select * from voters where nid = %s and phone = %s"
                  cursor.execute(np, (b[0],a[1]))
                  npe = cursor.fetchall() 
                  for row in npe: 
                     if (row[2]==a[1]):
                        nid+=1 
                        row_count = cursor.rowcount
                  
           
           
        # First step
    if phn == 1 and cnt == 2:
         if nid == 1 :
                      if (b[1].upper() == 'A'):
                           sq = "select * from voters where nid = %s"
                           cursor.execute(sq, (b[0],))
                           rec = cursor.fetchall()
                           for row in rec:                 
                                if row[3] == "N/A":                 
                                    sq2 = """Update voters set status = %s , time = %s where nid = %s"""
                                    cursor.execute(sq2, (stat,a[3],b[0]))
                                    connection.commit()
                                    A+=1  
                                    print("Voted Soccessfully")
                                    message = client.messages \
                                                    .create(
                                                         body= "You have successfully voted on the test SMS voting platform 'Vot4u' ",
                                                         from_='+1510400****',
                                                         to=a[1]
                                                     )
                                    #print(message.sid)                 
                                    phn = 0                          
                                    cnt = 0
                                    nid = 0         
                                elif row[3] == "DONE":
                                    print("Vote didn't cast. ")
                                    message = client.messages \
                                                    .create(
                                                         body="Several attempts. Please use a valid NID no. and a valid phone number to vote on the test SMS voting platform 'Vot4u' ",
                                                         from_='+1510400****',
                                                         to=a[1]
                                                     )
                                   # print(message.sid)                                                           
                                    phn = 0                          
                                    cnt = 0
                                    nid = 0
                                               
                      elif (b[1].upper() == 'B'):
                           sq = "select * from voters where nid = %s"
                           cursor.execute(sq, (b[0],))
                           rec = cursor.fetchall()
                           for row in rec:                 
                                if row[3] == "N/A":                 
                                    sq2 = """Update voters set status = %s , time = %s where nid = %s"""
                                    cursor.execute(sq2, (stat,a[3],b[0]))
                                    connection.commit()
                                    B+=1  
                                    print("Voted Soccessfully")
                                    message = client.messages \
                                                    .create(
                                                         body="You have successfully voted on the test SMS voting platform 'Vot4u' ",
                                                         from_='+1510400****',
                                                         to=a[1]
                                                     )
                                   # print(message.sid)
                                    phn = 0                          
                                    cnt = 0
                                    nid = 0         
                                elif row[3] == "DONE":
                                    print("Vote didn't cast. ") 
                                    print("Vote didn't cast. ")
                                    message = client.messages \
                                                    .create(
                                                         body="Several attempts. Please use a valid NID no. and a valid phone number to vote on the test SMS voting platform 'Vot4u' ",
                                                         from_='+1510400****',
                                                         to=a[1]
                                                     )
                                   # print(message.sid)                                                          
                                    phn = 0                          
                                    cnt = 0
                                    nid = 0
                      elif (b[1].upper() == 'C'):
                           sq = "select * from voters where nid = %s"
                           cursor.execute(sq, (b[0],))
                           rec = cursor.fetchall()
                           for row in rec:                 
                                if row[3] == "N/A":                 
                                    sq2 = """Update voters set status = %s , time = %s where nid = %s"""
                                    cursor.execute(sq2, (stat,a[3],b[0]))
                                    connection.commit()
                                    C+=1  
                                    print("Voted Soccessfully")
                                    message = client.messages \
                                                    .create(
                                                         body="You have successfully voted on the test SMS voting platform 'Vot4u' ",
                                                         from_='+1510400****',
                                                         to=a[1]
                                                     )
                                   # print(message.sid)
                                    phn = 0                          
                                    cnt = 0
                                    nid = 0         
                                elif row[3] == "DONE":
                                    print("Vote didn't cast. ") 
                                    print("Vote didn't cast. ")
                                    message = client.messages \
                                                    .create(
                                                         body="Several attempts. Please use a valid NID no. and a valid phone number to vote on the test SMS voting platform 'Vot4u' ",
                                                         from_='+1510400****',
                                                         to=a[1]
                                                     )
                                   # print(message.sid)                                                          
                                    phn = 0                          
                                    cnt = 0
                                    nid = 0     

                      
                          
                      else :
                           print("Invalid voting option. Please type A, B or C ")
                           message = client.messages \
                                                    .create(
                                                         body="Invalid voting option. Please type A, B or C to vote on 'Vot4u'",
                                                         from_='+1510400****',
                                                         to=a[1]
                                                     )
                           #print(message.sid)
                           phn = 0
                           nid = 0
                           cnt = 0 

                      print("A:",A," B:",B," C:",C)  
                      thingspeak_post(A,B,C)        
          
                      
  

         elif nid == 0 :
            print("You aren't a voter. Please register as a voter next time. ")
            message = client.messages \
                            .create(
                                 body="You aren't a voter. Please register as a voter next time. -Regards 'Vot4u'",
                                 from_='+1510400****',
                                 to=a[1]
                             )
           # print(message.sid)
            
            phn = 0
            cnt = 0    


        
     
    # second step 
    elif phn == 0 and cnt == 2:
      if nid == 1:
        print("You can't vote from this number ", a[1])
        message = client.messages \
                        .create(
                            body="Please use your registered phone number to vote on the test SMS voting platform 'Vot4u'",
                            from_='+1510400****',
                            to=a[1]
                         )
       # print(message.sid)
        phn = 0
        nid = 0
        cnt = 0
        
      elif nid == 0:
        print(b[0], "You are not a voter ") 
        message = client.messages \
                        .create(
                            body="You aren't a voter. Please register as a voter next time. -Regards 'Vot4u'",
                            from_='+1510400****',
                            to=a[1]
                         )
      #  print(message.sid)
        phn = 0
               
        cnt = 0
    
  
              
              
      
        
