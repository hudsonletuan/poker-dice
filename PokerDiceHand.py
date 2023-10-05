import random

class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides

    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides + 1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        # return "MSDie({}) : {}".format(self.num_sides, self.current_value)
        return f"MSDie({self.num_sides}) : {self.current_value}"
    
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
    
    def has_five_of_a_kind(self):
        if 5 in self.counts():
            return True
        
    def has_four_of_a_kind(self):
        if 4 in self.counts():
            return True
        
    def has_three_of_a_kind(self):
        if 3 in self.counts():
            return True
        
    def has_one_pair(self):
        if 2 in self.counts():
            return True
        
    def has_two_pair(self):
        result = 0
        for x in self.counts():
            if x == 2:
                result += 1
        if result == 2:
            return True
        
    def has_full_house(self):
        if 3 in self.counts() and 2 in self.counts():
            return True
        
    def has_straight(self):
        if self.counts()[1] != 0 and self.counts()[-1] != 0:
            return False
        count = 0
        for x in self.counts():
            if x == 1:
                count += 1
        if count == 5:
            return True
        
    def has_short_straight(self):
        if self.counts()[3] == 0:
            return False
        if self.counts()[4] == 0:
            return False
        little_count = 0
        for x in self.counts():
            if x == 1 or x == 2:
                little_count += 1
        if little_count == 4 or little_count == 5:
            return True
        
    def rank(self):
        if self.has_five_of_a_kind() == True:
            return "has five of a kind" # [DR: `return print` is always going to return None.]
        if self.has_four_of_a_kind() == True: # [DR: Just return the strings.]
            return "has four of a kind"
        if self.has_full_house() == True:
            return "has full house"
        if self.has_straight() == True:
            return "has straight"
        if self.has_short_straight() == True:
            return "has short straight"
        if self.has_three_of_a_kind() == True:
            return "has three of a kind"
        if self.has_two_pair() == True:
            return "has two pairs"
        if self.has_one_pair() == True:
            return "has one pair"
        else:
            return "has nothing"

class PokerDiceHand(Hand):

    def __init__(self):
        # YOUR CODE HERE
        self.num_sides = 6
        self.num_dice = 5
        self.dice = []
        for i in range(self.num_dice):
            self.dice.append(MSDie(self.num_sides))

    def reroll(self, pos_list):
        """
        The `reroll()` method takes a list of indices (positions in the dice list,
        that is `int` values from 1 through 5). For example, `h.reroll([2, 3])`
        rerolls `h.dice[1]` and `h.dice[2]`, leaving `h.dice[0]`, `h.dice[3]`, and
        `h.dice[4]` alone. If `reroll()` method is passed any values in this
        list that are not integers, or that are not between 1 and 5, it raises `ValueError`.
        """
        # YOUR CODE HERE
        for i in pos_list:
#            if type(i) != type(1):
#                raise ValueError
#            elif not (1 <= i) and not (1 < 5):
#                raise ValueError
            self.dice[i - 1].roll()
        return self.dice