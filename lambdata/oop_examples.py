"""This is an example class"""


class BareMinimumClass:
    pass


class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for Complex numbers.
        Complex numbers are part real and part imaginary.
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        """
        Takes another complex number and adds it
        to itself.
        """
        # other_complex = num2
        # self = num1
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return "({}, i{})".format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100


if __name__ == "__main__":
    num1 = Complex(3, -5)  # num1.r == 3, num1.i == -5
    num2 = Complex(2, 6)  # num2.r == 2, num2.i == 6
    num1.add(num2)
    print(num1.r, num1.i)

user = SocialMediaUser(name="Carl", location="United States")
user2 = SocialMediaUser(name="Carlton", location="Costa Rica")
user3 = SocialMediaUser(name="Carlos", location="Argentina", upvotes=12345)
user4 = SocialMediaUser(name="George Washington", location="Djibouti"),
