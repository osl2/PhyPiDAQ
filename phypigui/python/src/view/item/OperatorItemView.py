from typing import Final

from PyQt5.QtWidgets import QWidget

from python.src.model.item import OperatorItem
from python.src.view.item.WorkspaceItemView import WorkspaceItemView


class OperatorItemView(WorkspaceItemView):
    FRAME_PATH: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget, id: int, icon_path: str):
        super().__init__(parent, id, icon_path)

        self.__model: OperatorItem = None