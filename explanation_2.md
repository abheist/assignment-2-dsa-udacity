Travesing the nested path is easy with recursion. Wrote a recursive function which recursively Travesing the nested directories. And if the current selected element is directory then going deep with recursion or else checking for `.c` file extension.
If found, then appending to the list as when finding the `.c` file.

Time complexity: O(depth * Number of directories in each level)
Space complexity: O(depth)