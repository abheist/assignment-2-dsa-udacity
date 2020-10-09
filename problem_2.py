import os


def find_files(suffix, path, files=[]):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    temporary = suffix

    if path:
        temporary = suffix + '/' + path

    list_dir = os.listdir(temporary)

    for file in list_dir:
        temporary1 = temporary + '/' + file

        if os.path.isfile(temporary1) and temporary1.endswith(".c"):
            files.append(temporary1)
        elif os.path.isdir(temporary1):
            files = find_files(temporary, file, files)

    return files


print(find_files('.', 'testdir'))
print(find_files('.', ''))
print(find_files('.', 'testdir/subdir1'))
print(find_files('.', 'testdir', ['t1.c']))
