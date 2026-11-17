class Movie:

    def __init__(self, movie_name, total_seats, ticket_price):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def show_status(self):
        seats_available = self.total_seats - self.booked_seats

        print("Movie Name:", self.movie_name)
        print("Seats Available:", seats_available)
        print("Booked Seats:", self.booked_seats)

    def book_tickets(self, number_of_tickets):

        seats_available = self.total_seats - self.booked_seats

        if number_of_tickets > seats_available:
            print("Sorry! Not enough seats available.")

        else:
            self.booked_seats += number_of_tickets

            print("Your ticket is booked.")
            print("Total Price:",
                  self.ticket_price * number_of_tickets)


movie = Movie("Krrish", 100, 499)

movie.show_status()

movie.book_tickets(70)

movie.show_status()

movie.book_tickets(70)