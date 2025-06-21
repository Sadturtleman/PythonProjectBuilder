from interface.builder import Builder
import os
import subprocess

class DefaultProjectBuilder(Builder):
    def _build(self, projectName: str, path: str):
        self.projectdir = os.path.join(path, projectName)

        if not os.path.exists(self.projectdir):
            print(f"[DefaultProjectBuilder] 경고: 프로젝트 디렉터리가 존재하지 않습니다: {self.projectdir}")
            return

        self.__createDirs()

    def __createDirs(self):
        dirs_to_create = ["res", "docs"]

        for d in dirs_to_create:
            full_path = os.path.join(self.projectdir, d)
            try:
                os.makedirs(full_path, exist_ok=True)
                print(f"[DefaultProjectBuilder] 디렉토리 생성됨: {full_path}")
            except OSError as e:
                print(f"[DefaultProjectBuilder] 디렉토리 생성 실패: {full_path} - {e}")

        # 이미 존재할 수 있는 디렉토리 안내만
        for d in ["src", "tests"]:
            full_path = os.path.join(self.projectdir, d)
            if os.path.exists(full_path):
                print(f"[DefaultProjectBuilder] '{d}/' 디렉토리는 이미 존재함 (Poetry가 생성한 것으로 추정)")


class PythonFileBuilder(Builder):
    def _build(self, projectName: str, path: str):
        src_path = os.path.join(path, projectName, "src")
        if not os.path.exists(src_path):
            raise FileNotFoundError(f"[PythonFileBuilder] {src_path} 폴더가 존재하지 않습니다. DefaultProjectBuilder가 먼저 실행되어야 합니다.")
        
        main_path = os.path.join(src_path, "main.py")
        with open(main_path, "w", encoding="utf-8") as f:
            f.write("# Entry point\n\nif __name__ == '__main__':\n    print('Hello, World!')")
        print("[PythonFileBuilder] main.py 생성 완료")


class PoetryNewBuilder(Builder):
    def _build(self, projectName: str, path: str):
        project_path = os.path.join(path, projectName)
        if os.path.exists(project_path):
            print(f"[PoetryNewBuilder] '{project_path}' 이미 존재합니다.")
            return
        
        try:
            subprocess.run(
                ["poetry", "new", "--src", projectName],
                cwd=path,
                check=True
            )
            print("[PoetryNewBuilder] poetry new 프로젝트 생성 완료")
        except subprocess.CalledProcessError as e:
            print(f"[PoetryNewBuilder] 실패: {e}")