"""
Customer Management System:
Add Customer
Search Customer
Delete Customer
Modify Customer

Display All Customers

requirement


customer id_list 
customer name
customer age
customer addar number
customer phone number
customer email id
customer pan number
customer pin code
customer city
customer state

"""

id_list=[10,20,30,40]
name_list=["Deepak","sujit","dipu","ranjit"]
age_list=[21,22,23,21 ]
addar_list=[58599655,3695266955,96225633,8549632522 ]
phone_list=[568542,5826569,859658,8574552]
email_list=["deepak5ikuamr@7855","manoj@4552","dilkhush@74585","sujit@859654"]
pan_number_list=["SDREGH854796","GDURD8547125","JJDK647215","DJJRKM854921"]
pin_code_list=[45852,843324,843306,8485585]
city_list=["delhi","sitamarhi","noida","mohali"]
state_list=["delhi","Bihar","up","pujab"]



while (1):
    print("WELCOME TO CMS")
    choice=input("""enter the your choic:1 addcust,2 searchcust,3
                 deletecust,4 modifycust,5 displayall,6 ban customer ,7 exit=""")
    print("Thankyou")
#Add customer
    if choice=="1":
        


        cust_id=int(input("enetr the customer id:"))
        cust_name =input("enetr the customer name:")
        cust_age = int(input("enter the customer age:"))
        cust_addar =int(input("enter the customer addar:"))
        cust_phone=input("enter the phone number:")
        cust_email=input("enter the customer email:")
        cust_pan_number=input("enter the customer :")
        cust_pin_code_list=input("enter the customer pin code:")
        cust_city=input("enter the customer city:")
        cust_state=input("enter the cust state:")

        #print("Cust ID:",cust_id)
        id_list.append(cust_id)
        name_list.append(cust_name)
        age_list.append(cust_age)
        addar_list.append(cust_addar)
        phone_list.append(cust_phone)
        email_list.append(cust_email)
        pan_number_list.append(cust_pan_number)
        pin_code_list.append(cust_pin_code_list)
        city_list.append(cust_city)
        state_list.append(cust_state)
        

        print("cust id",cust_id)
        print("Cust Name:",cust_name)
        print("cust age:",cust_age)
        print("cust addar:",cust_addar)
        print("cust phone number:",cust_phone)
        print("cust email id is:",cust_email)
        print("cust pan number is:",cust_pan_number)
        print("cust pin code is:",cust_pin_code_list)
        print("the city of cust is:",cust_city)
        print("the state if cust is:",state_list)

#Search Customer 
    

    if choice=="2":

        id=int(input("Enter Cust Id:")) #id=20
        # nm=input("enter the cust name:")
        i=id_list.index(id) 
        


        print("Cust ID is:",id)
        print("Cust Name is:",name_list[i])
        print("Cust Age is:",age_list[i])
        print("cust addar number is:",addar_list[i])
        print("cust email id is:",email_list[i])
        print("cust pan number is :",pan_number_list[i])

        print("cust pin code is:",pin_code_list[i])
        print("cust city is:",city_list[i])
        print("cust state is:",state_list[i])


        
             
#Delete Customer
    if choice=="3":
       id = int(input("Enter the cust id : "))
       i = id_list.index(id)
       id_list.pop(i)
       name_list.pop(i)
       age_list.pop(i)
       addar_list.pop(i)
       phone_list.pop(i)
       email_list.pop(i)
       pan_number_list.pop(i)
       pin_code_list.pop(i)
       city_list.pop(i)
       state_list.pop(i)

       print("cust id is:",id_list)
       print("cust name:",name_list)
       print("cust age is:",age_list)
       print("cust addar is",addar_list)
       print("cust phone number is:",phone_list)
       print("cust email id is :",email_list)
       print("cust pan number is :",pan_number_list)
       print("cust pin code is:",pin_code_list)
       print("cust city is:",city_list)
       print("cust state is :",state_list)


#Modify Customer
    if choice=="4":
        id=int(input("enter the cust id:"))
        # i=id_list.index(id)
        update_name=input("enter the new cust name:")
        update_age=int(input("enter the new cust age:"))
        update_addar=int(input("enter the new cust addar:"))
        update_phone=input("enter the new cust phone number:")
        update_email=input("enter the new cust email id:")
        update_pan=input("enter the cust new pan number:")
        update_pin=input("enter the cust new pin code:")
        update_city=input("enter the new city of the  customer: ")
        update_state=input("enetr the new state of the customer:")

        i=id_list.index(id)
        name_list[i]=update_name
        age_list[i]=update_age
        addar_list[i]=update_addar
        phone_list[i]=update_phone
        email_list[i]=update_email
        pan_number_list[i]=update_pan
        pin_code_list[i]=update_pin
        city_list[i]=update_city
        state_list[i]=update_state

        print("cust id is:",id_list)
        print("cust name is:",name_list)
        print("cust age is:",age_list)
        print("cust addar number is:",addar_list)
        print("cust phone number is",phone_list)
        print("cust email id is:",email_list)
        print("cust pan number is:",pan_number_list)
        print("cust pin code is:",pin_code_list)
        print("the city of the cust is:",city_list)
        print("the state of the cust is:",state_list)



#Display All Customers
    if choice=="5":
        d = "display"
        display= input("Enter [display] all customer :")
        if display==d:
            print("customer id is:  ",id_list)
            print("customer name is :  ",name_list)
            print("customer age is: ",age_list)
            print("customer addar number is:",addar_list)
            print("cusutomer phone number is  ",phone_list)
            print("customer email id is",email_list)
            print("customer pan number is :",pan_number_list)
            print("cutomer pin code is:",pin_code_list)
            print("the cust cityn is:",city_list)
            print("the cust state is is:",state_list)


# Exit CRM
    if choice=="6":
        break
    




        


