from abc import ABC, abstractmethod



class Father(ABC):

    @abstractmethod
    def show(self):
        '''test'''


class Son(Father):

    def show(self):
        print("some")


Son().show()


print(list([1, 2, 3]))


print([name for name in globals()])
import inspect

import test

for name, func in inspect.getmembers(test, inspect.isfunction):
    func()
