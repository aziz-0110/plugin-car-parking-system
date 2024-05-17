from src.plugin_interface import PluginInterface
from src.models.model_apps import Model, ModelApps
from src.controllers.control_anypoint import AnypointConfig
from .ui_main import Ui_Form
from PyQt6 import QtWidgets
import cv2


class Controller(QtWidgets.QWidget):
    def __init__(self, model: Model):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = model
        self.moildev = None
        self.model_apps = ModelApps()
        self.anypoint_config = AnypointConfig(self.ui)
        self.model_apps.update_file_config()
        self.set_stylesheet()

    def set_stylesheet(self):
        # cek modul yg digunakan
        [label.setStyleSheet(self.model.style_label()) for label in self.findChildren(QtWidgets.QLabel)]
        [button.setStyleSheet(self.model.style_pushbutton()) for button in self.findChildren(QtWidgets.QPushButton)]
  
 
    def close(self):
        self.ui.label.setText(" ")
        self.model_apps.__image_result = None
        self.model_apps.image = None
        self.model_apps.image_result = None
        self.model_apps.image_resize = None
        self.model_apps.reset_config()
        self.model_apps.cap = None

class Percobaan(PluginInterface):
    def __init__(self):
        super().__init__()
        self.widget = None
        self.description = "This is a plugins application"

    def set_plugin_widget(self, model):
        self.widget = Controller(model)
        return self.widget

    def set_icon_apps(self):
        return "icon.jpeg"

    def change_stylesheet(self):
        self.widget.set_stylesheet()

