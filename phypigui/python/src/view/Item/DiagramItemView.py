from abc import ABC
from typing import Final

from PyQt5.QtWidgets import QWidget

from ..Item.WorkspaceItemView import WorkspaceItemView


diagram_path = "../resources/images/items/diagram/"


class DiagramItemView(WorkspaceItemView, ABC):
    FRAME_PATH: Final[str] = ""  # TODO: frame erstellen

    def __init__(self, parent: QWidget, num_of_inputs: int = 1):
        super().__init__(parent, num_of_inputs, 0)

        # TODO: Model & DiagramView in jeder Klasse selbst hinzufügen


class TimeDiagramItemView(DiagramItemView):
    icon_path: str = diagram_path + 'time.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent)


class BarDiagramItemView(DiagramItemView):
    icon_path: str = diagram_path + 'bar.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent, 3)


class DualDiagramItemView(DiagramItemView):
    icon_path: str = diagram_path + 'dual.svg'

    def __init__(self, parent: QWidget):
        super().__init__(parent, 2)
