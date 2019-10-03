"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...

Ex: Input = ['Ryan', 'Kieran', 'Jason', 'Yous'], Output = ['Ryan', 'Yous']

Note: keep the original order of the names in the output.
"""

from  friend_foe import friend


def test_friend():
    """
    Test if friend returns correct values.
    """
    # Setup
    people  = ['Ryan', 'Kieran', 'Jason', 'Yous']
    friends = ['Ryan', 'Yous']

    # Exercise
    result = friend(people)

    # Verify
    assert result == friends

    # Cleanup - none necessary
