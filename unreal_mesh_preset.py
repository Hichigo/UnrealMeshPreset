bl_info = {
	"name": "Add mesh for unreal engine 4",
	"author": "Nexus Studio",
	"version": (0, 1),
	"blender": (2, 78),
	"location": "View3D -> E key",
	"description": "Description",
	"warning": "",
	"wiki_url": "none",
	"category": "User",
}

import bpy
from bpy.types import Operator

def uv_create():
	bpy.ops.mesh.uv_texture_add()
	bpy.context.scene.objects.active.data.uv_layers[0].name = 'UV_Main'
	bpy.ops.mesh.uv_texture_add()
	bpy.context.scene.objects.active.data.uv_layers[1].name = 'UV_Lightpack'

class add_unreal_plane(bpy.types.Operator):
	"""create plane mesh"""
	bl_idname = "mesh.add_unreal_plane"
	bl_label = "UnrealPlane"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.mesh.primitive_plane_add()
		bpy.context.scene.objects.active.name = "SM_Mesh"
		uv_create()
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		return bpy.context.mode == 'OBJECT'


class add_unreal_cube(bpy.types.Operator):
	"""create cube mesh"""
	bl_idname = "mesh.add_unreal_cube"
	bl_label = "UnrealCube"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.mesh.primitive_cube_add()
		bpy.context.scene.objects.active.name = "SM_Mesh"
		uv_create()
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		return bpy.context.mode == 'OBJECT'

class add_unreal_circle(bpy.types.Operator):
	"""create circle mesh"""
	bl_idname = "mesh.add_unreal_cube"
	bl_label = "UnrealCircle"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.mesh.primitive_circle_add()
		bpy.context.scene.objects.active.name = "SM_Mesh"
		uv_create()
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		return bpy.context.mode == 'OBJECT'


class add_unreal_uv_sphere(bpy.types.Operator):
	"""create uv sphere mesh"""
	bl_idname = "mesh.add_unreal_uv_sphere"
	bl_label = "UnrealUVSphere"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.mesh.primitive_uv_sphere_add()
		bpy.context.scene.objects.active.name = "SM_Mesh"
		uv_create()
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		return bpy.context.mode == 'OBJECT'



class UnrealMeshMenu(bpy.types.Menu):
	bl_label = "Add unreal mesh"

	def draw(self, context):
		layout = self.layout

		layout.operator("mesh.add_unreal_plane", text="Plane", icon='MESH_PLANE')
		layout.operator("mesh.add_unreal_cube", text="Cube", icon='MESH_CUBE')
		layout.operator("mesh.add_unreal_circle", text="Circle", icon='MESH_CIRCLE')
		layout.operator("mesh.add_unreal_uv_sphere", text="UV Sphere", icon='MESH_UVSPHERE')
		layout.operator("mesh.add_unreal_ico_sphere", text="Ico Sphere", icon='MESH_ICOSPHERE')
		layout.operator("mesh.add_unreal_cylinder", text="Cylinder", icon='MESH_CYLINDER')
		layout.operator("mesh.add_unreal_cone", text="Cone", icon='MESH_CONE')
		layout.operator("mesh.add_unreal_torus", text="Torus", icon='MESH_TORUS')
		layout.operator("mesh.add_unreal_grid", text="Grid", icon='MESH_GRID')
		layout.operator("mesh.add_unreal_monkey", text="Monkey", icon='MESH_MONKEY')

addon_keymaps = []
keymapsList = [
	{
		'name_view': "3D View",
		'space_type': "VIEW_3D",
		'prop_name': "UnrealMeshMenu"
	}
]

def register():
	bpy.utils.register_module(__name__)

	kc = bpy.context.window_manager.keyconfigs.addon
	if kc:
		for keym in keymapsList:
			km = kc.keymaps.new(name=keym['name_view'], space_type=keym['space_type'])
			kmi = km.keymap_items.new('wm.call_menu', 'E', 'PRESS')
			kmi.properties.name = keym['prop_name']
			addon_keymaps.append(km)

def unregister():
	bpy.utils.unregister_module(__name__)

	wm = bpy.context.window_manager
	if wm.keyconfigs.addon:
		for km in addon_keymaps:
			for kmi in km.keymap_items:
				km.keymap_items.remove(kmi)
	addon_keymaps.clear()

if __name__ == "__main__":
	register()
