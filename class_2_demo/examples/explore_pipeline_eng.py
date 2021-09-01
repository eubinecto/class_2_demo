from transformers import pipeline
from sys import stdout
import logging
logging.basicConfig(stream=stdout, level=logging.INFO)


def main():
    # 정무님이 만들고 싶었던 것의 간단한 프로토타입을 구현.
    # 분류기를 가져오는 것 같고?
    classifier = pipeline("sentiment-analysis")
    # classifier -> __call__ (문장) -> list -> 첫번째 -> 결과
    result = classifier("I hate you")[0]
    print(result)
    # 한글은 학습을 하지 않은 감성분석 모델.
    result = classifier("나는 널 싫어해")[0]
    print(result)
    # 비꼬는 말에 대응? - saracasm에는 대응하지 못한다.
    result = classifier("Well, what a surprise.")[0]
    print(result)


if __name__ == '__main__':
    main()