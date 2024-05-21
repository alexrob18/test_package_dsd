"""
Test code
"""


def say_many_hello(message, nb_of_hello: int = 1):
    """


    :param message:
    :param nb_of_hello:
    :return:
    """
    for _ in range(nb_of_hello):
        print(message)


if __name__ == "__main__":

    message = "Bonjour Monde"
    say_many_hello(message, 3)