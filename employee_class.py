class Employee(object):
    """A sample of Employee class"""
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __reper__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)


