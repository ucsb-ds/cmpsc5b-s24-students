OK_FORMAT = True

test = {   'name': 'q3_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> print(isinstance(preban_rates, Table))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> print(preban_rates.num_rows == 44)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> print(np.all(preban_rates.column('Death Penalty') == True))\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> print(np.all(preban_rates.column('Year') == 1971))\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> print(all((elem in death_penalty.column('State') for elem in preban_rates.column('State'))))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
