#the program gets inputs from the user and displays a list of holiday destinations to choose from

print('1: Edinburgh \t 2:London \t 3: Amsterdam \t 4: Munich \t 5: Sydney')
city_flight = int(input('enter the destination you want to go to: 1, 2, 3, 4, or 5 ')) #convert the user inputs to an integer so that we don't have to convert them later
rental_days = int(input('How many days do you plan on hiring a car? '))
num_nights = int(input('How many nights will you plan on staying at a hotel? '))

#three functions are created to calculate the hotel cost, the plane cost and the car rental cost.
def hotel_cost(num_nights):
    cost = 50 * num_nights
    return cost


def plane_cost(city_flight):
    destination_costs = {1: 200, 2: 250, 3: 180, 4: 220} # a dictionary is created containing the options for the holiday destination and the cost for each destination
    flight = destination_costs.get(city_flight,0)# the cost for the destination is obtained using city_flight as a key to access the flight cost. in the case that the usesr input gives a number outside of this range (e.g, 6) then 0 is returned as the cost
    return flight
    
def car_rental(rental_days):
    cost = 35 * rental_days
    return cost
    
def holiday_cost():
    hotel= hotel_cost(num_nights) # call all three functions to totalcost
    plane = plane_cost(city_flight)
    car = car_rental(rental_days)
    total = hotel + plane + car 
    print(f'The total cost for this holiday is £{total:.2f}') #calculate and display the total cost
    
holiday_cost()