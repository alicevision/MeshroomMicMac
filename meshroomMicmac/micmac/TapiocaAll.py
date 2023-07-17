__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class TapiocaAll(node.MicmacNode):
    commandLine = 'mm3d Tapioca All {imagePatternValue} {imageSizeValue} {allParams}'
    documentation = '''Tapioca All'''

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
            value='.*.(jpg|jpeg|JPG|png|PNG|tif|tiff|TIF|TIFF|arw|ARW|crw|CRW|nef|NEF)',
            group='unnamedParams',
            uid=[0],
        ),    
        desc.IntParam(
            name='imageSize',
            label='Image Size',
            description='Size of image.',
            group='unnamedParams',
            value=-1,
            range=(-1, 16000, 10),
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