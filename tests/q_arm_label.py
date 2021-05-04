test = {
  'name': 'Question arm_label',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'arm_label'
          >>> 'arm_label' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'arm_label'
          >>> # from its initial state (of ...)
          >>> arm_label is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You need something about the Test given the Disease
          >>> arm_label in (3, 4, 5, 6)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The disease is not present (D-)
          >>> arm_label in (4, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> arm_label == 5
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
