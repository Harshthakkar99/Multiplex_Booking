total_seat = 100
available_seat = [f"{i:02}" for i in range(1, total_seat + 1)]
booked_seat = []

while True:
    print("\n=== Ticket Booking System ===")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Display Booking")
    print("4. Exit")
    menu = int(input("Choose an option: "))

    if menu == 1:
        if any(seat.isdigit() for seat in available_seat):
            n = int(input("How many seats do you want to book: "))
            user_name = input("Enter your name here: ")
            for i in range(n):
                seat_number = input("Enter which seat you want: ")
                if len(seat_number) == 1:
                    seat_number = f"0{seat_number}"
                
                if seat_number in available_seat:
                    booked_seat.append((user_name, seat_number))
                    index = available_seat.index(seat_number)
                    available_seat[index] = " ✘"
                    total_seat -= 1
                    print(f"Seat {seat_number} booked successfully for {user_name}")
                else:
                    print("Ticket is not available")
        else:
            print("All seats are booked")

    elif menu == 2:
        if booked_seat:
            user_name = input("Enter the name with booked ticket: ")
            user_booked_seats = [seat for name, seat in booked_seat if name == user_name]
            
            if user_booked_seats:
                print(f"You have booked the following seats: {user_booked_seats}")
                cancel_count = int(input("How many tickets do you want to cancel? "))

                if cancel_count > len(user_booked_seats):
                    print("You don't have this much ticket")
                else:
                    for _ in range(cancel_count):
                        seat_number = input("Enter the seat number you want to cancel: ")

                        if len(seat_number) == 1:
                            seat_number = f"0{seat_number}"

                        if seat_number in user_booked_seats:
                            index = available_seat.index(" ✘")
                            available_seat[index] = seat_number
                            booked_seat.remove((user_name, seat_number))
                            user_booked_seats.remove(seat_number)
                            total_seat += 1
                            print(f"✅ Seat {seat_number} canceled successfully for {user_name}.")
                        else:
                            print(f"❌ You did not book seat {seat_number}.")
            else:
                print("❌ You did not book any tickets yet.")
        else:
            print("❌ No tickets are available.")

    elif menu == 3:
        print(f"\nTotal available tickets are: {total_seat}")
        for i in range(len(available_seat)):
            if (i + 1) % 10 == 0:
                print(available_seat[i])
            else:
                print(available_seat[i], end=" ")
        print("\n\nBooked seats:", sorted([seat for _, seat in booked_seat]))

    elif menu == 4:
        print("Exiting...")
        break
    else:
        print("❌ Invalid option. Please try again.")
