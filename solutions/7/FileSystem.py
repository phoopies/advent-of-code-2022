from typing import List, Union
from Folder import Folder
from File import File


class FileSystem:
    def __init__(self) -> None:
        self.root = Folder("/", None)
        self.current: Folder = self.root

    def handle_command(self, command: str, args: List[str]):
        if command == "cd":
            self.cd(args[0])
        elif command == "ls":
            pass  # print(self.current)

    def cd(self, where: str) -> None:
        if where == "/":
            self.current = self.root
        elif where == "..":
            if not self.current.parent:
                print("Current directory does not have a parent")
                return
            self.current = self.current.parent
        else:
            i = self.current.find(where)
            if i == -1:
                print(f"{where} does not exist in the current directory")
                return
            self.current = self.current.folders[i]

    def add(self, other: Union["Folder", File]):
        self.current.add(other)
