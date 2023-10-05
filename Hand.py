from MSDie import MSDie
class Hand:
    """
    A hand of dice, all with the same number of sides.

    Instance variables:
      num_sides - the number of faces each die has
      num_dice  - the number of dice in the hand
      dice      - a list of length num_dice, consisting of MSDie objects each with num_sides faces
    """

    def __init__(self, num_sides, num_dice):
        """
        Roll the hand for the first time. Dice are initialized as rolled with a MSDie.current_value.
        """
        # YOUR CODE HERE
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.dice = []
        for i in range(self.num_dice):
            self.dice.append(MSDie(self.num_sides))
    def __str__(self):
        # YOUR CODE HERE
        str_list = []
        for die in self.dice:
            str_list.append(str(die))
        return ' '.join(str_list)

    def __repr__(self):
        # YOUR CODE HERE
        result = []
        for die in self.dice:
            result.append(repr(die))
        return ', '.join(result)
        #return "MSDie ({}): {}".format(self.num_sides, self.num_dice)

    def roll(self):
        """
        Randomly assign new values to all the MSDie instances in self.dice: that is, reroll the entire hand.
        """
        # YOUR CODE HERE
        for die in self.dice:
            die.roll()
        
    def values(self):
        """
        Return a list of the current_value values for each of the MSDie instances in self.dice.
        """
        # YOUR CODE HERE
        value_list = []
        for die in self.dice:
            value_list.append(die.current_value)
        return value_list
        
    def counts(self):
        """
        Return a list of int values. The value in position i in the returned list is the number
        of MSDie instances in self.dice with current_value == i. Note that the 0th entry of the list is unused.
        """
        # YOUR CODE HERE
        count_list = []
        for _ in range(0, self.num_sides + 1):
            count_list.append(0)
        for i in range(1, self.num_sides + 1):
            for die in self.dice:
                if i == die.current_value:
                    count_list[die.current_value] += 1
        return count_list