import bpy

# Define a list of old suffixes and corresponding new names
suffix_mapping = [
    ('_Head', 'LINKLIKE_Head'),
    ('_Hips', 'LINKLIKE_Hips'),
    ('_LArm', 'LINKLIKE_LArm'),
    ('_LArmBendHalf', 'LINKLIKE_LArmBendHalf'),
    ('_LArmRoll', 'LINKLIKE_LArmRoll'),
    ('_LArmRollHalf', 'LINKLIKE_LArmRollHalf'),
    ('_LFoot', 'LINKLIKE_LFoot'),
    ('_LForeArm', 'LINKLIKE_LForeArm'),
    ('_LForeArmBendHalf', 'LINKLIKE_LForeArmBendHalf'),
    ('_LHand', 'LINKLIKE_LHand'),
    ('_LHandBendHalf', 'LINKLIKE_LHandBendHalf'),
    ('_LHandElbowSub1', 'LINKLIKE_LHandElbowSub1'),
    ('_LHandElbowSub2', 'LINKLIKE_LHandElbowSub2'),
    ('_LHandIndex_01', 'LINKLIKE_LHandIndex_01'),
    ('_LHandIndex_02', 'LINKLIKE_LHandIndex_02'),
    ('_LHandIndex_03', 'LINKLIKE_LHandIndex_03'),
    ('_LHandMiddle_01', 'LINKLIKE_LHandMiddle_01'),
    ('_LHandMiddle_02', 'LINKLIKE_LHandMiddle_02'),
    ('_LHandMiddle_03', 'LINKLIKE_LHandMiddle_03'),
    ('_LHandPinky_01', 'LINKLIKE_LHandPinky_01'),
    ('_LHandPinky_02', 'LINKLIKE_LHandPinky_02'),
    ('_LHandPinky_03', 'LINKLIKE_LHandPinky_03'),
    ('_LHandRing_01', 'LINKLIKE_LHandRing_01'),
    ('_LHandRing_02', 'LINKLIKE_LHandRing_02'),
    ('_LHandRing_03', 'LINKLIKE_LHandRing_03'),
    ('_LHandRoll', 'LINKLIKE_LHandRoll'),
    ('_LHandRollHalf', 'LINKLIKE_LHandRollHalf'),
    ('_LHandRollHalf2', 'LINKLIKE_LHandRollHalf2'),
    ('_LHandThumb_01', 'LINKLIKE_LHandThumb_01'),
    ('_LHandThumb_02', 'LINKLIKE_LHandThumb_02'),
    ('_LHandThumb_03', 'LINKLIKE_LHandThumb_03'),
    ('_LKneeSub', 'LINKLIKE_LKneeSub'),
    ('_LLegBendHalf', 'LINKLIKE_LLegBendHalf'),
    ('_LLegSlide', 'LINKLIKE_LLegSlide'),
    ('_LShoulder', 'LINKLIKE_LShoulder'),
    ('_LToeBase', 'LINKLIKE_LToeBase'),
    ('_LUpLeg', 'LINKLIKE_LUpLeg'),
    ('_LUpLegBendHalf', 'LINKLIKE_LUpLegBendHalf'),
    ('_LUpLegRoll', 'LINKLIKE_LUpLegRoll'),
    ('_LUpLegRollHalf', 'LINKLIKE_LUpLegRollHalf'),
    ('_LUpLegSideSub', 'LINKLIKE_LUpLegSideSub'),
    ('_Neck', 'LINKLIKE_Neck'),
    ('_RArm', 'LINKLIKE_RArm'),
    ('_RArmBendHalf', 'LINKLIKE_RArmBendHalf'),
    ('_RArmRoll', 'LINKLIKE_RArmRoll'),
    ('_RArmRollHalf', 'LINKLIKE_RArmRollHalf'),
    ('_RFoot', 'LINKLIKE_RFoot'),
    ('_RForeArm', 'LINKLIKE_RForeArm'),
    ('_RForeArmBendHalf', 'LINKLIKE_RForeArmBendHalf'),
    ('_RHand', 'LINKLIKE_RHand'),
    ('_RHandBendHalf', 'LINKLIKE_RHandBendHalf'),
    ('_RHandElbowSub1', 'LINKLIKE_RHandElbowSub1'),
    ('_RHandElbowSub2', 'LINKLIKE_RHandElbowSub2'),
    ('_RHandIndex_01', 'LINKLIKE_RHandIndex_01'),
    ('_RHandIndex_02', 'LINKLIKE_RHandIndex_02'),
    ('_RHandIndex_03', 'LINKLIKE_RHandIndex_03'),
    ('_RHandMiddle_01', 'LINKLIKE_RHandMiddle_01'),
    ('_RHandMiddle_02', 'LINKLIKE_RHandMiddle_02'),
    ('_RHandMiddle_03', 'LINKLIKE_RHandMiddle_03'),
    ('_RHandPinky_01', 'LINKLIKE_RHandPinky_01'),
    ('_RHandPinky_02', 'LINKLIKE_RHandPinky_02'),
    ('_RHandPinky_03', 'LINKLIKE_RHandPinky_03'),
    ('_RHandRing_01', 'LINKLIKE_RHandRing_01'),
    ('_RHandRing_02', 'LINKLIKE_RHandRing_02'),
    ('_RHandRing_03', 'LINKLIKE_RHandRing_03'),
    ('_RHandRoll', 'LINKLIKE_RHandRoll'),
    ('_RHandRollHalf', 'LINKLIKE_RHandRollHalf'),
    ('_RHandRollHalf2', 'LINKLIKE_RHandRollHalf2'),
    ('_RHandThumb_01', 'LINKLIKE_RHandThumb_01'),
    ('_RHandThumb_02', 'LINKLIKE_RHandThumb_02'),
    ('_RHandThumb_03', 'LINKLIKE_RHandThumb_03'),
    ('_RKneeSub', 'LINKLIKE_RKneeSub'),
    ('_RLegBendHalf', 'LINKLIKE_RLegBendHalf'),
    ('_RLegSlide', 'LINKLIKE_RLegSlide'),
    ('_RShoulder', 'LINKLIKE_RShoulder'),
    ('_RToeBase', 'LINKLIKE_RToeBase'),
    ('_RUpLeg', 'LINKLIKE_RUpLeg'),
    ('_RUpLegBendHalf', 'LINKLIKE_RUpLegBendHalf'),
    ('_RUpLegRoll', 'LINKLIKE_RUpLegRoll'),
    ('_RUpLegRollHalf', 'LINKLIKE_RUpLegRollHalf'),
    ('_RUpLegSideSub', 'LINKLIKE_RUpLegSideSub'),
    ('_SP_LBreast', 'LINKLIKE_SP_LBreast'),
    ('_SP_RBreast', 'LINKLIKE_SP_RBreast'),
    ('_Spine_01', 'LINKLIKE_Spine_01'),
    ('_Spine_02', 'LINKLIKE_Spine_02'),
    ('_Spine_03', 'LINKLIKE_Spine_03'),
    # Add more suffixes and new names as needed
]

# Get the active object
obj = bpy.context.active_object

# Check if the object is in 'OBJECT' mode
if obj.mode == 'OBJECT':
    # Create a dictionary to store the mappings
    name_dict = {}

    # Iterate through the suffix mappings and create a dictionary
    for old_suffix, new_name in suffix_mapping:
        for vgroup in obj.vertex_groups:
            if vgroup.name.endswith(old_suffix):
                name_dict[vgroup.name] = new_name

    # Rename the vertex groups based on the dictionary
    for vgroup in obj.vertex_groups:
        if vgroup.name in name_dict:
            vgroup.name = name_dict[vgroup.name]
