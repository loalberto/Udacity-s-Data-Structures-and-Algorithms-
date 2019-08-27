class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if user in group.users:  # Base Case: if in this group then return True
        return True
    for group in group.groups:  # Check if it's inside a subgroup
        val = is_user_in_group(user, group)  # Recursively check if the user is in any of the groups
        if val is True:
            return True  # If the user is then return True

    return False  # If never found then return False


def test_case(user, group):
    is_user_in_group(user, group)


# Test Case 1:
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

"""This will initiate three groups and then check if the lowest child group 
    exists in the the parent group. It should return True."""
print(is_user_in_group("sub_child_user", parent))

# Test Case 2:
deserts = Group("deserts")
cookie = Group("cookie")
cake = Group("cake")

chocolate_user = "chocolate_user"
cake.add_user(chocolate_user)

cookie.add_group(cake)
deserts.add_group(cookie)
"""This should print out false because a carrot is not part of the desert group 
    or cookie group or cake group. It should return False."""
print(is_user_in_group("cucumber", deserts))

# Test Case 3:
high_school = Group("")
middle_school = Group("")

principle_user = "principle_user"
high_school.add_user(principle_user)

high_school.add_group(middle_school)

"""I will be checking the middle school's empty groups. It should return False."""
print(is_user_in_group("student", middle_school))
