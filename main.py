import random

def main() ->list[int]:
    """The main function to be callled by the pipeline

    :return: _description_
    :rtype: list
    """
    _list = [random.randint(0,20) for i in range(50)]

    return _list
