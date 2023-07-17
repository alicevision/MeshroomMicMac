__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class AperiCloud(node.MicmacNode):
    commandLine = 'mm3d AperiCloud {imagePatternValue} {orientationDirValue} {allParams}'
    documentation = '''AperiCloud'''

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
            value="",
            uid=[0],
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Exp Txt',
            description='Tie Point use txt format', 
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
            name='RGB',
            label='RGB',
            description='Use RGB image to color points.', 
            value=True,
            uid=[0],
        ),
        desc.FloatParam(
            name='SeuilEc',
            label='Seuil Ec',
            description='Max residual.',
            value=10.0,
            range=(0.0, 100.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='LimBsH',
            label='Lim BsH',
            description='Limit ratio base to height.',
            value=1e-2,
            range=(0.0, 100.0, 0.1),
            uid=[0],
        ),
        desc.BoolParam(
            name='WithPoints',
            label='With Points',
            description='Add point cloud.', 
            value=True,
            uid=[0],
        ),
        desc.BoolParam(
            name='CalPerIm',
            label='Cal Per Im',
            description='Calibration per image was used.', 
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='WithCam',
            label='With Cam',
            description='Camera representation.', 
            value=True,
            uid=[0],
        ),
        desc.FloatParam(
            name='StepIm',
            label='Step Im',
            description='if image in camera are wanted, indicate reduction factor.',
            value=-1.0,
            range=(-1.0, 100.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='ProfCam',
            label='Prof Cam',
            description='Size of focal exageration factor for pyramid representing camera.',
            value=0.3,
            range=(0.0, 100.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='RabDrBundle',
            label='Rab Dr Bundle',
            description='Lenght to add in budle drawing.',
            value=0.0,
            range=(0.0, 100.0, 0.1),
            uid=[0],
        ),
        desc.BoolParam(
            name='SavePtsCol',
            label='Save Pts Col',
            description='Don t store point color element in PLY file to save disk space.', 
            value=True,
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Point Cloud',
            description='Output PLY point cloud name.',
            value='AperiCloud.ply',
            uid=[0],
        ),
    ]
