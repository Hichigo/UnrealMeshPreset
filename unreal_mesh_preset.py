bl_info = {
	"name": "Unreal Mesh Preset",
	"author": "Nexus Studio",
	"version": (0, 2),
	"blender": (2, 78),
	"location": "View3D -> shift+A -> Mesh",
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
	bl_idname = "mesh.add_unreal_circle"
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

class add_unreal_ico_sphere(bpy.types.Operator):
	"""create ico sphere mesh"""
	bl_idname = "mesh.add_unreal_ico_sphere"
	bl_label = "UnrealIcoSphere"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.mesh.primitive_ico_sphere_add()
		bpy.context.scene.objects.active.name = "SM_Mesh"
		uv_create()
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		return bpy.context.mode == 'OBJECT'

class add_unreal_cylinder(bpy.types.Operator):
	"""create cylinder mesh"""
	bl_idname = "mesh.add_unreal_cylinder"
	bl_label = "UnrealCylinder"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.mesh.primitive_cylinder_add()
		bpy.context.scene.objects.active.name = "SM_Mesh"
		uv_create()
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		return bpy.context.mode == 'OBJECT'

class add_unreal_cone(bpy.types.Operator):
	"""create cone mesh"""
	bl_idname = "mesh.add_unreal_cone"
	bl_label = "UnrealCone"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.mesh.primitive_cone_add()
		bpy.context.scene.objects.active.name = "SM_Mesh"
		uv_create()
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		return bpy.context.mode == 'OBJECT'

class add_unreal_torus(bpy.types.Operator):
	"""create torus mesh"""
	bl_idname = "mesh.add_unreal_torus"
	bl_label = "UnrealTorus"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.mesh.primitive_torus_add()
		bpy.context.scene.objects.active.name = "SM_Mesh"
		uv_create()
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		return bpy.context.mode == 'OBJECT'

class add_unreal_grid(bpy.types.Operator):
	"""create grid mesh"""
	bl_idname = "mesh.add_unreal_grid"
	bl_label = "UnrealGrid"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.mesh.primitive_grid_add()
		bpy.context.scene.objects.active.name = "SM_Mesh"
		uv_create()
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		return bpy.context.mode == 'OBJECT'

class add_unreal_monkey(bpy.types.Operator):
	"""create monkey mesh"""
	bl_idname = "mesh.add_unreal_monkey"
	bl_label = "UnrealMonkey"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.ops.mesh.primitive_monkey_add()
		bpy.context.scene.objects.active.name = "SM_Mesh"
		uv_create()
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		return bpy.context.mode == 'OBJECT'

class UnrealMeshMenu(bpy.types.Menu):
	bl_idname = "UnrealMeshMenu"
	bl_label = "Unreal mesh"

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
		layout.separator()
		layout.operator("mesh.add_unreal_grid", text="Grid", icon='MESH_GRID')
		layout.operator("mesh.add_unreal_monkey", text="Monkey", icon='MESH_MONKEY')

def submenu(self, context):
	self.layout.menu("UnrealMeshMenu", icon='OUTLINER_OB_MESH')

# addon_keymaps = []
# keymapsList = [
# 	{
# 		'name_view': "3D View",
# 		'space_type': "VIEW_3D",
# 		'prop_name': "custom_primitive"
# 	}
# ]

def register():
	# bpy.utils.register_class(UnrealMeshSubmenu)
	bpy.utils.register_module(__name__)

	bpy.types.INFO_MT_add.prepend(submenu)

	# kc = bpy.context.window_manager.keyconfigs.addon
	# if kc:
	# 	for keym in keymapsList:
	# 		km = kc.keymaps.new(name=keym['name_view'], space_type=keym['space_type'])
	# 		kmi = km.keymap_items.new('wm.call_menu', 'E', 'PRESS')
	# 		kmi.properties.name = keym['prop_name']
	# 		addon_keymaps.append(km)

def unregister():
	# bpy.utils.unregister_class(UnrealMeshSubmenu)
	bpy.utils.unregister_module(__name__)

	bpy.types.INFO_MT_add.remove(submenu)


	# wm = bpy.context.window_manager
	# if wm.keyconfigs.addon:
	# 	for km in addon_keymaps:
	# 		for kmi in km.keymap_items:
	# 			km.keymap_items.remove(kmi)
	# addon_keymaps.clear()

if __name__ == "__main__":
	register()
