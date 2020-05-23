import sys
from .field import Field
from .essences import Fish, CrayFish, Rock, EmptyCell


def main(src=sys.stdin, dst=sys.stdout):
    gens = int(src.readline().strip())
    n, m = map(int, src.readline().strip().split())
    input_data = [src.readline().strip() for i in range(n)]
    field = Field(input_data)
    field.run(gens)
    print(field, file=dst)


if __name__ == '__main__':
    main()
