import projectBuilder

def run():
    poetry = projectBuilder.PoetryNewBuilder()
    default = projectBuilder.DefaultProjectBuilder()
    pythonfile = projectBuilder.PythonFileBuilder()

    poetry.setNext(default).setNext(pythonfile)
    poetry.create("MyProject", ".")


if __name__ == "__main__":
    run()