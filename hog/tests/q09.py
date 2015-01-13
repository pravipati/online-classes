test = {
  'names': [
    'q09',
    '9',
    'q9'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> swap_strategy(23, 60) # 23 + (1 + abs(6 - 0)) = 30
        aa5583c8c6d4fd34018f09900374ac68
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(27, 17) # 27 + (1 + abs(1 - 7)) = 34
        23e1b9da9cf4a7d1fa29ae26512645ef
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(50, 80) # 1 + abs(8 - 0) = 9
        aa5583c8c6d4fd34018f09900374ac68
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(12, 12) # Baseline
        23e1b9da9cf4a7d1fa29ae26512645ef
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': """
        >>> swap_strategy(15, 34, 5, 4) # beneficial swap
        aa5583c8c6d4fd34018f09900374ac68
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(8, 9, 5, 4) # harmful swap
        b1dfe57e56297284419307592a8af908
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}