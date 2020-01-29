from ...model.config.FileOption import FileOption
from .OptionView import OptionView
from PyQt5 import QtWidgets


class FileOptionView(OptionView):

    def __init__(self, parent: QtWidgets.QWidget, option: FileOption):
        self.__option: FileOption = option
        super().__init__(parent, option.name, option.description)

    @property
    def option(self) -> FileOption:
        return self.__option