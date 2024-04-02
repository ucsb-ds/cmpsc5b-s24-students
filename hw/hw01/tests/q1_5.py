OK_FORMAT = True

test = {   'name': 'q1_5',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> # It looks like your simulation isn't random\n>>> np.std([simulate() for _ in range(1000)]) > 0\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> all(possible_area_codes == np.arange(200, 1000))\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> np.random.seed(10)\n>>> abs(np.mean([simulate() for _ in range(1000)]) - (1/16)) <= 0.02\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
