import numpy as np
import struct
import visa
from pyslave.data import Lecroy_trace

# VISA resource manager
visa_rm = visa.ResourceManager()

# Wavesurfer : ws=LecroyScope('VICP::129.175.82.34::INSTR')
# Or : %openinstr VICP::192.168.0.2::INSTR

class LecroyScope:
    """Lecroy oscilloscope instrument driver.
    Direct call to the instrument invokes the fetch method."""
    endian = '<'
    def __init__(self, resource, *args, **kwargs):
        self.instrument = visa_rm.open_resource(resource, *args, **kwargs)
        self.lastvar = None
        self.__call__ = self.fetch

    def fetch(self, channel='C1'):
        """Fetch the waveform from the specified channel ('C1','C2,'TA', ...) and return it as a lecroy_trace data object."""
        ret = self.write('{0}:WF?'.format(channel))
        trc = self.read_raw()
        full_output = lecroy_decode(trc, self.endian)
        params_to_save = ['horiz_interval', 'horiz_offset', 'sweeps_per_acq','bandwidth_limit',
                          'vertical_gain', 'vertical_offset', 'vert_coupling', 'acq_vert_offset','probe_att','wave']
        return Lecroy_trace( dict( [ (k, full_output[k] ) for k in params_to_save ] ) )

    def write(self, str):
        """Write GPIB command."""
        self.instrument.write(str)

    def read_raw(self):
        return self.instrument.read_raw()

    def close(self):
        self.instrument.close()

class LT322(LecroyScope):
    """LT 322 Lecroy Oscilloscope instrument driver.
    Direct call to the instrument invokes the fetch method."""
    endian = '>'

def lecroy_decode(trc,endian='<'):
    """ Decode the string `trc` returned by a Lecroy scope or read from a Lecroy TRC file.
    Return a dictionary containing the data and the parameters included in the WAVEDESC descriptor.

    This Lecroy waveform interpreter is adapted from :
    LeCrunch
    Copyright (C) 2010 Anthony LaTorre"""

    # Parse the WAVEDESC block
    startpos = trc.find('WAVEDESC')
    param = dict(endian = endian)
    for name, pos, datatype in wavedesc:
        pos += startpos
        raw = trc[pos : pos + datatype.length]
        if datatype in (String, UnitDefinition):
            param[name] = raw.rstrip('\x00')
        elif datatype in (TimeStamp,):
            param[name] = struct.unpack( param['endian'] + datatype.packfmt, raw)
        else:
            param[name] = struct.unpack( param['endian'] + datatype.packfmt, raw)[0]

    # Read binary data block
    datatype = Word if param['comm_type'] else Byte
    y = np.fromstring(trc[startpos + param['wave_descriptor'] + param['user_text'] : ],
                      dtype = param['endian'] + datatype.packfmt,
                      count = param['wave_array_count'] )
    param['wave'] = y
    return param


# data types in lecroy binary blocks, where:
# length  -- byte length of type
# packfmt -- format string for struct.unpack()
class String:
    length = 16
class Byte:
    length = 1
    packfmt = 'b'
class Word:
    length = 2
    packfmt = 'h'
class Long:
    length = 4
    packfmt = 'l'
class Enum:
    length = 2
    packfmt = 'h'
class Float:
    length = 4
    packfmt = 'f'
class Double:
    length = 8
    packfmt = 'd'
class TimeStamp:
    length = 16
    packfmt = 'dbbbbhh'
class UnitDefinition:
    length = 48

# template of wavedesc block, where each entry in tuple is:
# (variable name, byte position from beginning of block, datatype)
wavedesc = ( ('descriptor_name'    , 0   , String),
             ('template_name'      , 16  , String),
             ('comm_type'          , 32  , Enum),
             ('comm_order'         , 34  , Enum),
             ('wave_descriptor'    , 36  , Long),
             ('user_text'          , 40  , Long),
             ('res_desc1'          , 44  , Long),
             ('trigtime_array'     , 48  , Long),
             ('ris_time_array'     , 52  , Long),
             ('res_array1'         , 56  , Long),
             ('wave_array_1'       , 60  , Long),
             ('wave_array_2'       , 64  , Long),
             ('res_array_2'        , 68  , Long),
             ('res_array_3'        , 72  , Long),
             ('instrument_name'    , 76  , String),
             ('instrument_number'  , 92  , Long),
             ('trace_label'        , 96  , String),
             ('reserved1'          , 112 , Word),
             ('reserved2'          , 114 , Word),
             ('wave_array_count'   , 116 , Long),
             ('pnts_per_screen'    , 120 , Long),
             ('first_valid_pnt'    , 124 , Long),
             ('last_valid_pnt'     , 128 , Long),
             ('first_point'        , 132 , Long),
             ('sparsing_factor'    , 136 , Long),
             ('segment_index'      , 140 , Long),
             ('subarray_count'     , 144 , Long),
             ('sweeps_per_acq'     , 148 , Long),
             ('points_per_pair'    , 152 , Word),
             ('pair_offset'        , 154 , Word),
             ('vertical_gain'      , 156 , Float),
             ('vertical_offset'    , 160 , Float),
             ('max_value'          , 164 , Float),
             ('min_value'          , 168 , Float),
             ('nominal_bits'       , 172 , Word),
             ('nom_subarray_count' , 174 , Word),
             ('horiz_interval'     , 176 , Float),
             ('horiz_offset'       , 180 , Double),
             ('pixel_offset'       , 188 , Double),
             ('vertunit'           , 196 , UnitDefinition),
             ('horunit'            , 244 , UnitDefinition),
             ('horiz_uncertainty'  , 292 , Float),
             ('trigger_time'       , 296 , TimeStamp),
             ('acq_duration'       , 312 , Float),
             ('record_type'        , 316 , Enum),
             ('processing_done'    , 318 , Enum),
             ('reserved5'          , 320 , Word),
             ('ris_sweeps'         , 322 , Word),
             ('timebase'           , 324 , Enum),
             ('vert_coupling'      , 326 , Enum),
             ('probe_att'          , 328 , Float),
             ('fixed_vert_gain'    , 332 , Enum),
             ('bandwidth_limit'    , 334 , Enum),
             ('vertical_vernier'   , 336 , Float),
             ('acq_vert_offset'    , 340 , Float),
             ('wave_source'        , 344 , Enum) )
