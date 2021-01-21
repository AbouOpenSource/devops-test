
def checker(expression):
    if len(expression) % 2 != 0:
        return False

    opening = ("(", "[", "{")
    closing = (")", "]", "}")
    mapping = {opening[0]: closing[0],
               opening[1]: closing[1],
               opening[2]: closing[2]}
    # start point well-formatted
    if expression[0] in closing:
        return False
    # end point well-formatted
    if expression[-1] in opening:
        return False

    closing_queue = []
    for letter in expression:
        if letter in opening:
            closing_queue.append(mapping[letter])
        elif letter in closing:
            if not closing_queue:
                return False
            if closing_queue[-1] == letter:
                closing_queue.pop()
            else:
                return False

    return True
