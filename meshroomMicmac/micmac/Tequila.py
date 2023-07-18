__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class Tequila(node.MicmacNode):
    commandLine = 'mm3d Tequila {imagePatternValue} {orientationDirValue} {plyNameValue} {allParams}'
    documentation = '''Tequila'''

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
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            group='', # unnamed parameter
            value="",
            uid=[0],
        ),
        desc.StringParam(
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            group='', # unnamed parameter
            value='',
            uid=[0],
        ),
        desc.StringParam(
            name='plyName',
            label='PLY Name',
            description='Ply filename.',
            group='', # unnamed parameter
            value='',
            uid=[0],
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description='Write PLY in binary mode.', 
            value=True,
            uid=[0],
        ),
        desc.BoolParam(
            name='Optim',
            label='Optim',
            description='Graph-cut optimization.', 
            value=False,
            uid=[0],
        ),
        desc.FloatParam(
            name='Lambda',
            label='Lambda',
            description='Lambda.',
            value=0.01,
            range=(0.0, 10.0, 0.01),
            uid=[0],
        ),
        desc.IntParam(
            name='Iter',
            label='Iter',
            description='Optimization iteration number.',
            value=2,
            range=(0, 20, 1),
            uid=[0],
        ),
        desc.BoolParam(
            name='Filter',
            label='Filter',
            description='Remove border faces.', 
            value=False,
            uid=[0],
        ),
        desc.IntParam(
            name='Sz',
            label='Sz',
            description='Texture max size.',
            value=8192,
            range=(100, 16000, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='Scale',
            label='Scale',
            description='Z-buffer downscale factor.',
            value=2,
            range=(0, 10, 1),
            uid=[0],
        ),
        desc.BoolParam(
            name='ZBufCache',
            label='ZBuf Cache',
            description='ZBuffer cache (if True: a little faster, more memory).',
            value=False,
            uid=[0],
        ),
        desc.IntParam(
            name='QUAL',
            label='Qual',
            description='jpeg compression quality.',
            value=70,
            range=(10, 100, 1),
            uid=[0],
        ),
        desc.FloatParam(
            name='Angle',
            label='Angle',
            description='Threshold angle, in degree, between triangle normal and image viewing direction',
            value=90.0,
            range=(0.0, 360.0, 0.01),
            uid=[0],
        ),
        desc.StringParam(
            name='Mode',
            label='Mode',
            description='Mode.',
            value='Pack',
            uid=[0],
        ),
        desc.StringParam(
            name='Crit',
            label='Crit',
            description='Texture choosing criterion.',
            value='Angle',
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Point Cloud',
            description='Output PLY point cloud name.',
            value='Tequila.ply',
            uid=[],
        ),
    ]
