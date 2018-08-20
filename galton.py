from random import randint

def galton(h, b):
    containers = [0] * (h + 1)
    for _ in range(b):
        pos = 0
        for i in range(0, h):
            turn = randint(0, 1)
            if turn == 1:
                pos += 1
        containers[pos] = containers[pos] + 1

    return containers


def print_graph(dataset):
    for val in dataset:
        print('\n' + str(val))
        for i in range(0, val):
            print('.', end='')


#h= height of dalton board , b= number of balls
containers = galton(h=13, b=321)
print_graph(containers)
