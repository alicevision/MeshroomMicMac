__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class Tawny(node.MicmacNode):
    commandLine = 'mm3d Tawny {dataDirectoryValue} {allParams}'
    documentation = 'Tawny'

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
            name='dataDirectory',
            label='Data Directory',
            description="Data directory",
            group='unnamedParams',
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='RadiomEgal',
            label='Radiom Egal',
            description="Perform or not radiometric egalization",
            uid=[0],
            value=True,
        ),
        desc.IntParam(
            name='DEq',
            label='D Eq',
            description="Degree of equalization",
            uid=[0],
            value=1,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.GroupAttribute(
            name='DEqXY',
            label='D Eq X Y',
            description="Degree of equalization, if diff in X and Y",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.IntParam(
                name="x",
                label="X",
                description="x.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
            desc.IntParam(
                name="y",
                label="Y",
                description="y.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
        ]),
        desc.BoolParam(
            name='AddCste',
            label='Add Cste',
            description="Add unknown constant for equalization",
            uid=[0],
            value=False,
        ),
        desc.IntParam(
            name='DegRap',
            label='Deg Rap',
            description="Degree of rappel to initial values",
            uid=[0],
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.GroupAttribute(
            name='DegRapXY',
            label='Deg Rap X Y',
            description="Degree of rappel to initial values",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.IntParam(
                name="x",
                label="X",
                description="x.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
            desc.IntParam(
                name="y",
                label="Y",
                description="y.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
        ]),
        desc.BoolParam(
            name='RGP',
            label='R G P',
            description="Rappel glob on physically equalized",
            uid=[0],
            value=True,
        ),
        desc.FloatParam(
            name='DynG',
            label='Dyn G',
            description="Global Dynamic (to correct saturation problems)",
            uid=[0],
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.StringParam(
            name='ImPrio',
            label='Im Prio',
            description="Pattern of image with high prio",
            uid=[0],
            value=".*",
        ),
        desc.IntParam(
            name='SzV',
            label='Sz V',
            description="Sz of Window for equalization (1 means 3x3)",
            uid=[0],
            value=1,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.FloatParam(
            name='CorThr',
            label='Cor Thr',
            description="Threshold of correlation to validate homologous",
            uid=[0],
            value=0.7,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.FloatParam(
            name='NbPerIm',
            label='Nb Per Im',
            description="Average number of point per image",
            uid=[0],
            value=1e4,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='L1F',
            label='L1 F',
            description="Do L1 Filter on couple",
            uid=[0],
            value=True,
        ),
        desc.FloatParam(
            name='SatThresh',
            label='Sat Thresh',
            description="Threshold determining saturation value (pixel >SatThresh will be ignored)",
            uid=[0],
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Out',
            description="Name of output file (in the folder)",
            uid=[0],
            value="Tawny",
        ),
    ]
