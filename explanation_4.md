Used recursion.

First:  user == group_name
Second: user in group
Third: check in childrens of the group recursively.
If never found, then return False

Time complexity: O(depth * No. of users)
Space complexity: O(depth * No. of users)