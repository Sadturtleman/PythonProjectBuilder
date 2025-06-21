from abc import ABC, abstractmethod

class Builder(ABC):
    def __init__(self):
        self.nextBuilder: Builder | None = None

    def setNext(self, builder: "Builder") -> "Builder":
        self.nextBuilder = builder
        return builder  # 체이닝 가능

    def create(self, projectName: str, path: str):
        self._build(projectName, path)
        if self.nextBuilder:
            self.nextBuilder.create(projectName, path)

    @abstractmethod
    def _build(self, projectName: str, path: str):
        pass
