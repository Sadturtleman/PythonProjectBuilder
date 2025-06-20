FROM python:3.11-slim

# Poetry 설치
RUN pip install --no-cache-dir poetry

# 작업 디렉토리 설정
WORKDIR /app

# 전체 복사 먼저 (중요!)
COPY . .

# poetry 가상환경을 프로젝트 내부에 생성 + 설치
RUN poetry config virtualenvs.in-project true \
    && poetry install --no-interaction --no-ansi

# 기본 실행 명령 (pytest)
CMD ["poetry", "run", "pytest"]
