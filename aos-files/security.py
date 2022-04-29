# Links that may help
# https://serverfault.com/questions/330069/how-to-create-an-sha-512-hashed-password-for-shadow
# 

# I'm too lazy to write any code so here's concept

banned = [] # Structure: banned = [('Username', 'Sha512 hash of pass'), etc..]
restricted = [] # Structure: restricted = [('Username', 'Sha512 hash of pass'), etc..]
valid = [] # Structure: valid = [('Username', 'Sha512 hash of pass'), etc..]
waiting = 0
# Structure: waiting = Cannot be determined, but concept is that we make a seperate thread that
# runs while the user is entering login details and that thread closes after the user logs in. 
# Incorrect password shouldn't close thread.

# However we can't retrieve credentials from someone who's logging in (duh) so we can only count the number of people waiting, not in a list.
import os
# flask ws: implement ip ban?
# DONT REMOVE COMMENTS!
# also once i implemented login system in PHP so basically it works 
# like this:
#   On Signup:
#      Store the username and sha512 hash of a password in a file.
#      [ Also, make sure the username is only alphanumeric chars to prevent xss]
#      [ ]
#   On Login(Username, Password):
#      If the Username is in file:
#        Retrieve Sha512 hash from file.
#        If The Sha512 Hash Of The Password Is equal to the Sha512 hash of the password the user entered, 
#           Logged In!
#        Else
#           Not logged in!
