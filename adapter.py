#!/usr/bin/python
# -*- coding: UTF-8 -*-

""" Test programs.
"""

class SystemA():
    """ Read and return user's input
    Public Attributes:
    Public Methods:
        read_data : read user's input
        query_data: return user's input
    """
    _data = None
    def read_data(self):
        """ Read input data
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        self._data = input("Type in a number to store in data:")

    def query_data(self):
        """ Return user's input
        Args:
        Returns:
            _data: user's input
        Raises:
            Native exceptions.
        """
        return self._data

class SystemB():
    """ Process and return data
    Public Attributes:
    Public Methods:
        process_data : pretend to process data
        query_data: print processed data
    """
    _data_processed = None
    def process_data(self):
        """ Pretend to process data
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        self._data_processed = ", has been processed"

    def query_data(self):
        """ Print processed data
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        print("The processed data, {}".format(self._data_processed))

class AdaptorSystemA():
    """ Adaptor of System A
    Public Attributes:
    Public Methods:
        read_data : read user's input
        query_data : return user's input
    """
    _system_a = SystemA()
    def read_data(self, data):
        """ Read input data
        Args:
            data : data to be read
        Returns:
        Raises:
            Native exceptions.
        """
        print("New preloaded data, {}, is for Client B".format(data))
        self._system_a.read_data()

    def query_data(self):
        """ Query input data
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        self._system_a.query_data()

class AdaptorSystemB():
    """ Adaptor of System B
    Public Attributes:
    Public Methods:
        process_data(data) : process data
        query_data : return processed data
    """
    _system_b = SystemB()
    _data = None
    def process_data(self, data):
        """ Process data
        Args:
            data : data to be processed
        Returns:
        Raises:
            Native exceptions.
        """
        self._data = data * 3
        self._system_b.process_data()
    def query_data(self):
        """ Print processed data
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        print("Processed result for new preloaded data is {}".format(self._data))
        self._system_b.query_data()


def client_a():
    """ Client A's procedure
    Args:
    Returns:
    Raises:
        Native exceptions.
    """
    system_a = SystemA()
    system_b = SystemB()
    system_a.read_data()
    system_b.process_data()
    system_b.query_data()

def client_b(data):
    """ Client B's procedure
    Args:
        data : data to be used
    Returns:
    Raises:
        Native exceptions.
    """
    system_a = AdaptorSystemA()
    system_b = AdaptorSystemB()
    system_a.read_data(data)
    system_b.process_data(data)
    system_b.query_data()

def main():
    """ Main flow code.
    Args:
    Returns:
    Raises:
        Native exceptions.
    """
    client_a()
    client_b(365)

if __name__ == '__main__':
    main()
