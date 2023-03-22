```Python
>>> D.objects.items()
[('Camera', bpy.data.objects['Camera']), ('Gridtastic', bpy.data.objects['Gridtastic']), ('Gridtastic.001', bpy.data.objects['Gridtastic.001']), ('Gridtastic.002', bpy.data.objects['Gridtastic.002']), ('Light', bpy.data.objects['Light']), ('Plane', bpy.data.objects['Plane'])]

>>> D.objects['Plane'].mod
                          e
                          ifiers
>>> D.objects['Plane'].modifiers
bpy.data.objects['Plane'].modifiers

>>> types = [m.type for m in D.objects['Plane'].modifiers]
>>> types
['NODES']


>>> bpy.data.node_groups['total view.001'].nodes['Transform'].inputs['Scale'].
>>> 
```
