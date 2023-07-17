__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class TapiocaMulScale(node.MicmacNode):
    commandLine = 'mm3d Tapioca MulScale {imagePatternValue} {imageSizeLowResolutionValue} {imageSizeHighResolutionValue} {allParams}'
    documentation = '''Tapioca MulScale'''

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
        desc.IntParam(
            name='imageSizeLowResolution',
            label='Image Size Low',
            description='Size of low resolution images.',
            group='unnamedParams',
            value=300,
            range=(-1, 10000, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='imageSizeHighResolution',
            label='Image Size High',
            description='Size of high resolution images.',
            group='unnamedParams',
            value=-1,
            range=(-1, 10000, 1),
            uid=[0],
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Export Files In Txt',
            description='Export files in text format (if false binary).', 
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='NoMax',
            label='No Max',
            description='No max.', 
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='NoMin',
            label='No Min',
            description='No min.', 
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='NoUnknown',
            label='No Unknown',
            description='No unknown.', 
            value=False,
            uid=[0],
        ),
        desc.FloatParam(
            name='Ratio',
            label='ANN Ratio',
            description='ANN closeness ration.',
            value=0.6,
            range=(0.1, 1.0, 0.1),
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='PostFix',
            label='Homol Directory', # Directory Postfix
            description='Homol Directory.',
            value="Tapioca",
            uid=[0],
        ),
    ]
