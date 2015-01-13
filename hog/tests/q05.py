test = {
  'names': [
    'q05',
    '5',
    'q5'
  ],
  'params': {
    'doctest': {
    
    }
  },
  'points': 3,
  'suites': [
    [
      {
        'answer': '353222728f4212135d051c71d83b64c0',
        'choices': [
          'While score0 and score1 are both less than goal',
          'While at least one of score0 or score1 is less than goal',
          'While score0 is less than goal',
          'While score1 is less than goal'
        ],
        'locked': True,
        'question': """
        The variables score0 and score1 are the scores for both
        players. Under what conditions should the game continue?
        """,
        'type': 'concept'
      },
      {
        'answer': '0b7326c1fa456698ab316b845031a4a5',
        'choices': [
          'strategy1(score1, score0)',
          'strategy1(score0, score1)',
          'strategy1(score1)',
          'strategy1(score0)'
        ],
        'locked': True,
        'question': """
        If strategy1 is Player 1's strategy function, score0 is
        Player 0's current score, and score1 is Player 1's current
        score, then which of the following demonstrates correct
        usage of strategy1?
        """,
        'type': 'concept'
      },
      {
        'answer': '02e713b742d935bc81a0e54743c46aae',
        'choices': [
          """
          After the current player takes her turn, and if either
          player's score is double the other player's score
          """,
          """
          After the current player takes her turn, and if the
          current player's score is double her opponent's score
          """,
          """
          Before the current player takes her turn, and if either
          player's score is double the other player's score
          """,
          """
          Before the current player takes her turn, and if the
          current player's score is double her opponent's score
          """
        ],
        'locked': True,
        'question': 'Recall the "swine swap" rule. When does this rule apply?',
        'type': 'concept'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(5), always(5))
        (92, 106)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(2), always(2))
        (17, 102)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(2), always(10))
        (19, 120)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(0), always(0))
        (101, 97)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(0), always(2))
        (100, 95)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(0), weird_strat)
        (64, 109)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(weird_strat, weird_strat)
        (108, 93)
        """,
        'type': 'doctest'
      }
    ],
    [
    
    ],
    [
    
    ]
  ]
}