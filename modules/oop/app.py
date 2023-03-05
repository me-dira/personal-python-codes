class Task():
    __name: str
    __isDone: bool

    def __init__(self, name: str):
        self.__name = name

    def exec(self):
        raise TypeError('Not implemented')

    def getName(self) -> str:
        return self.__name

    def markAsDone(self) -> None:
        self.__isDone = True

    def isDone(self) -> bool:
        return self.__isDone


class InformationLoaderTask(Task):
    __target: str = None
    __data: str = None

    def __init__(self, name: str, target: str):
        Task.__init__(self, name)
        self.__target = target

    # Main and entry point

    def exec(self) -> bool:
        try:
            data = self.__downloadData()
            # Do what ever you like with data

            if data != None:
                return False

            return True

        except Exception as err:
            return False

    def getTarget(self) -> str:
        return self.__target

    # Private methods ----------------------------------

    def __downloadData(self):
        if (self.__data != None):
            return self.__data

        else:
            # ..... Data downloaded and passed to __data
            self.__data = "bulked data"
            return self.__data


class App:
    __tasks = []

    def __init__(self):
        pass

    def run(self):
        pass

    def addTask(self, task: Task):
        try:
            if isinstance(task, Task):
                self.__tasks.append(task)

        except Exception as err:
            raise err

    def removeTask(self, name: str) -> bool:
        try:
            index = self.__getTaskIndex(name)
            if index < 0:
                raise IndexError()

            self.__tasks.pop(index)
            return True

        except Exception as err:
            # Its not best case to return something here.
            # Better to manage the error and raise another error object
            # And generate more information.
            print("Error in removing task with name", name)
            return False

    # Private methods --------------------------------------|

    def __getTaskIndex(self, name: str):
        target_index = -1

        for i, task in enumerate(self.__tasks):
            if task.getName() == name:
                target_index = i

        return target_index
