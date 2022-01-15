# The try statement in Python can have an optional finally clause.
# This clause is executed no matter what,
# and is generally used to release external resources.

# For example, we may be connected to a remote data center through the network or working with a file or a Graphical User Interface(GUI).

# In all these circumstances, we must clean up the resource before the program comes to a halt whether it successfully ran or not.
# These actions(closing a file, GUI or disconnecting from network) are performed in the finally clause to guarantee the execution.


try:
    f = open("test.txt", encoding='utf-8')
    # perform file operations
finally:
    f.close()
