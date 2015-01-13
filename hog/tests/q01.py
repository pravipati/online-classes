test = {
  'names': [
    'q01',
    '1',
    'q1'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> roll_dice(2, make_test_dice(4, 6, 1))
        0d67364f3a6639e82e67af0673b4cc6e
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> roll_dice(3, make_test_dice(4, 6, 1))
        e2f636ebfe71bb770b320ce6f799139c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> roll_dice(3, make_test_dice(1, 2, 3))
        e2f636ebfe71bb770b320ce6f799139c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> counted_dice = make_test_dice(4, 1, 2, 6)
        >>> roll_dice(3, counted_dice)
        e2f636ebfe71bb770b320ce6f799139c
        # locked
        >>> roll_dice(1, counted_dice)  # Make sure you call dice exactly num_rolls times!
        414f04076138a0647c6470ad3afd249d
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}