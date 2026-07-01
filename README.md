# Git 실습용 Python 계산기

이 폴더는 Git 실습을 위해 만든 아주 작은 Python 프로젝트입니다.

## 파일 설명

- `calculator.py`: 계산기 함수가 들어 있는 파일입니다.
- `test_calculator.py`: 계산기 함수가 잘 동작하는지 확인하는 테스트 파일입니다.

## 실행 방법

테스트를 실행하려면 터미널에서 아래 명령어를 입력합니다.

```bash
python3 -m unittest test_calculator.py
```

위 명령어는 `test_calculator.py`에 있는 모든 테스트를 실행합니다.
새 기능을 추가한 뒤에도 같은 명령어로 전체 테스트를 다시 확인하면 됩니다.

## 현재 기능

- `add(a, b)`: 두 값을 더한 결과를 돌려줍니다.
- `subtract(a, b)`: 첫 번째 값에서 두 번째 값을 뺀 결과를 돌려줍니다.

## 사용 예시

```python
from calculator import add, subtract

print(add(2, 3))       # 5가 출력됩니다.
print(subtract(7, 4))  # 3이 출력됩니다.
```
