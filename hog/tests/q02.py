test = {
  'names': [
    'q02',
    '2',
    'q2'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> take_turn(2, 0,  make_test_dice(4, 6, 1))
        0d67364f3a6639e82e67af0673b4cc6e
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(3, 20, make_test_dice(4, 6, 1))
        e2f636ebfe71bb770b320ce6f799139c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(0, 35)
        55276f8aa6de04cbfb3423b6224f512b
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(0, 71)
        799f5230fcf128de00f2264719ab9961
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(0, 7)
        b700c9593871c1b6969ba0a954aa7f8f
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}