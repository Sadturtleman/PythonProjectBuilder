# Dockerfile
FROM python:3.11-slim

# Poetry 설치
RUN pip install --no-cache-dir poetry

# 프로젝트 디렉터리 설정
WORKDIR /app

# pyproject.toml과 lock 파일 먼저 복사
COPY pyproject.toml poetry.lock* ./

# 종속성 설치 (가상환경은 프로젝트 안에 만들기)
RUN poetry config virtualenvs.in-project true \
    && poetry install --no-interaction --no-ansi

# 전체 프로젝트 복사
COPY . .

# 기본 실행 명령
CMD ["poetry", "run", "pytest"]
