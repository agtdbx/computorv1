# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    x.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/26 20:16:04 by auguste           #+#    #+#              #
#    Updated: 2024/05/01 00:11:00 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class X:
    def __init__(self) -> None:
        self.multiplication = 1
        self.power = 1

    def __str__(self) -> str:
        string = "x"
        if self.multiplication == -1:
            string = "-x"
        elif self.multiplication != 1:
            string = f"{self.multiplication}x"

        if self.power != 1:
            string += f"^{self.power}"

        return string

    def __eq__(self, value) -> bool:
        return self.multiplication == value.multiplication\
                and self.power == value.power

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + f"x[{self.multiplication},{self.power}]"

        return string

    # Public methods ###########################################################

    def copy(self):
        x = X()
        x.multiplication = self.multiplication
        x.power = self.power
        return x
