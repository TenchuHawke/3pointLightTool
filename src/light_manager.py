import pymel.core as pm

def create_or_use_light(light_type, name, position, intensity, color):
    if pm.objExists(name):
        light = pm.PyNode(name)
    else:
        light = pm.directionalLight(name=name)
        print(f'Created light: {name}')
    light.translate.set(position)
    light.intensity.set(intensity)
    light.color.set((color[0]/255.0, color[1]/255.0, color[2]/255.0))  # Normalize RGB to [0,1]
