import bpy

sel = bpy.context.selected_objects

for obj in sel:
    for slots in obj.material_slots:
        nt = slots.material.node_tree
        bsdf = False
        for n in slots.material.node_tree.nodes:
            if n.type == 'BSDF_PRINCIPLED':
                bsdf = True
        if bsdf:
            continue
        nn = nt.nodes.new('ShaderNodeBsdfPrincipled')
        for l in nt.links:
            # Link diffuse, multi, and normals as before
            if l.to_node.type == "GROUP" and l.to_socket.name == "texture_diffuse":
                nt.links.new(nn.inputs[0], l.from_socket)
            if l.to_node.type == "OUTPUT_MATERIAL":
                nt.links.new(l.to_socket, nn.outputs[0])

        # Add your specified node tree adjustments
        nt.nodes["Principled BSDF"].inputs[7].default_value = 1  # Transmission
        nt.nodes["Principled BSDF"].inputs[9].default_value = 1  # Alpha
        nt.nodes["Principled BSDF"].inputs[0].default_value = (1, 1, 1, 1)  # Base color

        # Remove GROUP nodes as before
        for n in slots.material.node_tree.nodes:
            if n.type == 'GROUP':
                nt.nodes.remove(n)
