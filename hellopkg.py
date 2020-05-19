# An example of a Python Package
# in this package, we have two objects
#  HELLOMSG - a string that contain the message
#  hello(@msg) - a function that print the message. It also returns the message
#     msg is the optional argument. The default value is to print HELLOMSG
#     but you can use a different text

HELLOMSG = "Hello world from hellopkg"

func hello(msg = HELLOMSG):
  print(msg)
  return msg
