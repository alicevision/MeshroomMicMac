__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class TapiocaGeoref(node.MicmacNode):
    commandLine = 'mm3d Tapioca Georef {imagePatternValue} {orientationDirValue} {allParams}'
    documentation = '''Tapioca Georef'''

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
        desc.StringParam(
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            group='unnamedParams',
            value='',
            uid=[0],
        ),
        desc.GroupAttribute(
            name='Grid',
            label='Grid',
            description='Tie points grid.',
            joinChar=',',
            brackets='[]',
            groupDesc=[
                desc.IntParam(
                    name='x',
                    label='X',
                    description='Tie points grid (x).',
                    value=25,
                    range=(1, 100, 1),
                    uid=[0],
                ),
                desc.IntParam(
                    name='y',
                    label='Y',
                    description='Tie points grid (y).',
                    value=25,
                    range=(1, 100, 1),
                    uid=[0],
                ),
            ]
        ),
        desc.IntParam(
            name='Zoom0',
            label='Zoom 0',
            description='Zoom init, pow of 2.',
            value=16,
            range=(1, 1024, 1),
            uid=[0],
        ),
        desc.FloatParam(
            name='Cor',
            label='Cor',
            description='Corelation threshold.',
            value=0.6,
            range=(0.1, 10.0, 0.1),
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
