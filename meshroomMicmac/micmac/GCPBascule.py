__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class GCPBascule(node.MicmacNode):
    commandLine = 'mm3d GCPBascule {imagePatternValue} {orientationInValue} {orientationOutValue} {groundControlPointsFileValue} {imageMeasurementsFileValue} {allParams}'
    documentation = 'GCPBascule'

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
            name='orientationIn',
            label='Orientation In',
            description="Orientation in",
            uid=[0],
            value="",
        ),
        desc.StringParam(
            name='orientationOut',
            label='Orientation Out',
            description="Orientation out",
            uid=[0],
            value="",
        ),
        desc.File(
            name='groundControlPointsFile',
            label='Ground Control Points File',
            description="Ground Control Points File",
            uid=[0],
            value="",
        ),
        desc.File(
            name='imageMeasurementsFile',
            label='Image Measurements File',
            description="Image Measurements File",
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='L1',
            label='L1',
            description="L1 minimisation vs L2",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='CPI',
            label='C P I',
            description="when Calib Per Image has to be used",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='ShowU',
            label='Show U',
            description="Show unused point",
            uid=[0],
            value=True,
        ),
        desc.BoolParam(
            name='ShowD',
            label='Show D',
            description="Show details",
            uid=[0],
            value=False,
        ),
        desc.StringParam(
            name='PatNLD',
            label='Pat N L D',
            description="Pattern for Non linear deformation, with aerial like geometry",
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='NLFR',
            label='N L F R',
            description="Non Linear : Force True Rot",
            uid=[0],
            value=True,
        ),
        desc.BoolParam(
            name='NLShow',
            label='N L Show',
            description="Non Linear : Show Details",
            uid=[0],
            value=False,
        ),
        desc.File(
            name='ForceSol',
            label='Force Sol',
            description="To Force Sol from existing solution (xml file)",
            uid=[0],
            value="",
        ),
    ]

    outputs = [
    ]
