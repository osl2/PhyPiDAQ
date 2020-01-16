from typing import Type, NoReturn

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from .DragItemView import DragItemView
from .ItemView import ItemView
from .WorkspaceItemView import WorkspaceItemView


class ListItemView(ItemView):
    def __init__(self, main: QWidget, item: Type[WorkspaceItemView]):
        super().__init__(None)

        self.__main = main
        self.__item: Type[WorkspaceItemView] = item
        # TODO: Sensor Fehlermeldung

        self.__init_ui()

    def __init_ui(self) -> NoReturn:
        # TODO
        pass

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        if event.buttons() == Qt.LeftButton:
            item = DragItemView(self.__main, event, self.__item)
            item.move(self.mapTo(self.__main, QPoint(0, 0)))
            item.show()
            item.grabMouse()
        
        super(ListItemView, self).mousePressEvent(event)
