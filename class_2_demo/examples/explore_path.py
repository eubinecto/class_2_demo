from pathlib import Path


def main():
    my_path = Path()
    # 뭔지 모르겠지만 출력해보니 현재 경로를 출력함.
    print(my_path.resolve())


if __name__ == '__main__':
    main()