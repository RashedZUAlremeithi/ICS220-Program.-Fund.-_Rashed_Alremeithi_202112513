from enum import Enum

# Enum for preferred language of customer
class PreferredLanguage(Enum):
    ARABIC = "Arabic"
    ENGLISH = "English"

# Enum for nationality of customer
class Nationality(Enum):
    EMIRATI = "Emirati"
    FOREIGNER = "Foreigner"

# Enum for room type in reservation
class RoomType(Enum):
    STANDARD = "Standard"
    DELUXE = "Deluxe"
    SUITE = "Suite"

# Enum for bed type in reservation
class BedType(Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    QUEEN = "Queen"
    KING = "King"


# Creating Customer class with attributes
class Customer:
    def __init__(self, name, gender, email, username, password, phone_number, preferred_language, nationality):
        self.__name = name  # Customer name
        self.__gender = gender  # Customer gender
        self.__email = email  # Customer email
        self.__username = username  # Customer account username (for online reservation)
        self.__password = password  # Customer account password (for online reservation)
        self.__phone_number = phone_number  # Customer phone number
        self.__preferred_language = preferred_language  # Customer preferred language
        self.__nationality = nationality  # Customer nationality (Emirati or Foreiner)

    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and Setter for gender
    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    # Getter and Setter for email
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    # Getter and Setter for username
    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    # Getter and Setter for password
    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    # Getter and Setter for phone number
    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # Getter and Setter for preferred language
    def get_preferred_language(self):
        return self.__preferred_language

    def set_preferred_language(self, preferred_language):
        self.__preferred_language = preferred_language

    # Getter and Setter for nationality
    def get_nationality(self):
        return self.__nationality

    def set_nationality(self, nationality):
        self.__nationality = nationality

    # Display function for Customer
    def displayCustomer(self):
        print(f"Customer Name: {self.__name}")
        print(f"Gender: {self.__gender}")
        print(f"Email: {self.__email}")
        print(f"Username: {self.__username}")
        print(f"Phone Number: {self.__phone_number}")
        print(f"Preferred Language: {self.__preferred_language.value}")
        print(f"Nationality: {self.__nationality.value}")

    # Function that prints and sends email to customer when they confirm their reservation
    def send_confirmation(self):
        print(f"Reservation confirmation sent to {self.__email}")


# Creating Reservation class with updated attributes
class Reservation:
    def __init__(self, reservation_number, checkin_date, checkout_date, room_number, room_type, bed_type):
        self.__reservation_number = reservation_number #Reservation number for the reservation that has been created
        self.__checkin_date = checkin_date #Date that Customer has checked-in to the hotel
        self.__checkout_date = checkout_date #Date that Customer has checked-out to the hotel
        self.__room_number = room_number #Number of the room reserved
        self.__room_type = room_type #Type of room reserved (Standard, Deluxe, or suite)
        self.__bed_type = bed_type #Type of bed in the room reserved (single, double, queen, or king)

    # Getter and Setter for reservation number
    def get_reservation_number(self):
        return self.__reservation_number

    def set_reservation_number(self, reservation_number):
        self.__reservation_number = reservation_number

    # Getter and Setter for check-in date
    def get_checkin_date(self):
        return self.__checkin_date

    def set_checkin_date(self, checkin_date):
        self.__checkin_date = checkin_date

    # Getter and Setter for check-out date
    def get_checkout_date(self):
        return self.__checkout_date

    def set_checkout_date(self, checkout_date):
        self.__checkout_date = checkout_date

    # Getter and Setter for room number
    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    # Getter and Setter for room type
    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, room_type):
        self.__room_type = room_type

    # Getter and Setter for bed type
    def get_bed_type(self):
        return self.__bed_type

    def set_bed_type(self, bed_type):
        self.__bed_type = bed_type

    # Display function for Reservation
    def displayReservation(self):
        print(f"Reservation Number: {self.__reservation_number}")
        print(f"Check-in Date: {self.__checkin_date}")
        print(f"Check-out Date: {self.__checkout_date}")
        print(f"Room Number: {self.__room_number}")
        print(f"Room Type: {self.__room_type.value}")
        print(f"Bed Type: {self.__bed_type.value}")

    # Function that checks room availability.
    #It will need to check the room_number for the room.
    #It will also check for checkin_date and Checkout_date to make sure that no one is using the room at that time.
    #It should return true(room is available) or False(room is not available.)
    def is_room_available(self, room_number, checkin_date, checkout_date):
        # Check room availability code here
        pass


