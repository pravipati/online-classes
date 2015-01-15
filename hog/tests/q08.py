test = {
  'names': [
    'q08',
    '8',
    'q8'
  ],
  'points': 1,
  'suites': [
    [
      {
        'test': r"""
        >>> bacon_strategy(0, 0)
        5
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> bacon_strategy(70, 50)
        5
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> bacon_strategy(50, 70)
        0
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> bacon_strategy(32, 4, 5, 4)
        0
        """,
        'type': 'doctest'
      },
      {
        'test': r"""
        >>> bacon_strategy(20, 25, 5, 4)
        4
        """,
        'type': 'doctest'
      }
    ]
  ]
}