class User:
    name = None
    user_id = None

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_list = []


class Student(User):
    name = None
    user_id = None
    roll_no = None
    max_borrow_limit = None

    def __init__(self, name, user_id, roll_no):
        super().__init__(name, user_id)
        self.roll_no = roll_no
        self.max_borrow_limit = 3


class Staff(User):
    name = None
    user_id = None
    employee_id = None

    def __init__(self, name, user_id, employee_id):
        super().__init__(name, user_id)
        self.employee_id = employee_id
        self.max_borrow_limit = 5

