

def show():
  s = [[str(e) for e in row] for row in h]
  lens = [max(map(len, col)) for col in zip(*s)]
  fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
  table = [fmt.format(*row) for row in s]
  print('\n'.join(table))
  
def checkInven():
  for i in range(1,len(h)):
    if(h[i][2]<=5):
      print("\nStock replinished")
      h[i][2]=20

h=[['Name','Price','Quantity', 'Manufacturer'],['earphone',500,20,'Boat'],['Headphones',1000,15,'Sony'],['Monitor',2500,10,'Logitech'],['MS Office 2021',1000,25,'Microsoft']]
n='a'
cost=0
while(n!='e'):
  checkInven()
  print("\nStock is\n")
  show()
  n=input("\np : Buy\nc : Stock\ne : exit\n")
  if(n=='p'):
    a=int(input("Select an Option (1=earphone, 2=headphone..) "))
    if(a>4):
      print("Oh no! Seems like you chose wrong option. Try again.")
      continue
    count=int(input("How many units do you want us to serve you with? "))
    if(h[a][2]<count):
      print("Sorry.. we're running out of stocks!!")
    else:
      h[a][2]-=count
      print("Thankyou for Shopping")
      cost+=h[a][1]*count
  elif(n=='c'):
    b=int(input("Select an option (1=earphone, 2=headphone..) "))
    if(b>4):
      print("Incorrect option. Try again.")
      continue
    print("Stock Left is ",h[b][2])
  elif(n=='e'):
    pass
  else:
    print("Oh no! Seems like you chose wrong option. Try again.")
print("\nYour total bill is ",cost,"\nThank you,Visit us Again.")

deli=['Zomato','Swiggy','Behrouz Biryani']
foo=['Pizza','crispy Chicken','Hyderabadi Dum Biryani']
pri=[120,100,200]
repeat='y'
while(repeat!='n'):
  user=int(input("1. Zomato\n2. Swiggy\n3. Behrouz Biryani\nEnter your preferred delivery partner "))
  choice=int(input("\n1. Pizza : 120/-\n2. crispy Chicken : 100/-\n3. Hyderabadi Dum Biryani : 200/-\nEnter your choice "))
  loc=input("\nEnter your address ")
  print("\nYour order for",foo[choice-1],"has been placed on",deli[user-1],"and will get delivered",loc,"\nYour Bill for the order is ",pri[choice-1])
  repeat=input("Do you wish to order again? (y/n)\n")



utilities=input("Enter all bills to be shared separated with a comma\n")
l1=utilities.split(",")
l2=[]
sum=0
n=int(input("Enter no. of tenants "))
n+=1
for i in range(len(l1)):
  print("Enter total amount for",l1[i],"bill ")
  l2.append(float(input()))
for i in range(len(l1)):
  sum+=round(l2[i]/n,2)
  print("The",l1[i],"bill is split as",round(l2[i]/n,2),"per head")
print("\nThe total per head is",sum)

ch=str(input("\"Do you want to recharge?\n Y-Yes and any key-No"))
if ch=='Y' or ch=='y':
  opt=int(input("Press 1 for prepaid and any key for postpaid"))
  if opt==1:
    no=int(input("Enter mobile no"))
    operator=int(input("Choose your operator\n1. Jio \n2. Airtel\n3.Vi"))
    amt=int(input("Choose a recharge amt\n399 : 1.5 GB data/day for 84 days\n 299 : 1 GB data/day for 56 days\n 199 : 1 GB data/day for 30 days"))
    confirm=int(input("Press 1 to confirm and any key to cancel"))
    if confirm==1:
      print("Your recharge for no {} for amt {} has been succesfull!".format(no,amt))