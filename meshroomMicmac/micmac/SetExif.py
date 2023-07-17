__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class SetExif(node.MicmacNode):
    commandLine = 'mm3d SetExif {imagePatternValue} {allParams}'
    documentation = '''SetExif'''

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group="micmac",
            uid=[0],
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            group='unnamedParams',
            value="",
            uid=[0],
        ),
        desc.FloatParam(
            name='F',
            label='F',
            description='Focal lenght.',
            value=50.0,
            range=(0.0, 800.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='F35',
            label='F35',
            description='Focal lenght equiv 35mm.',
            value=50.0,
            range=(0.0, 800.0, 0.1),
            uid=[0],
        ),
        desc.StringParam(
            name='Cam',
            label='Cam',
            description='Camera model.',
            value='',
            uid=[0],
        ),
        desc.StringParam(
            name='Tps',
            label='Tps',
            description='Image timestamp.',
            value='',
            uid=[0],
        ),
        desc.BoolParam(
            name='Purge',
            label='Purge',
            description='Purge created exiv2 command file.', 
            value=True,
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
