""" Access MySQL database.
"""

import mysql.connector as mariadb


class AgentSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(AgentSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Agent(object):
    __metaclass__ = AgentSingleton
    _host = '127.0.0.1'
    _user = 'root'
    _passwd = 'sh791114'
    _db_conn = None
    _db_cursor = None
    def connect(self, db_name=None):
        """ Connect to db
            Args:
            db_name:    database name for db connecting
            Returns:
            Raises:
            Native exceptions.
            """
        # --> open database connection
        if db_name:
            #db_conn = mariadb.connect(self._host,
            #                          self._user,
            #                          self._passwd,
            #                          db_name)
            self._db_conn = mariadb.connect(user=self._user,
                                            password=self._passwd,
                                            database=db_name)
        else:
            #db_conn = mariadb.connect(self._host,
            #                          self._user,
            #                          self._passwd)
            self._db_conn = mariadb.connect(user=self._user,
                                            password=self._passwd)

        # --> prepare a cursor object using cursor() method
        self._db_cursor = self._db_conn.cursor()

    def query_from_table(self, epicenter):
        query_command = "SELECT epicenter FROM earthquake WHERE epicenter = %19.4f" % epicenter

        print(query_command)
        self._db_cursor.execute(query_command)
        answer = self._db_cursor.fetchall()

        if answer:
            print("Found the number")
            print(answer)
        else:
            print("Not Found")
            print(answer)


class Account(Agent):
    name = None
    _epicenter = None
    def __init__(self, name):
        self.name = name

    def query(self, epicenter):
        _key = None
        self._epicenter = epicenter

        if self._epicenter[2] >= 0:
            _key = 10**4 + abs(self._epicenter[2])
        else:
            _key = abs(self._epicenter[2])
        if self._epicenter[1] >= 0:
            _key = _key + 10**11 + abs(self._epicenter[1]) * 10**9
        else:
            _key = _key + abs(self._epicenter[1]) * 10**9
        if self._epicenter[0] >= 0:
            _key = _key + abs(self._epicenter[0]) * 10**16
        else:
            _key = -(_key + abs(self._epicenter[0]) * 10**16)

        AgentAccount = Agent()
        AgentAccount.connect("singleton")
        AgentAccount.query_from_table(_key)


def main():
    """ Main flow code.
    Args:
    Returns:
    Raises:
        Native exceptions.
    """
    accounts = []
    option = 1

    while option != '3':
        option = input('Choose to [1]create user account [2]choose a user account [3]exit:')
        if option == '1':
            name = input('Type in the account name:')
            accounts.append(Account(name))
        elif option == '2':
            name_account = input('Type in the user account\'s name:')
            for account in accounts:
                if account.name == name_account:
                    epicenter = [float(x) for x in input('Type in the epicenter:').split()]
                    account.query(epicenter)
                    break
        elif option == '3':
            print('Goodbye')
        else:
            print('Wrong option. Please choose again')

if __name__ == "__main__":
    main()
