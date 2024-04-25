TOKEN_TYPE_NONE = "none"            # Value = none
TOKEN_TYPE_OPERATOR = "operator"    # Value = which operator
TOKEN_TYPE_NUMBER = "number"        # Value = number ^^
TOKEN_TYPE_X = "x"                  # Value = power
TOKEN_PARENTHESES = "parentheses"   # Value = list of token in parenthese

class Token:
    def __init__(self):
        self.type = TOKEN_TYPE_NONE
        self.value = None
