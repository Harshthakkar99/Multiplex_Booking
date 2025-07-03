# Ticket Booking System

A Python-based console application for managing ticket bookings with seat selection, cancellation, and booking display features. This system simulates a theater or cinema seat booking experience with a user-friendly command-line interface.

## Features

- **Interactive Menu System**: Easy-to-use console interface with numbered options
- **Seat Booking**: Book multiple seats with user name registration
- **Ticket Cancellation**: Cancel specific seats by user name
- **Visual Seat Display**: Shows available and booked seats in a grid format
- **Real-time Updates**: Dynamic seat availability tracking
- **Input Validation**: Handles various input formats and edge cases
- **User Management**: Track bookings by individual users

## Prerequisites

This project requires only Python's built-in libraries:
- No external dependencies needed
- Compatible with Python 3.x

## Installation

1. Clone or download the project file
2. Ensure Python 3.x is installed on your system
3. Run the script:
   ```bash
   python ticket_booking.py
   ```

## Usage

1. **Start the Application**: Run the Python script
2. **Choose Options**: Select from the main menu (1-4)
3. **Book Tickets**: Enter your name and select seat numbers
4. **Cancel Tickets**: Provide your name and specify seats to cancel
5. **View Bookings**: See current seat availability and booked seats
6. **Exit**: Choose option 4 to quit the application

## Code Implementation

### 1. Initial Setup and Data Structures

```python
total_seat = 100
available_seat = [f"{i:02}" for i in range(1, total_seat + 1)]
booked_seat = []
```

This section initializes the system with 100 seats numbered from 01 to 100. The `available_seat` list stores seat numbers with zero-padding (01, 02, 03...), while `booked_seat` stores tuples of (user_name, seat_number) for tracking bookings.

### 2. Main Menu Loop

```python
while True:
    print("\n=== Ticket Booking System ===")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Display Booking")
    print("4. Exit")
    menu = int(input("Choose an option: "))
```

Creates an infinite loop displaying the main menu options. Users can choose between booking, canceling, viewing bookings, or exiting the system.

### 3. Ticket Booking Logic

```python
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
```

Handles the booking process by checking seat availability, accepting user input for seat selection, and updating the data structures. It automatically formats single-digit seat numbers with zero-padding and marks booked seats with a "✘" symbol.

### 4. Ticket Cancellation System

```python
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
```

Manages ticket cancellation by first identifying the user's booked seats, then allowing them to cancel specific seats. It validates that users can only cancel seats they actually booked and updates the availability accordingly.

### 5. Booking Display System

```python
elif menu == 3:
    print(f"\nTotal available tickets are: {total_seat}")
    for i in range(len(available_seat)):
        if (i + 1) % 10 == 0:
            print(available_seat[i])
        else:
            print(available_seat[i], end=" ")
    print("\n\nBooked seats:", sorted([seat for _, seat in booked_seat]))
```

Displays the current booking status in a visual grid format (10 seats per row) and shows all booked seats in sorted order. Available seats show their numbers, while booked seats display "✘" symbols.

### 6. Exit and Error Handling

```python
elif menu == 4:
    print("Exiting...")
    break
else:
    print("❌ Invalid option. Please try again.")
```

Provides a clean exit option and handles invalid menu selections with user-friendly error messages.

## Key Features Explained

### Seat Numbering System
- **Zero-Padding**: Seats are numbered 01-100 for consistent display
- **Format Handling**: Accepts both single-digit (5) and double-digit (05) input
- **Visual Representation**: Uses "✘" symbols for booked seats

### User Management
- **Name-Based Tracking**: Each booking is associated with a user name
- **Individual Cancellation**: Users can only cancel their own bookings
- **Booking History**: System tracks who booked which seats

### Data Integrity
- **Real-time Updates**: Seat availability updates immediately
- **Validation**: Prevents double-booking and invalid cancellations
- **Consistency**: Maintains accurate counts of available seats

## System Limitations

- **No Data Persistence**: Bookings are lost when the program closes
- **Single Session**: No multi-user concurrent access
- **Memory-Based**: All data stored in program variables
- **No Authentication**: Users identified by name only

## Error Handling

The system includes several error handling mechanisms:
- **Seat Availability Check**: Prevents booking unavailable seats
- **User Validation**: Ensures users can only cancel their own bookings
- **Input Validation**: Handles various seat number formats
- **Boundary Checks**: Prevents canceling more tickets than owned

## Future Enhancements

- **File Storage**: Save bookings to a file for persistence
- **Database Integration**: Store data in a database for better management
- **GUI Interface**: Create a graphical user interface
- **Payment Integration**: Add payment processing functionality
- **Seat Categories**: Implement different seat types and pricing
- **Time Slots**: Add show times and date selection
- **User Authentication**: Implement secure user login system

## Example Usage

```
=== Ticket Booking System ===
1. Book Ticket
2. Cancel Ticket
3. Display Booking
4. Exit
Choose an option: 1

How many seats do you want to book: 2
Enter your name here: John
Enter which seat you want: 5
Seat 05 booked successfully for John
Enter which seat you want: 10
Seat 10 booked successfully for John
```

## Contributing

Feel free to fork this project and submit pull requests for improvements. Some areas for contribution:
- Adding new features
- Improving error handling
- Enhancing the user interface
- Adding data persistence
- Writing unit tests

## License

This project is open source and available for educational and personal use.

## Disclaimer

This is a demonstration project for learning purposes. For production use, consider implementing proper data persistence, security measures, and error handling.
