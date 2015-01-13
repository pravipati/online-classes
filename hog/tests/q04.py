test = {
  'names': [
    'q04',
    '4',
    'q4'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(1, 1, goal=100) # start can be 0 or 1
        >>> score0
        45c3dfe5cfe404cc9d7c2d858c9ddfce
        # locked
        >>> score1
        45c3dfe5cfe404cc9d7c2d858c9ddfce
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(2, 7, goal=100)
        >>> score0
        aa5583c8c6d4fd34018f09900374ac68
        # locked
        >>> score1
        0d67364f3a6639e82e67af0673b4cc6e
        # locked
        >>> start
        e2f636ebfe71bb770b320ce6f799139c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(8, 3, goal=100)
        >>> score0
        0d67364f3a6639e82e67af0673b4cc6e
        # locked
        >>> score1
        aa5583c8c6d4fd34018f09900374ac68
        # locked
        >>> start
        aa5583c8c6d4fd34018f09900374ac68
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(4, 3, goal=100)
        >>> score0
        55276f8aa6de04cbfb3423b6224f512b
        # locked
        >>> score1
        b1dfe57e56297284419307592a8af908
        # locked
        >>> start
        aa5583c8c6d4fd34018f09900374ac68
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(3, 4, goal=100)
        >>> score0
        b1dfe57e56297284419307592a8af908
        # locked
        >>> score1
        55276f8aa6de04cbfb3423b6224f512b
        # locked
        >>> start
        e2f636ebfe71bb770b320ce6f799139c
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}