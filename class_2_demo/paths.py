
from pathlib import Path
from os import path

# 프로젝트의 디렉토리를 설정
ROOT_DIR = Path().resolve().parent.__str__()


# 이렇게 미리 경로를 선언해주면, 나중에 이 상수를 임포트만 해서 사용할 수 있습니다.
TXT_PATH = path.join(ROOT_DIR, "data", "text.txt")