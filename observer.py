#!/usr/bin/python
# -*- coding: UTF-8 -*-

""" Test programs.
"""

class Event():
    """ Control event by parent class
    Public Attributes:
    Public Methods:
        registeruser : register new user
        removeuser : remove specific user
        notifyuser : alert user with event
    """
    def registeruser(self, user):
        """ Register new user
        Args:
            user : user
        Returns:
        Raises:
            Native exceptions.
        """
        pass
    def removeuser(self, user):
        """ Remove specific user
        Args:
            user : user
        Returns:
        Raises:
            Native exceptions.
        """
        pass
    def notifyuser(self, event):
        """ Alert user with event
        Args:
            event : earthquake event
        Returns:
        Raises:
            Native exceptions.
        """
        pass

class User():
    """ Notify user by parent class
    Public Attributes:
    Public Methods:
        notify : user's action after notification
    """
    def notify(self, event):
        """ Notify user with event
        Args:
            event : earthquake event
        Returns:
        Raises:
            Native exceptions.
        """
        pass

class MessageUser(User):
    """ Message user after notification
    Public Attributes:
    Public Methods:
        notify(event) : print user's action after notification
    """
    _name = None
    def __init__(self, name):
        self._name = name
    def notify(self, event):
        """ Notify user by printing event
        Args:
            event : earthquake event ID
        Returns:
        Raises:
            Native exceptions.
        """
        result = event + " earthquake has been messaged to " + self._name
        print(result)

class EmailUser(User):
    """ Email user after notification
    Public Attributes:
    Public Methods:
        notify(event) : print user's action after notification
    """
    _name = None
    def __init__(self, name):
        self._name = name
    def notify(self, event):
        """ Notify user by printing event
        Args:
            event : earthquake event ID
        Returns:
        Raises:
            Native exceptions.
        """
        result = event + " earthquake has been emailed to " + self._name
        print(result)

class PhoneUser(User):
    """ Call user after notification
    Public Attributes:
    Public Methods:
        notify(event) : print user's action after notification
    """
    _name = None
    def __init__(self, name):
        self._name = name
    def notify(self, event):
        """ Notify user by printing event
        Args:
            event : earthquake event ID
        Returns:
        Raises:
            Native exceptions.
        """
        result = event + " earthquake has been phoned to " + self._name
        print(result)

class EarthquakeManager(Event):
    """ Control event by parent class
    Public Attributes:
    Public Methods:
        registeruser : register new user account
        removeuser : remove specific user account
        notifyuser : alert user with earthquake event
    """
    _users = []
    def registeruser(self, user):
        """ Register new user
        Args:
            user : user's account name
        Returns:
        Raises:
            Native exceptions.
        """
        self._users.append(user)
    def removeuser(self, user):
        """ Remove specific user
        Args:
            user : user's account name
        Returns:
        Raises:
            Native exceptions.
        """
        self._users.remove(user)
    def notifyuser(self, event):
        """ Alert user with event
        Args:
            event : earthquake event ID
        Returns:
        Raises:
            Native exceptions.
        """
        for user in self._users:
            user.notify(event)

def main():
    """ Main flow code.
    Args:
    Returns:
    Raises:
        Native exceptions.
    """
    option = None
    earthquakes = EarthquakeManager()

    while option != '3':
        option = input("Choose to [1]create an account [2]issue an earthquake [3]exit:")
        if option == '1':
            username = input("Type in the user name:")
            usertype = input("Choose to inform user with [1]message [2]email [3]phone:")
            if usertype == '1':
                user = MessageUser(username)
            elif usertype == '2':
                user = EmailUser(username)
            elif usertype == '3':
                user = PhoneUser(username)
            earthquakes.registeruser(user)
        elif option == '2':
            event = input("Type in the event ID:")
            earthquakes.notifyuser(event)
        elif option == '3':
            print("Goodbye...")
        else:
            print("Wrong option. Please type again.")


if __name__ == '__main__':
    main()
