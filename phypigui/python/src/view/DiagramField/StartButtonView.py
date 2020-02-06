from typing import NoReturn

from PyQt5.QtCore import QRunnable, QThreadPool
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from ...GlobalSignals import GlobalSignals
from ..Translator import Translator
from ...model.manager.ManagerModel import ManagerModel


class StartButtonView(QPushButton):
    """This class represents the start button"""
    class Start(QRunnable):
        def run(self) -> NoReturn:
            ManagerModel.start()

    __button: 'StartButtonView'

    def __init__(self, parent):
        super().__init__(parent)

        StartButtonView.__button = self

        self.__is_started = False
        self.__start_icon = QIcon("../resources/images/buttons/start.svg")
        self.__stop_icon = QIcon("../resources/images/buttons/stop.svg")

        self.setFixedSize(31, 31)
        self.setIcon(self.__start_icon)

        self.clicked.connect(self.__on_click)
        GlobalSignals.about_to_quit.signal.connect(ManagerModel.stop)
        Translator.language_changed.signal.connect(self.__update_text)

        self.__update_text()

    def __update_text(self):
        tooltip = "Stop" if self.__is_started else "Start"
        self.setToolTip(Translator.tr(tooltip))

    def __on_click(self) -> NoReturn:
        if self.__is_started:
            ManagerModel.stop()
            self.setIcon(self.__start_icon)
        else:
            QThreadPool.globalInstance().start(self.Start())
            self.setIcon(self.__stop_icon)

        self.__is_started = not self.__is_started

        self.__update_text()
        self.clearFocus()

    @staticmethod
    def click() -> NoReturn:
        """a static method of on_click that executes the running of the program on the Managermodel"""
        StartButtonView.__button.__on_click()

    @staticmethod
    def interrupt_mp() -> bool:
        """Interrupt a measurement process in the model and set StartButtonView on 'stop-state'

        Returns:
            bool: True, if there was a measurement process running
        """
        was_running: bool = StartButtonView.__button.__is_started
        if was_running:
            StartButtonView.__button.__on_click()
        return was_running

    @staticmethod
    def start_mp() -> NoReturn:
        """Starts a measurement process in the model and set StartButtonView on 'start-state'"""
        if not StartButtonView.__button.__is_started:
            StartButtonView.click()

    @staticmethod
    def restart() -> NoReturn:
        """Restarts a measurement process in the model"""
        ManagerModel.stop()
        QThreadPool.globalInstance().start(StartButtonView.__button.Start())
        StartButtonView.__button.__is_started = True
        StartButtonView.__button.__update_text()
        StartButtonView.__button.clearFocus()
