from typing import Dict
from xml.dom import minidom

from PyQt5.QtCore import QLocale, pyqtSignal, QObject


class Translator:
    """Static class for getting translations and changing languages

        Attributes:
            language_changed (Signal): Emits updates when the language is changed.
    """

    class Signal(QObject):
        signal = pyqtSignal()

    __translator: Dict[str, str] = None
    language_changed: Signal = Signal()

    @staticmethod
    def install_translator(language: int) -> bool:
        """Installs a translator with the given language

            Args:
                language (int): A Qt language from QLocale. (e.g.: QLocale.English)

            Returns:
                bool: If the installation was successful.
                    Mostly depends on if the given language has a language file in /resources/languages/.
        """
        if language == QLocale.German:
            Translator.__translator = None
        else:
            try:
                items = minidom.parse('../resources/languages/' + QLocale(language).name() + '.xml').getElementsByTagName('item')
            except FileNotFoundError:
                return False

            Translator.__translator = {}
            for item in items:
                Translator.__translator[item.childNodes[1].firstChild.data] = item.childNodes[3].firstChild.data

        Translator.language_changed.signal.emit()
        return True

    @staticmethod
    def tr(original: str) -> str:
        """Translates the given string

            Args:
                original (str): The original string, which will be translated.

            Returns:
                str: Returns the translated sting. If no translator is installed or the current language does not have a
                    translation for the original, returns the original string.
        """
        if Translator.__translator is None:
            return original

        translated = Translator.__translator.get(original)
        if translated is None:
            print("No existing translation for " + original)
            return original

        return translated
