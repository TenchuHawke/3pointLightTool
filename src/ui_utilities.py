def update_fields(ui, preset_data):
    for light_type, data in preset_data.items():
        getattr(ui, f'{light_type}_Name').setText(light_type)
        getattr(ui, f'{light_type}_X').setText(str(data[0][0]))
        getattr(ui, f'{light_type}_Y').setText(str(data[0][1]))
        getattr(ui, f'{light_type}_Z').setText(str(data[0][2]))
        getattr(ui, f'{light_type}_Intensity').setText(str(data[1]))
        getattr(ui, f'{light_type}_R').setText(str(data[2][0]))
        getattr(ui, f'{light_type}_G').setText(str(data[2][1]))
        getattr(ui, f'{light_type}_B').setText(str(data[2][2]))

def toggle_fields(ui, enable):
    for light_type in ['Pri', 'Sec', 'Tert']:
        getattr(ui, f'{light_type}_Name').setEnabled(enable)
        getattr(ui, f'{light_type}_X').setEnabled(enable)
        getattr(ui, f'{light_type}_Y').setEnabled(enable)
        getattr(ui, f'{light_type}_Z').setEnabled(enable)
        getattr(ui, f'{light_type}_Intensity').setEnabled(enable)
        getattr(ui, f'{light_type}_R').setEnabled(enable)
        getattr(ui, f'{light_type}_G').setEnabled(enable)
        getattr(ui, f'{light_type}_B').setEnabled(enable)
