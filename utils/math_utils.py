# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    math_utils.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/25 19:33:32 by auguste           #+#    #+#              #
#    Updated: 2024/04/25 23:13:32 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def pow(number: float, power: int) -> float:
    result = 1
    is_power_negative = False

    if power < 0:
        power = -power
        is_power_negative = True

    i = 0
    while i < power:
        result *= number
        i += 1

    if is_power_negative:
        return 1.0 / result

    return result


def sqrt(number: float) -> float:
    if number <= 0.0:
        return 0.0

    tmp = 0.0
    result = number / 2.0

    while result != tmp:
        tmp = result
        result = (number / tmp + tmp) / 2

    return result
