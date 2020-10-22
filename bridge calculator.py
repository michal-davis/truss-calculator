import math
'''A highly simplified calculator for finding forces in trusses
Requires that the truss be regular (all diagonal members same length, among other things)
Does not set up the equations for you - just solves them
Wouldn't really teach you much if it did'''

# bridge attributes
force_on_joint = 350
number_of_span_joints = 5
force_on_end = force_on_joint * number_of_span_joints / 2
y_component_multiplier = math.sqrt(3) / 2
x_component_multiplier = 1 / 2


def is_number(thing):
    # not mine - from https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
    try:
        float(thing)
        return True
    except ValueError:
        return False


def find_component_multiplier(variable):
    if variable.endswith("x"):
        return 1 / x_component_multiplier
    if variable.endswith("y"):
        return 1/ y_component_multiplier
    return 1

def check_side_for_unknown(side, other_side):
    for index, element in enumerate(side):
        if not is_number(element):
            index_of_unknown = index
            # every item on the other side, minus every item but the unknown on this side,
            # multiplied by some factor determined by whether this unknown is an x or y component
            return find_component_multiplier(element) * (sum(other_side) -
                                                sum(side[:index_of_unknown:])
                                                - sum(side[index_of_unknown + 1::])
                                                )
    return -1

def solve_static_equation(left_side, right_side):
    ''' takes two lists, one of which contains the unknown. There may only be exactly one unknown. The unknown should be expressed as any string
    returns the value of the unknown'''
    value_of_unknown = check_side_for_unknown(right_side, left_side)

    if value_of_unknown == -1:
        value_of_unknown = check_side_for_unknown(left_side, right_side)

    if value_of_unknown == -1:
        return "Error: no unknown found"

    return value_of_unknown


if __name__ == "__main__":
    '''how to use:
    set up a dictionary (like vars just below) with all the variables you need to solve for
    write out the equations you want to use somewhere else (I find it kinda hard to keep track of them in here, at least)
    set items in your dictionary equal to the results of a solve_static_equation call,
    with all the elements on one side of the equation in the first argument as a list
    and the same thing for the terms on the other side in the second argument
     * be sure that it's a [] list not just a number if there's only one term *
     use a string as the one unknown in the equation
     ex. 1 + 2 = x is input as
     solve_static_equation([1, 2], ["x"])'''
     sample_dictionary = {"x": -1, "z": -1}
     solve_static_equation([1, 2], ["x"])
