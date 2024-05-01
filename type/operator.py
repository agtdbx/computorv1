# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operator.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/26 20:16:09 by auguste           #+#    #+#              #
#    Updated: 2024/05/01 01:49:08 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.parentheses import    Parentheses

################################################################################
# Power ########################################################################
class Power:
    def __init__(self, number, power) -> None:
        self.left = number
        self.right = power

    def __str__(self) -> str:
        return str(self.left) + '^' + str(self.right)

    def __eq__(self, value) -> bool:
        if value == None:
            return False
        return self.left == value.left and self.right == value.right

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "power :\n"
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
            return [self.left]

        return []

    def get_tokens_right(self) -> list:
        right_type = type(self.right)

        if right_type == Parentheses:
            return self.right.tokens

        elif right_type == Power\
                or right_type == Multiplication or right_type == Division\
                or right_type == Addition or right_type == Substraction:
            return [self.right]

        return []

    # Public methods ###########################################################

    def copy(self):
        return Power(self.left.copy(), self.right.copy())


################################################################################
# Multiplication ###############################################################
class Multiplication:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " * " + str(self.right)

    def __eq__(self, value) -> bool:
        if value == None:
            return False
        return self.left == value.left and self.right == value.right

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
                or left_type == Multiplication or left_type == Division\
                or left_type == Addition or left_type == Substraction:
            return [self.left]

        return []

    def get_tokens_right(self) -> list:
        right_type = type(self.right)

        if right_type == Parentheses:
            return self.right.tokens

        elif right_type == Power\
                or right_type == Multiplication or right_type == Division\
                or right_type == Addition or right_type == Substraction:
            return [self.right]

        return []

    # Public methods ###########################################################

    def copy(self):
        return Multiplication(self.left.copy(), self.right.copy())


################################################################################
# Division #####################################################################

class Division:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " / " + str(self.right)

    def __eq__(self, value) -> bool:
        if value == None:
            return False
        return self.left == value.left and self.right == value.right

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
                or left_type == Multiplication or left_type == Division\
                or left_type == Addition or left_type == Substraction:
            return [self.left]

        return []

    def get_tokens_right(self) -> list:
        right_type = type(self.right)

        if right_type == Parentheses:
            return self.right.tokens

        elif right_type == Power\
                or right_type == Multiplication or right_type == Division\
                or right_type == Addition or right_type == Substraction:
            return [self.right]

        return []

    # Public methods ###########################################################

    def copy(self):
        return Division(self.left.copy(), self.right.copy())


################################################################################
# Addition #####################################################################
class Addition:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " + " + str(self.right)

    def __eq__(self, value) -> bool:
        if value == None:
            return False
        return self.left == value.left and self.right == value.right

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
            return [self.left]

        return []

    def get_tokens_right(self) -> list:
        right_type = type(self.right)

        if right_type == Parentheses:
            return self.right.tokens

        elif right_type == Power\
                or right_type == Multiplication or right_type == Division\
                or right_type == Addition or right_type == Substraction:
            return [self.right]

        return []

    # Public methods ###########################################################

    def copy(self):
        return Addition(self.left.copy(), self.right.copy())

################################################################################
# Substraction #################################################################
class Substraction:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " - " + str(self.right)

    def __eq__(self, value) -> bool:
        if value == None:
            return False
        return self.left == value.left and self.right == value.right

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
            return [self.left]

        return []

    def get_tokens_right(self) -> list:
        right_type = type(self.right)

        if right_type == Parentheses:
            return self.right.tokens

        elif right_type == Power\
                or right_type == Multiplication or right_type == Division\
                or right_type == Addition or right_type == Substraction:
            return [self.right]

        return []

    # Public methods ###########################################################

    def copy(self):
        return Substraction(self.left.copy(), self.right.copy())
