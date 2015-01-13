test = {
  'names': [
    'q00',
    '0',
    'q0'
  ],
  'points': 0,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> test_dice = make_test_dice(4, 1, 2)
        >>> test_dice()
        b1dfe57e56297284419307592a8af908
        # locked
        >>> test_dice() # Second call
        e2f636ebfe71bb770b320ce6f799139c
        # locked
        >>> test_dice() # Third call
        b587b791ef1e90c186282b68a1ba1c16
        # locked
        >>> test_dice() # Fourth call
        b1dfe57e56297284419307592a8af908
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}