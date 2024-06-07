OK_FORMAT = True

test = {   'name': 'q1_9_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(prob_test) in set([float, np.float32, np.float64])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 0 <= prob_test <= 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(prob_test, 0.5)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
