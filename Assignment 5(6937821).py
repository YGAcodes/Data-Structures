"""
Computer Assignment 5
Index Number:6937821

"""
# list of available cars and their prices 
cars = {'Toyota Corolla': 30000,'Accord': 30562,
 'RollsRoycePhantom': 456000, 'Lamboghini Urus': 250000,
 'RollsRoyceCullinan': 460000,'Lamboghini Aventador SVJ': 350000,
 'Corolla Cross': 35000, 'Santa Fe': 25050,'Sonata Hybrid': 50000,
 'Nissan Sentra': 5000,'Toyota Yaris': 3000,
 'Toyota Land Cruiser': 50000,'Mercedes-Benz Gclass': 43550,
 'Kia Sorento': 2500,'Bentley Bentayga SUV': 187600,
 'Bentley Flying Spur Sedan': 198100, 'Audi A4': 40000,
 'BMW X7': 74000,'Chevrolet Camaro': 25000,'Mercedes-Benz c300': 40000,
 'Dodge Charger': 31000,'Ford F-150': 28000,
 'Honda Civic': 22000, 'Jeep Wrangler': 28500,
 'Lexus RX': 45000,'Mazda CX-5': 26000,'Picanto': 1000,
 'Porsche 911': 100000,'Tesla Model S': 80000, 'Volkswagen Golf': 23500}
# get user input for car name
print('WELCOME TO A&A GARAGE')
car_brand = input('Enter the name of the car you would like to purchase :')
# Check if the car brand is in the dictionary
if car_brand in cars:
    print("Yes, the car is available.")
    print(f"The price of {car_brand} is ${cars[car_brand]:,}.")
else:
    print("Sorry, the car is not available.")