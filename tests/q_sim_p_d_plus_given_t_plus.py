test = {
  'name': 'Question sim_p_d_plus_given_t_plus',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'sim_p_d_plus_given_t_plus'
          >>> 'sim_p_d_plus_given_t_plus' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'sim_p_d_plus_given_t_plus'
          >>> # from its initial state (of ...)
          >>> sim_p_d_plus_given_t_plus is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0.054 < sim_p_d_plus_given_t_plus < 0.14
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
