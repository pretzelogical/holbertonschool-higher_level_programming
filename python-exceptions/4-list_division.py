#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides 2 lists element by element

    Args:
        my_list_1 (int/float[]): list to divide
        my_list_2 (int/float[]): list to divide
        list_length (int): self_explanitory

    Errors:
        List member not float or int:
            print "wrong type"
        Division can't be done (divide by 0):
            print "division by 0"
        Either list is too short:
            print "out of range"
    """
    divided = []
    div_element = 0
    for i in range(list_length):
        try:
            div_element = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_element = 0
        except ZeroDivisionError:
            print("division by 0")
            div_element = 0
        except IndexError:
            print("out of range")
            div_element = 0
        finally:
            divided.append(div_element)
    return divided
