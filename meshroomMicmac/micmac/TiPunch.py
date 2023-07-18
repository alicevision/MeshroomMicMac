__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class TiPunch(node.MicmacNode):
    commandLine = 'mm3d TiPunch {plyNameValue} {allParams}'
    documentation = '''TiPunch'''

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
            name='Pattern',
            label='Image Pattern',
            description='Image Pattern.',
            value="",
            uid=[0],
        ),
        desc.File(
            name='plyName',
            label='Point Cloud',
            description='Point cloud PLY filename.',
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
        desc.IntParam(
            name='Depth',
            label='Depth',
            description='Maximum reconstruction depth for PoissonRecon.',
            value=8,
            range=(0, 20, 1),
            uid=[0],
        ),
        desc.BoolParam(
            name='Rm',
            label='Rm',
            description='Remove intermediary Poisson mesh.', 
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='Filter',
            label='Filter',
            description='Filter mesh.', 
            value=True,
            uid=[0],
        ),
        desc.StringParam(
            name='Mode',
            label='Mode',
            description='C3DC mode.',
            value='Statue',
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
            name='FFB',
            label='FFB',
            description='Filter from border.', 
            value=True,
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Point Cloud',
            description='Output PLY point cloud name.',
            value='TiPunch.ply',
            uid=[],
        ),
    ]
