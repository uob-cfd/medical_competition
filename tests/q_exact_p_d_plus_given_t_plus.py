test = {
  'name': 'Question exact_p_d_plus_given_t_plus',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'exact_p_d_plus_given_t_plus'
          >>> 'exact_p_d_plus_given_t_plus' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'exact_p_d_plus_given_t_plus'
          >>> # from its initial state (of ...)
          >>> exact_p_d_plus_given_t_plus is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(exact_p_d_plus_given_t_plus, 0.09183673)
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
