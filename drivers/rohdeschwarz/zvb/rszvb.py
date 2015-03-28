import numpy as numpy
from ctypes import *

# Prerequisition: installed rszvb driver 32-bit

# Reference to rszvb dll
rszvbDLL = windll.rszvb_32

class ZVBDLLERROR(Exception):
	pass
        
iStringBufferLen = 1024
sStringBuffer = create_string_buffer(iStringBufferLen)

def __errorcheck__(iCode, func, args):
    if iCode<0:
        iHandle = args[0]
        rszvbDLL.rszvb_error_message(iHandle, iCode, sStringBuffer)
        msg = " {} : {}".format(func.name, sStringBuffer.value)
        eqcode = c_int(0)
        rszvbDLL.rszvb_error_query (iHandle, byref(eqcode), sStringBuffer)
        if eqcode.value != 0:
            msg += " - ZVB Instrument Error : {}".format(sStringBuffer.value)
        raise ZVBDLLERROR(msg)
    else:
        return args



#DLL constants

RSZVB_EMF = 0
RSZVB_BMP = 1
RSZVB_JPG = 2
RSZVB_PNG = 3
RSZVB_HCOPY_ALL = 0
RSZVB_HCOPY_ACTIVE = 1
RSZVB_HCOPY_SINGLE = 2
RSZVB_PORTRAIT = 0
RSZVB_LANDSCAPE = 1
RSZVB_FILE_MAN_CDRIVE = 0
RSZVB_FILE_MAN_CDIR = 1
RSZVB_FILE_MAN_MDIR = 2
RSZVB_FILE_MAN_RDIR = 3
RSZVB_FILE_MAN_COPY = 4
RSZVB_FILE_MAN_MOVE = 5
RSZVB_FILE_MAN_DELETE = 6
RSZVB_FILE_MAN_CDIR_DEF = 7
RSZVB_SINGLE_ENDED = 0
RSZVB_DIFFERENTIAL = 1
RSZVB_COMMON = 2
RSZVB_RATIO_B2_A1_SRC_PORT_1 = 0
RSZVB_RATIO_B1_A1_SRC_PORT_1 = 1
RSZVB_RATIO_B2_B1_SRC_PORT_1 = 2
RSZVB_RATIO_B1_B2_SRC_PORT_1 = 3
RSZVB_PORT_1 = 1
RSZVB_PORT_2 = 2
RSZVB_PORT_3 = 3
RSZVB_PORT_4 = 4
RSZVB_PWRM_1 = 1
RSZVB_PWRM_2 = 2
RSZVB_A = 0
RSZVB_B = 1
RSZVB_WQUANTITY_A1_SRC_PORT_1 = 0
RSZVB_WQUANTITY_B1_SRC_PORT_1 = 1
RSZVB_WQUANTITY_B2_SRC_PORT_1 = 2
RSZVB_WQUANTITY_A2_SRC_PORT_2 = 3
RSZVB_WQUANTITY_B1_SRC_PORT_2 = 4
RSZVB_WQUANTITY_B2_SRC_PORT_2 = 5
RSZVB_DET_RMS = 0
RSZVB_DET_PEAK = 1
RSZVB_DET_AVG = 2
RSZVB_SFACTOR_K = 0
RSZVB_SFACTOR_U1 = 1
RSZVB_SFACTOR_U2 = 2
RSZVB_DC_MEAS_1V = 0
RSZVB_DC_MEAS_10V = 1
RSZVB_PAE_EXP_C10 = 0
RSZVB_PAE_EXP_C1 = 1
RSZVB_PAE_EXP_K101 = 2
RSZVB_PAE_EXP_CK11 = 3
RSZVB_DB_MAG = 0
RSZVB_PHASE = 1
RSZVB_SMITH = 2
RSZVB_POLAR = 3
RSZVB_DELAY = 4
RSZVB_SWR = 5
RSZVB_LIN_MAG = 6
RSZVB_REAL = 7
RSZVB_IMAG = 8
RSZVB_ISMITH = 9
RSZVB_UPHASE = 10
RSZVB_DB_MAG_PHASE = 11
RSZVB_LIN_MAG_PHASE = 12
RSZVB_REAL_IMAG = 13
RSZVB_DEFAULT = 14
RSZVB_R_JX = 15
RSZVB_G_JB = 16
RSZVB_SWEEP_LIN = 0
RSZVB_SWEEP_LOG = 1
RSZVB_SWEEP_SEG = 2
RSZVB_SWEEP_POW = 3
RSZVB_SWEEP_TIM = 4
RSZVB_SWEEP_CW = 5
RSZVB_SWEEP_PULSE = 6
RSZVB_SWEEP_IAMP = 7
RSZVB_SWEEP_IPH = 8
RSZVB_SEG_TIME = 0
RSZVB_SEG_POINT = 1
RSZVB_NEG = 0
RSZVB_POS = 1
RSZVB_TRGSEQ_SWE = 0
RSZVB_TRGSEQ_SEGM = 1
RSZVB_TRGSEQ_POIN = 2
RSZVB_TRGSEQ_PPO = 3
RSZVB_TRG_IMM = 0
RSZVB_TRG_EXT = 1
RSZVB_TRG_TIM = 2
RSZVB_TRG_MAN = 3
RSZVB_TRG_RFP = 4
RSZVB_TRG_PGE = 5
RSZVB_SWEEP_SINGLE_CHAN = 0
RSZVB_SWEEP_ALL_CHAN = 1
RSZVB_SWEEP_SINGLE = 0
RSZVB_SWEEP_CONT = 1
RSZVB_AVOID_AUTO = 0
RSZVB_AVOID_POS = 1
RSZVB_AVOID_NEG = 2
RSZVB_CONNECTOR_N50FEMALE = 0
RSZVB_CONNECTOR_N50MALE = 1
RSZVB_CONNECTOR_N75FEMALE = 2
RSZVB_CONNECTOR_N75MALE = 3
RSZVB_CONNECTOR_PC7 = 4
RSZVB_CONNECTOR_PC35FEMALE = 5
RSZVB_CONNECTOR_PC35MALE = 6
RSZVB_CONNECTOR_PC292FEMALE = 7
RSZVB_CONNECTOR_PC292MALE = 8
RSZVB_CONNECTOR_UFEMALE1 = 9
RSZVB_CONNECTOR_UMALE1 = 10
RSZVB_CONNECTOR_UFEMALE2 = 11
RSZVB_CONNECTOR_UMALE2 = 12
RSZVB_CONNECTOR_SMAFEMALE = 13
RSZVB_CONNECTOR_SMAMALE = 14
RSZVB_CONNECTOR_PC1FEMALE = 15
RSZVB_CONNECTOR_PC1MALE = 16
RSZVB_CONNECTOR_PC185FEMALE = 17
RSZVB_CONNECTOR_PC185MALE = 18
RSZVB_CONNECTOR_PC24FEMALE = 19
RSZVB_CONNECTOR_PC24MALE = 20
RSZVB_CONNECTOR_KIT_N50 = 0
RSZVB_CONNECTOR_KIT_N75 = 1
RSZVB_CONNECTOR_KIT_PC7 = 2
RSZVB_CONNECTOR_KIT_PC35 = 3
RSZVB_CONNECTOR_KIT_PC292 = 4
RSZVB_CONNECTOR_KIT_USER1 = 5
RSZVB_CONNECTOR_KIT_USER2 = 6
RSZVB_CONNECTOR_KIT_SMA = 7
RSZVB_CALTYPE_REFL = 0
RSZVB_CALTYPE_RSH = 1
RSZVB_CALTYPE_FOP = 2
RSZVB_CALTYPE_FRTR = 3
RSZVB_CALTYPE_OPTP = 4
RSZVB_CALTYPE_TOSM = 5
RSZVB_CALTYPE_TOM = 6
RSZVB_CALTYPE_TRM = 7
RSZVB_CALTYPE_TRL = 8
RSZVB_CALTYPE_TNA = 9
RSZVB_CALTYPE_FNP = 10
RSZVB_CALTYPE_SFTP = 11
RSZVB_CALTYPE_UOSM = 12
RSZVB_CALTYPE_FTR = 13
RSZVB_CALTYPE_RTR = 14
RSZVB_CALTYPE_NMTR = 16
RSZVB_CALCOLLSTD_THR = 0
RSZVB_CALCOLLSTD_OPEN1 = 1
RSZVB_CALCOLLSTD_OPEN2 = 2
RSZVB_CALCOLLSTD_OPEN12 = 3
RSZVB_CALCOLLSTD_SHORT1 = 4
RSZVB_CALCOLLSTD_SHORT2 = 5
RSZVB_CALCOLLSTD_SHORT12 = 6
RSZVB_CALCOLLSTD_MATCH1 = 7
RSZVB_CALCOLLSTD_MATCH2 = 8
RSZVB_CALCOLLSTD_MATCH12 = 9
RSZVB_CALCOLLSTD_NET = 10
RSZVB_CALCOLLSTD_ATT = 11
RSZVB_CALCOLLSTD_REFL1 = 12
RSZVB_CALCOLLSTD_REFL2 = 13
RSZVB_CALCOLLSTD_LINE1 = 14
RSZVB_CALCOLLSTD_LINE2 = 15
RSZVB_CALCOLLSTD_M1O2 = 16
RSZVB_CALCOLLSTD_O1M2 = 17
RSZVB_CALCOLLSTD_M1S2 = 18
RSZVB_CALCOLLSTD_S1M2 = 19
RSZVB_CALCOLLSTD_OSH1 = 20
RSZVB_CALCOLLSTD_OSH2 = 21
RSZVB_CALCOLLSTDGEN_THR = 0
RSZVB_CALCOLLSTDGEN_OPEN = 1
RSZVB_CALCOLLSTDGEN_SHORT = 2
RSZVB_CALCOLLSTDGEN_MATCH = 3
RSZVB_CALCOLLSTDGEN_NET = 4
RSZVB_CALCOLLSTDGEN_ATT = 5
RSZVB_CALCOLLSTDGEN_REFL = 6
RSZVB_CALCOLLSTDGEN_LINE = 7
RSZVB_CALCOLLSTDGEN_LINE_2 = 8
RSZVB_CALCOLLSTDGEN_OSH = 9
RSZVB_CALCOLLSTDGEN_LINE_3 = 10
RSZVB_CALCOLLSTDGEN_SLID = 11
RSZVB_CALCOLLSTDGEN_OSH_2 = 12
RSZVB_CALCOLLSTDGEN_OSH_3 = 13
RSZVB_CALCOLLSTDGEN_ISOL = 15
RSZVB_CALCOLLSTDGEN_UTHR = 0
RSZVB_CORR_MAN_COPY = 0
RSZVB_CORR_MAN_APPLY = 1
RSZVB_CORR_MAN_RESOLVE = 2
RSZVB_CORR_MAN_DELETE = 3
RSZVB_CORR_MAN_APPLY_ALL = 4
RSZVB_CORR_MAN_RESOLVE_ALL = 5
RSZVB_CORR_MAN_MERGE = 7
RSZVB_KIT_N50 = 0
RSZVB_KIT_N75 = 1
RSZVB_KIT_SMA = 2
RSZVB_KIT_PC7 = 3
RSZVB_KIT_PC35 = 4
RSZVB_KIT_USER1 = 5
RSZVB_KIT_USER2 = 6
RSZVB_KIT_PC292 = 7
RSZVB_OPEN = 0
RSZVB_SHORT = 1
RSZVB_MATCH = 2
RSZVB_RESTORE = 0
RSZVB_MAXIMIZE = 1
RSZVB_PRESET_SINGLE = 0
RSZVB_PRESET_ALL = 1
RSZVB_INT = 0
RSZVB_EXT = 1
RSZVB_FULL_SPAN = 0
RSZVB_RANGE_1 = 1
RSZVB_RANGE_2 = 2
RSZVB_RANGE_3 = 3
RSZVB_RANGE_4 = 4
RSZVB_RANGE_5 = 5
RSZVB_RANGE_6 = 6
RSZVB_RANGE_7 = 7
RSZVB_RANGE_8 = 8
RSZVB_RANGE_9 = 9
RSZVB_RANGE_10 = 10
RSZVB_ALL = 0
RSZVB_MEAN = 1
RSZVB_STDDEV = 2
RSZVB_MAX = 3
RSZVB_MIN = 4
RSZVB_RMS = 5
RSZVB_PTPEAK = 6
RSZVB_ELENGTH = 7
RSZVB_PDELAY = 8
RSZVB_SLOPE = 9
RSZVB_FLATNESS = 10
RSZVB_GAIN = 11
RSZVB_UNFORMATTED = 0
RSZVB_FORMATTED = 1
RSZVB_UNFORMATTED_MATH = 2
RSZVB_PULSE_PROFILE = 3
RSZVB_CONTINUOUS = 0
RSZVB_DISCRETE = 1
RSZVB_NORMAL = 0
RSZVB_FIXED = 1
RSZVB_MARKER_MAX = 0
RSZVB_MARKER_MIN = 1
RSZVB_MARKER_NEXT = 2
RSZVB_MARKER_RPEAK = 3
RSZVB_MARKER_LPEAK = 4
RSZVB_MARKER_TARGET = 0
RSZVB_MARKER_RTARGET = 1
RSZVB_MARKER_LTARGET = 2
RSZVB_LIMIT_OFF = 0
RSZVB_LIMIT_UPPER = 1
RSZVB_LIMIT_LOWER = 2
RSZVB_LIMIT_ALL = 3
RSZVB_CAL_DATA_DIRECTIVITY = 0
RSZVB_CAL_DATA_SRCMATCH = 1
RSZVB_CAL_DATA_REFLTRACK = 2
RSZVB_CAL_DATA_ISOLATION = 3
RSZVB_CAL_DATA_LOADMATCH = 4
RSZVB_CAL_DATA_TRANSTRACK = 5
RSZVB_CAL_DATA_G11 = 6
RSZVB_CAL_DATA_G12 = 7
RSZVB_CAL_DATA_G21 = 8
RSZVB_CAL_DATA_G22 = 9
RSZVB_CAL_DATA_H11 = 10
RSZVB_CAL_DATA_H12 = 11
RSZVB_CAL_DATA_H21 = 12
RSZVB_CAL_DATA_H22 = 13
RSZVB_DISP_UPDATE_OFF = 0
RSZVB_DISP_UPDATE_ON = 1
RSZVB_DISP_UPDATE_ONCE = 2
RSZVB_DBACKGROUND = 0
RSZVB_LBACKGROUND = 1
RSZVB_BW_LSTYLES = 2
RSZVB_BW_SOLID = 3
RSZVB_FREQUENCY = 0
RSZVB_TIME = 1
RSZVB_DISTANCE = 0
RSZVB_TYPE_BPAS_IMP = 0
RSZVB_TYPE_LPAS_IMP = 1
RSZVB_TYPE_LPAS_STEP = 2
RSZVB_FILTER_RECT = 0
RSZVB_FILTER_HANN = 1
RSZVB_FILTER_HAMM = 2
RSZVB_FILTER_BOHM = 3
RSZVB_FILTER_DCH = 4
RSZVB_GRID_KFST = 0
RSZVB_GRID_KDFR = 1
RSZVB_GRID_KSDFR = 2
RSZVB_TGATE_TYPE_BPAS = 0
RSZVB_TGATE_TYPE_NOTCH = 1
RSZVB_MEAS_FUNDAMENTAL = 0
RSZVB_MEAS_HARMONIC = 1
RSZVB_CALSTATE_CAL = 0
RSZVB_CALSTATE_CAI = 1
RSZVB_CALSTATE_CA = 2
RSZVB_CALSTATE_CAV = 3
RSZVB_CALSTATE_CALOFF = 4
RSZVB_CALSTATE_NONE = 5
RSZVB_CALUNIT_STD_THR = 0
RSZVB_CALUNIT_STD_OPEN = 1
RSZVB_CALUNIT_STD_SHOR = 2
RSZVB_CALUNIT_STD_MATC = 3
RSZVB_MIX_MODE_MIXER = 0
RSZVB_MIX_MODE_FREQ_CONV_OFF = 1
RSZVB_FUNDAMENTAL_TYPE_RF = 0
RSZVB_FUNDAMENTAL_TYPE_LO = 1
RSZVB_FUNDAMENTAL_TYPE_IF = 2
RSZVB_FUNDAMENTAL_TYPE_LO1 = 3
RSZVB_FUNDAMENTAL_TYPE_LO2 = 4
RSZVB_FUNDAMENTAL_TYPE_AUX = 5
RSZVB_CONVERSION_DCLOWER = 0
RSZVB_CONVERSION_DCUPPER = 1
RSZVB_CONVERSION_UCONVERSION = 2
RSZVB_POWER_MODE_FIXED = 0
RSZVB_POWER_MODE_FUNDAMENTAL = 1
RSZVB_PWR_CAL_PORT = 0
RSZVB_PWR_CAL_GEN = 1
RSZVB_PWR_CAL_CONV = 2
RSZVB_PWR_CAL_ASENSOR = 0
RSZVB_PWR_CAL_BSENSOR = 1
RSZVB_PWR_CAL_OFFSET_ONLY = 0
RSZVB_PWR_CAL_OFFSET_CPADD = 1
RSZVB_PWR_CAL_AWAVE = 0
RSZVB_PWR_CAL_BWAVE = 1
RSZVB_PWR_CAL_B1 = 2
RSZVB_PWR_CAL_B2 = 3
RSZVB_PWR_CAL_B3 = 4
RSZVB_PWR_CAL_B4 = 5
RSZVB_PWR_CAL_B5 = 6
RSZVB_PWR_CAL_B6 = 7
RSZVB_PWR_CAL_B7 = 8
RSZVB_PWR_CAL_B8 = 9
RSZVB_TGATE_SHAPE_MAX = 0
RSZVB_TGATE_SHAPE_WIDE = 1
RSZVB_TGATE_SHAPE_NORM = 2
RSZVB_TGATE_SHAPE_MIN = 3
RSZVB_SAW_SBAL = 0
RSZVB_LIMIT_RDOM_COMP_S = 0
RSZVB_LIMIT_RDOM_COMP_SINV = 1
RSZVB_LIMIT_RDOM_COMP_Y = 2
RSZVB_LIMIT_RDOM_COMP_Z = 3
RSZVB_LIMIT_RDOM_COMP_YREL = 4
RSZVB_LIMIT_RDOM_COMP_ZREL = 5
RSZVB_LIMIT_RDOM_FORM_COMP = 0
RSZVB_LIMIT_RDOM_FORM_MAGN = 1
RSZVB_LIMIT_RDOM_FORM_PHAS = 2
RSZVB_LIMIT_RDOM_FORM_REAL = 3
RSZVB_LIMIT_RDOM_FORM_IMAG = 4
RSZVB_LIMIT_RDOM_FORM_SWR = 5
RSZVB_LIMIT_RDOM_FORM_GDEL = 6
RSZVB_LIMIT_RDOM_FORM_L = 7
RSZVB_LIMIT_RDOM_FORM_C = 8
RSZVB_LIMIT_RDOM_SPAC_LIN = 0
RSZVB_LIMIT_RDOM_SPAC_LOG = 1
RSZVB_LIMIT_RDOM_SPAC_DB = 2
RSZVB_LIMIT_RDOM_SPAC_SIC = 3
RSZVB_LIMIT_DOM_FLIN = 0
RSZVB_LIMIT_DOM_FLOG = 1
RSZVB_LIMIT_DOM_FSEG = 2
RSZVB_LIMIT_DOM_FSIN = 3
RSZVB_LIMIT_DOM_TLIN = 4
RSZVB_LIMIT_DOM_TLOG = 5
RSZVB_LIMIT_DOM_PLIN = 6
RSZVB_LIMIT_DOM_PLOG = 7
RSZVB_LIMIT_DOM_PSIN = 8
RSZVB_MATH_FUNC_NORM = 0
RSZVB_MATH_FUNC_ADD = 1
RSZVB_MATH_FUNC_SUB = 2
RSZVB_MATH_FUNC_MULT = 3
RSZVB_MATH_FUNC_DIV = 4
RSZVB_CONV_S = 0
RSZVB_CONV_Y = 1
RSZVB_CONV_Z = 2
RSZVB_VNET_FUNC_DEEMBED = 0
RSZVB_VNET_FUNC_EMBED = 1
RSZVB_VNET_PARAM_C = 0
RSZVB_VNET_PARAM_L = 1
RSZVB_VNET_PARAM_R = 2
RSZVB_BALANCED_CIRCUIT_FIMP = 0
RSZVB_BALANCED_CIRCUIT_STSL = 1
RSZVB_BALANCED_CIRCUIT_STSC = 2
RSZVB_BALANCED_CIRCUIT_SLST = 3
RSZVB_BALANCED_CIRCUIT_SCST = 4
RSZVB_BALANCED_CIRCUIT_CSSL = 5
RSZVB_BALANCED_CIRCUIT_LSSC = 6
RSZVB_BALANCED_CIRCUIT_CSSC = 7
RSZVB_BALANCED_CIRCUIT_LSSL = 8
RSZVB_BALANCED_CIRCUIT_SLCS = 9
RSZVB_BALANCED_CIRCUIT_SCLS = 10
RSZVB_BALANCED_CIRCUIT_SCCS = 11
RSZVB_BALANCED_CIRCUIT_SLLS = 12
RSZVB_SENDED_CIRCUIT_FIMP = 0
RSZVB_SENDED_CIRCUIT_CSL = 1
RSZVB_SENDED_CIRCUIT_LSC = 2
RSZVB_SENDED_CIRCUIT_CSC = 3
RSZVB_SENDED_CIRCUIT_LSL = 4
RSZVB_SENDED_CIRCUIT_SLC = 5
RSZVB_SENDED_CIRCUIT_SCL = 6
RSZVB_SENDED_CIRCUIT_SCC = 7
RSZVB_SENDED_CIRCUIT_SLL = 8
RSZVB_ELEMENT_BACKGROUND = 1
RSZVB_ELEMENT_TEXT = 2
RSZVB_ELEMENT_SELTEXT = 3
RSZVB_ELEMENT_GRID = 4
RSZVB_ELEMENT_REFLINE = 5
RSZVB_ELEMENT_ALLMAKERS = 6
RSZVB_ELEMENT_HLINE = 7
RSZVB_ELEMENT_DTITLE = 8
RSZVB_ELEMENT_LIMITFAILTRACE = 9
RSZVB_ELEMENT_LIMITLINEOFF = 10
RSZVB_ELEMENT_LIMITLINEUPPER = 11
RSZVB_ELEMENT_LIMITLINELOWER = 12
RSZVB_ELEMENT_TRACE1 = 13
RSZVB_ELEMENT_TRACE2 = 14
RSZVB_ELEMENT_TRACE3 = 15
RSZVB_ELEMENT_TRACE4 = 16
RSZVB_ELEMENT_TRACE5 = 17
RSZVB_ELEMENT_TRACE6 = 18
RSZVB_ELEMENT_TRACE7 = 19
RSZVB_ELEMENT_TRACE8 = 20
RSZVB_ELEMENT_TRACE9 = 21
RSZVB_ELEMENT_TRACE10 = 22
RSZVB_ELEMENT_TRACE11 = 23
RSZVB_ELEMENT_TRACE12 = 24
RSZVB_ELEMENT_TRACE13 = 25
RSZVB_ELEMENT_TRACE14 = 26
RSZVB_ELEMENT_TRACE15 = 27
RSZVB_ELEMENT_TRACE16 = 28
RSZVB_TRACE_STYLE_SOLID = 0
RSZVB_TRACE_STYLE_DASHED = 1
RSZVB_TRACE_STYLE_DOTTED = 2
RSZVB_TRACE_STYLE_DDOTTED = 3
RSZVB_TRACE_STYLE_DDDOTTED = 4
RSZVB_CALSTD_MMTH = 0
RSZVB_CALSTD_FFTH = 1
RSZVB_CALSTD_MFTH = 2
RSZVB_CALSTD_MMLI = 3
RSZVB_CALSTD_FFLI = 4
RSZVB_CALSTD_MFLI = 5
RSZVB_CALSTD_OSH = 6
RSZVB_CALSTD_MOSH = 7
RSZVB_CALSTD_FOSH = 8
RSZVB_CALSTD_MMAT = 9
RSZVB_CALSTD_FFAT = 10
RSZVB_CALSTD_MFAT = 11
RSZVB_CALSTD_MMSN = 12
RSZVB_CALSTD_FFSN = 13
RSZVB_CALSTD_MFSN = 14
RSZVB_CALSTD_MOP = 15
RSZVB_CALSTD_FOP = 16
RSZVB_CALSTD_MSH = 17
RSZVB_CALSTD_FSH = 18
RSZVB_CALSTD_MREF = 19
RSZVB_CALSTD_FREF = 20
RSZVB_CALSTD_MMTC = 21
RSZVB_CALSTD_FMTC = 22
RSZVB_CALSTD_MSM = 23
RSZVB_CALSTD_FSM = 24
RSZVB_CALSTD_MMLI_2 = 25
RSZVB_CALSTD_FFLI_2 = 26
RSZVB_CALSTD_MFLI_2 = 27
RSZVB_CALSTD_MMLI_3 = 28
RSZVB_CALSTD_FFLI_3 = 29
RSZVB_CALSTD_MFLI_3 = 30
RSZVB_CALSTD_MOSH_2 = 31
RSZVB_CALSTD_FOSH_2 = 32
RSZVB_CALSTD_MOSH_3 = 33
RSZVB_CALSTD_FOSH_3 = 34
RSZVB_VNET_PARAM_PMAIN = 0
RSZVB_VNET_PARAM_PSECOND = 1
RSZVB_CONNECTION_MODE_TEM = 0
RSZVB_CONNECTION_MODE_WGUIDE = 1
RSZVB_CONNECTION_CONNECTOR_GENDER = 0
RSZVB_CONNECTION_CONNECTOR_NGENDER = 1
RSZVB_RECEIVER = 0
RSZVB_SOURCE = 1
RSZVB_SWEEP_TYPE_SWEEP = 0
RSZVB_SWEEP_TYPE_FIXED = 1
RSZVB_SELECTIVITY_NORMAL = 0
RSZVB_SELECTIVITY_HIGH = 1
RSZVB_ATTEN_AREC = 0
RSZVB_ATTEN_BREC = 1
RSZVB_ATTEN_CREC = 2
RSZVB_ATTEN_DREC = 3
RSZVB_IF_GAIN_AUTO = 0
RSZVB_IF_GAIN_LNOISE = 1
RSZVB_IF_GAIN_LDIST = 2
RSZVB_TRACE_MDATA1 = 0
RSZVB_TRACE_MDATA2 = 1
RSZVB_TRACE_MDATA3 = 2
RSZVB_TRACE_MDATA4 = 3
RSZVB_TRACE_MDATA5 = 4
RSZVB_TRACE_MDATA6 = 5
RSZVB_TRACE_MDATA7 = 6
RSZVB_TRACE_MDATA8 = 7
RSZVB_ALT_SWE_MODE_NORMAL = 0
RSZVB_ALT_SWE_MODE_ALTER = 1
RSZVB_CONNECTOR_GENDER_MALE = 0
RSZVB_CONNECTOR_GENDER_FEMALE = 1
RSZVB_DISPLAY_RESULTS_EPD = 0
RSZVB_DISPLAY_RESULTS_MMPT = 1
RSZVB_DISPLAY_RESULTS_MSTD = 2
RSZVB_DISPLAY_RESULTS_RMS = 3
RSZVB_DISPLAY_RESULTS_SFL = 4
RSZVB_DISPLAY_RESULTS_COMP = 5
RSZVB_COMPLEX = 0
RSZVB_LINP = 1
RSZVB_LOGP = 2
RSZVB_PULSE_REC_A = 0
RSZVB_PULSE_REC_B = 1
RSZVB_PULSE_INTERFACE_GEN = 0
RSZVB_PULSE_INTERFACE_SRC = 1
RSZVB_PULSE_MODE_NORMAL = 0
RSZVB_PULSE_MODE_MEAN = 1
RSZVB_FORMAT_BORDER_SWAP = 0
RSZVB_FORMAT_BORDER_NORM = 1
RSZVB_TRACE_ZVR_CH1DATA = 0
RSZVB_TRACE_ZVR_CH2DATA = 1
RSZVB_TRACE_ZVR_CH3DATA = 2
RSZVB_TRACE_ZVR_CH4DATA = 3
RSZVB_TRACE_ZVR_CH1MEM = 4
RSZVB_TRACE_ZVR_CH2MEM = 5
RSZVB_TRACE_ZVR_CH3MEM = 6
RSZVB_TRACE_ZVR_CH4MEM = 7
RSZVB_TRACE_ZVR_MDATA1 = 8
RSZVB_TRACE_ZVR_MDATA2 = 9
RSZVB_TRACE_ZVR_MDATA3 = 10
RSZVB_TRACE_ZVR_MDATA4 = 11
RSZVB_TRACE_ZVR_MDATA5 = 12
RSZVB_TRACE_ZVR_MDATA6 = 13
RSZVB_TRACE_ZVR_MDATA7 = 14
RSZVB_TRACE_ZVR_MDATA8 = 15
RSZVB_POWER_SENDED = 0
RSZVB_POWER_DCMODE = 1
RSZVB_FREQ_CONVERSION_RILI = 0
RSZVB_FREQ_CONVERSION_RILE = 1
RSZVB_CHANNEL_TRACE_SINGLE = 0
RSZVB_CHANNEL_TRACE_ALL = 1
RSZVB_SAVE = 0
RSZVB_RECALL = 1
RSZVB_POIN = 0
RSZVB_COMM = 1
RSZVB_SEM = 0
RSZVB_TAB = 2
RSZVB_SPAC = 3
RSZVB_RENORMALIZATION_TWAV = 0
RSZVB_RENORMALIZATION_PWAV = 1
RSZVB_IMOD_SRC_NONE = 0
RSZVB_IMOD_SRC_PORT = 1
RSZVB_IMOD_SRC_GEN = 2
RSZVB_IMOD_SRC_EMB = 3
RSZVB_UTHR_AUTO = 0
RSZVB_UTHR_MAN = 1
RSZVB_LANG_SCPI = 0
RSZVB_LANG_PNA = 1
RSZVB_LANG_HP8510 = 2
RSZVB_LANG_HP8720 = 3
RSZVB_LANG_HP8753 = 4
RSZVB_BWID_MODE_BPAS = 0
RSZVB_BWID_MODE_BST = 1
RSZVB_BWID_MODE_BPRM = 2
RSZVB_BWID_MODE_BSRM = 3
RSZVB_BWID_MODE_BPAB = 4
RSZVB_BWID_MODE_BSAB = 5
RSZVB_ATTEN_MODE_AUTO = 0
RSZVB_ATTEN_MODE_MAN = 1
RSZVB_ATTEN_MODE_LNO = 2
RSZVB_MIXER_LOAD_FILE = 0
RSZVB_MIXER_LOAD_DELAY = 1
RSZVB_IMOD_SOURCE_PORT = 0
RSZVB_IMOD_SOURCE_EDEV = 1
RSZVB_DISP_TRAC_DATA = 0
RSZVB_DISP_TRAC_MEM = 1
RSZVB_DISP_TRAC_SING = 2
RSZVB_HOLD_OFF = 0
RSZVB_HOLD_MAX = 1
RSZVB_HOLD_MIN = 2
RSZVB_PULS_TYPE_SING = 0
RSZVB_PULS_TYPE_TRAI = 1
RSZVB_PULS_TYPE_CHIG = 2
RSZVB_PULS_TYPE_CLOW = 3
RSZVB_PULS_POL_NORM = 0
RSZVB_PULS_POL_INV = 1
RSZVB_PULS_MODE_CSP = 0
RSZVB_PULS_MODE_CONT = 1
RSZVB_ASSIGN_G1M = 0
RSZVB_ASSIGN_G2M = 1
RSZVB_ASSIGN_G2M2 = 2
RSZVB_ASSIGN_G1M3 = 3
RSZVB_MIX_MODE_VMIXER = 0
RSZVB_GLOOP_CIRCUIT_FIMP = 0
RSZVB_GLOOP_CIRCUIT_SL = 1
RSZVB_GLOOP_CIRCUIT_SC = 2
RSZVB_LDEV_OFF = 0
RSZVB_LDEV_ON = 1
RSZVB_LDEV_TRAC = 2
RSZVB_NOISE_FIGURE_CAL_STEP_REC = 0
RSZVB_NOISE_FIGURE_CAL_STEP_SRC = 1
RSZVB_NOISE_FIGURE_CAL_STEP_ATT = 2
RSZVB_MODE_PALL = 0
RSZVB_MODE_PSP = 1
RSZVB_PRIORITY_NORMAL = 0
RSZVB_PRIORITY_ABOVE_NORMAL = 1
RSZVB_PRIORITY_HIGH = 2
RSZVB_MDEL_LAN1 = 1
RSZVB_MDEL_LAN2 = 2
RSZVB_UNIT_POW = 0
RSZVB_UNIT_VOLT = 1
RSZVB_CONVERTER_DSET = 0
RSZVB_CONVERTER_LAPP = 1
RSZVB_CONVERTER_ELEC = 2
RSZVB_CONVERTER_NONE = 3
RSZVB_CONVERTER_ATT_MECH = 0
RSZVB_CONVERTER_ATT_EL = 1
RSZVB_CORR_TCO_LOAD = 0
RSZVB_CORR_TCO_STORE = 1
RSZVB_PS_POSITION_DEV = 0
RSZVB_PS_POSITION_PWR = 1
RSZVB_CORR_TCO_LIST_INSERT = 0
RSZVB_CORR_TCO_LIST_APPEND = 1
RSZVB_RESTART_KEEP = 0
RSZVB_RESTART_RESET = 1
RSZVB_CALC_GEOM = 0
RSZVB_CALC_ARIT = 1
RSZVB_S_PARAMETER_DETECTOR_NORMAL = 0
RSZVB_S_PARAMETER_DETECTOR_AVERAGE = 1
RSZVB_PORT_BIT_A = 0
RSZVB_PORT_BIT_B = 1
RSZVB_PORT_BIT_C = 2
RSZVB_PORT_BIT_D = 3
RSZVB_PORT_BIT_E = 4
RSZVB_PORT_BIT_F = 5
RSZVB_RF_OFF_BEHAVIOR_FAST = 0
RSZVB_RF_OFF_BEHAVIOR_LBN = 1
RSZVB_REF_POWER_A_WAVE = 0
RSZVB_REF_POWER_NOMINAL = 1
RSZVB_RENORMALIZATION_MODE_AUTO = 0
RSZVB_RENORMALIZATION_MODE_EXPL = 1
RSZVB_SPUR_AVOID_POSITIVE = 0
RSZVB_SPUR_AVOID_NEGATIVE = 1
RSZVB_SPUR_AVOID_AUTO = 2
RSZVB_DIRECTION_IN = 0
RSZVB_DIRECTION_OUT = 1
RSZVB_MINIMUM_FREQUENCY_OFFSET_DIRECT = 0
RSZVB_MINIMUM_FREQUENCY_OFFSET_BANDWIDTH = 1
RSZVB_TRM_PMODULATOR = 0
RSZVB_TRM_COMBINER = 1
RSZVB_TRM_OUTPUT = 2
RSZVB_TRM_SOURCE_OFF = 0
RSZVB_TRM_SOURCE_G1INT = 1
RSZVB_TRM_SOURCE_G2INT = 2
RSZVB_TRM_SOURCE_G1EXT = 3
RSZVB_TRM_SOURCE_G2EXT = 4
RSZVB_CALTYPE_DEF = 0
RSZVB_PWR_CAL_METHOD_POWER_METER_ONLY = 0
RSZVB_PWR_CAL_METHOD_REF_RECEIVER_AFTER = 1
RSZVB_PWR_CAL_METHOD_REF_RECEIVER_ONLY = 2
RSZVB_CONVERTER_DATA_SET_FACTORY = 0
RSZVB_CONVERTER_DATA_SET_USER = 1
RSZVB_VMIX_MODE_BASE = 0
RSZVB_VMIX_MODE_MIXER = 1
RSZVB_MIXER_PARAM_AUTO = 0
RSZVB_MIXER_PARAM_USER = 1

#DLL functions

# rszvb_init ['ViRsrc resourceName', 'ViBoolean IDQuery', 'ViBoolean resetDevice', 'ViSession* instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_char_p,c_bool,c_bool,POINTER(c_int))
paramflags = ((1, 'resourceName'),(1, 'IDQuery'),(1, 'resetDevice'),(2, 'instrumentHandle'),)
rszvb_init  = prototype(('rszvb_init', rszvbDLL), paramflags)
rszvb_init.name = 'rszvb_init'
rszvb_init.errcheck = __errorcheck__
rszvb_init.output = True
# rszvb_ApplicationExample ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 startFrequency', 'ViReal64 stopFrequency', 'ViReal64 power', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR stimulusData[]', 'ViReal64 _VI_FAR responseData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double,c_double,c_double,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'startFrequency'),(1, 'stopFrequency'),(1, 'power'),(2, 'noOfValues'),(1, 'stimulusData[]'),(1, 'responseData[]'),)
rszvb_ApplicationExample  = prototype(('rszvb_ApplicationExample', rszvbDLL), paramflags)
rszvb_ApplicationExample.name = 'rszvb_ApplicationExample'
rszvb_ApplicationExample.errcheck = __errorcheck__
rszvb_ApplicationExample.output = True
# rszvb_WindowNew ['ViSession instrumentHandle', 'ViString setupName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'setupName'),)
rszvb_WindowNew  = prototype(('rszvb_WindowNew', rszvbDLL), paramflags)
rszvb_WindowNew.name = 'rszvb_WindowNew'
rszvb_WindowNew.errcheck = __errorcheck__
rszvb_WindowNew.output = False
# rszvb_WindowSelect ['ViSession instrumentHandle', 'ViString setupName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'setupName'),)
rszvb_WindowSelect  = prototype(('rszvb_WindowSelect', rszvbDLL), paramflags)
rszvb_WindowSelect.name = 'rszvb_WindowSelect'
rszvb_WindowSelect.errcheck = __errorcheck__
rszvb_WindowSelect.output = False
# rszvb_WindowClose ['ViSession instrumentHandle', 'ViString setupName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'setupName'),)
rszvb_WindowClose  = prototype(('rszvb_WindowClose', rszvbDLL), paramflags)
rszvb_WindowClose.name = 'rszvb_WindowClose'
rszvb_WindowClose.errcheck = __errorcheck__
rszvb_WindowClose.output = False
# rszvb_WindowList ['ViSession instrumentHandle', 'ViChar _VI_FAR catalog[]', 'ViInt32 bufferSize']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'catalog[]'),(1, 'bufferSize'),)
rszvb_WindowList  = prototype(('rszvb_WindowList', rszvbDLL), paramflags)
rszvb_WindowList.name = 'rszvb_WindowList'
rszvb_WindowList.errcheck = __errorcheck__
rszvb_WindowList.output = False
# rszvb_Print ['ViSession instrumentHandle', 'ViString printerName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'printerName'),)
rszvb_Print  = prototype(('rszvb_Print', rszvbDLL), paramflags)
rszvb_Print.name = 'rszvb_Print'
rszvb_Print.errcheck = __errorcheck__
rszvb_Print.output = False
# rszvb_PrinttoFile ['ViSession instrumentHandle', 'ViString fileName', 'ViInt32 fileFormat', 'ViInt32 diagramArea', 'ViBoolean logo', 'ViBoolean dateAndTime', 'ViBoolean markerList']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_int32,c_int32,c_bool,c_bool,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),(1, 'fileFormat'),(1, 'diagramArea'),(1, 'logo'),(1, 'dateAndTime'),(1, 'markerList'),)
rszvb_PrinttoFile  = prototype(('rszvb_PrinttoFile', rszvbDLL), paramflags)
rszvb_PrinttoFile.name = 'rszvb_PrinttoFile'
rszvb_PrinttoFile.errcheck = __errorcheck__
rszvb_PrinttoFile.output = False
# rszvb_PrintSetup ['ViSession instrumentHandle', 'ViInt32 diagramArea', 'ViBoolean logo', 'ViBoolean dateAndTime', 'ViBoolean markerList', 'ViInt32 pageOrientation', 'ViReal64 leftMargin', 'ViReal64 rightMargin', 'ViReal64 topMargin', 'ViReal64 bottomMargin']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool,c_bool,c_bool,c_int32,c_double,c_double,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'diagramArea'),(1, 'logo'),(1, 'dateAndTime'),(1, 'markerList'),(1, 'pageOrientation'),(1, 'leftMargin'),(1, 'rightMargin'),(1, 'topMargin'),(1, 'bottomMargin'),)
rszvb_PrintSetup  = prototype(('rszvb_PrintSetup', rszvbDLL), paramflags)
rszvb_PrintSetup.name = 'rszvb_PrintSetup'
rszvb_PrintSetup.errcheck = __errorcheck__
rszvb_PrintSetup.output = False
# rszvb_FileManager ['ViSession instrumentHandle', 'ViInt32 operationToBePerformed', 'ViString source', 'ViString destination']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'operationToBePerformed'),(1, 'source'),(1, 'destination'),)
rszvb_FileManager  = prototype(('rszvb_FileManager', rszvbDLL), paramflags)
rszvb_FileManager.name = 'rszvb_FileManager'
rszvb_FileManager.errcheck = __errorcheck__
rszvb_FileManager.output = False
# rszvb_GetCurrentDirectory ['ViSession instrumentHandle', 'ViChar _VI_FAR currentDirectory[]']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'currentDirectory[]'),)
rszvb_GetCurrentDirectory  = prototype(('rszvb_GetCurrentDirectory', rszvbDLL), paramflags)
rszvb_GetCurrentDirectory.name = 'rszvb_GetCurrentDirectory'
rszvb_GetCurrentDirectory.errcheck = __errorcheck__
rszvb_GetCurrentDirectory.output = False
# rszvb_SetupSave ['ViSession instrumentHandle', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),)
rszvb_SetupSave  = prototype(('rszvb_SetupSave', rszvbDLL), paramflags)
rszvb_SetupSave.name = 'rszvb_SetupSave'
rszvb_SetupSave.errcheck = __errorcheck__
rszvb_SetupSave.output = False
# rszvb_SetupRecall ['ViSession instrumentHandle', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),)
rszvb_SetupRecall  = prototype(('rszvb_SetupRecall', rszvbDLL), paramflags)
rszvb_SetupRecall.name = 'rszvb_SetupRecall'
rszvb_SetupRecall.errcheck = __errorcheck__
rszvb_SetupRecall.output = False
# rszvb_readToFile ['ViSession instrumentHandle', 'ViString source', 'ViString destination']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'source'),(1, 'destination'),)
rszvb_readToFile  = prototype(('rszvb_readToFile', rszvbDLL), paramflags)
rszvb_readToFile.name = 'rszvb_readToFile'
rszvb_readToFile.errcheck = __errorcheck__
rszvb_readToFile.output = False
# rszvb_writeFromFile ['ViSession instrumentHandle', 'ViString source', 'ViString destination']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'source'),(1, 'destination'),)
rszvb_writeFromFile  = prototype(('rszvb_writeFromFile', rszvbDLL), paramflags)
rszvb_writeFromFile.name = 'rszvb_writeFromFile'
rszvb_writeFromFile.errcheck = __errorcheck__
rszvb_writeFromFile.output = False
# rszvb_SelectPowerMeter ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 powerMeter', 'ViInt32 outPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'powerMeter'),(1, 'outPort'),)
rszvb_SelectPowerMeter  = prototype(('rszvb_SelectPowerMeter', rszvbDLL), paramflags)
rszvb_SelectPowerMeter.name = 'rszvb_SelectPowerMeter'
rszvb_SelectPowerMeter.errcheck = __errorcheck__
rszvb_SelectPowerMeter.output = False
# rszvb_SelectSParameters ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 outPort', 'ViInt32 inPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'outPort'),(1, 'inPort'),)
rszvb_SelectSParameters  = prototype(('rszvb_SelectSParameters', rszvbDLL), paramflags)
rszvb_SelectSParameters.name = 'rszvb_SelectSParameters'
rszvb_SelectSParameters.errcheck = __errorcheck__
rszvb_SelectSParameters.output = False
# rszvb_SelectMoreSParameters ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 outMode', 'ViInt32 outPort', 'ViInt32 inMode', 'ViInt32 inPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'outMode'),(1, 'outPort'),(1, 'inMode'),(1, 'inPort'),)
rszvb_SelectMoreSParameters  = prototype(('rszvb_SelectMoreSParameters', rszvbDLL), paramflags)
rszvb_SelectMoreSParameters.name = 'rszvb_SelectMoreSParameters'
rszvb_SelectMoreSParameters.errcheck = __errorcheck__
rszvb_SelectMoreSParameters.output = False
# rszvb_SelectRatios ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 ratios']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'ratios'),)
rszvb_SelectRatios  = prototype(('rszvb_SelectRatios', rszvbDLL), paramflags)
rszvb_SelectRatios.name = 'rszvb_SelectRatios'
rszvb_SelectRatios.errcheck = __errorcheck__
rszvb_SelectRatios.output = False
# rszvb_SelectMoreRatios ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 sourcePort', 'ViInt32 numeratorType', 'ViInt32 numeratorPortNumber', 'ViInt32 denominatorType', 'ViInt32 denominatorPortNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'sourcePort'),(1, 'numeratorType'),(1, 'numeratorPortNumber'),(1, 'denominatorType'),(1, 'denominatorPortNumber'),)
rszvb_SelectMoreRatios  = prototype(('rszvb_SelectMoreRatios', rszvbDLL), paramflags)
rszvb_SelectMoreRatios.name = 'rszvb_SelectMoreRatios'
rszvb_SelectMoreRatios.errcheck = __errorcheck__
rszvb_SelectMoreRatios.output = False
# rszvb_SelectMoreRatiosWithDetector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 sourcePort', 'ViInt32 numeratorType', 'ViInt32 numeratorPortNumber', 'ViInt32 denominatorType', 'ViInt32 denominatorPortNumber', 'ViInt32 detector', 'ViReal64 observationTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'sourcePort'),(1, 'numeratorType'),(1, 'numeratorPortNumber'),(1, 'denominatorType'),(1, 'denominatorPortNumber'),(1, 'detector'),(1, 'observationTime'),)
rszvb_SelectMoreRatiosWithDetector  = prototype(('rszvb_SelectMoreRatiosWithDetector', rszvbDLL), paramflags)
rszvb_SelectMoreRatiosWithDetector.name = 'rszvb_SelectMoreRatiosWithDetector'
rszvb_SelectMoreRatiosWithDetector.errcheck = __errorcheck__
rszvb_SelectMoreRatiosWithDetector.output = False
# rszvb_SelectMoreRatiosGenerator ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 generatorNumber', 'ViInt32 numeratorType', 'ViInt32 numeratorPortNumber', 'ViInt32 denominatorType', 'ViInt32 denominatorPortNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'generatorNumber'),(1, 'numeratorType'),(1, 'numeratorPortNumber'),(1, 'denominatorType'),(1, 'denominatorPortNumber'),)
rszvb_SelectMoreRatiosGenerator  = prototype(('rszvb_SelectMoreRatiosGenerator', rszvbDLL), paramflags)
rszvb_SelectMoreRatiosGenerator.name = 'rszvb_SelectMoreRatiosGenerator'
rszvb_SelectMoreRatiosGenerator.errcheck = __errorcheck__
rszvb_SelectMoreRatiosGenerator.output = False
# rszvb_SelectMoreRatiosGeneratorWithDetector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 generatorNumber', 'ViInt32 numeratorType', 'ViInt32 numeratorPortNumber', 'ViInt32 denominatorType', 'ViInt32 denominatorPortNumber', 'ViInt32 detector', 'ViReal64 observationTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'generatorNumber'),(1, 'numeratorType'),(1, 'numeratorPortNumber'),(1, 'denominatorType'),(1, 'denominatorPortNumber'),(1, 'detector'),(1, 'observationTime'),)
rszvb_SelectMoreRatiosGeneratorWithDetector  = prototype(('rszvb_SelectMoreRatiosGeneratorWithDetector', rszvbDLL), paramflags)
rszvb_SelectMoreRatiosGeneratorWithDetector.name = 'rszvb_SelectMoreRatiosGeneratorWithDetector'
rszvb_SelectMoreRatiosGeneratorWithDetector.errcheck = __errorcheck__
rszvb_SelectMoreRatiosGeneratorWithDetector.output = False
# rszvb_SelectWaveQuantities ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 waveQuantities']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'waveQuantities'),)
rszvb_SelectWaveQuantities  = prototype(('rszvb_SelectWaveQuantities', rszvbDLL), paramflags)
rszvb_SelectWaveQuantities.name = 'rszvb_SelectWaveQuantities'
rszvb_SelectWaveQuantities.errcheck = __errorcheck__
rszvb_SelectWaveQuantities.output = False
# rszvb_SelectMoreWaveQuantities ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 waveQuantityType', 'ViInt32 waveQuantityPortNumber', 'ViInt32 sourcePort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'waveQuantityType'),(1, 'waveQuantityPortNumber'),(1, 'sourcePort'),)
rszvb_SelectMoreWaveQuantities  = prototype(('rszvb_SelectMoreWaveQuantities', rszvbDLL), paramflags)
rszvb_SelectMoreWaveQuantities.name = 'rszvb_SelectMoreWaveQuantities'
rszvb_SelectMoreWaveQuantities.errcheck = __errorcheck__
rszvb_SelectMoreWaveQuantities.output = False
# rszvb_SelectMoreWaveQuantitiesWithDetector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 waveQuantityType', 'ViInt32 waveQuantityPortNumber', 'ViInt32 sourcePort', 'ViInt32 detector', 'ViReal64 observationTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'waveQuantityType'),(1, 'waveQuantityPortNumber'),(1, 'sourcePort'),(1, 'detector'),(1, 'observationTime'),)
rszvb_SelectMoreWaveQuantitiesWithDetector  = prototype(('rszvb_SelectMoreWaveQuantitiesWithDetector', rszvbDLL), paramflags)
rszvb_SelectMoreWaveQuantitiesWithDetector.name = 'rszvb_SelectMoreWaveQuantitiesWithDetector'
rszvb_SelectMoreWaveQuantitiesWithDetector.errcheck = __errorcheck__
rszvb_SelectMoreWaveQuantitiesWithDetector.output = False
# rszvb_SelectImpedances ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 outPort', 'ViInt32 inPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'outPort'),(1, 'inPort'),)
rszvb_SelectImpedances  = prototype(('rszvb_SelectImpedances', rszvbDLL), paramflags)
rszvb_SelectImpedances.name = 'rszvb_SelectImpedances'
rszvb_SelectImpedances.errcheck = __errorcheck__
rszvb_SelectImpedances.output = False
# rszvb_SelectMoreImpedances ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 outMode', 'ViInt32 outPort', 'ViInt32 inMode', 'ViInt32 inPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'outMode'),(1, 'outPort'),(1, 'inMode'),(1, 'inPort'),)
rszvb_SelectMoreImpedances  = prototype(('rszvb_SelectMoreImpedances', rszvbDLL), paramflags)
rszvb_SelectMoreImpedances.name = 'rszvb_SelectMoreImpedances'
rszvb_SelectMoreImpedances.errcheck = __errorcheck__
rszvb_SelectMoreImpedances.output = False
# rszvb_SelectAdmitances ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 outPort', 'ViInt32 inPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'outPort'),(1, 'inPort'),)
rszvb_SelectAdmitances  = prototype(('rszvb_SelectAdmitances', rszvbDLL), paramflags)
rszvb_SelectAdmitances.name = 'rszvb_SelectAdmitances'
rszvb_SelectAdmitances.errcheck = __errorcheck__
rszvb_SelectAdmitances.output = False
# rszvb_SelectMoreAdmitances ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 outMode', 'ViInt32 outPort', 'ViInt32 inMode', 'ViInt32 inPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'outMode'),(1, 'outPort'),(1, 'inMode'),(1, 'inPort'),)
rszvb_SelectMoreAdmitances  = prototype(('rszvb_SelectMoreAdmitances', rszvbDLL), paramflags)
rszvb_SelectMoreAdmitances.name = 'rszvb_SelectMoreAdmitances'
rszvb_SelectMoreAdmitances.errcheck = __errorcheck__
rszvb_SelectMoreAdmitances.output = False
# rszvb_SelectZParameters ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 outMode', 'ViInt32 outPort', 'ViInt32 inMode', 'ViInt32 inPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'outMode'),(1, 'outPort'),(1, 'inMode'),(1, 'inPort'),)
rszvb_SelectZParameters  = prototype(('rszvb_SelectZParameters', rszvbDLL), paramflags)
rszvb_SelectZParameters.name = 'rszvb_SelectZParameters'
rszvb_SelectZParameters.errcheck = __errorcheck__
rszvb_SelectZParameters.output = False
# rszvb_SelectYParameters ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 outMode', 'ViInt32 outPort', 'ViInt32 inMode', 'ViInt32 inPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'outMode'),(1, 'outPort'),(1, 'inMode'),(1, 'inPort'),)
rszvb_SelectYParameters  = prototype(('rszvb_SelectYParameters', rszvbDLL), paramflags)
rszvb_SelectYParameters.name = 'rszvb_SelectYParameters'
rszvb_SelectYParameters.errcheck = __errorcheck__
rszvb_SelectYParameters.output = False
# rszvb_SelectStabilityFactors ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 DUTOut', 'ViInt32 DUTIn', 'ViInt32 stabilityFactor']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'DUTOut'),(1, 'DUTIn'),(1, 'stabilityFactor'),)
rszvb_SelectStabilityFactors  = prototype(('rszvb_SelectStabilityFactors', rszvbDLL), paramflags)
rszvb_SelectStabilityFactors.name = 'rszvb_SelectStabilityFactors'
rszvb_SelectStabilityFactors.errcheck = __errorcheck__
rszvb_SelectStabilityFactors.output = False
# rszvb_SelectDCMeasurement ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 DCMeas']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'DCMeas'),)
rszvb_SelectDCMeasurement  = prototype(('rszvb_SelectDCMeasurement', rszvbDLL), paramflags)
rszvb_SelectDCMeasurement.name = 'rszvb_SelectDCMeasurement'
rszvb_SelectDCMeasurement.errcheck = __errorcheck__
rszvb_SelectDCMeasurement.output = False
# rszvb_SelectPAEMeasurement ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 DUTOut', 'ViInt32 DUTIn']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'DUTOut'),(1, 'DUTIn'),)
rszvb_SelectPAEMeasurement  = prototype(('rszvb_SelectPAEMeasurement', rszvbDLL), paramflags)
rszvb_SelectPAEMeasurement.name = 'rszvb_SelectPAEMeasurement'
rszvb_SelectPAEMeasurement.errcheck = __errorcheck__
rszvb_SelectPAEMeasurement.output = False
# rszvb_DefinePAEMeasurement ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 testModel', 'ViReal64 constantC', 'ViReal64 constantK']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'testModel'),(1, 'constantC'),(1, 'constantK'),)
rszvb_DefinePAEMeasurement  = prototype(('rszvb_DefinePAEMeasurement', rszvbDLL), paramflags)
rszvb_DefinePAEMeasurement.name = 'rszvb_DefinePAEMeasurement'
rszvb_DefinePAEMeasurement.errcheck = __errorcheck__
rszvb_DefinePAEMeasurement.output = False
# rszvb_SelectNoiseFigure ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 outPort', 'ViInt32 inPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'outPort'),(1, 'inPort'),)
rszvb_SelectNoiseFigure  = prototype(('rszvb_SelectNoiseFigure', rszvbDLL), paramflags)
rszvb_SelectNoiseFigure.name = 'rszvb_SelectNoiseFigure'
rszvb_SelectNoiseFigure.errcheck = __errorcheck__
rszvb_SelectNoiseFigure.output = False
# rszvb_CreateTrace ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViString parameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'parameter'),)
rszvb_CreateTrace  = prototype(('rszvb_CreateTrace', rszvbDLL), paramflags)
rszvb_CreateTrace.name = 'rszvb_CreateTrace'
rszvb_CreateTrace.errcheck = __errorcheck__
rszvb_CreateTrace.output = False
# rszvb_ConfigureMesurementParameters ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViString parameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'parameter'),)
rszvb_ConfigureMesurementParameters  = prototype(('rszvb_ConfigureMesurementParameters', rszvbDLL), paramflags)
rszvb_ConfigureMesurementParameters.name = 'rszvb_ConfigureMesurementParameters'
rszvb_ConfigureMesurementParameters.errcheck = __errorcheck__
rszvb_ConfigureMesurementParameters.output = False
# rszvb_QueryMesurementParameters ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 bufferSize', 'ViChar _VI_FAR parameters[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'bufferSize'),(1, 'parameters[]'),)
rszvb_QueryMesurementParameters  = prototype(('rszvb_QueryMesurementParameters', rszvbDLL), paramflags)
rszvb_QueryMesurementParameters.name = 'rszvb_QueryMesurementParameters'
rszvb_QueryMesurementParameters.errcheck = __errorcheck__
rszvb_QueryMesurementParameters.output = False
# rszvb_SetTraceFormat ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 format']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'format'),)
rszvb_SetTraceFormat  = prototype(('rszvb_SetTraceFormat', rszvbDLL), paramflags)
rszvb_SetTraceFormat.name = 'rszvb_SetTraceFormat'
rszvb_SetTraceFormat.errcheck = __errorcheck__
rszvb_SetTraceFormat.output = False
# rszvb_GetTraceFormat ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* format']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'format'),)
rszvb_GetTraceFormat  = prototype(('rszvb_GetTraceFormat', rszvbDLL), paramflags)
rszvb_GetTraceFormat.name = 'rszvb_GetTraceFormat'
rszvb_GetTraceFormat.errcheck = __errorcheck__
rszvb_GetTraceFormat.output = True
# rszvb_SetTraceUnit ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 format']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'format'),)
rszvb_SetTraceUnit  = prototype(('rszvb_SetTraceUnit', rszvbDLL), paramflags)
rszvb_SetTraceUnit.name = 'rszvb_SetTraceUnit'
rszvb_SetTraceUnit.errcheck = __errorcheck__
rszvb_SetTraceUnit.output = False
# rszvb_GetTraceUnit ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* format']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'format'),)
rszvb_GetTraceUnit  = prototype(('rszvb_GetTraceUnit', rszvbDLL), paramflags)
rszvb_GetTraceUnit.name = 'rszvb_GetTraceUnit'
rszvb_GetTraceUnit.errcheck = __errorcheck__
rszvb_GetTraceUnit.output = True
# rszvb_SetApertureGroupDelaySteps ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 steps']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'steps'),)
rszvb_SetApertureGroupDelaySteps  = prototype(('rszvb_SetApertureGroupDelaySteps', rszvbDLL), paramflags)
rszvb_SetApertureGroupDelaySteps.name = 'rszvb_SetApertureGroupDelaySteps'
rszvb_SetApertureGroupDelaySteps.errcheck = __errorcheck__
rszvb_SetApertureGroupDelaySteps.output = False
# rszvb_GetApertureGroupDelaySteps ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* steps']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'steps'),)
rszvb_GetApertureGroupDelaySteps  = prototype(('rszvb_GetApertureGroupDelaySteps', rszvbDLL), paramflags)
rszvb_GetApertureGroupDelaySteps.name = 'rszvb_GetApertureGroupDelaySteps'
rszvb_GetApertureGroupDelaySteps.errcheck = __errorcheck__
rszvb_GetApertureGroupDelaySteps.output = True
# rszvb_TraceAutoscale ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),)
rszvb_TraceAutoscale  = prototype(('rszvb_TraceAutoscale', rszvbDLL), paramflags)
rszvb_TraceAutoscale.name = 'rszvb_TraceAutoscale'
rszvb_TraceAutoscale.errcheck = __errorcheck__
rszvb_TraceAutoscale.output = False
# rszvb_TraceAutoscaleByName ['ViSession instrumentHandle', 'ViInt32 window', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'traceName'),)
rszvb_TraceAutoscaleByName  = prototype(('rszvb_TraceAutoscaleByName', rszvbDLL), paramflags)
rszvb_TraceAutoscaleByName.name = 'rszvb_TraceAutoscaleByName'
rszvb_TraceAutoscaleByName.errcheck = __errorcheck__
rszvb_TraceAutoscaleByName.output = False
# rszvb_SetTraceBottom ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64 bottom']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'bottom'),)
rszvb_SetTraceBottom  = prototype(('rszvb_SetTraceBottom', rszvbDLL), paramflags)
rszvb_SetTraceBottom.name = 'rszvb_SetTraceBottom'
rszvb_SetTraceBottom.errcheck = __errorcheck__
rszvb_SetTraceBottom.output = False
# rszvb_GetTraceBottom ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64* bottom']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(2, 'bottom'),)
rszvb_GetTraceBottom  = prototype(('rszvb_GetTraceBottom', rszvbDLL), paramflags)
rszvb_GetTraceBottom.name = 'rszvb_GetTraceBottom'
rszvb_GetTraceBottom.errcheck = __errorcheck__
rszvb_GetTraceBottom.output = True
# rszvb_SetTraceScaleDivisions ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64 scaleDivisions']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'scaleDivisions'),)
rszvb_SetTraceScaleDivisions  = prototype(('rszvb_SetTraceScaleDivisions', rszvbDLL), paramflags)
rszvb_SetTraceScaleDivisions.name = 'rszvb_SetTraceScaleDivisions'
rszvb_SetTraceScaleDivisions.errcheck = __errorcheck__
rszvb_SetTraceScaleDivisions.output = False
# rszvb_SetTraceScaleDivisionsByName ['ViSession instrumentHandle', 'ViInt32 window', 'ViReal64 scaleDivisions', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'scaleDivisions'),(1, 'traceName'),)
rszvb_SetTraceScaleDivisionsByName  = prototype(('rszvb_SetTraceScaleDivisionsByName', rszvbDLL), paramflags)
rszvb_SetTraceScaleDivisionsByName.name = 'rszvb_SetTraceScaleDivisionsByName'
rszvb_SetTraceScaleDivisionsByName.errcheck = __errorcheck__
rszvb_SetTraceScaleDivisionsByName.output = False
# rszvb_GetTraceScaleDivisions ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64* scaleDivisions']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(2, 'scaleDivisions'),)
rszvb_GetTraceScaleDivisions  = prototype(('rszvb_GetTraceScaleDivisions', rszvbDLL), paramflags)
rszvb_GetTraceScaleDivisions.name = 'rszvb_GetTraceScaleDivisions'
rszvb_GetTraceScaleDivisions.errcheck = __errorcheck__
rszvb_GetTraceScaleDivisions.output = True
# rszvb_SetTraceRefValue ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64 referenceLevel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'referenceLevel'),)
rszvb_SetTraceRefValue  = prototype(('rszvb_SetTraceRefValue', rszvbDLL), paramflags)
rszvb_SetTraceRefValue.name = 'rszvb_SetTraceRefValue'
rszvb_SetTraceRefValue.errcheck = __errorcheck__
rszvb_SetTraceRefValue.output = False
# rszvb_SetTraceRefValueByName ['ViSession instrumentHandle', 'ViInt32 window', 'ViReal64 referenceLevel', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'referenceLevel'),(1, 'traceName'),)
rszvb_SetTraceRefValueByName  = prototype(('rszvb_SetTraceRefValueByName', rszvbDLL), paramflags)
rszvb_SetTraceRefValueByName.name = 'rszvb_SetTraceRefValueByName'
rszvb_SetTraceRefValueByName.errcheck = __errorcheck__
rszvb_SetTraceRefValueByName.output = False
# rszvb_GetTraceRefValue ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64* referenceLevel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(2, 'referenceLevel'),)
rszvb_GetTraceRefValue  = prototype(('rszvb_GetTraceRefValue', rszvbDLL), paramflags)
rszvb_GetTraceRefValue.name = 'rszvb_GetTraceRefValue'
rszvb_GetTraceRefValue.errcheck = __errorcheck__
rszvb_GetTraceRefValue.output = True
# rszvb_SetTraceRefPosition ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64 referencePosition']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'referencePosition'),)
rszvb_SetTraceRefPosition  = prototype(('rszvb_SetTraceRefPosition', rszvbDLL), paramflags)
rszvb_SetTraceRefPosition.name = 'rszvb_SetTraceRefPosition'
rszvb_SetTraceRefPosition.errcheck = __errorcheck__
rszvb_SetTraceRefPosition.output = False
# rszvb_SetTraceRefPositionByName ['ViSession instrumentHandle', 'ViInt32 window', 'ViReal64 referencePosition', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'referencePosition'),(1, 'traceName'),)
rszvb_SetTraceRefPositionByName  = prototype(('rszvb_SetTraceRefPositionByName', rszvbDLL), paramflags)
rszvb_SetTraceRefPositionByName.name = 'rszvb_SetTraceRefPositionByName'
rszvb_SetTraceRefPositionByName.errcheck = __errorcheck__
rszvb_SetTraceRefPositionByName.output = False
# rszvb_GetTraceRefPosition ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64* referencePosition']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(2, 'referencePosition'),)
rszvb_GetTraceRefPosition  = prototype(('rszvb_GetTraceRefPosition', rszvbDLL), paramflags)
rszvb_GetTraceRefPosition.name = 'rszvb_GetTraceRefPosition'
rszvb_GetTraceRefPosition.errcheck = __errorcheck__
rszvb_GetTraceRefPosition.output = True
# rszvb_SetTraceTop ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64 top']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'top'),)
rszvb_SetTraceTop  = prototype(('rszvb_SetTraceTop', rszvbDLL), paramflags)
rszvb_SetTraceTop.name = 'rszvb_SetTraceTop'
rszvb_SetTraceTop.errcheck = __errorcheck__
rszvb_SetTraceTop.output = False
# rszvb_GetTraceTop ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64* top']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(2, 'top'),)
rszvb_GetTraceTop  = prototype(('rszvb_GetTraceTop', rszvbDLL), paramflags)
rszvb_GetTraceTop.name = 'rszvb_GetTraceTop'
rszvb_GetTraceTop.errcheck = __errorcheck__
rszvb_GetTraceTop.output = True
# rszvb_TraceAdd ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),)
rszvb_TraceAdd  = prototype(('rszvb_TraceAdd', rszvbDLL), paramflags)
rszvb_TraceAdd.name = 'rszvb_TraceAdd'
rszvb_TraceAdd.errcheck = __errorcheck__
rszvb_TraceAdd.output = False
# rszvb_TraceAddMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName', 'ViInt32 outMode', 'ViInt32 inMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),(1, 'outMode'),(1, 'inMode'),)
rszvb_TraceAddMode  = prototype(('rszvb_TraceAddMode', rszvbDLL), paramflags)
rszvb_TraceAddMode.name = 'rszvb_TraceAddMode'
rszvb_TraceAddMode.errcheck = __errorcheck__
rszvb_TraceAddMode.output = False
# rszvb_SetTraceDisplayState ['ViSession instrumentHandle', 'ViInt32 traceType', 'ViString singleTraceName', 'ViBoolean showTrace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'traceType'),(1, 'singleTraceName'),(1, 'showTrace'),)
rszvb_SetTraceDisplayState  = prototype(('rszvb_SetTraceDisplayState', rszvbDLL), paramflags)
rszvb_SetTraceDisplayState.name = 'rszvb_SetTraceDisplayState'
rszvb_SetTraceDisplayState.errcheck = __errorcheck__
rszvb_SetTraceDisplayState.output = False
# rszvb_GetTraceDisplayState ['ViSession instrumentHandle', 'ViInt32 traceType', 'ViString singleTraceName', 'ViBoolean* showTrace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'traceType'),(1, 'singleTraceName'),(2, 'showTrace'),)
rszvb_GetTraceDisplayState  = prototype(('rszvb_GetTraceDisplayState', rszvbDLL), paramflags)
rszvb_GetTraceDisplayState.name = 'rszvb_GetTraceDisplayState'
rszvb_GetTraceDisplayState.errcheck = __errorcheck__
rszvb_GetTraceDisplayState.output = True
# rszvb_TraceAddSParameterGroup ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 numberOfLogicalPortNumbers', 'ViInt32 _VI_FAR logicalPortNumber_s[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'numberOfLogicalPortNumbers'),(1, 'logicalPortNumber_s[]'),)
rszvb_TraceAddSParameterGroup  = prototype(('rszvb_TraceAddSParameterGroup', rszvbDLL), paramflags)
rszvb_TraceAddSParameterGroup.name = 'rszvb_TraceAddSParameterGroup'
rszvb_TraceAddSParameterGroup.errcheck = __errorcheck__
rszvb_TraceAddSParameterGroup.output = False
# rszvb_QueryTraceAddSParameterGroup ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 _VI_FAR logicalPortNumber_s[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'logicalPortNumber_s[]'),)
rszvb_QueryTraceAddSParameterGroup  = prototype(('rszvb_QueryTraceAddSParameterGroup', rszvbDLL), paramflags)
rszvb_QueryTraceAddSParameterGroup.name = 'rszvb_QueryTraceAddSParameterGroup'
rszvb_QueryTraceAddSParameterGroup.errcheck = __errorcheck__
rszvb_QueryTraceAddSParameterGroup.output = False
# rszvb_TraceAddDiagramArea ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViInt32 channel', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'channel',1),(1, 'traceName'),)
rszvb_TraceAddDiagramArea  = prototype(('rszvb_TraceAddDiagramArea', rszvbDLL), paramflags)
rszvb_TraceAddDiagramArea.name = 'rszvb_TraceAddDiagramArea'
rszvb_TraceAddDiagramArea.errcheck = __errorcheck__
rszvb_TraceAddDiagramArea.output = False
# rszvb_TraceAssignDiagramArea ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'traceName'),)
rszvb_TraceAssignDiagramArea  = prototype(('rszvb_TraceAssignDiagramArea', rszvbDLL), paramflags)
rszvb_TraceAssignDiagramArea.name = 'rszvb_TraceAssignDiagramArea'
rszvb_TraceAssignDiagramArea.errcheck = __errorcheck__
rszvb_TraceAssignDiagramArea.output = False
# rszvb_TraceAssignWindowDiagramArea ['ViSession instrumentHandle', 'ViInt32 window', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'traceName'),)
rszvb_TraceAssignWindowDiagramArea  = prototype(('rszvb_TraceAssignWindowDiagramArea', rszvbDLL), paramflags)
rszvb_TraceAssignWindowDiagramArea.name = 'rszvb_TraceAssignWindowDiagramArea'
rszvb_TraceAssignWindowDiagramArea.errcheck = __errorcheck__
rszvb_TraceAssignWindowDiagramArea.output = False
# rszvb_TraceUnassignDiagramArea ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),)
rszvb_TraceUnassignDiagramArea  = prototype(('rszvb_TraceUnassignDiagramArea', rszvbDLL), paramflags)
rszvb_TraceUnassignDiagramArea.name = 'rszvb_TraceUnassignDiagramArea'
rszvb_TraceUnassignDiagramArea.errcheck = __errorcheck__
rszvb_TraceUnassignDiagramArea.output = False
# rszvb_TraceSelect ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),)
rszvb_TraceSelect  = prototype(('rszvb_TraceSelect', rszvbDLL), paramflags)
rszvb_TraceSelect.name = 'rszvb_TraceSelect'
rszvb_TraceSelect.errcheck = __errorcheck__
rszvb_TraceSelect.output = False
# rszvb_TraceDelete ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),)
rszvb_TraceDelete  = prototype(('rszvb_TraceDelete', rszvbDLL), paramflags)
rszvb_TraceDelete.name = 'rszvb_TraceDelete'
rszvb_TraceDelete.errcheck = __errorcheck__
rszvb_TraceDelete.output = False
# rszvb_TraceDeleteAll ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_TraceDeleteAll  = prototype(('rszvb_TraceDeleteAll', rszvbDLL), paramflags)
rszvb_TraceDeleteAll.name = 'rszvb_TraceDeleteAll'
rszvb_TraceDeleteAll.errcheck = __errorcheck__
rszvb_TraceDeleteAll.output = False
# rszvb_TraceDeleteAllChannels ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_TraceDeleteAllChannels  = prototype(('rszvb_TraceDeleteAllChannels', rszvbDLL), paramflags)
rszvb_TraceDeleteAllChannels.name = 'rszvb_TraceDeleteAllChannels'
rszvb_TraceDeleteAllChannels.errcheck = __errorcheck__
rszvb_TraceDeleteAllChannels.output = False
# rszvb_TraceList ['ViSession instrumentHandle', 'ViInt32 channel', 'ViChar _VI_FAR catalog[]', 'ViInt32 bufferSize']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'catalog[]'),(1, 'bufferSize'),)
rszvb_TraceList  = prototype(('rszvb_TraceList', rszvbDLL), paramflags)
rszvb_TraceList.name = 'rszvb_TraceList'
rszvb_TraceList.errcheck = __errorcheck__
rszvb_TraceList.output = False
# rszvb_TraceRename ['ViSession instrumentHandle', 'ViString oldTraceName', 'ViString newTraceName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'oldTraceName'),(1, 'newTraceName'),)
rszvb_TraceRename  = prototype(('rszvb_TraceRename', rszvbDLL), paramflags)
rszvb_TraceRename.name = 'rszvb_TraceRename'
rszvb_TraceRename.errcheck = __errorcheck__
rszvb_TraceRename.output = False
# rszvb_ChannelTraceRename ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),)
rszvb_ChannelTraceRename  = prototype(('rszvb_ChannelTraceRename', rszvbDLL), paramflags)
rszvb_ChannelTraceRename.name = 'rszvb_ChannelTraceRename'
rszvb_ChannelTraceRename.errcheck = __errorcheck__
rszvb_ChannelTraceRename.output = False
# rszvb_TraceListCatalog ['ViSession instrumentHandle', 'ViChar _VI_FAR catalog[]', 'ViInt32 bufferSize']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'catalog[]'),(1, 'bufferSize'),)
rszvb_TraceListCatalog  = prototype(('rszvb_TraceListCatalog', rszvbDLL), paramflags)
rszvb_TraceListCatalog.name = 'rszvb_TraceListCatalog'
rszvb_TraceListCatalog.errcheck = __errorcheck__
rszvb_TraceListCatalog.output = False
# rszvb_TraceGetTraceName ['ViSession instrumentHandle', 'ViInt32 traceNumber', 'ViChar _VI_FAR traceName[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'traceNumber'),(1, 'traceName[]'),)
rszvb_TraceGetTraceName  = prototype(('rszvb_TraceGetTraceName', rszvbDLL), paramflags)
rszvb_TraceGetTraceName.name = 'rszvb_TraceGetTraceName'
rszvb_TraceGetTraceName.errcheck = __errorcheck__
rszvb_TraceGetTraceName.output = False
# rszvb_TraceGetTraceNumber ['ViSession instrumentHandle', 'ViString traceName', 'ViInt32* traceNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(2, 'traceNumber'),)
rszvb_TraceGetTraceNumber  = prototype(('rszvb_TraceGetTraceNumber', rszvbDLL), paramflags)
rszvb_TraceGetTraceNumber.name = 'rszvb_TraceGetTraceNumber'
rszvb_TraceGetTraceNumber.errcheck = __errorcheck__
rszvb_TraceGetTraceNumber.output = True
# rszvb_TraceGetChannelName ['ViSession instrumentHandle', 'ViString traceName', 'ViChar _VI_FAR channelName[]']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(1, 'channelName[]'),)
rszvb_TraceGetChannelName  = prototype(('rszvb_TraceGetChannelName', rszvbDLL), paramflags)
rszvb_TraceGetChannelName.name = 'rszvb_TraceGetChannelName'
rszvb_TraceGetChannelName.errcheck = __errorcheck__
rszvb_TraceGetChannelName.output = False
# rszvb_TraceGetChannelNumber ['ViSession instrumentHandle', 'ViString traceName', 'ViInt32* channelNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(2, 'channelNumber'),)
rszvb_TraceGetChannelNumber  = prototype(('rszvb_TraceGetChannelNumber', rszvbDLL), paramflags)
rszvb_TraceGetChannelNumber.name = 'rszvb_TraceGetChannelNumber'
rszvb_TraceGetChannelNumber.errcheck = __errorcheck__
rszvb_TraceGetChannelNumber.output = True
# rszvb_TraceDataToMemory ['ViSession instrumentHandle', 'ViInt32 channel_Trace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),)
rszvb_TraceDataToMemory  = prototype(('rszvb_TraceDataToMemory', rszvbDLL), paramflags)
rszvb_TraceDataToMemory.name = 'rszvb_TraceDataToMemory'
rszvb_TraceDataToMemory.errcheck = __errorcheck__
rszvb_TraceDataToMemory.output = False
# rszvb_TraceDataToMemoryTrace ['ViSession instrumentHandle', 'ViString memoryTrace', 'ViString dataTrace']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'memoryTrace'),(1, 'dataTrace'),)
rszvb_TraceDataToMemoryTrace  = prototype(('rszvb_TraceDataToMemoryTrace', rszvbDLL), paramflags)
rszvb_TraceDataToMemoryTrace.name = 'rszvb_TraceDataToMemoryTrace'
rszvb_TraceDataToMemoryTrace.errcheck = __errorcheck__
rszvb_TraceDataToMemoryTrace.output = False
# rszvb_TraceMathToMemoryTrace ['ViSession instrumentHandle', 'ViString memoryTrace', 'ViString dataTrace']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'memoryTrace'),(1, 'dataTrace'),)
rszvb_TraceMathToMemoryTrace  = prototype(('rszvb_TraceMathToMemoryTrace', rszvbDLL), paramflags)
rszvb_TraceMathToMemoryTrace.name = 'rszvb_TraceMathToMemoryTrace'
rszvb_TraceMathToMemoryTrace.errcheck = __errorcheck__
rszvb_TraceMathToMemoryTrace.output = False
# rszvb_DeleteMemoryTrace ['ViSession instrumentHandle', 'ViInt32 memoryTrace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'memoryTrace'),)
rszvb_DeleteMemoryTrace  = prototype(('rszvb_DeleteMemoryTrace', rszvbDLL), paramflags)
rszvb_DeleteMemoryTrace.name = 'rszvb_DeleteMemoryTrace'
rszvb_DeleteMemoryTrace.errcheck = __errorcheck__
rszvb_DeleteMemoryTrace.output = False
# rszvb_TraceUserDefinedMath ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViString mathematicalExpression']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'mathematicalExpression'),)
rszvb_TraceUserDefinedMath  = prototype(('rszvb_TraceUserDefinedMath', rszvbDLL), paramflags)
rszvb_TraceUserDefinedMath.name = 'rszvb_TraceUserDefinedMath'
rszvb_TraceUserDefinedMath.errcheck = __errorcheck__
rszvb_TraceUserDefinedMath.output = False
# rszvb_SetTraceMathState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean mathState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'mathState'),)
rszvb_SetTraceMathState  = prototype(('rszvb_SetTraceMathState', rszvbDLL), paramflags)
rszvb_SetTraceMathState.name = 'rszvb_SetTraceMathState'
rszvb_SetTraceMathState.errcheck = __errorcheck__
rszvb_SetTraceMathState.output = False
# rszvb_GetTraceMathState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* mathState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'mathState'),)
rszvb_GetTraceMathState  = prototype(('rszvb_GetTraceMathState', rszvbDLL), paramflags)
rszvb_GetTraceMathState.name = 'rszvb_GetTraceMathState'
rszvb_GetTraceMathState.errcheck = __errorcheck__
rszvb_GetTraceMathState.output = True
# rszvb_SetTraceMathFunction ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 mathematicalFunction']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'mathematicalFunction'),)
rszvb_SetTraceMathFunction  = prototype(('rszvb_SetTraceMathFunction', rszvbDLL), paramflags)
rszvb_SetTraceMathFunction.name = 'rszvb_SetTraceMathFunction'
rszvb_SetTraceMathFunction.errcheck = __errorcheck__
rszvb_SetTraceMathFunction.output = False
# rszvb_GetTraceMathFunction ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* mathematicalFunction']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'mathematicalFunction'),)
rszvb_GetTraceMathFunction  = prototype(('rszvb_GetTraceMathFunction', rszvbDLL), paramflags)
rszvb_GetTraceMathFunction.name = 'rszvb_GetTraceMathFunction'
rszvb_GetTraceMathFunction.errcheck = __errorcheck__
rszvb_GetTraceMathFunction.output = True
# rszvb_SetTraceMathWaveQuantityState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean mathWaveQuantityState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'mathWaveQuantityState'),)
rszvb_SetTraceMathWaveQuantityState  = prototype(('rszvb_SetTraceMathWaveQuantityState', rszvbDLL), paramflags)
rszvb_SetTraceMathWaveQuantityState.name = 'rszvb_SetTraceMathWaveQuantityState'
rszvb_SetTraceMathWaveQuantityState.errcheck = __errorcheck__
rszvb_SetTraceMathWaveQuantityState.output = False
# rszvb_GetTraceMathWaveQuantityState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* mathWaveQuantityState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'mathWaveQuantityState'),)
rszvb_GetTraceMathWaveQuantityState  = prototype(('rszvb_GetTraceMathWaveQuantityState', rszvbDLL), paramflags)
rszvb_GetTraceMathWaveQuantityState.name = 'rszvb_GetTraceMathWaveQuantityState'
rszvb_GetTraceMathWaveQuantityState.errcheck = __errorcheck__
rszvb_GetTraceMathWaveQuantityState.output = True
# rszvb_SetTraceTransformDomain ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 transformDomain']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'transformDomain'),)
rszvb_SetTraceTransformDomain  = prototype(('rszvb_SetTraceTransformDomain', rszvbDLL), paramflags)
rszvb_SetTraceTransformDomain.name = 'rszvb_SetTraceTransformDomain'
rszvb_SetTraceTransformDomain.errcheck = __errorcheck__
rszvb_SetTraceTransformDomain.output = False
# rszvb_GetTraceTransformDomain ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* transformDomain']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'transformDomain'),)
rszvb_GetTraceTransformDomain  = prototype(('rszvb_GetTraceTransformDomain', rszvbDLL), paramflags)
rszvb_GetTraceTransformDomain.name = 'rszvb_GetTraceTransformDomain'
rszvb_GetTraceTransformDomain.errcheck = __errorcheck__
rszvb_GetTraceTransformDomain.output = True
# rszvb_SetTraceTransformConversion ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 conversion']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'conversion'),)
rszvb_SetTraceTransformConversion  = prototype(('rszvb_SetTraceTransformConversion', rszvbDLL), paramflags)
rszvb_SetTraceTransformConversion.name = 'rszvb_SetTraceTransformConversion'
rszvb_SetTraceTransformConversion.errcheck = __errorcheck__
rszvb_SetTraceTransformConversion.output = False
# rszvb_GetTraceTransformConversion ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* conversion']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'conversion'),)
rszvb_GetTraceTransformConversion  = prototype(('rszvb_GetTraceTransformConversion', rszvbDLL), paramflags)
rszvb_GetTraceTransformConversion.name = 'rszvb_GetTraceTransformConversion'
rszvb_GetTraceTransformConversion.errcheck = __errorcheck__
rszvb_GetTraceTransformConversion.output = True
# rszvb_SetTimeDomainStartTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 startTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'startTime'),)
rszvb_SetTimeDomainStartTime  = prototype(('rszvb_SetTimeDomainStartTime', rszvbDLL), paramflags)
rszvb_SetTimeDomainStartTime.name = 'rszvb_SetTimeDomainStartTime'
rszvb_SetTimeDomainStartTime.errcheck = __errorcheck__
rszvb_SetTimeDomainStartTime.output = False
# rszvb_GetTimeDomainStartTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* startTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'startTime'),)
rszvb_GetTimeDomainStartTime  = prototype(('rszvb_GetTimeDomainStartTime', rszvbDLL), paramflags)
rszvb_GetTimeDomainStartTime.name = 'rszvb_GetTimeDomainStartTime'
rszvb_GetTimeDomainStartTime.errcheck = __errorcheck__
rszvb_GetTimeDomainStartTime.output = True
# rszvb_SetTimeDomainStopTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 stopTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'stopTime'),)
rszvb_SetTimeDomainStopTime  = prototype(('rszvb_SetTimeDomainStopTime', rszvbDLL), paramflags)
rszvb_SetTimeDomainStopTime.name = 'rszvb_SetTimeDomainStopTime'
rszvb_SetTimeDomainStopTime.errcheck = __errorcheck__
rszvb_SetTimeDomainStopTime.output = False
# rszvb_GetTimeDomainStopTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* stopTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'stopTime'),)
rszvb_GetTimeDomainStopTime  = prototype(('rszvb_GetTimeDomainStopTime', rszvbDLL), paramflags)
rszvb_GetTimeDomainStopTime.name = 'rszvb_GetTimeDomainStopTime'
rszvb_GetTimeDomainStopTime.errcheck = __errorcheck__
rszvb_GetTimeDomainStopTime.output = True
# rszvb_SetTimeDomainCenterTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 centerTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'centerTime'),)
rszvb_SetTimeDomainCenterTime  = prototype(('rszvb_SetTimeDomainCenterTime', rszvbDLL), paramflags)
rszvb_SetTimeDomainCenterTime.name = 'rszvb_SetTimeDomainCenterTime'
rszvb_SetTimeDomainCenterTime.errcheck = __errorcheck__
rszvb_SetTimeDomainCenterTime.output = False
# rszvb_GetTimeDomainCenterTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* centerTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'centerTime'),)
rszvb_GetTimeDomainCenterTime  = prototype(('rszvb_GetTimeDomainCenterTime', rszvbDLL), paramflags)
rszvb_GetTimeDomainCenterTime.name = 'rszvb_GetTimeDomainCenterTime'
rszvb_GetTimeDomainCenterTime.errcheck = __errorcheck__
rszvb_GetTimeDomainCenterTime.output = True
# rszvb_SetTimeDomainTimeSpan ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 timeSpan']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'timeSpan'),)
rszvb_SetTimeDomainTimeSpan  = prototype(('rszvb_SetTimeDomainTimeSpan', rszvbDLL), paramflags)
rszvb_SetTimeDomainTimeSpan.name = 'rszvb_SetTimeDomainTimeSpan'
rszvb_SetTimeDomainTimeSpan.errcheck = __errorcheck__
rszvb_SetTimeDomainTimeSpan.output = False
# rszvb_GetTimeDomainTimeSpan ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* timeSpan']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'timeSpan'),)
rszvb_GetTimeDomainTimeSpan  = prototype(('rszvb_GetTimeDomainTimeSpan', rszvbDLL), paramflags)
rszvb_GetTimeDomainTimeSpan.name = 'rszvb_GetTimeDomainTimeSpan'
rszvb_GetTimeDomainTimeSpan.errcheck = __errorcheck__
rszvb_GetTimeDomainTimeSpan.output = True
# rszvb_SetTimeDomainTimeAxisScaling ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 timeAxisScaling']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'timeAxisScaling'),)
rszvb_SetTimeDomainTimeAxisScaling  = prototype(('rszvb_SetTimeDomainTimeAxisScaling', rszvbDLL), paramflags)
rszvb_SetTimeDomainTimeAxisScaling.name = 'rszvb_SetTimeDomainTimeAxisScaling'
rszvb_SetTimeDomainTimeAxisScaling.errcheck = __errorcheck__
rszvb_SetTimeDomainTimeAxisScaling.output = False
# rszvb_GetTimeDomainTimeAxisScaling ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* timeAxisScaling']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'timeAxisScaling'),)
rszvb_GetTimeDomainTimeAxisScaling  = prototype(('rszvb_GetTimeDomainTimeAxisScaling', rszvbDLL), paramflags)
rszvb_GetTimeDomainTimeAxisScaling.name = 'rszvb_GetTimeDomainTimeAxisScaling'
rszvb_GetTimeDomainTimeAxisScaling.errcheck = __errorcheck__
rszvb_GetTimeDomainTimeAxisScaling.output = True
# rszvb_SetTimeDomainTransformationType ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 transformationType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'transformationType'),)
rszvb_SetTimeDomainTransformationType  = prototype(('rszvb_SetTimeDomainTransformationType', rszvbDLL), paramflags)
rszvb_SetTimeDomainTransformationType.name = 'rszvb_SetTimeDomainTransformationType'
rszvb_SetTimeDomainTransformationType.errcheck = __errorcheck__
rszvb_SetTimeDomainTransformationType.output = False
# rszvb_GetTimeDomainTransformationType ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* transformationType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'transformationType'),)
rszvb_GetTimeDomainTransformationType  = prototype(('rszvb_GetTimeDomainTransformationType', rszvbDLL), paramflags)
rszvb_GetTimeDomainTransformationType.name = 'rszvb_GetTimeDomainTransformationType'
rszvb_GetTimeDomainTransformationType.errcheck = __errorcheck__
rszvb_GetTimeDomainTransformationType.output = True
# rszvb_SetTimeDomainTransformationFilter ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 filterType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'filterType'),)
rszvb_SetTimeDomainTransformationFilter  = prototype(('rszvb_SetTimeDomainTransformationFilter', rszvbDLL), paramflags)
rszvb_SetTimeDomainTransformationFilter.name = 'rszvb_SetTimeDomainTransformationFilter'
rszvb_SetTimeDomainTransformationFilter.errcheck = __errorcheck__
rszvb_SetTimeDomainTransformationFilter.output = False
# rszvb_GetTimeDomainTransformationFilter ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* filterType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'filterType'),)
rszvb_GetTimeDomainTransformationFilter  = prototype(('rszvb_GetTimeDomainTransformationFilter', rszvbDLL), paramflags)
rszvb_GetTimeDomainTransformationFilter.name = 'rszvb_GetTimeDomainTransformationFilter'
rszvb_GetTimeDomainTransformationFilter.errcheck = __errorcheck__
rszvb_GetTimeDomainTransformationFilter.output = True
# rszvb_SetTimeDomainTransformationSidebandSuppression ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 sidebandSuppression']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'sidebandSuppression'),)
rszvb_SetTimeDomainTransformationSidebandSuppression  = prototype(('rszvb_SetTimeDomainTransformationSidebandSuppression', rszvbDLL), paramflags)
rszvb_SetTimeDomainTransformationSidebandSuppression.name = 'rszvb_SetTimeDomainTransformationSidebandSuppression'
rszvb_SetTimeDomainTransformationSidebandSuppression.errcheck = __errorcheck__
rszvb_SetTimeDomainTransformationSidebandSuppression.output = False
# rszvb_GetTimeDomainTransformationSidebandSuppression ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* sidebandSuppression']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'sidebandSuppression'),)
rszvb_GetTimeDomainTransformationSidebandSuppression  = prototype(('rszvb_GetTimeDomainTransformationSidebandSuppression', rszvbDLL), paramflags)
rszvb_GetTimeDomainTransformationSidebandSuppression.name = 'rszvb_GetTimeDomainTransformationSidebandSuppression'
rszvb_GetTimeDomainTransformationSidebandSuppression.errcheck = __errorcheck__
rszvb_GetTimeDomainTransformationSidebandSuppression.output = True
# rszvb_SetTimeDomainTransformationResolutionEfactor ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 resolution']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'resolution'),)
rszvb_SetTimeDomainTransformationResolutionEfactor  = prototype(('rszvb_SetTimeDomainTransformationResolutionEfactor', rszvbDLL), paramflags)
rszvb_SetTimeDomainTransformationResolutionEfactor.name = 'rszvb_SetTimeDomainTransformationResolutionEfactor'
rszvb_SetTimeDomainTransformationResolutionEfactor.errcheck = __errorcheck__
rszvb_SetTimeDomainTransformationResolutionEfactor.output = False
# rszvb_GetTimeDomainTransformationResolutionEfactor ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* resolution']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'resolution'),)
rszvb_GetTimeDomainTransformationResolutionEfactor  = prototype(('rszvb_GetTimeDomainTransformationResolutionEfactor', rszvbDLL), paramflags)
rszvb_GetTimeDomainTransformationResolutionEfactor.name = 'rszvb_GetTimeDomainTransformationResolutionEfactor'
rszvb_GetTimeDomainTransformationResolutionEfactor.errcheck = __errorcheck__
rszvb_GetTimeDomainTransformationResolutionEfactor.output = True
# rszvb_SetHarmonicGridAndKeep ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 calculationMethod']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'calculationMethod'),)
rszvb_SetHarmonicGridAndKeep  = prototype(('rszvb_SetHarmonicGridAndKeep', rszvbDLL), paramflags)
rszvb_SetHarmonicGridAndKeep.name = 'rszvb_SetHarmonicGridAndKeep'
rszvb_SetHarmonicGridAndKeep.errcheck = __errorcheck__
rszvb_SetHarmonicGridAndKeep.output = False
# rszvb_SetDCValue ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 DCValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'DCValue'),)
rszvb_SetDCValue  = prototype(('rszvb_SetDCValue', rszvbDLL), paramflags)
rszvb_SetDCValue.name = 'rszvb_SetDCValue'
rszvb_SetDCValue.errcheck = __errorcheck__
rszvb_SetDCValue.output = False
# rszvb_GetDCValue ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* DCValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'DCValue'),)
rszvb_GetDCValue  = prototype(('rszvb_GetDCValue', rszvbDLL), paramflags)
rszvb_GetDCValue.name = 'rszvb_GetDCValue'
rszvb_GetDCValue.errcheck = __errorcheck__
rszvb_GetDCValue.output = True
# rszvb_ExtrapolateDCValue ['ViSession instrumentHandle', 'ViInt32 channel_Trace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),)
rszvb_ExtrapolateDCValue  = prototype(('rszvb_ExtrapolateDCValue', rszvbDLL), paramflags)
rszvb_ExtrapolateDCValue.name = 'rszvb_ExtrapolateDCValue'
rszvb_ExtrapolateDCValue.errcheck = __errorcheck__
rszvb_ExtrapolateDCValue.output = False
# rszvb_SetContinuousExtrapolation ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean continuousExtrapolation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'continuousExtrapolation'),)
rszvb_SetContinuousExtrapolation  = prototype(('rszvb_SetContinuousExtrapolation', rszvbDLL), paramflags)
rszvb_SetContinuousExtrapolation.name = 'rszvb_SetContinuousExtrapolation'
rszvb_SetContinuousExtrapolation.errcheck = __errorcheck__
rszvb_SetContinuousExtrapolation.output = False
# rszvb_GetContinuousExtrapolation ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* continuousExtrapolation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'continuousExtrapolation'),)
rszvb_GetContinuousExtrapolation  = prototype(('rszvb_GetContinuousExtrapolation', rszvbDLL), paramflags)
rszvb_GetContinuousExtrapolation.name = 'rszvb_GetContinuousExtrapolation'
rszvb_GetContinuousExtrapolation.errcheck = __errorcheck__
rszvb_GetContinuousExtrapolation.output = True
# rszvb_CalculateHarmonicGrid ['ViSession instrumentHandle', 'ViInt32 channel_Trace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),)
rszvb_CalculateHarmonicGrid  = prototype(('rszvb_CalculateHarmonicGrid', rszvbDLL), paramflags)
rszvb_CalculateHarmonicGrid.name = 'rszvb_CalculateHarmonicGrid'
rszvb_CalculateHarmonicGrid.errcheck = __errorcheck__
rszvb_CalculateHarmonicGrid.output = False
# rszvb_SetTimeGateState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean timeGate']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'timeGate'),)
rszvb_SetTimeGateState  = prototype(('rszvb_SetTimeGateState', rszvbDLL), paramflags)
rszvb_SetTimeGateState.name = 'rszvb_SetTimeGateState'
rszvb_SetTimeGateState.errcheck = __errorcheck__
rszvb_SetTimeGateState.output = False
# rszvb_GetTimeGateState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* timeGate']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'timeGate'),)
rszvb_GetTimeGateState  = prototype(('rszvb_GetTimeGateState', rszvbDLL), paramflags)
rszvb_GetTimeGateState.name = 'rszvb_GetTimeGateState'
rszvb_GetTimeGateState.errcheck = __errorcheck__
rszvb_GetTimeGateState.output = True
# rszvb_SetTimeGateStartTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 startTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'startTime'),)
rszvb_SetTimeGateStartTime  = prototype(('rszvb_SetTimeGateStartTime', rszvbDLL), paramflags)
rszvb_SetTimeGateStartTime.name = 'rszvb_SetTimeGateStartTime'
rszvb_SetTimeGateStartTime.errcheck = __errorcheck__
rszvb_SetTimeGateStartTime.output = False
# rszvb_GetTimeGateStartTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* startTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'startTime'),)
rszvb_GetTimeGateStartTime  = prototype(('rszvb_GetTimeGateStartTime', rszvbDLL), paramflags)
rszvb_GetTimeGateStartTime.name = 'rszvb_GetTimeGateStartTime'
rszvb_GetTimeGateStartTime.errcheck = __errorcheck__
rszvb_GetTimeGateStartTime.output = True
# rszvb_SetTimeGateStopTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 stopTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'stopTime'),)
rszvb_SetTimeGateStopTime  = prototype(('rszvb_SetTimeGateStopTime', rszvbDLL), paramflags)
rszvb_SetTimeGateStopTime.name = 'rszvb_SetTimeGateStopTime'
rszvb_SetTimeGateStopTime.errcheck = __errorcheck__
rszvb_SetTimeGateStopTime.output = False
# rszvb_GetTimeGateStopTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* stopTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'stopTime'),)
rszvb_GetTimeGateStopTime  = prototype(('rszvb_GetTimeGateStopTime', rszvbDLL), paramflags)
rszvb_GetTimeGateStopTime.name = 'rszvb_GetTimeGateStopTime'
rszvb_GetTimeGateStopTime.errcheck = __errorcheck__
rszvb_GetTimeGateStopTime.output = True
# rszvb_SetTimeGateCenterTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 centerTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'centerTime'),)
rszvb_SetTimeGateCenterTime  = prototype(('rszvb_SetTimeGateCenterTime', rszvbDLL), paramflags)
rszvb_SetTimeGateCenterTime.name = 'rszvb_SetTimeGateCenterTime'
rszvb_SetTimeGateCenterTime.errcheck = __errorcheck__
rszvb_SetTimeGateCenterTime.output = False
# rszvb_GetTimeGateCenterTime ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* centerTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'centerTime'),)
rszvb_GetTimeGateCenterTime  = prototype(('rszvb_GetTimeGateCenterTime', rszvbDLL), paramflags)
rszvb_GetTimeGateCenterTime.name = 'rszvb_GetTimeGateCenterTime'
rszvb_GetTimeGateCenterTime.errcheck = __errorcheck__
rszvb_GetTimeGateCenterTime.output = True
# rszvb_SetTimeGateType ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 timeGateType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'timeGateType'),)
rszvb_SetTimeGateType  = prototype(('rszvb_SetTimeGateType', rszvbDLL), paramflags)
rszvb_SetTimeGateType.name = 'rszvb_SetTimeGateType'
rszvb_SetTimeGateType.errcheck = __errorcheck__
rszvb_SetTimeGateType.output = False
# rszvb_GetTimeGateType ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* timeGateType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'timeGateType'),)
rszvb_GetTimeGateType  = prototype(('rszvb_GetTimeGateType', rszvbDLL), paramflags)
rszvb_GetTimeGateType.name = 'rszvb_GetTimeGateType'
rszvb_GetTimeGateType.errcheck = __errorcheck__
rszvb_GetTimeGateType.output = True
# rszvb_SetTimeGateFilter ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 filterType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'filterType'),)
rszvb_SetTimeGateFilter  = prototype(('rszvb_SetTimeGateFilter', rszvbDLL), paramflags)
rszvb_SetTimeGateFilter.name = 'rszvb_SetTimeGateFilter'
rszvb_SetTimeGateFilter.errcheck = __errorcheck__
rszvb_SetTimeGateFilter.output = False
# rszvb_GetTimeGateFilter ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* filterType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'filterType'),)
rszvb_GetTimeGateFilter  = prototype(('rszvb_GetTimeGateFilter', rszvbDLL), paramflags)
rszvb_GetTimeGateFilter.name = 'rszvb_GetTimeGateFilter'
rszvb_GetTimeGateFilter.errcheck = __errorcheck__
rszvb_GetTimeGateFilter.output = True
# rszvb_SetTimeGateSidebandSuppression ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 sidebandSuppression']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'sidebandSuppression'),)
rszvb_SetTimeGateSidebandSuppression  = prototype(('rszvb_SetTimeGateSidebandSuppression', rszvbDLL), paramflags)
rszvb_SetTimeGateSidebandSuppression.name = 'rszvb_SetTimeGateSidebandSuppression'
rszvb_SetTimeGateSidebandSuppression.errcheck = __errorcheck__
rszvb_SetTimeGateSidebandSuppression.output = False
# rszvb_GetTimeGateSidebandSuppression ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* sidebandSuppression']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'sidebandSuppression'),)
rszvb_GetTimeGateSidebandSuppression  = prototype(('rszvb_GetTimeGateSidebandSuppression', rszvbDLL), paramflags)
rszvb_GetTimeGateSidebandSuppression.name = 'rszvb_GetTimeGateSidebandSuppression'
rszvb_GetTimeGateSidebandSuppression.errcheck = __errorcheck__
rszvb_GetTimeGateSidebandSuppression.output = True
# rszvb_SetTimeGateShape ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 timeGateShape']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'timeGateShape'),)
rszvb_SetTimeGateShape  = prototype(('rszvb_SetTimeGateShape', rszvbDLL), paramflags)
rszvb_SetTimeGateShape.name = 'rszvb_SetTimeGateShape'
rszvb_SetTimeGateShape.errcheck = __errorcheck__
rszvb_SetTimeGateShape.output = False
# rszvb_GetTimeGateShape ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* timeGateShape']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'timeGateShape'),)
rszvb_GetTimeGateShape  = prototype(('rszvb_GetTimeGateShape', rszvbDLL), paramflags)
rszvb_GetTimeGateShape.name = 'rszvb_GetTimeGateShape'
rszvb_GetTimeGateShape.errcheck = __errorcheck__
rszvb_GetTimeGateShape.output = True
# rszvb_SetTimeGateSpan ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 span']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'span'),)
rszvb_SetTimeGateSpan  = prototype(('rszvb_SetTimeGateSpan', rszvbDLL), paramflags)
rszvb_SetTimeGateSpan.name = 'rszvb_SetTimeGateSpan'
rszvb_SetTimeGateSpan.errcheck = __errorcheck__
rszvb_SetTimeGateSpan.output = False
# rszvb_GetTimeGateSpan ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* span']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'span'),)
rszvb_GetTimeGateSpan  = prototype(('rszvb_GetTimeGateSpan', rszvbDLL), paramflags)
rszvb_GetTimeGateSpan.name = 'rszvb_GetTimeGateSpan'
rszvb_GetTimeGateSpan.errcheck = __errorcheck__
rszvb_GetTimeGateSpan.output = True
# rszvb_SetTimeGateDisplayState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean timeGateDisplay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'timeGateDisplay'),)
rszvb_SetTimeGateDisplayState  = prototype(('rszvb_SetTimeGateDisplayState', rszvbDLL), paramflags)
rszvb_SetTimeGateDisplayState.name = 'rszvb_SetTimeGateDisplayState'
rszvb_SetTimeGateDisplayState.errcheck = __errorcheck__
rszvb_SetTimeGateDisplayState.output = False
# rszvb_GetTimeGateDisplayState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* timeGateDisplay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'timeGateDisplay'),)
rszvb_GetTimeGateDisplayState  = prototype(('rszvb_GetTimeGateDisplayState', rszvbDLL), paramflags)
rszvb_GetTimeGateDisplayState.name = 'rszvb_GetTimeGateDisplayState'
rszvb_GetTimeGateDisplayState.errcheck = __errorcheck__
rszvb_GetTimeGateDisplayState.output = True
# rszvb_TraceEvaluationRange ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 evaluationRange', 'ViReal64 start', 'ViReal64 stop']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'evaluationRange'),(1, 'start'),(1, 'stop'),)
rszvb_TraceEvaluationRange  = prototype(('rszvb_TraceEvaluationRange', rszvbDLL), paramflags)
rszvb_TraceEvaluationRange.name = 'rszvb_TraceEvaluationRange'
rszvb_TraceEvaluationRange.errcheck = __errorcheck__
rszvb_TraceEvaluationRange.output = False
# rszvb_TraceStatisticalEvaluation ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 statisticalParameter', 'ViBoolean infoField', 'ViReal64 _VI_FAR responseValue_s[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool,numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'statisticalParameter'),(1, 'infoField'),(1, 'responseValue_s[]'),)
rszvb_TraceStatisticalEvaluation  = prototype(('rszvb_TraceStatisticalEvaluation', rszvbDLL), paramflags)
rszvb_TraceStatisticalEvaluation.name = 'rszvb_TraceStatisticalEvaluation'
rszvb_TraceStatisticalEvaluation.errcheck = __errorcheck__
rszvb_TraceStatisticalEvaluation.output = False
# rszvb_SetTraceEvaluationRangeShow ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean showRange']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'showRange'),)
rszvb_SetTraceEvaluationRangeShow  = prototype(('rszvb_SetTraceEvaluationRangeShow', rszvbDLL), paramflags)
rszvb_SetTraceEvaluationRangeShow.name = 'rszvb_SetTraceEvaluationRangeShow'
rszvb_SetTraceEvaluationRangeShow.errcheck = __errorcheck__
rszvb_SetTraceEvaluationRangeShow.output = False
# rszvb_GetTraceEvaluationRangeShow ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* showRange']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'showRange'),)
rszvb_GetTraceEvaluationRangeShow  = prototype(('rszvb_GetTraceEvaluationRangeShow', rszvbDLL), paramflags)
rszvb_GetTraceEvaluationRangeShow.name = 'rszvb_GetTraceEvaluationRangeShow'
rszvb_GetTraceEvaluationRangeShow.errcheck = __errorcheck__
rszvb_GetTraceEvaluationRangeShow.output = True
# rszvb_SetTraceCompressionValue ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64 compressionValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'compressionValue'),)
rszvb_SetTraceCompressionValue  = prototype(('rszvb_SetTraceCompressionValue', rszvbDLL), paramflags)
rszvb_SetTraceCompressionValue.name = 'rszvb_SetTraceCompressionValue'
rszvb_SetTraceCompressionValue.errcheck = __errorcheck__
rszvb_SetTraceCompressionValue.output = False
# rszvb_GetTraceCompressionValue ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* compressionValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'compressionValue'),)
rszvb_GetTraceCompressionValue  = prototype(('rszvb_GetTraceCompressionValue', rszvbDLL), paramflags)
rszvb_GetTraceCompressionValue.name = 'rszvb_GetTraceCompressionValue'
rszvb_GetTraceCompressionValue.errcheck = __errorcheck__
rszvb_GetTraceCompressionValue.output = True
# rszvb_GetTraceCompressionPoint ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViReal64* compressionPointIn', 'ViReal64* compressionPointOut']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'compressionPointIn'),(2, 'compressionPointOut'),)
rszvb_GetTraceCompressionPoint  = prototype(('rszvb_GetTraceCompressionPoint', rszvbDLL), paramflags)
rszvb_GetTraceCompressionPoint.name = 'rszvb_GetTraceCompressionPoint'
rszvb_GetTraceCompressionPoint.errcheck = __errorcheck__
rszvb_GetTraceCompressionPoint.output = True
# rszvb_SetDisplayResultsState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 resultType', 'ViBoolean displayResults']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'resultType'),(1, 'displayResults'),)
rszvb_SetDisplayResultsState  = prototype(('rszvb_SetDisplayResultsState', rszvbDLL), paramflags)
rszvb_SetDisplayResultsState.name = 'rszvb_SetDisplayResultsState'
rszvb_SetDisplayResultsState.errcheck = __errorcheck__
rszvb_SetDisplayResultsState.output = False
# rszvb_GetDisplayResultsState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 resultType', 'ViBoolean* displayResults']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'resultType'),(2, 'displayResults'),)
rszvb_GetDisplayResultsState  = prototype(('rszvb_GetDisplayResultsState', rszvbDLL), paramflags)
rszvb_GetDisplayResultsState.name = 'rszvb_GetDisplayResultsState'
rszvb_GetDisplayResultsState.errcheck = __errorcheck__
rszvb_GetDisplayResultsState.output = True
# rszvb_SetTraceSmoothing ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean smoothing', 'ViReal64 aperture']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'smoothing'),(1, 'aperture'),)
rszvb_SetTraceSmoothing  = prototype(('rszvb_SetTraceSmoothing', rszvbDLL), paramflags)
rszvb_SetTraceSmoothing.name = 'rszvb_SetTraceSmoothing'
rszvb_SetTraceSmoothing.errcheck = __errorcheck__
rszvb_SetTraceSmoothing.output = False
# rszvb_GetTraceSmoothing ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* smoothing', 'ViReal64* aperture']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'smoothing'),(2, 'aperture'),)
rszvb_GetTraceSmoothing  = prototype(('rszvb_GetTraceSmoothing', rszvbDLL), paramflags)
rszvb_GetTraceSmoothing.name = 'rszvb_GetTraceSmoothing'
rszvb_GetTraceSmoothing.errcheck = __errorcheck__
rszvb_GetTraceSmoothing.output = True
# rszvb_TraceResponseData ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 dataFormat', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'dataFormat'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceResponseData  = prototype(('rszvb_TraceResponseData', rszvbDLL), paramflags)
rszvb_TraceResponseData.name = 'rszvb_TraceResponseData'
rszvb_TraceResponseData.errcheck = __errorcheck__
rszvb_TraceResponseData.output = True
# rszvb_TraceResponseDataError ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 errorTerm', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'errorTerm'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceResponseDataError  = prototype(('rszvb_TraceResponseDataError', rszvbDLL), paramflags)
rszvb_TraceResponseDataError.name = 'rszvb_TraceResponseDataError'
rszvb_TraceResponseDataError.errcheck = __errorcheck__
rszvb_TraceResponseDataError.output = True
# rszvb_TraceResponseDataAll ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 dataFormat', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'dataFormat'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceResponseDataAll  = prototype(('rszvb_TraceResponseDataAll', rszvbDLL), paramflags)
rszvb_TraceResponseDataAll.name = 'rszvb_TraceResponseDataAll'
rszvb_TraceResponseDataAll.errcheck = __errorcheck__
rszvb_TraceResponseDataAll.output = True
# rszvb_TraceComplexResponseData ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 dataFormat', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'dataFormat'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceComplexResponseData  = prototype(('rszvb_TraceComplexResponseData', rszvbDLL), paramflags)
rszvb_TraceComplexResponseData.name = 'rszvb_TraceComplexResponseData'
rszvb_TraceComplexResponseData.errcheck = __errorcheck__
rszvb_TraceComplexResponseData.output = True
# rszvb_TraceComplexResponseCatalog ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 bufferSize', 'ViChar _VI_FAR catalog[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'bufferSize'),(1, 'catalog[]'),)
rszvb_TraceComplexResponseCatalog  = prototype(('rszvb_TraceComplexResponseCatalog', rszvbDLL), paramflags)
rszvb_TraceComplexResponseCatalog.name = 'rszvb_TraceComplexResponseCatalog'
rszvb_TraceComplexResponseCatalog.errcheck = __errorcheck__
rszvb_TraceComplexResponseCatalog.output = False
# rszvb_TraceResponseDataAllData ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 dataFormat', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'dataFormat'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceResponseDataAllData  = prototype(('rszvb_TraceResponseDataAllData', rszvbDLL), paramflags)
rszvb_TraceResponseDataAllData.name = 'rszvb_TraceResponseDataAllData'
rszvb_TraceResponseDataAllData.errcheck = __errorcheck__
rszvb_TraceResponseDataAllData.output = True
# rszvb_TraceResponseSingleSweepData ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 sweepNumber', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'sweepNumber'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceResponseSingleSweepData  = prototype(('rszvb_TraceResponseSingleSweepData', rszvbDLL), paramflags)
rszvb_TraceResponseSingleSweepData.name = 'rszvb_TraceResponseSingleSweepData'
rszvb_TraceResponseSingleSweepData.errcheck = __errorcheck__
rszvb_TraceResponseSingleSweepData.output = True
# rszvb_TraceResponseSingleSweepDataCount ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* sweepCount']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'sweepCount'),)
rszvb_TraceResponseSingleSweepDataCount  = prototype(('rszvb_TraceResponseSingleSweepDataCount', rszvbDLL), paramflags)
rszvb_TraceResponseSingleSweepDataCount.name = 'rszvb_TraceResponseSingleSweepDataCount'
rszvb_TraceResponseSingleSweepDataCount.errcheck = __errorcheck__
rszvb_TraceResponseSingleSweepDataCount.output = True
# rszvb_TraceResponseSingleSweepDataForward ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 sweepNumber', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'sweepNumber'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceResponseSingleSweepDataForward  = prototype(('rszvb_TraceResponseSingleSweepDataForward', rszvbDLL), paramflags)
rszvb_TraceResponseSingleSweepDataForward.name = 'rszvb_TraceResponseSingleSweepDataForward'
rszvb_TraceResponseSingleSweepDataForward.errcheck = __errorcheck__
rszvb_TraceResponseSingleSweepDataForward.output = True
# rszvb_TraceStimulusData ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceStimulusData  = prototype(('rszvb_TraceStimulusData', rszvbDLL), paramflags)
rszvb_TraceStimulusData.name = 'rszvb_TraceStimulusData'
rszvb_TraceStimulusData.errcheck = __errorcheck__
rszvb_TraceStimulusData.output = True
# rszvb_WriteMemoryTraceData ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 noOfPoints', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'noOfPoints'),(1, 'traceData[]'),)
rszvb_WriteMemoryTraceData  = prototype(('rszvb_WriteMemoryTraceData', rszvbDLL), paramflags)
rszvb_WriteMemoryTraceData.name = 'rszvb_WriteMemoryTraceData'
rszvb_WriteMemoryTraceData.errcheck = __errorcheck__
rszvb_WriteMemoryTraceData.output = False
# rszvb_WriteMemoryTraceDataExt ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 dataFormat', 'ViInt32 noOfPoints', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'dataFormat'),(1, 'noOfPoints'),(1, 'traceData[]'),)
rszvb_WriteMemoryTraceDataExt  = prototype(('rszvb_WriteMemoryTraceDataExt', rszvbDLL), paramflags)
rszvb_WriteMemoryTraceDataExt.name = 'rszvb_WriteMemoryTraceDataExt'
rszvb_WriteMemoryTraceDataExt.errcheck = __errorcheck__
rszvb_WriteMemoryTraceDataExt.output = False
# rszvb_SetTraceFormatZVR ['ViSession instrumentHandle', 'ViInt32 dataFormat']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'dataFormat'),)
rszvb_SetTraceFormatZVR  = prototype(('rszvb_SetTraceFormatZVR', rszvbDLL), paramflags)
rszvb_SetTraceFormatZVR.name = 'rszvb_SetTraceFormatZVR'
rszvb_SetTraceFormatZVR.errcheck = __errorcheck__
rszvb_SetTraceFormatZVR.output = False
# rszvb_GetTraceFormatZVR ['ViSession instrumentHandle', 'ViInt32* dataFormat']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'dataFormat'),)
rszvb_GetTraceFormatZVR  = prototype(('rszvb_GetTraceFormatZVR', rszvbDLL), paramflags)
rszvb_GetTraceFormatZVR.name = 'rszvb_GetTraceFormatZVR'
rszvb_GetTraceFormatZVR.errcheck = __errorcheck__
rszvb_GetTraceFormatZVR.output = True
# rszvb_TraceResponseDataZVR ['ViSession instrumentHandle', 'ViInt32 dataFormat', 'ViInt32 valuesToReturn', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'dataFormat'),(1, 'valuesToReturn'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceResponseDataZVR  = prototype(('rszvb_TraceResponseDataZVR', rszvbDLL), paramflags)
rszvb_TraceResponseDataZVR.name = 'rszvb_TraceResponseDataZVR'
rszvb_TraceResponseDataZVR.errcheck = __errorcheck__
rszvb_TraceResponseDataZVR.output = True
# rszvb_TraceStimulusDataZVR ['ViSession instrumentHandle', 'ViInt32 dataFormat', 'ViInt32 valuesToReturn', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'dataFormat'),(1, 'valuesToReturn'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceStimulusDataZVR  = prototype(('rszvb_TraceStimulusDataZVR', rszvbDLL), paramflags)
rszvb_TraceStimulusDataZVR.name = 'rszvb_TraceStimulusDataZVR'
rszvb_TraceStimulusDataZVR.errcheck = __errorcheck__
rszvb_TraceStimulusDataZVR.output = True
# rszvb_TraceResponseDataSParameterGroup ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 dataFormat', 'ViInt32 valuesToReturn', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'dataFormat'),(1, 'valuesToReturn'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_TraceResponseDataSParameterGroup  = prototype(('rszvb_TraceResponseDataSParameterGroup', rszvbDLL), paramflags)
rszvb_TraceResponseDataSParameterGroup.name = 'rszvb_TraceResponseDataSParameterGroup'
rszvb_TraceResponseDataSParameterGroup.errcheck = __errorcheck__
rszvb_TraceResponseDataSParameterGroup.output = True
# rszvb_TraceImportData ['ViSession instrumentHandle', 'ViString traceName', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(1, 'fileName'),)
rszvb_TraceImportData  = prototype(('rszvb_TraceImportData', rszvbDLL), paramflags)
rszvb_TraceImportData.name = 'rszvb_TraceImportData'
rszvb_TraceImportData.errcheck = __errorcheck__
rszvb_TraceImportData.output = False
# rszvb_TraceExportData ['ViSession instrumentHandle', 'ViString traceName', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(1, 'fileName'),)
rszvb_TraceExportData  = prototype(('rszvb_TraceExportData', rszvbDLL), paramflags)
rszvb_TraceExportData.name = 'rszvb_TraceExportData'
rszvb_TraceExportData.errcheck = __errorcheck__
rszvb_TraceExportData.output = False
# rszvb_TraceExportDataWithOptions ['ViSession instrumentHandle', 'ViString traceName', 'ViString fileName', 'ViInt32 exportFormat', 'ViInt32 exportData']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(1, 'fileName'),(1, 'exportFormat'),(1, 'exportData'),)
rszvb_TraceExportDataWithOptions  = prototype(('rszvb_TraceExportDataWithOptions', rszvbDLL), paramflags)
rszvb_TraceExportDataWithOptions.name = 'rszvb_TraceExportDataWithOptions'
rszvb_TraceExportDataWithOptions.errcheck = __errorcheck__
rszvb_TraceExportDataWithOptions.output = False
# rszvb_TraceExportDataWithOptionsExt ['ViSession instrumentHandle', 'ViString traceName', 'ViString fileName', 'ViInt32 exportFormat', 'ViInt32 exportData', 'ViInt32 decimalSeparator', 'ViInt32 fieldSeparator']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(1, 'fileName'),(1, 'exportFormat'),(1, 'exportData'),(1, 'decimalSeparator'),(1, 'fieldSeparator'),)
rszvb_TraceExportDataWithOptionsExt  = prototype(('rszvb_TraceExportDataWithOptionsExt', rszvbDLL), paramflags)
rszvb_TraceExportDataWithOptionsExt.name = 'rszvb_TraceExportDataWithOptionsExt'
rszvb_TraceExportDataWithOptionsExt.errcheck = __errorcheck__
rszvb_TraceExportDataWithOptionsExt.output = False
# rszvb_ChannelTraceExportData ['ViSession instrumentHandle', 'ViInt32 selectChannel', 'ViInt32 channel_Trace', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'selectChannel'),(1, 'channel_Trace'),(1, 'fileName'),)
rszvb_ChannelTraceExportData  = prototype(('rszvb_ChannelTraceExportData', rszvbDLL), paramflags)
rszvb_ChannelTraceExportData.name = 'rszvb_ChannelTraceExportData'
rszvb_ChannelTraceExportData.errcheck = __errorcheck__
rszvb_ChannelTraceExportData.output = False
# rszvb_ChannelTraceExportDataWithOptions ['ViSession instrumentHandle', 'ViInt32 selectChannel', 'ViInt32 channel_Trace', 'ViString fileName', 'ViInt32 exportFormat', 'ViInt32 exportData']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'selectChannel'),(1, 'channel_Trace'),(1, 'fileName'),(1, 'exportFormat'),(1, 'exportData'),)
rszvb_ChannelTraceExportDataWithOptions  = prototype(('rszvb_ChannelTraceExportDataWithOptions', rszvbDLL), paramflags)
rszvb_ChannelTraceExportDataWithOptions.name = 'rszvb_ChannelTraceExportDataWithOptions'
rszvb_ChannelTraceExportDataWithOptions.errcheck = __errorcheck__
rszvb_ChannelTraceExportDataWithOptions.output = False
# rszvb_ChannelTraceExportDataWithOptionsExt ['ViSession instrumentHandle', 'ViInt32 selectChannel', 'ViInt32 channel_Trace', 'ViString fileName', 'ViInt32 exportFormat', 'ViInt32 exportData', 'ViInt32 decimalSeparator', 'ViInt32 fieldSeparator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'selectChannel'),(1, 'channel_Trace'),(1, 'fileName'),(1, 'exportFormat'),(1, 'exportData'),(1, 'decimalSeparator'),(1, 'fieldSeparator'),)
rszvb_ChannelTraceExportDataWithOptionsExt  = prototype(('rszvb_ChannelTraceExportDataWithOptionsExt', rszvbDLL), paramflags)
rszvb_ChannelTraceExportDataWithOptionsExt.name = 'rszvb_ChannelTraceExportDataWithOptionsExt'
rszvb_ChannelTraceExportDataWithOptionsExt.errcheck = __errorcheck__
rszvb_ChannelTraceExportDataWithOptionsExt.output = False
# rszvb_TraceExportDataPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString fileName', 'ViInt32 exportData', 'ViInt32 port1', 'ViInt32 port2', 'ViInt32 port3', 'ViInt32 port4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fileName'),(1, 'exportData'),(1, 'port1'),(1, 'port2'),(1, 'port3'),(1, 'port4'),)
rszvb_TraceExportDataPorts  = prototype(('rszvb_TraceExportDataPorts', rszvbDLL), paramflags)
rszvb_TraceExportDataPorts.name = 'rszvb_TraceExportDataPorts'
rszvb_TraceExportDataPorts.errcheck = __errorcheck__
rszvb_TraceExportDataPorts.output = False
# rszvb_TraceExportDataPortsIncomplete ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString fileName', 'ViInt32 exportData', 'ViInt32 port1', 'ViInt32 port2', 'ViInt32 port3', 'ViInt32 port4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fileName'),(1, 'exportData'),(1, 'port1'),(1, 'port2'),(1, 'port3'),(1, 'port4'),)
rszvb_TraceExportDataPortsIncomplete  = prototype(('rszvb_TraceExportDataPortsIncomplete', rszvbDLL), paramflags)
rszvb_TraceExportDataPortsIncomplete.name = 'rszvb_TraceExportDataPortsIncomplete'
rszvb_TraceExportDataPortsIncomplete.errcheck = __errorcheck__
rszvb_TraceExportDataPortsIncomplete.output = False
# rszvb_SetRenormalizationState ['ViSession instrumentHandle', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'state'),)
rszvb_SetRenormalizationState  = prototype(('rszvb_SetRenormalizationState', rszvbDLL), paramflags)
rszvb_SetRenormalizationState.name = 'rszvb_SetRenormalizationState'
rszvb_SetRenormalizationState.errcheck = __errorcheck__
rszvb_SetRenormalizationState.output = False
# rszvb_GetRenormalizationState ['ViSession instrumentHandle', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'state'),)
rszvb_GetRenormalizationState  = prototype(('rszvb_GetRenormalizationState', rszvbDLL), paramflags)
rszvb_GetRenormalizationState.name = 'rszvb_GetRenormalizationState'
rszvb_GetRenormalizationState.errcheck = __errorcheck__
rszvb_GetRenormalizationState.output = True
# rszvb_SetRenormalizationMode ['ViSession instrumentHandle', 'ViInt32 mode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'mode'),)
rszvb_SetRenormalizationMode  = prototype(('rszvb_SetRenormalizationMode', rszvbDLL), paramflags)
rszvb_SetRenormalizationMode.name = 'rszvb_SetRenormalizationMode'
rszvb_SetRenormalizationMode.errcheck = __errorcheck__
rszvb_SetRenormalizationMode.output = False
# rszvb_GetRenormalizationMode ['ViSession instrumentHandle', 'ViInt32* mode']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'mode'),)
rszvb_GetRenormalizationMode  = prototype(('rszvb_GetRenormalizationMode', rszvbDLL), paramflags)
rszvb_GetRenormalizationMode.name = 'rszvb_GetRenormalizationMode'
rszvb_GetRenormalizationMode.errcheck = __errorcheck__
rszvb_GetRenormalizationMode.output = True
# rszvb_SetRenormalizationImpedance ['ViSession instrumentHandle', 'ViReal64 impedance']
prototype = WINFUNCTYPE(c_int, c_int,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'impedance'),)
rszvb_SetRenormalizationImpedance  = prototype(('rszvb_SetRenormalizationImpedance', rszvbDLL), paramflags)
rszvb_SetRenormalizationImpedance.name = 'rszvb_SetRenormalizationImpedance'
rszvb_SetRenormalizationImpedance.errcheck = __errorcheck__
rszvb_SetRenormalizationImpedance.output = False
# rszvb_GetRenormalizationImpedance ['ViSession instrumentHandle', 'ViReal64* impedance']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(2, 'impedance'),)
rszvb_GetRenormalizationImpedance  = prototype(('rszvb_GetRenormalizationImpedance', rszvbDLL), paramflags)
rszvb_GetRenormalizationImpedance.name = 'rszvb_GetRenormalizationImpedance'
rszvb_GetRenormalizationImpedance.errcheck = __errorcheck__
rszvb_GetRenormalizationImpedance.output = True
# rszvb_TraceShiftStimulusValue ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64 shiftStimulusValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'shiftStimulusValue'),)
rszvb_TraceShiftStimulusValue  = prototype(('rszvb_TraceShiftStimulusValue', rszvbDLL), paramflags)
rszvb_TraceShiftStimulusValue.name = 'rszvb_TraceShiftStimulusValue'
rszvb_TraceShiftStimulusValue.errcheck = __errorcheck__
rszvb_TraceShiftStimulusValue.output = False
# rszvb_TraceShiftResponseValue ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViReal64 magnitude', 'ViReal64 phase', 'ViReal64 real', 'ViReal64 imaginary']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'magnitude'),(1, 'phase'),(1, 'real'),(1, 'imaginary'),)
rszvb_TraceShiftResponseValue  = prototype(('rszvb_TraceShiftResponseValue', rszvbDLL), paramflags)
rszvb_TraceShiftResponseValue.name = 'rszvb_TraceShiftResponseValue'
rszvb_TraceShiftResponseValue.errcheck = __errorcheck__
rszvb_TraceShiftResponseValue.output = False
# rszvb_SetHold ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 hold']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'hold'),)
rszvb_SetHold  = prototype(('rszvb_SetHold', rszvbDLL), paramflags)
rszvb_SetHold.name = 'rszvb_SetHold'
rszvb_SetHold.errcheck = __errorcheck__
rszvb_SetHold.output = False
# rszvb_GetHold ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* hold']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'hold'),)
rszvb_GetHold  = prototype(('rszvb_GetHold', rszvbDLL), paramflags)
rszvb_GetHold.name = 'rszvb_GetHold'
rszvb_GetHold.errcheck = __errorcheck__
rszvb_GetHold.output = True
# rszvb_LinearityDeviationManual ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 slope', 'ViReal64 constant', 'ViReal64 electricalLength']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'slope'),(1, 'constant'),(1, 'electricalLength'),)
rszvb_LinearityDeviationManual  = prototype(('rszvb_LinearityDeviationManual', rszvbDLL), paramflags)
rszvb_LinearityDeviationManual.name = 'rszvb_LinearityDeviationManual'
rszvb_LinearityDeviationManual.errcheck = __errorcheck__
rszvb_LinearityDeviationManual.output = False
# rszvb_LinearityDeviationAuto ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_LinearityDeviationAuto  = prototype(('rszvb_LinearityDeviationAuto', rszvbDLL), paramflags)
rszvb_LinearityDeviationAuto.name = 'rszvb_LinearityDeviationAuto'
rszvb_LinearityDeviationAuto.errcheck = __errorcheck__
rszvb_LinearityDeviationAuto.output = False
# rszvb_SetLinearityDeviationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetLinearityDeviationState  = prototype(('rszvb_SetLinearityDeviationState', rszvbDLL), paramflags)
rszvb_SetLinearityDeviationState.name = 'rszvb_SetLinearityDeviationState'
rszvb_SetLinearityDeviationState.errcheck = __errorcheck__
rszvb_SetLinearityDeviationState.output = False
# rszvb_GetLinearityDeviationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetLinearityDeviationState  = prototype(('rszvb_GetLinearityDeviationState', rszvbDLL), paramflags)
rszvb_GetLinearityDeviationState.name = 'rszvb_GetLinearityDeviationState'
rszvb_GetLinearityDeviationState.errcheck = __errorcheck__
rszvb_GetLinearityDeviationState.output = True
# rszvb_SetLinearityDeviationSlope ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 slope']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'slope'),)
rszvb_SetLinearityDeviationSlope  = prototype(('rszvb_SetLinearityDeviationSlope', rszvbDLL), paramflags)
rszvb_SetLinearityDeviationSlope.name = 'rszvb_SetLinearityDeviationSlope'
rszvb_SetLinearityDeviationSlope.errcheck = __errorcheck__
rszvb_SetLinearityDeviationSlope.output = False
# rszvb_GetLinearityDeviationSlope ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* slope']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'slope'),)
rszvb_GetLinearityDeviationSlope  = prototype(('rszvb_GetLinearityDeviationSlope', rszvbDLL), paramflags)
rszvb_GetLinearityDeviationSlope.name = 'rszvb_GetLinearityDeviationSlope'
rszvb_GetLinearityDeviationSlope.errcheck = __errorcheck__
rszvb_GetLinearityDeviationSlope.output = True
# rszvb_SetLinearityDeviationConstant ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 constant']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'constant'),)
rszvb_SetLinearityDeviationConstant  = prototype(('rszvb_SetLinearityDeviationConstant', rszvbDLL), paramflags)
rszvb_SetLinearityDeviationConstant.name = 'rszvb_SetLinearityDeviationConstant'
rszvb_SetLinearityDeviationConstant.errcheck = __errorcheck__
rszvb_SetLinearityDeviationConstant.output = False
# rszvb_GetLinearityDeviationConstant ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* constant']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'constant'),)
rszvb_GetLinearityDeviationConstant  = prototype(('rszvb_GetLinearityDeviationConstant', rszvbDLL), paramflags)
rszvb_GetLinearityDeviationConstant.name = 'rszvb_GetLinearityDeviationConstant'
rszvb_GetLinearityDeviationConstant.errcheck = __errorcheck__
rszvb_GetLinearityDeviationConstant.output = True
# rszvb_SetLinearityDeviationElectricalLength ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 electricalLength']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'electricalLength'),)
rszvb_SetLinearityDeviationElectricalLength  = prototype(('rszvb_SetLinearityDeviationElectricalLength', rszvbDLL), paramflags)
rszvb_SetLinearityDeviationElectricalLength.name = 'rszvb_SetLinearityDeviationElectricalLength'
rszvb_SetLinearityDeviationElectricalLength.errcheck = __errorcheck__
rszvb_SetLinearityDeviationElectricalLength.output = False
# rszvb_GetLinearityDeviationElectricalLength ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* electricalLength']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'electricalLength'),)
rszvb_GetLinearityDeviationElectricalLength  = prototype(('rszvb_GetLinearityDeviationElectricalLength', rszvbDLL), paramflags)
rszvb_GetLinearityDeviationElectricalLength.name = 'rszvb_GetLinearityDeviationElectricalLength'
rszvb_GetLinearityDeviationElectricalLength.errcheck = __errorcheck__
rszvb_GetLinearityDeviationElectricalLength.output = True
# rszvb_SetMarkerState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean markerState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'markerState'),)
rszvb_SetMarkerState  = prototype(('rszvb_SetMarkerState', rszvbDLL), paramflags)
rszvb_SetMarkerState.name = 'rszvb_SetMarkerState'
rszvb_SetMarkerState.errcheck = __errorcheck__
rszvb_SetMarkerState.output = False
# rszvb_GetMarkerState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean* markerState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'markerState'),)
rszvb_GetMarkerState  = prototype(('rszvb_GetMarkerState', rszvbDLL), paramflags)
rszvb_GetMarkerState.name = 'rszvb_GetMarkerState'
rszvb_GetMarkerState.errcheck = __errorcheck__
rszvb_GetMarkerState.output = True
# rszvb_SetMarkerStimulus ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64 markerStimulus']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'markerStimulus'),)
rszvb_SetMarkerStimulus  = prototype(('rszvb_SetMarkerStimulus', rszvbDLL), paramflags)
rszvb_SetMarkerStimulus.name = 'rszvb_SetMarkerStimulus'
rszvb_SetMarkerStimulus.errcheck = __errorcheck__
rszvb_SetMarkerStimulus.output = False
# rszvb_GetMarkerStimulus ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64* markerStimulus']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'markerStimulus'),)
rszvb_GetMarkerStimulus  = prototype(('rszvb_GetMarkerStimulus', rszvbDLL), paramflags)
rszvb_GetMarkerStimulus.name = 'rszvb_GetMarkerStimulus'
rszvb_GetMarkerStimulus.errcheck = __errorcheck__
rszvb_GetMarkerStimulus.output = True
# rszvb_GetMarkerResponse ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64 _VI_FAR markerResponse[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'markerResponse[]'),)
rszvb_GetMarkerResponse  = prototype(('rszvb_GetMarkerResponse', rszvbDLL), paramflags)
rszvb_GetMarkerResponse.name = 'rszvb_GetMarkerResponse'
rszvb_GetMarkerResponse.errcheck = __errorcheck__
rszvb_GetMarkerResponse.output = False
# rszvb_SetReferenceMarkerState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean referenceMarkerState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'referenceMarkerState'),)
rszvb_SetReferenceMarkerState  = prototype(('rszvb_SetReferenceMarkerState', rszvbDLL), paramflags)
rszvb_SetReferenceMarkerState.name = 'rszvb_SetReferenceMarkerState'
rszvb_SetReferenceMarkerState.errcheck = __errorcheck__
rszvb_SetReferenceMarkerState.output = False
# rszvb_GetReferenceMarkerState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean* referenceMarkerState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'referenceMarkerState'),)
rszvb_GetReferenceMarkerState  = prototype(('rszvb_GetReferenceMarkerState', rszvbDLL), paramflags)
rszvb_GetReferenceMarkerState.name = 'rszvb_GetReferenceMarkerState'
rszvb_GetReferenceMarkerState.errcheck = __errorcheck__
rszvb_GetReferenceMarkerState.output = True
# rszvb_SetReferenceMarkerStimulus ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64 referenceMarkerStimulus']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'referenceMarkerStimulus'),)
rszvb_SetReferenceMarkerStimulus  = prototype(('rszvb_SetReferenceMarkerStimulus', rszvbDLL), paramflags)
rszvb_SetReferenceMarkerStimulus.name = 'rszvb_SetReferenceMarkerStimulus'
rszvb_SetReferenceMarkerStimulus.errcheck = __errorcheck__
rszvb_SetReferenceMarkerStimulus.output = False
# rszvb_GetReferenceMarkerStimulus ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64* referenceMarkerStimulus']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'referenceMarkerStimulus'),)
rszvb_GetReferenceMarkerStimulus  = prototype(('rszvb_GetReferenceMarkerStimulus', rszvbDLL), paramflags)
rszvb_GetReferenceMarkerStimulus.name = 'rszvb_GetReferenceMarkerStimulus'
rszvb_GetReferenceMarkerStimulus.errcheck = __errorcheck__
rszvb_GetReferenceMarkerStimulus.output = True
# rszvb_GetReferenceMarkerResponse ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64* referenceMarkerResponse']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'referenceMarkerResponse'),)
rszvb_GetReferenceMarkerResponse  = prototype(('rszvb_GetReferenceMarkerResponse', rszvbDLL), paramflags)
rszvb_GetReferenceMarkerResponse.name = 'rszvb_GetReferenceMarkerResponse'
rszvb_GetReferenceMarkerResponse.errcheck = __errorcheck__
rszvb_GetReferenceMarkerResponse.output = True
# rszvb_SetReferenceDiscreteMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32 mode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'mode'),)
rszvb_SetReferenceDiscreteMarker  = prototype(('rszvb_SetReferenceDiscreteMarker', rszvbDLL), paramflags)
rszvb_SetReferenceDiscreteMarker.name = 'rszvb_SetReferenceDiscreteMarker'
rszvb_SetReferenceDiscreteMarker.errcheck = __errorcheck__
rszvb_SetReferenceDiscreteMarker.output = False
# rszvb_GetReferenceDiscreteMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32* mode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'mode'),)
rszvb_GetReferenceDiscreteMarker  = prototype(('rszvb_GetReferenceDiscreteMarker', rszvbDLL), paramflags)
rszvb_GetReferenceDiscreteMarker.name = 'rszvb_GetReferenceDiscreteMarker'
rszvb_GetReferenceDiscreteMarker.errcheck = __errorcheck__
rszvb_GetReferenceDiscreteMarker.output = True
# rszvb_SetReferenceFixedMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32 type']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'type'),)
rszvb_SetReferenceFixedMarker  = prototype(('rszvb_SetReferenceFixedMarker', rszvbDLL), paramflags)
rszvb_SetReferenceFixedMarker.name = 'rszvb_SetReferenceFixedMarker'
rszvb_SetReferenceFixedMarker.errcheck = __errorcheck__
rszvb_SetReferenceFixedMarker.output = False
# rszvb_GetReferenceFixedMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32* type']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'type'),)
rszvb_GetReferenceFixedMarker  = prototype(('rszvb_GetReferenceFixedMarker', rszvbDLL), paramflags)
rszvb_GetReferenceFixedMarker.name = 'rszvb_GetReferenceFixedMarker'
rszvb_GetReferenceFixedMarker.errcheck = __errorcheck__
rszvb_GetReferenceFixedMarker.output = True
# rszvb_SetDeltaMarkerState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean deltaMarkerState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'deltaMarkerState'),)
rszvb_SetDeltaMarkerState  = prototype(('rszvb_SetDeltaMarkerState', rszvbDLL), paramflags)
rszvb_SetDeltaMarkerState.name = 'rszvb_SetDeltaMarkerState'
rszvb_SetDeltaMarkerState.errcheck = __errorcheck__
rszvb_SetDeltaMarkerState.output = False
# rszvb_GetDeltaMarkerState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean* deltaMarkerState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'deltaMarkerState'),)
rszvb_GetDeltaMarkerState  = prototype(('rszvb_GetDeltaMarkerState', rszvbDLL), paramflags)
rszvb_GetDeltaMarkerState.name = 'rszvb_GetDeltaMarkerState'
rszvb_GetDeltaMarkerState.errcheck = __errorcheck__
rszvb_GetDeltaMarkerState.output = True
# rszvb_SetCoupledMarkers ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean markerCoupled']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'markerCoupled'),)
rszvb_SetCoupledMarkers  = prototype(('rszvb_SetCoupledMarkers', rszvbDLL), paramflags)
rszvb_SetCoupledMarkers.name = 'rszvb_SetCoupledMarkers'
rszvb_SetCoupledMarkers.errcheck = __errorcheck__
rszvb_SetCoupledMarkers.output = False
# rszvb_GetCoupledMarkers ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean* markerCoupled']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'markerCoupled'),)
rszvb_GetCoupledMarkers  = prototype(('rszvb_GetCoupledMarkers', rszvbDLL), paramflags)
rszvb_GetCoupledMarkers.name = 'rszvb_GetCoupledMarkers'
rszvb_GetCoupledMarkers.errcheck = __errorcheck__
rszvb_GetCoupledMarkers.output = True
# rszvb_SetDiscreteMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32 discreteMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'discreteMode'),)
rszvb_SetDiscreteMarker  = prototype(('rszvb_SetDiscreteMarker', rszvbDLL), paramflags)
rszvb_SetDiscreteMarker.name = 'rszvb_SetDiscreteMarker'
rszvb_SetDiscreteMarker.errcheck = __errorcheck__
rszvb_SetDiscreteMarker.output = False
# rszvb_GetDiscreteMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32* discreteMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'discreteMode'),)
rszvb_GetDiscreteMarker  = prototype(('rszvb_GetDiscreteMarker', rszvbDLL), paramflags)
rszvb_GetDiscreteMarker.name = 'rszvb_GetDiscreteMarker'
rszvb_GetDiscreteMarker.errcheck = __errorcheck__
rszvb_GetDiscreteMarker.output = True
# rszvb_SetFixedMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32 fixedMarker']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'fixedMarker'),)
rszvb_SetFixedMarker  = prototype(('rszvb_SetFixedMarker', rszvbDLL), paramflags)
rszvb_SetFixedMarker.name = 'rszvb_SetFixedMarker'
rszvb_SetFixedMarker.errcheck = __errorcheck__
rszvb_SetFixedMarker.output = False
# rszvb_GetFixedMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32* fixedMarker']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'fixedMarker'),)
rszvb_GetFixedMarker  = prototype(('rszvb_GetFixedMarker', rszvbDLL), paramflags)
rszvb_GetFixedMarker.name = 'rszvb_GetFixedMarker'
rszvb_GetFixedMarker.errcheck = __errorcheck__
rszvb_GetFixedMarker.output = True
# rszvb_SetMarkerFormat ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32 markerFormat']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'markerFormat'),)
rszvb_SetMarkerFormat  = prototype(('rszvb_SetMarkerFormat', rszvbDLL), paramflags)
rszvb_SetMarkerFormat.name = 'rszvb_SetMarkerFormat'
rszvb_SetMarkerFormat.errcheck = __errorcheck__
rszvb_SetMarkerFormat.output = False
# rszvb_GetMarkerFormat ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32* markerFormat']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'markerFormat'),)
rszvb_GetMarkerFormat  = prototype(('rszvb_GetMarkerFormat', rszvbDLL), paramflags)
rszvb_GetMarkerFormat.name = 'rszvb_GetMarkerFormat'
rszvb_GetMarkerFormat.errcheck = __errorcheck__
rszvb_GetMarkerFormat.output = True
# rszvb_SetAllMarkersOff ['ViSession instrumentHandle', 'ViInt32 channel_Trace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),)
rszvb_SetAllMarkersOff  = prototype(('rszvb_SetAllMarkersOff', rszvbDLL), paramflags)
rszvb_SetAllMarkersOff.name = 'rszvb_SetAllMarkersOff'
rszvb_SetAllMarkersOff.errcheck = __errorcheck__
rszvb_SetAllMarkersOff.output = False
# rszvb_SaveAllMarkers ['ViSession instrumentHandle', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),)
rszvb_SaveAllMarkers  = prototype(('rszvb_SaveAllMarkers', rszvbDLL), paramflags)
rszvb_SaveAllMarkers.name = 'rszvb_SaveAllMarkers'
rszvb_SaveAllMarkers.errcheck = __errorcheck__
rszvb_SaveAllMarkers.output = False
# rszvb_MarkerSearch ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32 search']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'search'),)
rszvb_MarkerSearch  = prototype(('rszvb_MarkerSearch', rszvbDLL), paramflags)
rszvb_MarkerSearch.name = 'rszvb_MarkerSearch'
rszvb_MarkerSearch.errcheck = __errorcheck__
rszvb_MarkerSearch.output = False
# rszvb_MarkerTargetSearch ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32 search']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'search'),)
rszvb_MarkerTargetSearch  = prototype(('rszvb_MarkerTargetSearch', rszvbDLL), paramflags)
rszvb_MarkerTargetSearch.name = 'rszvb_MarkerTargetSearch'
rszvb_MarkerTargetSearch.errcheck = __errorcheck__
rszvb_MarkerTargetSearch.output = False
# rszvb_SetMarkerTargetValue ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64 targetValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'targetValue'),)
rszvb_SetMarkerTargetValue  = prototype(('rszvb_SetMarkerTargetValue', rszvbDLL), paramflags)
rszvb_SetMarkerTargetValue.name = 'rszvb_SetMarkerTargetValue'
rszvb_SetMarkerTargetValue.errcheck = __errorcheck__
rszvb_SetMarkerTargetValue.output = False
# rszvb_GetMarkerTargetValue ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64* targetValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'targetValue'),)
rszvb_GetMarkerTargetValue  = prototype(('rszvb_GetMarkerTargetValue', rszvbDLL), paramflags)
rszvb_GetMarkerTargetValue.name = 'rszvb_GetMarkerTargetValue'
rszvb_GetMarkerTargetValue.errcheck = __errorcheck__
rszvb_GetMarkerTargetValue.output = True
# rszvb_MarkerBandpassSearch ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),)
rszvb_MarkerBandpassSearch  = prototype(('rszvb_MarkerBandpassSearch', rszvbDLL), paramflags)
rszvb_MarkerBandpassSearch.name = 'rszvb_MarkerBandpassSearch'
rszvb_MarkerBandpassSearch.errcheck = __errorcheck__
rszvb_MarkerBandpassSearch.output = False
# rszvb_MarkerBandstopSearch ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),)
rszvb_MarkerBandstopSearch  = prototype(('rszvb_MarkerBandstopSearch', rszvbDLL), paramflags)
rszvb_MarkerBandstopSearch.name = 'rszvb_MarkerBandstopSearch'
rszvb_MarkerBandstopSearch.errcheck = __errorcheck__
rszvb_MarkerBandstopSearch.output = False
# rszvb_SetMarkerSearchMode ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32 searchMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'searchMode'),)
rszvb_SetMarkerSearchMode  = prototype(('rszvb_SetMarkerSearchMode', rszvbDLL), paramflags)
rszvb_SetMarkerSearchMode.name = 'rszvb_SetMarkerSearchMode'
rszvb_SetMarkerSearchMode.errcheck = __errorcheck__
rszvb_SetMarkerSearchMode.output = False
# rszvb_GetMarkerSearchMode ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32* searchMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'searchMode'),)
rszvb_GetMarkerSearchMode  = prototype(('rszvb_GetMarkerSearchMode', rszvbDLL), paramflags)
rszvb_GetMarkerSearchMode.name = 'rszvb_GetMarkerSearchMode'
rszvb_GetMarkerSearchMode.errcheck = __errorcheck__
rszvb_GetMarkerSearchMode.output = True
# rszvb_MarkerBandfilterTracking ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean bandfilterTracking']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'bandfilterTracking'),)
rszvb_MarkerBandfilterTracking  = prototype(('rszvb_MarkerBandfilterTracking', rszvbDLL), paramflags)
rszvb_MarkerBandfilterTracking.name = 'rszvb_MarkerBandfilterTracking'
rszvb_MarkerBandfilterTracking.errcheck = __errorcheck__
rszvb_MarkerBandfilterTracking.output = False
# rszvb_MarkerxdBBandwidth ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64 xDBBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'xDBBandwidth'),)
rszvb_MarkerxdBBandwidth  = prototype(('rszvb_MarkerxdBBandwidth', rszvbDLL), paramflags)
rszvb_MarkerxdBBandwidth.name = 'rszvb_MarkerxdBBandwidth'
rszvb_MarkerxdBBandwidth.errcheck = __errorcheck__
rszvb_MarkerxdBBandwidth.output = False
# rszvb_MarkerBandfilterResults ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64* bandwidth', 'ViReal64* centerStimulus', 'ViReal64* q', 'ViReal64* loss', 'ViReal64* LBE', 'ViReal64* UBE']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double),POINTER(c_double),POINTER(c_double),POINTER(c_double),POINTER(c_double),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'bandwidth'),(2, 'centerStimulus'),(2, 'q'),(2, 'loss'),(2, 'LBE'),(2, 'UBE'),)
rszvb_MarkerBandfilterResults  = prototype(('rszvb_MarkerBandfilterResults', rszvbDLL), paramflags)
rszvb_MarkerBandfilterResults.name = 'rszvb_MarkerBandfilterResults'
rszvb_MarkerBandfilterResults.errcheck = __errorcheck__
rszvb_MarkerBandfilterResults.output = True
# rszvb_MarkerxdBBandwidthZVR ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64 xDBBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'xDBBandwidth'),)
rszvb_MarkerxdBBandwidthZVR  = prototype(('rszvb_MarkerxdBBandwidthZVR', rszvbDLL), paramflags)
rszvb_MarkerxdBBandwidthZVR.name = 'rszvb_MarkerxdBBandwidthZVR'
rszvb_MarkerxdBBandwidthZVR.errcheck = __errorcheck__
rszvb_MarkerxdBBandwidthZVR.output = False
# rszvb_MarkerBandfilterResultsZVR ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64* bandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'bandwidth'),)
rszvb_MarkerBandfilterResultsZVR  = prototype(('rszvb_MarkerBandfilterResultsZVR', rszvbDLL), paramflags)
rszvb_MarkerBandfilterResultsZVR.name = 'rszvb_MarkerBandfilterResultsZVR'
rszvb_MarkerBandfilterResultsZVR.errcheck = __errorcheck__
rszvb_MarkerBandfilterResultsZVR.output = True
# rszvb_SetMarkerSearchResultState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean searchResults']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'searchResults'),)
rszvb_SetMarkerSearchResultState  = prototype(('rszvb_SetMarkerSearchResultState', rszvbDLL), paramflags)
rszvb_SetMarkerSearchResultState.name = 'rszvb_SetMarkerSearchResultState'
rszvb_SetMarkerSearchResultState.errcheck = __errorcheck__
rszvb_SetMarkerSearchResultState.output = False
# rszvb_GetMarkerSearchResultState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean* searchResults']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'searchResults'),)
rszvb_GetMarkerSearchResultState  = prototype(('rszvb_GetMarkerSearchResultState', rszvbDLL), paramflags)
rszvb_GetMarkerSearchResultState.name = 'rszvb_GetMarkerSearchResultState'
rszvb_GetMarkerSearchResultState.errcheck = __errorcheck__
rszvb_GetMarkerSearchResultState.output = True
# rszvb_SetMarkerTracking ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean markerTracking']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'markerTracking'),)
rszvb_SetMarkerTracking  = prototype(('rszvb_SetMarkerTracking', rszvbDLL), paramflags)
rszvb_SetMarkerTracking.name = 'rszvb_SetMarkerTracking'
rszvb_SetMarkerTracking.errcheck = __errorcheck__
rszvb_SetMarkerTracking.output = False
# rszvb_GetMarkerTracking ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean* markerTracking']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'markerTracking'),)
rszvb_GetMarkerTracking  = prototype(('rszvb_GetMarkerTracking', rszvbDLL), paramflags)
rszvb_GetMarkerTracking.name = 'rszvb_GetMarkerTracking'
rszvb_GetMarkerTracking.errcheck = __errorcheck__
rszvb_GetMarkerTracking.output = True
# rszvb_MarkerSearchRange ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViInt32 searchRange', 'ViReal64 start', 'ViReal64 stop']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'searchRange'),(1, 'start'),(1, 'stop'),)
rszvb_MarkerSearchRange  = prototype(('rszvb_MarkerSearchRange', rszvbDLL), paramflags)
rszvb_MarkerSearchRange.name = 'rszvb_MarkerSearchRange'
rszvb_MarkerSearchRange.errcheck = __errorcheck__
rszvb_MarkerSearchRange.output = False
# rszvb_SetMarkerSearchRangeShow ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean showRange']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(1, 'showRange'),)
rszvb_SetMarkerSearchRangeShow  = prototype(('rszvb_SetMarkerSearchRangeShow', rszvbDLL), paramflags)
rszvb_SetMarkerSearchRangeShow.name = 'rszvb_SetMarkerSearchRangeShow'
rszvb_SetMarkerSearchRangeShow.errcheck = __errorcheck__
rszvb_SetMarkerSearchRangeShow.output = False
# rszvb_GetMarkerSearchRangeShow ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViBoolean* showRange']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'showRange'),)
rszvb_GetMarkerSearchRangeShow  = prototype(('rszvb_GetMarkerSearchRangeShow', rszvbDLL), paramflags)
rszvb_GetMarkerSearchRangeShow.name = 'rszvb_GetMarkerSearchRangeShow'
rszvb_GetMarkerSearchRangeShow.errcheck = __errorcheck__
rszvb_GetMarkerSearchRangeShow.output = True
# rszvb_MarkerSearchResults ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker', 'ViReal64* markerStimulus', 'ViReal64 _VI_FAR markerResponse[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),(2, 'markerStimulus'),(1, 'markerResponse[]'),)
rszvb_MarkerSearchResults  = prototype(('rszvb_MarkerSearchResults', rszvbDLL), paramflags)
rszvb_MarkerSearchResults.name = 'rszvb_MarkerSearchResults'
rszvb_MarkerSearchResults.errcheck = __errorcheck__
rszvb_MarkerSearchResults.output = True
# rszvb_SetStartToMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),)
rszvb_SetStartToMarker  = prototype(('rszvb_SetStartToMarker', rszvbDLL), paramflags)
rszvb_SetStartToMarker.name = 'rszvb_SetStartToMarker'
rszvb_SetStartToMarker.errcheck = __errorcheck__
rszvb_SetStartToMarker.output = False
# rszvb_SetStopToMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),)
rszvb_SetStopToMarker  = prototype(('rszvb_SetStopToMarker', rszvbDLL), paramflags)
rszvb_SetStopToMarker.name = 'rszvb_SetStopToMarker'
rszvb_SetStopToMarker.errcheck = __errorcheck__
rszvb_SetStopToMarker.output = False
# rszvb_SetCenterToMarker ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 marker']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'marker'),)
rszvb_SetCenterToMarker  = prototype(('rszvb_SetCenterToMarker', rszvbDLL), paramflags)
rszvb_SetCenterToMarker.name = 'rszvb_SetCenterToMarker'
rszvb_SetCenterToMarker.errcheck = __errorcheck__
rszvb_SetCenterToMarker.output = False
# rszvb_ShowLimitLine ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean displayLimitLine']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'displayLimitLine'),)
rszvb_ShowLimitLine  = prototype(('rszvb_ShowLimitLine', rszvbDLL), paramflags)
rszvb_ShowLimitLine.name = 'rszvb_ShowLimitLine'
rszvb_ShowLimitLine.errcheck = __errorcheck__
rszvb_ShowLimitLine.output = False
# rszvb_SetLimitCheck ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 limitLine', 'ViBoolean limitCheck']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'limitLine'),(1, 'limitCheck'),)
rszvb_SetLimitCheck  = prototype(('rszvb_SetLimitCheck', rszvbDLL), paramflags)
rszvb_SetLimitCheck.name = 'rszvb_SetLimitCheck'
rszvb_SetLimitCheck.errcheck = __errorcheck__
rszvb_SetLimitCheck.output = False
# rszvb_GetLimitCheck ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 limitLine', 'ViBoolean* limitCheck']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'limitLine'),(2, 'limitCheck'),)
rszvb_GetLimitCheck  = prototype(('rszvb_GetLimitCheck', rszvbDLL), paramflags)
rszvb_GetLimitCheck.name = 'rszvb_GetLimitCheck'
rszvb_GetLimitCheck.errcheck = __errorcheck__
rszvb_GetLimitCheck.output = True
# rszvb_SetLimitLineFailBeep ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean failBeep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'failBeep'),)
rszvb_SetLimitLineFailBeep  = prototype(('rszvb_SetLimitLineFailBeep', rszvbDLL), paramflags)
rszvb_SetLimitLineFailBeep.name = 'rszvb_SetLimitLineFailBeep'
rszvb_SetLimitLineFailBeep.errcheck = __errorcheck__
rszvb_SetLimitLineFailBeep.output = False
# rszvb_GetLimitLineFailBeep ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* failBeep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'failBeep'),)
rszvb_GetLimitLineFailBeep  = prototype(('rszvb_GetLimitLineFailBeep', rszvbDLL), paramflags)
rszvb_GetLimitLineFailBeep.name = 'rszvb_GetLimitLineFailBeep'
rszvb_GetLimitLineFailBeep.errcheck = __errorcheck__
rszvb_GetLimitLineFailBeep.output = True
# rszvb_GetLimitCheckResult ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* limitCheckResult']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'limitCheckResult'),)
rszvb_GetLimitCheckResult  = prototype(('rszvb_GetLimitCheckResult', rszvbDLL), paramflags)
rszvb_GetLimitCheckResult.name = 'rszvb_GetLimitCheckResult'
rszvb_GetLimitCheckResult.errcheck = __errorcheck__
rszvb_GetLimitCheckResult.output = True
# rszvb_AddLimitLineSegment ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 segment', 'ViInt32 type', 'ViReal64 startStimulus', 'ViReal64 stopStimulus', 'ViReal64 startResponse', 'ViReal64 stopResponse']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_double,c_double,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'segment'),(1, 'type'),(1, 'startStimulus'),(1, 'stopStimulus'),(1, 'startResponse'),(1, 'stopResponse'),)
rszvb_AddLimitLineSegment  = prototype(('rszvb_AddLimitLineSegment', rszvbDLL), paramflags)
rszvb_AddLimitLineSegment.name = 'rszvb_AddLimitLineSegment'
rszvb_AddLimitLineSegment.errcheck = __errorcheck__
rszvb_AddLimitLineSegment.output = False
# rszvb_EditLimitLineSegment ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 segment', 'ViInt32 type', 'ViReal64 startStimulus', 'ViReal64 stopStimulus', 'ViReal64 startResponse', 'ViReal64 stopResponse']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_double,c_double,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'segment'),(1, 'type'),(1, 'startStimulus'),(1, 'stopStimulus'),(1, 'startResponse'),(1, 'stopResponse'),)
rszvb_EditLimitLineSegment  = prototype(('rszvb_EditLimitLineSegment', rszvbDLL), paramflags)
rszvb_EditLimitLineSegment.name = 'rszvb_EditLimitLineSegment'
rszvb_EditLimitLineSegment.errcheck = __errorcheck__
rszvb_EditLimitLineSegment.output = False
# rszvb_ReadLimitLineSegmentList ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 listSize', 'ViInt32* segmentsCount', 'ViInt32 _VI_FAR type[]', 'ViReal64 _VI_FAR startStimulus[]', 'ViReal64 _VI_FAR stopStimulus[]', 'ViReal64 _VI_FAR startResponse[]', 'ViReal64 _VI_FAR stopResponse[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'listSize'),(2, 'segmentsCount'),(1, 'type[]'),(1, 'startStimulus[]'),(1, 'stopStimulus[]'),(1, 'startResponse[]'),(1, 'stopResponse[]'),)
rszvb_ReadLimitLineSegmentList  = prototype(('rszvb_ReadLimitLineSegmentList', rszvbDLL), paramflags)
rszvb_ReadLimitLineSegmentList.name = 'rszvb_ReadLimitLineSegmentList'
rszvb_ReadLimitLineSegmentList.errcheck = __errorcheck__
rszvb_ReadLimitLineSegmentList.output = True
# rszvb_WriteLimitLineSegmentList ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 listSize', 'ViInt32 type', 'ViReal64 _VI_FAR startStimulus[]', 'ViReal64 _VI_FAR stopStimulus[]', 'ViReal64 _VI_FAR startResponse[]', 'ViReal64 _VI_FAR stopResponse[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'listSize'),(1, 'type'),(1, 'startStimulus[]'),(1, 'stopStimulus[]'),(1, 'startResponse[]'),(1, 'stopResponse[]'),)
rszvb_WriteLimitLineSegmentList  = prototype(('rszvb_WriteLimitLineSegmentList', rszvbDLL), paramflags)
rszvb_WriteLimitLineSegmentList.name = 'rszvb_WriteLimitLineSegmentList'
rszvb_WriteLimitLineSegmentList.errcheck = __errorcheck__
rszvb_WriteLimitLineSegmentList.output = False
# rszvb_ShiftLimitLineSegmentList ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 limitLineType', 'ViReal64 stimulusOffset', 'ViReal64 responseOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'limitLineType'),(1, 'stimulusOffset'),(1, 'responseOffset'),)
rszvb_ShiftLimitLineSegmentList  = prototype(('rszvb_ShiftLimitLineSegmentList', rszvbDLL), paramflags)
rszvb_ShiftLimitLineSegmentList.name = 'rszvb_ShiftLimitLineSegmentList'
rszvb_ShiftLimitLineSegmentList.errcheck = __errorcheck__
rszvb_ShiftLimitLineSegmentList.output = False
# rszvb_DeleteLimitLineSegments ['ViSession instrumentHandle', 'ViInt32 channel_Trace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),)
rszvb_DeleteLimitLineSegments  = prototype(('rszvb_DeleteLimitLineSegments', rszvbDLL), paramflags)
rszvb_DeleteLimitLineSegments.name = 'rszvb_DeleteLimitLineSegments'
rszvb_DeleteLimitLineSegments.errcheck = __errorcheck__
rszvb_DeleteLimitLineSegments.output = False
# rszvb_RecallLimitLine ['ViSession instrumentHandle', 'ViString traceName', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(1, 'fileName'),)
rszvb_RecallLimitLine  = prototype(('rszvb_RecallLimitLine', rszvbDLL), paramflags)
rszvb_RecallLimitLine.name = 'rszvb_RecallLimitLine'
rszvb_RecallLimitLine.errcheck = __errorcheck__
rszvb_RecallLimitLine.output = False
# rszvb_RecallLimitLineWithOptions ['ViSession instrumentHandle', 'ViString traceName', 'ViString fileName', 'ViString sParameter', 'ViReal64 xOffset', 'ViReal64 yOffset', 'ViInt32 type']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p,c_char_p,c_double,c_double,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(1, 'fileName'),(1, 'sParameter'),(1, 'xOffset'),(1, 'yOffset'),(1, 'type'),)
rszvb_RecallLimitLineWithOptions  = prototype(('rszvb_RecallLimitLineWithOptions', rszvbDLL), paramflags)
rszvb_RecallLimitLineWithOptions.name = 'rszvb_RecallLimitLineWithOptions'
rszvb_RecallLimitLineWithOptions.errcheck = __errorcheck__
rszvb_RecallLimitLineWithOptions.output = False
# rszvb_SaveLimitLine ['ViSession instrumentHandle', 'ViString traceName', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(1, 'fileName'),)
rszvb_SaveLimitLine  = prototype(('rszvb_SaveLimitLine', rszvbDLL), paramflags)
rszvb_SaveLimitLine.name = 'rszvb_SaveLimitLine'
rszvb_SaveLimitLine.errcheck = __errorcheck__
rszvb_SaveLimitLine.output = False
# rszvb_ImportTraceasLimitLine ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 limitLineType', 'ViReal64 stimulusOffset', 'ViReal64 responseOffset', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'limitLineType'),(1, 'stimulusOffset'),(1, 'responseOffset'),(1, 'traceName'),)
rszvb_ImportTraceasLimitLine  = prototype(('rszvb_ImportTraceasLimitLine', rszvbDLL), paramflags)
rszvb_ImportTraceasLimitLine.name = 'rszvb_ImportTraceasLimitLine'
rszvb_ImportTraceasLimitLine.errcheck = __errorcheck__
rszvb_ImportTraceasLimitLine.output = False
# rszvb_SetLimitLineTTLOutPass ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 outputNo', 'ViBoolean TTLOutput']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'outputNo'),(1, 'TTLOutput'),)
rszvb_SetLimitLineTTLOutPass  = prototype(('rszvb_SetLimitLineTTLOutPass', rszvbDLL), paramflags)
rszvb_SetLimitLineTTLOutPass.name = 'rszvb_SetLimitLineTTLOutPass'
rszvb_SetLimitLineTTLOutPass.errcheck = __errorcheck__
rszvb_SetLimitLineTTLOutPass.output = False
# rszvb_GetLimitLineTTLOutPass ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 outputNo', 'ViBoolean* TTLOutput']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'outputNo'),(2, 'TTLOutput'),)
rszvb_GetLimitLineTTLOutPass  = prototype(('rszvb_GetLimitLineTTLOutPass', rszvbDLL), paramflags)
rszvb_GetLimitLineTTLOutPass.name = 'rszvb_GetLimitLineTTLOutPass'
rszvb_GetLimitLineTTLOutPass.errcheck = __errorcheck__
rszvb_GetLimitLineTTLOutPass.output = True
# rszvb_SetDisplayLine ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean displayLine', 'ViReal64 position']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'displayLine'),(1, 'position'),)
rszvb_SetDisplayLine  = prototype(('rszvb_SetDisplayLine', rszvbDLL), paramflags)
rszvb_SetDisplayLine.name = 'rszvb_SetDisplayLine'
rszvb_SetDisplayLine.errcheck = __errorcheck__
rszvb_SetDisplayLine.output = False
# rszvb_GetDisplayLine ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* displayLine', 'ViReal64* position']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'displayLine'),(2, 'position'),)
rszvb_GetDisplayLine  = prototype(('rszvb_GetDisplayLine', rszvbDLL), paramflags)
rszvb_GetDisplayLine.name = 'rszvb_GetDisplayLine'
rszvb_GetDisplayLine.errcheck = __errorcheck__
rszvb_GetDisplayLine.output = True
# rszvb_SetLimitDomainUnits ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 domainUnits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'domainUnits'),)
rszvb_SetLimitDomainUnits  = prototype(('rszvb_SetLimitDomainUnits', rszvbDLL), paramflags)
rszvb_SetLimitDomainUnits.name = 'rszvb_SetLimitDomainUnits'
rszvb_SetLimitDomainUnits.errcheck = __errorcheck__
rszvb_SetLimitDomainUnits.output = False
# rszvb_SetLimitResponseDomainComplexUnits ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 responseUnits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'responseUnits'),)
rszvb_SetLimitResponseDomainComplexUnits  = prototype(('rszvb_SetLimitResponseDomainComplexUnits', rszvbDLL), paramflags)
rszvb_SetLimitResponseDomainComplexUnits.name = 'rszvb_SetLimitResponseDomainComplexUnits'
rszvb_SetLimitResponseDomainComplexUnits.errcheck = __errorcheck__
rszvb_SetLimitResponseDomainComplexUnits.output = False
# rszvb_SetLimitResponseDomainFormatUnits ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 responseUnits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'responseUnits'),)
rszvb_SetLimitResponseDomainFormatUnits  = prototype(('rszvb_SetLimitResponseDomainFormatUnits', rszvbDLL), paramflags)
rszvb_SetLimitResponseDomainFormatUnits.name = 'rszvb_SetLimitResponseDomainFormatUnits'
rszvb_SetLimitResponseDomainFormatUnits.errcheck = __errorcheck__
rszvb_SetLimitResponseDomainFormatUnits.output = False
# rszvb_SetLimitResponseDomainSpacingUnits ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 responseUnits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'responseUnits'),)
rszvb_SetLimitResponseDomainSpacingUnits  = prototype(('rszvb_SetLimitResponseDomainSpacingUnits', rszvbDLL), paramflags)
rszvb_SetLimitResponseDomainSpacingUnits.name = 'rszvb_SetLimitResponseDomainSpacingUnits'
rszvb_SetLimitResponseDomainSpacingUnits.errcheck = __errorcheck__
rszvb_SetLimitResponseDomainSpacingUnits.output = False
# rszvb_SetRippleCheckOn ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean limitCheck']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'limitCheck'),)
rszvb_SetRippleCheckOn  = prototype(('rszvb_SetRippleCheckOn', rszvbDLL), paramflags)
rszvb_SetRippleCheckOn.name = 'rszvb_SetRippleCheckOn'
rszvb_SetRippleCheckOn.errcheck = __errorcheck__
rszvb_SetRippleCheckOn.output = False
# rszvb_GetRippleCheckOn ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* limitCheck']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'limitCheck'),)
rszvb_GetRippleCheckOn  = prototype(('rszvb_GetRippleCheckOn', rszvbDLL), paramflags)
rszvb_GetRippleCheckOn.name = 'rszvb_GetRippleCheckOn'
rszvb_GetRippleCheckOn.errcheck = __errorcheck__
rszvb_GetRippleCheckOn.output = True
# rszvb_GetRippleLimitGlobalCheckResult ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* rippleLimitCheckResult']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'rippleLimitCheckResult'),)
rszvb_GetRippleLimitGlobalCheckResult  = prototype(('rszvb_GetRippleLimitGlobalCheckResult', rszvbDLL), paramflags)
rszvb_GetRippleLimitGlobalCheckResult.name = 'rszvb_GetRippleLimitGlobalCheckResult'
rszvb_GetRippleLimitGlobalCheckResult.errcheck = __errorcheck__
rszvb_GetRippleLimitGlobalCheckResult.output = True
# rszvb_SetCheckRippleLimitRangeSegment ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 segment', 'ViBoolean limitCheck']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'segment'),(1, 'limitCheck'),)
rszvb_SetCheckRippleLimitRangeSegment  = prototype(('rszvb_SetCheckRippleLimitRangeSegment', rszvbDLL), paramflags)
rszvb_SetCheckRippleLimitRangeSegment.name = 'rszvb_SetCheckRippleLimitRangeSegment'
rszvb_SetCheckRippleLimitRangeSegment.errcheck = __errorcheck__
rszvb_SetCheckRippleLimitRangeSegment.output = False
# rszvb_GetCheckRippleLimitRangeSegment ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 segment', 'ViBoolean* limitCheck']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'segment'),(2, 'limitCheck'),)
rszvb_GetCheckRippleLimitRangeSegment  = prototype(('rszvb_GetCheckRippleLimitRangeSegment', rszvbDLL), paramflags)
rszvb_GetCheckRippleLimitRangeSegment.name = 'rszvb_GetCheckRippleLimitRangeSegment'
rszvb_GetCheckRippleLimitRangeSegment.errcheck = __errorcheck__
rszvb_GetCheckRippleLimitRangeSegment.output = True
# rszvb_GetRippleLimitCheckSegmentResult ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 segment', 'ViInt32* fail', 'ViReal64* limitCheckResult']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'segment'),(2, 'fail'),(2, 'limitCheckResult'),)
rszvb_GetRippleLimitCheckSegmentResult  = prototype(('rszvb_GetRippleLimitCheckSegmentResult', rszvbDLL), paramflags)
rszvb_GetRippleLimitCheckSegmentResult.name = 'rszvb_GetRippleLimitCheckSegmentResult'
rszvb_GetRippleLimitCheckSegmentResult.errcheck = __errorcheck__
rszvb_GetRippleLimitCheckSegmentResult.output = True
# rszvb_SetRippleLimitsDisplayState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean displayLine']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'displayLine'),)
rszvb_SetRippleLimitsDisplayState  = prototype(('rszvb_SetRippleLimitsDisplayState', rszvbDLL), paramflags)
rszvb_SetRippleLimitsDisplayState.name = 'rszvb_SetRippleLimitsDisplayState'
rszvb_SetRippleLimitsDisplayState.errcheck = __errorcheck__
rszvb_SetRippleLimitsDisplayState.output = False
# rszvb_GetRippleLimitsDisplayState ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* displayLine']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'displayLine'),)
rszvb_GetRippleLimitsDisplayState  = prototype(('rszvb_GetRippleLimitsDisplayState', rszvbDLL), paramflags)
rszvb_GetRippleLimitsDisplayState.name = 'rszvb_GetRippleLimitsDisplayState'
rszvb_GetRippleLimitsDisplayState.errcheck = __errorcheck__
rszvb_GetRippleLimitsDisplayState.output = True
# rszvb_SetRippleFailBeepOn ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean failBeep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'failBeep'),)
rszvb_SetRippleFailBeepOn  = prototype(('rszvb_SetRippleFailBeepOn', rszvbDLL), paramflags)
rszvb_SetRippleFailBeepOn.name = 'rszvb_SetRippleFailBeepOn'
rszvb_SetRippleFailBeepOn.errcheck = __errorcheck__
rszvb_SetRippleFailBeepOn.output = False
# rszvb_GetRippleFailBeepOn ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViBoolean* failBeep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'failBeep'),)
rszvb_GetRippleFailBeepOn  = prototype(('rszvb_GetRippleFailBeepOn', rszvbDLL), paramflags)
rszvb_GetRippleFailBeepOn.name = 'rszvb_GetRippleFailBeepOn'
rszvb_GetRippleFailBeepOn.errcheck = __errorcheck__
rszvb_GetRippleFailBeepOn.output = True
# rszvb_AddRippleLimitLineRangesSegment ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 noOfValues', 'ViInt32 _VI_FAR type[]', 'ViReal64 _VI_FAR startStimulus[]', 'ViReal64 _VI_FAR stopStimulus[]', 'ViReal64 _VI_FAR limit[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'noOfValues'),(1, 'type[]'),(1, 'startStimulus[]'),(1, 'stopStimulus[]'),(1, 'limit[]'),)
rszvb_AddRippleLimitLineRangesSegment  = prototype(('rszvb_AddRippleLimitLineRangesSegment', rszvbDLL), paramflags)
rszvb_AddRippleLimitLineRangesSegment.name = 'rszvb_AddRippleLimitLineRangesSegment'
rszvb_AddRippleLimitLineRangesSegment.errcheck = __errorcheck__
rszvb_AddRippleLimitLineRangesSegment.output = False
# rszvb_EditRippleLimitLineSegment ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 segment', 'ViReal64 startStimulus', 'ViReal64 stopStimulus']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'segment'),(1, 'startStimulus'),(1, 'stopStimulus'),)
rszvb_EditRippleLimitLineSegment  = prototype(('rszvb_EditRippleLimitLineSegment', rszvbDLL), paramflags)
rszvb_EditRippleLimitLineSegment.name = 'rszvb_EditRippleLimitLineSegment'
rszvb_EditRippleLimitLineSegment.errcheck = __errorcheck__
rszvb_EditRippleLimitLineSegment.output = False
# rszvb_DeleteAllRippleLimitRanges ['ViSession instrumentHandle', 'ViInt32 channel_Trace']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),)
rszvb_DeleteAllRippleLimitRanges  = prototype(('rszvb_DeleteAllRippleLimitRanges', rszvbDLL), paramflags)
rszvb_DeleteAllRippleLimitRanges.name = 'rszvb_DeleteAllRippleLimitRanges'
rszvb_DeleteAllRippleLimitRanges.errcheck = __errorcheck__
rszvb_DeleteAllRippleLimitRanges.output = False
# rszvb_SetRippleLimitPhysicalUnits ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 physicalUnits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'physicalUnits'),)
rszvb_SetRippleLimitPhysicalUnits  = prototype(('rszvb_SetRippleLimitPhysicalUnits', rszvbDLL), paramflags)
rszvb_SetRippleLimitPhysicalUnits.name = 'rszvb_SetRippleLimitPhysicalUnits'
rszvb_SetRippleLimitPhysicalUnits.errcheck = __errorcheck__
rszvb_SetRippleLimitPhysicalUnits.output = False
# rszvb_SetRippleLimitResponseDomainFormatUnits ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 responseUnits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'responseUnits'),)
rszvb_SetRippleLimitResponseDomainFormatUnits  = prototype(('rszvb_SetRippleLimitResponseDomainFormatUnits', rszvbDLL), paramflags)
rszvb_SetRippleLimitResponseDomainFormatUnits.name = 'rszvb_SetRippleLimitResponseDomainFormatUnits'
rszvb_SetRippleLimitResponseDomainFormatUnits.errcheck = __errorcheck__
rszvb_SetRippleLimitResponseDomainFormatUnits.output = False
# rszvb_GetNumberRippleLimitRanges ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 segment', 'ViInt32* number']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'segment'),(2, 'number'),)
rszvb_GetNumberRippleLimitRanges  = prototype(('rszvb_GetNumberRippleLimitRanges', rszvbDLL), paramflags)
rszvb_GetNumberRippleLimitRanges.name = 'rszvb_GetNumberRippleLimitRanges'
rszvb_GetNumberRippleLimitRanges.errcheck = __errorcheck__
rszvb_GetNumberRippleLimitRanges.output = True
# rszvb_SetRippleLimitRange ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 segment', 'ViReal64 limit']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'segment'),(1, 'limit'),)
rszvb_SetRippleLimitRange  = prototype(('rszvb_SetRippleLimitRange', rszvbDLL), paramflags)
rszvb_SetRippleLimitRange.name = 'rszvb_SetRippleLimitRange'
rszvb_SetRippleLimitRange.errcheck = __errorcheck__
rszvb_SetRippleLimitRange.output = False
# rszvb_GetRippleLimitRange ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32 segment', 'ViReal64* limit']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(1, 'segment'),(2, 'limit'),)
rszvb_GetRippleLimitRange  = prototype(('rszvb_GetRippleLimitRange', rszvbDLL), paramflags)
rszvb_GetRippleLimitRange.name = 'rszvb_GetRippleLimitRange'
rszvb_GetRippleLimitRange.errcheck = __errorcheck__
rszvb_GetRippleLimitRange.output = True
# rszvb_SaveRecallRippleLimit ['ViSession instrumentHandle', 'ViInt32 operationToBePerformed', 'ViString traceName', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'operationToBePerformed'),(1, 'traceName'),(1, 'fileName'),)
rszvb_SaveRecallRippleLimit  = prototype(('rszvb_SaveRecallRippleLimit', rszvbDLL), paramflags)
rszvb_SaveRecallRippleLimit.name = 'rszvb_SaveRecallRippleLimit'
rszvb_SaveRecallRippleLimit.errcheck = __errorcheck__
rszvb_SaveRecallRippleLimit.output = False
# rszvb_SetStartFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 startFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'startFrequency'),)
rszvb_SetStartFrequency  = prototype(('rszvb_SetStartFrequency', rszvbDLL), paramflags)
rszvb_SetStartFrequency.name = 'rszvb_SetStartFrequency'
rszvb_SetStartFrequency.errcheck = __errorcheck__
rszvb_SetStartFrequency.output = False
# rszvb_GetStartFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* startFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'startFrequency'),)
rszvb_GetStartFrequency  = prototype(('rszvb_GetStartFrequency', rszvbDLL), paramflags)
rszvb_GetStartFrequency.name = 'rszvb_GetStartFrequency'
rszvb_GetStartFrequency.errcheck = __errorcheck__
rszvb_GetStartFrequency.output = True
# rszvb_SetStopFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 stopFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'stopFrequency'),)
rszvb_SetStopFrequency  = prototype(('rszvb_SetStopFrequency', rszvbDLL), paramflags)
rszvb_SetStopFrequency.name = 'rszvb_SetStopFrequency'
rszvb_SetStopFrequency.errcheck = __errorcheck__
rszvb_SetStopFrequency.output = False
# rszvb_GetStopFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* stopFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'stopFrequency'),)
rszvb_GetStopFrequency  = prototype(('rszvb_GetStopFrequency', rszvbDLL), paramflags)
rszvb_GetStopFrequency.name = 'rszvb_GetStopFrequency'
rszvb_GetStopFrequency.errcheck = __errorcheck__
rszvb_GetStopFrequency.output = True
# rszvb_SetCenterFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 centerFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'centerFrequency'),)
rszvb_SetCenterFrequency  = prototype(('rszvb_SetCenterFrequency', rszvbDLL), paramflags)
rszvb_SetCenterFrequency.name = 'rszvb_SetCenterFrequency'
rszvb_SetCenterFrequency.errcheck = __errorcheck__
rszvb_SetCenterFrequency.output = False
# rszvb_GetCenterFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* centerFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'centerFrequency'),)
rszvb_GetCenterFrequency  = prototype(('rszvb_GetCenterFrequency', rszvbDLL), paramflags)
rszvb_GetCenterFrequency.name = 'rszvb_GetCenterFrequency'
rszvb_GetCenterFrequency.errcheck = __errorcheck__
rszvb_GetCenterFrequency.output = True
# rszvb_SetFrequencySpan ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 span']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'span'),)
rszvb_SetFrequencySpan  = prototype(('rszvb_SetFrequencySpan', rszvbDLL), paramflags)
rszvb_SetFrequencySpan.name = 'rszvb_SetFrequencySpan'
rszvb_SetFrequencySpan.errcheck = __errorcheck__
rszvb_SetFrequencySpan.output = False
# rszvb_GetFrequencySpan ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* span']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'span'),)
rszvb_GetFrequencySpan  = prototype(('rszvb_GetFrequencySpan', rszvbDLL), paramflags)
rszvb_GetFrequencySpan.name = 'rszvb_GetFrequencySpan'
rszvb_GetFrequencySpan.errcheck = __errorcheck__
rszvb_GetFrequencySpan.output = True
# rszvb_SetPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 power']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'power'),)
rszvb_SetPower  = prototype(('rszvb_SetPower', rszvbDLL), paramflags)
rszvb_SetPower.name = 'rszvb_SetPower'
rszvb_SetPower.errcheck = __errorcheck__
rszvb_SetPower.output = False
# rszvb_GetPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* power']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'power'),)
rszvb_GetPower  = prototype(('rszvb_GetPower', rszvbDLL), paramflags)
rszvb_GetPower.name = 'rszvb_GetPower'
rszvb_GetPower.errcheck = __errorcheck__
rszvb_GetPower.output = True
# rszvb_SetCWFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 CWFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'CWFrequency'),)
rszvb_SetCWFrequency  = prototype(('rszvb_SetCWFrequency', rszvbDLL), paramflags)
rszvb_SetCWFrequency.name = 'rszvb_SetCWFrequency'
rszvb_SetCWFrequency.errcheck = __errorcheck__
rszvb_SetCWFrequency.output = False
# rszvb_GetCWFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* CWFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'CWFrequency'),)
rszvb_GetCWFrequency  = prototype(('rszvb_GetCWFrequency', rszvbDLL), paramflags)
rszvb_GetCWFrequency.name = 'rszvb_GetCWFrequency'
rszvb_GetCWFrequency.errcheck = __errorcheck__
rszvb_GetCWFrequency.output = True
# rszvb_SetStartPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 startPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'startPower'),)
rszvb_SetStartPower  = prototype(('rszvb_SetStartPower', rszvbDLL), paramflags)
rszvb_SetStartPower.name = 'rszvb_SetStartPower'
rszvb_SetStartPower.errcheck = __errorcheck__
rszvb_SetStartPower.output = False
# rszvb_GetStartPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* startPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'startPower'),)
rszvb_GetStartPower  = prototype(('rszvb_GetStartPower', rszvbDLL), paramflags)
rszvb_GetStartPower.name = 'rszvb_GetStartPower'
rszvb_GetStartPower.errcheck = __errorcheck__
rszvb_GetStartPower.output = True
# rszvb_SetStopPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 stopPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'stopPower'),)
rszvb_SetStopPower  = prototype(('rszvb_SetStopPower', rszvbDLL), paramflags)
rszvb_SetStopPower.name = 'rszvb_SetStopPower'
rszvb_SetStopPower.errcheck = __errorcheck__
rszvb_SetStopPower.output = False
# rszvb_GetStopPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* stopPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'stopPower'),)
rszvb_GetStopPower  = prototype(('rszvb_GetStopPower', rszvbDLL), paramflags)
rszvb_GetStopPower.name = 'rszvb_GetStopPower'
rszvb_GetStopPower.errcheck = __errorcheck__
rszvb_GetStopPower.output = True
# rszvb_SetSourcePort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 sourcePort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'sourcePort'),)
rszvb_SetSourcePort  = prototype(('rszvb_SetSourcePort', rszvbDLL), paramflags)
rszvb_SetSourcePort.name = 'rszvb_SetSourcePort'
rszvb_SetSourcePort.errcheck = __errorcheck__
rszvb_SetSourcePort.output = False
# rszvb_GetSourcePort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* sourcePort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'sourcePort'),)
rszvb_GetSourcePort  = prototype(('rszvb_GetSourcePort', rszvbDLL), paramflags)
rszvb_GetSourcePort.name = 'rszvb_GetSourcePort'
rszvb_GetSourcePort.errcheck = __errorcheck__
rszvb_GetSourcePort.output = True
# rszvb_ConfigurePowerBandwidthAverage ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean RFState', 'ViReal64 measBandwidth', 'ViBoolean averageState', 'ViInt32 averageFactor']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool,c_double,c_bool,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'RFState'),(1, 'measBandwidth'),(1, 'averageState'),(1, 'averageFactor'),)
rszvb_ConfigurePowerBandwidthAverage  = prototype(('rszvb_ConfigurePowerBandwidthAverage', rszvbDLL), paramflags)
rszvb_ConfigurePowerBandwidthAverage.name = 'rszvb_ConfigurePowerBandwidthAverage'
rszvb_ConfigurePowerBandwidthAverage.errcheck = __errorcheck__
rszvb_ConfigurePowerBandwidthAverage.output = False
# rszvb_SetReceiverStepAttenuators ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 analyzerPort', 'ViReal64 attenuationFactor']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'analyzerPort'),(1, 'attenuationFactor'),)
rszvb_SetReceiverStepAttenuators  = prototype(('rszvb_SetReceiverStepAttenuators', rszvbDLL), paramflags)
rszvb_SetReceiverStepAttenuators.name = 'rszvb_SetReceiverStepAttenuators'
rszvb_SetReceiverStepAttenuators.errcheck = __errorcheck__
rszvb_SetReceiverStepAttenuators.output = False
# rszvb_GetReceiverStepAttenuators ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 analyzerPort', 'ViReal64* attenuationFactor']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'analyzerPort'),(2, 'attenuationFactor'),)
rszvb_GetReceiverStepAttenuators  = prototype(('rszvb_GetReceiverStepAttenuators', rszvbDLL), paramflags)
rszvb_GetReceiverStepAttenuators.name = 'rszvb_GetReceiverStepAttenuators'
rszvb_GetReceiverStepAttenuators.errcheck = __errorcheck__
rszvb_GetReceiverStepAttenuators.output = True
# rszvb_SetGeneratorStepAttenuators ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 attenuationFactor']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'attenuationFactor'),)
rszvb_SetGeneratorStepAttenuators  = prototype(('rszvb_SetGeneratorStepAttenuators', rszvbDLL), paramflags)
rszvb_SetGeneratorStepAttenuators.name = 'rszvb_SetGeneratorStepAttenuators'
rszvb_SetGeneratorStepAttenuators.errcheck = __errorcheck__
rszvb_SetGeneratorStepAttenuators.output = False
# rszvb_GetGeneratorStepAttenuators ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* attenuationFactor']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'attenuationFactor'),)
rszvb_GetGeneratorStepAttenuators  = prototype(('rszvb_GetGeneratorStepAttenuators', rszvbDLL), paramflags)
rszvb_GetGeneratorStepAttenuators.name = 'rszvb_GetGeneratorStepAttenuators'
rszvb_GetGeneratorStepAttenuators.errcheck = __errorcheck__
rszvb_GetGeneratorStepAttenuators.output = True
# rszvb_SetAutomaticGeneratorAttenuator ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean automaticAttenuation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'automaticAttenuation'),)
rszvb_SetAutomaticGeneratorAttenuator  = prototype(('rszvb_SetAutomaticGeneratorAttenuator', rszvbDLL), paramflags)
rszvb_SetAutomaticGeneratorAttenuator.name = 'rszvb_SetAutomaticGeneratorAttenuator'
rszvb_SetAutomaticGeneratorAttenuator.errcheck = __errorcheck__
rszvb_SetAutomaticGeneratorAttenuator.output = False
# rszvb_GetAutomaticGeneratorAttenuator ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* automaticAttenuation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'automaticAttenuation'),)
rszvb_GetAutomaticGeneratorAttenuator  = prototype(('rszvb_GetAutomaticGeneratorAttenuator', rszvbDLL), paramflags)
rszvb_GetAutomaticGeneratorAttenuator.name = 'rszvb_GetAutomaticGeneratorAttenuator'
rszvb_GetAutomaticGeneratorAttenuator.errcheck = __errorcheck__
rszvb_GetAutomaticGeneratorAttenuator.output = True
# rszvb_GetAutomaticGeneratorAttenuation ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* attenuation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'attenuation'),)
rszvb_GetAutomaticGeneratorAttenuation  = prototype(('rszvb_GetAutomaticGeneratorAttenuation', rszvbDLL), paramflags)
rszvb_GetAutomaticGeneratorAttenuation.name = 'rszvb_GetAutomaticGeneratorAttenuation'
rszvb_GetAutomaticGeneratorAttenuation.errcheck = __errorcheck__
rszvb_GetAutomaticGeneratorAttenuation.output = True
# rszvb_SetGeneratorAttenuatorMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 attenuationMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'attenuationMode'),)
rszvb_SetGeneratorAttenuatorMode  = prototype(('rszvb_SetGeneratorAttenuatorMode', rszvbDLL), paramflags)
rszvb_SetGeneratorAttenuatorMode.name = 'rszvb_SetGeneratorAttenuatorMode'
rszvb_SetGeneratorAttenuatorMode.errcheck = __errorcheck__
rszvb_SetGeneratorAttenuatorMode.output = False
# rszvb_GetGeneratorAttenuatorMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* attenuationMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'attenuationMode'),)
rszvb_GetGeneratorAttenuatorMode  = prototype(('rszvb_GetGeneratorAttenuatorMode', rszvbDLL), paramflags)
rszvb_GetGeneratorAttenuatorMode.name = 'rszvb_GetGeneratorAttenuatorMode'
rszvb_GetGeneratorAttenuatorMode.errcheck = __errorcheck__
rszvb_GetGeneratorAttenuatorMode.output = True
# rszvb_SetRFState ['ViSession instrumentHandle', 'ViBoolean RFState']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'RFState'),)
rszvb_SetRFState  = prototype(('rszvb_SetRFState', rszvbDLL), paramflags)
rszvb_SetRFState.name = 'rszvb_SetRFState'
rszvb_SetRFState.errcheck = __errorcheck__
rszvb_SetRFState.output = False
# rszvb_GetRFState ['ViSession instrumentHandle', 'ViBoolean* RFState']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'RFState'),)
rszvb_GetRFState  = prototype(('rszvb_GetRFState', rszvbDLL), paramflags)
rszvb_GetRFState.name = 'rszvb_GetRFState'
rszvb_GetRFState.errcheck = __errorcheck__
rszvb_GetRFState.output = True
# rszvb_SetMeasBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 measBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'measBandwidth'),)
rszvb_SetMeasBandwidth  = prototype(('rszvb_SetMeasBandwidth', rszvbDLL), paramflags)
rszvb_SetMeasBandwidth.name = 'rszvb_SetMeasBandwidth'
rszvb_SetMeasBandwidth.errcheck = __errorcheck__
rszvb_SetMeasBandwidth.output = False
# rszvb_GetMeasBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* measBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'measBandwidth'),)
rszvb_GetMeasBandwidth  = prototype(('rszvb_GetMeasBandwidth', rszvbDLL), paramflags)
rszvb_GetMeasBandwidth.name = 'rszvb_GetMeasBandwidth'
rszvb_GetMeasBandwidth.errcheck = __errorcheck__
rszvb_GetMeasBandwidth.output = True
# rszvb_SetMeasBandwidthSelectivity ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 measBandwidthSelectivity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'measBandwidthSelectivity'),)
rszvb_SetMeasBandwidthSelectivity  = prototype(('rszvb_SetMeasBandwidthSelectivity', rszvbDLL), paramflags)
rszvb_SetMeasBandwidthSelectivity.name = 'rszvb_SetMeasBandwidthSelectivity'
rszvb_SetMeasBandwidthSelectivity.errcheck = __errorcheck__
rszvb_SetMeasBandwidthSelectivity.output = False
# rszvb_GetMeasBandwidthSelectivity ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* measBandwidthSelectivity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'measBandwidthSelectivity'),)
rszvb_GetMeasBandwidthSelectivity  = prototype(('rszvb_GetMeasBandwidthSelectivity', rszvbDLL), paramflags)
rszvb_GetMeasBandwidthSelectivity.name = 'rszvb_GetMeasBandwidthSelectivity'
rszvb_GetMeasBandwidthSelectivity.errcheck = __errorcheck__
rszvb_GetMeasBandwidthSelectivity.output = True
# rszvb_SetMeasBandwidthReduction ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean reduction']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'reduction'),)
rszvb_SetMeasBandwidthReduction  = prototype(('rszvb_SetMeasBandwidthReduction', rszvbDLL), paramflags)
rszvb_SetMeasBandwidthReduction.name = 'rszvb_SetMeasBandwidthReduction'
rszvb_SetMeasBandwidthReduction.errcheck = __errorcheck__
rszvb_SetMeasBandwidthReduction.output = False
# rszvb_GetMeasBandwidthReduction ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* reduction']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'reduction'),)
rszvb_GetMeasBandwidthReduction  = prototype(('rszvb_GetMeasBandwidthReduction', rszvbDLL), paramflags)
rszvb_GetMeasBandwidthReduction.name = 'rszvb_GetMeasBandwidthReduction'
rszvb_GetMeasBandwidthReduction.errcheck = __errorcheck__
rszvb_GetMeasBandwidthReduction.output = True
# rszvb_SetAverageState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean averageState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'averageState'),)
rszvb_SetAverageState  = prototype(('rszvb_SetAverageState', rszvbDLL), paramflags)
rszvb_SetAverageState.name = 'rszvb_SetAverageState'
rszvb_SetAverageState.errcheck = __errorcheck__
rszvb_SetAverageState.output = False
# rszvb_GetAverageState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* averageState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'averageState'),)
rszvb_GetAverageState  = prototype(('rszvb_GetAverageState', rszvbDLL), paramflags)
rszvb_GetAverageState.name = 'rszvb_GetAverageState'
rszvb_GetAverageState.errcheck = __errorcheck__
rszvb_GetAverageState.output = True
# rszvb_SetAverageFactor ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 averageFactor']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'averageFactor'),)
rszvb_SetAverageFactor  = prototype(('rszvb_SetAverageFactor', rszvbDLL), paramflags)
rszvb_SetAverageFactor.name = 'rszvb_SetAverageFactor'
rszvb_SetAverageFactor.errcheck = __errorcheck__
rszvb_SetAverageFactor.output = False
# rszvb_GetAverageFactor ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* averageFactor']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'averageFactor'),)
rszvb_GetAverageFactor  = prototype(('rszvb_GetAverageFactor', rszvbDLL), paramflags)
rszvb_GetAverageFactor.name = 'rszvb_GetAverageFactor'
rszvb_GetAverageFactor.errcheck = __errorcheck__
rszvb_GetAverageFactor.output = True
# rszvb_GetCurrentSweep ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* currentSweep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'currentSweep'),)
rszvb_GetCurrentSweep  = prototype(('rszvb_GetCurrentSweep', rszvbDLL), paramflags)
rszvb_GetCurrentSweep.name = 'rszvb_GetCurrentSweep'
rszvb_GetCurrentSweep.errcheck = __errorcheck__
rszvb_GetCurrentSweep.output = True
# rszvb_RestartAverage ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_RestartAverage  = prototype(('rszvb_RestartAverage', rszvbDLL), paramflags)
rszvb_RestartAverage.name = 'rszvb_RestartAverage'
rszvb_RestartAverage.errcheck = __errorcheck__
rszvb_RestartAverage.output = False
# rszvb_SetPartialMeasurementResolutionBandwidthMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 bandwidthMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'bandwidthMode'),)
rszvb_SetPartialMeasurementResolutionBandwidthMode  = prototype(('rszvb_SetPartialMeasurementResolutionBandwidthMode', rszvbDLL), paramflags)
rszvb_SetPartialMeasurementResolutionBandwidthMode.name = 'rszvb_SetPartialMeasurementResolutionBandwidthMode'
rszvb_SetPartialMeasurementResolutionBandwidthMode.errcheck = __errorcheck__
rszvb_SetPartialMeasurementResolutionBandwidthMode.output = False
# rszvb_GetPartialMeasurementResolutionBandwidthMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* bandwidthMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'bandwidthMode'),)
rszvb_GetPartialMeasurementResolutionBandwidthMode  = prototype(('rszvb_GetPartialMeasurementResolutionBandwidthMode', rszvbDLL), paramflags)
rszvb_GetPartialMeasurementResolutionBandwidthMode.name = 'rszvb_GetPartialMeasurementResolutionBandwidthMode'
rszvb_GetPartialMeasurementResolutionBandwidthMode.errcheck = __errorcheck__
rszvb_GetPartialMeasurementResolutionBandwidthMode.output = True
# rszvb_SetGeneratorPortResolutionBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generatorPort', 'ViReal64 resolutionBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generatorPort'),(1, 'resolutionBandwidth'),)
rszvb_SetGeneratorPortResolutionBandwidth  = prototype(('rszvb_SetGeneratorPortResolutionBandwidth', rszvbDLL), paramflags)
rszvb_SetGeneratorPortResolutionBandwidth.name = 'rszvb_SetGeneratorPortResolutionBandwidth'
rszvb_SetGeneratorPortResolutionBandwidth.errcheck = __errorcheck__
rszvb_SetGeneratorPortResolutionBandwidth.output = False
# rszvb_GetGeneratorPortResolutionBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generatorPort', 'ViReal64* resolutionBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generatorPort'),(2, 'resolutionBandwidth'),)
rszvb_GetGeneratorPortResolutionBandwidth  = prototype(('rszvb_GetGeneratorPortResolutionBandwidth', rszvbDLL), paramflags)
rszvb_GetGeneratorPortResolutionBandwidth.name = 'rszvb_GetGeneratorPortResolutionBandwidth'
rszvb_GetGeneratorPortResolutionBandwidth.errcheck = __errorcheck__
rszvb_GetGeneratorPortResolutionBandwidth.output = True
# rszvb_SetPhysicalPortResolutionBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 analyzerPort', 'ViReal64 resolutionBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'analyzerPort'),(1, 'resolutionBandwidth'),)
rszvb_SetPhysicalPortResolutionBandwidth  = prototype(('rszvb_SetPhysicalPortResolutionBandwidth', rszvbDLL), paramflags)
rszvb_SetPhysicalPortResolutionBandwidth.name = 'rszvb_SetPhysicalPortResolutionBandwidth'
rszvb_SetPhysicalPortResolutionBandwidth.errcheck = __errorcheck__
rszvb_SetPhysicalPortResolutionBandwidth.output = False
# rszvb_GetPhysicalPortResolutionBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 analyzerPort', 'ViReal64* resolutionBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'analyzerPort'),(2, 'resolutionBandwidth'),)
rszvb_GetPhysicalPortResolutionBandwidth  = prototype(('rszvb_GetPhysicalPortResolutionBandwidth', rszvbDLL), paramflags)
rszvb_GetPhysicalPortResolutionBandwidth.name = 'rszvb_GetPhysicalPortResolutionBandwidth'
rszvb_GetPhysicalPortResolutionBandwidth.errcheck = __errorcheck__
rszvb_GetPhysicalPortResolutionBandwidth.output = True
# rszvb_SetSweepType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'sweepType'),)
rszvb_SetSweepType  = prototype(('rszvb_SetSweepType', rszvbDLL), paramflags)
rszvb_SetSweepType.name = 'rszvb_SetSweepType'
rszvb_SetSweepType.errcheck = __errorcheck__
rszvb_SetSweepType.output = False
# rszvb_GetSweepType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'sweepType'),)
rszvb_GetSweepType  = prototype(('rszvb_GetSweepType', rszvbDLL), paramflags)
rszvb_GetSweepType.name = 'rszvb_GetSweepType'
rszvb_GetSweepType.errcheck = __errorcheck__
rszvb_GetSweepType.output = True
# rszvb_InsertNewSegment ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64 startFrequency', 'ViReal64 stopFrequency', 'ViInt32 numberOfPoints', 'ViReal64 power', 'ViInt32 sweepTimeSelect', 'ViReal64 time', 'ViReal64 pointDelay', 'ViReal64 measBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double,c_int32,c_double,c_int32,c_double,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'startFrequency'),(1, 'stopFrequency'),(1, 'numberOfPoints'),(1, 'power'),(1, 'sweepTimeSelect'),(1, 'time'),(1, 'pointDelay'),(1, 'measBandwidth'),)
rszvb_InsertNewSegment  = prototype(('rszvb_InsertNewSegment', rszvbDLL), paramflags)
rszvb_InsertNewSegment.name = 'rszvb_InsertNewSegment'
rszvb_InsertNewSegment.errcheck = __errorcheck__
rszvb_InsertNewSegment.output = False
# rszvb_RedefineSegment ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64 startFrequency', 'ViReal64 stopFrequency', 'ViInt32 numberOfPoints', 'ViReal64 power', 'ViInt32 sweepTimeSelect', 'ViReal64 time', 'ViReal64 pointDelay', 'ViReal64 measBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double,c_int32,c_double,c_int32,c_double,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'startFrequency'),(1, 'stopFrequency'),(1, 'numberOfPoints'),(1, 'power'),(1, 'sweepTimeSelect'),(1, 'time'),(1, 'pointDelay'),(1, 'measBandwidth'),)
rszvb_RedefineSegment  = prototype(('rszvb_RedefineSegment', rszvbDLL), paramflags)
rszvb_RedefineSegment.name = 'rszvb_RedefineSegment'
rszvb_RedefineSegment.errcheck = __errorcheck__
rszvb_RedefineSegment.output = False
# rszvb_AddNewSegment ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),)
rszvb_AddNewSegment  = prototype(('rszvb_AddNewSegment', rszvbDLL), paramflags)
rszvb_AddNewSegment.name = 'rszvb_AddNewSegment'
rszvb_AddNewSegment.errcheck = __errorcheck__
rszvb_AddNewSegment.output = False
# rszvb_DeleteSelectedSegment ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),)
rszvb_DeleteSelectedSegment  = prototype(('rszvb_DeleteSelectedSegment', rszvbDLL), paramflags)
rszvb_DeleteSelectedSegment.name = 'rszvb_DeleteSelectedSegment'
rszvb_DeleteSelectedSegment.errcheck = __errorcheck__
rszvb_DeleteSelectedSegment.output = False
# rszvb_DeleteAllSegments ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_DeleteAllSegments  = prototype(('rszvb_DeleteAllSegments', rszvbDLL), paramflags)
rszvb_DeleteAllSegments.name = 'rszvb_DeleteAllSegments'
rszvb_DeleteAllSegments.errcheck = __errorcheck__
rszvb_DeleteAllSegments.output = False
# rszvb_GetSweepSegmentsCount ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* count']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'count'),)
rszvb_GetSweepSegmentsCount  = prototype(('rszvb_GetSweepSegmentsCount', rszvbDLL), paramflags)
rszvb_GetSweepSegmentsCount.name = 'rszvb_GetSweepSegmentsCount'
rszvb_GetSweepSegmentsCount.errcheck = __errorcheck__
rszvb_GetSweepSegmentsCount.output = True
# rszvb_SetSweepSegmentState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'state'),)
rszvb_SetSweepSegmentState  = prototype(('rszvb_SetSweepSegmentState', rszvbDLL), paramflags)
rszvb_SetSweepSegmentState.name = 'rszvb_SetSweepSegmentState'
rszvb_SetSweepSegmentState.errcheck = __errorcheck__
rszvb_SetSweepSegmentState.output = False
# rszvb_GetSweepSegmentState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'state'),)
rszvb_GetSweepSegmentState  = prototype(('rszvb_GetSweepSegmentState', rszvbDLL), paramflags)
rszvb_GetSweepSegmentState.name = 'rszvb_GetSweepSegmentState'
rszvb_GetSweepSegmentState.errcheck = __errorcheck__
rszvb_GetSweepSegmentState.output = True
# rszvb_SetSweepSegmentStartFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64 startFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'startFrequency'),)
rszvb_SetSweepSegmentStartFrequency  = prototype(('rszvb_SetSweepSegmentStartFrequency', rszvbDLL), paramflags)
rszvb_SetSweepSegmentStartFrequency.name = 'rszvb_SetSweepSegmentStartFrequency'
rszvb_SetSweepSegmentStartFrequency.errcheck = __errorcheck__
rszvb_SetSweepSegmentStartFrequency.output = False
# rszvb_GetSweepSegmentStartFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64* startFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'startFrequency'),)
rszvb_GetSweepSegmentStartFrequency  = prototype(('rszvb_GetSweepSegmentStartFrequency', rszvbDLL), paramflags)
rszvb_GetSweepSegmentStartFrequency.name = 'rszvb_GetSweepSegmentStartFrequency'
rszvb_GetSweepSegmentStartFrequency.errcheck = __errorcheck__
rszvb_GetSweepSegmentStartFrequency.output = True
# rszvb_SetSweepSegmentStopFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64 stopFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'stopFrequency'),)
rszvb_SetSweepSegmentStopFrequency  = prototype(('rszvb_SetSweepSegmentStopFrequency', rszvbDLL), paramflags)
rszvb_SetSweepSegmentStopFrequency.name = 'rszvb_SetSweepSegmentStopFrequency'
rszvb_SetSweepSegmentStopFrequency.errcheck = __errorcheck__
rszvb_SetSweepSegmentStopFrequency.output = False
# rszvb_GetSweepSegmentStopFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64* stopFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'stopFrequency'),)
rszvb_GetSweepSegmentStopFrequency  = prototype(('rszvb_GetSweepSegmentStopFrequency', rszvbDLL), paramflags)
rszvb_GetSweepSegmentStopFrequency.name = 'rszvb_GetSweepSegmentStopFrequency'
rszvb_GetSweepSegmentStopFrequency.errcheck = __errorcheck__
rszvb_GetSweepSegmentStopFrequency.output = True
# rszvb_SetSweepSegmentNumberOfPoints ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViInt32 numberOfPoints']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'numberOfPoints'),)
rszvb_SetSweepSegmentNumberOfPoints  = prototype(('rszvb_SetSweepSegmentNumberOfPoints', rszvbDLL), paramflags)
rszvb_SetSweepSegmentNumberOfPoints.name = 'rszvb_SetSweepSegmentNumberOfPoints'
rszvb_SetSweepSegmentNumberOfPoints.errcheck = __errorcheck__
rszvb_SetSweepSegmentNumberOfPoints.output = False
# rszvb_GetSweepSegmentNumberOfPoints ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViInt32* numberOfPoints']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'numberOfPoints'),)
rszvb_GetSweepSegmentNumberOfPoints  = prototype(('rszvb_GetSweepSegmentNumberOfPoints', rszvbDLL), paramflags)
rszvb_GetSweepSegmentNumberOfPoints.name = 'rszvb_GetSweepSegmentNumberOfPoints'
rszvb_GetSweepSegmentNumberOfPoints.errcheck = __errorcheck__
rszvb_GetSweepSegmentNumberOfPoints.output = True
# rszvb_SetSweepSegmentName ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViString name']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'name'),)
rszvb_SetSweepSegmentName  = prototype(('rszvb_SetSweepSegmentName', rszvbDLL), paramflags)
rszvb_SetSweepSegmentName.name = 'rszvb_SetSweepSegmentName'
rszvb_SetSweepSegmentName.errcheck = __errorcheck__
rszvb_SetSweepSegmentName.output = False
# rszvb_GetSweepSegmentName ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViInt32 bufferSize', 'ViChar _VI_FAR name[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'bufferSize'),(1, 'name[]'),)
rszvb_GetSweepSegmentName  = prototype(('rszvb_GetSweepSegmentName', rszvbDLL), paramflags)
rszvb_GetSweepSegmentName.name = 'rszvb_GetSweepSegmentName'
rszvb_GetSweepSegmentName.errcheck = __errorcheck__
rszvb_GetSweepSegmentName.output = False
# rszvb_SetSweepSegmentPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64 power']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'power'),)
rszvb_SetSweepSegmentPower  = prototype(('rszvb_SetSweepSegmentPower', rszvbDLL), paramflags)
rszvb_SetSweepSegmentPower.name = 'rszvb_SetSweepSegmentPower'
rszvb_SetSweepSegmentPower.errcheck = __errorcheck__
rszvb_SetSweepSegmentPower.output = False
# rszvb_GetSweepSegmentPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64* power']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'power'),)
rszvb_GetSweepSegmentPower  = prototype(('rszvb_GetSweepSegmentPower', rszvbDLL), paramflags)
rszvb_GetSweepSegmentPower.name = 'rszvb_GetSweepSegmentPower'
rszvb_GetSweepSegmentPower.errcheck = __errorcheck__
rszvb_GetSweepSegmentPower.output = True
# rszvb_SetSweepSegmentIndependentPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean power']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'power'),)
rszvb_SetSweepSegmentIndependentPower  = prototype(('rszvb_SetSweepSegmentIndependentPower', rszvbDLL), paramflags)
rszvb_SetSweepSegmentIndependentPower.name = 'rszvb_SetSweepSegmentIndependentPower'
rszvb_SetSweepSegmentIndependentPower.errcheck = __errorcheck__
rszvb_SetSweepSegmentIndependentPower.output = False
# rszvb_GetSweepSegmentIndependentPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean* power']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'power'),)
rszvb_GetSweepSegmentIndependentPower  = prototype(('rszvb_GetSweepSegmentIndependentPower', rszvbDLL), paramflags)
rszvb_GetSweepSegmentIndependentPower.name = 'rszvb_GetSweepSegmentIndependentPower'
rszvb_GetSweepSegmentIndependentPower.errcheck = __errorcheck__
rszvb_GetSweepSegmentIndependentPower.output = True
# rszvb_SetSweepSegmentMeasBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64 measBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'measBandwidth'),)
rszvb_SetSweepSegmentMeasBandwidth  = prototype(('rszvb_SetSweepSegmentMeasBandwidth', rszvbDLL), paramflags)
rszvb_SetSweepSegmentMeasBandwidth.name = 'rszvb_SetSweepSegmentMeasBandwidth'
rszvb_SetSweepSegmentMeasBandwidth.errcheck = __errorcheck__
rszvb_SetSweepSegmentMeasBandwidth.output = False
# rszvb_GetSweepSegmentMeasBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64* measBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'measBandwidth'),)
rszvb_GetSweepSegmentMeasBandwidth  = prototype(('rszvb_GetSweepSegmentMeasBandwidth', rszvbDLL), paramflags)
rszvb_GetSweepSegmentMeasBandwidth.name = 'rszvb_GetSweepSegmentMeasBandwidth'
rszvb_GetSweepSegmentMeasBandwidth.errcheck = __errorcheck__
rszvb_GetSweepSegmentMeasBandwidth.output = True
# rszvb_SetSweepSegmentIndependentBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean measBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'measBandwidth'),)
rszvb_SetSweepSegmentIndependentBandwidth  = prototype(('rszvb_SetSweepSegmentIndependentBandwidth', rszvbDLL), paramflags)
rszvb_SetSweepSegmentIndependentBandwidth.name = 'rszvb_SetSweepSegmentIndependentBandwidth'
rszvb_SetSweepSegmentIndependentBandwidth.errcheck = __errorcheck__
rszvb_SetSweepSegmentIndependentBandwidth.output = False
# rszvb_GetSweepSegmentIndependentBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean* measBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'measBandwidth'),)
rszvb_GetSweepSegmentIndependentBandwidth  = prototype(('rszvb_GetSweepSegmentIndependentBandwidth', rszvbDLL), paramflags)
rszvb_GetSweepSegmentIndependentBandwidth.name = 'rszvb_GetSweepSegmentIndependentBandwidth'
rszvb_GetSweepSegmentIndependentBandwidth.errcheck = __errorcheck__
rszvb_GetSweepSegmentIndependentBandwidth.output = True
# rszvb_SetSweepSegmentSpurAvoid ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViInt32 spurAvoid']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'spurAvoid'),)
rszvb_SetSweepSegmentSpurAvoid  = prototype(('rszvb_SetSweepSegmentSpurAvoid', rszvbDLL), paramflags)
rszvb_SetSweepSegmentSpurAvoid.name = 'rszvb_SetSweepSegmentSpurAvoid'
rszvb_SetSweepSegmentSpurAvoid.errcheck = __errorcheck__
rszvb_SetSweepSegmentSpurAvoid.output = False
# rszvb_GetSweepSegmentSpurAvoid ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViInt32* spurAvoid']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'spurAvoid'),)
rszvb_GetSweepSegmentSpurAvoid  = prototype(('rszvb_GetSweepSegmentSpurAvoid', rszvbDLL), paramflags)
rszvb_GetSweepSegmentSpurAvoid.name = 'rszvb_GetSweepSegmentSpurAvoid'
rszvb_GetSweepSegmentSpurAvoid.errcheck = __errorcheck__
rszvb_GetSweepSegmentSpurAvoid.output = True
# rszvb_SetSweepSegmentIndependentSpurAvoid ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean spurAvoid']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'spurAvoid'),)
rszvb_SetSweepSegmentIndependentSpurAvoid  = prototype(('rszvb_SetSweepSegmentIndependentSpurAvoid', rszvbDLL), paramflags)
rszvb_SetSweepSegmentIndependentSpurAvoid.name = 'rszvb_SetSweepSegmentIndependentSpurAvoid'
rszvb_SetSweepSegmentIndependentSpurAvoid.errcheck = __errorcheck__
rszvb_SetSweepSegmentIndependentSpurAvoid.output = False
# rszvb_GetSweepSegmentIndependentSpurAvoid ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean* spurAvoid']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'spurAvoid'),)
rszvb_GetSweepSegmentIndependentSpurAvoid  = prototype(('rszvb_GetSweepSegmentIndependentSpurAvoid', rszvbDLL), paramflags)
rszvb_GetSweepSegmentIndependentSpurAvoid.name = 'rszvb_GetSweepSegmentIndependentSpurAvoid'
rszvb_GetSweepSegmentIndependentSpurAvoid.errcheck = __errorcheck__
rszvb_GetSweepSegmentIndependentSpurAvoid.output = True
# rszvb_SetSweepSegmentSelectivity ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViInt32 selectivity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'selectivity'),)
rszvb_SetSweepSegmentSelectivity  = prototype(('rszvb_SetSweepSegmentSelectivity', rszvbDLL), paramflags)
rszvb_SetSweepSegmentSelectivity.name = 'rszvb_SetSweepSegmentSelectivity'
rszvb_SetSweepSegmentSelectivity.errcheck = __errorcheck__
rszvb_SetSweepSegmentSelectivity.output = False
# rszvb_GetSweepSegmentSelectivity ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViInt32* selectivity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'selectivity'),)
rszvb_GetSweepSegmentSelectivity  = prototype(('rszvb_GetSweepSegmentSelectivity', rszvbDLL), paramflags)
rszvb_GetSweepSegmentSelectivity.name = 'rszvb_GetSweepSegmentSelectivity'
rszvb_GetSweepSegmentSelectivity.errcheck = __errorcheck__
rszvb_GetSweepSegmentSelectivity.output = True
# rszvb_SetSweepSegmentIndependentSelectivity ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean selectivity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'selectivity'),)
rszvb_SetSweepSegmentIndependentSelectivity  = prototype(('rszvb_SetSweepSegmentIndependentSelectivity', rszvbDLL), paramflags)
rszvb_SetSweepSegmentIndependentSelectivity.name = 'rszvb_SetSweepSegmentIndependentSelectivity'
rszvb_SetSweepSegmentIndependentSelectivity.errcheck = __errorcheck__
rszvb_SetSweepSegmentIndependentSelectivity.output = False
# rszvb_GetSweepSegmentIndependentSelectivity ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean* selectivity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'selectivity'),)
rszvb_GetSweepSegmentIndependentSelectivity  = prototype(('rszvb_GetSweepSegmentIndependentSelectivity', rszvbDLL), paramflags)
rszvb_GetSweepSegmentIndependentSelectivity.name = 'rszvb_GetSweepSegmentIndependentSelectivity'
rszvb_GetSweepSegmentIndependentSelectivity.errcheck = __errorcheck__
rszvb_GetSweepSegmentIndependentSelectivity.output = True
# rszvb_SetSweepSegmentSweepTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64 time']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'time'),)
rszvb_SetSweepSegmentSweepTime  = prototype(('rszvb_SetSweepSegmentSweepTime', rszvbDLL), paramflags)
rszvb_SetSweepSegmentSweepTime.name = 'rszvb_SetSweepSegmentSweepTime'
rszvb_SetSweepSegmentSweepTime.errcheck = __errorcheck__
rszvb_SetSweepSegmentSweepTime.output = False
# rszvb_GetSweepSegmentSweepTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64* time']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'time'),)
rszvb_GetSweepSegmentSweepTime  = prototype(('rszvb_GetSweepSegmentSweepTime', rszvbDLL), paramflags)
rszvb_GetSweepSegmentSweepTime.name = 'rszvb_GetSweepSegmentSweepTime'
rszvb_GetSweepSegmentSweepTime.errcheck = __errorcheck__
rszvb_GetSweepSegmentSweepTime.output = True
# rszvb_SetSweepSegmentIndependentTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean time']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'time'),)
rszvb_SetSweepSegmentIndependentTime  = prototype(('rszvb_SetSweepSegmentIndependentTime', rszvbDLL), paramflags)
rszvb_SetSweepSegmentIndependentTime.name = 'rszvb_SetSweepSegmentIndependentTime'
rszvb_SetSweepSegmentIndependentTime.errcheck = __errorcheck__
rszvb_SetSweepSegmentIndependentTime.output = False
# rszvb_GetSweepSegmentIndependentTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean* time']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'time'),)
rszvb_GetSweepSegmentIndependentTime  = prototype(('rszvb_GetSweepSegmentIndependentTime', rszvbDLL), paramflags)
rszvb_GetSweepSegmentIndependentTime.name = 'rszvb_GetSweepSegmentIndependentTime'
rszvb_GetSweepSegmentIndependentTime.errcheck = __errorcheck__
rszvb_GetSweepSegmentIndependentTime.output = True
# rszvb_SetSweepSegmentPointDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64 pointDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'pointDelay'),)
rszvb_SetSweepSegmentPointDelay  = prototype(('rszvb_SetSweepSegmentPointDelay', rszvbDLL), paramflags)
rszvb_SetSweepSegmentPointDelay.name = 'rszvb_SetSweepSegmentPointDelay'
rszvb_SetSweepSegmentPointDelay.errcheck = __errorcheck__
rszvb_SetSweepSegmentPointDelay.output = False
# rszvb_GetSweepSegmentPointDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64* pointDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'pointDelay'),)
rszvb_GetSweepSegmentPointDelay  = prototype(('rszvb_GetSweepSegmentPointDelay', rszvbDLL), paramflags)
rszvb_GetSweepSegmentPointDelay.name = 'rszvb_GetSweepSegmentPointDelay'
rszvb_GetSweepSegmentPointDelay.errcheck = __errorcheck__
rszvb_GetSweepSegmentPointDelay.output = True
# rszvb_SetSweepSegmentIndependentPointDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean pointDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'pointDelay'),)
rszvb_SetSweepSegmentIndependentPointDelay  = prototype(('rszvb_SetSweepSegmentIndependentPointDelay', rszvbDLL), paramflags)
rszvb_SetSweepSegmentIndependentPointDelay.name = 'rszvb_SetSweepSegmentIndependentPointDelay'
rszvb_SetSweepSegmentIndependentPointDelay.errcheck = __errorcheck__
rszvb_SetSweepSegmentIndependentPointDelay.output = False
# rszvb_GetSweepSegmentIndependentPointDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean* pointDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'pointDelay'),)
rszvb_GetSweepSegmentIndependentPointDelay  = prototype(('rszvb_GetSweepSegmentIndependentPointDelay', rszvbDLL), paramflags)
rszvb_GetSweepSegmentIndependentPointDelay.name = 'rszvb_GetSweepSegmentIndependentPointDelay'
rszvb_GetSweepSegmentIndependentPointDelay.errcheck = __errorcheck__
rszvb_GetSweepSegmentIndependentPointDelay.output = True
# rszvb_SetSweepSegmentTriggering ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean triggering']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'triggering'),)
rszvb_SetSweepSegmentTriggering  = prototype(('rszvb_SetSweepSegmentTriggering', rszvbDLL), paramflags)
rszvb_SetSweepSegmentTriggering.name = 'rszvb_SetSweepSegmentTriggering'
rszvb_SetSweepSegmentTriggering.errcheck = __errorcheck__
rszvb_SetSweepSegmentTriggering.output = False
# rszvb_GetSweepSegmentTriggering ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean* triggering']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'triggering'),)
rszvb_GetSweepSegmentTriggering  = prototype(('rszvb_GetSweepSegmentTriggering', rszvbDLL), paramflags)
rszvb_GetSweepSegmentTriggering.name = 'rszvb_GetSweepSegmentTriggering'
rszvb_GetSweepSegmentTriggering.errcheck = __errorcheck__
rszvb_GetSweepSegmentTriggering.output = True
# rszvb_SetSweepSelectiveSegmentTriggering ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean triggering']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'triggering'),)
rszvb_SetSweepSelectiveSegmentTriggering  = prototype(('rszvb_SetSweepSelectiveSegmentTriggering', rszvbDLL), paramflags)
rszvb_SetSweepSelectiveSegmentTriggering.name = 'rszvb_SetSweepSelectiveSegmentTriggering'
rszvb_SetSweepSelectiveSegmentTriggering.errcheck = __errorcheck__
rszvb_SetSweepSelectiveSegmentTriggering.output = False
# rszvb_GetSweepSelectiveSegmentTriggering ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* triggering']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'triggering'),)
rszvb_GetSweepSelectiveSegmentTriggering  = prototype(('rszvb_GetSweepSelectiveSegmentTriggering', rszvbDLL), paramflags)
rszvb_GetSweepSelectiveSegmentTriggering.name = 'rszvb_GetSweepSelectiveSegmentTriggering'
rszvb_GetSweepSelectiveSegmentTriggering.errcheck = __errorcheck__
rszvb_GetSweepSelectiveSegmentTriggering.output = True
# rszvb_SetSweepSegmentBitsState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetSweepSegmentBitsState  = prototype(('rszvb_SetSweepSegmentBitsState', rszvbDLL), paramflags)
rszvb_SetSweepSegmentBitsState.name = 'rszvb_SetSweepSegmentBitsState'
rszvb_SetSweepSegmentBitsState.errcheck = __errorcheck__
rszvb_SetSweepSegmentBitsState.output = False
# rszvb_GetSweepSegmentBitsState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetSweepSegmentBitsState  = prototype(('rszvb_GetSweepSegmentBitsState', rszvbDLL), paramflags)
rszvb_GetSweepSegmentBitsState.name = 'rszvb_GetSweepSegmentBitsState'
rszvb_GetSweepSegmentBitsState.errcheck = __errorcheck__
rszvb_GetSweepSegmentBitsState.output = True
# rszvb_SetSweepSegmentBitValues ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean bit0', 'ViBoolean bit1', 'ViBoolean bit2', 'ViBoolean bit3']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool,c_bool,c_bool,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'bit0'),(1, 'bit1'),(1, 'bit2'),(1, 'bit3'),)
rszvb_SetSweepSegmentBitValues  = prototype(('rszvb_SetSweepSegmentBitValues', rszvbDLL), paramflags)
rszvb_SetSweepSegmentBitValues.name = 'rszvb_SetSweepSegmentBitValues'
rszvb_SetSweepSegmentBitValues.errcheck = __errorcheck__
rszvb_SetSweepSegmentBitValues.output = False
# rszvb_GetSweepSegmentBitValues ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean* bit0', 'ViBoolean* bit1', 'ViBoolean* bit2', 'ViBoolean* bit3']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool),POINTER(c_bool),POINTER(c_bool),POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'bit0'),(2, 'bit1'),(2, 'bit2'),(2, 'bit3'),)
rszvb_GetSweepSegmentBitValues  = prototype(('rszvb_GetSweepSegmentBitValues', rszvbDLL), paramflags)
rszvb_GetSweepSegmentBitValues.name = 'rszvb_GetSweepSegmentBitValues'
rszvb_GetSweepSegmentBitValues.errcheck = __errorcheck__
rszvb_GetSweepSegmentBitValues.output = True
# rszvb_GetSweepSegmentCenterFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64* centerFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'centerFrequency'),)
rszvb_GetSweepSegmentCenterFrequency  = prototype(('rszvb_GetSweepSegmentCenterFrequency', rszvbDLL), paramflags)
rszvb_GetSweepSegmentCenterFrequency.name = 'rszvb_GetSweepSegmentCenterFrequency'
rszvb_GetSweepSegmentCenterFrequency.errcheck = __errorcheck__
rszvb_GetSweepSegmentCenterFrequency.output = True
# rszvb_GetSweepSegmentFrequencySpan ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64* frequencySpan']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'frequencySpan'),)
rszvb_GetSweepSegmentFrequencySpan  = prototype(('rszvb_GetSweepSegmentFrequencySpan', rszvbDLL), paramflags)
rszvb_GetSweepSegmentFrequencySpan.name = 'rszvb_GetSweepSegmentFrequencySpan'
rszvb_GetSweepSegmentFrequencySpan.errcheck = __errorcheck__
rszvb_GetSweepSegmentFrequencySpan.output = True
# rszvb_SaveSegment ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fileName'),)
rszvb_SaveSegment  = prototype(('rszvb_SaveSegment', rszvbDLL), paramflags)
rszvb_SaveSegment.name = 'rszvb_SaveSegment'
rszvb_SaveSegment.errcheck = __errorcheck__
rszvb_SaveSegment.output = False
# rszvb_LoadSegment ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fileName'),)
rszvb_LoadSegment  = prototype(('rszvb_LoadSegment', rszvbDLL), paramflags)
rszvb_LoadSegment.name = 'rszvb_LoadSegment'
rszvb_LoadSegment.errcheck = __errorcheck__
rszvb_LoadSegment.output = False
# rszvb_QueryOverlappingSweepSegments ['ViSession instrumentHandle', 'ViInt32 segment', 'ViBoolean* overlapping']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'segment'),(2, 'overlapping'),)
rszvb_QueryOverlappingSweepSegments  = prototype(('rszvb_QueryOverlappingSweepSegments', rszvbDLL), paramflags)
rszvb_QueryOverlappingSweepSegments.name = 'rszvb_QueryOverlappingSweepSegments'
rszvb_QueryOverlappingSweepSegments.errcheck = __errorcheck__
rszvb_QueryOverlappingSweepSegments.output = True
# rszvb_QuerySumOfSweepSegmentsTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* sweepTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'sweepTime'),)
rszvb_QuerySumOfSweepSegmentsTime  = prototype(('rszvb_QuerySumOfSweepSegmentsTime', rszvbDLL), paramflags)
rszvb_QuerySumOfSweepSegmentsTime.name = 'rszvb_QuerySumOfSweepSegmentsTime'
rszvb_QuerySumOfSweepSegmentsTime.errcheck = __errorcheck__
rszvb_QuerySumOfSweepSegmentsTime.output = True
# rszvb_SetPulseTimeStart ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 timeStart']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'timeStart'),)
rszvb_SetPulseTimeStart  = prototype(('rszvb_SetPulseTimeStart', rszvbDLL), paramflags)
rszvb_SetPulseTimeStart.name = 'rszvb_SetPulseTimeStart'
rszvb_SetPulseTimeStart.errcheck = __errorcheck__
rszvb_SetPulseTimeStart.output = False
# rszvb_GetPulseTimeStart ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* timeStart']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'timeStart'),)
rszvb_GetPulseTimeStart  = prototype(('rszvb_GetPulseTimeStart', rszvbDLL), paramflags)
rszvb_GetPulseTimeStart.name = 'rszvb_GetPulseTimeStart'
rszvb_GetPulseTimeStart.errcheck = __errorcheck__
rszvb_GetPulseTimeStart.output = True
# rszvb_SetPulseTimeStop ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 timeStop']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'timeStop'),)
rszvb_SetPulseTimeStop  = prototype(('rszvb_SetPulseTimeStop', rszvbDLL), paramflags)
rszvb_SetPulseTimeStop.name = 'rszvb_SetPulseTimeStop'
rszvb_SetPulseTimeStop.errcheck = __errorcheck__
rszvb_SetPulseTimeStop.output = False
# rszvb_GetPulseTimeStop ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* timeStop']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'timeStop'),)
rszvb_GetPulseTimeStop  = prototype(('rszvb_GetPulseTimeStop', rszvbDLL), paramflags)
rszvb_GetPulseTimeStop.name = 'rszvb_GetPulseTimeStop'
rszvb_GetPulseTimeStop.errcheck = __errorcheck__
rszvb_GetPulseTimeStop.output = True
# rszvb_SetPulseTimeBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 timeBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'timeBandwidth'),)
rszvb_SetPulseTimeBandwidth  = prototype(('rszvb_SetPulseTimeBandwidth', rszvbDLL), paramflags)
rszvb_SetPulseTimeBandwidth.name = 'rszvb_SetPulseTimeBandwidth'
rszvb_SetPulseTimeBandwidth.errcheck = __errorcheck__
rszvb_SetPulseTimeBandwidth.output = False
# rszvb_GetPulseTimeBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* timeBandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'timeBandwidth'),)
rszvb_GetPulseTimeBandwidth  = prototype(('rszvb_GetPulseTimeBandwidth', rszvbDLL), paramflags)
rszvb_GetPulseTimeBandwidth.name = 'rszvb_GetPulseTimeBandwidth'
rszvb_GetPulseTimeBandwidth.errcheck = __errorcheck__
rszvb_GetPulseTimeBandwidth.output = True
# rszvb_SetPulseCoupledSectionLimitLinesState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean coupleLimits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'coupleLimits'),)
rszvb_SetPulseCoupledSectionLimitLinesState  = prototype(('rszvb_SetPulseCoupledSectionLimitLinesState', rszvbDLL), paramflags)
rszvb_SetPulseCoupledSectionLimitLinesState.name = 'rszvb_SetPulseCoupledSectionLimitLinesState'
rszvb_SetPulseCoupledSectionLimitLinesState.errcheck = __errorcheck__
rszvb_SetPulseCoupledSectionLimitLinesState.output = False
# rszvb_GetPulseCoupledSectionLimitLinesState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* coupleLimits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'coupleLimits'),)
rszvb_GetPulseCoupledSectionLimitLinesState  = prototype(('rszvb_GetPulseCoupledSectionLimitLinesState', rszvbDLL), paramflags)
rszvb_GetPulseCoupledSectionLimitLinesState.name = 'rszvb_GetPulseCoupledSectionLimitLinesState'
rszvb_GetPulseCoupledSectionLimitLinesState.errcheck = __errorcheck__
rszvb_GetPulseCoupledSectionLimitLinesState.output = True
# rszvb_SetPulseEvaluationMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverType', 'ViInt32 recordNumber', 'ViInt32 interfaceType', 'ViInt32 generatorPortNumber', 'ViInt32 evaluationMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverType'),(1, 'recordNumber'),(1, 'interfaceType'),(1, 'generatorPortNumber'),(1, 'evaluationMode'),)
rszvb_SetPulseEvaluationMode  = prototype(('rszvb_SetPulseEvaluationMode', rszvbDLL), paramflags)
rszvb_SetPulseEvaluationMode.name = 'rszvb_SetPulseEvaluationMode'
rszvb_SetPulseEvaluationMode.errcheck = __errorcheck__
rszvb_SetPulseEvaluationMode.output = False
# rszvb_GetPulseEvaluationMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverType', 'ViInt32 recordNumber', 'ViInt32 interfaceType', 'ViInt32 generatorPortNumber', 'ViInt32* evaluationMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverType'),(1, 'recordNumber'),(1, 'interfaceType'),(1, 'generatorPortNumber'),(2, 'evaluationMode'),)
rszvb_GetPulseEvaluationMode  = prototype(('rszvb_GetPulseEvaluationMode', rszvbDLL), paramflags)
rszvb_GetPulseEvaluationMode.name = 'rszvb_GetPulseEvaluationMode'
rszvb_GetPulseEvaluationMode.errcheck = __errorcheck__
rszvb_GetPulseEvaluationMode.output = True
# rszvb_SetPulseEvaluationSectionStart ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverType', 'ViInt32 recordNumber', 'ViInt32 interfaceType', 'ViInt32 generatorPortNumber', 'ViReal64 evaluationStartTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverType'),(1, 'recordNumber'),(1, 'interfaceType'),(1, 'generatorPortNumber'),(1, 'evaluationStartTime'),)
rszvb_SetPulseEvaluationSectionStart  = prototype(('rszvb_SetPulseEvaluationSectionStart', rszvbDLL), paramflags)
rszvb_SetPulseEvaluationSectionStart.name = 'rszvb_SetPulseEvaluationSectionStart'
rszvb_SetPulseEvaluationSectionStart.errcheck = __errorcheck__
rszvb_SetPulseEvaluationSectionStart.output = False
# rszvb_GetPulseEvaluationSectionStart ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverType', 'ViInt32 recordNumber', 'ViInt32 interfaceType', 'ViInt32 generatorPortNumber', 'ViReal64* evaluationStartTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverType'),(1, 'recordNumber'),(1, 'interfaceType'),(1, 'generatorPortNumber'),(2, 'evaluationStartTime'),)
rszvb_GetPulseEvaluationSectionStart  = prototype(('rszvb_GetPulseEvaluationSectionStart', rszvbDLL), paramflags)
rszvb_GetPulseEvaluationSectionStart.name = 'rszvb_GetPulseEvaluationSectionStart'
rszvb_GetPulseEvaluationSectionStart.errcheck = __errorcheck__
rszvb_GetPulseEvaluationSectionStart.output = True
# rszvb_SetPulseEvaluationSectionStop ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverType', 'ViInt32 recordNumber', 'ViInt32 interfaceType', 'ViInt32 generatorPortNumber', 'ViReal64 evaluationStopTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverType'),(1, 'recordNumber'),(1, 'interfaceType'),(1, 'generatorPortNumber'),(1, 'evaluationStopTime'),)
rszvb_SetPulseEvaluationSectionStop  = prototype(('rszvb_SetPulseEvaluationSectionStop', rszvbDLL), paramflags)
rszvb_SetPulseEvaluationSectionStop.name = 'rszvb_SetPulseEvaluationSectionStop'
rszvb_SetPulseEvaluationSectionStop.errcheck = __errorcheck__
rszvb_SetPulseEvaluationSectionStop.output = False
# rszvb_GetPulseEvaluationSectionStop ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverType', 'ViInt32 recordNumber', 'ViInt32 interfaceType', 'ViInt32 generatorPortNumber', 'ViReal64* evaluationStopTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverType'),(1, 'recordNumber'),(1, 'interfaceType'),(1, 'generatorPortNumber'),(2, 'evaluationStopTime'),)
rszvb_GetPulseEvaluationSectionStop  = prototype(('rszvb_GetPulseEvaluationSectionStop', rszvbDLL), paramflags)
rszvb_GetPulseEvaluationSectionStop.name = 'rszvb_GetPulseEvaluationSectionStop'
rszvb_GetPulseEvaluationSectionStop.errcheck = __errorcheck__
rszvb_GetPulseEvaluationSectionStop.output = True
# rszvb_SetPulseSectionLimitLinesState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverType', 'ViInt32 recordNumber', 'ViInt32 interfaceType', 'ViInt32 generatorPortNumber', 'ViBoolean limitLinesState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverType'),(1, 'recordNumber'),(1, 'interfaceType'),(1, 'generatorPortNumber'),(1, 'limitLinesState'),)
rszvb_SetPulseSectionLimitLinesState  = prototype(('rszvb_SetPulseSectionLimitLinesState', rszvbDLL), paramflags)
rszvb_SetPulseSectionLimitLinesState.name = 'rszvb_SetPulseSectionLimitLinesState'
rszvb_SetPulseSectionLimitLinesState.errcheck = __errorcheck__
rszvb_SetPulseSectionLimitLinesState.output = False
# rszvb_GetPulseSectionLimitLinesState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverType', 'ViInt32 recordNumber', 'ViInt32 interfaceType', 'ViInt32 generatorPortNumber', 'ViBoolean* limitLinesState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverType'),(1, 'recordNumber'),(1, 'interfaceType'),(1, 'generatorPortNumber'),(2, 'limitLinesState'),)
rszvb_GetPulseSectionLimitLinesState  = prototype(('rszvb_GetPulseSectionLimitLinesState', rszvbDLL), paramflags)
rszvb_GetPulseSectionLimitLinesState.name = 'rszvb_GetPulseSectionLimitLinesState'
rszvb_GetPulseSectionLimitLinesState.errcheck = __errorcheck__
rszvb_GetPulseSectionLimitLinesState.output = True
# rszvb_SetPulseShiftStimulus ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverType', 'ViInt32 recordNumber', 'ViInt32 interfaceType', 'ViInt32 generatorPortNumber', 'ViReal64 shiftStimulus']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverType'),(1, 'recordNumber'),(1, 'interfaceType'),(1, 'generatorPortNumber'),(1, 'shiftStimulus'),)
rszvb_SetPulseShiftStimulus  = prototype(('rszvb_SetPulseShiftStimulus', rszvbDLL), paramflags)
rszvb_SetPulseShiftStimulus.name = 'rszvb_SetPulseShiftStimulus'
rszvb_SetPulseShiftStimulus.errcheck = __errorcheck__
rszvb_SetPulseShiftStimulus.output = False
# rszvb_GetPulseShiftStimulus ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverType', 'ViInt32 recordNumber', 'ViInt32 interfaceType', 'ViInt32 generatorPortNumber', 'ViReal64* shiftStimulus']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverType'),(1, 'recordNumber'),(1, 'interfaceType'),(1, 'generatorPortNumber'),(2, 'shiftStimulus'),)
rszvb_GetPulseShiftStimulus  = prototype(('rszvb_GetPulseShiftStimulus', rszvbDLL), paramflags)
rszvb_GetPulseShiftStimulus.name = 'rszvb_GetPulseShiftStimulus'
rszvb_GetPulseShiftStimulus.errcheck = __errorcheck__
rszvb_GetPulseShiftStimulus.output = True
# rszvb_ReadTimeSamplesData ['ViSession instrumentHandle', 'ViInt32 channel_Trace', 'ViInt32* noOfValues', 'ViReal64 _VI_FAR traceData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel_Trace'),(2, 'noOfValues'),(1, 'traceData[]'),)
rszvb_ReadTimeSamplesData  = prototype(('rszvb_ReadTimeSamplesData', rszvbDLL), paramflags)
rszvb_ReadTimeSamplesData.name = 'rszvb_ReadTimeSamplesData'
rszvb_ReadTimeSamplesData.errcheck = __errorcheck__
rszvb_ReadTimeSamplesData.output = True
# rszvb_SetSweepNumberOfPoints ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 numberOfPoints']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'numberOfPoints'),)
rszvb_SetSweepNumberOfPoints  = prototype(('rszvb_SetSweepNumberOfPoints', rszvbDLL), paramflags)
rszvb_SetSweepNumberOfPoints.name = 'rszvb_SetSweepNumberOfPoints'
rszvb_SetSweepNumberOfPoints.errcheck = __errorcheck__
rszvb_SetSweepNumberOfPoints.output = False
# rszvb_GetSweepNumberOfPoints ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* numberOfPoints']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'numberOfPoints'),)
rszvb_GetSweepNumberOfPoints  = prototype(('rszvb_GetSweepNumberOfPoints', rszvbDLL), paramflags)
rszvb_GetSweepNumberOfPoints.name = 'rszvb_GetSweepNumberOfPoints'
rszvb_GetSweepNumberOfPoints.errcheck = __errorcheck__
rszvb_GetSweepNumberOfPoints.output = True
# rszvb_SetFrequencyStepSize ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 stepSize']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'stepSize'),)
rszvb_SetFrequencyStepSize  = prototype(('rszvb_SetFrequencyStepSize', rszvbDLL), paramflags)
rszvb_SetFrequencyStepSize.name = 'rszvb_SetFrequencyStepSize'
rszvb_SetFrequencyStepSize.errcheck = __errorcheck__
rszvb_SetFrequencyStepSize.output = False
# rszvb_GetFrequencyStepSize ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* stepSize']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'stepSize'),)
rszvb_GetFrequencyStepSize  = prototype(('rszvb_GetFrequencyStepSize', rszvbDLL), paramflags)
rszvb_GetFrequencyStepSize.name = 'rszvb_GetFrequencyStepSize'
rszvb_GetFrequencyStepSize.errcheck = __errorcheck__
rszvb_GetFrequencyStepSize.output = True
# rszvb_SetSweepCount ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 sweepCount']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'sweepCount'),)
rszvb_SetSweepCount  = prototype(('rszvb_SetSweepCount', rszvbDLL), paramflags)
rszvb_SetSweepCount.name = 'rszvb_SetSweepCount'
rszvb_SetSweepCount.errcheck = __errorcheck__
rszvb_SetSweepCount.output = False
# rszvb_GetSweepCount ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* sweepCount']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'sweepCount'),)
rszvb_GetSweepCount  = prototype(('rszvb_GetSweepCount', rszvbDLL), paramflags)
rszvb_GetSweepCount.name = 'rszvb_GetSweepCount'
rszvb_GetSweepCount.errcheck = __errorcheck__
rszvb_GetSweepCount.output = True
# rszvb_ConfigureSweepTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean autoSweepTime', 'ViReal64 sweepTime', 'ViReal64 measDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'autoSweepTime'),(1, 'sweepTime'),(1, 'measDelay'),)
rszvb_ConfigureSweepTime  = prototype(('rszvb_ConfigureSweepTime', rszvbDLL), paramflags)
rszvb_ConfigureSweepTime.name = 'rszvb_ConfigureSweepTime'
rszvb_ConfigureSweepTime.errcheck = __errorcheck__
rszvb_ConfigureSweepTime.output = False
# rszvb_SetSweepTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 sweepTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'sweepTime'),)
rszvb_SetSweepTime  = prototype(('rszvb_SetSweepTime', rszvbDLL), paramflags)
rszvb_SetSweepTime.name = 'rszvb_SetSweepTime'
rszvb_SetSweepTime.errcheck = __errorcheck__
rszvb_SetSweepTime.output = False
# rszvb_GetSweepTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* sweepTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'sweepTime'),)
rszvb_GetSweepTime  = prototype(('rszvb_GetSweepTime', rszvbDLL), paramflags)
rszvb_GetSweepTime.name = 'rszvb_GetSweepTime'
rszvb_GetSweepTime.errcheck = __errorcheck__
rszvb_GetSweepTime.output = True
# rszvb_SetSweepMeasDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 measDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'measDelay'),)
rszvb_SetSweepMeasDelay  = prototype(('rszvb_SetSweepMeasDelay', rszvbDLL), paramflags)
rszvb_SetSweepMeasDelay.name = 'rszvb_SetSweepMeasDelay'
rszvb_SetSweepMeasDelay.errcheck = __errorcheck__
rszvb_SetSweepMeasDelay.output = False
# rszvb_GetSweepMeasDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* measDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'measDelay'),)
rszvb_GetSweepMeasDelay  = prototype(('rszvb_GetSweepMeasDelay', rszvbDLL), paramflags)
rszvb_GetSweepMeasDelay.name = 'rszvb_GetSweepMeasDelay'
rszvb_GetSweepMeasDelay.errcheck = __errorcheck__
rszvb_GetSweepMeasDelay.output = True
# rszvb_SetSweepTimeAuto ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean autoSweepTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'autoSweepTime'),)
rszvb_SetSweepTimeAuto  = prototype(('rszvb_SetSweepTimeAuto', rszvbDLL), paramflags)
rszvb_SetSweepTimeAuto.name = 'rszvb_SetSweepTimeAuto'
rszvb_SetSweepTimeAuto.errcheck = __errorcheck__
rszvb_SetSweepTimeAuto.output = False
# rszvb_GetSweepTimeAuto ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* autoSweepTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'autoSweepTime'),)
rszvb_GetSweepTimeAuto  = prototype(('rszvb_GetSweepTimeAuto', rszvbDLL), paramflags)
rszvb_GetSweepTimeAuto.name = 'rszvb_GetSweepTimeAuto'
rszvb_GetSweepTimeAuto.errcheck = __errorcheck__
rszvb_GetSweepTimeAuto.output = True
# rszvb_ConfigureTriggerFreeRun ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_ConfigureTriggerFreeRun  = prototype(('rszvb_ConfigureTriggerFreeRun', rszvbDLL), paramflags)
rszvb_ConfigureTriggerFreeRun.name = 'rszvb_ConfigureTriggerFreeRun'
rszvb_ConfigureTriggerFreeRun.errcheck = __errorcheck__
rszvb_ConfigureTriggerFreeRun.output = False
# rszvb_ConfigureTriggerExternal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 triggerOn']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'triggerOn'),)
rszvb_ConfigureTriggerExternal  = prototype(('rszvb_ConfigureTriggerExternal', rszvbDLL), paramflags)
rszvb_ConfigureTriggerExternal.name = 'rszvb_ConfigureTriggerExternal'
rszvb_ConfigureTriggerExternal.errcheck = __errorcheck__
rszvb_ConfigureTriggerExternal.output = False
# rszvb_ConfigureTriggerPeriodic ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 triggerPeriod']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'triggerPeriod'),)
rszvb_ConfigureTriggerPeriodic  = prototype(('rszvb_ConfigureTriggerPeriodic', rszvbDLL), paramflags)
rszvb_ConfigureTriggerPeriodic.name = 'rszvb_ConfigureTriggerPeriodic'
rszvb_ConfigureTriggerPeriodic.errcheck = __errorcheck__
rszvb_ConfigureTriggerPeriodic.output = False
# rszvb_ConfigureTriggerRFPower ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_ConfigureTriggerRFPower  = prototype(('rszvb_ConfigureTriggerRFPower', rszvbDLL), paramflags)
rszvb_ConfigureTriggerRFPower.name = 'rszvb_ConfigureTriggerRFPower'
rszvb_ConfigureTriggerRFPower.errcheck = __errorcheck__
rszvb_ConfigureTriggerRFPower.output = False
# rszvb_ConfigureTriggerManual ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_ConfigureTriggerManual  = prototype(('rszvb_ConfigureTriggerManual', rszvbDLL), paramflags)
rszvb_ConfigureTriggerManual.name = 'rszvb_ConfigureTriggerManual'
rszvb_ConfigureTriggerManual.errcheck = __errorcheck__
rszvb_ConfigureTriggerManual.output = False
# rszvb_ConfigureTriggerSettings ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 triggerMeasSequence', 'ViReal64 triggerDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'triggerMeasSequence'),(1, 'triggerDelay'),)
rszvb_ConfigureTriggerSettings  = prototype(('rszvb_ConfigureTriggerSettings', rszvbDLL), paramflags)
rszvb_ConfigureTriggerSettings.name = 'rszvb_ConfigureTriggerSettings'
rszvb_ConfigureTriggerSettings.errcheck = __errorcheck__
rszvb_ConfigureTriggerSettings.output = False
# rszvb_SetTriggerSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 triggerSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'triggerSource'),)
rszvb_SetTriggerSource  = prototype(('rszvb_SetTriggerSource', rszvbDLL), paramflags)
rszvb_SetTriggerSource.name = 'rszvb_SetTriggerSource'
rszvb_SetTriggerSource.errcheck = __errorcheck__
rszvb_SetTriggerSource.output = False
# rszvb_GetTriggerSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* triggerSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'triggerSource'),)
rszvb_GetTriggerSource  = prototype(('rszvb_GetTriggerSource', rszvbDLL), paramflags)
rszvb_GetTriggerSource.name = 'rszvb_GetTriggerSource'
rszvb_GetTriggerSource.errcheck = __errorcheck__
rszvb_GetTriggerSource.output = True
# rszvb_SetTriggerDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 triggerDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'triggerDelay'),)
rszvb_SetTriggerDelay  = prototype(('rszvb_SetTriggerDelay', rszvbDLL), paramflags)
rszvb_SetTriggerDelay.name = 'rszvb_SetTriggerDelay'
rszvb_SetTriggerDelay.errcheck = __errorcheck__
rszvb_SetTriggerDelay.output = False
# rszvb_GetTriggerDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* triggerDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'triggerDelay'),)
rszvb_GetTriggerDelay  = prototype(('rszvb_GetTriggerDelay', rszvbDLL), paramflags)
rszvb_GetTriggerDelay.name = 'rszvb_GetTriggerDelay'
rszvb_GetTriggerDelay.errcheck = __errorcheck__
rszvb_GetTriggerDelay.output = True
# rszvb_SetPartialMeasurementTriggerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 triggerMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'triggerMode'),)
rszvb_SetPartialMeasurementTriggerMode  = prototype(('rszvb_SetPartialMeasurementTriggerMode', rszvbDLL), paramflags)
rszvb_SetPartialMeasurementTriggerMode.name = 'rszvb_SetPartialMeasurementTriggerMode'
rszvb_SetPartialMeasurementTriggerMode.errcheck = __errorcheck__
rszvb_SetPartialMeasurementTriggerMode.output = False
# rszvb_GetPartialMeasurementTriggerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* triggerMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'triggerMode'),)
rszvb_GetPartialMeasurementTriggerMode  = prototype(('rszvb_GetPartialMeasurementTriggerMode', rszvbDLL), paramflags)
rszvb_GetPartialMeasurementTriggerMode.name = 'rszvb_GetPartialMeasurementTriggerMode'
rszvb_GetPartialMeasurementTriggerMode.errcheck = __errorcheck__
rszvb_GetPartialMeasurementTriggerMode.output = True
# rszvb_SetGeneratorPortTriggerDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generatorPort', 'ViReal64 triggerDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generatorPort'),(1, 'triggerDelay'),)
rszvb_SetGeneratorPortTriggerDelay  = prototype(('rszvb_SetGeneratorPortTriggerDelay', rszvbDLL), paramflags)
rszvb_SetGeneratorPortTriggerDelay.name = 'rszvb_SetGeneratorPortTriggerDelay'
rszvb_SetGeneratorPortTriggerDelay.errcheck = __errorcheck__
rszvb_SetGeneratorPortTriggerDelay.output = False
# rszvb_GetGeneratorPortTriggerDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generatorPort', 'ViReal64* triggerDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generatorPort'),(2, 'triggerDelay'),)
rszvb_GetGeneratorPortTriggerDelay  = prototype(('rszvb_GetGeneratorPortTriggerDelay', rszvbDLL), paramflags)
rszvb_GetGeneratorPortTriggerDelay.name = 'rszvb_GetGeneratorPortTriggerDelay'
rszvb_GetGeneratorPortTriggerDelay.errcheck = __errorcheck__
rszvb_GetGeneratorPortTriggerDelay.output = True
# rszvb_SetPhysicalPortTriggerDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 analyzerPort', 'ViReal64 triggerDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'analyzerPort'),(1, 'triggerDelay'),)
rszvb_SetPhysicalPortTriggerDelay  = prototype(('rszvb_SetPhysicalPortTriggerDelay', rszvbDLL), paramflags)
rszvb_SetPhysicalPortTriggerDelay.name = 'rszvb_SetPhysicalPortTriggerDelay'
rszvb_SetPhysicalPortTriggerDelay.errcheck = __errorcheck__
rszvb_SetPhysicalPortTriggerDelay.output = False
# rszvb_GetPhysicalPortTriggerDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 analyzerPort', 'ViReal64* triggerDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'analyzerPort'),(2, 'triggerDelay'),)
rszvb_GetPhysicalPortTriggerDelay  = prototype(('rszvb_GetPhysicalPortTriggerDelay', rszvbDLL), paramflags)
rszvb_GetPhysicalPortTriggerDelay.name = 'rszvb_GetPhysicalPortTriggerDelay'
rszvb_GetPhysicalPortTriggerDelay.errcheck = __errorcheck__
rszvb_GetPhysicalPortTriggerDelay.output = True
# rszvb_SetTriggeredMeasSequence ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 triggerMeasSequence']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'triggerMeasSequence'),)
rszvb_SetTriggeredMeasSequence  = prototype(('rszvb_SetTriggeredMeasSequence', rszvbDLL), paramflags)
rszvb_SetTriggeredMeasSequence.name = 'rszvb_SetTriggeredMeasSequence'
rszvb_SetTriggeredMeasSequence.errcheck = __errorcheck__
rszvb_SetTriggeredMeasSequence.output = False
# rszvb_GetTriggeredMeasSequence ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* triggerMeasSequence']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'triggerMeasSequence'),)
rszvb_GetTriggeredMeasSequence  = prototype(('rszvb_GetTriggeredMeasSequence', rszvbDLL), paramflags)
rszvb_GetTriggeredMeasSequence.name = 'rszvb_GetTriggeredMeasSequence'
rszvb_GetTriggeredMeasSequence.errcheck = __errorcheck__
rszvb_GetTriggeredMeasSequence.output = True
# rszvb_SetTriggerOn ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 triggerOn']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'triggerOn'),)
rszvb_SetTriggerOn  = prototype(('rszvb_SetTriggerOn', rszvbDLL), paramflags)
rszvb_SetTriggerOn.name = 'rszvb_SetTriggerOn'
rszvb_SetTriggerOn.errcheck = __errorcheck__
rszvb_SetTriggerOn.output = False
# rszvb_GetTriggerOn ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* triggerOn']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'triggerOn'),)
rszvb_GetTriggerOn  = prototype(('rszvb_GetTriggerOn', rszvbDLL), paramflags)
rszvb_GetTriggerOn.name = 'rszvb_GetTriggerOn'
rszvb_GetTriggerOn.errcheck = __errorcheck__
rszvb_GetTriggerOn.output = True
# rszvb_SetTriggerPeriod ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 triggerPeriod']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'triggerPeriod'),)
rszvb_SetTriggerPeriod  = prototype(('rszvb_SetTriggerPeriod', rszvbDLL), paramflags)
rszvb_SetTriggerPeriod.name = 'rszvb_SetTriggerPeriod'
rszvb_SetTriggerPeriod.errcheck = __errorcheck__
rszvb_SetTriggerPeriod.output = False
# rszvb_GetTriggerPeriod ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* triggerPeriod']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'triggerPeriod'),)
rszvb_GetTriggerPeriod  = prototype(('rszvb_GetTriggerPeriod', rszvbDLL), paramflags)
rszvb_GetTriggerPeriod.name = 'rszvb_GetTriggerPeriod'
rszvb_GetTriggerPeriod.errcheck = __errorcheck__
rszvb_GetTriggerPeriod.output = True
# rszvb_SendTrigger ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_SendTrigger  = prototype(('rszvb_SendTrigger', rszvbDLL), paramflags)
rszvb_SendTrigger.name = 'rszvb_SendTrigger'
rszvb_SendTrigger.errcheck = __errorcheck__
rszvb_SendTrigger.output = False
# rszvb_SendTriggerWaitOPC ['ViSession instrumentHandle', 'ViInt32 timeout']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'timeout'),)
rszvb_SendTriggerWaitOPC  = prototype(('rszvb_SendTriggerWaitOPC', rszvbDLL), paramflags)
rszvb_SendTriggerWaitOPC.name = 'rszvb_SendTriggerWaitOPC'
rszvb_SendTriggerWaitOPC.errcheck = __errorcheck__
rszvb_SendTriggerWaitOPC.output = False
# rszvb_SendChannelTrigger ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_SendChannelTrigger  = prototype(('rszvb_SendChannelTrigger', rszvbDLL), paramflags)
rszvb_SendChannelTrigger.name = 'rszvb_SendChannelTrigger'
rszvb_SendChannelTrigger.errcheck = __errorcheck__
rszvb_SendChannelTrigger.output = False
# rszvb_SendChannelTriggerWaitOPC ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 timeout']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'timeout'),)
rszvb_SendChannelTriggerWaitOPC  = prototype(('rszvb_SendChannelTriggerWaitOPC', rszvbDLL), paramflags)
rszvb_SendChannelTriggerWaitOPC.name = 'rszvb_SendChannelTriggerWaitOPC'
rszvb_SendChannelTriggerWaitOPC.errcheck = __errorcheck__
rszvb_SendChannelTriggerWaitOPC.output = False
# rszvb_SetSweepSingleAllChans ['ViSession instrumentHandle', 'ViInt32 singleSweep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'singleSweep'),)
rszvb_SetSweepSingleAllChans  = prototype(('rszvb_SetSweepSingleAllChans', rszvbDLL), paramflags)
rszvb_SetSweepSingleAllChans.name = 'rszvb_SetSweepSingleAllChans'
rszvb_SetSweepSingleAllChans.errcheck = __errorcheck__
rszvb_SetSweepSingleAllChans.output = False
# rszvb_GetSweepSingleAllChans ['ViSession instrumentHandle', 'ViInt32* singleSweep']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'singleSweep'),)
rszvb_GetSweepSingleAllChans  = prototype(('rszvb_GetSweepSingleAllChans', rszvbDLL), paramflags)
rszvb_GetSweepSingleAllChans.name = 'rszvb_GetSweepSingleAllChans'
rszvb_GetSweepSingleAllChans.errcheck = __errorcheck__
rszvb_GetSweepSingleAllChans.output = True
# rszvb_SweepRestart ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_SweepRestart  = prototype(('rszvb_SweepRestart', rszvbDLL), paramflags)
rszvb_SweepRestart.name = 'rszvb_SweepRestart'
rszvb_SweepRestart.errcheck = __errorcheck__
rszvb_SweepRestart.output = False
# rszvb_SetSweepSingle ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 singleSweep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'singleSweep'),)
rszvb_SetSweepSingle  = prototype(('rszvb_SetSweepSingle', rszvbDLL), paramflags)
rszvb_SetSweepSingle.name = 'rszvb_SetSweepSingle'
rszvb_SetSweepSingle.errcheck = __errorcheck__
rszvb_SetSweepSingle.output = False
# rszvb_GetSweepSingle ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* singleSweep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'singleSweep'),)
rszvb_GetSweepSingle  = prototype(('rszvb_GetSweepSingle', rszvbDLL), paramflags)
rszvb_GetSweepSingle.name = 'rszvb_GetSweepSingle'
rszvb_GetSweepSingle.errcheck = __errorcheck__
rszvb_GetSweepSingle.output = True
# rszvb_DefineGroupOfMeasuredPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 group', 'ViInt32 firstPort', 'ViInt32 lastPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'group'),(1, 'firstPort'),(1, 'lastPort'),)
rszvb_DefineGroupOfMeasuredPorts  = prototype(('rszvb_DefineGroupOfMeasuredPorts', rszvbDLL), paramflags)
rszvb_DefineGroupOfMeasuredPorts.name = 'rszvb_DefineGroupOfMeasuredPorts'
rszvb_DefineGroupOfMeasuredPorts.errcheck = __errorcheck__
rszvb_DefineGroupOfMeasuredPorts.output = False
# rszvb_GetGroupOfMeasuredPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 group', 'ViInt32* firstPort', 'ViInt32* lastPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'group'),(2, 'firstPort'),(2, 'lastPort'),)
rszvb_GetGroupOfMeasuredPorts  = prototype(('rszvb_GetGroupOfMeasuredPorts', rszvbDLL), paramflags)
rszvb_GetGroupOfMeasuredPorts.name = 'rszvb_GetGroupOfMeasuredPorts'
rszvb_GetGroupOfMeasuredPorts.errcheck = __errorcheck__
rszvb_GetGroupOfMeasuredPorts.output = True
# rszvb_DefineGroupOfAllMeasuredPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 group', 'ViInt32 numberOfPortsInGroup', 'ViInt32 _VI_FAR ports[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'group'),(1, 'numberOfPortsInGroup'),(1, 'ports[]'),)
rszvb_DefineGroupOfAllMeasuredPorts  = prototype(('rszvb_DefineGroupOfAllMeasuredPorts', rszvbDLL), paramflags)
rszvb_DefineGroupOfAllMeasuredPorts.name = 'rszvb_DefineGroupOfAllMeasuredPorts'
rszvb_DefineGroupOfAllMeasuredPorts.errcheck = __errorcheck__
rszvb_DefineGroupOfAllMeasuredPorts.output = False
# rszvb_GetGroupOfAllMeasuredPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 group', 'ViInt32* numberOfPortsInGroup', 'ViInt32 _VI_FAR ports[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'group'),(2, 'numberOfPortsInGroup'),(1, 'ports[]'),)
rszvb_GetGroupOfAllMeasuredPorts  = prototype(('rszvb_GetGroupOfAllMeasuredPorts', rszvbDLL), paramflags)
rszvb_GetGroupOfAllMeasuredPorts.name = 'rszvb_GetGroupOfAllMeasuredPorts'
rszvb_GetGroupOfAllMeasuredPorts.errcheck = __errorcheck__
rszvb_GetGroupOfAllMeasuredPorts.output = True
# rszvb_GetPortGroupsCount ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* portGroups']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'portGroups'),)
rszvb_GetPortGroupsCount  = prototype(('rszvb_GetPortGroupsCount', rszvbDLL), paramflags)
rszvb_GetPortGroupsCount.name = 'rszvb_GetPortGroupsCount'
rszvb_GetPortGroupsCount.errcheck = __errorcheck__
rszvb_GetPortGroupsCount.output = True
# rszvb_DeleteGroupOfMeasuredPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 group']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'group'),)
rszvb_DeleteGroupOfMeasuredPorts  = prototype(('rszvb_DeleteGroupOfMeasuredPorts', rszvbDLL), paramflags)
rszvb_DeleteGroupOfMeasuredPorts.name = 'rszvb_DeleteGroupOfMeasuredPorts'
rszvb_DeleteGroupOfMeasuredPorts.errcheck = __errorcheck__
rszvb_DeleteGroupOfMeasuredPorts.output = False
# rszvb_DeleteAllGroupsOfMeasuredPorts ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_DeleteAllGroupsOfMeasuredPorts  = prototype(('rszvb_DeleteAllGroupsOfMeasuredPorts', rszvbDLL), paramflags)
rszvb_DeleteAllGroupsOfMeasuredPorts.name = 'rszvb_DeleteAllGroupsOfMeasuredPorts'
rszvb_DeleteAllGroupsOfMeasuredPorts.errcheck = __errorcheck__
rszvb_DeleteAllGroupsOfMeasuredPorts.output = False
# rszvb_DefineBalancedPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 logicalPort', 'ViInt32 physicalPort1', 'ViInt32 physicalPort2']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'logicalPort'),(1, 'physicalPort1'),(1, 'physicalPort2'),)
rszvb_DefineBalancedPort  = prototype(('rszvb_DefineBalancedPort', rszvbDLL), paramflags)
rszvb_DefineBalancedPort.name = 'rszvb_DefineBalancedPort'
rszvb_DefineBalancedPort.errcheck = __errorcheck__
rszvb_DefineBalancedPort.output = False
# rszvb_GetBalancedPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 logicalPort', 'ViInt32* physicalPort1', 'ViInt32* physicalPort2']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'logicalPort'),(2, 'physicalPort1'),(2, 'physicalPort2'),)
rszvb_GetBalancedPort  = prototype(('rszvb_GetBalancedPort', rszvbDLL), paramflags)
rszvb_GetBalancedPort.name = 'rszvb_GetBalancedPort'
rszvb_GetBalancedPort.errcheck = __errorcheck__
rszvb_GetBalancedPort.output = True
# rszvb_DeleteBalancedPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 logicalPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'logicalPort'),)
rszvb_DeleteBalancedPort  = prototype(('rszvb_DeleteBalancedPort', rszvbDLL), paramflags)
rszvb_DeleteBalancedPort.name = 'rszvb_DeleteBalancedPort'
rszvb_DeleteBalancedPort.errcheck = __errorcheck__
rszvb_DeleteBalancedPort.output = False
# rszvb_DeleteAllBalancedPorts ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_DeleteAllBalancedPorts  = prototype(('rszvb_DeleteAllBalancedPorts', rszvbDLL), paramflags)
rszvb_DeleteAllBalancedPorts.name = 'rszvb_DeleteAllBalancedPorts'
rszvb_DeleteAllBalancedPorts.errcheck = __errorcheck__
rszvb_DeleteAllBalancedPorts.output = False
# rszvb_SetDifferentialModeImpedance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 logicalPort', 'ViReal64 impedance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'logicalPort'),(1, 'impedance'),)
rszvb_SetDifferentialModeImpedance  = prototype(('rszvb_SetDifferentialModeImpedance', rszvbDLL), paramflags)
rszvb_SetDifferentialModeImpedance.name = 'rszvb_SetDifferentialModeImpedance'
rszvb_SetDifferentialModeImpedance.errcheck = __errorcheck__
rszvb_SetDifferentialModeImpedance.output = False
# rszvb_GetDifferentialModeImpedance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 logicalPort', 'ViReal64* impedance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'logicalPort'),(2, 'impedance'),)
rszvb_GetDifferentialModeImpedance  = prototype(('rszvb_GetDifferentialModeImpedance', rszvbDLL), paramflags)
rszvb_GetDifferentialModeImpedance.name = 'rszvb_GetDifferentialModeImpedance'
rszvb_GetDifferentialModeImpedance.errcheck = __errorcheck__
rszvb_GetDifferentialModeImpedance.output = True
# rszvb_SetCommonModeImpedance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 logicalPort', 'ViReal64 impedance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'logicalPort'),(1, 'impedance'),)
rszvb_SetCommonModeImpedance  = prototype(('rszvb_SetCommonModeImpedance', rszvbDLL), paramflags)
rszvb_SetCommonModeImpedance.name = 'rszvb_SetCommonModeImpedance'
rszvb_SetCommonModeImpedance.errcheck = __errorcheck__
rszvb_SetCommonModeImpedance.output = False
# rszvb_GetCommonModeImpedance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 logicalPort', 'ViReal64* impedance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'logicalPort'),(2, 'impedance'),)
rszvb_GetCommonModeImpedance  = prototype(('rszvb_GetCommonModeImpedance', rszvbDLL), paramflags)
rszvb_GetCommonModeImpedance.name = 'rszvb_GetCommonModeImpedance'
rszvb_GetCommonModeImpedance.errcheck = __errorcheck__
rszvb_GetCommonModeImpedance.output = True
# rszvb_DefinePortPair ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 portPair', 'ViInt32 port1', 'ViInt32 port2']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'portPair'),(1, 'port1'),(1, 'port2'),)
rszvb_DefinePortPair  = prototype(('rszvb_DefinePortPair', rszvbDLL), paramflags)
rszvb_DefinePortPair.name = 'rszvb_DefinePortPair'
rszvb_DefinePortPair.errcheck = __errorcheck__
rszvb_DefinePortPair.output = False
# rszvb_DeletePortPair ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 portPair']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'portPair'),)
rszvb_DeletePortPair  = prototype(('rszvb_DeletePortPair', rszvbDLL), paramflags)
rszvb_DeletePortPair.name = 'rszvb_DeletePortPair'
rszvb_DeletePortPair.errcheck = __errorcheck__
rszvb_DeletePortPair.output = False
# rszvb_SetDefaultConfigurationState ['ViSession instrumentHandle', 'ViBoolean defaultSettings']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'defaultSettings'),)
rszvb_SetDefaultConfigurationState  = prototype(('rszvb_SetDefaultConfigurationState', rszvbDLL), paramflags)
rszvb_SetDefaultConfigurationState.name = 'rszvb_SetDefaultConfigurationState'
rszvb_SetDefaultConfigurationState.errcheck = __errorcheck__
rszvb_SetDefaultConfigurationState.output = False
# rszvb_GetDefaultConfigurationState ['ViSession instrumentHandle', 'ViBoolean* defaultSettings']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'defaultSettings'),)
rszvb_GetDefaultConfigurationState  = prototype(('rszvb_GetDefaultConfigurationState', rszvbDLL), paramflags)
rszvb_GetDefaultConfigurationState.name = 'rszvb_GetDefaultConfigurationState'
rszvb_GetDefaultConfigurationState.errcheck = __errorcheck__
rszvb_GetDefaultConfigurationState.output = True
# rszvb_SetPortConfigration ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portGroupA', 'ViInt32 portGroupB', 'ViInt32 portGroupC', 'ViInt32 portGroupD']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portGroupA'),(1, 'portGroupB'),(1, 'portGroupC'),(1, 'portGroupD'),)
rszvb_SetPortConfigration  = prototype(('rszvb_SetPortConfigration', rszvbDLL), paramflags)
rszvb_SetPortConfigration.name = 'rszvb_SetPortConfigration'
rszvb_SetPortConfigration.errcheck = __errorcheck__
rszvb_SetPortConfigration.output = False
# rszvb_GetPortConfigration ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* portGroupA', 'ViInt32* portGroupB', 'ViInt32* portGroupC', 'ViInt32* portGroupD']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'portGroupA'),(2, 'portGroupB'),(2, 'portGroupC'),(2, 'portGroupD'),)
rszvb_GetPortConfigration  = prototype(('rszvb_GetPortConfigration', rszvbDLL), paramflags)
rszvb_GetPortConfigration.name = 'rszvb_GetPortConfigration'
rszvb_GetPortConfigration.errcheck = __errorcheck__
rszvb_GetPortConfigration.output = True
# rszvb_SetConverterPowerOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 portPowerOffset', 'ViInt32 offsetParameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'portPowerOffset'),(1, 'offsetParameter'),)
rszvb_SetConverterPowerOffset  = prototype(('rszvb_SetConverterPowerOffset', rszvbDLL), paramflags)
rszvb_SetConverterPowerOffset.name = 'rszvb_SetConverterPowerOffset'
rszvb_SetConverterPowerOffset.errcheck = __errorcheck__
rszvb_SetConverterPowerOffset.output = False
# rszvb_GetConverterPowerOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* portPowerOffset', 'ViInt32* offsetParameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'portPowerOffset'),(2, 'offsetParameter'),)
rszvb_GetConverterPowerOffset  = prototype(('rszvb_GetConverterPowerOffset', rszvbDLL), paramflags)
rszvb_GetConverterPowerOffset.name = 'rszvb_GetConverterPowerOffset'
rszvb_GetConverterPowerOffset.errcheck = __errorcheck__
rszvb_GetConverterPowerOffset.output = True
# rszvb_SetConverterCalPowerOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 converter', 'ViReal64 calPowerOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'converter'),(1, 'calPowerOffset'),)
rszvb_SetConverterCalPowerOffset  = prototype(('rszvb_SetConverterCalPowerOffset', rszvbDLL), paramflags)
rszvb_SetConverterCalPowerOffset.name = 'rszvb_SetConverterCalPowerOffset'
rszvb_SetConverterCalPowerOffset.errcheck = __errorcheck__
rszvb_SetConverterCalPowerOffset.output = False
# rszvb_GetConverterCalPowerOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 converter', 'ViReal64* calPowerOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'converter'),(2, 'calPowerOffset'),)
rszvb_GetConverterCalPowerOffset  = prototype(('rszvb_GetConverterCalPowerOffset', rszvbDLL), paramflags)
rszvb_GetConverterCalPowerOffset.name = 'rszvb_GetConverterCalPowerOffset'
rszvb_GetConverterCalPowerOffset.errcheck = __errorcheck__
rszvb_GetConverterCalPowerOffset.output = True
# rszvb_SetAdvancedPowerTransferModelFrequencyState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetAdvancedPowerTransferModelFrequencyState  = prototype(('rszvb_SetAdvancedPowerTransferModelFrequencyState', rszvbDLL), paramflags)
rszvb_SetAdvancedPowerTransferModelFrequencyState.name = 'rszvb_SetAdvancedPowerTransferModelFrequencyState'
rszvb_SetAdvancedPowerTransferModelFrequencyState.errcheck = __errorcheck__
rszvb_SetAdvancedPowerTransferModelFrequencyState.output = False
# rszvb_GetAdvancedPowerTransferModelFrequencyState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetAdvancedPowerTransferModelFrequencyState  = prototype(('rszvb_GetAdvancedPowerTransferModelFrequencyState', rszvbDLL), paramflags)
rszvb_GetAdvancedPowerTransferModelFrequencyState.name = 'rszvb_GetAdvancedPowerTransferModelFrequencyState'
rszvb_GetAdvancedPowerTransferModelFrequencyState.errcheck = __errorcheck__
rszvb_GetAdvancedPowerTransferModelFrequencyState.output = True
# rszvb_SetSenseTypeOfPortTransferModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 modelType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'modelType'),)
rszvb_SetSenseTypeOfPortTransferModel  = prototype(('rszvb_SetSenseTypeOfPortTransferModel', rszvbDLL), paramflags)
rszvb_SetSenseTypeOfPortTransferModel.name = 'rszvb_SetSenseTypeOfPortTransferModel'
rszvb_SetSenseTypeOfPortTransferModel.errcheck = __errorcheck__
rszvb_SetSenseTypeOfPortTransferModel.output = False
# rszvb_GetSenseTypeOfPortTransferModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* modelType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'modelType'),)
rszvb_GetSenseTypeOfPortTransferModel  = prototype(('rszvb_GetSenseTypeOfPortTransferModel', rszvbDLL), paramflags)
rszvb_GetSenseTypeOfPortTransferModel.name = 'rszvb_GetSenseTypeOfPortTransferModel'
rszvb_GetSenseTypeOfPortTransferModel.errcheck = __errorcheck__
rszvb_GetSenseTypeOfPortTransferModel.output = True
# rszvb_SetSenseTypeOfAdvancedPowerTransferModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 modelType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'modelType'),)
rszvb_SetSenseTypeOfAdvancedPowerTransferModel  = prototype(('rszvb_SetSenseTypeOfAdvancedPowerTransferModel', rszvbDLL), paramflags)
rszvb_SetSenseTypeOfAdvancedPowerTransferModel.name = 'rszvb_SetSenseTypeOfAdvancedPowerTransferModel'
rszvb_SetSenseTypeOfAdvancedPowerTransferModel.errcheck = __errorcheck__
rszvb_SetSenseTypeOfAdvancedPowerTransferModel.output = False
# rszvb_GetSenseTypeOfAdvancedPowerTransferModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* modelType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'modelType'),)
rszvb_GetSenseTypeOfAdvancedPowerTransferModel  = prototype(('rszvb_GetSenseTypeOfAdvancedPowerTransferModel', rszvbDLL), paramflags)
rszvb_GetSenseTypeOfAdvancedPowerTransferModel.name = 'rszvb_GetSenseTypeOfAdvancedPowerTransferModel'
rszvb_GetSenseTypeOfAdvancedPowerTransferModel.errcheck = __errorcheck__
rszvb_GetSenseTypeOfAdvancedPowerTransferModel.output = True
# rszvb_SetConverterDataSetType ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32 dataSetType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'dataSetType'),)
rszvb_SetConverterDataSetType  = prototype(('rszvb_SetConverterDataSetType', rszvbDLL), paramflags)
rszvb_SetConverterDataSetType.name = 'rszvb_SetConverterDataSetType'
rszvb_SetConverterDataSetType.errcheck = __errorcheck__
rszvb_SetConverterDataSetType.output = False
# rszvb_GetConverterDataSetType ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32* dataSetType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(2, 'dataSetType'),)
rszvb_GetConverterDataSetType  = prototype(('rszvb_GetConverterDataSetType', rszvbDLL), paramflags)
rszvb_GetConverterDataSetType.name = 'rszvb_GetConverterDataSetType'
rszvb_GetConverterDataSetType.errcheck = __errorcheck__
rszvb_GetConverterDataSetType.output = True
# rszvb_SetConverterUserDataSetDirectory ['ViSession instrumentHandle', 'ViInt32 port', 'ViString directory']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'directory'),)
rszvb_SetConverterUserDataSetDirectory  = prototype(('rszvb_SetConverterUserDataSetDirectory', rszvbDLL), paramflags)
rszvb_SetConverterUserDataSetDirectory.name = 'rszvb_SetConverterUserDataSetDirectory'
rszvb_SetConverterUserDataSetDirectory.errcheck = __errorcheck__
rszvb_SetConverterUserDataSetDirectory.output = False
# rszvb_GetConverterUserDataSetDirectory ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32 bufferSize', 'ViChar _VI_FAR directory[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'bufferSize'),(1, 'directory[]'),)
rszvb_GetConverterUserDataSetDirectory  = prototype(('rszvb_GetConverterUserDataSetDirectory', rszvbDLL), paramflags)
rszvb_GetConverterUserDataSetDirectory.name = 'rszvb_GetConverterUserDataSetDirectory'
rszvb_GetConverterUserDataSetDirectory.errcheck = __errorcheck__
rszvb_GetConverterUserDataSetDirectory.output = False
# rszvb_SetConverterPortAssignment ['ViSession instrumentHandle', 'ViInt32 port', 'ViString serialNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'serialNumber'),)
rszvb_SetConverterPortAssignment  = prototype(('rszvb_SetConverterPortAssignment', rszvbDLL), paramflags)
rszvb_SetConverterPortAssignment.name = 'rszvb_SetConverterPortAssignment'
rszvb_SetConverterPortAssignment.errcheck = __errorcheck__
rszvb_SetConverterPortAssignment.output = False
# rszvb_GetConverterPortAssignment ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32 bufferSize', 'ViChar _VI_FAR serialNumber[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'bufferSize'),(1, 'serialNumber[]'),)
rszvb_GetConverterPortAssignment  = prototype(('rszvb_GetConverterPortAssignment', rszvbDLL), paramflags)
rszvb_GetConverterPortAssignment.name = 'rszvb_GetConverterPortAssignment'
rszvb_GetConverterPortAssignment.errcheck = __errorcheck__
rszvb_GetConverterPortAssignment.output = False
# rszvb_SetPortTransferModelState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'state'),)
rszvb_SetPortTransferModelState  = prototype(('rszvb_SetPortTransferModelState', rszvbDLL), paramflags)
rszvb_SetPortTransferModelState.name = 'rszvb_SetPortTransferModelState'
rszvb_SetPortTransferModelState.errcheck = __errorcheck__
rszvb_SetPortTransferModelState.output = False
# rszvb_GetPortTransferModelState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'state'),)
rszvb_GetPortTransferModelState  = prototype(('rszvb_GetPortTransferModelState', rszvbDLL), paramflags)
rszvb_GetPortTransferModelState.name = 'rszvb_GetPortTransferModelState'
rszvb_GetPortTransferModelState.errcheck = __errorcheck__
rszvb_GetPortTransferModelState.output = True
# rszvb_SetPortWaveguideAttenuator ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 waveguideAttenuator', 'ViReal64 attenuation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'waveguideAttenuator'),(1, 'attenuation'),)
rszvb_SetPortWaveguideAttenuator  = prototype(('rszvb_SetPortWaveguideAttenuator', rszvbDLL), paramflags)
rszvb_SetPortWaveguideAttenuator.name = 'rszvb_SetPortWaveguideAttenuator'
rszvb_SetPortWaveguideAttenuator.errcheck = __errorcheck__
rszvb_SetPortWaveguideAttenuator.output = False
# rszvb_GetPortWaveguideAttenuatorType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* waveguideAttenuator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'waveguideAttenuator'),)
rszvb_GetPortWaveguideAttenuatorType  = prototype(('rszvb_GetPortWaveguideAttenuatorType', rszvbDLL), paramflags)
rszvb_GetPortWaveguideAttenuatorType.name = 'rszvb_GetPortWaveguideAttenuatorType'
rszvb_GetPortWaveguideAttenuatorType.errcheck = __errorcheck__
rszvb_GetPortWaveguideAttenuatorType.output = True
# rszvb_GetPortWaveguideAttenuator ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 waveguideAttenuator', 'ViReal64* attenuation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'waveguideAttenuator'),(2, 'attenuation'),)
rszvb_GetPortWaveguideAttenuator  = prototype(('rszvb_GetPortWaveguideAttenuator', rszvbDLL), paramflags)
rszvb_GetPortWaveguideAttenuator.name = 'rszvb_GetPortWaveguideAttenuator'
rszvb_GetPortWaveguideAttenuator.errcheck = __errorcheck__
rszvb_GetPortWaveguideAttenuator.output = True
# rszvb_SetPortWaveguideAttenuatorSlope ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 slope']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'slope'),)
rszvb_SetPortWaveguideAttenuatorSlope  = prototype(('rszvb_SetPortWaveguideAttenuatorSlope', rszvbDLL), paramflags)
rszvb_SetPortWaveguideAttenuatorSlope.name = 'rszvb_SetPortWaveguideAttenuatorSlope'
rszvb_SetPortWaveguideAttenuatorSlope.errcheck = __errorcheck__
rszvb_SetPortWaveguideAttenuatorSlope.output = False
# rszvb_GetPortWaveguideAttenuatorSlope ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* slope']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'slope'),)
rszvb_GetPortWaveguideAttenuatorSlope  = prototype(('rszvb_GetPortWaveguideAttenuatorSlope', rszvbDLL), paramflags)
rszvb_GetPortWaveguideAttenuatorSlope.name = 'rszvb_GetPortWaveguideAttenuatorSlope'
rszvb_GetPortWaveguideAttenuatorSlope.errcheck = __errorcheck__
rszvb_GetPortWaveguideAttenuatorSlope.output = True
# rszvb_SetPortWaveguideAttenuatorOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 offset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'offset'),)
rszvb_SetPortWaveguideAttenuatorOffset  = prototype(('rszvb_SetPortWaveguideAttenuatorOffset', rszvbDLL), paramflags)
rszvb_SetPortWaveguideAttenuatorOffset.name = 'rszvb_SetPortWaveguideAttenuatorOffset'
rszvb_SetPortWaveguideAttenuatorOffset.errcheck = __errorcheck__
rszvb_SetPortWaveguideAttenuatorOffset.output = False
# rszvb_GetPortWaveguideAttenuatorOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* offset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'offset'),)
rszvb_GetPortWaveguideAttenuatorOffset  = prototype(('rszvb_GetPortWaveguideAttenuatorOffset', rszvbDLL), paramflags)
rszvb_GetPortWaveguideAttenuatorOffset.name = 'rszvb_GetPortWaveguideAttenuatorOffset'
rszvb_GetPortWaveguideAttenuatorOffset.errcheck = __errorcheck__
rszvb_GetPortWaveguideAttenuatorOffset.output = True
# rszvb_SetPortElectronicPowerTreshold ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 threshold']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'threshold'),)
rszvb_SetPortElectronicPowerTreshold  = prototype(('rszvb_SetPortElectronicPowerTreshold', rszvbDLL), paramflags)
rszvb_SetPortElectronicPowerTreshold.name = 'rszvb_SetPortElectronicPowerTreshold'
rszvb_SetPortElectronicPowerTreshold.errcheck = __errorcheck__
rszvb_SetPortElectronicPowerTreshold.output = False
# rszvb_GetPortElectronicPowerTreshold ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* threshold']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'threshold'),)
rszvb_GetPortElectronicPowerTreshold  = prototype(('rszvb_GetPortElectronicPowerTreshold', rszvbDLL), paramflags)
rszvb_GetPortElectronicPowerTreshold.name = 'rszvb_GetPortElectronicPowerTreshold'
rszvb_GetPortElectronicPowerTreshold.errcheck = __errorcheck__
rszvb_GetPortElectronicPowerTreshold.output = True
# rszvb_SetPortElectronicPowerReduction ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 reduction']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'reduction'),)
rszvb_SetPortElectronicPowerReduction  = prototype(('rszvb_SetPortElectronicPowerReduction', rszvbDLL), paramflags)
rszvb_SetPortElectronicPowerReduction.name = 'rszvb_SetPortElectronicPowerReduction'
rszvb_SetPortElectronicPowerReduction.errcheck = __errorcheck__
rszvb_SetPortElectronicPowerReduction.output = False
# rszvb_GetPortElectronicPowerReduction ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* reduction']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'reduction'),)
rszvb_GetPortElectronicPowerReduction  = prototype(('rszvb_GetPortElectronicPowerReduction', rszvbDLL), paramflags)
rszvb_GetPortElectronicPowerReduction.name = 'rszvb_GetPortElectronicPowerReduction'
rszvb_GetPortElectronicPowerReduction.errcheck = __errorcheck__
rszvb_GetPortElectronicPowerReduction.output = True
# rszvb_SetSimultaneousMeasurementOfPortsGroups ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetSimultaneousMeasurementOfPortsGroups  = prototype(('rszvb_SetSimultaneousMeasurementOfPortsGroups', rszvbDLL), paramflags)
rszvb_SetSimultaneousMeasurementOfPortsGroups.name = 'rszvb_SetSimultaneousMeasurementOfPortsGroups'
rszvb_SetSimultaneousMeasurementOfPortsGroups.errcheck = __errorcheck__
rszvb_SetSimultaneousMeasurementOfPortsGroups.output = False
# rszvb_GetSimultaneousMeasurementOfPortsGroups ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetSimultaneousMeasurementOfPortsGroups  = prototype(('rszvb_GetSimultaneousMeasurementOfPortsGroups', rszvbDLL), paramflags)
rszvb_GetSimultaneousMeasurementOfPortsGroups.name = 'rszvb_GetSimultaneousMeasurementOfPortsGroups'
rszvb_GetSimultaneousMeasurementOfPortsGroups.errcheck = __errorcheck__
rszvb_GetSimultaneousMeasurementOfPortsGroups.output = True
# rszvb_SetSimultaneousMeasurementFrequencyOffsetState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetSimultaneousMeasurementFrequencyOffsetState  = prototype(('rszvb_SetSimultaneousMeasurementFrequencyOffsetState', rszvbDLL), paramflags)
rszvb_SetSimultaneousMeasurementFrequencyOffsetState.name = 'rszvb_SetSimultaneousMeasurementFrequencyOffsetState'
rszvb_SetSimultaneousMeasurementFrequencyOffsetState.errcheck = __errorcheck__
rszvb_SetSimultaneousMeasurementFrequencyOffsetState.output = False
# rszvb_GetSimultaneousMeasurementFrequencyOffsetState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetSimultaneousMeasurementFrequencyOffsetState  = prototype(('rszvb_GetSimultaneousMeasurementFrequencyOffsetState', rszvbDLL), paramflags)
rszvb_GetSimultaneousMeasurementFrequencyOffsetState.name = 'rszvb_GetSimultaneousMeasurementFrequencyOffsetState'
rszvb_GetSimultaneousMeasurementFrequencyOffsetState.errcheck = __errorcheck__
rszvb_GetSimultaneousMeasurementFrequencyOffsetState.output = True
# rszvb_SetSimultaneousMeasurementMinimumFrequencyOffsetMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 minimumFrequencyOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'minimumFrequencyOffset'),)
rszvb_SetSimultaneousMeasurementMinimumFrequencyOffsetMode  = prototype(('rszvb_SetSimultaneousMeasurementMinimumFrequencyOffsetMode', rszvbDLL), paramflags)
rszvb_SetSimultaneousMeasurementMinimumFrequencyOffsetMode.name = 'rszvb_SetSimultaneousMeasurementMinimumFrequencyOffsetMode'
rszvb_SetSimultaneousMeasurementMinimumFrequencyOffsetMode.errcheck = __errorcheck__
rszvb_SetSimultaneousMeasurementMinimumFrequencyOffsetMode.output = False
# rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* minimumFrequencyOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'minimumFrequencyOffset'),)
rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetMode  = prototype(('rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetMode', rszvbDLL), paramflags)
rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetMode.name = 'rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetMode'
rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetMode.errcheck = __errorcheck__
rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetMode.output = True
# rszvb_SetFrequencyConversion ['ViSession instrumentHandle', 'ViInt32 measurementType', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 numerator', 'ViInt32 denominator', 'ViReal64 offset', 'ViInt32 sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_double,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'measurementType'),(1, 'channel',1),(1, 'port'),(1, 'numerator'),(1, 'denominator'),(1, 'offset'),(1, 'sweepType'),)
rszvb_SetFrequencyConversion  = prototype(('rszvb_SetFrequencyConversion', rszvbDLL), paramflags)
rszvb_SetFrequencyConversion.name = 'rszvb_SetFrequencyConversion'
rszvb_SetFrequencyConversion.errcheck = __errorcheck__
rszvb_SetFrequencyConversion.output = False
# rszvb_GetFrequencyConversion ['ViSession instrumentHandle', 'ViInt32 measurementType', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* numerator', 'ViInt32* denominator', 'ViReal64* offset', 'ViInt32* sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_int32),POINTER(c_int32),POINTER(c_double),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'measurementType'),(1, 'channel',1),(1, 'port'),(2, 'numerator'),(2, 'denominator'),(2, 'offset'),(2, 'sweepType'),)
rszvb_GetFrequencyConversion  = prototype(('rszvb_GetFrequencyConversion', rszvbDLL), paramflags)
rszvb_GetFrequencyConversion.name = 'rszvb_GetFrequencyConversion'
rszvb_GetFrequencyConversion.errcheck = __errorcheck__
rszvb_GetFrequencyConversion.output = True
# rszvb_SetPowerMeterFrequencyConversion ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 powerMeterNumber', 'ViInt32 numerator', 'ViInt32 denominator', 'ViReal64 offset', 'ViInt32 sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_double,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'powerMeterNumber'),(1, 'numerator'),(1, 'denominator'),(1, 'offset'),(1, 'sweepType'),)
rszvb_SetPowerMeterFrequencyConversion  = prototype(('rszvb_SetPowerMeterFrequencyConversion', rszvbDLL), paramflags)
rszvb_SetPowerMeterFrequencyConversion.name = 'rszvb_SetPowerMeterFrequencyConversion'
rszvb_SetPowerMeterFrequencyConversion.errcheck = __errorcheck__
rszvb_SetPowerMeterFrequencyConversion.output = False
# rszvb_GetPowerMeterFrequencyConversion ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 powerMeterNumber', 'ViInt32* numerator', 'ViInt32* denominator', 'ViReal64* offset', 'ViInt32* sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),POINTER(c_int32),POINTER(c_double),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'powerMeterNumber'),(2, 'numerator'),(2, 'denominator'),(2, 'offset'),(2, 'sweepType'),)
rszvb_GetPowerMeterFrequencyConversion  = prototype(('rszvb_GetPowerMeterFrequencyConversion', rszvbDLL), paramflags)
rszvb_GetPowerMeterFrequencyConversion.name = 'rszvb_GetPowerMeterFrequencyConversion'
rszvb_GetPowerMeterFrequencyConversion.errcheck = __errorcheck__
rszvb_GetPowerMeterFrequencyConversion.output = True
# rszvb_SetGeneratorFrequencyConversion ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 generatorNumber', 'ViBoolean state', 'ViInt32 numerator', 'ViInt32 denominator', 'ViReal64 offset', 'ViInt32 sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_bool,c_int32,c_int32,c_double,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'generatorNumber'),(1, 'state'),(1, 'numerator'),(1, 'denominator'),(1, 'offset'),(1, 'sweepType'),)
rszvb_SetGeneratorFrequencyConversion  = prototype(('rszvb_SetGeneratorFrequencyConversion', rszvbDLL), paramflags)
rszvb_SetGeneratorFrequencyConversion.name = 'rszvb_SetGeneratorFrequencyConversion'
rszvb_SetGeneratorFrequencyConversion.errcheck = __errorcheck__
rszvb_SetGeneratorFrequencyConversion.output = False
# rszvb_GetGeneratorFrequencyConversion ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 generatorNumber', 'ViBoolean* state', 'ViInt32* numerator', 'ViInt32* denominator', 'ViReal64* offset', 'ViInt32* sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_bool),POINTER(c_int32),POINTER(c_int32),POINTER(c_double),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'generatorNumber'),(2, 'state'),(2, 'numerator'),(2, 'denominator'),(2, 'offset'),(2, 'sweepType'),)
rszvb_GetGeneratorFrequencyConversion  = prototype(('rszvb_GetGeneratorFrequencyConversion', rszvbDLL), paramflags)
rszvb_GetGeneratorFrequencyConversion.name = 'rszvb_GetGeneratorFrequencyConversion'
rszvb_GetGeneratorFrequencyConversion.errcheck = __errorcheck__
rszvb_GetGeneratorFrequencyConversion.output = True
# rszvb_SetConverterSourceFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 numerator', 'ViInt32 denominator', 'ViReal64 offset', 'ViInt32 sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_double,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'numerator'),(1, 'denominator'),(1, 'offset'),(1, 'sweepType'),)
rszvb_SetConverterSourceFrequency  = prototype(('rszvb_SetConverterSourceFrequency', rszvbDLL), paramflags)
rszvb_SetConverterSourceFrequency.name = 'rszvb_SetConverterSourceFrequency'
rszvb_SetConverterSourceFrequency.errcheck = __errorcheck__
rszvb_SetConverterSourceFrequency.output = False
# rszvb_GetConverterSourceFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* numerator', 'ViInt32* denominator', 'ViReal64* offset', 'ViInt32* sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),POINTER(c_int32),POINTER(c_double),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'numerator'),(2, 'denominator'),(2, 'offset'),(2, 'sweepType'),)
rszvb_GetConverterSourceFrequency  = prototype(('rszvb_GetConverterSourceFrequency', rszvbDLL), paramflags)
rszvb_GetConverterSourceFrequency.name = 'rszvb_GetConverterSourceFrequency'
rszvb_GetConverterSourceFrequency.errcheck = __errorcheck__
rszvb_GetConverterSourceFrequency.output = True
# rszvb_SetMeasureAWavesState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetMeasureAWavesState  = prototype(('rszvb_SetMeasureAWavesState', rszvbDLL), paramflags)
rszvb_SetMeasureAWavesState.name = 'rszvb_SetMeasureAWavesState'
rszvb_SetMeasureAWavesState.errcheck = __errorcheck__
rszvb_SetMeasureAWavesState.output = False
# rszvb_GetMeasureAWavesState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetMeasureAWavesState  = prototype(('rszvb_GetMeasureAWavesState', rszvbDLL), paramflags)
rszvb_GetMeasureAWavesState.name = 'rszvb_GetMeasureAWavesState'
rszvb_GetMeasureAWavesState.errcheck = __errorcheck__
rszvb_GetMeasureAWavesState.output = True
# rszvb_SetLocalOscilatorAState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'state'),)
rszvb_SetLocalOscilatorAState  = prototype(('rszvb_SetLocalOscilatorAState', rszvbDLL), paramflags)
rszvb_SetLocalOscilatorAState.name = 'rszvb_SetLocalOscilatorAState'
rszvb_SetLocalOscilatorAState.errcheck = __errorcheck__
rszvb_SetLocalOscilatorAState.output = False
# rszvb_GetLocalOscilatorAState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'state'),)
rszvb_GetLocalOscilatorAState  = prototype(('rszvb_GetLocalOscilatorAState', rszvbDLL), paramflags)
rszvb_GetLocalOscilatorAState.name = 'rszvb_GetLocalOscilatorAState'
rszvb_GetLocalOscilatorAState.errcheck = __errorcheck__
rszvb_GetLocalOscilatorAState.output = True
# rszvb_SetLocalOscilatorBState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'state'),)
rszvb_SetLocalOscilatorBState  = prototype(('rszvb_SetLocalOscilatorBState', rszvbDLL), paramflags)
rszvb_SetLocalOscilatorBState.name = 'rszvb_SetLocalOscilatorBState'
rszvb_SetLocalOscilatorBState.errcheck = __errorcheck__
rszvb_SetLocalOscilatorBState.output = False
# rszvb_GetLocalOscilatorBState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'state'),)
rszvb_GetLocalOscilatorBState  = prototype(('rszvb_GetLocalOscilatorBState', rszvbDLL), paramflags)
rszvb_GetLocalOscilatorBState.name = 'rszvb_GetLocalOscilatorBState'
rszvb_GetLocalOscilatorBState.errcheck = __errorcheck__
rszvb_GetLocalOscilatorBState.output = True
# rszvb_SetLogicalPortCommonRefImpedance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 real', 'ViReal64 imaginary']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'real'),(1, 'imaginary'),)
rszvb_SetLogicalPortCommonRefImpedance  = prototype(('rszvb_SetLogicalPortCommonRefImpedance', rszvbDLL), paramflags)
rszvb_SetLogicalPortCommonRefImpedance.name = 'rszvb_SetLogicalPortCommonRefImpedance'
rszvb_SetLogicalPortCommonRefImpedance.errcheck = __errorcheck__
rszvb_SetLogicalPortCommonRefImpedance.output = False
# rszvb_GetLogicalPortCommonRefImpedance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* real', 'ViReal64* imaginary']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'real'),(2, 'imaginary'),)
rszvb_GetLogicalPortCommonRefImpedance  = prototype(('rszvb_GetLogicalPortCommonRefImpedance', rszvbDLL), paramflags)
rszvb_GetLogicalPortCommonRefImpedance.name = 'rszvb_GetLogicalPortCommonRefImpedance'
rszvb_GetLogicalPortCommonRefImpedance.errcheck = __errorcheck__
rszvb_GetLogicalPortCommonRefImpedance.output = True
# rszvb_SetLogicalPortDifferentialRefImpedance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 real', 'ViReal64 imaginary']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'real'),(1, 'imaginary'),)
rszvb_SetLogicalPortDifferentialRefImpedance  = prototype(('rszvb_SetLogicalPortDifferentialRefImpedance', rszvbDLL), paramflags)
rszvb_SetLogicalPortDifferentialRefImpedance.name = 'rszvb_SetLogicalPortDifferentialRefImpedance'
rszvb_SetLogicalPortDifferentialRefImpedance.errcheck = __errorcheck__
rszvb_SetLogicalPortDifferentialRefImpedance.output = False
# rszvb_GetLogicalPortDifferentialRefImpedance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* real', 'ViReal64* imaginary']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'real'),(2, 'imaginary'),)
rszvb_GetLogicalPortDifferentialRefImpedance  = prototype(('rszvb_GetLogicalPortDifferentialRefImpedance', rszvbDLL), paramflags)
rszvb_GetLogicalPortDifferentialRefImpedance.name = 'rszvb_GetLogicalPortDifferentialRefImpedance'
rszvb_GetLogicalPortDifferentialRefImpedance.errcheck = __errorcheck__
rszvb_GetLogicalPortDifferentialRefImpedance.output = True
# rszvb_SetPortImpedancesRenormalization ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 theory']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'theory'),)
rszvb_SetPortImpedancesRenormalization  = prototype(('rszvb_SetPortImpedancesRenormalization', rszvbDLL), paramflags)
rszvb_SetPortImpedancesRenormalization.name = 'rszvb_SetPortImpedancesRenormalization'
rszvb_SetPortImpedancesRenormalization.errcheck = __errorcheck__
rszvb_SetPortImpedancesRenormalization.output = False
# rszvb_GetPortImpedancesRenormalization ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* theory']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'theory'),)
rszvb_GetPortImpedancesRenormalization  = prototype(('rszvb_GetPortImpedancesRenormalization', rszvbDLL), paramflags)
rszvb_GetPortImpedancesRenormalization.name = 'rszvb_GetPortImpedancesRenormalization'
rszvb_GetPortImpedancesRenormalization.errcheck = __errorcheck__
rszvb_GetPortImpedancesRenormalization.output = True
# rszvb_SetPhysicalPortRefImpedance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 real', 'ViReal64 imaginary']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'real'),(1, 'imaginary'),)
rszvb_SetPhysicalPortRefImpedance  = prototype(('rszvb_SetPhysicalPortRefImpedance', rszvbDLL), paramflags)
rszvb_SetPhysicalPortRefImpedance.name = 'rszvb_SetPhysicalPortRefImpedance'
rszvb_SetPhysicalPortRefImpedance.errcheck = __errorcheck__
rszvb_SetPhysicalPortRefImpedance.output = False
# rszvb_GetPhysicalPortRefImpedance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* real', 'ViReal64* imaginary']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'real'),(2, 'imaginary'),)
rszvb_GetPhysicalPortRefImpedance  = prototype(('rszvb_GetPhysicalPortRefImpedance', rszvbDLL), paramflags)
rszvb_GetPhysicalPortRefImpedance.name = 'rszvb_GetPhysicalPortRefImpedance'
rszvb_GetPhysicalPortRefImpedance.errcheck = __errorcheck__
rszvb_GetPhysicalPortRefImpedance.output = True
# rszvb_SetIFGain ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 IFGain']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'IFGain'),)
rszvb_SetIFGain  = prototype(('rszvb_SetIFGain', rszvbDLL), paramflags)
rszvb_SetIFGain.name = 'rszvb_SetIFGain'
rszvb_SetIFGain.errcheck = __errorcheck__
rszvb_SetIFGain.output = False
# rszvb_GetIFGain ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* IFGain']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'IFGain'),)
rszvb_GetIFGain  = prototype(('rszvb_GetIFGain', rszvbDLL), paramflags)
rszvb_GetIFGain.name = 'rszvb_GetIFGain'
rszvb_GetIFGain.errcheck = __errorcheck__
rszvb_GetIFGain.output = True
# rszvb_SetIFGainReferenceChannel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 IFGain']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'IFGain'),)
rszvb_SetIFGainReferenceChannel  = prototype(('rszvb_SetIFGainReferenceChannel', rszvbDLL), paramflags)
rszvb_SetIFGainReferenceChannel.name = 'rszvb_SetIFGainReferenceChannel'
rszvb_SetIFGainReferenceChannel.errcheck = __errorcheck__
rszvb_SetIFGainReferenceChannel.output = False
# rszvb_GetIFGainReferenceChannel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* IFGain']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'IFGain'),)
rszvb_GetIFGainReferenceChannel  = prototype(('rszvb_GetIFGainReferenceChannel', rszvbDLL), paramflags)
rszvb_GetIFGainReferenceChannel.name = 'rszvb_GetIFGainReferenceChannel'
rszvb_GetIFGainReferenceChannel.errcheck = __errorcheck__
rszvb_GetIFGainReferenceChannel.output = True
# rszvb_SetRFSignalSourceState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'state'),)
rszvb_SetRFSignalSourceState  = prototype(('rszvb_SetRFSignalSourceState', rszvbDLL), paramflags)
rszvb_SetRFSignalSourceState.name = 'rszvb_SetRFSignalSourceState'
rszvb_SetRFSignalSourceState.errcheck = __errorcheck__
rszvb_SetRFSignalSourceState.output = False
# rszvb_GetRFSignalSourceState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'state'),)
rszvb_GetRFSignalSourceState  = prototype(('rszvb_GetRFSignalSourceState', rszvbDLL), paramflags)
rszvb_GetRFSignalSourceState.name = 'rszvb_GetRFSignalSourceState'
rszvb_GetRFSignalSourceState.errcheck = __errorcheck__
rszvb_GetRFSignalSourceState.output = True
# rszvb_SetPermanentSignalSourceState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'state'),)
rszvb_SetPermanentSignalSourceState  = prototype(('rszvb_SetPermanentSignalSourceState', rszvbDLL), paramflags)
rszvb_SetPermanentSignalSourceState.name = 'rszvb_SetPermanentSignalSourceState'
rszvb_SetPermanentSignalSourceState.errcheck = __errorcheck__
rszvb_SetPermanentSignalSourceState.output = False
# rszvb_GetPermanentSignalSourceState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'state'),)
rszvb_GetPermanentSignalSourceState  = prototype(('rszvb_GetPermanentSignalSourceState', rszvbDLL), paramflags)
rszvb_GetPermanentSignalSourceState.name = 'rszvb_GetPermanentSignalSourceState'
rszvb_GetPermanentSignalSourceState.errcheck = __errorcheck__
rszvb_GetPermanentSignalSourceState.output = True
# rszvb_SetPermanentSignalGeneratorState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 generatorNumber', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'generatorNumber'),(1, 'state'),)
rszvb_SetPermanentSignalGeneratorState  = prototype(('rszvb_SetPermanentSignalGeneratorState', rszvbDLL), paramflags)
rszvb_SetPermanentSignalGeneratorState.name = 'rszvb_SetPermanentSignalGeneratorState'
rszvb_SetPermanentSignalGeneratorState.errcheck = __errorcheck__
rszvb_SetPermanentSignalGeneratorState.output = False
# rszvb_GetPermanentSignalGeneratorState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 generatorNumber', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'generatorNumber'),(2, 'state'),)
rszvb_GetPermanentSignalGeneratorState  = prototype(('rszvb_GetPermanentSignalGeneratorState', rszvbDLL), paramflags)
rszvb_GetPermanentSignalGeneratorState.name = 'rszvb_GetPermanentSignalGeneratorState'
rszvb_GetPermanentSignalGeneratorState.errcheck = __errorcheck__
rszvb_GetPermanentSignalGeneratorState.output = True
# rszvb_SetPortPowerGeneratorOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViInt32 generatorNumber', 'ViReal64 portPowerOffset', 'ViInt32 offsetParameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_double,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'generatorNumber'),(1, 'portPowerOffset'),(1, 'offsetParameter'),)
rszvb_SetPortPowerGeneratorOffset  = prototype(('rszvb_SetPortPowerGeneratorOffset', rszvbDLL), paramflags)
rszvb_SetPortPowerGeneratorOffset.name = 'rszvb_SetPortPowerGeneratorOffset'
rszvb_SetPortPowerGeneratorOffset.errcheck = __errorcheck__
rszvb_SetPortPowerGeneratorOffset.output = False
# rszvb_GetPortPowerGeneratorOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViInt32 generatorNumber', 'ViReal64* portPowerOffset', 'ViInt32* offsetParameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_double),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'generatorNumber'),(2, 'portPowerOffset'),(2, 'offsetParameter'),)
rszvb_GetPortPowerGeneratorOffset  = prototype(('rszvb_GetPortPowerGeneratorOffset', rszvbDLL), paramflags)
rszvb_GetPortPowerGeneratorOffset.name = 'rszvb_GetPortPowerGeneratorOffset'
rszvb_GetPortPowerGeneratorOffset.errcheck = __errorcheck__
rszvb_GetPortPowerGeneratorOffset.output = True
# rszvb_SetSlope ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 slope']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'slope'),)
rszvb_SetSlope  = prototype(('rszvb_SetSlope', rszvbDLL), paramflags)
rszvb_SetSlope.name = 'rszvb_SetSlope'
rszvb_SetSlope.errcheck = __errorcheck__
rszvb_SetSlope.output = False
# rszvb_GetSlope ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* slope']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'slope'),)
rszvb_GetSlope  = prototype(('rszvb_GetSlope', rszvbDLL), paramflags)
rszvb_GetSlope.name = 'rszvb_GetSlope'
rszvb_GetSlope.errcheck = __errorcheck__
rszvb_GetSlope.output = True
# rszvb_SetSourceCombinerState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetSourceCombinerState  = prototype(('rszvb_SetSourceCombinerState', rszvbDLL), paramflags)
rszvb_SetSourceCombinerState.name = 'rszvb_SetSourceCombinerState'
rszvb_SetSourceCombinerState.errcheck = __errorcheck__
rszvb_SetSourceCombinerState.output = False
# rszvb_GetSourceCombinerState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetSourceCombinerState  = prototype(('rszvb_GetSourceCombinerState', rszvbDLL), paramflags)
rszvb_GetSourceCombinerState.name = 'rszvb_GetSourceCombinerState'
rszvb_GetSourceCombinerState.errcheck = __errorcheck__
rszvb_GetSourceCombinerState.output = True
# rszvb_SetFrequencyStimulus ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString frequencyStimulus']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'frequencyStimulus'),)
rszvb_SetFrequencyStimulus  = prototype(('rszvb_SetFrequencyStimulus', rszvbDLL), paramflags)
rszvb_SetFrequencyStimulus.name = 'rszvb_SetFrequencyStimulus'
rszvb_SetFrequencyStimulus.errcheck = __errorcheck__
rszvb_SetFrequencyStimulus.output = False
# rszvb_GetFrequencyStimulus ['ViSession instrumentHandle', 'ViInt32 channel', 'ViChar _VI_FAR frequencyStimulus[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'frequencyStimulus[]'),)
rszvb_GetFrequencyStimulus  = prototype(('rszvb_GetFrequencyStimulus', rszvbDLL), paramflags)
rszvb_GetFrequencyStimulus.name = 'rszvb_GetFrequencyStimulus'
rszvb_GetFrequencyStimulus.errcheck = __errorcheck__
rszvb_GetFrequencyStimulus.output = False
# rszvb_SetPowerStimulus ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString powerStimulus']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'powerStimulus'),)
rszvb_SetPowerStimulus  = prototype(('rszvb_SetPowerStimulus', rszvbDLL), paramflags)
rszvb_SetPowerStimulus.name = 'rszvb_SetPowerStimulus'
rszvb_SetPowerStimulus.errcheck = __errorcheck__
rszvb_SetPowerStimulus.output = False
# rszvb_GetPowerStimulus ['ViSession instrumentHandle', 'ViInt32 channel', 'ViChar _VI_FAR powerStimulus[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'powerStimulus[]'),)
rszvb_GetPowerStimulus  = prototype(('rszvb_GetPowerStimulus', rszvbDLL), paramflags)
rszvb_GetPowerStimulus.name = 'rszvb_GetPowerStimulus'
rszvb_GetPowerStimulus.errcheck = __errorcheck__
rszvb_GetPowerStimulus.output = False
# rszvb_SetTDIFState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean trueDifferentialModeState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'trueDifferentialModeState'),)
rszvb_SetTDIFState  = prototype(('rszvb_SetTDIFState', rszvbDLL), paramflags)
rszvb_SetTDIFState.name = 'rszvb_SetTDIFState'
rszvb_SetTDIFState.errcheck = __errorcheck__
rszvb_SetTDIFState.output = False
# rszvb_GetTDIFState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* trueDifferentialModeState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'trueDifferentialModeState'),)
rszvb_GetTDIFState  = prototype(('rszvb_GetTDIFState', rszvbDLL), paramflags)
rszvb_GetTDIFState.name = 'rszvb_GetTDIFState'
rszvb_GetTDIFState.errcheck = __errorcheck__
rszvb_GetTDIFState.output = True
# rszvb_SetTDIFAmplitudeImbalanceLogicalPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),)
rszvb_SetTDIFAmplitudeImbalanceLogicalPort  = prototype(('rszvb_SetTDIFAmplitudeImbalanceLogicalPort', rszvbDLL), paramflags)
rszvb_SetTDIFAmplitudeImbalanceLogicalPort.name = 'rszvb_SetTDIFAmplitudeImbalanceLogicalPort'
rszvb_SetTDIFAmplitudeImbalanceLogicalPort.errcheck = __errorcheck__
rszvb_SetTDIFAmplitudeImbalanceLogicalPort.output = False
# rszvb_GetTDIFAmplitudeImbalanceLogicalPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* port']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'port'),)
rszvb_GetTDIFAmplitudeImbalanceLogicalPort  = prototype(('rszvb_GetTDIFAmplitudeImbalanceLogicalPort', rszvbDLL), paramflags)
rszvb_GetTDIFAmplitudeImbalanceLogicalPort.name = 'rszvb_GetTDIFAmplitudeImbalanceLogicalPort'
rszvb_GetTDIFAmplitudeImbalanceLogicalPort.errcheck = __errorcheck__
rszvb_GetTDIFAmplitudeImbalanceLogicalPort.output = True
# rszvb_SetTDIFAmplitudeImbalanceStartPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 startPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'startPower'),)
rszvb_SetTDIFAmplitudeImbalanceStartPower  = prototype(('rszvb_SetTDIFAmplitudeImbalanceStartPower', rszvbDLL), paramflags)
rszvb_SetTDIFAmplitudeImbalanceStartPower.name = 'rszvb_SetTDIFAmplitudeImbalanceStartPower'
rszvb_SetTDIFAmplitudeImbalanceStartPower.errcheck = __errorcheck__
rszvb_SetTDIFAmplitudeImbalanceStartPower.output = False
# rszvb_GetTDIFAmplitudeImbalanceStartPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* startPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'startPower'),)
rszvb_GetTDIFAmplitudeImbalanceStartPower  = prototype(('rszvb_GetTDIFAmplitudeImbalanceStartPower', rszvbDLL), paramflags)
rszvb_GetTDIFAmplitudeImbalanceStartPower.name = 'rszvb_GetTDIFAmplitudeImbalanceStartPower'
rszvb_GetTDIFAmplitudeImbalanceStartPower.errcheck = __errorcheck__
rszvb_GetTDIFAmplitudeImbalanceStartPower.output = True
# rszvb_SetTDIFAmplitudeImbalanceStopPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 stopPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'stopPower'),)
rszvb_SetTDIFAmplitudeImbalanceStopPower  = prototype(('rszvb_SetTDIFAmplitudeImbalanceStopPower', rszvbDLL), paramflags)
rszvb_SetTDIFAmplitudeImbalanceStopPower.name = 'rszvb_SetTDIFAmplitudeImbalanceStopPower'
rszvb_SetTDIFAmplitudeImbalanceStopPower.errcheck = __errorcheck__
rszvb_SetTDIFAmplitudeImbalanceStopPower.output = False
# rszvb_GetTDIFAmplitudeImbalanceStopPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* stopPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'stopPower'),)
rszvb_GetTDIFAmplitudeImbalanceStopPower  = prototype(('rszvb_GetTDIFAmplitudeImbalanceStopPower', rszvbDLL), paramflags)
rszvb_GetTDIFAmplitudeImbalanceStopPower.name = 'rszvb_GetTDIFAmplitudeImbalanceStopPower'
rszvb_GetTDIFAmplitudeImbalanceStopPower.errcheck = __errorcheck__
rszvb_GetTDIFAmplitudeImbalanceStopPower.output = True
# rszvb_SetTDIFPhaseImbalanceLogicalPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),)
rszvb_SetTDIFPhaseImbalanceLogicalPort  = prototype(('rszvb_SetTDIFPhaseImbalanceLogicalPort', rszvbDLL), paramflags)
rszvb_SetTDIFPhaseImbalanceLogicalPort.name = 'rszvb_SetTDIFPhaseImbalanceLogicalPort'
rszvb_SetTDIFPhaseImbalanceLogicalPort.errcheck = __errorcheck__
rszvb_SetTDIFPhaseImbalanceLogicalPort.output = False
# rszvb_GetTDIFPhaseImbalanceLogicalPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* port']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'port'),)
rszvb_GetTDIFPhaseImbalanceLogicalPort  = prototype(('rszvb_GetTDIFPhaseImbalanceLogicalPort', rszvbDLL), paramflags)
rszvb_GetTDIFPhaseImbalanceLogicalPort.name = 'rszvb_GetTDIFPhaseImbalanceLogicalPort'
rszvb_GetTDIFPhaseImbalanceLogicalPort.errcheck = __errorcheck__
rszvb_GetTDIFPhaseImbalanceLogicalPort.output = True
# rszvb_SetTDIFPhaseImbalanceStartPhase ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 startPhase']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'startPhase'),)
rszvb_SetTDIFPhaseImbalanceStartPhase  = prototype(('rszvb_SetTDIFPhaseImbalanceStartPhase', rszvbDLL), paramflags)
rszvb_SetTDIFPhaseImbalanceStartPhase.name = 'rszvb_SetTDIFPhaseImbalanceStartPhase'
rszvb_SetTDIFPhaseImbalanceStartPhase.errcheck = __errorcheck__
rszvb_SetTDIFPhaseImbalanceStartPhase.output = False
# rszvb_GetTDIFPhaseImbalanceStartPhase ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* startPhase']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'startPhase'),)
rszvb_GetTDIFPhaseImbalanceStartPhase  = prototype(('rszvb_GetTDIFPhaseImbalanceStartPhase', rszvbDLL), paramflags)
rszvb_GetTDIFPhaseImbalanceStartPhase.name = 'rszvb_GetTDIFPhaseImbalanceStartPhase'
rszvb_GetTDIFPhaseImbalanceStartPhase.errcheck = __errorcheck__
rszvb_GetTDIFPhaseImbalanceStartPhase.output = True
# rszvb_SetTDIFPhaseImbalanceStopPhase ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 stopPhase']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'stopPhase'),)
rszvb_SetTDIFPhaseImbalanceStopPhase  = prototype(('rszvb_SetTDIFPhaseImbalanceStopPhase', rszvbDLL), paramflags)
rszvb_SetTDIFPhaseImbalanceStopPhase.name = 'rszvb_SetTDIFPhaseImbalanceStopPhase'
rszvb_SetTDIFPhaseImbalanceStopPhase.errcheck = __errorcheck__
rszvb_SetTDIFPhaseImbalanceStopPhase.output = False
# rszvb_GetTDIFPhaseImbalanceStopPhase ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* stopPhase']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'stopPhase'),)
rszvb_GetTDIFPhaseImbalanceStopPhase  = prototype(('rszvb_GetTDIFPhaseImbalanceStopPhase', rszvbDLL), paramflags)
rszvb_GetTDIFPhaseImbalanceStopPhase.name = 'rszvb_GetTDIFPhaseImbalanceStopPhase'
rszvb_GetTDIFPhaseImbalanceStopPhase.errcheck = __errorcheck__
rszvb_GetTDIFPhaseImbalanceStopPhase.output = True
# rszvb_SetTDIFSourcePowerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 sourcePowerMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'sourcePowerMode'),)
rszvb_SetTDIFSourcePowerMode  = prototype(('rszvb_SetTDIFSourcePowerMode', rszvbDLL), paramflags)
rszvb_SetTDIFSourcePowerMode.name = 'rszvb_SetTDIFSourcePowerMode'
rszvb_SetTDIFSourcePowerMode.errcheck = __errorcheck__
rszvb_SetTDIFSourcePowerMode.output = False
# rszvb_GetTDIFSourcePowerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* sourcePowerMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'sourcePowerMode'),)
rszvb_GetTDIFSourcePowerMode  = prototype(('rszvb_GetTDIFSourcePowerMode', rszvbDLL), paramflags)
rszvb_GetTDIFSourcePowerMode.name = 'rszvb_GetTDIFSourcePowerMode'
rszvb_GetTDIFSourcePowerMode.errcheck = __errorcheck__
rszvb_GetTDIFSourcePowerMode.output = True
# rszvb_SetTDIFCompensationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean compensationState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'compensationState'),)
rszvb_SetTDIFCompensationState  = prototype(('rszvb_SetTDIFCompensationState', rszvbDLL), paramflags)
rszvb_SetTDIFCompensationState.name = 'rszvb_SetTDIFCompensationState'
rszvb_SetTDIFCompensationState.errcheck = __errorcheck__
rszvb_SetTDIFCompensationState.output = False
# rszvb_GetTDIFCompensationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* compensationState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'compensationState'),)
rszvb_GetTDIFCompensationState  = prototype(('rszvb_GetTDIFCompensationState', rszvbDLL), paramflags)
rszvb_GetTDIFCompensationState.name = 'rszvb_GetTDIFCompensationState'
rszvb_GetTDIFCompensationState.errcheck = __errorcheck__
rszvb_GetTDIFCompensationState.output = True
# rszvb_SetTDIFReceiverFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 receiverFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverFrequency'),)
rszvb_SetTDIFReceiverFrequency  = prototype(('rszvb_SetTDIFReceiverFrequency', rszvbDLL), paramflags)
rszvb_SetTDIFReceiverFrequency.name = 'rszvb_SetTDIFReceiverFrequency'
rszvb_SetTDIFReceiverFrequency.errcheck = __errorcheck__
rszvb_SetTDIFReceiverFrequency.output = False
# rszvb_GetTDIFReceiverFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* receiverFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'receiverFrequency'),)
rszvb_GetTDIFReceiverFrequency  = prototype(('rszvb_GetTDIFReceiverFrequency', rszvbDLL), paramflags)
rszvb_GetTDIFReceiverFrequency.name = 'rszvb_GetTDIFReceiverFrequency'
rszvb_GetTDIFReceiverFrequency.errcheck = __errorcheck__
rszvb_GetTDIFReceiverFrequency.output = True
# rszvb_SetPulseGeneratorState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean pulseGeneratorState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'pulseGeneratorState'),)
rszvb_SetPulseGeneratorState  = prototype(('rszvb_SetPulseGeneratorState', rszvbDLL), paramflags)
rszvb_SetPulseGeneratorState.name = 'rszvb_SetPulseGeneratorState'
rszvb_SetPulseGeneratorState.errcheck = __errorcheck__
rszvb_SetPulseGeneratorState.output = False
# rszvb_GetPulseGeneratorState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* pulseGeneratorState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'pulseGeneratorState'),)
rszvb_GetPulseGeneratorState  = prototype(('rszvb_GetPulseGeneratorState', rszvbDLL), paramflags)
rszvb_GetPulseGeneratorState.name = 'rszvb_GetPulseGeneratorState'
rszvb_GetPulseGeneratorState.errcheck = __errorcheck__
rszvb_GetPulseGeneratorState.output = True
# rszvb_DefinePulseGenerator ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generator', 'ViInt32 pulseType', 'ViReal64 pulseWidth', 'ViReal64 singleTrainPulsePeriod', 'ViInt32 pulsePolarity', 'ViInt32 pulseMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_double,c_double,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generator'),(1, 'pulseType'),(1, 'pulseWidth'),(1, 'singleTrainPulsePeriod'),(1, 'pulsePolarity'),(1, 'pulseMode'),)
rszvb_DefinePulseGenerator  = prototype(('rszvb_DefinePulseGenerator', rszvbDLL), paramflags)
rszvb_DefinePulseGenerator.name = 'rszvb_DefinePulseGenerator'
rszvb_DefinePulseGenerator.errcheck = __errorcheck__
rszvb_DefinePulseGenerator.output = False
# rszvb_DefinePulseTrainSegments ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 bufferSize', 'ViInt32 _VI_FAR pulseTrainActive[]', 'ViReal64 _VI_FAR startTime[]', 'ViReal64 _VI_FAR stopTime[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'bufferSize'),(1, 'pulseTrainActive[]'),(1, 'startTime[]'),(1, 'stopTime[]'),)
rszvb_DefinePulseTrainSegments  = prototype(('rszvb_DefinePulseTrainSegments', rszvbDLL), paramflags)
rszvb_DefinePulseTrainSegments.name = 'rszvb_DefinePulseTrainSegments'
rszvb_DefinePulseTrainSegments.errcheck = __errorcheck__
rszvb_DefinePulseTrainSegments.output = False
# rszvb_ConfigureChoppedPulseProfile ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean choppedPulseProfileMode', 'ViReal64 delayIncrement']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'choppedPulseProfileMode'),(1, 'delayIncrement'),)
rszvb_ConfigureChoppedPulseProfile  = prototype(('rszvb_ConfigureChoppedPulseProfile', rszvbDLL), paramflags)
rszvb_ConfigureChoppedPulseProfile.name = 'rszvb_ConfigureChoppedPulseProfile'
rszvb_ConfigureChoppedPulseProfile.errcheck = __errorcheck__
rszvb_ConfigureChoppedPulseProfile.output = False
# rszvb_SetPulseGeneratorType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generator', 'ViInt32 pulseType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generator'),(1, 'pulseType'),)
rszvb_SetPulseGeneratorType  = prototype(('rszvb_SetPulseGeneratorType', rszvbDLL), paramflags)
rszvb_SetPulseGeneratorType.name = 'rszvb_SetPulseGeneratorType'
rszvb_SetPulseGeneratorType.errcheck = __errorcheck__
rszvb_SetPulseGeneratorType.output = False
# rszvb_GetPulseGeneratorType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generator', 'ViInt32* pulseType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generator'),(2, 'pulseType'),)
rszvb_GetPulseGeneratorType  = prototype(('rszvb_GetPulseGeneratorType', rszvbDLL), paramflags)
rszvb_GetPulseGeneratorType.name = 'rszvb_GetPulseGeneratorType'
rszvb_GetPulseGeneratorType.errcheck = __errorcheck__
rszvb_GetPulseGeneratorType.output = True
# rszvb_SetPulseGeneratorWidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generator', 'ViReal64 pulseWidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generator'),(1, 'pulseWidth'),)
rszvb_SetPulseGeneratorWidth  = prototype(('rszvb_SetPulseGeneratorWidth', rszvbDLL), paramflags)
rszvb_SetPulseGeneratorWidth.name = 'rszvb_SetPulseGeneratorWidth'
rszvb_SetPulseGeneratorWidth.errcheck = __errorcheck__
rszvb_SetPulseGeneratorWidth.output = False
# rszvb_GetPulseGeneratorWidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generator', 'ViReal64* pulseWidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generator'),(2, 'pulseWidth'),)
rszvb_GetPulseGeneratorWidth  = prototype(('rszvb_GetPulseGeneratorWidth', rszvbDLL), paramflags)
rszvb_GetPulseGeneratorWidth.name = 'rszvb_GetPulseGeneratorWidth'
rszvb_GetPulseGeneratorWidth.errcheck = __errorcheck__
rszvb_GetPulseGeneratorWidth.output = True
# rszvb_SetPulseGeneratorSinglePeriod ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 singlePulsePeriod']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'singlePulsePeriod'),)
rszvb_SetPulseGeneratorSinglePeriod  = prototype(('rszvb_SetPulseGeneratorSinglePeriod', rszvbDLL), paramflags)
rszvb_SetPulseGeneratorSinglePeriod.name = 'rszvb_SetPulseGeneratorSinglePeriod'
rszvb_SetPulseGeneratorSinglePeriod.errcheck = __errorcheck__
rszvb_SetPulseGeneratorSinglePeriod.output = False
# rszvb_GetPulseGeneratorSinglePeriod ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* singlePulsePeriod']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'singlePulsePeriod'),)
rszvb_GetPulseGeneratorSinglePeriod  = prototype(('rszvb_GetPulseGeneratorSinglePeriod', rszvbDLL), paramflags)
rszvb_GetPulseGeneratorSinglePeriod.name = 'rszvb_GetPulseGeneratorSinglePeriod'
rszvb_GetPulseGeneratorSinglePeriod.errcheck = __errorcheck__
rszvb_GetPulseGeneratorSinglePeriod.output = True
# rszvb_SetPulseGeneratorTrainPeriod ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 trainPulsePeriod']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'trainPulsePeriod'),)
rszvb_SetPulseGeneratorTrainPeriod  = prototype(('rszvb_SetPulseGeneratorTrainPeriod', rszvbDLL), paramflags)
rszvb_SetPulseGeneratorTrainPeriod.name = 'rszvb_SetPulseGeneratorTrainPeriod'
rszvb_SetPulseGeneratorTrainPeriod.errcheck = __errorcheck__
rszvb_SetPulseGeneratorTrainPeriod.output = False
# rszvb_GetPulseGeneratorTrainPeriod ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* trainPulsePeriod']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'trainPulsePeriod'),)
rszvb_GetPulseGeneratorTrainPeriod  = prototype(('rszvb_GetPulseGeneratorTrainPeriod', rszvbDLL), paramflags)
rszvb_GetPulseGeneratorTrainPeriod.name = 'rszvb_GetPulseGeneratorTrainPeriod'
rszvb_GetPulseGeneratorTrainPeriod.errcheck = __errorcheck__
rszvb_GetPulseGeneratorTrainPeriod.output = True
# rszvb_SetPulseGeneratorPolarity ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generator', 'ViInt32 pulsePolarity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generator'),(1, 'pulsePolarity'),)
rszvb_SetPulseGeneratorPolarity  = prototype(('rszvb_SetPulseGeneratorPolarity', rszvbDLL), paramflags)
rszvb_SetPulseGeneratorPolarity.name = 'rszvb_SetPulseGeneratorPolarity'
rszvb_SetPulseGeneratorPolarity.errcheck = __errorcheck__
rszvb_SetPulseGeneratorPolarity.output = False
# rszvb_GetPulseGeneratorPolarity ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generator', 'ViInt32* pulsePolarity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generator'),(2, 'pulsePolarity'),)
rszvb_GetPulseGeneratorPolarity  = prototype(('rszvb_GetPulseGeneratorPolarity', rszvbDLL), paramflags)
rszvb_GetPulseGeneratorPolarity.name = 'rszvb_GetPulseGeneratorPolarity'
rszvb_GetPulseGeneratorPolarity.errcheck = __errorcheck__
rszvb_GetPulseGeneratorPolarity.output = True
# rszvb_SetPulseGeneratorMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 pulseMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'pulseMode'),)
rszvb_SetPulseGeneratorMode  = prototype(('rszvb_SetPulseGeneratorMode', rszvbDLL), paramflags)
rszvb_SetPulseGeneratorMode.name = 'rszvb_SetPulseGeneratorMode'
rszvb_SetPulseGeneratorMode.errcheck = __errorcheck__
rszvb_SetPulseGeneratorMode.output = False
# rszvb_GetPulseGeneratorMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* pulseMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'pulseMode'),)
rszvb_GetPulseGeneratorMode  = prototype(('rszvb_GetPulseGeneratorMode', rszvbDLL), paramflags)
rszvb_GetPulseGeneratorMode.name = 'rszvb_GetPulseGeneratorMode'
rszvb_GetPulseGeneratorMode.errcheck = __errorcheck__
rszvb_GetPulseGeneratorMode.output = True
# rszvb_SetPulseGeneratorMasterChannel ['ViSession instrumentHandle', 'ViInt32 masterChannel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'masterChannel'),)
rszvb_SetPulseGeneratorMasterChannel  = prototype(('rszvb_SetPulseGeneratorMasterChannel', rszvbDLL), paramflags)
rszvb_SetPulseGeneratorMasterChannel.name = 'rszvb_SetPulseGeneratorMasterChannel'
rszvb_SetPulseGeneratorMasterChannel.errcheck = __errorcheck__
rszvb_SetPulseGeneratorMasterChannel.output = False
# rszvb_GetPulseGeneratorMasterChannel ['ViSession instrumentHandle', 'ViInt32* masterChannel']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'masterChannel'),)
rszvb_GetPulseGeneratorMasterChannel  = prototype(('rszvb_GetPulseGeneratorMasterChannel', rszvbDLL), paramflags)
rszvb_GetPulseGeneratorMasterChannel.name = 'rszvb_GetPulseGeneratorMasterChannel'
rszvb_GetPulseGeneratorMasterChannel.errcheck = __errorcheck__
rszvb_GetPulseGeneratorMasterChannel.output = True
# rszvb_GetPulseTrainSegments ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 bufferSize', 'ViInt32 _VI_FAR pulseTrainActive[]', 'ViReal64 _VI_FAR startTime[]', 'ViReal64 _VI_FAR stopTime[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'bufferSize'),(1, 'pulseTrainActive[]'),(1, 'startTime[]'),(1, 'stopTime[]'),)
rszvb_GetPulseTrainSegments  = prototype(('rszvb_GetPulseTrainSegments', rszvbDLL), paramflags)
rszvb_GetPulseTrainSegments.name = 'rszvb_GetPulseTrainSegments'
rszvb_GetPulseTrainSegments.errcheck = __errorcheck__
rszvb_GetPulseTrainSegments.output = False
# rszvb_SetPulseTrainSegmentState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean segmentState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'segmentState'),)
rszvb_SetPulseTrainSegmentState  = prototype(('rszvb_SetPulseTrainSegmentState', rszvbDLL), paramflags)
rszvb_SetPulseTrainSegmentState.name = 'rszvb_SetPulseTrainSegmentState'
rszvb_SetPulseTrainSegmentState.errcheck = __errorcheck__
rszvb_SetPulseTrainSegmentState.output = False
# rszvb_GetPulseTrainSegmentState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViBoolean* segmentState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'segmentState'),)
rszvb_GetPulseTrainSegmentState  = prototype(('rszvb_GetPulseTrainSegmentState', rszvbDLL), paramflags)
rszvb_GetPulseTrainSegmentState.name = 'rszvb_GetPulseTrainSegmentState'
rszvb_GetPulseTrainSegmentState.errcheck = __errorcheck__
rszvb_GetPulseTrainSegmentState.output = True
# rszvb_SetPulseTrainSegmentStart ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64 segmentStart']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'segmentStart'),)
rszvb_SetPulseTrainSegmentStart  = prototype(('rszvb_SetPulseTrainSegmentStart', rszvbDLL), paramflags)
rszvb_SetPulseTrainSegmentStart.name = 'rszvb_SetPulseTrainSegmentStart'
rszvb_SetPulseTrainSegmentStart.errcheck = __errorcheck__
rszvb_SetPulseTrainSegmentStart.output = False
# rszvb_GetPulseTrainSegmentStart ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64* segmentStart']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'segmentStart'),)
rszvb_GetPulseTrainSegmentStart  = prototype(('rszvb_GetPulseTrainSegmentStart', rszvbDLL), paramflags)
rszvb_GetPulseTrainSegmentStart.name = 'rszvb_GetPulseTrainSegmentStart'
rszvb_GetPulseTrainSegmentStart.errcheck = __errorcheck__
rszvb_GetPulseTrainSegmentStart.output = True
# rszvb_SetPulseTrainSegmentStop ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64 segmentStop']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(1, 'segmentStop'),)
rszvb_SetPulseTrainSegmentStop  = prototype(('rszvb_SetPulseTrainSegmentStop', rszvbDLL), paramflags)
rszvb_SetPulseTrainSegmentStop.name = 'rszvb_SetPulseTrainSegmentStop'
rszvb_SetPulseTrainSegmentStop.errcheck = __errorcheck__
rszvb_SetPulseTrainSegmentStop.output = False
# rszvb_GetPulseTrainSegmentStop ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 segment', 'ViReal64* segmentStop']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'segment'),(2, 'segmentStop'),)
rszvb_GetPulseTrainSegmentStop  = prototype(('rszvb_GetPulseTrainSegmentStop', rszvbDLL), paramflags)
rszvb_GetPulseTrainSegmentStop.name = 'rszvb_GetPulseTrainSegmentStop'
rszvb_GetPulseTrainSegmentStop.errcheck = __errorcheck__
rszvb_GetPulseTrainSegmentStop.output = True
# rszvb_GetPulseTrainSegmentCount ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* segmentCount']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'segmentCount'),)
rszvb_GetPulseTrainSegmentCount  = prototype(('rszvb_GetPulseTrainSegmentCount', rszvbDLL), paramflags)
rszvb_GetPulseTrainSegmentCount.name = 'rszvb_GetPulseTrainSegmentCount'
rszvb_GetPulseTrainSegmentCount.errcheck = __errorcheck__
rszvb_GetPulseTrainSegmentCount.output = True
# rszvb_DeleteAllPulseTrainSegments ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_DeleteAllPulseTrainSegments  = prototype(('rszvb_DeleteAllPulseTrainSegments', rszvbDLL), paramflags)
rszvb_DeleteAllPulseTrainSegments.name = 'rszvb_DeleteAllPulseTrainSegments'
rszvb_DeleteAllPulseTrainSegments.errcheck = __errorcheck__
rszvb_DeleteAllPulseTrainSegments.output = False
# rszvb_SavePulseTrainFile ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generator', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generator'),(1, 'fileName'),)
rszvb_SavePulseTrainFile  = prototype(('rszvb_SavePulseTrainFile', rszvbDLL), paramflags)
rszvb_SavePulseTrainFile.name = 'rszvb_SavePulseTrainFile'
rszvb_SavePulseTrainFile.errcheck = __errorcheck__
rszvb_SavePulseTrainFile.output = False
# rszvb_LoadPulseTrainFile ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 generator', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'generator'),(1, 'fileName'),)
rszvb_LoadPulseTrainFile  = prototype(('rszvb_LoadPulseTrainFile', rszvbDLL), paramflags)
rszvb_LoadPulseTrainFile.name = 'rszvb_LoadPulseTrainFile'
rszvb_LoadPulseTrainFile.errcheck = __errorcheck__
rszvb_LoadPulseTrainFile.output = False
# rszvb_SetPulseGeneratorDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 delay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'delay'),)
rszvb_SetPulseGeneratorDelay  = prototype(('rszvb_SetPulseGeneratorDelay', rszvbDLL), paramflags)
rszvb_SetPulseGeneratorDelay.name = 'rszvb_SetPulseGeneratorDelay'
rszvb_SetPulseGeneratorDelay.errcheck = __errorcheck__
rszvb_SetPulseGeneratorDelay.output = False
# rszvb_GetPulseGeneratorDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* delay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'delay'),)
rszvb_GetPulseGeneratorDelay  = prototype(('rszvb_GetPulseGeneratorDelay', rszvbDLL), paramflags)
rszvb_GetPulseGeneratorDelay.name = 'rszvb_GetPulseGeneratorDelay'
rszvb_GetPulseGeneratorDelay.errcheck = __errorcheck__
rszvb_GetPulseGeneratorDelay.output = True
# rszvb_SetChoppedPulseProfileMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean choppedPulseProfileMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'choppedPulseProfileMode'),)
rszvb_SetChoppedPulseProfileMode  = prototype(('rszvb_SetChoppedPulseProfileMode', rszvbDLL), paramflags)
rszvb_SetChoppedPulseProfileMode.name = 'rszvb_SetChoppedPulseProfileMode'
rszvb_SetChoppedPulseProfileMode.errcheck = __errorcheck__
rszvb_SetChoppedPulseProfileMode.output = False
# rszvb_GetChoppedPulseProfileMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* choppedPulseProfileMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'choppedPulseProfileMode'),)
rszvb_GetChoppedPulseProfileMode  = prototype(('rszvb_GetChoppedPulseProfileMode', rszvbDLL), paramflags)
rszvb_GetChoppedPulseProfileMode.name = 'rszvb_GetChoppedPulseProfileMode'
rszvb_GetChoppedPulseProfileMode.errcheck = __errorcheck__
rszvb_GetChoppedPulseProfileMode.output = True
# rszvb_SetChoppedPulseProfileDelayIncrement ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 delayIncrement']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'delayIncrement'),)
rszvb_SetChoppedPulseProfileDelayIncrement  = prototype(('rszvb_SetChoppedPulseProfileDelayIncrement', rszvbDLL), paramflags)
rszvb_SetChoppedPulseProfileDelayIncrement.name = 'rszvb_SetChoppedPulseProfileDelayIncrement'
rszvb_SetChoppedPulseProfileDelayIncrement.errcheck = __errorcheck__
rszvb_SetChoppedPulseProfileDelayIncrement.output = False
# rszvb_GetChoppedPulseProfileDelayIncrement ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* delayIncrement']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'delayIncrement'),)
rszvb_GetChoppedPulseProfileDelayIncrement  = prototype(('rszvb_GetChoppedPulseProfileDelayIncrement', rszvbDLL), paramflags)
rszvb_GetChoppedPulseProfileDelayIncrement.name = 'rszvb_GetChoppedPulseProfileDelayIncrement'
rszvb_GetChoppedPulseProfileDelayIncrement.errcheck = __errorcheck__
rszvb_GetChoppedPulseProfileDelayIncrement.output = True
# rszvb_ConfigureZVAXPath ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean internalCombiner', 'ViBoolean harmonicFilter', 'ViBoolean pulseModulator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool,c_bool,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(1, 'internalCombiner'),(1, 'harmonicFilter'),(1, 'pulseModulator'),)
rszvb_ConfigureZVAXPath  = prototype(('rszvb_ConfigureZVAXPath', rszvbDLL), paramflags)
rszvb_ConfigureZVAXPath.name = 'rszvb_ConfigureZVAXPath'
rszvb_ConfigureZVAXPath.errcheck = __errorcheck__
rszvb_ConfigureZVAXPath.output = False
# rszvb_ConfigurePulseGenerators ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean extSignalGeneratorInput', 'ViBoolean extSignalGeneratorOutput', 'ViInt32 assignment']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool,c_bool,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'extSignalGeneratorInput'),(1, 'extSignalGeneratorOutput'),(1, 'assignment'),)
rszvb_ConfigurePulseGenerators  = prototype(('rszvb_ConfigurePulseGenerators', rszvbDLL), paramflags)
rszvb_ConfigurePulseGenerators.name = 'rszvb_ConfigurePulseGenerators'
rszvb_ConfigurePulseGenerators.errcheck = __errorcheck__
rszvb_ConfigurePulseGenerators.output = False
# rszvb_SetInternalCombiner ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean internalCombiner']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'internalCombiner'),)
rszvb_SetInternalCombiner  = prototype(('rszvb_SetInternalCombiner', rszvbDLL), paramflags)
rszvb_SetInternalCombiner.name = 'rszvb_SetInternalCombiner'
rszvb_SetInternalCombiner.errcheck = __errorcheck__
rszvb_SetInternalCombiner.output = False
# rszvb_GetInternalCombiner ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* internalCombiner']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'internalCombiner'),)
rszvb_GetInternalCombiner  = prototype(('rszvb_GetInternalCombiner', rszvbDLL), paramflags)
rszvb_GetInternalCombiner.name = 'rszvb_GetInternalCombiner'
rszvb_GetInternalCombiner.errcheck = __errorcheck__
rszvb_GetInternalCombiner.output = True
# rszvb_SetHarmonicFilter ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean harmonicFilter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(1, 'harmonicFilter'),)
rszvb_SetHarmonicFilter  = prototype(('rszvb_SetHarmonicFilter', rszvbDLL), paramflags)
rszvb_SetHarmonicFilter.name = 'rszvb_SetHarmonicFilter'
rszvb_SetHarmonicFilter.errcheck = __errorcheck__
rszvb_SetHarmonicFilter.output = False
# rszvb_GetHarmonicFilter ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean* harmonicFilter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(2, 'harmonicFilter'),)
rszvb_GetHarmonicFilter  = prototype(('rszvb_GetHarmonicFilter', rszvbDLL), paramflags)
rszvb_GetHarmonicFilter.name = 'rszvb_GetHarmonicFilter'
rszvb_GetHarmonicFilter.errcheck = __errorcheck__
rszvb_GetHarmonicFilter.output = True
# rszvb_SetLNPreamplifier ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetLNPreamplifier  = prototype(('rszvb_SetLNPreamplifier', rszvbDLL), paramflags)
rszvb_SetLNPreamplifier.name = 'rszvb_SetLNPreamplifier'
rszvb_SetLNPreamplifier.errcheck = __errorcheck__
rszvb_SetLNPreamplifier.output = False
# rszvb_GetLNPreamplifier ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetLNPreamplifier  = prototype(('rszvb_GetLNPreamplifier', rszvbDLL), paramflags)
rszvb_GetLNPreamplifier.name = 'rszvb_GetLNPreamplifier'
rszvb_GetLNPreamplifier.errcheck = __errorcheck__
rszvb_GetLNPreamplifier.output = True
# rszvb_SetPulseModulator ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean pulseModulator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(1, 'pulseModulator'),)
rszvb_SetPulseModulator  = prototype(('rszvb_SetPulseModulator', rszvbDLL), paramflags)
rszvb_SetPulseModulator.name = 'rszvb_SetPulseModulator'
rszvb_SetPulseModulator.errcheck = __errorcheck__
rszvb_SetPulseModulator.output = False
# rszvb_GetPulseModulator ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean* pulseModulator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(2, 'pulseModulator'),)
rszvb_GetPulseModulator  = prototype(('rszvb_GetPulseModulator', rszvbDLL), paramflags)
rszvb_GetPulseModulator.name = 'rszvb_GetPulseModulator'
rszvb_GetPulseModulator.errcheck = __errorcheck__
rszvb_GetPulseModulator.output = True
# rszvb_SetExternalSignalGeneratorInput ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean extSignalGeneratorInput']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'extSignalGeneratorInput'),)
rszvb_SetExternalSignalGeneratorInput  = prototype(('rszvb_SetExternalSignalGeneratorInput', rszvbDLL), paramflags)
rszvb_SetExternalSignalGeneratorInput.name = 'rszvb_SetExternalSignalGeneratorInput'
rszvb_SetExternalSignalGeneratorInput.errcheck = __errorcheck__
rszvb_SetExternalSignalGeneratorInput.output = False
# rszvb_GetExternalSignalGeneratorInput ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* extSignalGeneratorInput']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'extSignalGeneratorInput'),)
rszvb_GetExternalSignalGeneratorInput  = prototype(('rszvb_GetExternalSignalGeneratorInput', rszvbDLL), paramflags)
rszvb_GetExternalSignalGeneratorInput.name = 'rszvb_GetExternalSignalGeneratorInput'
rszvb_GetExternalSignalGeneratorInput.errcheck = __errorcheck__
rszvb_GetExternalSignalGeneratorInput.output = True
# rszvb_SetPulseGeneratorAssignment ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 assignment']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'assignment'),)
rszvb_SetPulseGeneratorAssignment  = prototype(('rszvb_SetPulseGeneratorAssignment', rszvbDLL), paramflags)
rszvb_SetPulseGeneratorAssignment.name = 'rszvb_SetPulseGeneratorAssignment'
rszvb_SetPulseGeneratorAssignment.errcheck = __errorcheck__
rszvb_SetPulseGeneratorAssignment.output = False
# rszvb_GetPulseGeneratorAssignment ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* assignment']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'assignment'),)
rszvb_GetPulseGeneratorAssignment  = prototype(('rszvb_GetPulseGeneratorAssignment', rszvbDLL), paramflags)
rszvb_GetPulseGeneratorAssignment.name = 'rszvb_GetPulseGeneratorAssignment'
rszvb_GetPulseGeneratorAssignment.errcheck = __errorcheck__
rszvb_GetPulseGeneratorAssignment.output = True
# rszvb_SetExternalSignalGeneratorOutput ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean extSignalGeneratorOutput']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'extSignalGeneratorOutput'),)
rszvb_SetExternalSignalGeneratorOutput  = prototype(('rszvb_SetExternalSignalGeneratorOutput', rszvbDLL), paramflags)
rszvb_SetExternalSignalGeneratorOutput.name = 'rszvb_SetExternalSignalGeneratorOutput'
rszvb_SetExternalSignalGeneratorOutput.errcheck = __errorcheck__
rszvb_SetExternalSignalGeneratorOutput.output = False
# rszvb_GetExternalSignalGeneratorOutput ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* extSignalGeneratorOutput']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'extSignalGeneratorOutput'),)
rszvb_GetExternalSignalGeneratorOutput  = prototype(('rszvb_GetExternalSignalGeneratorOutput', rszvbDLL), paramflags)
rszvb_GetExternalSignalGeneratorOutput.name = 'rszvb_GetExternalSignalGeneratorOutput'
rszvb_GetExternalSignalGeneratorOutput.errcheck = __errorcheck__
rszvb_GetExternalSignalGeneratorOutput.output = True
# rszvb_SetTRMMeasureInput ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViInt32 input']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(1, 'input'),)
rszvb_SetTRMMeasureInput  = prototype(('rszvb_SetTRMMeasureInput', rszvbDLL), paramflags)
rszvb_SetTRMMeasureInput.name = 'rszvb_SetTRMMeasureInput'
rszvb_SetTRMMeasureInput.errcheck = __errorcheck__
rszvb_SetTRMMeasureInput.output = False
# rszvb_GetTRMMeasureInput ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViInt32* input']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(2, 'input'),)
rszvb_GetTRMMeasureInput  = prototype(('rszvb_GetTRMMeasureInput', rszvbDLL), paramflags)
rszvb_GetTRMMeasureInput.name = 'rszvb_GetTRMMeasureInput'
rszvb_GetTRMMeasureInput.errcheck = __errorcheck__
rszvb_GetTRMMeasureInput.output = True
# rszvb_SetTRMCombinerState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean combinerState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(1, 'combinerState'),)
rszvb_SetTRMCombinerState  = prototype(('rszvb_SetTRMCombinerState', rszvbDLL), paramflags)
rszvb_SetTRMCombinerState.name = 'rszvb_SetTRMCombinerState'
rszvb_SetTRMCombinerState.errcheck = __errorcheck__
rszvb_SetTRMCombinerState.output = False
# rszvb_GetTRMCombinerState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean* combinerState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(2, 'combinerState'),)
rszvb_GetTRMCombinerState  = prototype(('rszvb_GetTRMCombinerState', rszvbDLL), paramflags)
rszvb_GetTRMCombinerState.name = 'rszvb_GetTRMCombinerState'
rszvb_GetTRMCombinerState.errcheck = __errorcheck__
rszvb_GetTRMCombinerState.output = True
# rszvb_SetTRMPowerAmplifierState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean powerAmplifierState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(1, 'powerAmplifierState'),)
rszvb_SetTRMPowerAmplifierState  = prototype(('rszvb_SetTRMPowerAmplifierState', rszvbDLL), paramflags)
rszvb_SetTRMPowerAmplifierState.name = 'rszvb_SetTRMPowerAmplifierState'
rszvb_SetTRMPowerAmplifierState.errcheck = __errorcheck__
rszvb_SetTRMPowerAmplifierState.output = False
# rszvb_GetTRMPowerAmplifierState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean* powerAmplifierState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(2, 'powerAmplifierState'),)
rszvb_GetTRMPowerAmplifierState  = prototype(('rszvb_GetTRMPowerAmplifierState', rszvbDLL), paramflags)
rszvb_GetTRMPowerAmplifierState.name = 'rszvb_GetTRMPowerAmplifierState'
rszvb_GetTRMPowerAmplifierState.errcheck = __errorcheck__
rszvb_GetTRMPowerAmplifierState.output = True
# rszvb_SetTRMPulseModulatorState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean pulseModulatorState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(1, 'pulseModulatorState'),)
rszvb_SetTRMPulseModulatorState  = prototype(('rszvb_SetTRMPulseModulatorState', rszvbDLL), paramflags)
rszvb_SetTRMPulseModulatorState.name = 'rszvb_SetTRMPulseModulatorState'
rszvb_SetTRMPulseModulatorState.errcheck = __errorcheck__
rszvb_SetTRMPulseModulatorState.output = False
# rszvb_GetTRMPulseModulatorState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean* pulseModulatorState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(2, 'pulseModulatorState'),)
rszvb_GetTRMPulseModulatorState  = prototype(('rszvb_GetTRMPulseModulatorState', rszvbDLL), paramflags)
rszvb_GetTRMPulseModulatorState.name = 'rszvb_GetTRMPulseModulatorState'
rszvb_GetTRMPulseModulatorState.errcheck = __errorcheck__
rszvb_GetTRMPulseModulatorState.output = True
# rszvb_SetTRMUserSourcePathExtensionState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean userSourcePathExtension']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(1, 'userSourcePathExtension'),)
rszvb_SetTRMUserSourcePathExtensionState  = prototype(('rszvb_SetTRMUserSourcePathExtensionState', rszvbDLL), paramflags)
rszvb_SetTRMUserSourcePathExtensionState.name = 'rszvb_SetTRMUserSourcePathExtensionState'
rszvb_SetTRMUserSourcePathExtensionState.errcheck = __errorcheck__
rszvb_SetTRMUserSourcePathExtensionState.output = False
# rszvb_GetTRMUserSourcePathExtensionState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean* userSourcePathExtension']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(2, 'userSourcePathExtension'),)
rszvb_GetTRMUserSourcePathExtensionState  = prototype(('rszvb_GetTRMUserSourcePathExtensionState', rszvbDLL), paramflags)
rszvb_GetTRMUserSourcePathExtensionState.name = 'rszvb_GetTRMUserSourcePathExtensionState'
rszvb_GetTRMUserSourcePathExtensionState.errcheck = __errorcheck__
rszvb_GetTRMUserSourcePathExtensionState.output = True
# rszvb_SetTRMUserMeasurementPathExtensionState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean userMeasurementPathExtension']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(1, 'userMeasurementPathExtension'),)
rszvb_SetTRMUserMeasurementPathExtensionState  = prototype(('rszvb_SetTRMUserMeasurementPathExtensionState', rszvbDLL), paramflags)
rszvb_SetTRMUserMeasurementPathExtensionState.name = 'rszvb_SetTRMUserMeasurementPathExtensionState'
rszvb_SetTRMUserMeasurementPathExtensionState.errcheck = __errorcheck__
rszvb_SetTRMUserMeasurementPathExtensionState.output = False
# rszvb_GetTRMUserMeasurementPathExtensionState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViBoolean* userMeasurementPathExtension']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(2, 'userMeasurementPathExtension'),)
rszvb_GetTRMUserMeasurementPathExtensionState  = prototype(('rszvb_GetTRMUserMeasurementPathExtensionState', rszvbDLL), paramflags)
rszvb_GetTRMUserMeasurementPathExtensionState.name = 'rszvb_GetTRMUserMeasurementPathExtensionState'
rszvb_GetTRMUserMeasurementPathExtensionState.errcheck = __errorcheck__
rszvb_GetTRMUserMeasurementPathExtensionState.output = True
# rszvb_SetTRMPulseModulatorSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViInt32 pulseModulatorSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(1, 'pulseModulatorSource'),)
rszvb_SetTRMPulseModulatorSource  = prototype(('rszvb_SetTRMPulseModulatorSource', rszvbDLL), paramflags)
rszvb_SetTRMPulseModulatorSource.name = 'rszvb_SetTRMPulseModulatorSource'
rszvb_SetTRMPulseModulatorSource.errcheck = __errorcheck__
rszvb_SetTRMPulseModulatorSource.output = False
# rszvb_GetTRMPulseModulatorSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 path', 'ViInt32* pulseModulatorSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'path'),(2, 'pulseModulatorSource'),)
rszvb_GetTRMPulseModulatorSource  = prototype(('rszvb_GetTRMPulseModulatorSource', rszvbDLL), paramflags)
rszvb_GetTRMPulseModulatorSource.name = 'rszvb_GetTRMPulseModulatorSource'
rszvb_GetTRMPulseModulatorSource.errcheck = __errorcheck__
rszvb_GetTRMPulseModulatorSource.output = True
# rszvb_SetTRMPulseGeneratorSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 extOut', 'ViInt32 pulseGeneratorSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'extOut'),(1, 'pulseGeneratorSource'),)
rszvb_SetTRMPulseGeneratorSource  = prototype(('rszvb_SetTRMPulseGeneratorSource', rszvbDLL), paramflags)
rszvb_SetTRMPulseGeneratorSource.name = 'rszvb_SetTRMPulseGeneratorSource'
rszvb_SetTRMPulseGeneratorSource.errcheck = __errorcheck__
rszvb_SetTRMPulseGeneratorSource.output = False
# rszvb_GetTRMPulseGeneratorSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 extOut', 'ViInt32* pulseGeneratorSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'extOut'),(2, 'pulseGeneratorSource'),)
rszvb_GetTRMPulseGeneratorSource  = prototype(('rszvb_GetTRMPulseGeneratorSource', rszvbDLL), paramflags)
rszvb_GetTRMPulseGeneratorSource.name = 'rszvb_GetTRMPulseGeneratorSource'
rszvb_GetTRMPulseGeneratorSource.errcheck = __errorcheck__
rszvb_GetTRMPulseGeneratorSource.output = True
# rszvb_SetTRMPulseGeneratorInvertSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 extOut', 'ViBoolean invertSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'extOut'),(1, 'invertSource'),)
rszvb_SetTRMPulseGeneratorInvertSource  = prototype(('rszvb_SetTRMPulseGeneratorInvertSource', rszvbDLL), paramflags)
rszvb_SetTRMPulseGeneratorInvertSource.name = 'rszvb_SetTRMPulseGeneratorInvertSource'
rszvb_SetTRMPulseGeneratorInvertSource.errcheck = __errorcheck__
rszvb_SetTRMPulseGeneratorInvertSource.output = False
# rszvb_GetTRMPulseGeneratorInvertSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 extOut', 'ViBoolean* invertSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'extOut'),(2, 'invertSource'),)
rszvb_GetTRMPulseGeneratorInvertSource  = prototype(('rszvb_GetTRMPulseGeneratorInvertSource', rszvbDLL), paramflags)
rszvb_GetTRMPulseGeneratorInvertSource.name = 'rszvb_GetTRMPulseGeneratorInvertSource'
rszvb_GetTRMPulseGeneratorInvertSource.errcheck = __errorcheck__
rszvb_GetTRMPulseGeneratorInvertSource.output = True
# rszvb_GetTRMNumberOfUnits ['ViSession instrumentHandle', 'ViInt32* numberOfUnits']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'numberOfUnits'),)
rszvb_GetTRMNumberOfUnits  = prototype(('rszvb_GetTRMNumberOfUnits', rszvbDLL), paramflags)
rszvb_GetTRMNumberOfUnits.name = 'rszvb_GetTRMNumberOfUnits'
rszvb_GetTRMNumberOfUnits.errcheck = __errorcheck__
rszvb_GetTRMNumberOfUnits.output = True
# rszvb_GetTRMUnitDeviceID ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR deviceID[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'deviceID[]'),)
rszvb_GetTRMUnitDeviceID  = prototype(('rszvb_GetTRMUnitDeviceID', rszvbDLL), paramflags)
rszvb_GetTRMUnitDeviceID.name = 'rszvb_GetTRMUnitDeviceID'
rszvb_GetTRMUnitDeviceID.errcheck = __errorcheck__
rszvb_GetTRMUnitDeviceID.output = False
# rszvb_GetTRMUnitHardwareOptions ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR optionList[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'optionList[]'),)
rszvb_GetTRMUnitHardwareOptions  = prototype(('rszvb_GetTRMUnitHardwareOptions', rszvbDLL), paramflags)
rszvb_GetTRMUnitHardwareOptions.name = 'rszvb_GetTRMUnitHardwareOptions'
rszvb_GetTRMUnitHardwareOptions.errcheck = __errorcheck__
rszvb_GetTRMUnitHardwareOptions.output = False
# rszvb_ConfigureHarmonicMeasurement ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 harmonicMeasurement', 'ViBoolean relativeHarmonicMeasurement', 'ViInt32 source', 'ViInt32 harmonicMeasuredAt', 'ViInt32 harmonicOrder']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'harmonicMeasurement'),(1, 'relativeHarmonicMeasurement'),(1, 'source'),(1, 'harmonicMeasuredAt'),(1, 'harmonicOrder'),)
rszvb_ConfigureHarmonicMeasurement  = prototype(('rszvb_ConfigureHarmonicMeasurement', rszvbDLL), paramflags)
rszvb_ConfigureHarmonicMeasurement.name = 'rszvb_ConfigureHarmonicMeasurement'
rszvb_ConfigureHarmonicMeasurement.errcheck = __errorcheck__
rszvb_ConfigureHarmonicMeasurement.output = False
# rszvb_SetHarmonicMeasurementState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 harmonicMeasurement']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'harmonicMeasurement'),)
rszvb_SetHarmonicMeasurementState  = prototype(('rszvb_SetHarmonicMeasurementState', rszvbDLL), paramflags)
rszvb_SetHarmonicMeasurementState.name = 'rszvb_SetHarmonicMeasurementState'
rszvb_SetHarmonicMeasurementState.errcheck = __errorcheck__
rszvb_SetHarmonicMeasurementState.output = False
# rszvb_GetHarmonicMeasurementState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* harmonicMeasurement']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'harmonicMeasurement'),)
rszvb_GetHarmonicMeasurementState  = prototype(('rszvb_GetHarmonicMeasurementState', rszvbDLL), paramflags)
rszvb_GetHarmonicMeasurementState.name = 'rszvb_GetHarmonicMeasurementState'
rszvb_GetHarmonicMeasurementState.errcheck = __errorcheck__
rszvb_GetHarmonicMeasurementState.output = True
# rszvb_SetHarmonicOrder ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 harmonicOrder']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'harmonicOrder'),)
rszvb_SetHarmonicOrder  = prototype(('rszvb_SetHarmonicOrder', rszvbDLL), paramflags)
rszvb_SetHarmonicOrder.name = 'rszvb_SetHarmonicOrder'
rszvb_SetHarmonicOrder.errcheck = __errorcheck__
rszvb_SetHarmonicOrder.output = False
# rszvb_GetHarmonicOrder ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* harmonicOrder']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'harmonicOrder'),)
rszvb_GetHarmonicOrder  = prototype(('rszvb_GetHarmonicOrder', rszvbDLL), paramflags)
rszvb_GetHarmonicOrder.name = 'rszvb_GetHarmonicOrder'
rszvb_GetHarmonicOrder.errcheck = __errorcheck__
rszvb_GetHarmonicOrder.output = True
# rszvb_SetHarmonicSourcePort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),)
rszvb_SetHarmonicSourcePort  = prototype(('rszvb_SetHarmonicSourcePort', rszvbDLL), paramflags)
rszvb_SetHarmonicSourcePort.name = 'rszvb_SetHarmonicSourcePort'
rszvb_SetHarmonicSourcePort.errcheck = __errorcheck__
rszvb_SetHarmonicSourcePort.output = False
# rszvb_GetHarmonicSourcePort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* port']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'port'),)
rszvb_GetHarmonicSourcePort  = prototype(('rszvb_GetHarmonicSourcePort', rszvbDLL), paramflags)
rszvb_GetHarmonicSourcePort.name = 'rszvb_GetHarmonicSourcePort'
rszvb_GetHarmonicSourcePort.errcheck = __errorcheck__
rszvb_GetHarmonicSourcePort.output = True
# rszvb_SetHarmonicReceivePort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),)
rszvb_SetHarmonicReceivePort  = prototype(('rszvb_SetHarmonicReceivePort', rszvbDLL), paramflags)
rszvb_SetHarmonicReceivePort.name = 'rszvb_SetHarmonicReceivePort'
rszvb_SetHarmonicReceivePort.errcheck = __errorcheck__
rszvb_SetHarmonicReceivePort.output = False
# rszvb_GetHarmonicReceivePort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* port']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'port'),)
rszvb_GetHarmonicReceivePort  = prototype(('rszvb_GetHarmonicReceivePort', rszvbDLL), paramflags)
rszvb_GetHarmonicReceivePort.name = 'rszvb_GetHarmonicReceivePort'
rszvb_GetHarmonicReceivePort.errcheck = __errorcheck__
rszvb_GetHarmonicReceivePort.output = True
# rszvb_SetHarmonicRelativeState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean relativeHarmonicMeasurement']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'relativeHarmonicMeasurement'),)
rszvb_SetHarmonicRelativeState  = prototype(('rszvb_SetHarmonicRelativeState', rszvbDLL), paramflags)
rszvb_SetHarmonicRelativeState.name = 'rszvb_SetHarmonicRelativeState'
rszvb_SetHarmonicRelativeState.errcheck = __errorcheck__
rszvb_SetHarmonicRelativeState.output = False
# rszvb_GetHarmonicRelativeState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* relativeHarmonicMeasurement']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'relativeHarmonicMeasurement'),)
rszvb_GetHarmonicRelativeState  = prototype(('rszvb_GetHarmonicRelativeState', rszvbDLL), paramflags)
rszvb_GetHarmonicRelativeState.name = 'rszvb_GetHarmonicRelativeState'
rszvb_GetHarmonicRelativeState.errcheck = __errorcheck__
rszvb_GetHarmonicRelativeState.output = True
# rszvb_SetMixerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 mixerMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'mixerMode'),)
rszvb_SetMixerMode  = prototype(('rszvb_SetMixerMode', rszvbDLL), paramflags)
rszvb_SetMixerMode.name = 'rszvb_SetMixerMode'
rszvb_SetMixerMode.errcheck = __errorcheck__
rszvb_SetMixerMode.output = False
# rszvb_GetMixerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* mixerMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'mixerMode'),)
rszvb_GetMixerMode  = prototype(('rszvb_GetMixerMode', rszvbDLL), paramflags)
rszvb_GetMixerMode.name = 'rszvb_GetMixerMode'
rszvb_GetMixerMode.errcheck = __errorcheck__
rszvb_GetMixerMode.output = True
# rszvb_SetNumberOfStages ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 numberOfStages']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'numberOfStages'),)
rszvb_SetNumberOfStages  = prototype(('rszvb_SetNumberOfStages', rszvbDLL), paramflags)
rszvb_SetNumberOfStages.name = 'rszvb_SetNumberOfStages'
rszvb_SetNumberOfStages.errcheck = __errorcheck__
rszvb_SetNumberOfStages.output = False
# rszvb_GetNumberOfStages ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* numberOfStages']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'numberOfStages'),)
rszvb_GetNumberOfStages  = prototype(('rszvb_GetNumberOfStages', rszvbDLL), paramflags)
rszvb_GetNumberOfStages.name = 'rszvb_GetNumberOfStages'
rszvb_GetNumberOfStages.errcheck = __errorcheck__
rszvb_GetNumberOfStages.output = True
# rszvb_SetSignalSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 stage', 'ViInt32 source', 'ViInt32 portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'stage'),(1, 'source'),(1, 'portNumber'),)
rszvb_SetSignalSource  = prototype(('rszvb_SetSignalSource', rszvbDLL), paramflags)
rszvb_SetSignalSource.name = 'rszvb_SetSignalSource'
rszvb_SetSignalSource.errcheck = __errorcheck__
rszvb_SetSignalSource.output = False
# rszvb_GetSignalSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 stage', 'ViInt32* source', 'ViInt32* portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'stage'),(2, 'source'),(2, 'portNumber'),)
rszvb_GetSignalSource  = prototype(('rszvb_GetSignalSource', rszvbDLL), paramflags)
rszvb_GetSignalSource.name = 'rszvb_GetSignalSource'
rszvb_GetSignalSource.errcheck = __errorcheck__
rszvb_GetSignalSource.output = True
# rszvb_SetIFSignalPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),)
rszvb_SetIFSignalPort  = prototype(('rszvb_SetIFSignalPort', rszvbDLL), paramflags)
rszvb_SetIFSignalPort.name = 'rszvb_SetIFSignalPort'
rszvb_SetIFSignalPort.errcheck = __errorcheck__
rszvb_SetIFSignalPort.output = False
# rszvb_GetIFSignalPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'portNumber'),)
rszvb_GetIFSignalPort  = prototype(('rszvb_GetIFSignalPort', rszvbDLL), paramflags)
rszvb_GetIFSignalPort.name = 'rszvb_GetIFSignalPort'
rszvb_GetIFSignalPort.errcheck = __errorcheck__
rszvb_GetIFSignalPort.output = True
# rszvb_SetRFSignalPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),)
rszvb_SetRFSignalPort  = prototype(('rszvb_SetRFSignalPort', rszvbDLL), paramflags)
rszvb_SetRFSignalPort.name = 'rszvb_SetRFSignalPort'
rszvb_SetRFSignalPort.errcheck = __errorcheck__
rszvb_SetRFSignalPort.output = False
# rszvb_GetRFSignalPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'portNumber'),)
rszvb_GetRFSignalPort  = prototype(('rszvb_GetRFSignalPort', rszvbDLL), paramflags)
rszvb_GetRFSignalPort.name = 'rszvb_GetRFSignalPort'
rszvb_GetRFSignalPort.errcheck = __errorcheck__
rszvb_GetRFSignalPort.output = True
# rszvb_SetInternalSignalSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 internalSignalSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'internalSignalSource'),)
rszvb_SetInternalSignalSource  = prototype(('rszvb_SetInternalSignalSource', rszvbDLL), paramflags)
rszvb_SetInternalSignalSource.name = 'rszvb_SetInternalSignalSource'
rszvb_SetInternalSignalSource.errcheck = __errorcheck__
rszvb_SetInternalSignalSource.output = False
# rszvb_GetInternalSignalSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* internalSignalSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'internalSignalSource'),)
rszvb_GetInternalSignalSource  = prototype(('rszvb_GetInternalSignalSource', rszvbDLL), paramflags)
rszvb_GetInternalSignalSource.name = 'rszvb_GetInternalSignalSource'
rszvb_GetInternalSignalSource.errcheck = __errorcheck__
rszvb_GetInternalSignalSource.output = True
# rszvb_SetExternalSignalSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 externalSignalSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'externalSignalSource'),)
rszvb_SetExternalSignalSource  = prototype(('rszvb_SetExternalSignalSource', rszvbDLL), paramflags)
rszvb_SetExternalSignalSource.name = 'rszvb_SetExternalSignalSource'
rszvb_SetExternalSignalSource.errcheck = __errorcheck__
rszvb_SetExternalSignalSource.output = False
# rszvb_GetExternalSignalSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* externalSignalSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'externalSignalSource'),)
rszvb_GetExternalSignalSource  = prototype(('rszvb_GetExternalSignalSource', rszvbDLL), paramflags)
rszvb_GetExternalSignalSource.name = 'rszvb_GetExternalSignalSource'
rszvb_GetExternalSignalSource.errcheck = __errorcheck__
rszvb_GetExternalSignalSource.output = True
# rszvb_ConfigurePowerSettings ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 fundamentalPower', 'ViReal64 fixedPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fundamentalPower'),(1, 'fixedPower'),)
rszvb_ConfigurePowerSettings  = prototype(('rszvb_ConfigurePowerSettings', rszvbDLL), paramflags)
rszvb_ConfigurePowerSettings.name = 'rszvb_ConfigurePowerSettings'
rszvb_ConfigurePowerSettings.errcheck = __errorcheck__
rszvb_ConfigurePowerSettings.output = False
# rszvb_SetFundamentalPowerSignal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 fundamentalPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fundamentalPower'),)
rszvb_SetFundamentalPowerSignal  = prototype(('rszvb_SetFundamentalPowerSignal', rszvbDLL), paramflags)
rszvb_SetFundamentalPowerSignal.name = 'rszvb_SetFundamentalPowerSignal'
rszvb_SetFundamentalPowerSignal.errcheck = __errorcheck__
rszvb_SetFundamentalPowerSignal.output = False
# rszvb_GetFundamentalPowerSignal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* fundamentalPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'fundamentalPower'),)
rszvb_GetFundamentalPowerSignal  = prototype(('rszvb_GetFundamentalPowerSignal', rszvbDLL), paramflags)
rszvb_GetFundamentalPowerSignal.name = 'rszvb_GetFundamentalPowerSignal'
rszvb_GetFundamentalPowerSignal.errcheck = __errorcheck__
rszvb_GetFundamentalPowerSignal.output = True
# rszvb_SetFixedPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 fixedPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fixedPower'),)
rszvb_SetFixedPower  = prototype(('rszvb_SetFixedPower', rszvbDLL), paramflags)
rszvb_SetFixedPower.name = 'rszvb_SetFixedPower'
rszvb_SetFixedPower.errcheck = __errorcheck__
rszvb_SetFixedPower.output = False
# rszvb_GetFixedPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* fixedPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'fixedPower'),)
rszvb_GetFixedPower  = prototype(('rszvb_GetFixedPower', rszvbDLL), paramflags)
rszvb_GetFixedPower.name = 'rszvb_GetFixedPower'
rszvb_GetFixedPower.errcheck = __errorcheck__
rszvb_GetFixedPower.output = True
# rszvb_SetFixedPowerToSignal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 signal', 'ViReal64 fixedPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'signal'),(1, 'fixedPower'),)
rszvb_SetFixedPowerToSignal  = prototype(('rszvb_SetFixedPowerToSignal', rszvbDLL), paramflags)
rszvb_SetFixedPowerToSignal.name = 'rszvb_SetFixedPowerToSignal'
rszvb_SetFixedPowerToSignal.errcheck = __errorcheck__
rszvb_SetFixedPowerToSignal.output = False
# rszvb_GetFixedPowerToSignal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 signal', 'ViReal64* fixedPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'signal'),(2, 'fixedPower'),)
rszvb_GetFixedPowerToSignal  = prototype(('rszvb_GetFixedPowerToSignal', rszvbDLL), paramflags)
rszvb_GetFixedPowerToSignal.name = 'rszvb_GetFixedPowerToSignal'
rszvb_GetFixedPowerToSignal.errcheck = __errorcheck__
rszvb_GetFixedPowerToSignal.output = True
# rszvb_SetSignalPowerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 signal', 'ViInt32 mode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'signal'),(1, 'mode'),)
rszvb_SetSignalPowerMode  = prototype(('rszvb_SetSignalPowerMode', rszvbDLL), paramflags)
rszvb_SetSignalPowerMode.name = 'rszvb_SetSignalPowerMode'
rszvb_SetSignalPowerMode.errcheck = __errorcheck__
rszvb_SetSignalPowerMode.output = False
# rszvb_GetSignalPowerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 signal', 'ViInt32* mode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'signal'),(2, 'mode'),)
rszvb_GetSignalPowerMode  = prototype(('rszvb_GetSignalPowerMode', rszvbDLL), paramflags)
rszvb_GetSignalPowerMode.name = 'rszvb_GetSignalPowerMode'
rszvb_GetSignalPowerMode.errcheck = __errorcheck__
rszvb_GetSignalPowerMode.output = True
# rszvb_ConfigureFrequencySettings ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 fundamentalFrequencySignal', 'ViInt32 fixedFrequencySignal', 'ViReal64 fixedFrequency', 'ViInt32 frequencyConversionMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_double,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fundamentalFrequencySignal'),(1, 'fixedFrequencySignal'),(1, 'fixedFrequency'),(1, 'frequencyConversionMode'),)
rszvb_ConfigureFrequencySettings  = prototype(('rszvb_ConfigureFrequencySettings', rszvbDLL), paramflags)
rszvb_ConfigureFrequencySettings.name = 'rszvb_ConfigureFrequencySettings'
rszvb_ConfigureFrequencySettings.errcheck = __errorcheck__
rszvb_ConfigureFrequencySettings.output = False
# rszvb_SetFundamentalFrequencySignal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 fundamentalFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fundamentalFrequency'),)
rszvb_SetFundamentalFrequencySignal  = prototype(('rszvb_SetFundamentalFrequencySignal', rszvbDLL), paramflags)
rszvb_SetFundamentalFrequencySignal.name = 'rszvb_SetFundamentalFrequencySignal'
rszvb_SetFundamentalFrequencySignal.errcheck = __errorcheck__
rszvb_SetFundamentalFrequencySignal.output = False
# rszvb_GetFundamentalFrequencySignal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* fundamentalFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'fundamentalFrequency'),)
rszvb_GetFundamentalFrequencySignal  = prototype(('rszvb_GetFundamentalFrequencySignal', rszvbDLL), paramflags)
rszvb_GetFundamentalFrequencySignal.name = 'rszvb_GetFundamentalFrequencySignal'
rszvb_GetFundamentalFrequencySignal.errcheck = __errorcheck__
rszvb_GetFundamentalFrequencySignal.output = True
# rszvb_SetFixedFrequencySignal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 fixedFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fixedFrequency'),)
rszvb_SetFixedFrequencySignal  = prototype(('rszvb_SetFixedFrequencySignal', rszvbDLL), paramflags)
rszvb_SetFixedFrequencySignal.name = 'rszvb_SetFixedFrequencySignal'
rszvb_SetFixedFrequencySignal.errcheck = __errorcheck__
rszvb_SetFixedFrequencySignal.output = False
# rszvb_GetFixedFrequencySignal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* fixedFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'fixedFrequency'),)
rszvb_GetFixedFrequencySignal  = prototype(('rszvb_GetFixedFrequencySignal', rszvbDLL), paramflags)
rszvb_GetFixedFrequencySignal.name = 'rszvb_GetFixedFrequencySignal'
rszvb_GetFixedFrequencySignal.errcheck = __errorcheck__
rszvb_GetFixedFrequencySignal.output = True
# rszvb_SetFixedFrequencySignalStage2 ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 fixedFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fixedFrequency'),)
rszvb_SetFixedFrequencySignalStage2  = prototype(('rszvb_SetFixedFrequencySignalStage2', rszvbDLL), paramflags)
rszvb_SetFixedFrequencySignalStage2.name = 'rszvb_SetFixedFrequencySignalStage2'
rszvb_SetFixedFrequencySignalStage2.errcheck = __errorcheck__
rszvb_SetFixedFrequencySignalStage2.output = False
# rszvb_GetFixedFrequencySignalStage2 ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* fixedFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'fixedFrequency'),)
rszvb_GetFixedFrequencySignalStage2  = prototype(('rszvb_GetFixedFrequencySignalStage2', rszvbDLL), paramflags)
rszvb_GetFixedFrequencySignalStage2.name = 'rszvb_GetFixedFrequencySignalStage2'
rszvb_GetFixedFrequencySignalStage2.errcheck = __errorcheck__
rszvb_GetFixedFrequencySignalStage2.output = True
# rszvb_SetFixedFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 fixedFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fixedFrequency'),)
rszvb_SetFixedFrequency  = prototype(('rszvb_SetFixedFrequency', rszvbDLL), paramflags)
rszvb_SetFixedFrequency.name = 'rszvb_SetFixedFrequency'
rszvb_SetFixedFrequency.errcheck = __errorcheck__
rszvb_SetFixedFrequency.output = False
# rszvb_GetFixedFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* fixedFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'fixedFrequency'),)
rszvb_GetFixedFrequency  = prototype(('rszvb_GetFixedFrequency', rszvbDLL), paramflags)
rszvb_GetFixedFrequency.name = 'rszvb_GetFixedFrequency'
rszvb_GetFixedFrequency.errcheck = __errorcheck__
rszvb_GetFixedFrequency.output = True
# rszvb_SetFixedFrequencyToSignal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 signal', 'ViReal64 fixedFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'signal'),(1, 'fixedFrequency'),)
rszvb_SetFixedFrequencyToSignal  = prototype(('rszvb_SetFixedFrequencyToSignal', rszvbDLL), paramflags)
rszvb_SetFixedFrequencyToSignal.name = 'rszvb_SetFixedFrequencyToSignal'
rszvb_SetFixedFrequencyToSignal.errcheck = __errorcheck__
rszvb_SetFixedFrequencyToSignal.output = False
# rszvb_GetFixedFrequencyToSignal ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 signal', 'ViReal64* fixedFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'signal'),(2, 'fixedFrequency'),)
rszvb_GetFixedFrequencyToSignal  = prototype(('rszvb_GetFixedFrequencyToSignal', rszvbDLL), paramflags)
rszvb_GetFixedFrequencyToSignal.name = 'rszvb_GetFixedFrequencyToSignal'
rszvb_GetFixedFrequencyToSignal.errcheck = __errorcheck__
rszvb_GetFixedFrequencyToSignal.output = True
# rszvb_SetFrequencyConversionMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 frequencyConversionMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'frequencyConversionMode'),)
rszvb_SetFrequencyConversionMode  = prototype(('rszvb_SetFrequencyConversionMode', rszvbDLL), paramflags)
rszvb_SetFrequencyConversionMode.name = 'rszvb_SetFrequencyConversionMode'
rszvb_SetFrequencyConversionMode.errcheck = __errorcheck__
rszvb_SetFrequencyConversionMode.output = False
# rszvb_GetFrequencyConversionMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* frequencyConversionMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'frequencyConversionMode'),)
rszvb_GetFrequencyConversionMode  = prototype(('rszvb_GetFrequencyConversionMode', rszvbDLL), paramflags)
rszvb_GetFrequencyConversionMode.name = 'rszvb_GetFrequencyConversionMode'
rszvb_GetFrequencyConversionMode.errcheck = __errorcheck__
rszvb_GetFrequencyConversionMode.output = True
# rszvb_SetFrequencyConversionModeStage2 ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 frequencyConversionMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'frequencyConversionMode'),)
rszvb_SetFrequencyConversionModeStage2  = prototype(('rszvb_SetFrequencyConversionModeStage2', rszvbDLL), paramflags)
rszvb_SetFrequencyConversionModeStage2.name = 'rszvb_SetFrequencyConversionModeStage2'
rszvb_SetFrequencyConversionModeStage2.errcheck = __errorcheck__
rszvb_SetFrequencyConversionModeStage2.output = False
# rszvb_GetFrequencyConversionModeStage2 ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* frequencyConversionMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'frequencyConversionMode'),)
rszvb_GetFrequencyConversionModeStage2  = prototype(('rszvb_GetFrequencyConversionModeStage2', rszvbDLL), paramflags)
rszvb_GetFrequencyConversionModeStage2.name = 'rszvb_GetFrequencyConversionModeStage2'
rszvb_GetFrequencyConversionModeStage2.errcheck = __errorcheck__
rszvb_GetFrequencyConversionModeStage2.output = True
# rszvb_SetFrequencyHighAccuracy ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean highAccuracy']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'highAccuracy'),)
rszvb_SetFrequencyHighAccuracy  = prototype(('rszvb_SetFrequencyHighAccuracy', rszvbDLL), paramflags)
rszvb_SetFrequencyHighAccuracy.name = 'rszvb_SetFrequencyHighAccuracy'
rszvb_SetFrequencyHighAccuracy.errcheck = __errorcheck__
rszvb_SetFrequencyHighAccuracy.output = False
# rszvb_GetFrequencyHighAccuracy ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* highAccuracy']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'highAccuracy'),)
rszvb_GetFrequencyHighAccuracy  = prototype(('rszvb_GetFrequencyHighAccuracy', rszvbDLL), paramflags)
rszvb_GetFrequencyHighAccuracy.name = 'rszvb_GetFrequencyHighAccuracy'
rszvb_GetFrequencyHighAccuracy.errcheck = __errorcheck__
rszvb_GetFrequencyHighAccuracy.output = True
# rszvb_SetFrequencyLOConversionFactor ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 stage', 'ViInt32 numerator', 'ViInt32 denominator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'stage'),(1, 'numerator'),(1, 'denominator'),)
rszvb_SetFrequencyLOConversionFactor  = prototype(('rszvb_SetFrequencyLOConversionFactor', rszvbDLL), paramflags)
rszvb_SetFrequencyLOConversionFactor.name = 'rszvb_SetFrequencyLOConversionFactor'
rszvb_SetFrequencyLOConversionFactor.errcheck = __errorcheck__
rszvb_SetFrequencyLOConversionFactor.output = False
# rszvb_GetFrequencyLOConversionFactor ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 stage', 'ViInt32* numerator', 'ViInt32* denominator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'stage'),(2, 'numerator'),(2, 'denominator'),)
rszvb_GetFrequencyLOConversionFactor  = prototype(('rszvb_GetFrequencyLOConversionFactor', rszvbDLL), paramflags)
rszvb_GetFrequencyLOConversionFactor.name = 'rszvb_GetFrequencyLOConversionFactor'
rszvb_GetFrequencyLOConversionFactor.errcheck = __errorcheck__
rszvb_GetFrequencyLOConversionFactor.output = True
# rszvb_SetFrequencyRFConversionFactor ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 numerator', 'ViInt32 denominator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'numerator'),(1, 'denominator'),)
rszvb_SetFrequencyRFConversionFactor  = prototype(('rszvb_SetFrequencyRFConversionFactor', rszvbDLL), paramflags)
rszvb_SetFrequencyRFConversionFactor.name = 'rszvb_SetFrequencyRFConversionFactor'
rszvb_SetFrequencyRFConversionFactor.errcheck = __errorcheck__
rszvb_SetFrequencyRFConversionFactor.output = False
# rszvb_GetFrequencyRFConversionFactor ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* numerator', 'ViInt32* denominator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'numerator'),(2, 'denominator'),)
rszvb_GetFrequencyRFConversionFactor  = prototype(('rszvb_GetFrequencyRFConversionFactor', rszvbDLL), paramflags)
rszvb_GetFrequencyRFConversionFactor.name = 'rszvb_GetFrequencyRFConversionFactor'
rszvb_GetFrequencyRFConversionFactor.errcheck = __errorcheck__
rszvb_GetFrequencyRFConversionFactor.output = True
# rszvb_SetRFImageFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean RFImageFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'RFImageFrequency'),)
rszvb_SetRFImageFrequency  = prototype(('rszvb_SetRFImageFrequency', rszvbDLL), paramflags)
rszvb_SetRFImageFrequency.name = 'rszvb_SetRFImageFrequency'
rszvb_SetRFImageFrequency.errcheck = __errorcheck__
rszvb_SetRFImageFrequency.output = False
# rszvb_GetRFImageFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* RFImageFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'RFImageFrequency'),)
rszvb_GetRFImageFrequency  = prototype(('rszvb_GetRFImageFrequency', rszvbDLL), paramflags)
rszvb_GetRFImageFrequency.name = 'rszvb_GetRFImageFrequency'
rszvb_GetRFImageFrequency.errcheck = __errorcheck__
rszvb_GetRFImageFrequency.output = True
# rszvb_SetExternalPowerMeter ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 numberOfExternalPowerMeter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'numberOfExternalPowerMeter'),)
rszvb_SetExternalPowerMeter  = prototype(('rszvb_SetExternalPowerMeter', rszvbDLL), paramflags)
rszvb_SetExternalPowerMeter.name = 'rszvb_SetExternalPowerMeter'
rszvb_SetExternalPowerMeter.errcheck = __errorcheck__
rszvb_SetExternalPowerMeter.output = False
# rszvb_GetExternalPowerMeter ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* numberOfExternalPowerMeter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'numberOfExternalPowerMeter'),)
rszvb_GetExternalPowerMeter  = prototype(('rszvb_GetExternalPowerMeter', rszvbDLL), paramflags)
rszvb_GetExternalPowerMeter.name = 'rszvb_GetExternalPowerMeter'
rszvb_GetExternalPowerMeter.errcheck = __errorcheck__
rszvb_GetExternalPowerMeter.output = True
# rszvb_RFSourceCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_RFSourceCalibration  = prototype(('rszvb_RFSourceCalibration', rszvbDLL), paramflags)
rszvb_RFSourceCalibration.name = 'rszvb_RFSourceCalibration'
rszvb_RFSourceCalibration.errcheck = __errorcheck__
rszvb_RFSourceCalibration.output = False
# rszvb_IFReceiverCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_IFReceiverCalibration  = prototype(('rszvb_IFReceiverCalibration', rszvbDLL), paramflags)
rszvb_IFReceiverCalibration.name = 'rszvb_IFReceiverCalibration'
rszvb_IFReceiverCalibration.errcheck = __errorcheck__
rszvb_IFReceiverCalibration.output = False
# rszvb_LOSourceCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_LOSourceCalibration  = prototype(('rszvb_LOSourceCalibration', rszvbDLL), paramflags)
rszvb_LOSourceCalibration.name = 'rszvb_LOSourceCalibration'
rszvb_LOSourceCalibration.errcheck = __errorcheck__
rszvb_LOSourceCalibration.output = False
# rszvb_LOSourceCalibrationStage2 ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_LOSourceCalibrationStage2  = prototype(('rszvb_LOSourceCalibrationStage2', rszvbDLL), paramflags)
rszvb_LOSourceCalibrationStage2.name = 'rszvb_LOSourceCalibrationStage2'
rszvb_LOSourceCalibrationStage2.errcheck = __errorcheck__
rszvb_LOSourceCalibrationStage2.output = False
# rszvb_SetMixerDelayMeasurementSetup ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 measurementSetup']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'measurementSetup'),)
rszvb_SetMixerDelayMeasurementSetup  = prototype(('rszvb_SetMixerDelayMeasurementSetup', rszvbDLL), paramflags)
rszvb_SetMixerDelayMeasurementSetup.name = 'rszvb_SetMixerDelayMeasurementSetup'
rszvb_SetMixerDelayMeasurementSetup.errcheck = __errorcheck__
rszvb_SetMixerDelayMeasurementSetup.output = False
# rszvb_GetMixerDelayMeasurementSetup ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* measurementSetup']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'measurementSetup'),)
rszvb_GetMixerDelayMeasurementSetup  = prototype(('rszvb_GetMixerDelayMeasurementSetup', rszvbDLL), paramflags)
rszvb_GetMixerDelayMeasurementSetup.name = 'rszvb_GetMixerDelayMeasurementSetup'
rszvb_GetMixerDelayMeasurementSetup.errcheck = __errorcheck__
rszvb_GetMixerDelayMeasurementSetup.output = True
# rszvb_SetMixerDelayLANConnection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 LANConnection']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'LANConnection'),)
rszvb_SetMixerDelayLANConnection  = prototype(('rszvb_SetMixerDelayLANConnection', rszvbDLL), paramflags)
rszvb_SetMixerDelayLANConnection.name = 'rszvb_SetMixerDelayLANConnection'
rszvb_SetMixerDelayLANConnection.errcheck = __errorcheck__
rszvb_SetMixerDelayLANConnection.output = False
# rszvb_GetMixerDelayLANConnection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* LANConnection']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'LANConnection'),)
rszvb_GetMixerDelayLANConnection  = prototype(('rszvb_GetMixerDelayLANConnection', rszvbDLL), paramflags)
rszvb_GetMixerDelayLANConnection.name = 'rszvb_GetMixerDelayLANConnection'
rszvb_GetMixerDelayLANConnection.errcheck = __errorcheck__
rszvb_GetMixerDelayLANConnection.output = True
# rszvb_DefineMixerDelayReceiver ['ViSession instrumentHandle', 'ViString measurementSetup']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'measurementSetup'),)
rszvb_DefineMixerDelayReceiver  = prototype(('rszvb_DefineMixerDelayReceiver', rszvbDLL), paramflags)
rszvb_DefineMixerDelayReceiver.name = 'rszvb_DefineMixerDelayReceiver'
rszvb_DefineMixerDelayReceiver.errcheck = __errorcheck__
rszvb_DefineMixerDelayReceiver.output = False
# rszvb_ClearMixerDelayReceiverList ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_ClearMixerDelayReceiverList  = prototype(('rszvb_ClearMixerDelayReceiverList', rszvbDLL), paramflags)
rszvb_ClearMixerDelayReceiverList.name = 'rszvb_ClearMixerDelayReceiverList'
rszvb_ClearMixerDelayReceiverList.errcheck = __errorcheck__
rszvb_ClearMixerDelayReceiverList.output = False
# rszvb_StartMixerDelayCalibrationSweep ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_StartMixerDelayCalibrationSweep  = prototype(('rszvb_StartMixerDelayCalibrationSweep', rszvbDLL), paramflags)
rszvb_StartMixerDelayCalibrationSweep.name = 'rszvb_StartMixerDelayCalibrationSweep'
rszvb_StartMixerDelayCalibrationSweep.errcheck = __errorcheck__
rszvb_StartMixerDelayCalibrationSweep.output = False
# rszvb_SetMixerDelayAperture ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 aperture']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'aperture'),)
rszvb_SetMixerDelayAperture  = prototype(('rszvb_SetMixerDelayAperture', rszvbDLL), paramflags)
rszvb_SetMixerDelayAperture.name = 'rszvb_SetMixerDelayAperture'
rszvb_SetMixerDelayAperture.errcheck = __errorcheck__
rszvb_SetMixerDelayAperture.output = False
# rszvb_GetMixerDelayAperture ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* aperture']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'aperture'),)
rszvb_GetMixerDelayAperture  = prototype(('rszvb_GetMixerDelayAperture', rszvbDLL), paramflags)
rszvb_GetMixerDelayAperture.name = 'rszvb_GetMixerDelayAperture'
rszvb_GetMixerDelayAperture.errcheck = __errorcheck__
rszvb_GetMixerDelayAperture.output = True
# rszvb_SetMixerDelayConstant ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 constantDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'constantDelay'),)
rszvb_SetMixerDelayConstant  = prototype(('rszvb_SetMixerDelayConstant', rszvbDLL), paramflags)
rszvb_SetMixerDelayConstant.name = 'rszvb_SetMixerDelayConstant'
rszvb_SetMixerDelayConstant.errcheck = __errorcheck__
rszvb_SetMixerDelayConstant.output = False
# rszvb_GetMixerDelayConstant ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* constantDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'constantDelay'),)
rszvb_GetMixerDelayConstant  = prototype(('rszvb_GetMixerDelayConstant', rszvbDLL), paramflags)
rszvb_GetMixerDelayConstant.name = 'rszvb_GetMixerDelayConstant'
rszvb_GetMixerDelayConstant.errcheck = __errorcheck__
rszvb_GetMixerDelayConstant.output = True
# rszvb_SetMixerDelayCombinerState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean internalCombiner']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'internalCombiner'),)
rszvb_SetMixerDelayCombinerState  = prototype(('rszvb_SetMixerDelayCombinerState', rszvbDLL), paramflags)
rszvb_SetMixerDelayCombinerState.name = 'rszvb_SetMixerDelayCombinerState'
rszvb_SetMixerDelayCombinerState.errcheck = __errorcheck__
rszvb_SetMixerDelayCombinerState.output = False
# rszvb_GetMixerDelayCombinerState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* internalCombiner']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'internalCombiner'),)
rszvb_GetMixerDelayCombinerState  = prototype(('rszvb_GetMixerDelayCombinerState', rszvbDLL), paramflags)
rszvb_GetMixerDelayCombinerState.name = 'rszvb_GetMixerDelayCombinerState'
rszvb_GetMixerDelayCombinerState.errcheck = __errorcheck__
rszvb_GetMixerDelayCombinerState.output = True
# rszvb_SetMixerDelayDivisionByTwoEnabled ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean divisionByTwo']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'divisionByTwo'),)
rszvb_SetMixerDelayDivisionByTwoEnabled  = prototype(('rszvb_SetMixerDelayDivisionByTwoEnabled', rszvbDLL), paramflags)
rszvb_SetMixerDelayDivisionByTwoEnabled.name = 'rszvb_SetMixerDelayDivisionByTwoEnabled'
rszvb_SetMixerDelayDivisionByTwoEnabled.errcheck = __errorcheck__
rszvb_SetMixerDelayDivisionByTwoEnabled.output = False
# rszvb_GetMixerDelayDivisionByTwoEnabled ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* divisionByTwo']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'divisionByTwo'),)
rszvb_GetMixerDelayDivisionByTwoEnabled  = prototype(('rszvb_GetMixerDelayDivisionByTwoEnabled', rszvbDLL), paramflags)
rszvb_GetMixerDelayDivisionByTwoEnabled.name = 'rszvb_GetMixerDelayDivisionByTwoEnabled'
rszvb_GetMixerDelayDivisionByTwoEnabled.errcheck = __errorcheck__
rszvb_GetMixerDelayDivisionByTwoEnabled.output = True
# rszvb_SetMixerConstantDelayEnabled ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean constantDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'constantDelay'),)
rszvb_SetMixerConstantDelayEnabled  = prototype(('rszvb_SetMixerConstantDelayEnabled', rszvbDLL), paramflags)
rszvb_SetMixerConstantDelayEnabled.name = 'rszvb_SetMixerConstantDelayEnabled'
rszvb_SetMixerConstantDelayEnabled.errcheck = __errorcheck__
rszvb_SetMixerConstantDelayEnabled.output = False
# rszvb_GetMixerConstantDelayEnabled ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* constantDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'constantDelay'),)
rszvb_GetMixerConstantDelayEnabled  = prototype(('rszvb_GetMixerConstantDelayEnabled', rszvbDLL), paramflags)
rszvb_GetMixerConstantDelayEnabled.name = 'rszvb_GetMixerConstantDelayEnabled'
rszvb_GetMixerConstantDelayEnabled.errcheck = __errorcheck__
rszvb_GetMixerConstantDelayEnabled.output = True
# rszvb_SetMixerDelayCorrection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean correction']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'correction'),)
rszvb_SetMixerDelayCorrection  = prototype(('rszvb_SetMixerDelayCorrection', rszvbDLL), paramflags)
rszvb_SetMixerDelayCorrection.name = 'rszvb_SetMixerDelayCorrection'
rszvb_SetMixerDelayCorrection.errcheck = __errorcheck__
rszvb_SetMixerDelayCorrection.output = False
# rszvb_GetMixerDelayCorrection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* correction']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'correction'),)
rszvb_GetMixerDelayCorrection  = prototype(('rszvb_GetMixerDelayCorrection', rszvbDLL), paramflags)
rszvb_GetMixerDelayCorrection.name = 'rszvb_GetMixerDelayCorrection'
rszvb_GetMixerDelayCorrection.errcheck = __errorcheck__
rszvb_GetMixerDelayCorrection.output = True
# rszvb_SetMixerDelayUpperToneSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 source', 'ViInt32 portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'source'),(1, 'portNumber'),)
rszvb_SetMixerDelayUpperToneSource  = prototype(('rszvb_SetMixerDelayUpperToneSource', rszvbDLL), paramflags)
rszvb_SetMixerDelayUpperToneSource.name = 'rszvb_SetMixerDelayUpperToneSource'
rszvb_SetMixerDelayUpperToneSource.errcheck = __errorcheck__
rszvb_SetMixerDelayUpperToneSource.output = False
# rszvb_GetMixerDelayUpperToneSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* source', 'ViInt32* portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'source'),(2, 'portNumber'),)
rszvb_GetMixerDelayUpperToneSource  = prototype(('rszvb_GetMixerDelayUpperToneSource', rszvbDLL), paramflags)
rszvb_GetMixerDelayUpperToneSource.name = 'rszvb_GetMixerDelayUpperToneSource'
rszvb_GetMixerDelayUpperToneSource.errcheck = __errorcheck__
rszvb_GetMixerDelayUpperToneSource.output = True
# rszvb_LoadMixerDelayValues ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 type', 'ViString file']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'type'),(1, 'file'),)
rszvb_LoadMixerDelayValues  = prototype(('rszvb_LoadMixerDelayValues', rszvbDLL), paramflags)
rszvb_LoadMixerDelayValues.name = 'rszvb_LoadMixerDelayValues'
rszvb_LoadMixerDelayValues.errcheck = __errorcheck__
rszvb_LoadMixerDelayValues.output = False
# rszvb_LoadMixerDelayCalibrationData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString file']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'file'),)
rszvb_LoadMixerDelayCalibrationData  = prototype(('rszvb_LoadMixerDelayCalibrationData', rszvbDLL), paramflags)
rszvb_LoadMixerDelayCalibrationData.name = 'rszvb_LoadMixerDelayCalibrationData'
rszvb_LoadMixerDelayCalibrationData.errcheck = __errorcheck__
rszvb_LoadMixerDelayCalibrationData.output = False
# rszvb_StoreMixerDelayCalibrationData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString file']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'file'),)
rszvb_StoreMixerDelayCalibrationData  = prototype(('rszvb_StoreMixerDelayCalibrationData', rszvbDLL), paramflags)
rszvb_StoreMixerDelayCalibrationData.name = 'rszvb_StoreMixerDelayCalibrationData'
rszvb_StoreMixerDelayCalibrationData.errcheck = __errorcheck__
rszvb_StoreMixerDelayCalibrationData.output = False
# rszvb_SetVectorMixerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 mixerMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'mixerMode'),)
rszvb_SetVectorMixerMode  = prototype(('rszvb_SetVectorMixerMode', rszvbDLL), paramflags)
rszvb_SetVectorMixerMode.name = 'rszvb_SetVectorMixerMode'
rszvb_SetVectorMixerMode.errcheck = __errorcheck__
rszvb_SetVectorMixerMode.output = False
# rszvb_GetVectorMixerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* mixerMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'mixerMode'),)
rszvb_GetVectorMixerMode  = prototype(('rszvb_GetVectorMixerMode', rszvbDLL), paramflags)
rszvb_GetVectorMixerMode.name = 'rszvb_GetVectorMixerMode'
rszvb_GetVectorMixerMode.errcheck = __errorcheck__
rszvb_GetVectorMixerMode.output = True
# rszvb_SetInternalSignalSourceAUX ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 internalSignalSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'internalSignalSource'),)
rszvb_SetInternalSignalSourceAUX  = prototype(('rszvb_SetInternalSignalSourceAUX', rszvbDLL), paramflags)
rszvb_SetInternalSignalSourceAUX.name = 'rszvb_SetInternalSignalSourceAUX'
rszvb_SetInternalSignalSourceAUX.errcheck = __errorcheck__
rszvb_SetInternalSignalSourceAUX.output = False
# rszvb_GetInternalSignalSourceAUX ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* internalSignalSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'internalSignalSource'),)
rszvb_GetInternalSignalSourceAUX  = prototype(('rszvb_GetInternalSignalSourceAUX', rszvbDLL), paramflags)
rszvb_GetInternalSignalSourceAUX.name = 'rszvb_GetInternalSignalSourceAUX'
rszvb_GetInternalSignalSourceAUX.errcheck = __errorcheck__
rszvb_GetInternalSignalSourceAUX.output = True
# rszvb_SetExternalSignalSourceAUX ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 externalSignalSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'externalSignalSource'),)
rszvb_SetExternalSignalSourceAUX  = prototype(('rszvb_SetExternalSignalSourceAUX', rszvbDLL), paramflags)
rszvb_SetExternalSignalSourceAUX.name = 'rszvb_SetExternalSignalSourceAUX'
rszvb_SetExternalSignalSourceAUX.errcheck = __errorcheck__
rszvb_SetExternalSignalSourceAUX.output = False
# rszvb_GetExternalSignalSourceAUX ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* externalSignalSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'externalSignalSource'),)
rszvb_GetExternalSignalSourceAUX  = prototype(('rszvb_GetExternalSignalSourceAUX', rszvbDLL), paramflags)
rszvb_GetExternalSignalSourceAUX.name = 'rszvb_GetExternalSignalSourceAUX'
rszvb_GetExternalSignalSourceAUX.errcheck = __errorcheck__
rszvb_GetExternalSignalSourceAUX.output = True
# rszvb_SetAUXMixerPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),)
rszvb_SetAUXMixerPort  = prototype(('rszvb_SetAUXMixerPort', rszvbDLL), paramflags)
rszvb_SetAUXMixerPort.name = 'rszvb_SetAUXMixerPort'
rszvb_SetAUXMixerPort.errcheck = __errorcheck__
rszvb_SetAUXMixerPort.output = False
# rszvb_GetAUXMixerPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'portNumber'),)
rszvb_GetAUXMixerPort  = prototype(('rszvb_GetAUXMixerPort', rszvbDLL), paramflags)
rszvb_GetAUXMixerPort.name = 'rszvb_GetAUXMixerPort'
rszvb_GetAUXMixerPort.errcheck = __errorcheck__
rszvb_GetAUXMixerPort.output = True
# rszvb_SetAUXFixedPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 fixedPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'fixedPower'),)
rszvb_SetAUXFixedPower  = prototype(('rszvb_SetAUXFixedPower', rszvbDLL), paramflags)
rszvb_SetAUXFixedPower.name = 'rszvb_SetAUXFixedPower'
rszvb_SetAUXFixedPower.errcheck = __errorcheck__
rszvb_SetAUXFixedPower.output = False
# rszvb_GetAUXFixedPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* fixedPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'fixedPower'),)
rszvb_GetAUXFixedPower  = prototype(('rszvb_GetAUXFixedPower', rszvbDLL), paramflags)
rszvb_GetAUXFixedPower.name = 'rszvb_GetAUXFixedPower'
rszvb_GetAUXFixedPower.errcheck = __errorcheck__
rszvb_GetAUXFixedPower.output = True
# rszvb_AutomaticVectorMixerCalibration ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 mode', 'ViBoolean dispersion', 'ViInt32 mixerParameter', 'ViReal64 delayPhase']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'mode'),(1, 'dispersion'),(1, 'mixerParameter'),(1, 'delayPhase'),)
rszvb_AutomaticVectorMixerCalibration  = prototype(('rszvb_AutomaticVectorMixerCalibration', rszvbDLL), paramflags)
rszvb_AutomaticVectorMixerCalibration.name = 'rszvb_AutomaticVectorMixerCalibration'
rszvb_AutomaticVectorMixerCalibration.errcheck = __errorcheck__
rszvb_AutomaticVectorMixerCalibration.output = False
# rszvb_SetIMODLowerToneSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 source', 'ViInt32 sourceNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'source'),(1, 'sourceNumber'),)
rszvb_SetIMODLowerToneSource  = prototype(('rszvb_SetIMODLowerToneSource', rszvbDLL), paramflags)
rszvb_SetIMODLowerToneSource.name = 'rszvb_SetIMODLowerToneSource'
rszvb_SetIMODLowerToneSource.errcheck = __errorcheck__
rszvb_SetIMODLowerToneSource.output = False
# rszvb_GetIMODLowerToneSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* source', 'ViInt32* sourceNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'source'),(2, 'sourceNumber'),)
rszvb_GetIMODLowerToneSource  = prototype(('rszvb_GetIMODLowerToneSource', rszvbDLL), paramflags)
rszvb_GetIMODLowerToneSource.name = 'rszvb_GetIMODLowerToneSource'
rszvb_GetIMODLowerToneSource.errcheck = __errorcheck__
rszvb_GetIMODLowerToneSource.output = True
# rszvb_SetIMODUpperToneSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 source', 'ViInt32 sourceNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'source'),(1, 'sourceNumber'),)
rszvb_SetIMODUpperToneSource  = prototype(('rszvb_SetIMODUpperToneSource', rszvbDLL), paramflags)
rszvb_SetIMODUpperToneSource.name = 'rszvb_SetIMODUpperToneSource'
rszvb_SetIMODUpperToneSource.errcheck = __errorcheck__
rszvb_SetIMODUpperToneSource.output = False
# rszvb_GetIMODUpperToneSource ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* source', 'ViInt32* sourceNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'source'),(2, 'sourceNumber'),)
rszvb_GetIMODUpperToneSource  = prototype(('rszvb_GetIMODUpperToneSource', rszvbDLL), paramflags)
rszvb_GetIMODUpperToneSource.name = 'rszvb_GetIMODUpperToneSource'
rszvb_GetIMODUpperToneSource.errcheck = __errorcheck__
rszvb_GetIMODUpperToneSource.output = True
# rszvb_SetIMODToneDistance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 toneDistance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'toneDistance'),)
rszvb_SetIMODToneDistance  = prototype(('rszvb_SetIMODToneDistance', rszvbDLL), paramflags)
rszvb_SetIMODToneDistance.name = 'rszvb_SetIMODToneDistance'
rszvb_SetIMODToneDistance.errcheck = __errorcheck__
rszvb_SetIMODToneDistance.output = False
# rszvb_GetIMODToneDistance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* toneDistance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'toneDistance'),)
rszvb_GetIMODToneDistance  = prototype(('rszvb_GetIMODToneDistance', rszvbDLL), paramflags)
rszvb_GetIMODToneDistance.name = 'rszvb_GetIMODToneDistance'
rszvb_GetIMODToneDistance.errcheck = __errorcheck__
rszvb_GetIMODToneDistance.output = True
# rszvb_SetIMODReceiverPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 receiverPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'receiverPort'),)
rszvb_SetIMODReceiverPort  = prototype(('rszvb_SetIMODReceiverPort', rszvbDLL), paramflags)
rszvb_SetIMODReceiverPort.name = 'rszvb_SetIMODReceiverPort'
rszvb_SetIMODReceiverPort.errcheck = __errorcheck__
rszvb_SetIMODReceiverPort.output = False
# rszvb_GetIMODReceiverPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* receiverPort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'receiverPort'),)
rszvb_GetIMODReceiverPort  = prototype(('rszvb_GetIMODReceiverPort', rszvbDLL), paramflags)
rszvb_GetIMODReceiverPort.name = 'rszvb_GetIMODReceiverPort'
rszvb_GetIMODReceiverPort.errcheck = __errorcheck__
rszvb_GetIMODReceiverPort.output = True
# rszvb_SetIMODMeasurementOrder ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 productOrder', 'ViBoolean measurementState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'productOrder'),(1, 'measurementState'),)
rszvb_SetIMODMeasurementOrder  = prototype(('rszvb_SetIMODMeasurementOrder', rszvbDLL), paramflags)
rszvb_SetIMODMeasurementOrder.name = 'rszvb_SetIMODMeasurementOrder'
rszvb_SetIMODMeasurementOrder.errcheck = __errorcheck__
rszvb_SetIMODMeasurementOrder.output = False
# rszvb_GetIMODMeasurementOrder ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 productOrder', 'ViBoolean* measurementState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'productOrder'),(2, 'measurementState'),)
rszvb_GetIMODMeasurementOrder  = prototype(('rszvb_GetIMODMeasurementOrder', rszvbDLL), paramflags)
rszvb_GetIMODMeasurementOrder.name = 'rszvb_GetIMODMeasurementOrder'
rszvb_GetIMODMeasurementOrder.errcheck = __errorcheck__
rszvb_GetIMODMeasurementOrder.output = True
# rszvb_SetIMODEnhancedWaveCorrection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetIMODEnhancedWaveCorrection  = prototype(('rszvb_SetIMODEnhancedWaveCorrection', rszvbDLL), paramflags)
rszvb_SetIMODEnhancedWaveCorrection.name = 'rszvb_SetIMODEnhancedWaveCorrection'
rszvb_SetIMODEnhancedWaveCorrection.errcheck = __errorcheck__
rszvb_SetIMODEnhancedWaveCorrection.output = False
# rszvb_GetIMODEnhancedWaveCorrection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetIMODEnhancedWaveCorrection  = prototype(('rszvb_GetIMODEnhancedWaveCorrection', rszvbDLL), paramflags)
rszvb_GetIMODEnhancedWaveCorrection.name = 'rszvb_GetIMODEnhancedWaveCorrection'
rszvb_GetIMODEnhancedWaveCorrection.errcheck = __errorcheck__
rszvb_GetIMODEnhancedWaveCorrection.output = True
# rszvb_SetIMODInternalCombiner ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean internalCombiner']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'internalCombiner'),)
rszvb_SetIMODInternalCombiner  = prototype(('rszvb_SetIMODInternalCombiner', rszvbDLL), paramflags)
rszvb_SetIMODInternalCombiner.name = 'rszvb_SetIMODInternalCombiner'
rszvb_SetIMODInternalCombiner.errcheck = __errorcheck__
rszvb_SetIMODInternalCombiner.output = False
# rszvb_GetIMODInternalCombiner ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* internalCombiner']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'internalCombiner'),)
rszvb_GetIMODInternalCombiner  = prototype(('rszvb_GetIMODInternalCombiner', rszvbDLL), paramflags)
rszvb_GetIMODInternalCombiner.name = 'rszvb_GetIMODInternalCombiner'
rszvb_GetIMODInternalCombiner.errcheck = __errorcheck__
rszvb_GetIMODInternalCombiner.output = True
# rszvb_SetIMODSpectrumMeasurement ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean spectrumMeasurement']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'spectrumMeasurement'),)
rszvb_SetIMODSpectrumMeasurement  = prototype(('rszvb_SetIMODSpectrumMeasurement', rszvbDLL), paramflags)
rszvb_SetIMODSpectrumMeasurement.name = 'rszvb_SetIMODSpectrumMeasurement'
rszvb_SetIMODSpectrumMeasurement.errcheck = __errorcheck__
rszvb_SetIMODSpectrumMeasurement.output = False
# rszvb_GetIMODSpectrumMeasurement ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* spectrumMeasurement']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'spectrumMeasurement'),)
rszvb_GetIMODSpectrumMeasurement  = prototype(('rszvb_GetIMODSpectrumMeasurement', rszvbDLL), paramflags)
rszvb_GetIMODSpectrumMeasurement.name = 'rszvb_GetIMODSpectrumMeasurement'
rszvb_GetIMODSpectrumMeasurement.errcheck = __errorcheck__
rszvb_GetIMODSpectrumMeasurement.output = True
# rszvb_SetIMODMaxOrder ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 maxOrder']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'maxOrder'),)
rszvb_SetIMODMaxOrder  = prototype(('rszvb_SetIMODMaxOrder', rszvbDLL), paramflags)
rszvb_SetIMODMaxOrder.name = 'rszvb_SetIMODMaxOrder'
rszvb_SetIMODMaxOrder.errcheck = __errorcheck__
rszvb_SetIMODMaxOrder.output = False
# rszvb_GetIMODMaxOrder ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* maxOrder']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'maxOrder'),)
rszvb_GetIMODMaxOrder  = prototype(('rszvb_GetIMODMaxOrder', rszvbDLL), paramflags)
rszvb_GetIMODMaxOrder.name = 'rszvb_GetIMODMaxOrder'
rszvb_GetIMODMaxOrder.errcheck = __errorcheck__
rszvb_GetIMODMaxOrder.output = True
# rszvb_SetIMODTwoToneOutput ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 twoToneOutput']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'twoToneOutput'),)
rszvb_SetIMODTwoToneOutput  = prototype(('rszvb_SetIMODTwoToneOutput', rszvbDLL), paramflags)
rszvb_SetIMODTwoToneOutput.name = 'rszvb_SetIMODTwoToneOutput'
rszvb_SetIMODTwoToneOutput.errcheck = __errorcheck__
rszvb_SetIMODTwoToneOutput.output = False
# rszvb_GetIMODTwoToneOutput ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* twoToneOutput']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'twoToneOutput'),)
rszvb_GetIMODTwoToneOutput  = prototype(('rszvb_GetIMODTwoToneOutput', rszvbDLL), paramflags)
rszvb_GetIMODTwoToneOutput.name = 'rszvb_GetIMODTwoToneOutput'
rszvb_GetIMODTwoToneOutput.errcheck = __errorcheck__
rszvb_GetIMODTwoToneOutput.output = True
# rszvb_StartIMODLowerToneSourcePowerCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_StartIMODLowerToneSourcePowerCalibration  = prototype(('rszvb_StartIMODLowerToneSourcePowerCalibration', rszvbDLL), paramflags)
rszvb_StartIMODLowerToneSourcePowerCalibration.name = 'rszvb_StartIMODLowerToneSourcePowerCalibration'
rszvb_StartIMODLowerToneSourcePowerCalibration.errcheck = __errorcheck__
rszvb_StartIMODLowerToneSourcePowerCalibration.output = False
# rszvb_StartIMODUpperToneSourcePowerCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_StartIMODUpperToneSourcePowerCalibration  = prototype(('rszvb_StartIMODUpperToneSourcePowerCalibration', rszvbDLL), paramflags)
rszvb_StartIMODUpperToneSourcePowerCalibration.name = 'rszvb_StartIMODUpperToneSourcePowerCalibration'
rszvb_StartIMODUpperToneSourcePowerCalibration.errcheck = __errorcheck__
rszvb_StartIMODUpperToneSourcePowerCalibration.output = False
# rszvb_StartIMODReceivePortSourcePowerCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_StartIMODReceivePortSourcePowerCalibration  = prototype(('rszvb_StartIMODReceivePortSourcePowerCalibration', rszvbDLL), paramflags)
rszvb_StartIMODReceivePortSourcePowerCalibration.name = 'rszvb_StartIMODReceivePortSourcePowerCalibration'
rszvb_StartIMODReceivePortSourcePowerCalibration.errcheck = __errorcheck__
rszvb_StartIMODReceivePortSourcePowerCalibration.output = False
# rszvb_StartIMODLowerUpperTonePortsSourcePowerCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_StartIMODLowerUpperTonePortsSourcePowerCalibration  = prototype(('rszvb_StartIMODLowerUpperTonePortsSourcePowerCalibration', rszvbDLL), paramflags)
rszvb_StartIMODLowerUpperTonePortsSourcePowerCalibration.name = 'rszvb_StartIMODLowerUpperTonePortsSourcePowerCalibration'
rszvb_StartIMODLowerUpperTonePortsSourcePowerCalibration.errcheck = __errorcheck__
rszvb_StartIMODLowerUpperTonePortsSourcePowerCalibration.output = False
# rszvb_StartIMODReceiverPortPowerCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_StartIMODReceiverPortPowerCalibration  = prototype(('rszvb_StartIMODReceiverPortPowerCalibration', rszvbDLL), paramflags)
rszvb_StartIMODReceiverPortPowerCalibration.name = 'rszvb_StartIMODReceiverPortPowerCalibration'
rszvb_StartIMODReceiverPortPowerCalibration.errcheck = __errorcheck__
rszvb_StartIMODReceiverPortPowerCalibration.output = False
# rszvb_StartIMODReceiverPowerCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_StartIMODReceiverPowerCalibration  = prototype(('rszvb_StartIMODReceiverPowerCalibration', rszvbDLL), paramflags)
rszvb_StartIMODReceiverPowerCalibration.name = 'rszvb_StartIMODReceiverPowerCalibration'
rszvb_StartIMODReceiverPowerCalibration.errcheck = __errorcheck__
rszvb_StartIMODReceiverPowerCalibration.output = False
# rszvb_SetIMODDistortionMeasurementCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetIMODDistortionMeasurementCalibrationState  = prototype(('rszvb_SetIMODDistortionMeasurementCalibrationState', rszvbDLL), paramflags)
rszvb_SetIMODDistortionMeasurementCalibrationState.name = 'rszvb_SetIMODDistortionMeasurementCalibrationState'
rszvb_SetIMODDistortionMeasurementCalibrationState.errcheck = __errorcheck__
rszvb_SetIMODDistortionMeasurementCalibrationState.output = False
# rszvb_GetIMODDistortionMeasurementCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetIMODDistortionMeasurementCalibrationState  = prototype(('rszvb_GetIMODDistortionMeasurementCalibrationState', rszvbDLL), paramflags)
rszvb_GetIMODDistortionMeasurementCalibrationState.name = 'rszvb_GetIMODDistortionMeasurementCalibrationState'
rszvb_GetIMODDistortionMeasurementCalibrationState.errcheck = __errorcheck__
rszvb_GetIMODDistortionMeasurementCalibrationState.output = True
# rszvb_DisableIMODMeasurement ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_DisableIMODMeasurement  = prototype(('rszvb_DisableIMODMeasurement', rszvbDLL), paramflags)
rszvb_DisableIMODMeasurement.name = 'rszvb_DisableIMODMeasurement'
rszvb_DisableIMODMeasurement.errcheck = __errorcheck__
rszvb_DisableIMODMeasurement.output = False
# rszvb_SetNoiseFigureDetectorMeasurementTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 detectorTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'detectorTime'),)
rszvb_SetNoiseFigureDetectorMeasurementTime  = prototype(('rszvb_SetNoiseFigureDetectorMeasurementTime', rszvbDLL), paramflags)
rszvb_SetNoiseFigureDetectorMeasurementTime.name = 'rszvb_SetNoiseFigureDetectorMeasurementTime'
rszvb_SetNoiseFigureDetectorMeasurementTime.errcheck = __errorcheck__
rszvb_SetNoiseFigureDetectorMeasurementTime.output = False
# rszvb_GetNoiseFigureDetectorMeasurementTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* detectorTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'detectorTime'),)
rszvb_GetNoiseFigureDetectorMeasurementTime  = prototype(('rszvb_GetNoiseFigureDetectorMeasurementTime', rszvbDLL), paramflags)
rszvb_GetNoiseFigureDetectorMeasurementTime.name = 'rszvb_GetNoiseFigureDetectorMeasurementTime'
rszvb_GetNoiseFigureDetectorMeasurementTime.errcheck = __errorcheck__
rszvb_GetNoiseFigureDetectorMeasurementTime.output = True
# rszvb_SetNoiseFigureMeasurementMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean measurementMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'measurementMode'),)
rszvb_SetNoiseFigureMeasurementMode  = prototype(('rszvb_SetNoiseFigureMeasurementMode', rszvbDLL), paramflags)
rszvb_SetNoiseFigureMeasurementMode.name = 'rszvb_SetNoiseFigureMeasurementMode'
rszvb_SetNoiseFigureMeasurementMode.errcheck = __errorcheck__
rszvb_SetNoiseFigureMeasurementMode.output = False
# rszvb_GetNoiseFigureMeasurementMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* measurementMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'measurementMode'),)
rszvb_GetNoiseFigureMeasurementMode  = prototype(('rszvb_GetNoiseFigureMeasurementMode', rszvbDLL), paramflags)
rszvb_GetNoiseFigureMeasurementMode.name = 'rszvb_GetNoiseFigureMeasurementMode'
rszvb_GetNoiseFigureMeasurementMode.errcheck = __errorcheck__
rszvb_GetNoiseFigureMeasurementMode.output = True
# rszvb_SetNoiseFigureLOOscillator ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean LOOscillator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'LOOscillator'),)
rszvb_SetNoiseFigureLOOscillator  = prototype(('rszvb_SetNoiseFigureLOOscillator', rszvbDLL), paramflags)
rszvb_SetNoiseFigureLOOscillator.name = 'rszvb_SetNoiseFigureLOOscillator'
rszvb_SetNoiseFigureLOOscillator.errcheck = __errorcheck__
rszvb_SetNoiseFigureLOOscillator.output = False
# rszvb_GetNoiseFigureLOOscillator ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* LOOscillator']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'LOOscillator'),)
rszvb_GetNoiseFigureLOOscillator  = prototype(('rszvb_GetNoiseFigureLOOscillator', rszvbDLL), paramflags)
rszvb_GetNoiseFigureLOOscillator.name = 'rszvb_GetNoiseFigureLOOscillator'
rszvb_GetNoiseFigureLOOscillator.errcheck = __errorcheck__
rszvb_GetNoiseFigureLOOscillator.output = True
# rszvb_SetNoiseFigureNarowbandDUT ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean narowbandDUT']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'narowbandDUT'),)
rszvb_SetNoiseFigureNarowbandDUT  = prototype(('rszvb_SetNoiseFigureNarowbandDUT', rszvbDLL), paramflags)
rszvb_SetNoiseFigureNarowbandDUT.name = 'rszvb_SetNoiseFigureNarowbandDUT'
rszvb_SetNoiseFigureNarowbandDUT.errcheck = __errorcheck__
rszvb_SetNoiseFigureNarowbandDUT.output = False
# rszvb_GetNoiseFigureNarowbandDUT ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* narowbandDUT']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'narowbandDUT'),)
rszvb_GetNoiseFigureNarowbandDUT  = prototype(('rszvb_GetNoiseFigureNarowbandDUT', rszvbDLL), paramflags)
rszvb_GetNoiseFigureNarowbandDUT.name = 'rszvb_GetNoiseFigureNarowbandDUT'
rszvb_GetNoiseFigureNarowbandDUT.errcheck = __errorcheck__
rszvb_GetNoiseFigureNarowbandDUT.output = True
# rszvb_SetNoiseFigureRFImageCorrection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean RFImageCorrection']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'RFImageCorrection'),)
rszvb_SetNoiseFigureRFImageCorrection  = prototype(('rszvb_SetNoiseFigureRFImageCorrection', rszvbDLL), paramflags)
rszvb_SetNoiseFigureRFImageCorrection.name = 'rszvb_SetNoiseFigureRFImageCorrection'
rszvb_SetNoiseFigureRFImageCorrection.errcheck = __errorcheck__
rszvb_SetNoiseFigureRFImageCorrection.output = False
# rszvb_GetNoiseFigureRFImageCorrection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* RFImageCorrection']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'RFImageCorrection'),)
rszvb_GetNoiseFigureRFImageCorrection  = prototype(('rszvb_GetNoiseFigureRFImageCorrection', rszvbDLL), paramflags)
rszvb_GetNoiseFigureRFImageCorrection.name = 'rszvb_GetNoiseFigureRFImageCorrection'
rszvb_GetNoiseFigureRFImageCorrection.errcheck = __errorcheck__
rszvb_GetNoiseFigureRFImageCorrection.output = True
# rszvb_SetNoiseFigureCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean calibration']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibration'),)
rszvb_SetNoiseFigureCalibrationState  = prototype(('rszvb_SetNoiseFigureCalibrationState', rszvbDLL), paramflags)
rszvb_SetNoiseFigureCalibrationState.name = 'rszvb_SetNoiseFigureCalibrationState'
rszvb_SetNoiseFigureCalibrationState.errcheck = __errorcheck__
rszvb_SetNoiseFigureCalibrationState.output = False
# rszvb_GetNoiseFigureCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* calibration']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'calibration'),)
rszvb_GetNoiseFigureCalibrationState  = prototype(('rszvb_GetNoiseFigureCalibrationState', rszvbDLL), paramflags)
rszvb_GetNoiseFigureCalibrationState.name = 'rszvb_GetNoiseFigureCalibrationState'
rszvb_GetNoiseFigureCalibrationState.errcheck = __errorcheck__
rszvb_GetNoiseFigureCalibrationState.output = True
# rszvb_GetNoiseFigureCalibrationStateLabel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 bufferSize', 'ViChar _VI_FAR label[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'bufferSize'),(1, 'label[]'),)
rszvb_GetNoiseFigureCalibrationStateLabel  = prototype(('rszvb_GetNoiseFigureCalibrationStateLabel', rszvbDLL), paramflags)
rszvb_GetNoiseFigureCalibrationStateLabel.name = 'rszvb_GetNoiseFigureCalibrationStateLabel'
rszvb_GetNoiseFigureCalibrationStateLabel.errcheck = __errorcheck__
rszvb_GetNoiseFigureCalibrationStateLabel.output = False
# rszvb_DefineNoiseFigureCalibrationSettings ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port1', 'ViInt32 port2', 'ViBoolean externalAttenuator', 'ViReal64 sourceNoiseCalAttenuation', 'ViReal64 DUTMeasurementAttenuation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_bool,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port1'),(1, 'port2'),(1, 'externalAttenuator'),(1, 'sourceNoiseCalAttenuation'),(1, 'DUTMeasurementAttenuation'),)
rszvb_DefineNoiseFigureCalibrationSettings  = prototype(('rszvb_DefineNoiseFigureCalibrationSettings', rszvbDLL), paramflags)
rszvb_DefineNoiseFigureCalibrationSettings.name = 'rszvb_DefineNoiseFigureCalibrationSettings'
rszvb_DefineNoiseFigureCalibrationSettings.errcheck = __errorcheck__
rszvb_DefineNoiseFigureCalibrationSettings.output = False
# rszvb_StartNoiseFigureCalibration ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationStep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationStep'),)
rszvb_StartNoiseFigureCalibration  = prototype(('rszvb_StartNoiseFigureCalibration', rszvbDLL), paramflags)
rszvb_StartNoiseFigureCalibration.name = 'rszvb_StartNoiseFigureCalibration'
rszvb_StartNoiseFigureCalibration.errcheck = __errorcheck__
rszvb_StartNoiseFigureCalibration.output = False
# rszvb_TerminateNoiseFigureCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_TerminateNoiseFigureCalibration  = prototype(('rszvb_TerminateNoiseFigureCalibration', rszvbDLL), paramflags)
rszvb_TerminateNoiseFigureCalibration.name = 'rszvb_TerminateNoiseFigureCalibration'
rszvb_TerminateNoiseFigureCalibration.errcheck = __errorcheck__
rszvb_TerminateNoiseFigureCalibration.output = False
# rszvb_CompleteNoiseFigureCalibration ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_CompleteNoiseFigureCalibration  = prototype(('rszvb_CompleteNoiseFigureCalibration', rszvbDLL), paramflags)
rszvb_CompleteNoiseFigureCalibration.name = 'rszvb_CompleteNoiseFigureCalibration'
rszvb_CompleteNoiseFigureCalibration.errcheck = __errorcheck__
rszvb_CompleteNoiseFigureCalibration.output = False
# rszvb_OverwriteNoiseFigureChannelSettings ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'traceName'),)
rszvb_OverwriteNoiseFigureChannelSettings  = prototype(('rszvb_OverwriteNoiseFigureChannelSettings', rszvbDLL), paramflags)
rszvb_OverwriteNoiseFigureChannelSettings.name = 'rszvb_OverwriteNoiseFigureChannelSettings'
rszvb_OverwriteNoiseFigureChannelSettings.errcheck = __errorcheck__
rszvb_OverwriteNoiseFigureChannelSettings.output = False
# rszvb_SetVirtualTransformBalancedState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 logicalPortNumber', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'logicalPortNumber'),(1, 'state'),)
rszvb_SetVirtualTransformBalancedState  = prototype(('rszvb_SetVirtualTransformBalancedState', rszvbDLL), paramflags)
rszvb_SetVirtualTransformBalancedState.name = 'rszvb_SetVirtualTransformBalancedState'
rszvb_SetVirtualTransformBalancedState.errcheck = __errorcheck__
rszvb_SetVirtualTransformBalancedState.output = False
# rszvb_GetVirtualTransformBalancedState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 logicalPortNumber', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'logicalPortNumber'),(2, 'state'),)
rszvb_GetVirtualTransformBalancedState  = prototype(('rszvb_GetVirtualTransformBalancedState', rszvbDLL), paramflags)
rszvb_GetVirtualTransformBalancedState.name = 'rszvb_GetVirtualTransformBalancedState'
rszvb_GetVirtualTransformBalancedState.errcheck = __errorcheck__
rszvb_GetVirtualTransformBalancedState.output = True
# rszvb_SetVirtualTransformBalancedPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 logicalPortNumber', 'ViInt32 parameterType', 'ViInt32 parameterNumber', 'ViInt32 circuitModel', 'ViReal64 value']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'logicalPortNumber'),(1, 'parameterType'),(1, 'parameterNumber'),(1, 'circuitModel'),(1, 'value'),)
rszvb_SetVirtualTransformBalancedPort  = prototype(('rszvb_SetVirtualTransformBalancedPort', rszvbDLL), paramflags)
rszvb_SetVirtualTransformBalancedPort.name = 'rszvb_SetVirtualTransformBalancedPort'
rszvb_SetVirtualTransformBalancedPort.errcheck = __errorcheck__
rszvb_SetVirtualTransformBalancedPort.output = False
# rszvb_GetVirtualTransformBalancedPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 logicalPortNumber', 'ViInt32 parameterType', 'ViInt32 parameterNumber', 'ViInt32 circuitModel', 'ViReal64* value']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'logicalPortNumber'),(1, 'parameterType'),(1, 'parameterNumber'),(1, 'circuitModel'),(2, 'value'),)
rszvb_GetVirtualTransformBalancedPort  = prototype(('rszvb_GetVirtualTransformBalancedPort', rszvbDLL), paramflags)
rszvb_GetVirtualTransformBalancedPort.name = 'rszvb_GetVirtualTransformBalancedPort'
rszvb_GetVirtualTransformBalancedPort.errcheck = __errorcheck__
rszvb_GetVirtualTransformBalancedPort.output = True
# rszvb_SetVirtualTransformBalancedCircuitModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 logicalPortNumber', 'ViInt32 circuitModel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'logicalPortNumber'),(1, 'circuitModel'),)
rszvb_SetVirtualTransformBalancedCircuitModel  = prototype(('rszvb_SetVirtualTransformBalancedCircuitModel', rszvbDLL), paramflags)
rszvb_SetVirtualTransformBalancedCircuitModel.name = 'rszvb_SetVirtualTransformBalancedCircuitModel'
rszvb_SetVirtualTransformBalancedCircuitModel.errcheck = __errorcheck__
rszvb_SetVirtualTransformBalancedCircuitModel.output = False
# rszvb_GetVirtualTransformBalancedCircuitModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 logicalPortNumber', 'ViInt32* circuitModel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'logicalPortNumber'),(2, 'circuitModel'),)
rszvb_GetVirtualTransformBalancedCircuitModel  = prototype(('rszvb_GetVirtualTransformBalancedCircuitModel', rszvbDLL), paramflags)
rszvb_GetVirtualTransformBalancedCircuitModel.name = 'rszvb_GetVirtualTransformBalancedCircuitModel'
rszvb_GetVirtualTransformBalancedCircuitModel.errcheck = __errorcheck__
rszvb_GetVirtualTransformBalancedCircuitModel.output = True
# rszvb_LoadBalancedPortCircuitModelData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 logicalPortNumber', 'ViString fileName', 'ViInt32 parameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'logicalPortNumber'),(1, 'fileName'),(1, 'parameter'),)
rszvb_LoadBalancedPortCircuitModelData  = prototype(('rszvb_LoadBalancedPortCircuitModelData', rszvbDLL), paramflags)
rszvb_LoadBalancedPortCircuitModelData.name = 'rszvb_LoadBalancedPortCircuitModelData'
rszvb_LoadBalancedPortCircuitModelData.errcheck = __errorcheck__
rszvb_LoadBalancedPortCircuitModelData.output = False
# rszvb_LoadAndInterchangeBalancedPortCircuitModelData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 logicalPortNumber', 'ViString fileName', 'ViInt32 parameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'logicalPortNumber'),(1, 'fileName'),(1, 'parameter'),)
rszvb_LoadAndInterchangeBalancedPortCircuitModelData  = prototype(('rszvb_LoadAndInterchangeBalancedPortCircuitModelData', rszvbDLL), paramflags)
rszvb_LoadAndInterchangeBalancedPortCircuitModelData.name = 'rszvb_LoadAndInterchangeBalancedPortCircuitModelData'
rszvb_LoadAndInterchangeBalancedPortCircuitModelData.errcheck = __errorcheck__
rszvb_LoadAndInterchangeBalancedPortCircuitModelData.output = False
# rszvb_SetVirtualTransformSingleEndedState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 physicalPortNumber', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'physicalPortNumber'),(1, 'state'),)
rszvb_SetVirtualTransformSingleEndedState  = prototype(('rszvb_SetVirtualTransformSingleEndedState', rszvbDLL), paramflags)
rszvb_SetVirtualTransformSingleEndedState.name = 'rszvb_SetVirtualTransformSingleEndedState'
rszvb_SetVirtualTransformSingleEndedState.errcheck = __errorcheck__
rszvb_SetVirtualTransformSingleEndedState.output = False
# rszvb_GetVirtualTransformSingleEndedState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 physicalPortNumber', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'physicalPortNumber'),(2, 'state'),)
rszvb_GetVirtualTransformSingleEndedState  = prototype(('rszvb_GetVirtualTransformSingleEndedState', rszvbDLL), paramflags)
rszvb_GetVirtualTransformSingleEndedState.name = 'rszvb_GetVirtualTransformSingleEndedState'
rszvb_GetVirtualTransformSingleEndedState.errcheck = __errorcheck__
rszvb_GetVirtualTransformSingleEndedState.output = True
# rszvb_SetVirtualTransformSingleEndedPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 physicalPortNumber', 'ViInt32 parameterType', 'ViInt32 parameterNumber', 'ViInt32 circuitModel', 'ViReal64 value']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'physicalPortNumber'),(1, 'parameterType'),(1, 'parameterNumber'),(1, 'circuitModel'),(1, 'value'),)
rszvb_SetVirtualTransformSingleEndedPort  = prototype(('rszvb_SetVirtualTransformSingleEndedPort', rszvbDLL), paramflags)
rszvb_SetVirtualTransformSingleEndedPort.name = 'rszvb_SetVirtualTransformSingleEndedPort'
rszvb_SetVirtualTransformSingleEndedPort.errcheck = __errorcheck__
rszvb_SetVirtualTransformSingleEndedPort.output = False
# rszvb_GetVirtualTransformSingleEndedPort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 physicalPortNumber', 'ViInt32 parameterType', 'ViInt32 parameterNumber', 'ViInt32 circuitModel', 'ViReal64* value']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'physicalPortNumber'),(1, 'parameterType'),(1, 'parameterNumber'),(1, 'circuitModel'),(2, 'value'),)
rszvb_GetVirtualTransformSingleEndedPort  = prototype(('rszvb_GetVirtualTransformSingleEndedPort', rszvbDLL), paramflags)
rszvb_GetVirtualTransformSingleEndedPort.name = 'rszvb_GetVirtualTransformSingleEndedPort'
rszvb_GetVirtualTransformSingleEndedPort.errcheck = __errorcheck__
rszvb_GetVirtualTransformSingleEndedPort.output = True
# rszvb_SetVirtualTransformSingleEndedCircuitModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 physicalPortNumber', 'ViInt32 circuitModel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'physicalPortNumber'),(1, 'circuitModel'),)
rszvb_SetVirtualTransformSingleEndedCircuitModel  = prototype(('rszvb_SetVirtualTransformSingleEndedCircuitModel', rszvbDLL), paramflags)
rszvb_SetVirtualTransformSingleEndedCircuitModel.name = 'rszvb_SetVirtualTransformSingleEndedCircuitModel'
rszvb_SetVirtualTransformSingleEndedCircuitModel.errcheck = __errorcheck__
rszvb_SetVirtualTransformSingleEndedCircuitModel.output = False
# rszvb_GetVirtualTransformSingleEndedCircuitModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 physicalPortNumber', 'ViInt32* circuitModel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'physicalPortNumber'),(2, 'circuitModel'),)
rszvb_GetVirtualTransformSingleEndedCircuitModel  = prototype(('rszvb_GetVirtualTransformSingleEndedCircuitModel', rszvbDLL), paramflags)
rszvb_GetVirtualTransformSingleEndedCircuitModel.name = 'rszvb_GetVirtualTransformSingleEndedCircuitModel'
rszvb_GetVirtualTransformSingleEndedCircuitModel.errcheck = __errorcheck__
rszvb_GetVirtualTransformSingleEndedCircuitModel.output = True
# rszvb_LoadSingleEndedPortCircuitModelData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 physicalPortNumber', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'physicalPortNumber'),(1, 'fileName'),)
rszvb_LoadSingleEndedPortCircuitModelData  = prototype(('rszvb_LoadSingleEndedPortCircuitModelData', rszvbDLL), paramflags)
rszvb_LoadSingleEndedPortCircuitModelData.name = 'rszvb_LoadSingleEndedPortCircuitModelData'
rszvb_LoadSingleEndedPortCircuitModelData.errcheck = __errorcheck__
rszvb_LoadSingleEndedPortCircuitModelData.output = False
# rszvb_LoadAndInterchangeSingleEndedPortCircuitModelData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 physicalPortNumber', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'physicalPortNumber'),(1, 'fileName'),)
rszvb_LoadAndInterchangeSingleEndedPortCircuitModelData  = prototype(('rszvb_LoadAndInterchangeSingleEndedPortCircuitModelData', rszvbDLL), paramflags)
rszvb_LoadAndInterchangeSingleEndedPortCircuitModelData.name = 'rszvb_LoadAndInterchangeSingleEndedPortCircuitModelData'
rszvb_LoadAndInterchangeSingleEndedPortCircuitModelData.errcheck = __errorcheck__
rszvb_LoadAndInterchangeSingleEndedPortCircuitModelData.output = False
# rszvb_SetVirtualTransformGroundLoopState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'state'),)
rszvb_SetVirtualTransformGroundLoopState  = prototype(('rszvb_SetVirtualTransformGroundLoopState', rszvbDLL), paramflags)
rszvb_SetVirtualTransformGroundLoopState.name = 'rszvb_SetVirtualTransformGroundLoopState'
rszvb_SetVirtualTransformGroundLoopState.errcheck = __errorcheck__
rszvb_SetVirtualTransformGroundLoopState.output = False
# rszvb_GetVirtualTransformGroundLoopState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(2, 'state'),)
rszvb_GetVirtualTransformGroundLoopState  = prototype(('rszvb_GetVirtualTransformGroundLoopState', rszvbDLL), paramflags)
rszvb_GetVirtualTransformGroundLoopState.name = 'rszvb_GetVirtualTransformGroundLoopState'
rszvb_GetVirtualTransformGroundLoopState.errcheck = __errorcheck__
rszvb_GetVirtualTransformGroundLoopState.output = True
# rszvb_SetVirtualTransformGroundLoop ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 parameterType', 'ViInt32 circuitModel', 'ViReal64 groundLoopValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'parameterType'),(1, 'circuitModel'),(1, 'groundLoopValue'),)
rszvb_SetVirtualTransformGroundLoop  = prototype(('rszvb_SetVirtualTransformGroundLoop', rszvbDLL), paramflags)
rszvb_SetVirtualTransformGroundLoop.name = 'rszvb_SetVirtualTransformGroundLoop'
rszvb_SetVirtualTransformGroundLoop.errcheck = __errorcheck__
rszvb_SetVirtualTransformGroundLoop.output = False
# rszvb_GetVirtualTransformGroundLoop ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 parameterType', 'ViInt32 circuitModel', 'ViReal64* groundLoopValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'parameterType'),(1, 'circuitModel'),(2, 'groundLoopValue'),)
rszvb_GetVirtualTransformGroundLoop  = prototype(('rszvb_GetVirtualTransformGroundLoop', rszvbDLL), paramflags)
rszvb_GetVirtualTransformGroundLoop.name = 'rszvb_GetVirtualTransformGroundLoop'
rszvb_GetVirtualTransformGroundLoop.errcheck = __errorcheck__
rszvb_GetVirtualTransformGroundLoop.output = True
# rszvb_SetVirtualTransformGroundLoopCircuitModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 circuitModel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'circuitModel'),)
rszvb_SetVirtualTransformGroundLoopCircuitModel  = prototype(('rszvb_SetVirtualTransformGroundLoopCircuitModel', rszvbDLL), paramflags)
rszvb_SetVirtualTransformGroundLoopCircuitModel.name = 'rszvb_SetVirtualTransformGroundLoopCircuitModel'
rszvb_SetVirtualTransformGroundLoopCircuitModel.errcheck = __errorcheck__
rszvb_SetVirtualTransformGroundLoopCircuitModel.output = False
# rszvb_GetVirtualTransformGroundLoopCircuitModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32* circuitModel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(2, 'circuitModel'),)
rszvb_GetVirtualTransformGroundLoopCircuitModel  = prototype(('rszvb_GetVirtualTransformGroundLoopCircuitModel', rszvbDLL), paramflags)
rszvb_GetVirtualTransformGroundLoopCircuitModel.name = 'rszvb_GetVirtualTransformGroundLoopCircuitModel'
rszvb_GetVirtualTransformGroundLoopCircuitModel.errcheck = __errorcheck__
rszvb_GetVirtualTransformGroundLoopCircuitModel.output = True
# rszvb_LoadGroundLoopCircuitModelData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'fileName'),)
rszvb_LoadGroundLoopCircuitModelData  = prototype(('rszvb_LoadGroundLoopCircuitModelData', rszvbDLL), paramflags)
rszvb_LoadGroundLoopCircuitModelData.name = 'rszvb_LoadGroundLoopCircuitModelData'
rszvb_LoadGroundLoopCircuitModelData.errcheck = __errorcheck__
rszvb_LoadGroundLoopCircuitModelData.output = False
# rszvb_SetVirtualTransformPortPairState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 portPair', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'portPair'),(1, 'state'),)
rszvb_SetVirtualTransformPortPairState  = prototype(('rszvb_SetVirtualTransformPortPairState', rszvbDLL), paramflags)
rszvb_SetVirtualTransformPortPairState.name = 'rszvb_SetVirtualTransformPortPairState'
rszvb_SetVirtualTransformPortPairState.errcheck = __errorcheck__
rszvb_SetVirtualTransformPortPairState.output = False
# rszvb_GetVirtualTransformPortPairState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 portPair', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'portPair'),(2, 'state'),)
rszvb_GetVirtualTransformPortPairState  = prototype(('rszvb_GetVirtualTransformPortPairState', rszvbDLL), paramflags)
rszvb_GetVirtualTransformPortPairState.name = 'rszvb_GetVirtualTransformPortPairState'
rszvb_GetVirtualTransformPortPairState.errcheck = __errorcheck__
rszvb_GetVirtualTransformPortPairState.output = True
# rszvb_SetVirtualTransformPortPair ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 portPair', 'ViInt32 parameterType', 'ViInt32 parameterNumber', 'ViInt32 circuitModel', 'ViReal64 value']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'portPair'),(1, 'parameterType'),(1, 'parameterNumber'),(1, 'circuitModel'),(1, 'value'),)
rszvb_SetVirtualTransformPortPair  = prototype(('rszvb_SetVirtualTransformPortPair', rszvbDLL), paramflags)
rszvb_SetVirtualTransformPortPair.name = 'rszvb_SetVirtualTransformPortPair'
rszvb_SetVirtualTransformPortPair.errcheck = __errorcheck__
rszvb_SetVirtualTransformPortPair.output = False
# rszvb_GetVirtualTransformPortPair ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 portPair', 'ViInt32 parameterType', 'ViInt32 parameterNumber', 'ViInt32 circuitModel', 'ViReal64* value']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'portPair'),(1, 'parameterType'),(1, 'parameterNumber'),(1, 'circuitModel'),(2, 'value'),)
rszvb_GetVirtualTransformPortPair  = prototype(('rszvb_GetVirtualTransformPortPair', rszvbDLL), paramflags)
rszvb_GetVirtualTransformPortPair.name = 'rszvb_GetVirtualTransformPortPair'
rszvb_GetVirtualTransformPortPair.errcheck = __errorcheck__
rszvb_GetVirtualTransformPortPair.output = True
# rszvb_SetVirtualTransformPortPairCircuitModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 portPair', 'ViInt32 circuitModel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'portPair'),(1, 'circuitModel'),)
rszvb_SetVirtualTransformPortPairCircuitModel  = prototype(('rszvb_SetVirtualTransformPortPairCircuitModel', rszvbDLL), paramflags)
rszvb_SetVirtualTransformPortPairCircuitModel.name = 'rszvb_SetVirtualTransformPortPairCircuitModel'
rszvb_SetVirtualTransformPortPairCircuitModel.errcheck = __errorcheck__
rszvb_SetVirtualTransformPortPairCircuitModel.output = False
# rszvb_GetVirtualTransformPortPairCircuitModel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 portPair', 'ViInt32* circuitModel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'portPair'),(2, 'circuitModel'),)
rszvb_GetVirtualTransformPortPairCircuitModel  = prototype(('rszvb_GetVirtualTransformPortPairCircuitModel', rszvbDLL), paramflags)
rszvb_GetVirtualTransformPortPairCircuitModel.name = 'rszvb_GetVirtualTransformPortPairCircuitModel'
rszvb_GetVirtualTransformPortPairCircuitModel.errcheck = __errorcheck__
rszvb_GetVirtualTransformPortPairCircuitModel.output = True
# rszvb_LoadPortPairCircuitModelData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 functionType', 'ViInt32 portPair', 'ViString fileName', 'ViInt32 parameter', 'ViBoolean interchangePortNumbers']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'functionType'),(1, 'portPair'),(1, 'fileName'),(1, 'parameter'),(1, 'interchangePortNumbers'),)
rszvb_LoadPortPairCircuitModelData  = prototype(('rszvb_LoadPortPairCircuitModelData', rszvbDLL), paramflags)
rszvb_LoadPortPairCircuitModelData.name = 'rszvb_LoadPortPairCircuitModelData'
rszvb_LoadPortPairCircuitModelData.errcheck = __errorcheck__
rszvb_LoadPortPairCircuitModelData.output = False
# rszvb_SetCoherentSignalState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean coherentSignal']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'coherentSignal'),)
rszvb_SetCoherentSignalState  = prototype(('rszvb_SetCoherentSignalState', rszvbDLL), paramflags)
rszvb_SetCoherentSignalState.name = 'rszvb_SetCoherentSignalState'
rszvb_SetCoherentSignalState.errcheck = __errorcheck__
rszvb_SetCoherentSignalState.output = False
# rszvb_GetCoherentSignalState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* coherentSignal']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'coherentSignal'),)
rszvb_GetCoherentSignalState  = prototype(('rszvb_GetCoherentSignalState', rszvbDLL), paramflags)
rszvb_GetCoherentSignalState.name = 'rszvb_GetCoherentSignalState'
rszvb_GetCoherentSignalState.errcheck = __errorcheck__
rszvb_GetCoherentSignalState.output = True
# rszvb_SetCoherentSignalAmplitude ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 amplitude']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'amplitude'),)
rszvb_SetCoherentSignalAmplitude  = prototype(('rszvb_SetCoherentSignalAmplitude', rszvbDLL), paramflags)
rszvb_SetCoherentSignalAmplitude.name = 'rszvb_SetCoherentSignalAmplitude'
rszvb_SetCoherentSignalAmplitude.errcheck = __errorcheck__
rszvb_SetCoherentSignalAmplitude.output = False
# rszvb_GetCoherentSignalAmplitude ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* amplitude']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'amplitude'),)
rszvb_GetCoherentSignalAmplitude  = prototype(('rszvb_GetCoherentSignalAmplitude', rszvbDLL), paramflags)
rszvb_GetCoherentSignalAmplitude.name = 'rszvb_GetCoherentSignalAmplitude'
rszvb_GetCoherentSignalAmplitude.errcheck = __errorcheck__
rszvb_GetCoherentSignalAmplitude.output = True
# rszvb_SetCoherentSignalPhase ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 phase']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'phase'),)
rszvb_SetCoherentSignalPhase  = prototype(('rszvb_SetCoherentSignalPhase', rszvbDLL), paramflags)
rszvb_SetCoherentSignalPhase.name = 'rszvb_SetCoherentSignalPhase'
rszvb_SetCoherentSignalPhase.errcheck = __errorcheck__
rszvb_SetCoherentSignalPhase.output = False
# rszvb_GetCoherentSignalPhase ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* phase']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'phase'),)
rszvb_GetCoherentSignalPhase  = prototype(('rszvb_GetCoherentSignalPhase', rszvbDLL), paramflags)
rszvb_GetCoherentSignalPhase.name = 'rszvb_GetCoherentSignalPhase'
rszvb_GetCoherentSignalPhase.errcheck = __errorcheck__
rszvb_GetCoherentSignalPhase.output = True
# rszvb_SetCoherentSignalReferencePort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 referencePort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'referencePort'),)
rszvb_SetCoherentSignalReferencePort  = prototype(('rszvb_SetCoherentSignalReferencePort', rszvbDLL), paramflags)
rszvb_SetCoherentSignalReferencePort.name = 'rszvb_SetCoherentSignalReferencePort'
rszvb_SetCoherentSignalReferencePort.errcheck = __errorcheck__
rszvb_SetCoherentSignalReferencePort.output = False
# rszvb_GetCoherentSignalReferencePort ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* referencePort']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'referencePort'),)
rszvb_GetCoherentSignalReferencePort  = prototype(('rszvb_GetCoherentSignalReferencePort', rszvbDLL), paramflags)
rszvb_GetCoherentSignalReferencePort.name = 'rszvb_GetCoherentSignalReferencePort'
rszvb_GetCoherentSignalReferencePort.errcheck = __errorcheck__
rszvb_GetCoherentSignalReferencePort.output = True
# rszvb_SetAlternateSweepMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 alternateSweepMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'alternateSweepMode'),)
rszvb_SetAlternateSweepMode  = prototype(('rszvb_SetAlternateSweepMode', rszvbDLL), paramflags)
rszvb_SetAlternateSweepMode.name = 'rszvb_SetAlternateSweepMode'
rszvb_SetAlternateSweepMode.errcheck = __errorcheck__
rszvb_SetAlternateSweepMode.output = False
# rszvb_GetAlternateSweepMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* alternateSweepMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'alternateSweepMode'),)
rszvb_GetAlternateSweepMode  = prototype(('rszvb_GetAlternateSweepMode', rszvbDLL), paramflags)
rszvb_GetAlternateSweepMode.name = 'rszvb_GetAlternateSweepMode'
rszvb_GetAlternateSweepMode.errcheck = __errorcheck__
rszvb_GetAlternateSweepMode.output = True
# rszvb_SetSpuriousAvoidance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 spuriousAvoidance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'spuriousAvoidance'),)
rszvb_SetSpuriousAvoidance  = prototype(('rszvb_SetSpuriousAvoidance', rszvbDLL), paramflags)
rszvb_SetSpuriousAvoidance.name = 'rszvb_SetSpuriousAvoidance'
rszvb_SetSpuriousAvoidance.errcheck = __errorcheck__
rszvb_SetSpuriousAvoidance.output = False
# rszvb_GetSpuriousAvoidance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* spuriousAvoidance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'spuriousAvoidance'),)
rszvb_GetSpuriousAvoidance  = prototype(('rszvb_GetSpuriousAvoidance', rszvbDLL), paramflags)
rszvb_GetSpuriousAvoidance.name = 'rszvb_GetSpuriousAvoidance'
rszvb_GetSpuriousAvoidance.errcheck = __errorcheck__
rszvb_GetSpuriousAvoidance.output = True
# rszvb_SetAutomaticLevelControlState ['ViSession instrumentHandle', 'ViBoolean ALCState']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'ALCState'),)
rszvb_SetAutomaticLevelControlState  = prototype(('rszvb_SetAutomaticLevelControlState', rszvbDLL), paramflags)
rszvb_SetAutomaticLevelControlState.name = 'rszvb_SetAutomaticLevelControlState'
rszvb_SetAutomaticLevelControlState.errcheck = __errorcheck__
rszvb_SetAutomaticLevelControlState.output = False
# rszvb_GetAutomaticLevelControlState ['ViSession instrumentHandle', 'ViBoolean* ALCState']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'ALCState'),)
rszvb_GetAutomaticLevelControlState  = prototype(('rszvb_GetAutomaticLevelControlState', rszvbDLL), paramflags)
rszvb_GetAutomaticLevelControlState.name = 'rszvb_GetAutomaticLevelControlState'
rszvb_GetAutomaticLevelControlState.errcheck = __errorcheck__
rszvb_GetAutomaticLevelControlState.output = True
# rszvb_SetIndividualALCPortState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'state'),)
rszvb_SetIndividualALCPortState  = prototype(('rszvb_SetIndividualALCPortState', rszvbDLL), paramflags)
rszvb_SetIndividualALCPortState.name = 'rszvb_SetIndividualALCPortState'
rszvb_SetIndividualALCPortState.errcheck = __errorcheck__
rszvb_SetIndividualALCPortState.output = False
# rszvb_GetIndividualALCPortState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'state'),)
rszvb_GetIndividualALCPortState  = prototype(('rszvb_GetIndividualALCPortState', rszvbDLL), paramflags)
rszvb_GetIndividualALCPortState.name = 'rszvb_GetIndividualALCPortState'
rszvb_GetIndividualALCPortState.errcheck = __errorcheck__
rszvb_GetIndividualALCPortState.output = True
# rszvb_SetALCPortState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'state'),)
rszvb_SetALCPortState  = prototype(('rszvb_SetALCPortState', rszvbDLL), paramflags)
rszvb_SetALCPortState.name = 'rszvb_SetALCPortState'
rszvb_SetALCPortState.errcheck = __errorcheck__
rszvb_SetALCPortState.output = False
# rszvb_GetALCPortState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'state'),)
rszvb_GetALCPortState  = prototype(('rszvb_GetALCPortState', rszvbDLL), paramflags)
rszvb_GetALCPortState.name = 'rszvb_GetALCPortState'
rszvb_GetALCPortState.errcheck = __errorcheck__
rszvb_GetALCPortState.output = True
# rszvb_SetALCPortClamp ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean clampState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'clampState'),)
rszvb_SetALCPortClamp  = prototype(('rszvb_SetALCPortClamp', rszvbDLL), paramflags)
rszvb_SetALCPortClamp.name = 'rszvb_SetALCPortClamp'
rszvb_SetALCPortClamp.errcheck = __errorcheck__
rszvb_SetALCPortClamp.output = False
# rszvb_GetALCPortClamp ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* clampState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'clampState'),)
rszvb_GetALCPortClamp  = prototype(('rszvb_GetALCPortClamp', rszvbDLL), paramflags)
rszvb_GetALCPortClamp.name = 'rszvb_GetALCPortClamp'
rszvb_GetALCPortClamp.errcheck = __errorcheck__
rszvb_GetALCPortClamp.output = True
# rszvb_SetALCPortAUBWState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'state'),)
rszvb_SetALCPortAUBWState  = prototype(('rszvb_SetALCPortAUBWState', rszvbDLL), paramflags)
rszvb_SetALCPortAUBWState.name = 'rszvb_SetALCPortAUBWState'
rszvb_SetALCPortAUBWState.errcheck = __errorcheck__
rszvb_SetALCPortAUBWState.output = False
# rszvb_GetALCPortAUBWState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'state'),)
rszvb_GetALCPortAUBWState  = prototype(('rszvb_GetALCPortAUBWState', rszvbDLL), paramflags)
rszvb_GetALCPortAUBWState.name = 'rszvb_GetALCPortAUBWState'
rszvb_GetALCPortAUBWState.errcheck = __errorcheck__
rszvb_GetALCPortAUBWState.output = True
# rszvb_SetALCPortBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 bandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'bandwidth'),)
rszvb_SetALCPortBandwidth  = prototype(('rszvb_SetALCPortBandwidth', rszvbDLL), paramflags)
rszvb_SetALCPortBandwidth.name = 'rszvb_SetALCPortBandwidth'
rszvb_SetALCPortBandwidth.errcheck = __errorcheck__
rszvb_SetALCPortBandwidth.output = False
# rszvb_GetALCPortBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* bandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'bandwidth'),)
rszvb_GetALCPortBandwidth  = prototype(('rszvb_GetALCPortBandwidth', rszvbDLL), paramflags)
rszvb_GetALCPortBandwidth.name = 'rszvb_GetALCPortBandwidth'
rszvb_GetALCPortBandwidth.errcheck = __errorcheck__
rszvb_GetALCPortBandwidth.output = True
# rszvb_SetALCPortCoupling ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetALCPortCoupling  = prototype(('rszvb_SetALCPortCoupling', rszvbDLL), paramflags)
rszvb_SetALCPortCoupling.name = 'rszvb_SetALCPortCoupling'
rszvb_SetALCPortCoupling.errcheck = __errorcheck__
rszvb_SetALCPortCoupling.output = False
# rszvb_GetALCPortCoupling ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetALCPortCoupling  = prototype(('rszvb_GetALCPortCoupling', rszvbDLL), paramflags)
rszvb_GetALCPortCoupling.name = 'rszvb_GetALCPortCoupling'
rszvb_GetALCPortCoupling.errcheck = __errorcheck__
rszvb_GetALCPortCoupling.output = True
# rszvb_SetALCChannelState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetALCChannelState  = prototype(('rszvb_SetALCChannelState', rszvbDLL), paramflags)
rszvb_SetALCChannelState.name = 'rszvb_SetALCChannelState'
rszvb_SetALCChannelState.errcheck = __errorcheck__
rszvb_SetALCChannelState.output = False
# rszvb_GetALCChannelState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetALCChannelState  = prototype(('rszvb_GetALCChannelState', rszvbDLL), paramflags)
rszvb_GetALCChannelState.name = 'rszvb_GetALCChannelState'
rszvb_GetALCChannelState.errcheck = __errorcheck__
rszvb_GetALCChannelState.output = True
# rszvb_SetALCLowPhaseNoiseMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetALCLowPhaseNoiseMode  = prototype(('rszvb_SetALCLowPhaseNoiseMode', rszvbDLL), paramflags)
rszvb_SetALCLowPhaseNoiseMode.name = 'rszvb_SetALCLowPhaseNoiseMode'
rszvb_SetALCLowPhaseNoiseMode.errcheck = __errorcheck__
rszvb_SetALCLowPhaseNoiseMode.output = False
# rszvb_GetALCLowPhaseNoiseMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetALCLowPhaseNoiseMode  = prototype(('rszvb_GetALCLowPhaseNoiseMode', rszvbDLL), paramflags)
rszvb_GetALCLowPhaseNoiseMode.name = 'rszvb_GetALCLowPhaseNoiseMode'
rszvb_GetALCLowPhaseNoiseMode.errcheck = __errorcheck__
rszvb_GetALCLowPhaseNoiseMode.output = True
# rszvb_SetALCPortOffsetState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'state'),)
rszvb_SetALCPortOffsetState  = prototype(('rszvb_SetALCPortOffsetState', rszvbDLL), paramflags)
rszvb_SetALCPortOffsetState.name = 'rszvb_SetALCPortOffsetState'
rszvb_SetALCPortOffsetState.errcheck = __errorcheck__
rszvb_SetALCPortOffsetState.output = False
# rszvb_GetALCPortOffsetState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'state'),)
rszvb_GetALCPortOffsetState  = prototype(('rszvb_GetALCPortOffsetState', rszvbDLL), paramflags)
rszvb_GetALCPortOffsetState.name = 'rszvb_GetALCPortOffsetState'
rszvb_GetALCPortOffsetState.errcheck = __errorcheck__
rszvb_GetALCPortOffsetState.output = True
# rszvb_SetALCPortControlRange ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 controlRange']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'controlRange'),)
rszvb_SetALCPortControlRange  = prototype(('rszvb_SetALCPortControlRange', rszvbDLL), paramflags)
rszvb_SetALCPortControlRange.name = 'rszvb_SetALCPortControlRange'
rszvb_SetALCPortControlRange.errcheck = __errorcheck__
rszvb_SetALCPortControlRange.output = False
# rszvb_GetALCPortControlRange ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* controlRange']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'controlRange'),)
rszvb_GetALCPortControlRange  = prototype(('rszvb_GetALCPortControlRange', rszvbDLL), paramflags)
rszvb_GetALCPortControlRange.name = 'rszvb_GetALCPortControlRange'
rszvb_GetALCPortControlRange.errcheck = __errorcheck__
rszvb_GetALCPortControlRange.output = True
# rszvb_SetALCPortStartOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 startOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'startOffset'),)
rszvb_SetALCPortStartOffset  = prototype(('rszvb_SetALCPortStartOffset', rszvbDLL), paramflags)
rszvb_SetALCPortStartOffset.name = 'rszvb_SetALCPortStartOffset'
rszvb_SetALCPortStartOffset.errcheck = __errorcheck__
rszvb_SetALCPortStartOffset.output = False
# rszvb_GetALCPortStartOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* startOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'startOffset'),)
rszvb_GetALCPortStartOffset  = prototype(('rszvb_GetALCPortStartOffset', rszvbDLL), paramflags)
rszvb_GetALCPortStartOffset.name = 'rszvb_GetALCPortStartOffset'
rszvb_GetALCPortStartOffset.errcheck = __errorcheck__
rszvb_GetALCPortStartOffset.output = True
# rszvb_SetALCPortSettingTolerance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 settingTolerance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'settingTolerance'),)
rszvb_SetALCPortSettingTolerance  = prototype(('rszvb_SetALCPortSettingTolerance', rszvbDLL), paramflags)
rszvb_SetALCPortSettingTolerance.name = 'rszvb_SetALCPortSettingTolerance'
rszvb_SetALCPortSettingTolerance.errcheck = __errorcheck__
rszvb_SetALCPortSettingTolerance.output = False
# rszvb_GetALCPortSettingTolerance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* settingTolerance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'settingTolerance'),)
rszvb_GetALCPortSettingTolerance  = prototype(('rszvb_GetALCPortSettingTolerance', rszvbDLL), paramflags)
rszvb_GetALCPortSettingTolerance.name = 'rszvb_GetALCPortSettingTolerance'
rszvb_GetALCPortSettingTolerance.errcheck = __errorcheck__
rszvb_GetALCPortSettingTolerance.output = True
# rszvb_SetLowPhaseNoiseState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean lowPhaseNoiseState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'lowPhaseNoiseState'),)
rszvb_SetLowPhaseNoiseState  = prototype(('rszvb_SetLowPhaseNoiseState', rszvbDLL), paramflags)
rszvb_SetLowPhaseNoiseState.name = 'rszvb_SetLowPhaseNoiseState'
rszvb_SetLowPhaseNoiseState.errcheck = __errorcheck__
rszvb_SetLowPhaseNoiseState.output = False
# rszvb_GetLowPhaseNoiseState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* lowPhaseNoiseState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'lowPhaseNoiseState'),)
rszvb_GetLowPhaseNoiseState  = prototype(('rszvb_GetLowPhaseNoiseState', rszvbDLL), paramflags)
rszvb_GetLowPhaseNoiseState.name = 'rszvb_GetLowPhaseNoiseState'
rszvb_GetLowPhaseNoiseState.errcheck = __errorcheck__
rszvb_GetLowPhaseNoiseState.output = True
# rszvb_ConfigurePortPIController ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 PIControllerMode', 'ViReal64 gain', 'ViReal64 integrationTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'PIControllerMode'),(1, 'gain'),(1, 'integrationTime'),)
rszvb_ConfigurePortPIController  = prototype(('rszvb_ConfigurePortPIController', rszvbDLL), paramflags)
rszvb_ConfigurePortPIController.name = 'rszvb_ConfigurePortPIController'
rszvb_ConfigurePortPIController.errcheck = __errorcheck__
rszvb_ConfigurePortPIController.output = False
# rszvb_ConfigureSAWMatchingNetwork ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean apply', 'ViReal64 parallelL', 'ViReal64 serialC', 'ViReal64 differentialModeImpedance', 'ViReal64 commonModeImpedance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool,c_double,c_double,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'apply'),(1, 'parallelL'),(1, 'serialC'),(1, 'differentialModeImpedance'),(1, 'commonModeImpedance'),)
rszvb_ConfigureSAWMatchingNetwork  = prototype(('rszvb_ConfigureSAWMatchingNetwork', rszvbDLL), paramflags)
rszvb_ConfigureSAWMatchingNetwork.name = 'rszvb_ConfigureSAWMatchingNetwork'
rszvb_ConfigureSAWMatchingNetwork.errcheck = __errorcheck__
rszvb_ConfigureSAWMatchingNetwork.output = False
# rszvb_SetSAWState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean apply']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'apply'),)
rszvb_SetSAWState  = prototype(('rszvb_SetSAWState', rszvbDLL), paramflags)
rszvb_SetSAWState.name = 'rszvb_SetSAWState'
rszvb_SetSAWState.errcheck = __errorcheck__
rszvb_SetSAWState.output = False
# rszvb_GetSAWState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* apply']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'apply'),)
rszvb_GetSAWState  = prototype(('rszvb_GetSAWState', rszvbDLL), paramflags)
rszvb_GetSAWState.name = 'rszvb_GetSAWState'
rszvb_GetSAWState.errcheck = __errorcheck__
rszvb_GetSAWState.output = True
# rszvb_SetSAWParallelL ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 parallelL']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'parallelL'),)
rszvb_SetSAWParallelL  = prototype(('rszvb_SetSAWParallelL', rszvbDLL), paramflags)
rszvb_SetSAWParallelL.name = 'rszvb_SetSAWParallelL'
rszvb_SetSAWParallelL.errcheck = __errorcheck__
rszvb_SetSAWParallelL.output = False
# rszvb_GetSAWParallelL ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* parallelL']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'parallelL'),)
rszvb_GetSAWParallelL  = prototype(('rszvb_GetSAWParallelL', rszvbDLL), paramflags)
rszvb_GetSAWParallelL.name = 'rszvb_GetSAWParallelL'
rszvb_GetSAWParallelL.errcheck = __errorcheck__
rszvb_GetSAWParallelL.output = True
# rszvb_SetSAWSerialC ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 serialC']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'serialC'),)
rszvb_SetSAWSerialC  = prototype(('rszvb_SetSAWSerialC', rszvbDLL), paramflags)
rszvb_SetSAWSerialC.name = 'rszvb_SetSAWSerialC'
rszvb_SetSAWSerialC.errcheck = __errorcheck__
rszvb_SetSAWSerialC.output = False
# rszvb_GetSAWSerialC ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* serialC']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'serialC'),)
rszvb_GetSAWSerialC  = prototype(('rszvb_GetSAWSerialC', rszvbDLL), paramflags)
rszvb_GetSAWSerialC.name = 'rszvb_GetSAWSerialC'
rszvb_GetSAWSerialC.errcheck = __errorcheck__
rszvb_GetSAWSerialC.output = True
# rszvb_SetSAWSimulationType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 type']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'type'),)
rszvb_SetSAWSimulationType  = prototype(('rszvb_SetSAWSimulationType', rszvbDLL), paramflags)
rszvb_SetSAWSimulationType.name = 'rszvb_SetSAWSimulationType'
rszvb_SetSAWSimulationType.errcheck = __errorcheck__
rszvb_SetSAWSimulationType.output = False
# rszvb_GetSAWSimulationType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* type']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'type'),)
rszvb_GetSAWSimulationType  = prototype(('rszvb_GetSAWSimulationType', rszvbDLL), paramflags)
rszvb_GetSAWSimulationType.name = 'rszvb_GetSAWSimulationType'
rszvb_GetSAWSimulationType.errcheck = __errorcheck__
rszvb_GetSAWSimulationType.output = True
# rszvb_SetPIControllerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 PIControllerMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'PIControllerMode'),)
rszvb_SetPIControllerMode  = prototype(('rszvb_SetPIControllerMode', rszvbDLL), paramflags)
rszvb_SetPIControllerMode.name = 'rszvb_SetPIControllerMode'
rszvb_SetPIControllerMode.errcheck = __errorcheck__
rszvb_SetPIControllerMode.output = False
# rszvb_GetPIControllerMode ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* PIControllerMode']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'PIControllerMode'),)
rszvb_GetPIControllerMode  = prototype(('rszvb_GetPIControllerMode', rszvbDLL), paramflags)
rszvb_GetPIControllerMode.name = 'rszvb_GetPIControllerMode'
rszvb_GetPIControllerMode.errcheck = __errorcheck__
rszvb_GetPIControllerMode.output = True
# rszvb_SetPIControllerGain ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 gain']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'gain'),)
rszvb_SetPIControllerGain  = prototype(('rszvb_SetPIControllerGain', rszvbDLL), paramflags)
rszvb_SetPIControllerGain.name = 'rszvb_SetPIControllerGain'
rszvb_SetPIControllerGain.errcheck = __errorcheck__
rszvb_SetPIControllerGain.output = False
# rszvb_GetPIControllerGain ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* gain']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'gain'),)
rszvb_GetPIControllerGain  = prototype(('rszvb_GetPIControllerGain', rszvbDLL), paramflags)
rszvb_GetPIControllerGain.name = 'rszvb_GetPIControllerGain'
rszvb_GetPIControllerGain.errcheck = __errorcheck__
rszvb_GetPIControllerGain.output = True
# rszvb_SetPIControllerIntegrationTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 integrationTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'integrationTime'),)
rszvb_SetPIControllerIntegrationTime  = prototype(('rszvb_SetPIControllerIntegrationTime', rszvbDLL), paramflags)
rszvb_SetPIControllerIntegrationTime.name = 'rszvb_SetPIControllerIntegrationTime'
rszvb_SetPIControllerIntegrationTime.errcheck = __errorcheck__
rszvb_SetPIControllerIntegrationTime.output = False
# rszvb_GetPIControllerIntegrationTime ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* integrationTime']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'integrationTime'),)
rszvb_GetPIControllerIntegrationTime  = prototype(('rszvb_GetPIControllerIntegrationTime', rszvbDLL), paramflags)
rszvb_GetPIControllerIntegrationTime.name = 'rszvb_GetPIControllerIntegrationTime'
rszvb_GetPIControllerIntegrationTime.errcheck = __errorcheck__
rszvb_GetPIControllerIntegrationTime.output = True
# rszvb_ChannelAdd ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString channelName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'channelName'),)
rszvb_ChannelAdd  = prototype(('rszvb_ChannelAdd', rszvbDLL), paramflags)
rszvb_ChannelAdd.name = 'rszvb_ChannelAdd'
rszvb_ChannelAdd.errcheck = __errorcheck__
rszvb_ChannelAdd.output = False
# rszvb_ChannelAddTrace ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViInt32 channel', 'ViString channelName', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'channel',1),(1, 'channelName'),(1, 'traceName'),)
rszvb_ChannelAddTrace  = prototype(('rszvb_ChannelAddTrace', rszvbDLL), paramflags)
rszvb_ChannelAddTrace.name = 'rszvb_ChannelAddTrace'
rszvb_ChannelAddTrace.errcheck = __errorcheck__
rszvb_ChannelAddTrace.output = False
# rszvb_ChannelAddTraceDiagramArea ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 window_Trace', 'ViInt32 channel', 'ViString channelName', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'window_Trace'),(1, 'channel',1),(1, 'channelName'),(1, 'traceName'),)
rszvb_ChannelAddTraceDiagramArea  = prototype(('rszvb_ChannelAddTraceDiagramArea', rszvbDLL), paramflags)
rszvb_ChannelAddTraceDiagramArea.name = 'rszvb_ChannelAddTraceDiagramArea'
rszvb_ChannelAddTraceDiagramArea.errcheck = __errorcheck__
rszvb_ChannelAddTraceDiagramArea.output = False
# rszvb_ChannelDelete ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_ChannelDelete  = prototype(('rszvb_ChannelDelete', rszvbDLL), paramflags)
rszvb_ChannelDelete.name = 'rszvb_ChannelDelete'
rszvb_ChannelDelete.errcheck = __errorcheck__
rszvb_ChannelDelete.output = False
# rszvb_ChannelList ['ViSession instrumentHandle', 'ViChar _VI_FAR catalog[]', 'ViInt32 bufferSize']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'catalog[]'),(1, 'bufferSize'),)
rszvb_ChannelList  = prototype(('rszvb_ChannelList', rszvbDLL), paramflags)
rszvb_ChannelList.name = 'rszvb_ChannelList'
rszvb_ChannelList.errcheck = __errorcheck__
rszvb_ChannelList.output = False
# rszvb_ChannelGetChannelName ['ViSession instrumentHandle', 'ViInt32 channel', 'ViChar _VI_FAR channelName[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'channelName[]'),)
rszvb_ChannelGetChannelName  = prototype(('rszvb_ChannelGetChannelName', rszvbDLL), paramflags)
rszvb_ChannelGetChannelName.name = 'rszvb_ChannelGetChannelName'
rszvb_ChannelGetChannelName.errcheck = __errorcheck__
rszvb_ChannelGetChannelName.output = False
# rszvb_ChannelGetChannelNumber ['ViSession instrumentHandle', 'ViString channelName', 'ViInt32* channelNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channelName'),(2, 'channelNumber'),)
rszvb_ChannelGetChannelNumber  = prototype(('rszvb_ChannelGetChannelNumber', rszvbDLL), paramflags)
rszvb_ChannelGetChannelNumber.name = 'rszvb_ChannelGetChannelNumber'
rszvb_ChannelGetChannelNumber.errcheck = __errorcheck__
rszvb_ChannelGetChannelNumber.output = True
# rszvb_ChannelSetActive ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_ChannelSetActive  = prototype(('rszvb_ChannelSetActive', rszvbDLL), paramflags)
rszvb_ChannelSetActive.name = 'rszvb_ChannelSetActive'
rszvb_ChannelSetActive.errcheck = __errorcheck__
rszvb_ChannelSetActive.output = False
# rszvb_ChannelGetActive ['ViSession instrumentHandle', 'ViInt32* channel']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'channel'),)
rszvb_ChannelGetActive  = prototype(('rszvb_ChannelGetActive', rszvbDLL), paramflags)
rszvb_ChannelGetActive.name = 'rszvb_ChannelGetActive'
rszvb_ChannelGetActive.errcheck = __errorcheck__
rszvb_ChannelGetActive.output = True
# rszvb_ChannelRename ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString channelName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'channelName'),)
rszvb_ChannelRename  = prototype(('rszvb_ChannelRename', rszvbDLL), paramflags)
rszvb_ChannelRename.name = 'rszvb_ChannelRename'
rszvb_ChannelRename.errcheck = __errorcheck__
rszvb_ChannelRename.output = False
# rszvb_SetConnector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32 connector']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'connector'),)
rszvb_SetConnector  = prototype(('rszvb_SetConnector', rszvbDLL), paramflags)
rszvb_SetConnector.name = 'rszvb_SetConnector'
rszvb_SetConnector.errcheck = __errorcheck__
rszvb_SetConnector.output = False
# rszvb_GetConnector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViInt32* connector']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'connector'),)
rszvb_GetConnector  = prototype(('rszvb_GetConnector', rszvbDLL), paramflags)
rszvb_GetConnector.name = 'rszvb_GetConnector'
rszvb_GetConnector.errcheck = __errorcheck__
rszvb_GetConnector.output = True
# rszvb_SetSameConnectorTypeAtAllPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean sameConnectorAtAllPorts']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'sameConnectorAtAllPorts'),)
rszvb_SetSameConnectorTypeAtAllPorts  = prototype(('rszvb_SetSameConnectorTypeAtAllPorts', rszvbDLL), paramflags)
rszvb_SetSameConnectorTypeAtAllPorts.name = 'rszvb_SetSameConnectorTypeAtAllPorts'
rszvb_SetSameConnectorTypeAtAllPorts.errcheck = __errorcheck__
rszvb_SetSameConnectorTypeAtAllPorts.output = False
# rszvb_GetSameConnectorTypeAtAllPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* sameConnectorAtAllPorts']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'sameConnectorAtAllPorts'),)
rszvb_GetSameConnectorTypeAtAllPorts  = prototype(('rszvb_GetSameConnectorTypeAtAllPorts', rszvbDLL), paramflags)
rszvb_GetSameConnectorTypeAtAllPorts.name = 'rszvb_GetSameConnectorTypeAtAllPorts'
rszvb_GetSameConnectorTypeAtAllPorts.errcheck = __errorcheck__
rszvb_GetSameConnectorTypeAtAllPorts.output = True
# rszvb_SetSameConnectorGenderAtAllPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean sameGenderAtAllPorts']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'sameGenderAtAllPorts'),)
rszvb_SetSameConnectorGenderAtAllPorts  = prototype(('rszvb_SetSameConnectorGenderAtAllPorts', rszvbDLL), paramflags)
rszvb_SetSameConnectorGenderAtAllPorts.name = 'rszvb_SetSameConnectorGenderAtAllPorts'
rszvb_SetSameConnectorGenderAtAllPorts.errcheck = __errorcheck__
rszvb_SetSameConnectorGenderAtAllPorts.output = False
# rszvb_GetSameConnectorGenderAtAllPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* sameGenderAtAllPorts']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'sameGenderAtAllPorts'),)
rszvb_GetSameConnectorGenderAtAllPorts  = prototype(('rszvb_GetSameConnectorGenderAtAllPorts', rszvbDLL), paramflags)
rszvb_GetSameConnectorGenderAtAllPorts.name = 'rszvb_GetSameConnectorGenderAtAllPorts'
rszvb_GetSameConnectorGenderAtAllPorts.errcheck = __errorcheck__
rszvb_GetSameConnectorGenderAtAllPorts.output = True
# rszvb_SetUserConnector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViString connector', 'ViInt32 connectorGender']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'connector'),(1, 'connectorGender'),)
rszvb_SetUserConnector  = prototype(('rszvb_SetUserConnector', rszvbDLL), paramflags)
rszvb_SetUserConnector.name = 'rszvb_SetUserConnector'
rszvb_SetUserConnector.errcheck = __errorcheck__
rszvb_SetUserConnector.output = False
# rszvb_GetUserConnector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViChar _VI_FAR connector[]', 'ViInt32* connectorGender']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'connector[]'),(2, 'connectorGender'),)
rszvb_GetUserConnector  = prototype(('rszvb_GetUserConnector', rszvbDLL), paramflags)
rszvb_GetUserConnector.name = 'rszvb_GetUserConnector'
rszvb_GetUserConnector.errcheck = __errorcheck__
rszvb_GetUserConnector.output = True
# rszvb_SetSameSweepSetup ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean sameSweepSetup']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'sameSweepSetup'),)
rszvb_SetSameSweepSetup  = prototype(('rszvb_SetSameSweepSetup', rszvbDLL), paramflags)
rszvb_SetSameSweepSetup.name = 'rszvb_SetSameSweepSetup'
rszvb_SetSameSweepSetup.errcheck = __errorcheck__
rszvb_SetSameSweepSetup.output = False
# rszvb_GetSameSweepSetup ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* sameSweepSetup']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'sameSweepSetup'),)
rszvb_GetSameSweepSetup  = prototype(('rszvb_GetSameSweepSetup', rszvbDLL), paramflags)
rszvb_GetSameSweepSetup.name = 'rszvb_GetSameSweepSetup'
rszvb_GetSameSweepSetup.errcheck = __errorcheck__
rszvb_GetSameSweepSetup.output = True
# rszvb_SetSParameterDetector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 sParameterDetector']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'sParameterDetector'),)
rszvb_SetSParameterDetector  = prototype(('rszvb_SetSParameterDetector', rszvbDLL), paramflags)
rszvb_SetSParameterDetector.name = 'rszvb_SetSParameterDetector'
rszvb_SetSParameterDetector.errcheck = __errorcheck__
rszvb_SetSParameterDetector.output = False
# rszvb_GetSParameterDetector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* sParameterDetector']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'sParameterDetector'),)
rszvb_GetSParameterDetector  = prototype(('rszvb_GetSParameterDetector', rszvbDLL), paramflags)
rszvb_GetSParameterDetector.name = 'rszvb_GetSParameterDetector'
rszvb_GetSParameterDetector.errcheck = __errorcheck__
rszvb_GetSParameterDetector.output = True
# rszvb_SelectCalibrationType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString calibrationName', 'ViInt32 parameters', 'ViInt32 port1', 'ViInt32 port2', 'ViInt32 port3', 'ViInt32 port4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationName'),(1, 'parameters'),(1, 'port1'),(1, 'port2'),(1, 'port3'),(1, 'port4'),)
rszvb_SelectCalibrationType  = prototype(('rszvb_SelectCalibrationType', rszvbDLL), paramflags)
rszvb_SelectCalibrationType.name = 'rszvb_SelectCalibrationType'
rszvb_SelectCalibrationType.errcheck = __errorcheck__
rszvb_SelectCalibrationType.output = False
# rszvb_GetCalibrationType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* calibrationType', 'ViInt32* port1', 'ViInt32* port2', 'ViInt32* port3', 'ViInt32* port4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'calibrationType'),(2, 'port1'),(2, 'port2'),(2, 'port3'),(2, 'port4'),)
rszvb_GetCalibrationType  = prototype(('rszvb_GetCalibrationType', rszvbDLL), paramflags)
rszvb_GetCalibrationType.name = 'rszvb_GetCalibrationType'
rszvb_GetCalibrationType.errcheck = __errorcheck__
rszvb_GetCalibrationType.output = True
# rszvb_StartCalibration ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 standard', 'ViInt32 port1', 'ViInt32 port2']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'standard'),(1, 'port1'),(1, 'port2'),)
rszvb_StartCalibration  = prototype(('rszvb_StartCalibration', rszvbDLL), paramflags)
rszvb_StartCalibration.name = 'rszvb_StartCalibration'
rszvb_StartCalibration.errcheck = __errorcheck__
rszvb_StartCalibration.output = False
# rszvb_StartCalibrationLine ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 line', 'ViInt32 port1', 'ViInt32 port2']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'line'),(1, 'port1'),(1, 'port2'),)
rszvb_StartCalibrationLine  = prototype(('rszvb_StartCalibrationLine', rszvbDLL), paramflags)
rszvb_StartCalibrationLine.name = 'rszvb_StartCalibrationLine'
rszvb_StartCalibrationLine.errcheck = __errorcheck__
rszvb_StartCalibrationLine.output = False
# rszvb_StartCalibrationWithOptions ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 standard', 'ViInt32 port1', 'ViInt32 port2', 'ViBoolean dispersion', 'ViInt32 delayPhase', 'ViReal64 delayPhaseValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_bool,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'standard'),(1, 'port1'),(1, 'port2'),(1, 'dispersion'),(1, 'delayPhase'),(1, 'delayPhaseValue'),)
rszvb_StartCalibrationWithOptions  = prototype(('rszvb_StartCalibrationWithOptions', rszvbDLL), paramflags)
rszvb_StartCalibrationWithOptions.name = 'rszvb_StartCalibrationWithOptions'
rszvb_StartCalibrationWithOptions.errcheck = __errorcheck__
rszvb_StartCalibrationWithOptions.output = False
# rszvb_SetCalibrationReferencePlaneShift ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 referencePlaneShift']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'referencePlaneShift'),)
rszvb_SetCalibrationReferencePlaneShift  = prototype(('rszvb_SetCalibrationReferencePlaneShift', rszvbDLL), paramflags)
rszvb_SetCalibrationReferencePlaneShift.name = 'rszvb_SetCalibrationReferencePlaneShift'
rszvb_SetCalibrationReferencePlaneShift.errcheck = __errorcheck__
rszvb_SetCalibrationReferencePlaneShift.output = False
# rszvb_GetCalibrationReferencePlaneShift ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* referencePlaneShift']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'referencePlaneShift'),)
rszvb_GetCalibrationReferencePlaneShift  = prototype(('rszvb_GetCalibrationReferencePlaneShift', rszvbDLL), paramflags)
rszvb_GetCalibrationReferencePlaneShift.name = 'rszvb_GetCalibrationReferencePlaneShift'
rszvb_GetCalibrationReferencePlaneShift.errcheck = __errorcheck__
rszvb_GetCalibrationReferencePlaneShift.output = True
# rszvb_SetCalibrationReferencePlaneShiftSpecific ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 referencePlaneShift', 'ViString calibrationName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'referencePlaneShift'),(1, 'calibrationName'),)
rszvb_SetCalibrationReferencePlaneShiftSpecific  = prototype(('rszvb_SetCalibrationReferencePlaneShiftSpecific', rszvbDLL), paramflags)
rszvb_SetCalibrationReferencePlaneShiftSpecific.name = 'rszvb_SetCalibrationReferencePlaneShiftSpecific'
rszvb_SetCalibrationReferencePlaneShiftSpecific.errcheck = __errorcheck__
rszvb_SetCalibrationReferencePlaneShiftSpecific.output = False
# rszvb_GetCalibrationReferencePlaneShiftSpecific ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString calibrationName', 'ViReal64* referencePlaneShift']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationName'),(2, 'referencePlaneShift'),)
rszvb_GetCalibrationReferencePlaneShiftSpecific  = prototype(('rszvb_GetCalibrationReferencePlaneShiftSpecific', rszvbDLL), paramflags)
rszvb_GetCalibrationReferencePlaneShiftSpecific.name = 'rszvb_GetCalibrationReferencePlaneShiftSpecific'
rszvb_GetCalibrationReferencePlaneShiftSpecific.errcheck = __errorcheck__
rszvb_GetCalibrationReferencePlaneShiftSpecific.output = True
# rszvb_QueryCalibrationReferencePlaneShift ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationIndex', 'ViReal64* referencePlaneShift']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationIndex'),(2, 'referencePlaneShift'),)
rszvb_QueryCalibrationReferencePlaneShift  = prototype(('rszvb_QueryCalibrationReferencePlaneShift', rszvbDLL), paramflags)
rszvb_QueryCalibrationReferencePlaneShift.name = 'rszvb_QueryCalibrationReferencePlaneShift'
rszvb_QueryCalibrationReferencePlaneShift.errcheck = __errorcheck__
rszvb_QueryCalibrationReferencePlaneShift.output = True
# rszvb_SaveCalibrationData ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_SaveCalibrationData  = prototype(('rszvb_SaveCalibrationData', rszvbDLL), paramflags)
rszvb_SaveCalibrationData.name = 'rszvb_SaveCalibrationData'
rszvb_SaveCalibrationData.errcheck = __errorcheck__
rszvb_SaveCalibrationData.output = False
# rszvb_GenerateDefaultCalibrationData ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_GenerateDefaultCalibrationData  = prototype(('rszvb_GenerateDefaultCalibrationData', rszvbDLL), paramflags)
rszvb_GenerateDefaultCalibrationData.name = 'rszvb_GenerateDefaultCalibrationData'
rszvb_GenerateDefaultCalibrationData.errcheck = __errorcheck__
rszvb_GenerateDefaultCalibrationData.output = False
# rszvb_DeleteCalibrationData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString calibrationName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationName'),)
rszvb_DeleteCalibrationData  = prototype(('rszvb_DeleteCalibrationData', rszvbDLL), paramflags)
rszvb_DeleteCalibrationData.name = 'rszvb_DeleteCalibrationData'
rszvb_DeleteCalibrationData.errcheck = __errorcheck__
rszvb_DeleteCalibrationData.output = False
# rszvb_DeleteAllCalibrationData ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_DeleteAllCalibrationData  = prototype(('rszvb_DeleteAllCalibrationData', rszvbDLL), paramflags)
rszvb_DeleteAllCalibrationData.name = 'rszvb_DeleteAllCalibrationData'
rszvb_DeleteAllCalibrationData.errcheck = __errorcheck__
rszvb_DeleteAllCalibrationData.output = False
# rszvb_ReadCalibrationData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 errorTermParameters', 'ViInt32 port1', 'ViInt32 port2', 'ViReal64 _VI_FAR calibrationData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'errorTermParameters'),(1, 'port1'),(1, 'port2'),(1, 'calibrationData[]'),)
rszvb_ReadCalibrationData  = prototype(('rszvb_ReadCalibrationData', rszvbDLL), paramflags)
rszvb_ReadCalibrationData.name = 'rszvb_ReadCalibrationData'
rszvb_ReadCalibrationData.errcheck = __errorcheck__
rszvb_ReadCalibrationData.output = False
# rszvb_WriteCalibrationData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 errorTermParameters', 'ViInt32 port1', 'ViInt32 port2', 'ViReal64 _VI_FAR calibrationData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'errorTermParameters'),(1, 'port1'),(1, 'port2'),(1, 'calibrationData[]'),)
rszvb_WriteCalibrationData  = prototype(('rszvb_WriteCalibrationData', rszvbDLL), paramflags)
rszvb_WriteCalibrationData.name = 'rszvb_WriteCalibrationData'
rszvb_WriteCalibrationData.errcheck = __errorcheck__
rszvb_WriteCalibrationData.output = False
# rszvb_SetCorrectionState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean correctionState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'correctionState'),)
rszvb_SetCorrectionState  = prototype(('rszvb_SetCorrectionState', rszvbDLL), paramflags)
rszvb_SetCorrectionState.name = 'rszvb_SetCorrectionState'
rszvb_SetCorrectionState.errcheck = __errorcheck__
rszvb_SetCorrectionState.output = False
# rszvb_GetCorrectionState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* correctionState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'correctionState'),)
rszvb_GetCorrectionState  = prototype(('rszvb_GetCorrectionState', rszvbDLL), paramflags)
rszvb_GetCorrectionState.name = 'rszvb_GetCorrectionState'
rszvb_GetCorrectionState.errcheck = __errorcheck__
rszvb_GetCorrectionState.output = True
# rszvb_AcquireSourcePowerCalibration ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 source', 'ViInt32 portNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'source'),(1, 'portNumber'),)
rszvb_AcquireSourcePowerCalibration  = prototype(('rszvb_AcquireSourcePowerCalibration', rszvbDLL), paramflags)
rszvb_AcquireSourcePowerCalibration.name = 'rszvb_AcquireSourcePowerCalibration'
rszvb_AcquireSourcePowerCalibration.errcheck = __errorcheck__
rszvb_AcquireSourcePowerCalibration.output = False
# rszvb_InitiateSourcePowerCalibration ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViInt32 externalPowerMeter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'externalPowerMeter'),)
rszvb_InitiateSourcePowerCalibration  = prototype(('rszvb_InitiateSourcePowerCalibration', rszvbDLL), paramflags)
rszvb_InitiateSourcePowerCalibration.name = 'rszvb_InitiateSourcePowerCalibration'
rszvb_InitiateSourcePowerCalibration.errcheck = __errorcheck__
rszvb_InitiateSourcePowerCalibration.output = False
# rszvb_SetDummySourcePowerCalibrationState ['ViSession instrumentHandle', 'ViBoolean dummySourcePowerCalibration']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'dummySourcePowerCalibration'),)
rszvb_SetDummySourcePowerCalibrationState  = prototype(('rszvb_SetDummySourcePowerCalibrationState', rszvbDLL), paramflags)
rszvb_SetDummySourcePowerCalibrationState.name = 'rszvb_SetDummySourcePowerCalibrationState'
rszvb_SetDummySourcePowerCalibrationState.errcheck = __errorcheck__
rszvb_SetDummySourcePowerCalibrationState.output = False
# rszvb_GetDummySourcePowerCalibrationState ['ViSession instrumentHandle', 'ViBoolean* dummySourcePowerCalibration']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'dummySourcePowerCalibration'),)
rszvb_GetDummySourcePowerCalibrationState  = prototype(('rszvb_GetDummySourcePowerCalibrationState', rszvbDLL), paramflags)
rszvb_GetDummySourcePowerCalibrationState.name = 'rszvb_GetDummySourcePowerCalibrationState'
rszvb_GetDummySourcePowerCalibrationState.errcheck = __errorcheck__
rszvb_GetDummySourcePowerCalibrationState.output = True
# rszvb_SetSourcePowerCalibrationPortState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean portState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'portState'),)
rszvb_SetSourcePowerCalibrationPortState  = prototype(('rszvb_SetSourcePowerCalibrationPortState', rszvbDLL), paramflags)
rszvb_SetSourcePowerCalibrationPortState.name = 'rszvb_SetSourcePowerCalibrationPortState'
rszvb_SetSourcePowerCalibrationPortState.errcheck = __errorcheck__
rszvb_SetSourcePowerCalibrationPortState.output = False
# rszvb_GetSourcePowerCalibrationPortState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean* portState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(2, 'portState'),)
rszvb_GetSourcePowerCalibrationPortState  = prototype(('rszvb_GetSourcePowerCalibrationPortState', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationPortState.name = 'rszvb_GetSourcePowerCalibrationPortState'
rszvb_GetSourcePowerCalibrationPortState.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationPortState.output = True
# rszvb_SetSourcePowerCalibrationGeneratorState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean generatorState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'generatorState'),)
rszvb_SetSourcePowerCalibrationGeneratorState  = prototype(('rszvb_SetSourcePowerCalibrationGeneratorState', rszvbDLL), paramflags)
rszvb_SetSourcePowerCalibrationGeneratorState.name = 'rszvb_SetSourcePowerCalibrationGeneratorState'
rszvb_SetSourcePowerCalibrationGeneratorState.errcheck = __errorcheck__
rszvb_SetSourcePowerCalibrationGeneratorState.output = False
# rszvb_GetSourcePowerCalibrationGeneratorState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean* generatorState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(2, 'generatorState'),)
rszvb_GetSourcePowerCalibrationGeneratorState  = prototype(('rszvb_GetSourcePowerCalibrationGeneratorState', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationGeneratorState.name = 'rszvb_GetSourcePowerCalibrationGeneratorState'
rszvb_GetSourcePowerCalibrationGeneratorState.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationGeneratorState.output = True
# rszvb_SetVerificationSweepState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean verificationSweep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'verificationSweep'),)
rszvb_SetVerificationSweepState  = prototype(('rszvb_SetVerificationSweepState', rszvbDLL), paramflags)
rszvb_SetVerificationSweepState.name = 'rszvb_SetVerificationSweepState'
rszvb_SetVerificationSweepState.errcheck = __errorcheck__
rszvb_SetVerificationSweepState.output = False
# rszvb_GetVerificationSweepState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* verificationSweep']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'verificationSweep'),)
rszvb_GetVerificationSweepState  = prototype(('rszvb_GetVerificationSweepState', rszvbDLL), paramflags)
rszvb_GetVerificationSweepState.name = 'rszvb_GetVerificationSweepState'
rszvb_GetVerificationSweepState.errcheck = __errorcheck__
rszvb_GetVerificationSweepState.output = True
# rszvb_QueryVerificationSweepResults ['ViSession instrumentHandle', 'ViBoolean* calibrationPassed', 'ViReal64* maxOffset']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(2, 'calibrationPassed'),(2, 'maxOffset'),)
rszvb_QueryVerificationSweepResults  = prototype(('rszvb_QueryVerificationSweepResults', rszvbDLL), paramflags)
rszvb_QueryVerificationSweepResults.name = 'rszvb_QueryVerificationSweepResults'
rszvb_QueryVerificationSweepResults.errcheck = __errorcheck__
rszvb_QueryVerificationSweepResults.output = True
# rszvb_GeneratorPowerCalibrationHarmonic ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_GeneratorPowerCalibrationHarmonic  = prototype(('rszvb_GeneratorPowerCalibrationHarmonic', rszvbDLL), paramflags)
rszvb_GeneratorPowerCalibrationHarmonic.name = 'rszvb_GeneratorPowerCalibrationHarmonic'
rszvb_GeneratorPowerCalibrationHarmonic.errcheck = __errorcheck__
rszvb_GeneratorPowerCalibrationHarmonic.output = False
# rszvb_SetSourcePowerCalibrationState ['ViSession instrumentHandle', 'ViBoolean calibrationState']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationState'),)
rszvb_SetSourcePowerCalibrationState  = prototype(('rszvb_SetSourcePowerCalibrationState', rszvbDLL), paramflags)
rszvb_SetSourcePowerCalibrationState.name = 'rszvb_SetSourcePowerCalibrationState'
rszvb_SetSourcePowerCalibrationState.errcheck = __errorcheck__
rszvb_SetSourcePowerCalibrationState.output = False
# rszvb_GetSourcePowerCalibrationState ['ViSession instrumentHandle', 'ViBoolean* calibrationState']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'calibrationState'),)
rszvb_GetSourcePowerCalibrationState  = prototype(('rszvb_GetSourcePowerCalibrationState', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationState.name = 'rszvb_GetSourcePowerCalibrationState'
rszvb_GetSourcePowerCalibrationState.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationState.output = True
# rszvb_SetReferenceReceiverCalibrationState ['ViSession instrumentHandle', 'ViBoolean calibrationState']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationState'),)
rszvb_SetReferenceReceiverCalibrationState  = prototype(('rszvb_SetReferenceReceiverCalibrationState', rszvbDLL), paramflags)
rszvb_SetReferenceReceiverCalibrationState.name = 'rszvb_SetReferenceReceiverCalibrationState'
rszvb_SetReferenceReceiverCalibrationState.errcheck = __errorcheck__
rszvb_SetReferenceReceiverCalibrationState.output = False
# rszvb_GetReferenceReceiverCalibrationState ['ViSession instrumentHandle', 'ViBoolean* calibrationState']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'calibrationState'),)
rszvb_GetReferenceReceiverCalibrationState  = prototype(('rszvb_GetReferenceReceiverCalibrationState', rszvbDLL), paramflags)
rszvb_GetReferenceReceiverCalibrationState.name = 'rszvb_GetReferenceReceiverCalibrationState'
rszvb_GetReferenceReceiverCalibrationState.errcheck = __errorcheck__
rszvb_GetReferenceReceiverCalibrationState.output = True
# rszvb_ModifySourcePowerCalibrationSettings ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViInt32 numberOfReadings', 'ViReal64 tolerance', 'ViBoolean otherSourcesState', 'ViReal64 portPowerOffset', 'ViInt32 offsetParameter', 'ViReal64 calibrationPowerOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_double,c_bool,c_double,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'numberOfReadings'),(1, 'tolerance'),(1, 'otherSourcesState'),(1, 'portPowerOffset'),(1, 'offsetParameter'),(1, 'calibrationPowerOffset'),)
rszvb_ModifySourcePowerCalibrationSettings  = prototype(('rszvb_ModifySourcePowerCalibrationSettings', rszvbDLL), paramflags)
rszvb_ModifySourcePowerCalibrationSettings.name = 'rszvb_ModifySourcePowerCalibrationSettings'
rszvb_ModifySourcePowerCalibrationSettings.errcheck = __errorcheck__
rszvb_ModifySourcePowerCalibrationSettings.output = False
# rszvb_SetNumberOfReadings ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 numberOfReadings']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'numberOfReadings'),)
rszvb_SetNumberOfReadings  = prototype(('rszvb_SetNumberOfReadings', rszvbDLL), paramflags)
rszvb_SetNumberOfReadings.name = 'rszvb_SetNumberOfReadings'
rszvb_SetNumberOfReadings.errcheck = __errorcheck__
rszvb_SetNumberOfReadings.output = False
# rszvb_GetNumberOfReadings ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* numberOfReadings']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'numberOfReadings'),)
rszvb_GetNumberOfReadings  = prototype(('rszvb_GetNumberOfReadings', rszvbDLL), paramflags)
rszvb_GetNumberOfReadings.name = 'rszvb_GetNumberOfReadings'
rszvb_GetNumberOfReadings.errcheck = __errorcheck__
rszvb_GetNumberOfReadings.output = True
# rszvb_SetTolerance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64 tolerance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'tolerance'),)
rszvb_SetTolerance  = prototype(('rszvb_SetTolerance', rszvbDLL), paramflags)
rszvb_SetTolerance.name = 'rszvb_SetTolerance'
rszvb_SetTolerance.errcheck = __errorcheck__
rszvb_SetTolerance.output = False
# rszvb_GetTolerance ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* tolerance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'tolerance'),)
rszvb_GetTolerance  = prototype(('rszvb_GetTolerance', rszvbDLL), paramflags)
rszvb_GetTolerance.name = 'rszvb_GetTolerance'
rszvb_GetTolerance.errcheck = __errorcheck__
rszvb_GetTolerance.output = True
# rszvb_SetOtherSourcesState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean otherSources']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'otherSources'),)
rszvb_SetOtherSourcesState  = prototype(('rszvb_SetOtherSourcesState', rszvbDLL), paramflags)
rszvb_SetOtherSourcesState.name = 'rszvb_SetOtherSourcesState'
rszvb_SetOtherSourcesState.errcheck = __errorcheck__
rszvb_SetOtherSourcesState.output = False
# rszvb_GetOtherSourcesState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* otherSources']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'otherSources'),)
rszvb_GetOtherSourcesState  = prototype(('rszvb_GetOtherSourcesState', rszvbDLL), paramflags)
rszvb_GetOtherSourcesState.name = 'rszvb_GetOtherSourcesState'
rszvb_GetOtherSourcesState.errcheck = __errorcheck__
rszvb_GetOtherSourcesState.output = True
# rszvb_SetPortPowerOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViReal64 portPowerOffset', 'ViInt32 offsetParameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'portPowerOffset'),(1, 'offsetParameter'),)
rszvb_SetPortPowerOffset  = prototype(('rszvb_SetPortPowerOffset', rszvbDLL), paramflags)
rszvb_SetPortPowerOffset.name = 'rszvb_SetPortPowerOffset'
rszvb_SetPortPowerOffset.errcheck = __errorcheck__
rszvb_SetPortPowerOffset.output = False
# rszvb_GetPortPowerOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViReal64* portPowerOffset', 'ViInt32* offsetParameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(2, 'portPowerOffset'),(2, 'offsetParameter'),)
rszvb_GetPortPowerOffset  = prototype(('rszvb_GetPortPowerOffset', rszvbDLL), paramflags)
rszvb_GetPortPowerOffset.name = 'rszvb_GetPortPowerOffset'
rszvb_GetPortPowerOffset.errcheck = __errorcheck__
rszvb_GetPortPowerOffset.output = True
# rszvb_SetCalibrationPowerOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViReal64 calibrationPowerOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'calibrationPowerOffset'),)
rszvb_SetCalibrationPowerOffset  = prototype(('rszvb_SetCalibrationPowerOffset', rszvbDLL), paramflags)
rszvb_SetCalibrationPowerOffset.name = 'rszvb_SetCalibrationPowerOffset'
rszvb_SetCalibrationPowerOffset.errcheck = __errorcheck__
rszvb_SetCalibrationPowerOffset.output = False
# rszvb_GetCalibrationPowerOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViReal64* calibrationPowerOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(2, 'calibrationPowerOffset'),)
rszvb_GetCalibrationPowerOffset  = prototype(('rszvb_GetCalibrationPowerOffset', rszvbDLL), paramflags)
rszvb_GetCalibrationPowerOffset.name = 'rszvb_GetCalibrationPowerOffset'
rszvb_GetCalibrationPowerOffset.errcheck = __errorcheck__
rszvb_GetCalibrationPowerOffset.output = True
# rszvb_SetCalibrationPowerGeneratorOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViInt32 generatorNumber', 'ViReal64 calPowerGeneratorOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'generatorNumber'),(1, 'calPowerGeneratorOffset'),)
rszvb_SetCalibrationPowerGeneratorOffset  = prototype(('rszvb_SetCalibrationPowerGeneratorOffset', rszvbDLL), paramflags)
rszvb_SetCalibrationPowerGeneratorOffset.name = 'rszvb_SetCalibrationPowerGeneratorOffset'
rszvb_SetCalibrationPowerGeneratorOffset.errcheck = __errorcheck__
rszvb_SetCalibrationPowerGeneratorOffset.output = False
# rszvb_GetCalibrationPowerGeneratorOffset ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViInt32 generatorNumber', 'ViReal64* calPowerGeneratorOffset']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'generatorNumber'),(2, 'calPowerGeneratorOffset'),)
rszvb_GetCalibrationPowerGeneratorOffset  = prototype(('rszvb_GetCalibrationPowerGeneratorOffset', rszvbDLL), paramflags)
rszvb_GetCalibrationPowerGeneratorOffset.name = 'rszvb_GetCalibrationPowerGeneratorOffset'
rszvb_GetCalibrationPowerGeneratorOffset.errcheck = __errorcheck__
rszvb_GetCalibrationPowerGeneratorOffset.output = True
# rszvb_SetReferenceReceiverAfterFirstCalSweep ['ViSession instrumentHandle', 'ViBoolean fastSourcePowerCalibration']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'fastSourcePowerCalibration'),)
rszvb_SetReferenceReceiverAfterFirstCalSweep  = prototype(('rszvb_SetReferenceReceiverAfterFirstCalSweep', rszvbDLL), paramflags)
rszvb_SetReferenceReceiverAfterFirstCalSweep.name = 'rszvb_SetReferenceReceiverAfterFirstCalSweep'
rszvb_SetReferenceReceiverAfterFirstCalSweep.errcheck = __errorcheck__
rszvb_SetReferenceReceiverAfterFirstCalSweep.output = False
# rszvb_GetReferenceReceiverAfterFirstCalSweep ['ViSession instrumentHandle', 'ViBoolean* fastSourcePowerCalibration']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'fastSourcePowerCalibration'),)
rszvb_GetReferenceReceiverAfterFirstCalSweep  = prototype(('rszvb_GetReferenceReceiverAfterFirstCalSweep', rszvbDLL), paramflags)
rszvb_GetReferenceReceiverAfterFirstCalSweep.name = 'rszvb_GetReferenceReceiverAfterFirstCalSweep'
rszvb_GetReferenceReceiverAfterFirstCalSweep.errcheck = __errorcheck__
rszvb_GetReferenceReceiverAfterFirstCalSweep.output = True
# rszvb_SetPowerCalibrationMethodSource ['ViSession instrumentHandle', 'ViInt32 methodSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'methodSource'),)
rszvb_SetPowerCalibrationMethodSource  = prototype(('rszvb_SetPowerCalibrationMethodSource', rszvbDLL), paramflags)
rszvb_SetPowerCalibrationMethodSource.name = 'rszvb_SetPowerCalibrationMethodSource'
rszvb_SetPowerCalibrationMethodSource.errcheck = __errorcheck__
rszvb_SetPowerCalibrationMethodSource.output = False
# rszvb_GetPowerCalibrationMethodSource ['ViSession instrumentHandle', 'ViInt32* methodSource']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'methodSource'),)
rszvb_GetPowerCalibrationMethodSource  = prototype(('rszvb_GetPowerCalibrationMethodSource', rszvbDLL), paramflags)
rszvb_GetPowerCalibrationMethodSource.name = 'rszvb_GetPowerCalibrationMethodSource'
rszvb_GetPowerCalibrationMethodSource.errcheck = __errorcheck__
rszvb_GetPowerCalibrationMethodSource.output = True
# rszvb_SetCalibrationPowerMeterReadings ['ViSession instrumentHandle', 'ViInt32 powerMeterReadings']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'powerMeterReadings'),)
rszvb_SetCalibrationPowerMeterReadings  = prototype(('rszvb_SetCalibrationPowerMeterReadings', rszvbDLL), paramflags)
rszvb_SetCalibrationPowerMeterReadings.name = 'rszvb_SetCalibrationPowerMeterReadings'
rszvb_SetCalibrationPowerMeterReadings.errcheck = __errorcheck__
rszvb_SetCalibrationPowerMeterReadings.output = False
# rszvb_GetCalibrationPowerMeterReadings ['ViSession instrumentHandle', 'ViInt32* powerMeterReadings']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'powerMeterReadings'),)
rszvb_GetCalibrationPowerMeterReadings  = prototype(('rszvb_GetCalibrationPowerMeterReadings', rszvbDLL), paramflags)
rszvb_GetCalibrationPowerMeterReadings.name = 'rszvb_GetCalibrationPowerMeterReadings'
rszvb_GetCalibrationPowerMeterReadings.errcheck = __errorcheck__
rszvb_GetCalibrationPowerMeterReadings.output = True
# rszvb_ReadSourcePowerCorrectionData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViString calibratedWave', 'ViInt32* numberOfValues', 'ViReal64 _VI_FAR powerCorrectionValues[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'calibratedWave'),(2, 'numberOfValues'),(1, 'powerCorrectionValues[]'),)
rszvb_ReadSourcePowerCorrectionData  = prototype(('rszvb_ReadSourcePowerCorrectionData', rszvbDLL), paramflags)
rszvb_ReadSourcePowerCorrectionData.name = 'rszvb_ReadSourcePowerCorrectionData'
rszvb_ReadSourcePowerCorrectionData.errcheck = __errorcheck__
rszvb_ReadSourcePowerCorrectionData.output = True
# rszvb_WriteSourcePowerCorrectionData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViString calibratedWave', 'ViInt32 numberOfValues', 'ViReal64 _VI_FAR powerCorrectionValues[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'calibratedWave'),(1, 'numberOfValues'),(1, 'powerCorrectionValues[]'),)
rszvb_WriteSourcePowerCorrectionData  = prototype(('rszvb_WriteSourcePowerCorrectionData', rszvbDLL), paramflags)
rszvb_WriteSourcePowerCorrectionData.name = 'rszvb_WriteSourcePowerCorrectionData'
rszvb_WriteSourcePowerCorrectionData.errcheck = __errorcheck__
rszvb_WriteSourcePowerCorrectionData.output = False
# rszvb_GetSourcePowerCalibrationNumberOfWaves ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* numberOfWaves']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'numberOfWaves'),)
rszvb_GetSourcePowerCalibrationNumberOfWaves  = prototype(('rszvb_GetSourcePowerCalibrationNumberOfWaves', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationNumberOfWaves.name = 'rszvb_GetSourcePowerCalibrationNumberOfWaves'
rszvb_GetSourcePowerCalibrationNumberOfWaves.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationNumberOfWaves.output = True
# rszvb_GetSourcePowerCalibrationParamaterWave ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationIndex', 'ViInt32 bufferSize', 'ViChar _VI_FAR calibratedWave[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationIndex'),(1, 'bufferSize'),(1, 'calibratedWave[]'),)
rszvb_GetSourcePowerCalibrationParamaterWave  = prototype(('rszvb_GetSourcePowerCalibrationParamaterWave', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationParamaterWave.name = 'rszvb_GetSourcePowerCalibrationParamaterWave'
rszvb_GetSourcePowerCalibrationParamaterWave.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationParamaterWave.output = False
# rszvb_GetSourcePowerCalibrationParamaterStart ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationIndex', 'ViReal64* start']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationIndex'),(2, 'start'),)
rszvb_GetSourcePowerCalibrationParamaterStart  = prototype(('rszvb_GetSourcePowerCalibrationParamaterStart', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationParamaterStart.name = 'rszvb_GetSourcePowerCalibrationParamaterStart'
rszvb_GetSourcePowerCalibrationParamaterStart.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationParamaterStart.output = True
# rszvb_GetSourcePowerCalibrationParamaterStop ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationIndex', 'ViReal64* stop']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationIndex'),(2, 'stop'),)
rszvb_GetSourcePowerCalibrationParamaterStop  = prototype(('rszvb_GetSourcePowerCalibrationParamaterStop', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationParamaterStop.name = 'rszvb_GetSourcePowerCalibrationParamaterStop'
rszvb_GetSourcePowerCalibrationParamaterStop.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationParamaterStop.output = True
# rszvb_GetSourcePowerCalibrationParamaterPoints ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationIndex', 'ViInt32* points']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationIndex'),(2, 'points'),)
rszvb_GetSourcePowerCalibrationParamaterPoints  = prototype(('rszvb_GetSourcePowerCalibrationParamaterPoints', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationParamaterPoints.name = 'rszvb_GetSourcePowerCalibrationParamaterPoints'
rszvb_GetSourcePowerCalibrationParamaterPoints.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationParamaterPoints.output = True
# rszvb_GetSourcePowerCalibrationParamaterType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationIndex', 'ViInt32* type']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationIndex'),(2, 'type'),)
rszvb_GetSourcePowerCalibrationParamaterType  = prototype(('rszvb_GetSourcePowerCalibrationParamaterType', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationParamaterType.name = 'rszvb_GetSourcePowerCalibrationParamaterType'
rszvb_GetSourcePowerCalibrationParamaterType.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationParamaterType.output = True
# rszvb_GetSourcePowerCalibrationParamaterAttenuation ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationIndex', 'ViReal64* attenuation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationIndex'),(2, 'attenuation'),)
rszvb_GetSourcePowerCalibrationParamaterAttenuation  = prototype(('rszvb_GetSourcePowerCalibrationParamaterAttenuation', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationParamaterAttenuation.name = 'rszvb_GetSourcePowerCalibrationParamaterAttenuation'
rszvb_GetSourcePowerCalibrationParamaterAttenuation.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationParamaterAttenuation.output = True
# rszvb_GetSourcePowerCalibrationParamaterCWPower ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationIndex', 'ViReal64* CWPower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationIndex'),(2, 'CWPower'),)
rszvb_GetSourcePowerCalibrationParamaterCWPower  = prototype(('rszvb_GetSourcePowerCalibrationParamaterCWPower', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationParamaterCWPower.name = 'rszvb_GetSourcePowerCalibrationParamaterCWPower'
rszvb_GetSourcePowerCalibrationParamaterCWPower.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationParamaterCWPower.output = True
# rszvb_GetSourcePowerCalibrationParamaterCWFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationIndex', 'ViReal64* CWFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationIndex'),(2, 'CWFrequency'),)
rszvb_GetSourcePowerCalibrationParamaterCWFrequency  = prototype(('rszvb_GetSourcePowerCalibrationParamaterCWFrequency', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationParamaterCWFrequency.name = 'rszvb_GetSourcePowerCalibrationParamaterCWFrequency'
rszvb_GetSourcePowerCalibrationParamaterCWFrequency.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationParamaterCWFrequency.output = True
# rszvb_GetSourcePowerCalibrationParamaterTimestamp ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibrationIndex', 'ViInt32 bufferSize', 'ViChar _VI_FAR timestamp[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationIndex'),(1, 'bufferSize'),(1, 'timestamp[]'),)
rszvb_GetSourcePowerCalibrationParamaterTimestamp  = prototype(('rszvb_GetSourcePowerCalibrationParamaterTimestamp', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationParamaterTimestamp.name = 'rszvb_GetSourcePowerCalibrationParamaterTimestamp'
rszvb_GetSourcePowerCalibrationParamaterTimestamp.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationParamaterTimestamp.output = False
# rszvb_SetSourcePowerCalibrationConvergenceFactor ['ViSession instrumentHandle', 'ViReal64 convergenceFactor']
prototype = WINFUNCTYPE(c_int, c_int,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'convergenceFactor'),)
rszvb_SetSourcePowerCalibrationConvergenceFactor  = prototype(('rszvb_SetSourcePowerCalibrationConvergenceFactor', rszvbDLL), paramflags)
rszvb_SetSourcePowerCalibrationConvergenceFactor.name = 'rszvb_SetSourcePowerCalibrationConvergenceFactor'
rszvb_SetSourcePowerCalibrationConvergenceFactor.errcheck = __errorcheck__
rszvb_SetSourcePowerCalibrationConvergenceFactor.output = False
# rszvb_GetSourcePowerCalibrationConvergenceFactor ['ViSession instrumentHandle', 'ViReal64* convergenceFactor']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(2, 'convergenceFactor'),)
rszvb_GetSourcePowerCalibrationConvergenceFactor  = prototype(('rszvb_GetSourcePowerCalibrationConvergenceFactor', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationConvergenceFactor.name = 'rszvb_GetSourcePowerCalibrationConvergenceFactor'
rszvb_GetSourcePowerCalibrationConvergenceFactor.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationConvergenceFactor.output = True
# rszvb_SetSourcePowerCalibrationConverterState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 converter', 'ViBoolean calibrationConverter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'converter'),(1, 'calibrationConverter'),)
rszvb_SetSourcePowerCalibrationConverterState  = prototype(('rszvb_SetSourcePowerCalibrationConverterState', rszvbDLL), paramflags)
rszvb_SetSourcePowerCalibrationConverterState.name = 'rszvb_SetSourcePowerCalibrationConverterState'
rszvb_SetSourcePowerCalibrationConverterState.errcheck = __errorcheck__
rszvb_SetSourcePowerCalibrationConverterState.output = False
# rszvb_GetSourcePowerCalibrationConverterState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 converter', 'ViBoolean* calibrationConverter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'converter'),(2, 'calibrationConverter'),)
rszvb_GetSourcePowerCalibrationConverterState  = prototype(('rszvb_GetSourcePowerCalibrationConverterState', rszvbDLL), paramflags)
rszvb_GetSourcePowerCalibrationConverterState.name = 'rszvb_GetSourcePowerCalibrationConverterState'
rszvb_GetSourcePowerCalibrationConverterState.errcheck = __errorcheck__
rszvb_GetSourcePowerCalibrationConverterState.output = True
# rszvb_AcquireReceiverPowerCalibration ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 wave', 'ViInt32 portNumber', 'ViInt32 source', 'ViInt32 sourceNumber', 'ViInt32 referencePower']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'wave'),(1, 'portNumber'),(1, 'source'),(1, 'sourceNumber'),(1, 'referencePower'),)
rszvb_AcquireReceiverPowerCalibration  = prototype(('rszvb_AcquireReceiverPowerCalibration', rszvbDLL), paramflags)
rszvb_AcquireReceiverPowerCalibration.name = 'rszvb_AcquireReceiverPowerCalibration'
rszvb_AcquireReceiverPowerCalibration.errcheck = __errorcheck__
rszvb_AcquireReceiverPowerCalibration.output = False
# rszvb_SetAWaveReceiverPowerCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean receiverPowerCalibration']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'receiverPowerCalibration'),)
rszvb_SetAWaveReceiverPowerCalibrationState  = prototype(('rszvb_SetAWaveReceiverPowerCalibrationState', rszvbDLL), paramflags)
rszvb_SetAWaveReceiverPowerCalibrationState.name = 'rszvb_SetAWaveReceiverPowerCalibrationState'
rszvb_SetAWaveReceiverPowerCalibrationState.errcheck = __errorcheck__
rszvb_SetAWaveReceiverPowerCalibrationState.output = False
# rszvb_GetAWaveReceiverPowerCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean* receiverPowerCalibration']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(2, 'receiverPowerCalibration'),)
rszvb_GetAWaveReceiverPowerCalibrationState  = prototype(('rszvb_GetAWaveReceiverPowerCalibrationState', rszvbDLL), paramflags)
rszvb_GetAWaveReceiverPowerCalibrationState.name = 'rszvb_GetAWaveReceiverPowerCalibrationState'
rszvb_GetAWaveReceiverPowerCalibrationState.errcheck = __errorcheck__
rszvb_GetAWaveReceiverPowerCalibrationState.output = True
# rszvb_SetAWaveIdealPowerMeterMatchState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'state'),)
rszvb_SetAWaveIdealPowerMeterMatchState  = prototype(('rszvb_SetAWaveIdealPowerMeterMatchState', rszvbDLL), paramflags)
rszvb_SetAWaveIdealPowerMeterMatchState.name = 'rszvb_SetAWaveIdealPowerMeterMatchState'
rszvb_SetAWaveIdealPowerMeterMatchState.errcheck = __errorcheck__
rszvb_SetAWaveIdealPowerMeterMatchState.output = False
# rszvb_GetAWaveIdealPowerMeterMatchState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(2, 'state'),)
rszvb_GetAWaveIdealPowerMeterMatchState  = prototype(('rszvb_GetAWaveIdealPowerMeterMatchState', rszvbDLL), paramflags)
rszvb_GetAWaveIdealPowerMeterMatchState.name = 'rszvb_GetAWaveIdealPowerMeterMatchState'
rszvb_GetAWaveIdealPowerMeterMatchState.errcheck = __errorcheck__
rszvb_GetAWaveIdealPowerMeterMatchState.output = True
# rszvb_SetBWaveReceiverPowerCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean receiverPowerCalibration']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'receiverPowerCalibration'),)
rszvb_SetBWaveReceiverPowerCalibrationState  = prototype(('rszvb_SetBWaveReceiverPowerCalibrationState', rszvbDLL), paramflags)
rszvb_SetBWaveReceiverPowerCalibrationState.name = 'rszvb_SetBWaveReceiverPowerCalibrationState'
rszvb_SetBWaveReceiverPowerCalibrationState.errcheck = __errorcheck__
rszvb_SetBWaveReceiverPowerCalibrationState.output = False
# rszvb_GetBWaveReceiverPowerCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean* receiverPowerCalibration']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(2, 'receiverPowerCalibration'),)
rszvb_GetBWaveReceiverPowerCalibrationState  = prototype(('rszvb_GetBWaveReceiverPowerCalibrationState', rszvbDLL), paramflags)
rszvb_GetBWaveReceiverPowerCalibrationState.name = 'rszvb_GetBWaveReceiverPowerCalibrationState'
rszvb_GetBWaveReceiverPowerCalibrationState.errcheck = __errorcheck__
rszvb_GetBWaveReceiverPowerCalibrationState.output = True
# rszvb_ReadReceiverPowerCorrectionData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViString calibratedWave', 'ViInt32* numberOfValues', 'ViReal64 _VI_FAR powerCorrectionValues[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,POINTER(c_int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'calibratedWave'),(2, 'numberOfValues'),(1, 'powerCorrectionValues[]'),)
rszvb_ReadReceiverPowerCorrectionData  = prototype(('rszvb_ReadReceiverPowerCorrectionData', rszvbDLL), paramflags)
rszvb_ReadReceiverPowerCorrectionData.name = 'rszvb_ReadReceiverPowerCorrectionData'
rszvb_ReadReceiverPowerCorrectionData.errcheck = __errorcheck__
rszvb_ReadReceiverPowerCorrectionData.output = True
# rszvb_WriteReceiverPowerCorrectionData ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViString calibratedWave', 'ViInt32 numberOfValues', 'ViReal64 _VI_FAR powerCorrectionValues[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'calibratedWave'),(1, 'numberOfValues'),(1, 'powerCorrectionValues[]'),)
rszvb_WriteReceiverPowerCorrectionData  = prototype(('rszvb_WriteReceiverPowerCorrectionData', rszvbDLL), paramflags)
rszvb_WriteReceiverPowerCorrectionData.name = 'rszvb_WriteReceiverPowerCorrectionData'
rszvb_WriteReceiverPowerCorrectionData.errcheck = __errorcheck__
rszvb_WriteReceiverPowerCorrectionData.output = False
# rszvb_ReceiverPowerCalibrationHarmonic ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_ReceiverPowerCalibrationHarmonic  = prototype(('rszvb_ReceiverPowerCalibrationHarmonic', rszvbDLL), paramflags)
rszvb_ReceiverPowerCalibrationHarmonic.name = 'rszvb_ReceiverPowerCalibrationHarmonic'
rszvb_ReceiverPowerCalibrationHarmonic.errcheck = __errorcheck__
rszvb_ReceiverPowerCalibrationHarmonic.output = False
# rszvb_CorrectionManager ['ViSession instrumentHandle', 'ViInt32 operationToBePerformed', 'ViString fileName', 'ViString loadParameter']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'operationToBePerformed'),(1, 'fileName'),(1, 'loadParameter'),)
rszvb_CorrectionManager  = prototype(('rszvb_CorrectionManager', rszvbDLL), paramflags)
rszvb_CorrectionManager.name = 'rszvb_CorrectionManager'
rszvb_CorrectionManager.errcheck = __errorcheck__
rszvb_CorrectionManager.output = False
# rszvb_SetPowerSensorPosition ['ViSession instrumentHandle', 'ViInt32 powerSensorPosition']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'powerSensorPosition'),)
rszvb_SetPowerSensorPosition  = prototype(('rszvb_SetPowerSensorPosition', rszvbDLL), paramflags)
rszvb_SetPowerSensorPosition.name = 'rszvb_SetPowerSensorPosition'
rszvb_SetPowerSensorPosition.errcheck = __errorcheck__
rszvb_SetPowerSensorPosition.output = False
# rszvb_GetPowerSensorPosition ['ViSession instrumentHandle', 'ViInt32* powerSensorPosition']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'powerSensorPosition'),)
rszvb_GetPowerSensorPosition  = prototype(('rszvb_GetPowerSensorPosition', rszvbDLL), paramflags)
rszvb_GetPowerSensorPosition.name = 'rszvb_GetPowerSensorPosition'
rszvb_GetPowerSensorPosition.errcheck = __errorcheck__
rszvb_GetPowerSensorPosition.output = True
# rszvb_SetTwoPortTransmissionCoefficientsEnabled ['ViSession instrumentHandle', 'ViBoolean twoPortEnabled']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'twoPortEnabled'),)
rszvb_SetTwoPortTransmissionCoefficientsEnabled  = prototype(('rszvb_SetTwoPortTransmissionCoefficientsEnabled', rszvbDLL), paramflags)
rszvb_SetTwoPortTransmissionCoefficientsEnabled.name = 'rszvb_SetTwoPortTransmissionCoefficientsEnabled'
rszvb_SetTwoPortTransmissionCoefficientsEnabled.errcheck = __errorcheck__
rszvb_SetTwoPortTransmissionCoefficientsEnabled.output = False
# rszvb_GetTwoPortTransmissionCoefficientsEnabled ['ViSession instrumentHandle', 'ViBoolean* twoPortEnabled']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'twoPortEnabled'),)
rszvb_GetTwoPortTransmissionCoefficientsEnabled  = prototype(('rszvb_GetTwoPortTransmissionCoefficientsEnabled', rszvbDLL), paramflags)
rszvb_GetTwoPortTransmissionCoefficientsEnabled.name = 'rszvb_GetTwoPortTransmissionCoefficientsEnabled'
rszvb_GetTwoPortTransmissionCoefficientsEnabled.errcheck = __errorcheck__
rszvb_GetTwoPortTransmissionCoefficientsEnabled.output = True
# rszvb_GetLossListNumberOfValues ['ViSession instrumentHandle', 'ViInt32* numberOfValues']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'numberOfValues'),)
rszvb_GetLossListNumberOfValues  = prototype(('rszvb_GetLossListNumberOfValues', rszvbDLL), paramflags)
rszvb_GetLossListNumberOfValues.name = 'rszvb_GetLossListNumberOfValues'
rszvb_GetLossListNumberOfValues.errcheck = __errorcheck__
rszvb_GetLossListNumberOfValues.output = True
# rszvb_SetPowerLossListCoefficient ['ViSession instrumentHandle', 'ViInt32 operationToBePerformed', 'ViInt32 point', 'ViReal64 frequency', 'ViReal64 transmissionCoefficient']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'operationToBePerformed'),(1, 'point'),(1, 'frequency'),(1, 'transmissionCoefficient'),)
rszvb_SetPowerLossListCoefficient  = prototype(('rszvb_SetPowerLossListCoefficient', rszvbDLL), paramflags)
rszvb_SetPowerLossListCoefficient.name = 'rszvb_SetPowerLossListCoefficient'
rszvb_SetPowerLossListCoefficient.errcheck = __errorcheck__
rszvb_SetPowerLossListCoefficient.output = False
# rszvb_GetPowerLossListCoefficient ['ViSession instrumentHandle', 'ViInt32 point', 'ViReal64* frequency', 'ViReal64* transmissionCoefficient']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'point'),(2, 'frequency'),(2, 'transmissionCoefficient'),)
rszvb_GetPowerLossListCoefficient  = prototype(('rszvb_GetPowerLossListCoefficient', rszvbDLL), paramflags)
rszvb_GetPowerLossListCoefficient.name = 'rszvb_GetPowerLossListCoefficient'
rszvb_GetPowerLossListCoefficient.errcheck = __errorcheck__
rszvb_GetPowerLossListCoefficient.output = True
# rszvb_DeleteAllPowerLossListPoints ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_DeleteAllPowerLossListPoints  = prototype(('rszvb_DeleteAllPowerLossListPoints', rszvbDLL), paramflags)
rszvb_DeleteAllPowerLossListPoints.name = 'rszvb_DeleteAllPowerLossListPoints'
rszvb_DeleteAllPowerLossListPoints.errcheck = __errorcheck__
rszvb_DeleteAllPowerLossListPoints.output = False
# rszvb_DeletePowerLossListSinglePoint ['ViSession instrumentHandle', 'ViInt32 point']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'point'),)
rszvb_DeletePowerLossListSinglePoint  = prototype(('rszvb_DeletePowerLossListSinglePoint', rszvbDLL), paramflags)
rszvb_DeletePowerLossListSinglePoint.name = 'rszvb_DeletePowerLossListSinglePoint'
rszvb_DeletePowerLossListSinglePoint.errcheck = __errorcheck__
rszvb_DeletePowerLossListSinglePoint.output = False
# rszvb_SetPowerLossListTrace ['ViSession instrumentHandle', 'ViString traceName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),)
rszvb_SetPowerLossListTrace  = prototype(('rszvb_SetPowerLossListTrace', rszvbDLL), paramflags)
rszvb_SetPowerLossListTrace.name = 'rszvb_SetPowerLossListTrace'
rszvb_SetPowerLossListTrace.errcheck = __errorcheck__
rszvb_SetPowerLossListTrace.output = False
# rszvb_SetSourcePowerCorrectionState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean sourcePowerCorrectionState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'sourcePowerCorrectionState'),)
rszvb_SetSourcePowerCorrectionState  = prototype(('rszvb_SetSourcePowerCorrectionState', rszvbDLL), paramflags)
rszvb_SetSourcePowerCorrectionState.name = 'rszvb_SetSourcePowerCorrectionState'
rszvb_SetSourcePowerCorrectionState.errcheck = __errorcheck__
rszvb_SetSourcePowerCorrectionState.output = False
# rszvb_GetSourcePowerCorrectionState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean* sourcePowerCorrectionState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(2, 'sourcePowerCorrectionState'),)
rszvb_GetSourcePowerCorrectionState  = prototype(('rszvb_GetSourcePowerCorrectionState', rszvbDLL), paramflags)
rszvb_GetSourcePowerCorrectionState.name = 'rszvb_GetSourcePowerCorrectionState'
rszvb_GetSourcePowerCorrectionState.errcheck = __errorcheck__
rszvb_GetSourcePowerCorrectionState.output = True
# rszvb_SetReceiverPowerCorrectionState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean receiverPowerCorrectionState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(1, 'receiverPowerCorrectionState'),)
rszvb_SetReceiverPowerCorrectionState  = prototype(('rszvb_SetReceiverPowerCorrectionState', rszvbDLL), paramflags)
rszvb_SetReceiverPowerCorrectionState.name = 'rszvb_SetReceiverPowerCorrectionState'
rszvb_SetReceiverPowerCorrectionState.errcheck = __errorcheck__
rszvb_SetReceiverPowerCorrectionState.output = False
# rszvb_GetReceiverPowerCorrectionState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 portNumber', 'ViBoolean* receiverPowerCorrectionState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'portNumber'),(2, 'receiverPowerCorrectionState'),)
rszvb_GetReceiverPowerCorrectionState  = prototype(('rszvb_GetReceiverPowerCorrectionState', rszvbDLL), paramflags)
rszvb_GetReceiverPowerCorrectionState.name = 'rszvb_GetReceiverPowerCorrectionState'
rszvb_GetReceiverPowerCorrectionState.errcheck = __errorcheck__
rszvb_GetReceiverPowerCorrectionState.output = True
# rszvb_CalibrationManager ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 operationToBePerformed', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'operationToBePerformed'),(1, 'fileName'),)
rszvb_CalibrationManager  = prototype(('rszvb_CalibrationManager', rszvbDLL), paramflags)
rszvb_CalibrationManager.name = 'rszvb_CalibrationManager'
rszvb_CalibrationManager.errcheck = __errorcheck__
rszvb_CalibrationManager.output = False
# rszvb_CalibrationAuto ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString calibrationKitName', 'ViInt32 analyzerPort1', 'ViInt32 analyzerPort2', 'ViInt32 analyzerPort3', 'ViInt32 analyzerPort4', 'ViInt32 calUnitPort1', 'ViInt32 calUnitPort2', 'ViInt32 calUnitPort3', 'ViInt32 calUnitPort4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationKitName'),(1, 'analyzerPort1'),(1, 'analyzerPort2'),(1, 'analyzerPort3'),(1, 'analyzerPort4'),(1, 'calUnitPort1'),(1, 'calUnitPort2'),(1, 'calUnitPort3'),(1, 'calUnitPort4'),)
rszvb_CalibrationAuto  = prototype(('rszvb_CalibrationAuto', rszvbDLL), paramflags)
rszvb_CalibrationAuto.name = 'rszvb_CalibrationAuto'
rszvb_CalibrationAuto.errcheck = __errorcheck__
rszvb_CalibrationAuto.output = False
# rszvb_CalibrationAutoSimplified ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString calibrationKitName', 'ViInt32 analyzerPort1', 'ViInt32 analyzerPort2', 'ViInt32 analyzerPort3', 'ViInt32 analyzerPort4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationKitName'),(1, 'analyzerPort1'),(1, 'analyzerPort2'),(1, 'analyzerPort3'),(1, 'analyzerPort4'),)
rszvb_CalibrationAutoSimplified  = prototype(('rszvb_CalibrationAutoSimplified', rszvbDLL), paramflags)
rszvb_CalibrationAutoSimplified.name = 'rszvb_CalibrationAutoSimplified'
rszvb_CalibrationAutoSimplified.errcheck = __errorcheck__
rszvb_CalibrationAutoSimplified.output = False
# rszvb_CalibrationAutoType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 parameters', 'ViString calibrationKitName', 'ViInt32 analyzerPort1', 'ViInt32 analyzerPort2', 'ViInt32 analyzerPort3', 'ViInt32 analyzerPort4', 'ViInt32 calUnitPort1', 'ViInt32 calUnitPort2', 'ViInt32 calUnitPort3', 'ViInt32 calUnitPort4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'parameters'),(1, 'calibrationKitName'),(1, 'analyzerPort1'),(1, 'analyzerPort2'),(1, 'analyzerPort3'),(1, 'analyzerPort4'),(1, 'calUnitPort1'),(1, 'calUnitPort2'),(1, 'calUnitPort3'),(1, 'calUnitPort4'),)
rszvb_CalibrationAutoType  = prototype(('rszvb_CalibrationAutoType', rszvbDLL), paramflags)
rszvb_CalibrationAutoType.name = 'rszvb_CalibrationAutoType'
rszvb_CalibrationAutoType.errcheck = __errorcheck__
rszvb_CalibrationAutoType.output = False
# rszvb_CalibrationAutoTypeSimplified ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 parameters', 'ViString calibrationKitName', 'ViInt32 analyzerPort1', 'ViInt32 analyzerPort2', 'ViInt32 analyzerPort3', 'ViInt32 analyzerPort4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'parameters'),(1, 'calibrationKitName'),(1, 'analyzerPort1'),(1, 'analyzerPort2'),(1, 'analyzerPort3'),(1, 'analyzerPort4'),)
rszvb_CalibrationAutoTypeSimplified  = prototype(('rszvb_CalibrationAutoTypeSimplified', rszvbDLL), paramflags)
rszvb_CalibrationAutoTypeSimplified.name = 'rszvb_CalibrationAutoTypeSimplified'
rszvb_CalibrationAutoTypeSimplified.errcheck = __errorcheck__
rszvb_CalibrationAutoTypeSimplified.output = False
# rszvb_CalibrationRetainPortGroups ['ViSession instrumentHandle', 'ViBoolean retainPortGroups']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'retainPortGroups'),)
rszvb_CalibrationRetainPortGroups  = prototype(('rszvb_CalibrationRetainPortGroups', rszvbDLL), paramflags)
rszvb_CalibrationRetainPortGroups.name = 'rszvb_CalibrationRetainPortGroups'
rszvb_CalibrationRetainPortGroups.errcheck = __errorcheck__
rszvb_CalibrationRetainPortGroups.output = False
# rszvb_GetCalibrationConnection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* analyzerPort1', 'ViInt32* analyzerPort2', 'ViInt32* analyzerPort3', 'ViInt32* analyzerPort4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'analyzerPort1'),(2, 'analyzerPort2'),(2, 'analyzerPort3'),(2, 'analyzerPort4'),)
rszvb_GetCalibrationConnection  = prototype(('rszvb_GetCalibrationConnection', rszvbDLL), paramflags)
rszvb_GetCalibrationConnection.name = 'rszvb_GetCalibrationConnection'
rszvb_GetCalibrationConnection.errcheck = __errorcheck__
rszvb_GetCalibrationConnection.output = True
# rszvb_CalibrationAutoEx ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString calibrationKitName', 'ViInt32 analyzerPort1', 'ViInt32 analyzerPort2', 'ViInt32 analyzerPort3', 'ViInt32 analyzerPort4', 'ViInt32 calUnitPort1', 'ViInt32 calUnitPort2', 'ViInt32 calUnitPort3', 'ViInt32 calUnitPort4', 'ViInt32 timeout']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibrationKitName'),(1, 'analyzerPort1'),(1, 'analyzerPort2'),(1, 'analyzerPort3'),(1, 'analyzerPort4'),(1, 'calUnitPort1'),(1, 'calUnitPort2'),(1, 'calUnitPort3'),(1, 'calUnitPort4'),(1, 'timeout'),)
rszvb_CalibrationAutoEx  = prototype(('rszvb_CalibrationAutoEx', rszvbDLL), paramflags)
rszvb_CalibrationAutoEx.name = 'rszvb_CalibrationAutoEx'
rszvb_CalibrationAutoEx.errcheck = __errorcheck__
rszvb_CalibrationAutoEx.output = False
# rszvb_CalibrationAutoAssignmentType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 parameters', 'ViString calibrationKitName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'parameters'),(1, 'calibrationKitName'),)
rszvb_CalibrationAutoAssignmentType  = prototype(('rszvb_CalibrationAutoAssignmentType', rszvbDLL), paramflags)
rszvb_CalibrationAutoAssignmentType.name = 'rszvb_CalibrationAutoAssignmentType'
rszvb_CalibrationAutoAssignmentType.errcheck = __errorcheck__
rszvb_CalibrationAutoAssignmentType.output = False
# rszvb_CalibrationAutoAssignmentDefinition ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 assignment', 'ViInt32 analyzerPort1', 'ViInt32 analyzerPort2', 'ViInt32 analyzerPort3', 'ViInt32 analyzerPort4', 'ViInt32 calUnitPort1', 'ViInt32 calUnitPort2', 'ViInt32 calUnitPort3', 'ViInt32 calUnitPort4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'assignment'),(1, 'analyzerPort1'),(1, 'analyzerPort2'),(1, 'analyzerPort3'),(1, 'analyzerPort4'),(1, 'calUnitPort1'),(1, 'calUnitPort2'),(1, 'calUnitPort3'),(1, 'calUnitPort4'),)
rszvb_CalibrationAutoAssignmentDefinition  = prototype(('rszvb_CalibrationAutoAssignmentDefinition', rszvbDLL), paramflags)
rszvb_CalibrationAutoAssignmentDefinition.name = 'rszvb_CalibrationAutoAssignmentDefinition'
rszvb_CalibrationAutoAssignmentDefinition.errcheck = __errorcheck__
rszvb_CalibrationAutoAssignmentDefinition.output = False
# rszvb_GetCalibrationAutoAssingnmentDefinition ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 assignment', 'ViInt32* analyzerPort1', 'ViInt32* analyzerPort2', 'ViInt32* analyzerPort3', 'ViInt32* analyzerPort4', 'ViInt32* calUnitPort1', 'ViInt32* calUnitPort2', 'ViInt32* calUnitPort3', 'ViInt32* calUnitPort4']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'assignment'),(2, 'analyzerPort1'),(2, 'analyzerPort2'),(2, 'analyzerPort3'),(2, 'analyzerPort4'),(2, 'calUnitPort1'),(2, 'calUnitPort2'),(2, 'calUnitPort3'),(2, 'calUnitPort4'),)
rszvb_GetCalibrationAutoAssingnmentDefinition  = prototype(('rszvb_GetCalibrationAutoAssingnmentDefinition', rszvbDLL), paramflags)
rszvb_GetCalibrationAutoAssingnmentDefinition.name = 'rszvb_GetCalibrationAutoAssingnmentDefinition'
rszvb_GetCalibrationAutoAssingnmentDefinition.errcheck = __errorcheck__
rszvb_GetCalibrationAutoAssingnmentDefinition.output = True
# rszvb_InitiateCalibrationAutoAssignment ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 assignment']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'assignment'),)
rszvb_InitiateCalibrationAutoAssignment  = prototype(('rszvb_InitiateCalibrationAutoAssignment', rszvbDLL), paramflags)
rszvb_InitiateCalibrationAutoAssignment.name = 'rszvb_InitiateCalibrationAutoAssignment'
rszvb_InitiateCalibrationAutoAssignment.errcheck = __errorcheck__
rszvb_InitiateCalibrationAutoAssignment.output = False
# rszvb_CalibrationAutoAssignmentSave ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_CalibrationAutoAssignmentSave  = prototype(('rszvb_CalibrationAutoAssignmentSave', rszvbDLL), paramflags)
rszvb_CalibrationAutoAssignmentSave.name = 'rszvb_CalibrationAutoAssignmentSave'
rszvb_CalibrationAutoAssignmentSave.errcheck = __errorcheck__
rszvb_CalibrationAutoAssignmentSave.output = False
# rszvb_CalibrationAutoAssingnmentDeleteAll ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_CalibrationAutoAssingnmentDeleteAll  = prototype(('rszvb_CalibrationAutoAssingnmentDeleteAll', rszvbDLL), paramflags)
rszvb_CalibrationAutoAssingnmentDeleteAll.name = 'rszvb_CalibrationAutoAssingnmentDeleteAll'
rszvb_CalibrationAutoAssingnmentDeleteAll.errcheck = __errorcheck__
rszvb_CalibrationAutoAssingnmentDeleteAll.output = False
# rszvb_SetCalibrationDataCurrentState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean keepMeasData']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'keepMeasData'),)
rszvb_SetCalibrationDataCurrentState  = prototype(('rszvb_SetCalibrationDataCurrentState', rszvbDLL), paramflags)
rszvb_SetCalibrationDataCurrentState.name = 'rszvb_SetCalibrationDataCurrentState'
rszvb_SetCalibrationDataCurrentState.errcheck = __errorcheck__
rszvb_SetCalibrationDataCurrentState.output = False
# rszvb_GetCalibrationDataCurrentState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* keepMeasData']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'keepMeasData'),)
rszvb_GetCalibrationDataCurrentState  = prototype(('rszvb_GetCalibrationDataCurrentState', rszvbDLL), paramflags)
rszvb_GetCalibrationDataCurrentState.name = 'rszvb_GetCalibrationDataCurrentState'
rszvb_GetCalibrationDataCurrentState.errcheck = __errorcheck__
rszvb_GetCalibrationDataCurrentState.output = True
# rszvb_SetCalibrationDataDefaultState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean keepMeasData']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'keepMeasData'),)
rszvb_SetCalibrationDataDefaultState  = prototype(('rszvb_SetCalibrationDataDefaultState', rszvbDLL), paramflags)
rszvb_SetCalibrationDataDefaultState.name = 'rszvb_SetCalibrationDataDefaultState'
rszvb_SetCalibrationDataDefaultState.errcheck = __errorcheck__
rszvb_SetCalibrationDataDefaultState.output = False
# rszvb_GetCalibrationDataDefaultState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* keepMeasData']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'keepMeasData'),)
rszvb_GetCalibrationDataDefaultState  = prototype(('rszvb_GetCalibrationDataDefaultState', rszvbDLL), paramflags)
rszvb_GetCalibrationDataDefaultState.name = 'rszvb_GetCalibrationDataDefaultState'
rszvb_GetCalibrationDataDefaultState.errcheck = __errorcheck__
rszvb_GetCalibrationDataDefaultState.output = True
# rszvb_ExpCharDataTouchstoneFile ['ViSession instrumentHandle', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),)
rszvb_ExpCharDataTouchstoneFile  = prototype(('rszvb_ExpCharDataTouchstoneFile', rszvbDLL), paramflags)
rszvb_ExpCharDataTouchstoneFile.name = 'rszvb_ExpCharDataTouchstoneFile'
rszvb_ExpCharDataTouchstoneFile.errcheck = __errorcheck__
rszvb_ExpCharDataTouchstoneFile.output = False
# rszvb_ExportUserCharacterizationDataTouchstoneFile ['ViSession instrumentHandle', 'ViString directoryName', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'directoryName'),(1, 'fileName'),)
rszvb_ExportUserCharacterizationDataTouchstoneFile  = prototype(('rszvb_ExportUserCharacterizationDataTouchstoneFile', rszvbDLL), paramflags)
rszvb_ExportUserCharacterizationDataTouchstoneFile.name = 'rszvb_ExportUserCharacterizationDataTouchstoneFile'
rszvb_ExportUserCharacterizationDataTouchstoneFile.errcheck = __errorcheck__
rszvb_ExportUserCharacterizationDataTouchstoneFile.output = False
# rszvb_SetCalibrationConnector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString connectorName', 'ViInt32 propagationMode', 'ViInt32 connectorType', 'ViReal64 relativePermittivity', 'ViReal64 impedance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'connectorName'),(1, 'propagationMode'),(1, 'connectorType'),(1, 'relativePermittivity'),(1, 'impedance'),)
rszvb_SetCalibrationConnector  = prototype(('rszvb_SetCalibrationConnector', rszvbDLL), paramflags)
rszvb_SetCalibrationConnector.name = 'rszvb_SetCalibrationConnector'
rszvb_SetCalibrationConnector.errcheck = __errorcheck__
rszvb_SetCalibrationConnector.output = False
# rszvb_GetCalibrationConnector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString connectorName', 'ViInt32* propagationMode', 'ViInt32* connectorType', 'ViReal64* relativePermittivity', 'ViReal64* impedance']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,POINTER(c_int32),POINTER(c_int32),POINTER(c_double),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'connectorName'),(2, 'propagationMode'),(2, 'connectorType'),(2, 'relativePermittivity'),(2, 'impedance'),)
rszvb_GetCalibrationConnector  = prototype(('rszvb_GetCalibrationConnector', rszvbDLL), paramflags)
rszvb_GetCalibrationConnector.name = 'rszvb_GetCalibrationConnector'
rszvb_GetCalibrationConnector.errcheck = __errorcheck__
rszvb_GetCalibrationConnector.output = True
# rszvb_CalibrationConnectorCatalog ['ViSession instrumentHandle', 'ViChar _VI_FAR catalog[]', 'ViInt32 bufferSize']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'catalog[]'),(1, 'bufferSize'),)
rszvb_CalibrationConnectorCatalog  = prototype(('rszvb_CalibrationConnectorCatalog', rszvbDLL), paramflags)
rszvb_CalibrationConnectorCatalog.name = 'rszvb_CalibrationConnectorCatalog'
rszvb_CalibrationConnectorCatalog.errcheck = __errorcheck__
rszvb_CalibrationConnectorCatalog.output = False
# rszvb_DeleteCalibrationConnector ['ViSession instrumentHandle', 'ViInt32 channel', 'ViString connectorName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'connectorName'),)
rszvb_DeleteCalibrationConnector  = prototype(('rszvb_DeleteCalibrationConnector', rszvbDLL), paramflags)
rszvb_DeleteCalibrationConnector.name = 'rszvb_DeleteCalibrationConnector'
rszvb_DeleteCalibrationConnector.errcheck = __errorcheck__
rszvb_DeleteCalibrationConnector.output = False
# rszvb_GetCalibrationDate ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 bufferSize', 'ViChar _VI_FAR calibrationDate[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'bufferSize'),(1, 'calibrationDate[]'),)
rszvb_GetCalibrationDate  = prototype(('rszvb_GetCalibrationDate', rszvbDLL), paramflags)
rszvb_GetCalibrationDate.name = 'rszvb_GetCalibrationDate'
rszvb_GetCalibrationDate.errcheck = __errorcheck__
rszvb_GetCalibrationDate.output = False
# rszvb_GetCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* calibrationState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'calibrationState'),)
rszvb_GetCalibrationState  = prototype(('rszvb_GetCalibrationState', rszvbDLL), paramflags)
rszvb_GetCalibrationState.name = 'rszvb_GetCalibrationState'
rszvb_GetCalibrationState.errcheck = __errorcheck__
rszvb_GetCalibrationState.output = True
# rszvb_GetCalibrationLabel ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 bufferSize', 'ViChar _VI_FAR label[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'bufferSize'),(1, 'label[]'),)
rszvb_GetCalibrationLabel  = prototype(('rszvb_GetCalibrationLabel', rszvbDLL), paramflags)
rszvb_GetCalibrationLabel.name = 'rszvb_GetCalibrationLabel'
rszvb_GetCalibrationLabel.errcheck = __errorcheck__
rszvb_GetCalibrationLabel.output = False
# rszvb_GetCalibrationDataParameters ['ViSession instrumentHandle', 'ViInt32 channel', 'ViReal64* frequencyStart', 'ViReal64* frequencyStop', 'ViInt32* numberOfPoints', 'ViReal64* internalSignalSourcePower', 'ViInt32* sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double),POINTER(c_double),POINTER(c_int32),POINTER(c_double),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'frequencyStart'),(2, 'frequencyStop'),(2, 'numberOfPoints'),(2, 'internalSignalSourcePower'),(2, 'sweepType'),)
rszvb_GetCalibrationDataParameters  = prototype(('rszvb_GetCalibrationDataParameters', rszvbDLL), paramflags)
rszvb_GetCalibrationDataParameters.name = 'rszvb_GetCalibrationDataParameters'
rszvb_GetCalibrationDataParameters.errcheck = __errorcheck__
rszvb_GetCalibrationDataParameters.output = True
# rszvb_GetCalibrationsNumber ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* numberOfCalibrations']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'numberOfCalibrations'),)
rszvb_GetCalibrationsNumber  = prototype(('rszvb_GetCalibrationsNumber', rszvbDLL), paramflags)
rszvb_GetCalibrationsNumber.name = 'rszvb_GetCalibrationsNumber'
rszvb_GetCalibrationsNumber.errcheck = __errorcheck__
rszvb_GetCalibrationsNumber.output = True
# rszvb_GetCalibrationDataParametersMoreCalibrations ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibration', 'ViReal64* frequencyStart', 'ViReal64* frequencyStop', 'ViInt32* numberOfPoints', 'ViReal64* internalSignalSourcePower', 'ViInt32* sweepType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double),POINTER(c_double),POINTER(c_int32),POINTER(c_double),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibration'),(2, 'frequencyStart'),(2, 'frequencyStop'),(2, 'numberOfPoints'),(2, 'internalSignalSourcePower'),(2, 'sweepType'),)
rszvb_GetCalibrationDataParametersMoreCalibrations  = prototype(('rszvb_GetCalibrationDataParametersMoreCalibrations', rszvbDLL), paramflags)
rszvb_GetCalibrationDataParametersMoreCalibrations.name = 'rszvb_GetCalibrationDataParametersMoreCalibrations'
rszvb_GetCalibrationDataParametersMoreCalibrations.errcheck = __errorcheck__
rszvb_GetCalibrationDataParametersMoreCalibrations.output = True
# rszvb_GetCalibrationDataBandwidth ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibration', 'ViReal64* bandwidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibration'),(2, 'bandwidth'),)
rszvb_GetCalibrationDataBandwidth  = prototype(('rszvb_GetCalibrationDataBandwidth', rszvbDLL), paramflags)
rszvb_GetCalibrationDataBandwidth.name = 'rszvb_GetCalibrationDataBandwidth'
rszvb_GetCalibrationDataBandwidth.errcheck = __errorcheck__
rszvb_GetCalibrationDataBandwidth.output = True
# rszvb_GetCalibrationDataPointDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibration', 'ViReal64* pointDelay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibration'),(2, 'pointDelay'),)
rszvb_GetCalibrationDataPointDelay  = prototype(('rszvb_GetCalibrationDataPointDelay', rszvbDLL), paramflags)
rszvb_GetCalibrationDataPointDelay.name = 'rszvb_GetCalibrationDataPointDelay'
rszvb_GetCalibrationDataPointDelay.errcheck = __errorcheck__
rszvb_GetCalibrationDataPointDelay.output = True
# rszvb_GetCalibrationDataReceiverAttenuation ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibration', 'ViInt32 arraySize', 'ViInt32 _VI_FAR calibrationPort[]', 'ViReal64 _VI_FAR attenuation[]', 'ViInt32* returnedValues']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.int32),numpy.ctypeslib.ndpointer(dtype=numpy.float64),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibration'),(1, 'arraySize'),(1, 'calibrationPort[]'),(1, 'attenuation[]'),(2, 'returnedValues'),)
rszvb_GetCalibrationDataReceiverAttenuation  = prototype(('rszvb_GetCalibrationDataReceiverAttenuation', rszvbDLL), paramflags)
rszvb_GetCalibrationDataReceiverAttenuation.name = 'rszvb_GetCalibrationDataReceiverAttenuation'
rszvb_GetCalibrationDataReceiverAttenuation.errcheck = __errorcheck__
rszvb_GetCalibrationDataReceiverAttenuation.output = True
# rszvb_GetCalibrationDataType ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibration', 'ViInt32* calibrationType']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibration'),(2, 'calibrationType'),)
rszvb_GetCalibrationDataType  = prototype(('rszvb_GetCalibrationDataType', rszvbDLL), paramflags)
rszvb_GetCalibrationDataType.name = 'rszvb_GetCalibrationDataType'
rszvb_GetCalibrationDataType.errcheck = __errorcheck__
rszvb_GetCalibrationDataType.output = True
# rszvb_GetCalibrationDataPorts ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibration', 'ViInt32 arraySize', 'ViInt32* calibrationPorts', 'ViInt32* returnedValues']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibration'),(1, 'arraySize'),(2, 'calibrationPorts'),(2, 'returnedValues'),)
rszvb_GetCalibrationDataPorts  = prototype(('rszvb_GetCalibrationDataPorts', rszvbDLL), paramflags)
rszvb_GetCalibrationDataPorts.name = 'rszvb_GetCalibrationDataPorts'
rszvb_GetCalibrationDataPorts.errcheck = __errorcheck__
rszvb_GetCalibrationDataPorts.output = True
# rszvb_GetCalibrationDataThroughs ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibration', 'ViInt32 bufferSize', 'ViChar _VI_FAR throughs[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibration'),(1, 'bufferSize'),(1, 'throughs[]'),)
rszvb_GetCalibrationDataThroughs  = prototype(('rszvb_GetCalibrationDataThroughs', rszvbDLL), paramflags)
rszvb_GetCalibrationDataThroughs.name = 'rszvb_GetCalibrationDataThroughs'
rszvb_GetCalibrationDataThroughs.errcheck = __errorcheck__
rszvb_GetCalibrationDataThroughs.output = False
# rszvb_GetCalibrationDataTimestamp ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 calibration', 'ViInt32 bufferSize', 'ViChar _VI_FAR timestamp[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'calibration'),(1, 'bufferSize'),(1, 'timestamp[]'),)
rszvb_GetCalibrationDataTimestamp  = prototype(('rszvb_GetCalibrationDataTimestamp', rszvbDLL), paramflags)
rszvb_GetCalibrationDataTimestamp.name = 'rszvb_GetCalibrationDataTimestamp'
rszvb_GetCalibrationDataTimestamp.errcheck = __errorcheck__
rszvb_GetCalibrationDataTimestamp.output = False
# rszvb_SetActiveCalibrationUnit ['ViSession instrumentHandle', 'ViString calibrationUnit']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationUnit'),)
rszvb_SetActiveCalibrationUnit  = prototype(('rszvb_SetActiveCalibrationUnit', rszvbDLL), paramflags)
rszvb_SetActiveCalibrationUnit.name = 'rszvb_SetActiveCalibrationUnit'
rszvb_SetActiveCalibrationUnit.errcheck = __errorcheck__
rszvb_SetActiveCalibrationUnit.output = False
# rszvb_GetActiveCalibrationUnit ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR calibrationUnit[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'calibrationUnit[]'),)
rszvb_GetActiveCalibrationUnit  = prototype(('rszvb_GetActiveCalibrationUnit', rszvbDLL), paramflags)
rszvb_GetActiveCalibrationUnit.name = 'rszvb_GetActiveCalibrationUnit'
rszvb_GetActiveCalibrationUnit.errcheck = __errorcheck__
rszvb_GetActiveCalibrationUnit.output = False
# rszvb_SetAutomaticPowerReductionState ['ViSession instrumentHandle', 'ViBoolean automaticPowerReduction']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'automaticPowerReduction'),)
rszvb_SetAutomaticPowerReductionState  = prototype(('rszvb_SetAutomaticPowerReductionState', rszvbDLL), paramflags)
rszvb_SetAutomaticPowerReductionState.name = 'rszvb_SetAutomaticPowerReductionState'
rszvb_SetAutomaticPowerReductionState.errcheck = __errorcheck__
rszvb_SetAutomaticPowerReductionState.output = False
# rszvb_GetAutomaticPowerReductionState ['ViSession instrumentHandle', 'ViBoolean* automaticPowerReduction']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'automaticPowerReduction'),)
rszvb_GetAutomaticPowerReductionState  = prototype(('rszvb_GetAutomaticPowerReductionState', rszvbDLL), paramflags)
rszvb_GetAutomaticPowerReductionState.name = 'rszvb_GetAutomaticPowerReductionState'
rszvb_GetAutomaticPowerReductionState.errcheck = __errorcheck__
rszvb_GetAutomaticPowerReductionState.output = True
# rszvb_GetAllCalibrationUnits ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR calibrationUnit[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'calibrationUnit[]'),)
rszvb_GetAllCalibrationUnits  = prototype(('rszvb_GetAllCalibrationUnits', rszvbDLL), paramflags)
rszvb_GetAllCalibrationUnits.name = 'rszvb_GetAllCalibrationUnits'
rszvb_GetAllCalibrationUnits.errcheck = __errorcheck__
rszvb_GetAllCalibrationUnits.output = False
# rszvb_ConfigureCalibrationUnitStandard ['ViSession instrumentHandle', 'ViInt32 standard', 'ViInt32 port1', 'ViInt32 port2']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'standard'),(1, 'port1'),(1, 'port2'),)
rszvb_ConfigureCalibrationUnitStandard  = prototype(('rszvb_ConfigureCalibrationUnitStandard', rszvbDLL), paramflags)
rszvb_ConfigureCalibrationUnitStandard.name = 'rszvb_ConfigureCalibrationUnitStandard'
rszvb_ConfigureCalibrationUnitStandard.errcheck = __errorcheck__
rszvb_ConfigureCalibrationUnitStandard.output = False
# rszvb_SetFactoryCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean factoryCalibration']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'factoryCalibration'),)
rszvb_SetFactoryCalibrationState  = prototype(('rszvb_SetFactoryCalibrationState', rszvbDLL), paramflags)
rszvb_SetFactoryCalibrationState.name = 'rszvb_SetFactoryCalibrationState'
rszvb_SetFactoryCalibrationState.errcheck = __errorcheck__
rszvb_SetFactoryCalibrationState.output = False
# rszvb_GetFactoryCalibrationState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* factoryCalibration']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'factoryCalibration'),)
rszvb_GetFactoryCalibrationState  = prototype(('rszvb_GetFactoryCalibrationState', rszvbDLL), paramflags)
rszvb_GetFactoryCalibrationState.name = 'rszvb_GetFactoryCalibrationState'
rszvb_GetFactoryCalibrationState.errcheck = __errorcheck__
rszvb_GetFactoryCalibrationState.output = True
# rszvb_SetEnhancedWaveCorrection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean errorCorrection']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'errorCorrection'),)
rszvb_SetEnhancedWaveCorrection  = prototype(('rszvb_SetEnhancedWaveCorrection', rszvbDLL), paramflags)
rszvb_SetEnhancedWaveCorrection.name = 'rszvb_SetEnhancedWaveCorrection'
rszvb_SetEnhancedWaveCorrection.errcheck = __errorcheck__
rszvb_SetEnhancedWaveCorrection.output = False
# rszvb_GetEnhancedWaveCorrection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* errorCorrection']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'errorCorrection'),)
rszvb_GetEnhancedWaveCorrection  = prototype(('rszvb_GetEnhancedWaveCorrection', rszvbDLL), paramflags)
rszvb_GetEnhancedWaveCorrection.name = 'rszvb_GetEnhancedWaveCorrection'
rszvb_GetEnhancedWaveCorrection.errcheck = __errorcheck__
rszvb_GetEnhancedWaveCorrection.output = True
# rszvb_SetLoadMatchingCorrection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean loadMatchingCorrection']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'loadMatchingCorrection'),)
rszvb_SetLoadMatchingCorrection  = prototype(('rszvb_SetLoadMatchingCorrection', rszvbDLL), paramflags)
rszvb_SetLoadMatchingCorrection.name = 'rszvb_SetLoadMatchingCorrection'
rszvb_SetLoadMatchingCorrection.errcheck = __errorcheck__
rszvb_SetLoadMatchingCorrection.output = False
# rszvb_GetLoadMatchingCorrection ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* loadMatchingCorrection']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'loadMatchingCorrection'),)
rszvb_GetLoadMatchingCorrection  = prototype(('rszvb_GetLoadMatchingCorrection', rszvbDLL), paramflags)
rszvb_GetLoadMatchingCorrection.name = 'rszvb_GetLoadMatchingCorrection'
rszvb_GetLoadMatchingCorrection.errcheck = __errorcheck__
rszvb_GetLoadMatchingCorrection.output = True
# rszvb_SetCalibrationCorrectionBaseFrequencyState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'state'),)
rszvb_SetCalibrationCorrectionBaseFrequencyState  = prototype(('rszvb_SetCalibrationCorrectionBaseFrequencyState', rszvbDLL), paramflags)
rszvb_SetCalibrationCorrectionBaseFrequencyState.name = 'rszvb_SetCalibrationCorrectionBaseFrequencyState'
rszvb_SetCalibrationCorrectionBaseFrequencyState.errcheck = __errorcheck__
rszvb_SetCalibrationCorrectionBaseFrequencyState.output = False
# rszvb_GetCalibrationCorrectionBaseFrequencyState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'state'),)
rszvb_GetCalibrationCorrectionBaseFrequencyState  = prototype(('rszvb_GetCalibrationCorrectionBaseFrequencyState', rszvbDLL), paramflags)
rszvb_GetCalibrationCorrectionBaseFrequencyState.name = 'rszvb_GetCalibrationCorrectionBaseFrequencyState'
rszvb_GetCalibrationCorrectionBaseFrequencyState.errcheck = __errorcheck__
rszvb_GetCalibrationCorrectionBaseFrequencyState.output = True
# rszvb_SetCalibrationKit ['ViSession instrumentHandle', 'ViInt32 connector', 'ViString calibrationKitName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'connector'),(1, 'calibrationKitName'),)
rszvb_SetCalibrationKit  = prototype(('rszvb_SetCalibrationKit', rszvbDLL), paramflags)
rszvb_SetCalibrationKit.name = 'rszvb_SetCalibrationKit'
rszvb_SetCalibrationKit.errcheck = __errorcheck__
rszvb_SetCalibrationKit.output = False
# rszvb_GetCalibrationKit ['ViSession instrumentHandle', 'ViInt32 connector', 'ViInt32 bufferSize', 'ViChar _VI_FAR calibrationKitName[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'connector'),(1, 'bufferSize'),(1, 'calibrationKitName[]'),)
rszvb_GetCalibrationKit  = prototype(('rszvb_GetCalibrationKit', rszvbDLL), paramflags)
rszvb_GetCalibrationKit.name = 'rszvb_GetCalibrationKit'
rszvb_GetCalibrationKit.errcheck = __errorcheck__
rszvb_GetCalibrationKit.output = False
# rszvb_SetCalibrationKitWithLabel ['ViSession instrumentHandle', 'ViInt32 connector', 'ViString calibrationKitName', 'ViString calibrationKitLabel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'connector'),(1, 'calibrationKitName'),(1, 'calibrationKitLabel'),)
rszvb_SetCalibrationKitWithLabel  = prototype(('rszvb_SetCalibrationKitWithLabel', rszvbDLL), paramflags)
rszvb_SetCalibrationKitWithLabel.name = 'rszvb_SetCalibrationKitWithLabel'
rszvb_SetCalibrationKitWithLabel.errcheck = __errorcheck__
rszvb_SetCalibrationKitWithLabel.output = False
# rszvb_SetCalibrationKitUserConnectorType ['ViSession instrumentHandle', 'ViString connector', 'ViString calibrationKitName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'connector'),(1, 'calibrationKitName'),)
rszvb_SetCalibrationKitUserConnectorType  = prototype(('rszvb_SetCalibrationKitUserConnectorType', rszvbDLL), paramflags)
rszvb_SetCalibrationKitUserConnectorType.name = 'rszvb_SetCalibrationKitUserConnectorType'
rszvb_SetCalibrationKitUserConnectorType.errcheck = __errorcheck__
rszvb_SetCalibrationKitUserConnectorType.output = False
# rszvb_GetCalibrationKitUserConnectorType ['ViSession instrumentHandle', 'ViString connector', 'ViInt32 bufferSize', 'ViChar _VI_FAR calibrationKitName[]']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'connector'),(1, 'bufferSize'),(1, 'calibrationKitName[]'),)
rszvb_GetCalibrationKitUserConnectorType  = prototype(('rszvb_GetCalibrationKitUserConnectorType', rszvbDLL), paramflags)
rszvb_GetCalibrationKitUserConnectorType.name = 'rszvb_GetCalibrationKitUserConnectorType'
rszvb_GetCalibrationKitUserConnectorType.errcheck = __errorcheck__
rszvb_GetCalibrationKitUserConnectorType.output = False
# rszvb_SetCalibrationKitUserConnectorTypeWithLabel ['ViSession instrumentHandle', 'ViString connectionType', 'ViString calibrationKitName', 'ViString calibrationKitLabel']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'connectionType'),(1, 'calibrationKitName'),(1, 'calibrationKitLabel'),)
rszvb_SetCalibrationKitUserConnectorTypeWithLabel  = prototype(('rszvb_SetCalibrationKitUserConnectorTypeWithLabel', rszvbDLL), paramflags)
rszvb_SetCalibrationKitUserConnectorTypeWithLabel.name = 'rszvb_SetCalibrationKitUserConnectorTypeWithLabel'
rszvb_SetCalibrationKitUserConnectorTypeWithLabel.errcheck = __errorcheck__
rszvb_SetCalibrationKitUserConnectorTypeWithLabel.output = False
# rszvb_GetCalibrationKitUserConnectorTypeWithLabel ['ViSession instrumentHandle', 'ViString connectionType', 'ViInt32 bufferSize', 'ViChar _VI_FAR calibrationKitData[]']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'connectionType'),(1, 'bufferSize'),(1, 'calibrationKitData[]'),)
rszvb_GetCalibrationKitUserConnectorTypeWithLabel  = prototype(('rszvb_GetCalibrationKitUserConnectorTypeWithLabel', rszvbDLL), paramflags)
rszvb_GetCalibrationKitUserConnectorTypeWithLabel.name = 'rszvb_GetCalibrationKitUserConnectorTypeWithLabel'
rszvb_GetCalibrationKitUserConnectorTypeWithLabel.errcheck = __errorcheck__
rszvb_GetCalibrationKitUserConnectorTypeWithLabel.output = False
# rszvb_CalibrationKitCatalog ['ViSession instrumentHandle', 'ViString connectorName', 'ViChar _VI_FAR catalog[]', 'ViInt32 bufferSize']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'connectorName'),(1, 'catalog[]'),(1, 'bufferSize'),)
rszvb_CalibrationKitCatalog  = prototype(('rszvb_CalibrationKitCatalog', rszvbDLL), paramflags)
rszvb_CalibrationKitCatalog.name = 'rszvb_CalibrationKitCatalog'
rszvb_CalibrationKitCatalog.errcheck = __errorcheck__
rszvb_CalibrationKitCatalog.output = False
# rszvb_CalibrationKitCatalogWithLabel ['ViSession instrumentHandle', 'ViString connectorName', 'ViInt32 bufferSize', 'ViChar _VI_FAR catalog[]']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'connectorName'),(1, 'bufferSize'),(1, 'catalog[]'),)
rszvb_CalibrationKitCatalogWithLabel  = prototype(('rszvb_CalibrationKitCatalogWithLabel', rszvbDLL), paramflags)
rszvb_CalibrationKitCatalogWithLabel.name = 'rszvb_CalibrationKitCatalogWithLabel'
rszvb_CalibrationKitCatalogWithLabel.errcheck = __errorcheck__
rszvb_CalibrationKitCatalogWithLabel.output = False
# rszvb_ImportZVRCalibrationKit ['ViSession instrumentHandle', 'ViString calibrationKitName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationKitName'),)
rszvb_ImportZVRCalibrationKit  = prototype(('rszvb_ImportZVRCalibrationKit', rszvbDLL), paramflags)
rszvb_ImportZVRCalibrationKit.name = 'rszvb_ImportZVRCalibrationKit'
rszvb_ImportZVRCalibrationKit.errcheck = __errorcheck__
rszvb_ImportZVRCalibrationKit.output = False
# rszvb_ConfigureCalibrationStandard ['ViSession instrumentHandle', 'ViInt32 connector', 'ViInt32 standard', 'ViString kit', 'ViString serialNumber', 'ViReal64 minFreqHz', 'ViReal64 maxFreqHz', 'ViReal64 lengthmm', 'ViReal64 loss', 'ViReal64 c0L0', 'ViReal64 c1L1', 'ViReal64 c2L2', 'ViReal64 c3L3', 'ViInt32 approximation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_char_p,c_char_p,c_double,c_double,c_double,c_double,c_double,c_double,c_double,c_double,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'connector'),(1, 'standard'),(1, 'kit'),(1, 'serialNumber'),(1, 'minFreqHz'),(1, 'maxFreqHz'),(1, 'lengthmm'),(1, 'loss'),(1, 'c0L0'),(1, 'c1L1'),(1, 'c2L2'),(1, 'c3L3'),(1, 'approximation'),)
rszvb_ConfigureCalibrationStandard  = prototype(('rszvb_ConfigureCalibrationStandard', rszvbDLL), paramflags)
rszvb_ConfigureCalibrationStandard.name = 'rszvb_ConfigureCalibrationStandard'
rszvb_ConfigureCalibrationStandard.errcheck = __errorcheck__
rszvb_ConfigureCalibrationStandard.output = False
# rszvb_ConfigureCalibrationStandardWithLabel ['ViSession instrumentHandle', 'ViInt32 standard', 'ViString connector', 'ViString calkitName', 'ViString calkitLabel', 'ViString standardLabel', 'ViReal64 minFreqHz', 'ViReal64 maxFreqHz', 'ViReal64 electricalLength', 'ViReal64 loss', 'ViReal64 z0', 'ViReal64 _VI_FAR capacitances[]', 'ViReal64 _VI_FAR residualInductances[]', 'ViInt32 approximation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p,c_char_p,c_char_p,c_double,c_double,c_double,c_double,c_double,numpy.ctypeslib.ndpointer(dtype=numpy.float64),numpy.ctypeslib.ndpointer(dtype=numpy.float64),c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'standard'),(1, 'connector'),(1, 'calkitName'),(1, 'calkitLabel'),(1, 'standardLabel'),(1, 'minFreqHz'),(1, 'maxFreqHz'),(1, 'electricalLength'),(1, 'loss'),(1, 'z0'),(1, 'capacitances[]'),(1, 'residualInductances[]'),(1, 'approximation'),)
rszvb_ConfigureCalibrationStandardWithLabel  = prototype(('rszvb_ConfigureCalibrationStandardWithLabel', rszvbDLL), paramflags)
rszvb_ConfigureCalibrationStandardWithLabel.name = 'rszvb_ConfigureCalibrationStandardWithLabel'
rszvb_ConfigureCalibrationStandardWithLabel.errcheck = __errorcheck__
rszvb_ConfigureCalibrationStandardWithLabel.output = False
# rszvb_CalibrationStandardsCatalog ['ViSession instrumentHandle', 'ViString calibrationKitName', 'ViChar _VI_FAR catalog[]', 'ViInt32 bufferSize']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationKitName'),(1, 'catalog[]'),(1, 'bufferSize'),)
rszvb_CalibrationStandardsCatalog  = prototype(('rszvb_CalibrationStandardsCatalog', rszvbDLL), paramflags)
rszvb_CalibrationStandardsCatalog.name = 'rszvb_CalibrationStandardsCatalog'
rszvb_CalibrationStandardsCatalog.errcheck = __errorcheck__
rszvb_CalibrationStandardsCatalog.output = False
# rszvb_CalibrationStandardsCatalogWithLabel ['ViSession instrumentHandle', 'ViString calibrationKitName', 'ViString calibrationKitLabel', 'ViInt32 bufferSize', 'ViChar _VI_FAR catalog[]']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationKitName'),(1, 'calibrationKitLabel'),(1, 'bufferSize'),(1, 'catalog[]'),)
rszvb_CalibrationStandardsCatalogWithLabel  = prototype(('rszvb_CalibrationStandardsCatalogWithLabel', rszvbDLL), paramflags)
rszvb_CalibrationStandardsCatalogWithLabel.name = 'rszvb_CalibrationStandardsCatalogWithLabel'
rszvb_CalibrationStandardsCatalogWithLabel.errcheck = __errorcheck__
rszvb_CalibrationStandardsCatalogWithLabel.output = False
# rszvb_SaveCalibrationKit ['ViSession instrumentHandle', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),)
rszvb_SaveCalibrationKit  = prototype(('rszvb_SaveCalibrationKit', rszvbDLL), paramflags)
rszvb_SaveCalibrationKit.name = 'rszvb_SaveCalibrationKit'
rszvb_SaveCalibrationKit.errcheck = __errorcheck__
rszvb_SaveCalibrationKit.output = False
# rszvb_SaveCalibrationKitPorts ['ViSession instrumentHandle', 'ViString fileName', 'ViInt32 parameters', 'ViInt32 arraySize', 'ViInt32 _VI_FAR VNAPorts[]', 'ViInt32 _VI_FAR calUnitPorts[]']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.int32),numpy.ctypeslib.ndpointer(dtype=numpy.int32))
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),(1, 'parameters'),(1, 'arraySize'),(1, 'VNAPorts[]'),(1, 'calUnitPorts[]'),)
rszvb_SaveCalibrationKitPorts  = prototype(('rszvb_SaveCalibrationKitPorts', rszvbDLL), paramflags)
rszvb_SaveCalibrationKitPorts.name = 'rszvb_SaveCalibrationKitPorts'
rszvb_SaveCalibrationKitPorts.errcheck = __errorcheck__
rszvb_SaveCalibrationKitPorts.output = False
# rszvb_LoadCalibrationKit ['ViSession instrumentHandle', 'ViString connectorName', 'ViString calibrationKitName', 'ViInt32 standard', 'ViString calibrationKitLabel', 'ViString fileName', 'ViInt32 portNumber1', 'ViInt32 portNumber2']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p,c_int32,c_char_p,c_char_p,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'connectorName'),(1, 'calibrationKitName'),(1, 'standard'),(1, 'calibrationKitLabel'),(1, 'fileName'),(1, 'portNumber1'),(1, 'portNumber2'),)
rszvb_LoadCalibrationKit  = prototype(('rszvb_LoadCalibrationKit', rszvbDLL), paramflags)
rszvb_LoadCalibrationKit.name = 'rszvb_LoadCalibrationKit'
rszvb_LoadCalibrationKit.errcheck = __errorcheck__
rszvb_LoadCalibrationKit.output = False
# rszvb_SetCalibrationKitLabel ['ViSession instrumentHandle', 'ViString calibrationKitName', 'ViString label']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationKitName'),(1, 'label'),)
rszvb_SetCalibrationKitLabel  = prototype(('rszvb_SetCalibrationKitLabel', rszvbDLL), paramflags)
rszvb_SetCalibrationKitLabel.name = 'rszvb_SetCalibrationKitLabel'
rszvb_SetCalibrationKitLabel.errcheck = __errorcheck__
rszvb_SetCalibrationKitLabel.output = False
# rszvb_RenameCalibrationKit ['ViSession instrumentHandle', 'ViString calibrationKitName', 'ViString label', 'ViString newLabel']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationKitName'),(1, 'label'),(1, 'newLabel'),)
rszvb_RenameCalibrationKit  = prototype(('rszvb_RenameCalibrationKit', rszvbDLL), paramflags)
rszvb_RenameCalibrationKit.name = 'rszvb_RenameCalibrationKit'
rszvb_RenameCalibrationKit.errcheck = __errorcheck__
rszvb_RenameCalibrationKit.output = False
# rszvb_GetCalibrationKitLabel ['ViSession instrumentHandle', 'ViString calibrationKitName', 'ViChar _VI_FAR label[]']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationKitName'),(1, 'label[]'),)
rszvb_GetCalibrationKitLabel  = prototype(('rszvb_GetCalibrationKitLabel', rszvbDLL), paramflags)
rszvb_GetCalibrationKitLabel.name = 'rszvb_GetCalibrationKitLabel'
rszvb_GetCalibrationKitLabel.errcheck = __errorcheck__
rszvb_GetCalibrationKitLabel.output = False
# rszvb_DeleteCalibrationKit ['ViSession instrumentHandle', 'ViString calibrationKitName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationKitName'),)
rszvb_DeleteCalibrationKit  = prototype(('rszvb_DeleteCalibrationKit', rszvbDLL), paramflags)
rszvb_DeleteCalibrationKit.name = 'rszvb_DeleteCalibrationKit'
rszvb_DeleteCalibrationKit.errcheck = __errorcheck__
rszvb_DeleteCalibrationKit.output = False
# rszvb_DeleteCalibrationKitWithLabel ['ViSession instrumentHandle', 'ViString calibrationKitName', 'ViString calibrationKitLabel']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'calibrationKitName'),(1, 'calibrationKitLabel'),)
rszvb_DeleteCalibrationKitWithLabel  = prototype(('rszvb_DeleteCalibrationKitWithLabel', rszvbDLL), paramflags)
rszvb_DeleteCalibrationKitWithLabel.name = 'rszvb_DeleteCalibrationKitWithLabel'
rszvb_DeleteCalibrationKitWithLabel.errcheck = __errorcheck__
rszvb_DeleteCalibrationKitWithLabel.output = False
# rszvb_ImportKit ['ViSession instrumentHandle', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),)
rszvb_ImportKit  = prototype(('rszvb_ImportKit', rszvbDLL), paramflags)
rszvb_ImportKit.name = 'rszvb_ImportKit'
rszvb_ImportKit.errcheck = __errorcheck__
rszvb_ImportKit.output = False
# rszvb_AdditionalDirectoryCalibrationKit ['ViSession instrumentHandle', 'ViString directory']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'directory'),)
rszvb_AdditionalDirectoryCalibrationKit  = prototype(('rszvb_AdditionalDirectoryCalibrationKit', rszvbDLL), paramflags)
rszvb_AdditionalDirectoryCalibrationKit.name = 'rszvb_AdditionalDirectoryCalibrationKit'
rszvb_AdditionalDirectoryCalibrationKit.errcheck = __errorcheck__
rszvb_AdditionalDirectoryCalibrationKit.output = False
# rszvb_ExportKit ['ViSession instrumentHandle', 'ViString kitName', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'kitName'),(1, 'fileName'),)
rszvb_ExportKit  = prototype(('rszvb_ExportKit', rszvbDLL), paramflags)
rszvb_ExportKit.name = 'rszvb_ExportKit'
rszvb_ExportKit.errcheck = __errorcheck__
rszvb_ExportKit.output = False
# rszvb_ExportKitWithLabel ['ViSession instrumentHandle', 'ViString kitName', 'ViString kitLabel', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'kitName'),(1, 'kitLabel'),(1, 'fileName'),)
rszvb_ExportKitWithLabel  = prototype(('rszvb_ExportKitWithLabel', rszvbDLL), paramflags)
rszvb_ExportKitWithLabel.name = 'rszvb_ExportKitWithLabel'
rszvb_ExportKitWithLabel.errcheck = __errorcheck__
rszvb_ExportKitWithLabel.output = False
# rszvb_ResetOffsets ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_ResetOffsets  = prototype(('rszvb_ResetOffsets', rszvbDLL), paramflags)
rszvb_ResetOffsets.name = 'rszvb_ResetOffsets'
rszvb_ResetOffsets.errcheck = __errorcheck__
rszvb_ResetOffsets.output = False
# rszvb_QueryResetOffsets ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32* offsets']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(2, 'offsets'),)
rszvb_QueryResetOffsets  = prototype(('rszvb_QueryResetOffsets', rszvbDLL), paramflags)
rszvb_QueryResetOffsets.name = 'rszvb_QueryResetOffsets'
rszvb_QueryResetOffsets.errcheck = __errorcheck__
rszvb_QueryResetOffsets.output = True
# rszvb_SetElectricalLength ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 electricalLength']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'electricalLength'),)
rszvb_SetElectricalLength  = prototype(('rszvb_SetElectricalLength', rszvbDLL), paramflags)
rszvb_SetElectricalLength.name = 'rszvb_SetElectricalLength'
rszvb_SetElectricalLength.errcheck = __errorcheck__
rszvb_SetElectricalLength.output = False
# rszvb_GetElectricalLength ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* electricalLength']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'electricalLength'),)
rszvb_GetElectricalLength  = prototype(('rszvb_GetElectricalLength', rszvbDLL), paramflags)
rszvb_GetElectricalLength.name = 'rszvb_GetElectricalLength'
rszvb_GetElectricalLength.errcheck = __errorcheck__
rszvb_GetElectricalLength.output = True
# rszvb_ConfigureMechanicalLength ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 mechanicalLength', 'ViReal64 permittivity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'mechanicalLength'),(1, 'permittivity'),)
rszvb_ConfigureMechanicalLength  = prototype(('rszvb_ConfigureMechanicalLength', rszvbDLL), paramflags)
rszvb_ConfigureMechanicalLength.name = 'rszvb_ConfigureMechanicalLength'
rszvb_ConfigureMechanicalLength.errcheck = __errorcheck__
rszvb_ConfigureMechanicalLength.output = False
# rszvb_SetMechanicalLength ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 mechanicalLength']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'mechanicalLength'),)
rszvb_SetMechanicalLength  = prototype(('rszvb_SetMechanicalLength', rszvbDLL), paramflags)
rszvb_SetMechanicalLength.name = 'rszvb_SetMechanicalLength'
rszvb_SetMechanicalLength.errcheck = __errorcheck__
rszvb_SetMechanicalLength.output = False
# rszvb_GetMechanicalLength ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* mechanicalLength']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'mechanicalLength'),)
rszvb_GetMechanicalLength  = prototype(('rszvb_GetMechanicalLength', rszvbDLL), paramflags)
rszvb_GetMechanicalLength.name = 'rszvb_GetMechanicalLength'
rszvb_GetMechanicalLength.errcheck = __errorcheck__
rszvb_GetMechanicalLength.output = True
# rszvb_SetPermittivity ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 permittivity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'permittivity'),)
rszvb_SetPermittivity  = prototype(('rszvb_SetPermittivity', rszvbDLL), paramflags)
rszvb_SetPermittivity.name = 'rszvb_SetPermittivity'
rszvb_SetPermittivity.errcheck = __errorcheck__
rszvb_SetPermittivity.output = False
# rszvb_GetPermittivity ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* permittivity']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'permittivity'),)
rszvb_GetPermittivity  = prototype(('rszvb_GetPermittivity', rszvbDLL), paramflags)
rszvb_GetPermittivity.name = 'rszvb_GetPermittivity'
rszvb_GetPermittivity.errcheck = __errorcheck__
rszvb_GetPermittivity.output = True
# rszvb_ConfigureLoss ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 lossAtDC', 'ViReal64 lossAtFrequency', 'ViReal64 lossReferenceFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double,c_double,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'lossAtDC'),(1, 'lossAtFrequency'),(1, 'lossReferenceFrequency'),)
rszvb_ConfigureLoss  = prototype(('rszvb_ConfigureLoss', rszvbDLL), paramflags)
rszvb_ConfigureLoss.name = 'rszvb_ConfigureLoss'
rszvb_ConfigureLoss.errcheck = __errorcheck__
rszvb_ConfigureLoss.output = False
# rszvb_SetLossAtDC ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 lossAtDC']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'lossAtDC'),)
rszvb_SetLossAtDC  = prototype(('rszvb_SetLossAtDC', rszvbDLL), paramflags)
rszvb_SetLossAtDC.name = 'rszvb_SetLossAtDC'
rszvb_SetLossAtDC.errcheck = __errorcheck__
rszvb_SetLossAtDC.output = False
# rszvb_GetLossAtDC ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* lossAtDC']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'lossAtDC'),)
rszvb_GetLossAtDC  = prototype(('rszvb_GetLossAtDC', rszvbDLL), paramflags)
rszvb_GetLossAtDC.name = 'rszvb_GetLossAtDC'
rszvb_GetLossAtDC.errcheck = __errorcheck__
rszvb_GetLossAtDC.output = True
# rszvb_SetLossAtFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 lossAtFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'lossAtFrequency'),)
rszvb_SetLossAtFrequency  = prototype(('rszvb_SetLossAtFrequency', rszvbDLL), paramflags)
rszvb_SetLossAtFrequency.name = 'rszvb_SetLossAtFrequency'
rszvb_SetLossAtFrequency.errcheck = __errorcheck__
rszvb_SetLossAtFrequency.output = False
# rszvb_GetLossAtFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* lossAtFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'lossAtFrequency'),)
rszvb_GetLossAtFrequency  = prototype(('rszvb_GetLossAtFrequency', rszvbDLL), paramflags)
rszvb_GetLossAtFrequency.name = 'rszvb_GetLossAtFrequency'
rszvb_GetLossAtFrequency.errcheck = __errorcheck__
rszvb_GetLossAtFrequency.output = True
# rszvb_SetLossReferenceFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 lossReferenceFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'lossReferenceFrequency'),)
rszvb_SetLossReferenceFrequency  = prototype(('rszvb_SetLossReferenceFrequency', rszvbDLL), paramflags)
rszvb_SetLossReferenceFrequency.name = 'rszvb_SetLossReferenceFrequency'
rszvb_SetLossReferenceFrequency.errcheck = __errorcheck__
rszvb_SetLossReferenceFrequency.output = False
# rszvb_GetLossReferenceFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* lossReferenceFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'lossReferenceFrequency'),)
rszvb_GetLossReferenceFrequency  = prototype(('rszvb_GetLossReferenceFrequency', rszvbDLL), paramflags)
rszvb_GetLossReferenceFrequency.name = 'rszvb_GetLossReferenceFrequency'
rszvb_GetLossReferenceFrequency.errcheck = __errorcheck__
rszvb_GetLossReferenceFrequency.output = True
# rszvb_SetDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 delay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'delay'),)
rszvb_SetDelay  = prototype(('rszvb_SetDelay', rszvbDLL), paramflags)
rszvb_SetDelay.name = 'rszvb_SetDelay'
rszvb_SetDelay.errcheck = __errorcheck__
rszvb_SetDelay.output = False
# rszvb_GetDelay ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* delay']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'delay'),)
rszvb_GetDelay  = prototype(('rszvb_GetDelay', rszvbDLL), paramflags)
rszvb_GetDelay.name = 'rszvb_GetDelay'
rszvb_GetDelay.errcheck = __errorcheck__
rszvb_GetDelay.output = True
# rszvb_QueryDirectFixtureCompensation ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* directFixtureCompensation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'directFixtureCompensation'),)
rszvb_QueryDirectFixtureCompensation  = prototype(('rszvb_QueryDirectFixtureCompensation', rszvbDLL), paramflags)
rszvb_QueryDirectFixtureCompensation.name = 'rszvb_QueryDirectFixtureCompensation'
rszvb_QueryDirectFixtureCompensation.errcheck = __errorcheck__
rszvb_QueryDirectFixtureCompensation.output = True
# rszvb_AutoLength ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),)
rszvb_AutoLength  = prototype(('rszvb_AutoLength', rszvbDLL), paramflags)
rszvb_AutoLength.name = 'rszvb_AutoLength'
rszvb_AutoLength.errcheck = __errorcheck__
rszvb_AutoLength.output = False
# rszvb_AutoLengthAndLoss ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),)
rszvb_AutoLengthAndLoss  = prototype(('rszvb_AutoLengthAndLoss', rszvbDLL), paramflags)
rszvb_AutoLengthAndLoss.name = 'rszvb_AutoLengthAndLoss'
rszvb_AutoLengthAndLoss.errcheck = __errorcheck__
rszvb_AutoLengthAndLoss.output = False
# rszvb_AcquireFixtureCompensationSweep ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 standardType', 'ViInt32 arraySize', 'ViInt32 _VI_FAR ports[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'standardType'),(1, 'arraySize'),(1, 'ports[]'),)
rszvb_AcquireFixtureCompensationSweep  = prototype(('rszvb_AcquireFixtureCompensationSweep', rszvbDLL), paramflags)
rszvb_AcquireFixtureCompensationSweep.name = 'rszvb_AcquireFixtureCompensationSweep'
rszvb_AcquireFixtureCompensationSweep.errcheck = __errorcheck__
rszvb_AcquireFixtureCompensationSweep.output = False
# rszvb_StartFixtureCompensationSweep ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_StartFixtureCompensationSweep  = prototype(('rszvb_StartFixtureCompensationSweep', rszvbDLL), paramflags)
rszvb_StartFixtureCompensationSweep.name = 'rszvb_StartFixtureCompensationSweep'
rszvb_StartFixtureCompensationSweep.errcheck = __errorcheck__
rszvb_StartFixtureCompensationSweep.output = False
# rszvb_SaveFixtureCompensationData ['ViSession instrumentHandle', 'ViInt32 channel']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),)
rszvb_SaveFixtureCompensationData  = prototype(('rszvb_SaveFixtureCompensationData', rszvbDLL), paramflags)
rszvb_SaveFixtureCompensationData.name = 'rszvb_SaveFixtureCompensationData'
rszvb_SaveFixtureCompensationData.errcheck = __errorcheck__
rszvb_SaveFixtureCompensationData.output = False
# rszvb_SetFixtureCompensationAutoLengthAndLossCalculation ['ViSession instrumentHandle', 'ViBoolean autoLengthAndLoss']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'autoLengthAndLoss'),)
rszvb_SetFixtureCompensationAutoLengthAndLossCalculation  = prototype(('rszvb_SetFixtureCompensationAutoLengthAndLossCalculation', rszvbDLL), paramflags)
rszvb_SetFixtureCompensationAutoLengthAndLossCalculation.name = 'rszvb_SetFixtureCompensationAutoLengthAndLossCalculation'
rszvb_SetFixtureCompensationAutoLengthAndLossCalculation.errcheck = __errorcheck__
rszvb_SetFixtureCompensationAutoLengthAndLossCalculation.output = False
# rszvb_GetFixtureCompensationAutoLengthAndLossCalculation ['ViSession instrumentHandle', 'ViBoolean* autoLengthAndLoss']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'autoLengthAndLoss'),)
rszvb_GetFixtureCompensationAutoLengthAndLossCalculation  = prototype(('rszvb_GetFixtureCompensationAutoLengthAndLossCalculation', rszvbDLL), paramflags)
rszvb_GetFixtureCompensationAutoLengthAndLossCalculation.name = 'rszvb_GetFixtureCompensationAutoLengthAndLossCalculation'
rszvb_GetFixtureCompensationAutoLengthAndLossCalculation.errcheck = __errorcheck__
rszvb_GetFixtureCompensationAutoLengthAndLossCalculation.output = True
# rszvb_SetFixtureCompensationDirectCompensation ['ViSession instrumentHandle', 'ViBoolean directCompensation']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'directCompensation'),)
rszvb_SetFixtureCompensationDirectCompensation  = prototype(('rszvb_SetFixtureCompensationDirectCompensation', rszvbDLL), paramflags)
rszvb_SetFixtureCompensationDirectCompensation.name = 'rszvb_SetFixtureCompensationDirectCompensation'
rszvb_SetFixtureCompensationDirectCompensation.errcheck = __errorcheck__
rszvb_SetFixtureCompensationDirectCompensation.output = False
# rszvb_GetFixtureCompensationDirectCompensation ['ViSession instrumentHandle', 'ViBoolean* directCompensation']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'directCompensation'),)
rszvb_GetFixtureCompensationDirectCompensation  = prototype(('rszvb_GetFixtureCompensationDirectCompensation', rszvbDLL), paramflags)
rszvb_GetFixtureCompensationDirectCompensation.name = 'rszvb_GetFixtureCompensationDirectCompensation'
rszvb_GetFixtureCompensationDirectCompensation.errcheck = __errorcheck__
rszvb_GetFixtureCompensationDirectCompensation.output = True
# rszvb_DiagramAreaAdd ['ViSession instrumentHandle', 'ViInt32 window']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),)
rszvb_DiagramAreaAdd  = prototype(('rszvb_DiagramAreaAdd', rszvbDLL), paramflags)
rszvb_DiagramAreaAdd.name = 'rszvb_DiagramAreaAdd'
rszvb_DiagramAreaAdd.errcheck = __errorcheck__
rszvb_DiagramAreaAdd.output = False
# rszvb_DiagramAreaDelete ['ViSession instrumentHandle', 'ViInt32 window']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),)
rszvb_DiagramAreaDelete  = prototype(('rszvb_DiagramAreaDelete', rszvbDLL), paramflags)
rszvb_DiagramAreaDelete.name = 'rszvb_DiagramAreaDelete'
rszvb_DiagramAreaDelete.errcheck = __errorcheck__
rszvb_DiagramAreaDelete.output = False
# rszvb_DiagramAreaMaximize ['ViSession instrumentHandle', 'ViInt32 window', 'ViInt32 diagramArea']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'diagramArea'),)
rszvb_DiagramAreaMaximize  = prototype(('rszvb_DiagramAreaMaximize', rszvbDLL), paramflags)
rszvb_DiagramAreaMaximize.name = 'rszvb_DiagramAreaMaximize'
rszvb_DiagramAreaMaximize.errcheck = __errorcheck__
rszvb_DiagramAreaMaximize.output = False
# rszvb_DiagramAreaTitle ['ViSession instrumentHandle', 'ViInt32 window', 'ViBoolean title', 'ViString titleString']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'title'),(1, 'titleString'),)
rszvb_DiagramAreaTitle  = prototype(('rszvb_DiagramAreaTitle', rszvbDLL), paramflags)
rszvb_DiagramAreaTitle.name = 'rszvb_DiagramAreaTitle'
rszvb_DiagramAreaTitle.errcheck = __errorcheck__
rszvb_DiagramAreaTitle.output = False
# rszvb_DiagramAreaName ['ViSession instrumentHandle', 'ViInt32 window', 'ViString areaName']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'areaName'),)
rszvb_DiagramAreaName  = prototype(('rszvb_DiagramAreaName', rszvbDLL), paramflags)
rszvb_DiagramAreaName.name = 'rszvb_DiagramAreaName'
rszvb_DiagramAreaName.errcheck = __errorcheck__
rszvb_DiagramAreaName.output = False
# rszvb_DiagramAreaCatalog ['ViSession instrumentHandle', 'ViInt32 window', 'ViChar _VI_FAR catalog[]', 'ViInt32 bufferSize']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'catalog[]'),(1, 'bufferSize'),)
rszvb_DiagramAreaCatalog  = prototype(('rszvb_DiagramAreaCatalog', rszvbDLL), paramflags)
rszvb_DiagramAreaCatalog.name = 'rszvb_DiagramAreaCatalog'
rszvb_DiagramAreaCatalog.errcheck = __errorcheck__
rszvb_DiagramAreaCatalog.output = False
# rszvb_TraceDiagramAreaCatalog ['ViSession instrumentHandle', 'ViInt32 window', 'ViChar _VI_FAR catalog[]', 'ViInt32 bufferSize']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'window'),(1, 'catalog[]'),(1, 'bufferSize'),)
rszvb_TraceDiagramAreaCatalog  = prototype(('rszvb_TraceDiagramAreaCatalog', rszvbDLL), paramflags)
rszvb_TraceDiagramAreaCatalog.name = 'rszvb_TraceDiagramAreaCatalog'
rszvb_TraceDiagramAreaCatalog.errcheck = __errorcheck__
rszvb_TraceDiagramAreaCatalog.output = False
# rszvb_SetColorScheme ['ViSession instrumentHandle', 'ViInt32 colorScheme']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'colorScheme'),)
rszvb_SetColorScheme  = prototype(('rszvb_SetColorScheme', rszvbDLL), paramflags)
rszvb_SetColorScheme.name = 'rszvb_SetColorScheme'
rszvb_SetColorScheme.errcheck = __errorcheck__
rszvb_SetColorScheme.output = False
# rszvb_GetColorScheme ['ViSession instrumentHandle', 'ViInt32* colorScheme']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'colorScheme'),)
rszvb_GetColorScheme  = prototype(('rszvb_GetColorScheme', rszvbDLL), paramflags)
rszvb_GetColorScheme.name = 'rszvb_GetColorScheme'
rszvb_GetColorScheme.errcheck = __errorcheck__
rszvb_GetColorScheme.output = True
# rszvb_SaveColorScheme ['ViSession instrumentHandle', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),)
rszvb_SaveColorScheme  = prototype(('rszvb_SaveColorScheme', rszvbDLL), paramflags)
rszvb_SaveColorScheme.name = 'rszvb_SaveColorScheme'
rszvb_SaveColorScheme.errcheck = __errorcheck__
rszvb_SaveColorScheme.output = False
# rszvb_LoadColorScheme ['ViSession instrumentHandle', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),)
rszvb_LoadColorScheme  = prototype(('rszvb_LoadColorScheme', rszvbDLL), paramflags)
rszvb_LoadColorScheme.name = 'rszvb_LoadColorScheme'
rszvb_LoadColorScheme.errcheck = __errorcheck__
rszvb_LoadColorScheme.output = False
# rszvb_SetFrequencyInfo ['ViSession instrumentHandle', 'ViBoolean frequencyInfo']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'frequencyInfo'),)
rszvb_SetFrequencyInfo  = prototype(('rszvb_SetFrequencyInfo', rszvbDLL), paramflags)
rszvb_SetFrequencyInfo.name = 'rszvb_SetFrequencyInfo'
rszvb_SetFrequencyInfo.errcheck = __errorcheck__
rszvb_SetFrequencyInfo.output = False
# rszvb_GetFrequencyInfo ['ViSession instrumentHandle', 'ViBoolean* frequencyInfo']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'frequencyInfo'),)
rszvb_GetFrequencyInfo  = prototype(('rszvb_GetFrequencyInfo', rszvbDLL), paramflags)
rszvb_GetFrequencyInfo.name = 'rszvb_GetFrequencyInfo'
rszvb_GetFrequencyInfo.errcheck = __errorcheck__
rszvb_GetFrequencyInfo.output = True
# rszvb_SetFontSize ['ViSession instrumentHandle', 'ViInt32 fontSize']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'fontSize'),)
rszvb_SetFontSize  = prototype(('rszvb_SetFontSize', rszvbDLL), paramflags)
rszvb_SetFontSize.name = 'rszvb_SetFontSize'
rszvb_SetFontSize.errcheck = __errorcheck__
rszvb_SetFontSize.output = False
# rszvb_GetFontSize ['ViSession instrumentHandle', 'ViInt32* fontSize']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'fontSize'),)
rszvb_GetFontSize  = prototype(('rszvb_GetFontSize', rszvbDLL), paramflags)
rszvb_GetFontSize.name = 'rszvb_GetFontSize'
rszvb_GetFontSize.errcheck = __errorcheck__
rszvb_GetFontSize.output = True
# rszvb_SetChannelInfo ['ViSession instrumentHandle', 'ViBoolean channelInfo']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channelInfo'),)
rszvb_SetChannelInfo  = prototype(('rszvb_SetChannelInfo', rszvbDLL), paramflags)
rszvb_SetChannelInfo.name = 'rszvb_SetChannelInfo'
rszvb_SetChannelInfo.errcheck = __errorcheck__
rszvb_SetChannelInfo.output = False
# rszvb_GetChannelInfo ['ViSession instrumentHandle', 'ViBoolean* channelInfo']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'channelInfo'),)
rszvb_GetChannelInfo  = prototype(('rszvb_GetChannelInfo', rszvbDLL), paramflags)
rszvb_GetChannelInfo.name = 'rszvb_GetChannelInfo'
rszvb_GetChannelInfo.errcheck = __errorcheck__
rszvb_GetChannelInfo.output = True
# rszvb_SetMarkerColorState ['ViSession instrumentHandle', 'ViBoolean sameColor']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'sameColor'),)
rszvb_SetMarkerColorState  = prototype(('rszvb_SetMarkerColorState', rszvbDLL), paramflags)
rszvb_SetMarkerColorState.name = 'rszvb_SetMarkerColorState'
rszvb_SetMarkerColorState.errcheck = __errorcheck__
rszvb_SetMarkerColorState.output = False
# rszvb_GetMarkerColorState ['ViSession instrumentHandle', 'ViBoolean* sameColor']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'sameColor'),)
rszvb_GetMarkerColorState  = prototype(('rszvb_GetMarkerColorState', rszvbDLL), paramflags)
rszvb_GetMarkerColorState.name = 'rszvb_GetMarkerColorState'
rszvb_GetMarkerColorState.errcheck = __errorcheck__
rszvb_GetMarkerColorState.output = True
# rszvb_SetRGBColor ['ViSession instrumentHandle', 'ViInt32 element', 'ViReal64 red', 'ViReal64 green', 'ViReal64 blue', 'ViInt32 traceStyle', 'ViInt32 traceWidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_double,c_double,c_double,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'element'),(1, 'red'),(1, 'green'),(1, 'blue'),(1, 'traceStyle'),(1, 'traceWidth'),)
rszvb_SetRGBColor  = prototype(('rszvb_SetRGBColor', rszvbDLL), paramflags)
rszvb_SetRGBColor.name = 'rszvb_SetRGBColor'
rszvb_SetRGBColor.errcheck = __errorcheck__
rszvb_SetRGBColor.output = False
# rszvb_GetRGBColor ['ViSession instrumentHandle', 'ViInt32 element', 'ViReal64* red', 'ViReal64* green', 'ViReal64* blue', 'ViInt32* traceStyle', 'ViInt32* traceWidth']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_double),POINTER(c_double),POINTER(c_double),POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'element'),(2, 'red'),(2, 'green'),(2, 'blue'),(2, 'traceStyle'),(2, 'traceWidth'),)
rszvb_GetRGBColor  = prototype(('rszvb_GetRGBColor', rszvbDLL), paramflags)
rszvb_GetRGBColor.name = 'rszvb_GetRGBColor'
rszvb_GetRGBColor.errcheck = __errorcheck__
rszvb_GetRGBColor.output = True
# rszvb_SetTraceColorState ['ViSession instrumentHandle', 'ViBoolean traceColor']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'traceColor'),)
rszvb_SetTraceColorState  = prototype(('rszvb_SetTraceColorState', rszvbDLL), paramflags)
rszvb_SetTraceColorState.name = 'rszvb_SetTraceColorState'
rszvb_SetTraceColorState.errcheck = __errorcheck__
rszvb_SetTraceColorState.output = False
# rszvb_GetTraceColorState ['ViSession instrumentHandle', 'ViBoolean* traceColor']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'traceColor'),)
rszvb_GetTraceColorState  = prototype(('rszvb_GetTraceColorState', rszvbDLL), paramflags)
rszvb_GetTraceColorState.name = 'rszvb_GetTraceColorState'
rszvb_GetTraceColorState.errcheck = __errorcheck__
rszvb_GetTraceColorState.output = True
# rszvb_TraceSetRGBColor ['ViSession instrumentHandle', 'ViString traceName', 'ViReal64 red', 'ViReal64 green', 'ViReal64 blue', 'ViInt32 traceStyle', 'ViInt32 traceWidth']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_double,c_double,c_double,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(1, 'red'),(1, 'green'),(1, 'blue'),(1, 'traceStyle'),(1, 'traceWidth'),)
rszvb_TraceSetRGBColor  = prototype(('rszvb_TraceSetRGBColor', rszvbDLL), paramflags)
rszvb_TraceSetRGBColor.name = 'rszvb_TraceSetRGBColor'
rszvb_TraceSetRGBColor.errcheck = __errorcheck__
rszvb_TraceSetRGBColor.output = False
# rszvb_TraceGetRGBColor ['ViSession instrumentHandle', 'ViString traceName', 'ViReal64* red', 'ViReal64* green', 'ViReal64* blue', 'ViInt32* traceStyle', 'ViInt32* traceWidth']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,POINTER(c_double),POINTER(c_double),POINTER(c_double),POINTER(c_int32),POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'traceName'),(2, 'red'),(2, 'green'),(2, 'blue'),(2, 'traceStyle'),(2, 'traceWidth'),)
rszvb_TraceGetRGBColor  = prototype(('rszvb_TraceGetRGBColor', rszvbDLL), paramflags)
rszvb_TraceGetRGBColor.name = 'rszvb_TraceGetRGBColor'
rszvb_TraceGetRGBColor.errcheck = __errorcheck__
rszvb_TraceGetRGBColor.output = True
# rszvb_SetPowerPortLimitState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean limitState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'limitState'),)
rszvb_SetPowerPortLimitState  = prototype(('rszvb_SetPowerPortLimitState', rszvbDLL), paramflags)
rszvb_SetPowerPortLimitState.name = 'rszvb_SetPowerPortLimitState'
rszvb_SetPowerPortLimitState.errcheck = __errorcheck__
rszvb_SetPowerPortLimitState.output = False
# rszvb_GetPowerPortLimitState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* limitState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'limitState'),)
rszvb_GetPowerPortLimitState  = prototype(('rszvb_GetPowerPortLimitState', rszvbDLL), paramflags)
rszvb_GetPowerPortLimitState.name = 'rszvb_GetPowerPortLimitState'
rszvb_GetPowerPortLimitState.errcheck = __errorcheck__
rszvb_GetPowerPortLimitState.output = True
# rszvb_SetPowerPortLimitValue ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64 limitValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_double)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'limitValue'),)
rszvb_SetPowerPortLimitValue  = prototype(('rszvb_SetPowerPortLimitValue', rszvbDLL), paramflags)
rszvb_SetPowerPortLimitValue.name = 'rszvb_SetPowerPortLimitValue'
rszvb_SetPowerPortLimitValue.errcheck = __errorcheck__
rszvb_SetPowerPortLimitValue.output = False
# rszvb_GetPowerPortLimitValue ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViReal64* limitValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'limitValue'),)
rszvb_GetPowerPortLimitValue  = prototype(('rszvb_GetPowerPortLimitValue', rszvbDLL), paramflags)
rszvb_GetPowerPortLimitValue.name = 'rszvb_GetPowerPortLimitValue'
rszvb_GetPowerPortLimitValue.errcheck = __errorcheck__
rszvb_GetPowerPortLimitValue.output = True
# rszvb_SetPowerPortLimitDirectGeneratorAndReceiverState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean DRGAccessState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(1, 'DRGAccessState'),)
rszvb_SetPowerPortLimitDirectGeneratorAndReceiverState  = prototype(('rszvb_SetPowerPortLimitDirectGeneratorAndReceiverState', rszvbDLL), paramflags)
rszvb_SetPowerPortLimitDirectGeneratorAndReceiverState.name = 'rszvb_SetPowerPortLimitDirectGeneratorAndReceiverState'
rszvb_SetPowerPortLimitDirectGeneratorAndReceiverState.errcheck = __errorcheck__
rszvb_SetPowerPortLimitDirectGeneratorAndReceiverState.output = False
# rszvb_GetPowerPortLimitDirectGeneratorAndReceiverState ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 port', 'ViBoolean* DRGAccessState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'port'),(2, 'DRGAccessState'),)
rszvb_GetPowerPortLimitDirectGeneratorAndReceiverState  = prototype(('rszvb_GetPowerPortLimitDirectGeneratorAndReceiverState', rszvbDLL), paramflags)
rszvb_GetPowerPortLimitDirectGeneratorAndReceiverState.name = 'rszvb_GetPowerPortLimitDirectGeneratorAndReceiverState'
rszvb_GetPowerPortLimitDirectGeneratorAndReceiverState.errcheck = __errorcheck__
rszvb_GetPowerPortLimitDirectGeneratorAndReceiverState.output = True
# rszvb_SetPresets ['ViSession instrumentHandle', 'ViInt32 presetScope']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'presetScope'),)
rszvb_SetPresets  = prototype(('rszvb_SetPresets', rszvbDLL), paramflags)
rszvb_SetPresets.name = 'rszvb_SetPresets'
rszvb_SetPresets.errcheck = __errorcheck__
rszvb_SetPresets.output = False
# rszvb_GetPresets ['ViSession instrumentHandle', 'ViInt32* presetScope']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'presetScope'),)
rszvb_GetPresets  = prototype(('rszvb_GetPresets', rszvbDLL), paramflags)
rszvb_GetPresets.name = 'rszvb_GetPresets'
rszvb_GetPresets.errcheck = __errorcheck__
rszvb_GetPresets.output = True
# rszvb_SetPresetSettingsState ['ViSession instrumentHandle', 'ViBoolean state']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'state'),)
rszvb_SetPresetSettingsState  = prototype(('rszvb_SetPresetSettingsState', rszvbDLL), paramflags)
rszvb_SetPresetSettingsState.name = 'rszvb_SetPresetSettingsState'
rszvb_SetPresetSettingsState.errcheck = __errorcheck__
rszvb_SetPresetSettingsState.output = False
# rszvb_GetPresetSettingsState ['ViSession instrumentHandle', 'ViBoolean* state']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'state'),)
rszvb_GetPresetSettingsState  = prototype(('rszvb_GetPresetSettingsState', rszvbDLL), paramflags)
rszvb_GetPresetSettingsState.name = 'rszvb_GetPresetSettingsState'
rszvb_GetPresetSettingsState.errcheck = __errorcheck__
rszvb_GetPresetSettingsState.output = True
# rszvb_SetUserDefinedPresetState ['ViSession instrumentHandle', 'ViBoolean userDefinedPreset']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'userDefinedPreset'),)
rszvb_SetUserDefinedPresetState  = prototype(('rszvb_SetUserDefinedPresetState', rszvbDLL), paramflags)
rszvb_SetUserDefinedPresetState.name = 'rszvb_SetUserDefinedPresetState'
rszvb_SetUserDefinedPresetState.errcheck = __errorcheck__
rszvb_SetUserDefinedPresetState.output = False
# rszvb_GetUserDefinedPresetState ['ViSession instrumentHandle', 'ViBoolean* userDefinedPreset']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'userDefinedPreset'),)
rszvb_GetUserDefinedPresetState  = prototype(('rszvb_GetUserDefinedPresetState', rszvbDLL), paramflags)
rszvb_GetUserDefinedPresetState.name = 'rszvb_GetUserDefinedPresetState'
rszvb_GetUserDefinedPresetState.errcheck = __errorcheck__
rszvb_GetUserDefinedPresetState.output = True
# rszvb_SetUserDefinedPresetFile ['ViSession instrumentHandle', 'ViString userDefinedPresetFile']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'userDefinedPresetFile'),)
rszvb_SetUserDefinedPresetFile  = prototype(('rszvb_SetUserDefinedPresetFile', rszvbDLL), paramflags)
rszvb_SetUserDefinedPresetFile.name = 'rszvb_SetUserDefinedPresetFile'
rszvb_SetUserDefinedPresetFile.errcheck = __errorcheck__
rszvb_SetUserDefinedPresetFile.output = False
# rszvb_GetUserDefinedPresetFile ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR userDefinedPresetFile[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'userDefinedPresetFile[]'),)
rszvb_GetUserDefinedPresetFile  = prototype(('rszvb_GetUserDefinedPresetFile', rszvbDLL), paramflags)
rszvb_GetUserDefinedPresetFile.name = 'rszvb_GetUserDefinedPresetFile'
rszvb_GetUserDefinedPresetFile.errcheck = __errorcheck__
rszvb_GetUserDefinedPresetFile.output = False
# rszvb_SetDisplayUpdate ['ViSession instrumentHandle', 'ViInt32 displayUpdate']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'displayUpdate'),)
rszvb_SetDisplayUpdate  = prototype(('rszvb_SetDisplayUpdate', rszvbDLL), paramflags)
rszvb_SetDisplayUpdate.name = 'rszvb_SetDisplayUpdate'
rszvb_SetDisplayUpdate.errcheck = __errorcheck__
rszvb_SetDisplayUpdate.output = False
# rszvb_GetDisplayUpdate ['ViSession instrumentHandle', 'ViInt32* displayUpdate']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'displayUpdate'),)
rszvb_GetDisplayUpdate  = prototype(('rszvb_GetDisplayUpdate', rszvbDLL), paramflags)
rszvb_GetDisplayUpdate.name = 'rszvb_GetDisplayUpdate'
rszvb_GetDisplayUpdate.errcheck = __errorcheck__
rszvb_GetDisplayUpdate.output = True
# rszvb_ImmediateSettingsUpdate ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_ImmediateSettingsUpdate  = prototype(('rszvb_ImmediateSettingsUpdate', rszvbDLL), paramflags)
rszvb_ImmediateSettingsUpdate.name = 'rszvb_ImmediateSettingsUpdate'
rszvb_ImmediateSettingsUpdate.errcheck = __errorcheck__
rszvb_ImmediateSettingsUpdate.output = False
# rszvb_QueryFrequencyRange ['ViSession instrumentHandle', 'ViReal64* minimumFrequency', 'ViReal64* maximumFrequency']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_double),POINTER(c_double))
paramflags = ((1, 'instrumentHandle'),(2, 'minimumFrequency'),(2, 'maximumFrequency'),)
rszvb_QueryFrequencyRange  = prototype(('rszvb_QueryFrequencyRange', rszvbDLL), paramflags)
rszvb_QueryFrequencyRange.name = 'rszvb_QueryFrequencyRange'
rszvb_QueryFrequencyRange.errcheck = __errorcheck__
rszvb_QueryFrequencyRange.output = True
# rszvb_SystemKeylock ['ViSession instrumentHandle', 'ViBoolean lockout']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'lockout'),)
rszvb_SystemKeylock  = prototype(('rszvb_SystemKeylock', rszvbDLL), paramflags)
rszvb_SystemKeylock.name = 'rszvb_SystemKeylock'
rszvb_SystemKeylock.errcheck = __errorcheck__
rszvb_SystemKeylock.output = False
# rszvb_SetRemoteLanguage ['ViSession instrumentHandle', 'ViInt32 language']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'language'),)
rszvb_SetRemoteLanguage  = prototype(('rszvb_SetRemoteLanguage', rszvbDLL), paramflags)
rszvb_SetRemoteLanguage.name = 'rszvb_SetRemoteLanguage'
rszvb_SetRemoteLanguage.errcheck = __errorcheck__
rszvb_SetRemoteLanguage.output = False
# rszvb_GetRemoteLanguage ['ViSession instrumentHandle', 'ViInt32* language']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'language'),)
rszvb_GetRemoteLanguage  = prototype(('rszvb_GetRemoteLanguage', rszvbDLL), paramflags)
rszvb_GetRemoteLanguage.name = 'rszvb_GetRemoteLanguage'
rszvb_GetRemoteLanguage.errcheck = __errorcheck__
rszvb_GetRemoteLanguage.output = True
# rszvb_ConfigureExternalGenerator ['ViSession instrumentHandle', 'ViInt32 generatorNumber', 'ViString generatorName', 'ViString generatorType', 'ViString interfaceType', 'ViString interfaceAddress', 'ViBoolean fastSweepMode', 'ViBoolean _10MHzReferenceFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p,c_char_p,c_char_p,c_bool,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'generatorNumber'),(1, 'generatorName'),(1, 'generatorType'),(1, 'interfaceType'),(1, 'interfaceAddress'),(1, 'fastSweepMode'),(1, '_10MHzReferenceFrequency'),)
rszvb_ConfigureExternalGenerator  = prototype(('rszvb_ConfigureExternalGenerator', rszvbDLL), paramflags)
rszvb_ConfigureExternalGenerator.name = 'rszvb_ConfigureExternalGenerator'
rszvb_ConfigureExternalGenerator.errcheck = __errorcheck__
rszvb_ConfigureExternalGenerator.output = False
# rszvb_QueryExternalGenerator ['ViSession instrumentHandle', 'ViInt32 generatorNumber', 'ViChar _VI_FAR generatorName[]', 'ViChar _VI_FAR generatorType[]', 'ViChar _VI_FAR interfaceType[]', 'ViChar _VI_FAR interfaceAddress[]', 'ViBoolean* fastSweepMode', 'ViBoolean* _10MHzReferenceFrequency']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p,c_char_p,c_char_p,POINTER(c_bool),POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'generatorNumber'),(1, 'generatorName[]'),(1, 'generatorType[]'),(1, 'interfaceType[]'),(1, 'interfaceAddress[]'),(2, 'fastSweepMode'),(2, '_10MHzReferenceFrequency'),)
rszvb_QueryExternalGenerator  = prototype(('rszvb_QueryExternalGenerator', rszvbDLL), paramflags)
rszvb_QueryExternalGenerator.name = 'rszvb_QueryExternalGenerator'
rszvb_QueryExternalGenerator.errcheck = __errorcheck__
rszvb_QueryExternalGenerator.output = True
# rszvb_QueryExternalGeneratorCount ['ViSession instrumentHandle', 'ViInt32* generatorCount']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'generatorCount'),)
rszvb_QueryExternalGeneratorCount  = prototype(('rszvb_QueryExternalGeneratorCount', rszvbDLL), paramflags)
rszvb_QueryExternalGeneratorCount.name = 'rszvb_QueryExternalGeneratorCount'
rszvb_QueryExternalGeneratorCount.errcheck = __errorcheck__
rszvb_QueryExternalGeneratorCount.output = True
# rszvb_QueryExternalGeneratorNumbers ['ViSession instrumentHandle', 'ViInt32 arraySize', 'ViChar _VI_FAR generatorNumbers[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'arraySize'),(1, 'generatorNumbers[]'),)
rszvb_QueryExternalGeneratorNumbers  = prototype(('rszvb_QueryExternalGeneratorNumbers', rszvbDLL), paramflags)
rszvb_QueryExternalGeneratorNumbers.name = 'rszvb_QueryExternalGeneratorNumbers'
rszvb_QueryExternalGeneratorNumbers.errcheck = __errorcheck__
rszvb_QueryExternalGeneratorNumbers.output = False
# rszvb_DeleteExternalGenerator ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_DeleteExternalGenerator  = prototype(('rszvb_DeleteExternalGenerator', rszvbDLL), paramflags)
rszvb_DeleteExternalGenerator.name = 'rszvb_DeleteExternalGenerator'
rszvb_DeleteExternalGenerator.errcheck = __errorcheck__
rszvb_DeleteExternalGenerator.output = False
# rszvb_ConfigureExternalPowerMeter ['ViSession instrumentHandle', 'ViInt32 powerMeterNumber', 'ViString powerMeterName', 'ViString powerMeterType', 'ViString interfaceType', 'ViString interfaceAddress']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'powerMeterNumber'),(1, 'powerMeterName'),(1, 'powerMeterType'),(1, 'interfaceType'),(1, 'interfaceAddress'),)
rszvb_ConfigureExternalPowerMeter  = prototype(('rszvb_ConfigureExternalPowerMeter', rszvbDLL), paramflags)
rszvb_ConfigureExternalPowerMeter.name = 'rszvb_ConfigureExternalPowerMeter'
rszvb_ConfigureExternalPowerMeter.errcheck = __errorcheck__
rszvb_ConfigureExternalPowerMeter.output = False
# rszvb_QueryExternalPowerMeter ['ViSession instrumentHandle', 'ViInt32 powerMeterNumber', 'ViChar _VI_FAR powerMeterName[]', 'ViChar _VI_FAR powerMeterType[]', 'ViChar _VI_FAR interfaceType[]', 'ViChar _VI_FAR interfaceAddress[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,c_char_p,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'powerMeterNumber'),(1, 'powerMeterName[]'),(1, 'powerMeterType[]'),(1, 'interfaceType[]'),(1, 'interfaceAddress[]'),)
rszvb_QueryExternalPowerMeter  = prototype(('rszvb_QueryExternalPowerMeter', rszvbDLL), paramflags)
rszvb_QueryExternalPowerMeter.name = 'rszvb_QueryExternalPowerMeter'
rszvb_QueryExternalPowerMeter.errcheck = __errorcheck__
rszvb_QueryExternalPowerMeter.output = False
# rszvb_QueryExternalPowerMeterCount ['ViSession instrumentHandle', 'ViInt32* powerMeterCount']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'powerMeterCount'),)
rszvb_QueryExternalPowerMeterCount  = prototype(('rszvb_QueryExternalPowerMeterCount', rszvbDLL), paramflags)
rszvb_QueryExternalPowerMeterCount.name = 'rszvb_QueryExternalPowerMeterCount'
rszvb_QueryExternalPowerMeterCount.errcheck = __errorcheck__
rszvb_QueryExternalPowerMeterCount.output = True
# rszvb_QueryExternalPowerMeterNumbers ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR powerMeterNumber[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'powerMeterNumber[]'),)
rszvb_QueryExternalPowerMeterNumbers  = prototype(('rszvb_QueryExternalPowerMeterNumbers', rszvbDLL), paramflags)
rszvb_QueryExternalPowerMeterNumbers.name = 'rszvb_QueryExternalPowerMeterNumbers'
rszvb_QueryExternalPowerMeterNumbers.errcheck = __errorcheck__
rszvb_QueryExternalPowerMeterNumbers.output = False
# rszvb_AutoZeroingExternalPowerMeter ['ViSession instrumentHandle', 'ViInt32 powerMeterNumber']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'powerMeterNumber'),)
rszvb_AutoZeroingExternalPowerMeter  = prototype(('rszvb_AutoZeroingExternalPowerMeter', rszvbDLL), paramflags)
rszvb_AutoZeroingExternalPowerMeter.name = 'rszvb_AutoZeroingExternalPowerMeter'
rszvb_AutoZeroingExternalPowerMeter.errcheck = __errorcheck__
rszvb_AutoZeroingExternalPowerMeter.output = False
# rszvb_SetAutoConfigNRPZxx ['ViSession instrumentHandle', 'ViInt32 powerMeterNumber', 'ViBoolean autoConfig']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'powerMeterNumber'),(1, 'autoConfig'),)
rszvb_SetAutoConfigNRPZxx  = prototype(('rszvb_SetAutoConfigNRPZxx', rszvbDLL), paramflags)
rszvb_SetAutoConfigNRPZxx.name = 'rszvb_SetAutoConfigNRPZxx'
rszvb_SetAutoConfigNRPZxx.errcheck = __errorcheck__
rszvb_SetAutoConfigNRPZxx.output = False
# rszvb_GetAutoConfigNRPZxx ['ViSession instrumentHandle', 'ViInt32 powerMeterNumber', 'ViBoolean* autoConfig']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(1, 'powerMeterNumber'),(2, 'autoConfig'),)
rszvb_GetAutoConfigNRPZxx  = prototype(('rszvb_GetAutoConfigNRPZxx', rszvbDLL), paramflags)
rszvb_GetAutoConfigNRPZxx.name = 'rszvb_GetAutoConfigNRPZxx'
rszvb_GetAutoConfigNRPZxx.errcheck = __errorcheck__
rszvb_GetAutoConfigNRPZxx.output = True
# rszvb_DeleteExternalPowerMeter ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_DeleteExternalPowerMeter  = prototype(('rszvb_DeleteExternalPowerMeter', rszvbDLL), paramflags)
rszvb_DeleteExternalPowerMeter.name = 'rszvb_DeleteExternalPowerMeter'
rszvb_DeleteExternalPowerMeter.errcheck = __errorcheck__
rszvb_DeleteExternalPowerMeter.output = False
# rszvb_SetAlarmSoundsState ['ViSession instrumentHandle', 'ViBoolean alarmSounds']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'alarmSounds'),)
rszvb_SetAlarmSoundsState  = prototype(('rszvb_SetAlarmSoundsState', rszvbDLL), paramflags)
rszvb_SetAlarmSoundsState.name = 'rszvb_SetAlarmSoundsState'
rszvb_SetAlarmSoundsState.errcheck = __errorcheck__
rszvb_SetAlarmSoundsState.output = False
# rszvb_GetAlarmSoundsState ['ViSession instrumentHandle', 'ViBoolean* alarmSounds']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'alarmSounds'),)
rszvb_GetAlarmSoundsState  = prototype(('rszvb_GetAlarmSoundsState', rszvbDLL), paramflags)
rszvb_GetAlarmSoundsState.name = 'rszvb_GetAlarmSoundsState'
rszvb_GetAlarmSoundsState.errcheck = __errorcheck__
rszvb_GetAlarmSoundsState.output = True
# rszvb_SetRestartBehavior ['ViSession instrumentHandle', 'ViInt32 restartBehavior']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'restartBehavior'),)
rszvb_SetRestartBehavior  = prototype(('rszvb_SetRestartBehavior', rszvbDLL), paramflags)
rszvb_SetRestartBehavior.name = 'rszvb_SetRestartBehavior'
rszvb_SetRestartBehavior.errcheck = __errorcheck__
rszvb_SetRestartBehavior.output = False
# rszvb_GetRestartBehavior ['ViSession instrumentHandle', 'ViInt32* restartBehavior']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'restartBehavior'),)
rszvb_GetRestartBehavior  = prototype(('rszvb_GetRestartBehavior', rszvbDLL), paramflags)
rszvb_GetRestartBehavior.name = 'rszvb_GetRestartBehavior'
rszvb_GetRestartBehavior.errcheck = __errorcheck__
rszvb_GetRestartBehavior.output = True
# rszvb_SetStatusSoundsState ['ViSession instrumentHandle', 'ViBoolean statusSounds']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'statusSounds'),)
rszvb_SetStatusSoundsState  = prototype(('rszvb_SetStatusSoundsState', rszvbDLL), paramflags)
rszvb_SetStatusSoundsState.name = 'rszvb_SetStatusSoundsState'
rszvb_SetStatusSoundsState.errcheck = __errorcheck__
rszvb_SetStatusSoundsState.output = False
# rszvb_GetStatusSoundsState ['ViSession instrumentHandle', 'ViBoolean* statusSounds']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'statusSounds'),)
rszvb_GetStatusSoundsState  = prototype(('rszvb_GetStatusSoundsState', rszvbDLL), paramflags)
rszvb_GetStatusSoundsState.name = 'rszvb_GetStatusSoundsState'
rszvb_GetStatusSoundsState.errcheck = __errorcheck__
rszvb_GetStatusSoundsState.output = True
# rszvb_SetDataTransfer ['ViSession instrumentHandle', 'ViInt32 dataTransfer']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'dataTransfer'),)
rszvb_SetDataTransfer  = prototype(('rszvb_SetDataTransfer', rszvbDLL), paramflags)
rszvb_SetDataTransfer.name = 'rszvb_SetDataTransfer'
rszvb_SetDataTransfer.errcheck = __errorcheck__
rszvb_SetDataTransfer.output = False
# rszvb_GetDataTransfer ['ViSession instrumentHandle', 'ViInt32* dataTransfer']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'dataTransfer'),)
rszvb_GetDataTransfer  = prototype(('rszvb_GetDataTransfer', rszvbDLL), paramflags)
rszvb_GetDataTransfer.name = 'rszvb_GetDataTransfer'
rszvb_GetDataTransfer.errcheck = __errorcheck__
rszvb_GetDataTransfer.output = True
# rszvb_SetErrorDisplayState ['ViSession instrumentHandle', 'ViBoolean errorDisplay']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'errorDisplay'),)
rszvb_SetErrorDisplayState  = prototype(('rszvb_SetErrorDisplayState', rszvbDLL), paramflags)
rszvb_SetErrorDisplayState.name = 'rszvb_SetErrorDisplayState'
rszvb_SetErrorDisplayState.errcheck = __errorcheck__
rszvb_SetErrorDisplayState.output = False
# rszvb_GetErrorDisplayState ['ViSession instrumentHandle', 'ViBoolean* errorDisplay']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'errorDisplay'),)
rszvb_GetErrorDisplayState  = prototype(('rszvb_GetErrorDisplayState', rszvbDLL), paramflags)
rszvb_GetErrorDisplayState.name = 'rszvb_GetErrorDisplayState'
rszvb_GetErrorDisplayState.errcheck = __errorcheck__
rszvb_GetErrorDisplayState.output = True
# rszvb_SetFrequencyConversionType ['ViSession instrumentHandle', 'ViString converterType']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'converterType'),)
rszvb_SetFrequencyConversionType  = prototype(('rszvb_SetFrequencyConversionType', rszvbDLL), paramflags)
rszvb_SetFrequencyConversionType.name = 'rszvb_SetFrequencyConversionType'
rszvb_SetFrequencyConversionType.errcheck = __errorcheck__
rszvb_SetFrequencyConversionType.output = False
# rszvb_GetFrequencyConversionType ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR converterType[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'converterType[]'),)
rszvb_GetFrequencyConversionType  = prototype(('rszvb_GetFrequencyConversionType', rszvbDLL), paramflags)
rszvb_GetFrequencyConversionType.name = 'rszvb_GetFrequencyConversionType'
rszvb_GetFrequencyConversionType.errcheck = __errorcheck__
rszvb_GetFrequencyConversionType.output = False
# rszvb_SetFrequencyConversionSource ['ViSession instrumentHandle', 'ViInt32 conversionSource']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'conversionSource'),)
rszvb_SetFrequencyConversionSource  = prototype(('rszvb_SetFrequencyConversionSource', rszvbDLL), paramflags)
rszvb_SetFrequencyConversionSource.name = 'rszvb_SetFrequencyConversionSource'
rszvb_SetFrequencyConversionSource.errcheck = __errorcheck__
rszvb_SetFrequencyConversionSource.output = False
# rszvb_GetFrequencyConversionSource ['ViSession instrumentHandle', 'ViInt32* conversionSource']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'conversionSource'),)
rszvb_GetFrequencyConversionSource  = prototype(('rszvb_GetFrequencyConversionSource', rszvbDLL), paramflags)
rszvb_GetFrequencyConversionSource.name = 'rszvb_GetFrequencyConversionSource'
rszvb_GetFrequencyConversionSource.errcheck = __errorcheck__
rszvb_GetFrequencyConversionSource.output = True
# rszvb_SetFastMultiportCorrection ['ViSession instrumentHandle', 'ViBoolean fastMultiportCorrection']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'fastMultiportCorrection'),)
rszvb_SetFastMultiportCorrection  = prototype(('rszvb_SetFastMultiportCorrection', rszvbDLL), paramflags)
rszvb_SetFastMultiportCorrection.name = 'rszvb_SetFastMultiportCorrection'
rszvb_SetFastMultiportCorrection.errcheck = __errorcheck__
rszvb_SetFastMultiportCorrection.output = False
# rszvb_GetFastMultiportCorrection ['ViSession instrumentHandle', 'ViBoolean* fastMultiportCorrection']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'fastMultiportCorrection'),)
rszvb_GetFastMultiportCorrection  = prototype(('rszvb_GetFastMultiportCorrection', rszvbDLL), paramflags)
rszvb_GetFastMultiportCorrection.name = 'rszvb_GetFastMultiportCorrection'
rszvb_GetFastMultiportCorrection.errcheck = __errorcheck__
rszvb_GetFastMultiportCorrection.output = True
# rszvb_SetPowerCoeficients ['ViSession instrumentHandle', 'ViInt32 port', 'ViReal64 _VI_FAR coeficient[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'coeficient[]'),)
rszvb_SetPowerCoeficients  = prototype(('rszvb_SetPowerCoeficients', rszvbDLL), paramflags)
rszvb_SetPowerCoeficients.name = 'rszvb_SetPowerCoeficients'
rszvb_SetPowerCoeficients.errcheck = __errorcheck__
rszvb_SetPowerCoeficients.output = False
# rszvb_GetPowerCoeficients ['ViSession instrumentHandle', 'ViInt32 port', 'ViReal64 _VI_FAR coeficients[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,numpy.ctypeslib.ndpointer(dtype=numpy.float64))
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'coeficients[]'),)
rszvb_GetPowerCoeficients  = prototype(('rszvb_GetPowerCoeficients', rszvbDLL), paramflags)
rszvb_GetPowerCoeficients.name = 'rszvb_GetPowerCoeficients'
rszvb_GetPowerCoeficients.errcheck = __errorcheck__
rszvb_GetPowerCoeficients.output = False
# rszvb_SetPowerCoeficientsDefault ['ViSession instrumentHandle', 'ViBoolean defaultCoeficients']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'defaultCoeficients'),)
rszvb_SetPowerCoeficientsDefault  = prototype(('rszvb_SetPowerCoeficientsDefault', rszvbDLL), paramflags)
rszvb_SetPowerCoeficientsDefault.name = 'rszvb_SetPowerCoeficientsDefault'
rszvb_SetPowerCoeficientsDefault.errcheck = __errorcheck__
rszvb_SetPowerCoeficientsDefault.output = False
# rszvb_GetPowerCoeficientsDefault ['ViSession instrumentHandle', 'ViBoolean* defaultCoeficients']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'defaultCoeficients'),)
rszvb_GetPowerCoeficientsDefault  = prototype(('rszvb_GetPowerCoeficientsDefault', rszvbDLL), paramflags)
rszvb_GetPowerCoeficientsDefault.name = 'rszvb_GetPowerCoeficientsDefault'
rszvb_GetPowerCoeficientsDefault.errcheck = __errorcheck__
rszvb_GetPowerCoeficientsDefault.output = True
# rszvb_QueryExtensionUnitDeviceID ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR deviceID[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'deviceID[]'),)
rszvb_QueryExtensionUnitDeviceID  = prototype(('rszvb_QueryExtensionUnitDeviceID', rszvbDLL), paramflags)
rszvb_QueryExtensionUnitDeviceID.name = 'rszvb_QueryExtensionUnitDeviceID'
rszvb_QueryExtensionUnitDeviceID.errcheck = __errorcheck__
rszvb_QueryExtensionUnitDeviceID.output = False
# rszvb_QueryExtensionUnitHardwareOptions ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR options[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'options[]'),)
rszvb_QueryExtensionUnitHardwareOptions  = prototype(('rszvb_QueryExtensionUnitHardwareOptions', rszvbDLL), paramflags)
rszvb_QueryExtensionUnitHardwareOptions.name = 'rszvb_QueryExtensionUnitHardwareOptions'
rszvb_QueryExtensionUnitHardwareOptions.errcheck = __errorcheck__
rszvb_QueryExtensionUnitHardwareOptions.output = False
# rszvb_SetNWAApplicationPriority ['ViSession instrumentHandle', 'ViInt32 priority']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'priority'),)
rszvb_SetNWAApplicationPriority  = prototype(('rszvb_SetNWAApplicationPriority', rszvbDLL), paramflags)
rszvb_SetNWAApplicationPriority.name = 'rszvb_SetNWAApplicationPriority'
rszvb_SetNWAApplicationPriority.errcheck = __errorcheck__
rszvb_SetNWAApplicationPriority.output = False
# rszvb_GetNWAApplicationPriority ['ViSession instrumentHandle', 'ViInt32* priority']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'priority'),)
rszvb_GetNWAApplicationPriority  = prototype(('rszvb_GetNWAApplicationPriority', rszvbDLL), paramflags)
rszvb_GetNWAApplicationPriority.name = 'rszvb_GetNWAApplicationPriority'
rszvb_GetNWAApplicationPriority.errcheck = __errorcheck__
rszvb_GetNWAApplicationPriority.output = True
# rszvb_SystemShutdown ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_SystemShutdown  = prototype(('rszvb_SystemShutdown', rszvbDLL), paramflags)
rszvb_SystemShutdown.name = 'rszvb_SystemShutdown'
rszvb_SystemShutdown.errcheck = __errorcheck__
rszvb_SystemShutdown.output = False
# rszvb_GenerateSystemReport ['ViSession instrumentHandle', 'ViString fileName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'fileName'),)
rszvb_GenerateSystemReport  = prototype(('rszvb_GenerateSystemReport', rszvbDLL), paramflags)
rszvb_GenerateSystemReport.name = 'rszvb_GenerateSystemReport'
rszvb_GenerateSystemReport.errcheck = __errorcheck__
rszvb_GenerateSystemReport.output = False
# rszvb_SetCalculationOfBandfilterCenterFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 marker', 'ViInt32 centerFrequencyCalculation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'marker'),(1, 'centerFrequencyCalculation'),)
rszvb_SetCalculationOfBandfilterCenterFrequency  = prototype(('rszvb_SetCalculationOfBandfilterCenterFrequency', rszvbDLL), paramflags)
rszvb_SetCalculationOfBandfilterCenterFrequency.name = 'rszvb_SetCalculationOfBandfilterCenterFrequency'
rszvb_SetCalculationOfBandfilterCenterFrequency.errcheck = __errorcheck__
rszvb_SetCalculationOfBandfilterCenterFrequency.output = False
# rszvb_GetCalculationOfBandfilterCenterFrequency ['ViSession instrumentHandle', 'ViInt32 channel', 'ViInt32 marker', 'ViInt32* centerFrequencyCalculation']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'channel',1),(1, 'marker'),(2, 'centerFrequencyCalculation'),)
rszvb_GetCalculationOfBandfilterCenterFrequency  = prototype(('rszvb_GetCalculationOfBandfilterCenterFrequency', rszvbDLL), paramflags)
rszvb_GetCalculationOfBandfilterCenterFrequency.name = 'rszvb_GetCalculationOfBandfilterCenterFrequency'
rszvb_GetCalculationOfBandfilterCenterFrequency.errcheck = __errorcheck__
rszvb_GetCalculationOfBandfilterCenterFrequency.output = True
# rszvb_SetRFOffBehavior ['ViSession instrumentHandle', 'ViInt32 RFOffBehavior']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'RFOffBehavior'),)
rszvb_SetRFOffBehavior  = prototype(('rszvb_SetRFOffBehavior', rszvbDLL), paramflags)
rszvb_SetRFOffBehavior.name = 'rszvb_SetRFOffBehavior'
rszvb_SetRFOffBehavior.errcheck = __errorcheck__
rszvb_SetRFOffBehavior.output = False
# rszvb_GetRFOffBehavior ['ViSession instrumentHandle', 'ViInt32* RFOffBehavior']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'RFOffBehavior'),)
rszvb_GetRFOffBehavior  = prototype(('rszvb_GetRFOffBehavior', rszvbDLL), paramflags)
rszvb_GetRFOffBehavior.name = 'rszvb_GetRFOffBehavior'
rszvb_GetRFOffBehavior.errcheck = __errorcheck__
rszvb_GetRFOffBehavior.output = True
# rszvb_SetRemoteDisplayTitle ['ViSession instrumentHandle', 'ViString title']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'title'),)
rszvb_SetRemoteDisplayTitle  = prototype(('rszvb_SetRemoteDisplayTitle', rszvbDLL), paramflags)
rszvb_SetRemoteDisplayTitle.name = 'rszvb_SetRemoteDisplayTitle'
rszvb_SetRemoteDisplayTitle.errcheck = __errorcheck__
rszvb_SetRemoteDisplayTitle.output = False
# rszvb_GetRemoteDisplayTitle ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR title[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'title[]'),)
rszvb_GetRemoteDisplayTitle  = prototype(('rszvb_GetRemoteDisplayTitle', rszvbDLL), paramflags)
rszvb_GetRemoteDisplayTitle.name = 'rszvb_GetRemoteDisplayTitle'
rszvb_GetRemoteDisplayTitle.errcheck = __errorcheck__
rszvb_GetRemoteDisplayTitle.output = False
# rszvb_SetAnalyzerHostname ['ViSession instrumentHandle', 'ViString hostName']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'hostName'),)
rszvb_SetAnalyzerHostname  = prototype(('rszvb_SetAnalyzerHostname', rszvbDLL), paramflags)
rszvb_SetAnalyzerHostname.name = 'rszvb_SetAnalyzerHostname'
rszvb_SetAnalyzerHostname.errcheck = __errorcheck__
rszvb_SetAnalyzerHostname.output = False
# rszvb_GetAnalyzerHostname ['ViSession instrumentHandle', 'ViInt32 bufferSize', 'ViChar _VI_FAR hostName[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'bufferSize'),(1, 'hostName[]'),)
rszvb_GetAnalyzerHostname  = prototype(('rszvb_GetAnalyzerHostname', rszvbDLL), paramflags)
rszvb_GetAnalyzerHostname.name = 'rszvb_GetAnalyzerHostname'
rszvb_GetAnalyzerHostname.errcheck = __errorcheck__
rszvb_GetAnalyzerHostname.output = False
# rszvb_SetSoftKeyLabel ['ViSession instrumentHandle', 'ViInt32 keyNumber', 'ViString label']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'keyNumber'),(1, 'label'),)
rszvb_SetSoftKeyLabel  = prototype(('rszvb_SetSoftKeyLabel', rszvbDLL), paramflags)
rszvb_SetSoftKeyLabel.name = 'rszvb_SetSoftKeyLabel'
rszvb_SetSoftKeyLabel.errcheck = __errorcheck__
rszvb_SetSoftKeyLabel.output = False
# rszvb_GetPressedSoftKey ['ViSession instrumentHandle', 'ViInt32* keyNumber', 'ViInt32 bufferSize', 'ViChar _VI_FAR label[]']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32),c_int32,c_char_p)
paramflags = ((1, 'instrumentHandle'),(2, 'keyNumber'),(1, 'bufferSize'),(1, 'label[]'),)
rszvb_GetPressedSoftKey  = prototype(('rszvb_GetPressedSoftKey', rszvbDLL), paramflags)
rszvb_GetPressedSoftKey.name = 'rszvb_GetPressedSoftKey'
rszvb_GetPressedSoftKey.errcheck = __errorcheck__
rszvb_GetPressedSoftKey.output = True
# rszvb_SetOutputPortBits ['ViSession instrumentHandle', 'ViInt32 outputPort', 'ViInt32 portBits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'outputPort'),(1, 'portBits'),)
rszvb_SetOutputPortBits  = prototype(('rszvb_SetOutputPortBits', rszvbDLL), paramflags)
rszvb_SetOutputPortBits.name = 'rszvb_SetOutputPortBits'
rszvb_SetOutputPortBits.errcheck = __errorcheck__
rszvb_SetOutputPortBits.output = False
# rszvb_GetOutputPortBits ['ViSession instrumentHandle', 'ViInt32 outputPort', 'ViInt32* portBits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'outputPort'),(2, 'portBits'),)
rszvb_GetOutputPortBits  = prototype(('rszvb_GetOutputPortBits', rszvbDLL), paramflags)
rszvb_GetOutputPortBits.name = 'rszvb_GetOutputPortBits'
rszvb_GetOutputPortBits.errcheck = __errorcheck__
rszvb_GetOutputPortBits.output = True
# rszvb_SetChannelBits ['ViSession instrumentHandle', 'ViInt32 channelBits']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'channelBits'),)
rszvb_SetChannelBits  = prototype(('rszvb_SetChannelBits', rszvbDLL), paramflags)
rszvb_SetChannelBits.name = 'rszvb_SetChannelBits'
rszvb_SetChannelBits.errcheck = __errorcheck__
rszvb_SetChannelBits.output = False
# rszvb_GetChannelBits ['ViSession instrumentHandle', 'ViInt32* channelBits']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'channelBits'),)
rszvb_GetChannelBits  = prototype(('rszvb_GetChannelBits', rszvbDLL), paramflags)
rszvb_GetChannelBits.name = 'rszvb_GetChannelBits'
rszvb_GetChannelBits.errcheck = __errorcheck__
rszvb_GetChannelBits.output = True
# rszvb_SetUIDirection ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32 direction']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'direction'),)
rszvb_SetUIDirection  = prototype(('rszvb_SetUIDirection', rszvbDLL), paramflags)
rszvb_SetUIDirection.name = 'rszvb_SetUIDirection'
rszvb_SetUIDirection.errcheck = __errorcheck__
rszvb_SetUIDirection.output = False
# rszvb_GetUIDirection ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32* direction']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(2, 'direction'),)
rszvb_GetUIDirection  = prototype(('rszvb_GetUIDirection', rszvbDLL), paramflags)
rszvb_GetUIDirection.name = 'rszvb_GetUIDirection'
rszvb_GetUIDirection.errcheck = __errorcheck__
rszvb_GetUIDirection.output = True
# rszvb_SetUIData ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32 data']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'data'),)
rszvb_SetUIData  = prototype(('rszvb_SetUIData', rszvbDLL), paramflags)
rszvb_SetUIData.name = 'rszvb_SetUIData'
rszvb_SetUIData.errcheck = __errorcheck__
rszvb_SetUIData.output = False
# rszvb_GetUIData ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32* data']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(2, 'data'),)
rszvb_GetUIData  = prototype(('rszvb_GetUIData', rszvbDLL), paramflags)
rszvb_GetUIData.name = 'rszvb_GetUIData'
rszvb_GetUIData.errcheck = __errorcheck__
rszvb_GetUIData.output = True
# rszvb_SetUISignalPin20 ['ViSession instrumentHandle', 'ViBoolean pin20']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'pin20'),)
rszvb_SetUISignalPin20  = prototype(('rszvb_SetUISignalPin20', rszvbDLL), paramflags)
rszvb_SetUISignalPin20.name = 'rszvb_SetUISignalPin20'
rszvb_SetUISignalPin20.errcheck = __errorcheck__
rszvb_SetUISignalPin20.output = False
# rszvb_GetUISignalPin20 ['ViSession instrumentHandle', 'ViBoolean* pin20']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'pin20'),)
rszvb_GetUISignalPin20  = prototype(('rszvb_GetUISignalPin20', rszvbDLL), paramflags)
rszvb_GetUISignalPin20.name = 'rszvb_GetUISignalPin20'
rszvb_GetUISignalPin20.errcheck = __errorcheck__
rszvb_GetUISignalPin20.output = True
# rszvb_SetUISignalPin21 ['ViSession instrumentHandle', 'ViBoolean pin21']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'pin21'),)
rszvb_SetUISignalPin21  = prototype(('rszvb_SetUISignalPin21', rszvbDLL), paramflags)
rszvb_SetUISignalPin21.name = 'rszvb_SetUISignalPin21'
rszvb_SetUISignalPin21.errcheck = __errorcheck__
rszvb_SetUISignalPin21.output = False
# rszvb_GetUISignalPin21 ['ViSession instrumentHandle', 'ViBoolean* pin21']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_bool))
paramflags = ((1, 'instrumentHandle'),(2, 'pin21'),)
rszvb_GetUISignalPin21  = prototype(('rszvb_GetUISignalPin21', rszvbDLL), paramflags)
rszvb_GetUISignalPin21.name = 'rszvb_GetUISignalPin21'
rszvb_GetUISignalPin21.errcheck = __errorcheck__
rszvb_GetUISignalPin21.output = True
# rszvb_SetUIPortBinaryData ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32 data']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'data'),)
rszvb_SetUIPortBinaryData  = prototype(('rszvb_SetUIPortBinaryData', rszvbDLL), paramflags)
rszvb_SetUIPortBinaryData.name = 'rszvb_SetUIPortBinaryData'
rszvb_SetUIPortBinaryData.errcheck = __errorcheck__
rszvb_SetUIPortBinaryData.output = False
# rszvb_GetUIPortBinaryData ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32* data']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(2, 'data'),)
rszvb_GetUIPortBinaryData  = prototype(('rszvb_GetUIPortBinaryData', rszvbDLL), paramflags)
rszvb_GetUIPortBinaryData.name = 'rszvb_GetUIPortBinaryData'
rszvb_GetUIPortBinaryData.errcheck = __errorcheck__
rszvb_GetUIPortBinaryData.output = True
# rszvb_SetUIPortNextState ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32 nextState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(1, 'nextState'),)
rszvb_SetUIPortNextState  = prototype(('rszvb_SetUIPortNextState', rszvbDLL), paramflags)
rszvb_SetUIPortNextState.name = 'rszvb_SetUIPortNextState'
rszvb_SetUIPortNextState.errcheck = __errorcheck__
rszvb_SetUIPortNextState.output = False
# rszvb_GetUIPortNextState ['ViSession instrumentHandle', 'ViInt32 port', 'ViInt32* nextState']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'port'),(2, 'nextState'),)
rszvb_GetUIPortNextState  = prototype(('rszvb_GetUIPortNextState', rszvbDLL), paramflags)
rszvb_GetUIPortNextState.name = 'rszvb_GetUIPortNextState'
rszvb_GetUIPortNextState.errcheck = __errorcheck__
rszvb_GetUIPortNextState.output = True
# rszvb_RestoreUIDefaultStates ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_RestoreUIDefaultStates  = prototype(('rszvb_RestoreUIDefaultStates', rszvbDLL), paramflags)
rszvb_RestoreUIDefaultStates.name = 'rszvb_RestoreUIDefaultStates'
rszvb_RestoreUIDefaultStates.errcheck = __errorcheck__
rszvb_RestoreUIDefaultStates.output = False
# rszvb_setStatusRegister ['ViSession instrumentHandle', 'ViInt32 registerOperation', 'ViInt32 questionableRegister', 'ViInt32 enable', 'ViInt32 PTransition', 'ViInt32 NTransition']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_int32,c_int32,c_int32,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'registerOperation'),(1, 'questionableRegister'),(1, 'enable'),(1, 'PTransition'),(1, 'NTransition'),)
rszvb_setStatusRegister  = prototype(('rszvb_setStatusRegister', rszvbDLL), paramflags)
rszvb_setStatusRegister.name = 'rszvb_setStatusRegister'
rszvb_setStatusRegister.errcheck = __errorcheck__
rszvb_setStatusRegister.output = False
# rszvb_getStatusRegister ['ViSession instrumentHandle', 'ViInt32 statusRegistersQuery', 'ViInt32* registerValue']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'statusRegistersQuery'),(2, 'registerValue'),)
rszvb_getStatusRegister  = prototype(('rszvb_getStatusRegister', rszvbDLL), paramflags)
rszvb_getStatusRegister.name = 'rszvb_getStatusRegister'
rszvb_getStatusRegister.errcheck = __errorcheck__
rszvb_getStatusRegister.output = True
# rszvb_setTimeOut ['ViSession instrumentHandle', 'ViInt32 timeout']
prototype = WINFUNCTYPE(c_int, c_int,c_int32)
paramflags = ((1, 'instrumentHandle'),(1, 'timeout'),)
rszvb_setTimeOut  = prototype(('rszvb_setTimeOut', rszvbDLL), paramflags)
rszvb_setTimeOut.name = 'rszvb_setTimeOut'
rszvb_setTimeOut.errcheck = __errorcheck__
rszvb_setTimeOut.output = False
# rszvb_getTimeOut ['ViSession instrumentHandle', 'ViInt32* timeout']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(2, 'timeout'),)
rszvb_getTimeOut  = prototype(('rszvb_getTimeOut', rszvbDLL), paramflags)
rszvb_getTimeOut.name = 'rszvb_getTimeOut'
rszvb_getTimeOut.errcheck = __errorcheck__
rszvb_getTimeOut.output = True
# rszvb_errorCheckState ['ViSession instrumentHandle', 'ViBoolean stateChecking']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'stateChecking'),)
rszvb_errorCheckState  = prototype(('rszvb_errorCheckState', rszvbDLL), paramflags)
rszvb_errorCheckState.name = 'rszvb_errorCheckState'
rszvb_errorCheckState.errcheck = __errorcheck__
rszvb_errorCheckState.output = False
# rszvb_setCheckOption ['ViSession instrumentHandle', 'ViBoolean optionChecking']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'optionChecking'),)
rszvb_setCheckOption  = prototype(('rszvb_setCheckOption', rszvbDLL), paramflags)
rszvb_setCheckOption.name = 'rszvb_setCheckOption'
rszvb_setCheckOption.errcheck = __errorcheck__
rszvb_setCheckOption.output = False
# rszvb_setCheckRange ['ViSession instrumentHandle', 'ViBoolean rangeChecking']
prototype = WINFUNCTYPE(c_int, c_int,c_bool)
paramflags = ((1, 'instrumentHandle'),(1, 'rangeChecking'),)
rszvb_setCheckRange  = prototype(('rszvb_setCheckRange', rszvbDLL), paramflags)
rszvb_setCheckRange.name = 'rszvb_setCheckRange'
rszvb_setCheckRange.errcheck = __errorcheck__
rszvb_setCheckRange.output = False
# rszvb_writeInstrData ['ViSession instrumentHandle', 'ViString writeBuffer']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'writeBuffer'),)
rszvb_writeInstrData  = prototype(('rszvb_writeInstrData', rszvbDLL), paramflags)
rszvb_writeInstrData.name = 'rszvb_writeInstrData'
rszvb_writeInstrData.errcheck = __errorcheck__
rszvb_writeInstrData.output = False
# rszvb_readInstrData ['ViSession instrumentHandle', 'ViInt32 numberBytesToRead', 'ViChar _VI_FAR readBuffer[]', 'ViInt32* numBytesRead']
prototype = WINFUNCTYPE(c_int, c_int,c_int32,c_char_p,POINTER(c_int32))
paramflags = ((1, 'instrumentHandle'),(1, 'numberBytesToRead'),(1, 'readBuffer[]'),(2, 'numBytesRead'),)
rszvb_readInstrData  = prototype(('rszvb_readInstrData', rszvbDLL), paramflags)
rszvb_readInstrData.name = 'rszvb_readInstrData'
rszvb_readInstrData.errcheck = __errorcheck__
rszvb_readInstrData.output = True
# rszvb_reset ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_reset  = prototype(('rszvb_reset', rszvbDLL), paramflags)
rszvb_reset.name = 'rszvb_reset'
rszvb_reset.errcheck = __errorcheck__
rszvb_reset.output = False
# rszvb_self_test ['ViSession instrumentHandle', 'ViInt16* selfTestResult', 'ViChar _VI_FAR selfTestMessage[]']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int16),c_char_p)
paramflags = ((1, 'instrumentHandle'),(2, 'selfTestResult'),(1, 'selfTestMessage[]'),)
rszvb_self_test  = prototype(('rszvb_self_test', rszvbDLL), paramflags)
rszvb_self_test.name = 'rszvb_self_test'
rszvb_self_test.errcheck = __errorcheck__
rszvb_self_test.output = True
# rszvb_error_query ['ViSession instrumentHandle', 'ViInt32* errorCode', 'ViChar _VI_FAR errorMessage[]']
prototype = WINFUNCTYPE(c_int, c_int,POINTER(c_int32),c_char_p)
paramflags = ((1, 'instrumentHandle'),(2, 'errorCode'),(1, 'errorMessage[]'),)
rszvb_error_query  = prototype(('rszvb_error_query', rszvbDLL), paramflags)
rszvb_error_query.name = 'rszvb_error_query'
rszvb_error_query.errcheck = __errorcheck__
rszvb_error_query.output = True
# rszvb_error_message ['ViSession instrumentHandle', 'ViStatus statusCode', 'ViChar _VI_FAR message[]']
prototype = WINFUNCTYPE(c_int, c_int,c_int,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'statusCode'),(1, 'message[]'),)
rszvb_error_message  = prototype(('rszvb_error_message', rszvbDLL), paramflags)
rszvb_error_message.name = 'rszvb_error_message'
rszvb_error_message.errcheck = __errorcheck__
rszvb_error_message.output = False
# rszvb_revision_query ['ViSession instrumentHandle', 'ViChar _VI_FAR instrumentDriverRevision[]', 'ViChar _VI_FAR firmwareRevision[]']
prototype = WINFUNCTYPE(c_int, c_int,c_char_p,c_char_p)
paramflags = ((1, 'instrumentHandle'),(1, 'instrumentDriverRevision[]'),(1, 'firmwareRevision[]'),)
rszvb_revision_query  = prototype(('rszvb_revision_query', rszvbDLL), paramflags)
rszvb_revision_query.name = 'rszvb_revision_query'
rszvb_revision_query.errcheck = __errorcheck__
rszvb_revision_query.output = False
# rszvb_close ['ViSession instrumentHandle']
prototype = WINFUNCTYPE(c_int, c_int)
paramflags = ((1, 'instrumentHandle'),)
rszvb_close  = prototype(('rszvb_close', rszvbDLL), paramflags)
rszvb_close.name = 'rszvb_close'
rszvb_close.errcheck = __errorcheck__
rszvb_close.output = False
