test = {
  'names': [
    'q03',
    '3',
    'q3'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> select_dice(4, 24) == six_sided
        b06675f84ffdb5e2bb8bff43dc1a0f46
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(16, 64) == six_sided
        011e6a022b3155f85730a33e529457ef
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(0, 0) == six_sided
        b06675f84ffdb5e2bb8bff43dc1a0f46
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(50, 80) == six_sided
        011e6a022b3155f85730a33e529457ef
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}