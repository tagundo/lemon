import bpy
# based on jhrino AuthEdit

# select empty & run script
# add constraint to camera
# set target to created empty
# change mix to After Original

# Define the camera shake parameters
divide_end = 2

camera_shake = [
    [1, 31, "ShakePitch", 1, 1],
    [273, 303, "ShakePitch", 0.5, 1],
    [289, 319, "ShakePitch", 0.5, 1],
    [433, 463, "ShakeRoll", 0.2, 1],
    [494, 524, "ShakePitch", 0.5, 1],
    [571, 601, "ShakeRoll", 0.5, 1],
    [993, 1023, "ShakePitch", 1, 1]
    [1117, 1147, "ShakePitch", 1, 1],
    [1161, 1191, "ShakePitch", 1, 1],
]

# Function to clear existing noise modifiers
def clear_noise_modifiers(obj):
    if obj.animation_data and obj.animation_data.action:
        for fcurve in obj.animation_data.action.fcurves:
            for mod in fcurve.modifiers:
                if mod.type == 'NOISE':
                    fcurve.modifiers.remove(mod)

# Function to add noise modifier
def add_noise_modifier(fcurve, scale, strength, start_frame, end_frame):
    noise_mod = fcurve.modifiers.new(type='NOISE')
    noise_mod.scale = scale
    noise_mod.strength = strength
    noise_mod.use_restricted_range = True
    noise_mod.frame_start = start_frame
    noise_mod.frame_end = int(end_frame / divide_end)

# Get the selected empty object
empty = bpy.context.object

# Ensure the empty has animation data
if empty and empty.type == 'EMPTY':
    if not empty.animation_data:
        empty.animation_data_create()

    # Clear existing noise modifiers
    clear_noise_modifiers(empty)

    # Apply the camera shake
    for shake in camera_shake:
        start_frame, end_frame, shake_type, strength, scale = shake

        if shake_type == "ShakePitch":
            fcurve = empty.animation_data.action.fcurves.find('rotation_euler', index=0)  # Y Euler Rotation
            if fcurve is None:
                fcurve = empty.animation_data.action.fcurves.new(data_path="rotation_euler", index=0)
        elif shake_type == "ShakeRoll":
            fcurve = empty.animation_data.action.fcurves.find('rotation_euler', index=1)  # X Euler Rotation
            if fcurve is None:
                fcurve = empty.animation_data.action.fcurves.new(data_path="rotation_euler", index=1)

        add_noise_modifier(fcurve, scale, strength, start_frame, end_frame)

    print("Camera shake modifiers applied to the selected empty.")
else:
    print("Please select an empty object.")
