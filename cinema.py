confirm = "N"
while confirm == "N":
    #Welcome message
    print("Welcome to the Cinema")

    #asking user for info 
    user_name = input("What is your name? ")
    user_phone= int(input("What is the valid phone number?"))

    #validating phone number 
    if user_phone == 1:
        print("correct")
    if user_phone != 1:
        while user_phone !=1 :
            print(" I am sorry. Your phone number not working, please enter different number")
            user_phone= int(input("What is valid phone number"))
            if user_phone == 1:
                break

    #movie selection
    print("1 = Iron man")
    print("2 = Spider-man")
    print("3 = Batman")

    def movies (movie):
        movie = movie.lower()
        match movie:
            case '1':
                return "Iron man"
            case '2':
                return "Spider-Man"
            case '3':
                return "Batman"
    
    movie = input("Which Movie? ")
    print (movies(movie))

    while  (movies(movie)) == 'Unidentified movie':
        if movies (movie) != 'Unidentified movie':
            print("info correct")
            break
        else:
                print(" ")
                print("error, input not accept.")
                print("1 = Iron man")
                print("2 = Spider-man")
                print("3 = Batman")
                movie = input("Which movie? ")
                print (movies(movie))
            
        #picking time
    print( "1 = Morning")
    print("2 = Afternoon")
    print("3 = Evening")
    def times (time):
        times = time.lower()
        match time:
            case '1' :
                return 'Morning'
            case '2' :
                return 'Afternoon'
            case '3' :
                return 'Evening'
            case _ :
                return 'Invalid Time'
      

    time = input("What time do you want? ")
    print (times(time))


    while (times(time)) == 'Invalid time':
        if (times(time)) != 'Invalid time':
            print("info correct")
            break
        else:
                print(" ")
                print("error, input not accept.")
                print("1 = Morning")
                print("2 = Afternoon")
                print("3 = Evening")
                movie = input("What time? ")
                print (times(time))

    #booking seat 

    available_seats = ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)', '(10)']
    print (available_seats)
    def seats (seat):
        seat = seat.lower()
        match seat :
            case '1':
                return 0
            case '2': 
                return 1
            case '3' :
                return 2
            case '4' :
                return 3
            case '5' :
                return 4
            case '6':
                return 5
            case '7':
                return 6
            case '8': 
                return 7
            case '9' :
                return 8
            case '10' :
                return 9
            case _:
                return 'Invalid seat'

    #seat validation
    seat = input('Which seat? ')
    if (seats(seat)) == 'Invalid seat':
        while (seats(seat)) == 'Invalid seat':
            seat = input("which seat?")
            if (seats(seat)) != 'Invalid seat':
                available_seats[seats(seat)] = "(X)"
                break
            else:
                print(" ")
                print("error, input not accept.")
                print(" ")
                print(available_seats)
                seat = input('Which seat? ')
                print(" ")

    available_seats[seats (seat)] = "(X)"
    print(available_seats)

    #confirming book
    print('confirm order: movies: ', (movies(movie)), ", time:" , (times(time)), ", seats:" , (available_seats), )
    confirm = input("comfirm ? Y/N")
    if confirm == "Y" :
        print ("Your seat has been confirmed")
        confirm == "Y"
    elif confirm == "N":
        print('')

    else:
        print("incorrect input")
        confirm = input("confirm? Y/N")
