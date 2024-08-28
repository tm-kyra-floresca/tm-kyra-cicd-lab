import sys

def main(num_a, num_b):
    num_a = int(num_a)
    num_b = int(num_b)

    print(f'NUM_A: {num_a}')
    print(f'NUM_B: {num_b}')
    print(f'SUM: {num_a + num_b}')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
