OK_FORMAT = True

test = {   'name': 'q3_4',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> print(isinstance(postban_rates, Table))\nTrue\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> print(postban_rates.num_rows == 44)\nTrue\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> print(np.all(postban_rates.column('Death Penalty') == False))\nTrue\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> print(np.all(postban_rates.column('Year') == 1973))\nTrue\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> print(all((elem in postban_rates.column('State') for elem in preban_rates.column('State'))))\nTrue\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