# Creating Receipt class with updated attributes
class Receipt:
    def __init__(self, billing_name, credit_card, room_cost, nights, room_subtotal, taxes, extra_cost, total_charges,
                 paid_amount, payment_done):
        self.__billing_name = billing_name #Name of payer
        self.__credit_card = credit_card #Type of credit card used For example: (Mastercard ending in 1234)
        self.__room_cost = room_cost #Cose of the room per night
        self.__nights = nights #number of nights reserved
        self.__room_subtotal = room_subtotal#Room_cost multiplied by number of nights
        self.__taxes = taxes#Extra tax for payment. Since this is in the UAE it will always be 5%
        self.__extra_cost = extra_cost#Cost of any missing or broken items when customer is checking-out
        self.__total_charges = total_charges#total cost of everything together
        self.__paid_amount = paid_amount#amount already paid by customer
        self.__payment_done = payment_done#a boolean value for if the customer has already paid or not

    # Getter and Setter for billing name
    def get_billing_name(self):
        return self.__billing_name

    def set_billing_name(self, billing_name):
        self.__billing_name = billing_name

    # Getter and Setter for credit card
    def get_credit_card(self):
        return self.__credit_card

    def set_credit_card(self, credit_card):
        self.__credit_card = credit_card

    # Getter and Setter for room cost
    def get_room_cost(self):
        return self.__room_cost

    def set_room_cost(self, room_cost):
        self.__room_cost = room_cost

    # Getter and Setter for nights
    def get_nights(self):
        return self.__nights

    def set_nights(self, nights):
        self.__nights = nights

    # Getter and Setter for room subtotal
    def get_room_subtotal(self):
        return self.__room_subtotal

    def set_room_subtotal(self, room_subtotal):
        self.__room_subtotal = room_subtotal

    # Getter and Setter for taxes
    def get_taxes(self):
        return self.__taxes

    def set_taxes(self, taxes):
        self.__taxes = taxes

    # Getter and Setter for extra cost
    def get_extra_cost(self):
        return self.__extra_cost

    def set_extra_cost(self, extra_cost):
        self.__extra_cost = extra_cost

    # Getter and Setter for total charges
    def get_total_charges(self):
        return self.__total_charges

    def set_total_charges(self, total_charges):
        self.__total_charges = total_charges

    # Getter and Setter for paid amount
    def get_paid_amount(self):
        return self.__paid_amount

    def set_paid_amount(self, paid_amount):
        self.__paid_amount = paid_amount

    # Getter and Setter for payment done
    def get_payment_done(self):
        return self.__payment_done

    def set_payment_done(self, payment_done):
        self.__payment_done = payment_done

    # Display function for Receipt
    # Updated display function for Receipt
    def displayReceipt(self):
        print(f"Billing Name: {self.__billing_name}")
        print(f"Credit Card: {self.__credit_card}")
        print(f"Room Cost per Night: {self.__room_cost}")
        print(f"Number of Nights: {self.__nights}")
        print(f"Room Subtotal: {self.__room_subtotal}")
        print(f"Taxes: {self.__taxes * 100}%")
        print(f"Extra Costs: {self.__extra_cost}")
        print(f"Total Charges: {self.__total_charges}")
        print(f"Paid Amount: {self.__paid_amount}")
        print(f"Payment Completed: {self.__payment_done}")

    # Function that calculates the roomsubtotal
    def calculate_room_subtotal(self):
        self.__room_subtotal = self.__room_cost * self.__nights

    # Function that calculates total charges
    def calculate_total_charges(self):
        self.__total_charges = self.__room_subtotal + self.__extra_cost + self.__taxes

    # Function that updates payment status if payment is done or not
    def update_payment_status(self):
        if self.__paid_amount == self.__total_charges:
            self.__payment_done = True
        else:
            self.__payment_done = False

    # Function that adds extra payment for nay damaged or missing items
    def add_extra_payment(self, extra_payment):
        self.__total_charges += extra_payment
        print(f"Added extra payment of {extra_payment}. New total charges are {self.__total_charges}")
        self.update_payment_status()

# Testing the Customer class
customer1 = Customer(name="Jane Smith", gender="Female", email="janesmith@gmail.com", username="janesmith123", password="password456",
                     phone_number="0501234568", preferred_language=PreferredLanguage.ENGLISH, nationality=Nationality.FOREIGNER)
customer2 = Customer(name="Rashed Al Remeithi", gender="Male", email="rashed@gmail.com", username="rashed123", password="securepassword123",
                     phone_number="0551234567", preferred_language=PreferredLanguage.ARABIC, nationality=Nationality.EMIRATI)

# Call functions on Customer objects
customer1.send_confirmation()
customer1.displayCustomer()

customer2.send_confirmation()
customer2.displayCustomer()

# Testing the Reservation class
reservation1 = Reservation(reservation_number=101, checkin_date="2024-10-01", checkout_date="2024-10-05",
                           room_number=305, room_type=RoomType.STANDARD, bed_type=BedType.QUEEN)
reservation2 = Reservation(reservation_number=102, checkin_date="2024-11-15", checkout_date="2024-11-20",
                           room_number=101, room_type=RoomType.DELUXE, bed_type=BedType.KING)

# Call functions on Reservation objects
reservation1.displayReservation()

reservation2.displayReservation()

# Testing the Receipt class
receipt1 = Receipt(billing_name="Jane Smith", credit_card="Mastercard ending in 1234", room_cost=300, nights=4,
                   room_subtotal=0, taxes=0.05, extra_cost=50, total_charges=0, paid_amount=1200, payment_done=False)
receipt2 = Receipt(billing_name="Rashed Al Remeithi", credit_card="Visa ending in 5678", room_cost=400, nights=5,
                   room_subtotal=0, taxes=0.05, extra_cost=100, total_charges=0, paid_amount=2100, payment_done=False)

# Call functions on Receipt objects
receipt1.calculate_room_subtotal()
receipt1.calculate_total_charges()
receipt1.update_payment_status()
receipt1.displayReceipt()


receipt1.add_extra_payment(250)


receipt2.calculate_room_subtotal()
receipt2.calculate_total_charges()
receipt2.update_payment_status()
receipt2.displayReceipt()
