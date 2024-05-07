import sys
from PyQt5 import QtWidgets, uic
from presets.lighting_presets import presets
from light_manager import create_or_use_light
from ui_utilities import update_fields, toggle_fields

class LightingSetupWindow(QtWidgets.QWidget):
    def __init__(self):
        super(LightingSetupWindow, self).__init__()
        uic.loadUi('data/3_point_lighting_tool.ui', self)
        self.setupUI()

    def setupUI(self):
        preset_keys = sorted(presets.keys()) + ["Custom"]
        for preset in preset_keys:
            self.presetComboBox.addItem(preset)
        self.okButton.clicked.connect(self.createLights)
        self.presetComboBox.currentIndexChanged.connect(self.onPresetChange)
        toggle_fields(self, False)

    def onPresetChange(self):
        preset_name = self.presetComboBox.currentText()
        if preset_name == "Custom":
            toggle_fields(self, True)
        else:
            update_fields(self, presets[preset_name])
            toggle_fields(self, False)

    def createLights(self):
        for light_type in ['Pri', 'Sec', 'Tert']:
            name = getattr(self, f'{light_type}_Name').text()
            x = float(getattr(self, f'{light_type}_X').text())
            y = float(getattr(self, f'{light_type}_Y').text())
            z = float(getattr(self, f'{light_type}_Z').text())
            intensity = float(getattr(self, f'{light_type}_Intensity').text())
            r = float(getattr(self, f'{light_type}_R').text())
            g = float(getattr(self, f'{light_type}_G').text())
            b = float(getattr(self, f'{light_type}_B').text())
            create_or_use_light('directionalLight', name, (x, y, z), intensity, (r, g, b))

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = LightingSetupWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
