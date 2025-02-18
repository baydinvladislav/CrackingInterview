import unittest


# my solution based on their solution
# Time Complexity: O(n * k)
# Space Complexity: O(k)
def max_duffel_bag_value(cake_tuples, weight_capacity):
    bags = [0] * (weight_capacity + 1)

    for i in range(len(bags)):
        current_max = 0
        for weight, value in cake_tuples:
            if weight == 0 and value != 0:
                return float('inf')

            if i >= weight:
                additional_bag_idx = i - weight
                current_max = max(current_max, value + bags[additional_bag_idx])

        bags[i] = current_max

    return bags[-1]


# my solution based on their solution
# Time Complexity: O(n * k)
# Space Complexity: O(k)
def fit_knapsack(cake_tuples, weight_capacity):
    # create dp array to store calculated results
    dp_arr = [0] * (weight_capacity + 1)

    # loop through all bag capacities from 0 to input capacity
    for current_capacity in range(len(dp_arr)):
        # reset after every capacity
        current_max_value = 0
        # loop through every item
        for weight, value in cake_tuples:
            # edge case, we have infinitive value in our bag
            if weight == 0 and value > 0:
                return float('inf')

            # if we have place for current item
            if weight <= current_capacity:
                # get index bag whose calculated value we can add to current value
                additional_bag_idx = current_capacity - weight
                # calculate current value plus calculated value on previous iteration
                max_value_with_that_cake = value + dp_arr[additional_bag_idx]
                # compare value with added item and without it
                current_max_value = max(current_max_value, max_value_with_that_cake)

        # save result for every bag
        dp_arr[current_capacity] = current_max_value

    # return target bag value
    return dp_arr[weight_capacity]


# their DP solution
# Time Complexity: O(n * k)
# Space Complexity: O(k)
def max_duffel_bag_value(cake_tuples, weight_capacity):
    # We make a list to hold the maximum possible value at every
    # duffel bag weight capacity from 0 to weight_capacity
    # starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in range(weight_capacity + 1):
        # Set a variable to hold the max monetary value so far
        # for current_capacity
        current_max_value = 0
        for cake_weight, cake_value in cake_tuples:
            # If a cake weighs 0 and has a positive value the value of
            # our duffel bag is infinite!
            if cake_weight == 0 and cake_value != 0:
                return float('inf')

            # If the current cake weighs as much or less than the
            # current weight capacity it's possible taking the cake
            # would get a better value
            if cake_weight <= current_capacity:
                # So we check: should we use the cake or not?
                # If we use the cake, the most kilograms we can include in
                # addition to the cake we're adding is the current capacity
                # minus the cake's weight. We find the max value at that
                # integer capacity in our list max_values_at_capacities
                bag_idx = current_capacity - cake_weight
                max_value_using_cake = (
                    cake_value + max_values_at_capacities[bag_idx]
                )

                # Now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake, current_max_value)

        # Add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight_capacity]


class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
