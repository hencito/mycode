#!/usr/bin/env python3
# create a list
my_list = [ "192.168.0.5", 5060, "UP" ]
# retrieve first item in the list via its index
print("The first item in the list (IP): " +  my_list[0])
# retrieve second item on the list via its index
print("The second item in the list (port): " + str(my_list[1]))
# retrieve last item on the list
print("The last item in the list (state): " + my_list[2])


# Challenge 01 - Please note that the answers are three versions of doing the same thing.
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
# example 1 - add up the strings, please note that you are concactinating a string to it
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# example 3 - use an 'f-string', you like 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")     
