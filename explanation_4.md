Used recursion for this problem. By using recursion, we can easily traverse the nested groups.

First:  user == group_name
Second: user in group
Third: check in childrens of the group recursively.
If never found, then return False

### Call stack

is_user_in_group("child", parent)
	is_user_in_group("child", child)
		returned True
	return True


Time complexity: O(depth * No. of users)
Space complexity: O(depth * No. of users)