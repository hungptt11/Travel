# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def getTicketPrice(i):
    switcher={
            1:100,
            2:102,
            3:105,
         }
    return switcher.get(i,100)
totalPrices = 0
print("Please book a ticket, enter a number: ")
print("1, Korean Air - 100USD\r\n" +
      "2, Jesu Air - 102USD\r\n" +
      "3, Asian Air - 105USD\r\n")
ticket = input()
totalPrices += getTicketPrice(int(ticket))
print("Where do you live?, enter a number: ");
print("1, Hotel\r\n" +
      "2, Other\r\n");
location = input()
if int(location) == 2:
    print("Enter the home stay prices : ")
    price = input()
    totalPrices += int(price)
else:
    print("Enter a number for the hotel : ")
    print("1, Hotel A - 100USD/Night/2bedroom - Inclued(Wifi, Pool, laundry)\r\n" +
          "2, Hotel B - 105USD/Night/1bedroom - Inclued(Wifi, Pool, laundry, breakfast, taxi)\r\n")
    hotel = input()
    if int(hotel) == 2:
        totalPrices += 105
    else:
        totalPrices += 100
        
print("Restaurant?, enter a number: ")
print("1, Restaurant A - 20USD\r\n" +
     "2, Restaurant B - 30USD\r\n")
restaurant = input()
if int(restaurant) == 2 :
     totalPrices += 30
else:
    totalPrices += 20
print("Visit Location?, enter a number: ")
print("1, Park A - 20USD\r\n" +
      "2, Beach B - 30USD\r\n")
visit = input()
if restaurant == 2:
    totalPrices += 30
else:
    totalPrices += 20

print("Transport?, enter a number: ")
print("1, Bus A - 20USD\r\n" +
      "2, Taxi B - 30USD\r\n")
transport = input()
if restaurant == 2:
    totalPrices += 30
else:
    totalPrices += 20
print("Total Prices : " + str(totalPrices) + "USD")