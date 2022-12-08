from File import File
from typing import Union, List, Iterable


class Folder:
    def __init__(self, name: str, parent: "Folder") -> None:
        self.name = name
        self.parent: Folder = parent
        self.folders: List[Folder] = []
        self.files: List[File] = []

    def __str__(self) -> str:
        fpath = [self.name]
        parent = self.parent
        while parent:
            fpath.insert(0, parent.name)
            parent = parent.parent
        return f"{' -> '.join(fpath)} : {len(self.folders), len(self.files)} : ({self.size()})"

    def add(self, other: Union["Folder", File]):
        if isinstance(other, Folder):
            other.parent = self
            self.folders.append(other)
        else:
            self.files.append(other)

    def find(self, folder_name: str) -> int:
        folder_names = [f.name for f in self.folders]
        if folder_name not in folder_names:
            return -1
        return folder_names.index(folder_name)

    def size(self) -> int:
        return sum([f.size for f in self.files]) + sum([f.size() for f in self.folders])

    def get_folder_sizes(self) -> List[Union[int, Iterable[int]]]:
        return [self.size(), [f.get_folder_sizes() for f in self.folders]]

    def get_folder_sizes_flat(self) -> List[int]:
        sizes = [self.size()]
        for f in self.folders:
            sizes = sizes + f.get_folder_sizes_flat()
        return sizes
