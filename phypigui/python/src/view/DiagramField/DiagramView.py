import time
from abc import ABC, abstractmethod
from typing import NoReturn, List, Dict

from mpl_toolkits import mplot3d
from matplotlib.axes import Subplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QSizePolicy, QFrame, QGridLayout

from ..Translator import Translator
from ..View import View
from ...model.item.DiagramItems.DiagramItem import DiagramItem
from ...model.item.DiagramItems.TimeDiagramItem import TimeDiagramItem
from ...model.item.DiagramItems.BarDiagramItem import BarDiagramItem
from ...model.item.DiagramItems.DualDiagramItem import DualDiagramItem
from ...model.item.DiagramItems.ThreeDimDiagramItem import ThreeDimDiagramItem
from .StartButtonView import StartButtonView


type_data = Dict[str, List[float]]


class DiagramViewMeta(type(QFrame), type(View)):
    pass


class DiagramView(QFrame, View, ABC, metaclass=DiagramViewMeta):
    """the super class of Time diagram, bar diagram and Dual diagram"""
    def __init__(self, data: type_data, item: DiagramItem, projection: str = 'rectilinear'):
        super().__init__()

        self._canvas = FigureCanvas(Figure(figsize=(4, 5), dpi=70))
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._canvas)
        self.setLayout(layout)

        self._ax: Subplot = self._canvas.figure.add_subplot(111, projection=projection)
        self._data: type_data = data
        self._item: DiagramItem = item
        self._item.attach(self)

        self.setStyleSheet("QFrame { border: 2px solid white; border-radius: 4px }")
        Translator.language_changed.signal.connect(self._draw_diagram)
        self.clear_diagram()

    @abstractmethod
    def _draw_diagram(self) -> NoReturn:
        pass

    @abstractmethod
    def _update_diagram(self, data: List[float]) -> NoReturn:
        pass

    @abstractmethod
    def clear_diagram(self) -> NoReturn:
        pass

    def update_view(self) -> NoReturn:
        self._update_diagram(self._item.data)

    def update_selected_view(self, selected: bool):
        border = "blue" if selected else "white"
        self.setStyleSheet("QFrame { border: 2px solid %s; border-radius: 4px }" % border)


class TimeDiagram(DiagramView):
    """this class represents a time diagram"""
    def __init__(self, item: TimeDiagramItem):
        """Initialising an TimeDiagram object

         Args:
             item (TimeDiagramItem): time plot diagram item
        """
        data: type_data = {'time': [], 'data': []}

        super().__init__(data, item)

    def _draw_diagram(self) -> NoReturn:
        self._ax.clear()

        self._ax.set_title(Translator.tr(self._item.name))
        self._ax.set_xlabel("s")
        self._ax.set_ylabel(self._item.unit[0])

        self._ax.plot(self._data['time'], self._data['data'])

        self._canvas.draw()

    def _update_diagram(self, data: List[float]) -> NoReturn:
        t = time.time() - StartButtonView.start_time
        while t - self._data['time'][0] > 10:
            for i in ['time', 'data']:
                self._data[i].pop(0)

        self._data['time'].append(t)
        self._data['data'].append(data[0])

        self._draw_diagram()

    def clear_diagram(self) -> NoReturn:
        self._data['time'] = [i / 5.0 for i in range(-50, 0)]
        self._data['data'] = [0.0] * 50

        self._draw_diagram()


class DualDiagram(DiagramView):
    """this class represents a dual diagram"""
    def __init__(self, item: DualDiagramItem):
        """Initialising an DualDiagram object

        Args:
            item (DualDiagramItem): plot diagram item
        """
        data: type_data = {'x': [0.0], 'y': [0.0]}

        super().__init__(data, item)

    def _draw_diagram(self) -> NoReturn:
        self._ax.clear()

        self._ax.set_title(Translator.tr(self._item.name))
        self._ax.set_xlabel(self._item.unit[0])
        self._ax.set_ylabel(self._item.unit[1])

        self._ax.plot(self._data['x'], self._data['y'])

        self._canvas.draw()

    def _update_diagram(self, data: List[float]) -> NoReturn:
        if len(self._data['x']) > 10:
            for i in ['x', 'y']:
                self._data[i].pop(0)

        for i, j in [['x', 0], ['y', 1]]:
            self._data[i].append(data[j])

        self._draw_diagram()

    def clear_diagram(self) -> NoReturn:
        for i in ['x', 'y']:
            self._data[i].clear()

        self._draw_diagram()


class BarDiagram(DiagramView):
    """this class represents a bar diagram """
    def __init__(self, item: BarDiagramItem):
        """Initialising an BarDiagram object

        Args:
            item (BarDiagramItem): bar chart diagram item
        """
        data: type_data = {'data': []}
        self.__labels: List[str] = ["first input", "second input", "third input"]

        super().__init__(data, item)

    def _draw_diagram(self):
        self._ax.clear()

        self._ax.set_title(Translator.tr(self._item.name))

        self._ax.bar(self.__labels, self._data['data'])

        self._canvas.draw()

    def _update_diagram(self, data: List[float]) -> NoReturn:
        self._data['data'] = data

        self._draw_diagram()

    def clear_diagram(self) -> NoReturn:
        self._data['data'] = [0.0] * 3

        self._draw_diagram()


class ThreeDimDiagram(DiagramView):
    """this class represents a 3D diagram"""
    def __init__(self, item: ThreeDimDiagramItem):
        """Initialising a ThreeDimDiagram object

        Args:
            item (ThreeDimDiagramItem): plot diagram item
        """
        data: type_data = {'x': [], 'y': [], 'z': []}

        super().__init__(data, item, '3d')

    def _draw_diagram(self) -> NoReturn:
        self._ax.clear()

        self._ax.set_title(Translator.tr(self._item.name))
        self._ax.set_xlabel(self._item.unit[0])
        self._ax.set_ylabel(self._item.unit[1])
        self._ax.set_zlabel(self._item.unit[2])

        self._ax.plot3D(self._data['x'], self._data['y'], self._data['z'])

        self._canvas.draw()

    def _update_diagram(self, data: List[float]) -> NoReturn:
        if len(self._data['x']) > 10:
            for i in ['x', 'y', 'z']:
                self._data[i].pop(0)

        for i, j in [['x', 0], ['y', 1], ['z', 2]]:
            self._data[i].append(data[j])

        self._draw_diagram()

    def clear_diagram(self) -> NoReturn:
        for i in ['x', 'y', 'z']:
            self._data[i].clear()

        self._draw_diagram()
