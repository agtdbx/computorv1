# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operator.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/26 20:16:09 by auguste           #+#    #+#              #
#    Updated: 2024/04/27 12:27:14 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from type.token import          Token
from type.parentheses import    Parentheses

################################################################################
# Power ########################################################################
class Power:
    def __init__(self, number, power) -> None:
        self.number = number
        self.power = power

    def __str__(self) -> str:
        return str(self.number) + '^' + str(self.power)

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "power :\n"
        depth += 2

        string += self.number.to_string(depth) + '\n'
        string += self.power.to_string(depth)

        return string

    # Getters ##################################################################

    def get_tokens_left(self) -> list:
        number_type = type(self.number)

        if number_type == Parentheses:
            return self.number.tokens

        elif number_type == Power:
            return self.number.get_tokens_left()

        return []

    def get_tokens_right(self) -> list:
        power_type = type(self.power)

        if power_type == Parentheses:
            return self.power.tokens

        elif power_type == Power:
            return self.number.get_tokens_right()

        return []


################################################################################
# Multiplication ###############################################################
class Multiplication:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " * " + str(self.right)

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "mutiplication :\n"
        depth += 2

        string += self.left.to_string(depth) + '\n'
        string += self.right.to_string(depth)

        return string

    # Getters ##################################################################

    def get_tokens_left(self) -> list:
        left_type = type(self.left)

        if left_type == Parentheses:
            return self.left.tokens

        elif left_type == Power\
                or left_type == Multiplication or left_type == Division:
            return self.left.get_tokens_left()

        return []

    def get_tokens_right(self) -> list:
        right_type = type(self.right)

        if right_type == Parentheses:
            return self.right.tokens

        elif right_type == Power\
                or right_type == Multiplication or right_type == Division:
            return self.right.get_tokens_right()

        return []


################################################################################
# Division #####################################################################

class Division:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " / " + str(self.right)

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "division :\n"
        depth += 2

        string += self.left.to_string(depth) + '\n'
        string += self.right.to_string(depth)

        return string

    # Getters ##################################################################

    def get_tokens_left(self) -> list:
        left_type = type(self.left)

        if left_type == Parentheses:
            return self.left.tokens

        elif left_type == Power\
                or left_type == Multiplication or left_type == Division:
            return self.left.get_tokens_left()

        return []

    def get_tokens_right(self) -> list:
        right_type = type(self.right)

        if right_type == Parentheses:
            return self.right.tokens

        elif right_type == Power\
                or right_type == Multiplication or right_type == Division:
            return self.right.get_tokens_right()

        return []


################################################################################
# Addition #####################################################################
class Addition:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " + " + str(self.right)

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "addition :\n"
        depth += 2

        string += self.left.to_string(depth) + '\n'
        string += self.right.to_string(depth)

        return string

    # Getters ##################################################################

    def get_tokens_left(self) -> list:
        left_type = type(self.left)

        if left_type == Parentheses:
            return self.left.tokens

        elif left_type == Power\
                or left_type == Multiplication or left_type == Division\
                or left_type == Addition or left_type == Substraction:
            return self.left.get_tokens_left()

        return []

    def get_tokens_right(self) -> list:
        right_type = type(self.right)

        if right_type == Parentheses:
            return self.right.tokens

        elif right_type == Power\
                or right_type == Multiplication or right_type == Division\
                or right_type == Addition or right_type == Substraction:
            return self.right.get_tokens_right()

        return []

################################################################################
# Substraction #################################################################
class Substraction:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " - " + str(self.right)

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "substraction :\n"
        depth += 2

        string += self.left.to_string(depth) + '\n'
        string += self.right.to_string(depth)

        return string

    # Getters ##################################################################

    def get_tokens_left(self) -> list:
        left_type = type(self.left)

        if left_type == Parentheses:
            return self.left.tokens

        elif left_type == Power\
                or left_type == Multiplication or left_type == Division\
                or left_type == Addition or left_type == Substraction:
            return self.left.get_tokens_left()

        return []

    def get_tokens_right(self) -> list:
        right_type = type(self.right)

        if right_type == Parentheses:
            return self.right.tokens

        elif right_type == Power\
                or right_type == Multiplication or right_type == Division\
                or right_type == Addition or right_type == Substraction:
            return self.right.get_tokens_right()

        return []
