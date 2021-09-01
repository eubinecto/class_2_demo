
from class_2_demo.paths import TXT_PATH


def main():
    with open(TXT_PATH, 'r') as fh:
        text = fh.read()

    print(text)


if __name__ == '__main__':
    main()