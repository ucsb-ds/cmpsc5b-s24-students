OK_FORMAT = True

test = {   'name': 'q3_6',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> print(rate_means.num_rows == 2)\nTrue\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> print(round(rate_means.where('Death Penalty', False).column(1).item(0), 15) == 8.120454540452272)\nTrue\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> print(round(rate_means.where('Death Penalty', True).column(1).item(0), 15) == 7.513636380386362)\nTrue\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
