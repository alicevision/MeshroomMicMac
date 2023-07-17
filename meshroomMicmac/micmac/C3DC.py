__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class C3DC(node.MicmacNode):
    commandLine = 'mm3d C3DC {modeValue} {imagePatternValue} {orientationDirValue} {allParams}'
    documentation = '''C3DC'''

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
            value="",
            group='unnamedParams',
            uid=[0],
        ),    
        desc.File(
            name='SH',
            label='Homol Directory',
            description="Homol Directory.",
            uid=[0],
            value="",
        ),
        desc.File(
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            group='unnamedParams',
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name="mode",
            label="Mode",
            description="Mode.",
            group='unnamedParams',
            value="MicMac",
            values=["Ground", "Statue", "Forest", "TestIGN", "QuickMac", "MicMac", "BigMac", "MTDTmp"],
            exclusive=True,
            uid=[0],
        ),
        desc.StringParam(
            name='Masq3D',
            label='Masq 3D',
            description='3D masq for point selection.',
            value="",
            uid=[0],
        ),
        desc.IntParam(
            name='SzNorm',
            label='Sz Norm',
            description='Size of param for normal evaluation (<=0 if none, 2 means 5x5).',
            value=2,
            range=(-1, 20, 1),
            uid=[0],
        ),
        desc.BoolParam(
            name='PlyCoul',
            label='Ply Coul',
            description='Colour in ply.', 
            value=True,
            uid=[0],
        ),
        desc.BoolParam(
            name='Purge',
            label='Purge',
            description='Purge result.', 
            value=True,
            uid=[0],
        ),
        desc.BoolParam(
            name='UseGpu',
            label='Use Gpu',
            description='Use CUDA.', 
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Exp Txt',
            description='Use txt tie points for determining image pairs.', 
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description='PLY in binary mode.',  
            value=True,
            uid=[0],
        ),
        desc.BoolParam(
            name='NormByC',
            label='Norm By C',
            description='Replace normal with camera position in PLY.',
            value=False,
            uid=[0],
        ),
        desc.FloatParam(
            name='TetaOpt',
            label='Teta Opt',
            description='For the choice of secondary images: Optimal angle of stereoscopy, in radian.',
            value=0.17,
            range=(0.0, 7.0, 0.01),
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Point Cloud',
            description='Output PLY point cloud name.',
            value='C3DC.ply',
            uid=[0],
        ),
    ]
