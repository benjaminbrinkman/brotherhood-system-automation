# This is an example of what can be done with Brotherhood System Automation
# Read comments to learn about each parameter

# Any given apprun file is simply the definition of a few different python lists.
# Within each list, there is an arbitrary number of dictionaries, that are used
# to describe a run of an external application and some other properties.

# Currently, the dictionaries only need two properties.  command and asynchronous
#
# command takes simply a string with a command and any options it needs.
#
# asynchronous takes a boolean value (True or False) that states whether the application
# should move on to the next command asynchronously without waiting for this one to finish.

exampledictionary = {"command": "ls -l", "asynchronous": False}

# singlerun is a list of apps (defined in the above dictionary structure) that are simply run once
# when the brotherhood-system-automation app is run

singlerun = [
    exampledictionary,
]
