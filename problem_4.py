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
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == group.get_name():
        return True
    if user in group.get_users():
        return True
    for group_ in group.get_groups():
        return is_user_in_group(user, group_)
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


print(is_user_in_group("child", child))  # True
print(is_user_in_group("", child))  # False
print(is_user_in_group("sub_child_user", parent))  # True


parent = Group("parent")
child_1 = Group("child_1")
child_2 = Group("child_2")
child_3 = Group("child_3")

child_1.add_user("grand_child")

parent.add_group(child_1)
parent.add_group(child_2)
parent.add_group(child_3)

print(is_user_in_group("grand_child", child_1))  # True
print(is_user_in_group("grand_child", child_2))  # False
print(is_user_in_group("grand_child", child_3))  # False
print(is_user_in_group("grand_child", parent))  # True
