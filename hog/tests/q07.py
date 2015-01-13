test = {
  'names': [
    'q07',
    '7',
    'q7'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(3)   # dice always returns 3
        >>> max_scoring_num_rolls(dice)
        0d67364f3a6639e82e67af0673b4cc6e
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'answer': '0e744f4c776b38e9abaa8fa41a6ea656',
        'choices': [
          'The lowest num_rolls',
          'The highest num_rolls',
          'A random num_rolls'
        ],
        'locked': True,
        'question': """
        If multiple num_rolls are tied for the highest scoring
        average, which should you return?
        """,
        'type': 'concept'
      },
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(2)     # dice always rolls 2
        >>> max_scoring_num_rolls(dice)
        0d67364f3a6639e82e67af0673b4cc6e
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
        >>> max_scoring_num_rolls(dice)
        e2f636ebfe71bb770b320ce6f799139c
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}