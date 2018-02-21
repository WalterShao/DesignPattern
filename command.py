#!/usr/bin/python
# -*- coding: UTF-8 -*-

""" Test programs.
"""

class Command():# pylint: disable=too-few-public-methods
    """ Command's parent class
    Public Attributes:
    Public Methods:
        execute : execute command
    """
    def execute(self):
        """ execute command
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        pass

class CommandInvoker():
    """ Command's parent class
    Public Attributes:
    Public Methods:
        add_command : add command object
        execute_all : execute all the commands
    """
    _all_cmds = []

    def add_command(self, cmd):
        """ Add new command
        Args:
            cmd : command
        Returns:
        Raises:
            Native exceptions.
        """
        self._all_cmds.append(cmd)
    def execute_all(self):
        """ Execute all the command
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        for cmd in self._all_cmds:
            cmd.execute()

class RetriveData(Command):# pylint: disable=too-few-public-methods
    """ Retrive data from stations
    Public Attributes:
    Public Methods:
        execute : execute command
    """
    def execute(self):
        """ execute command
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        print("Retrive data from stations")

class InformStation(Command):# pylint: disable=too-few-public-methods
    """ Inform station with computed earthquake location
    Public Attributes:
    Public Methods:
        execute : execute command
    """
    def execute(self):
        """ execute command
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        print("Inform stations with computed earthquake")

class AlertPeople(Command):# pylint: disable=too-few-public-methods
    """ Use message to alert people
    Public Attributes:
    Public Methods:
        execute : execute command
    """
    def execute(self):
        """ execute command
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        print("Query if alerting people with message")

class QueryTime(Command):# pylint: disable=too-few-public-methods
    """ Check the real travel time of stations
    Public Attributes:
    Public Methods:
        execute : execute command
    """
    def execute(self):
        """ execute command
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        print("Query the real travel time from stations")


def main():
    """ Main flow code.
    Args:
    Returns:
    Raises:
        Native exceptions.
    """

    retrieve = RetriveData()
    inform = InformStation()
    alert = AlertPeople()
    query = QueryTime()

    cmd_invoker = CommandInvoker()
    cmd_invoker.add_command(retrieve)
    cmd_invoker.add_command(inform)
    cmd_invoker.add_command(alert)
    cmd_invoker.add_command(query)

    cmd_invoker.execute_all()


if __name__ == '__main__':
    main()
