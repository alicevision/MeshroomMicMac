__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class SaisieMasqQT(node.MicmacNode):
    commandLine = 'mm3d SaisieMasqQT {filePathValue} {allParams}'
    documentation = '''SaisieMasqQT'''

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group='', # required to execute mm3d command line
            uid=[0],
        ),
        desc.File(
            name='filePath',
            label='File Path',
            description='''Path of the file to open (image or PLY or camera XML).''',
            group='', # unnamed parameter
            value="",
            uid=[0],
        ),
        desc.GroupAttribute(
            name='SzW',
            label='Window Size',
            description='''Window Size in pixels.''',
            joinChar=",",
            groupDesc=[
                desc.IntParam(name="x", label="x", description="", value=900, uid=[0], range=(100, 1920, 1)),
                desc.IntParam(name="y", label="y", description="", value=700, uid=[0], range=(100, 1080, 1)),
            ]
        ),
        desc.StringParam(
            name='Post',
            label='File Postfix',
            description='''Output file postfix.''',
            value="_Masq",
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output',
            description='Output folder',
            group='',
            value=desc.Node.internalFolder,
            uid=[],
        ),
    ]
