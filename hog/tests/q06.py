test = {
  'names': [
    'q06',
    '6',
    'q6'
  ],
  'points': 2,
  'suites': [
    [
      {
        'test': r"""
        >>> dice = make_test_dice(3, 1, 5, 6)
        >>> averaged_dice = make_averaged(dice, 1000)
        >>> averaged_dice()  # average of calling dice 1000 times
        3.75
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': r"""
        >>> dice = make_test_dice(3, 1, 5, 6)
        >>> averaged_roll_dice = make_averaged(roll_dice, 1000)
        >>> averaged_roll_dice(2, dice)
        6.0
        """,
        'type': 'doctest'
      }
    ]
  ]
}