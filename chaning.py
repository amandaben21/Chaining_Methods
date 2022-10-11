#Same code from User.py, but this time we are chaning it
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"First: {self.first_name}")
        print(f"Last: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age} years old!")
        print(f"Is a member: {self.is_rewards_member}")
        print(f"Current Points:{self.gold_card_points}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        return self #we return self in each method


    def enroll(self):
        if self.is_rewards_member:
            print("Already a memeber!")
            return False

        #set to true
        self.is_rewards_member = True

        #set to 200
        self.gold_card_points = 200

        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:      #we put an if statement 1st b/c we dont want the points to show negative
            print(f"You dont't have enough points to spend {amount}, below you will see your current points")
            return #stop running

        self.gold_card_points = self.gold_card_points - amount

        return self



amanda = User("Amanda", "Contreras", "xyz@gmail.com", 100)
toby = User("Toby", "Benitez", "abc@gmail.com", 50)
hunter = User("Hunter", "Love", "efg@gmail.com", 20)

########################################################
"""""
So instead of this:

amanda.display_info() 
amanda.enroll() 
amanda.display_info()
amanda.spend_points(50) 
amanda.display_info() 
"""""
#we do this:
amanda.display_info().enroll().display_info().spend_points(50).display_info()

#############################################################
