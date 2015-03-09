/*= R&S ZVB Network Analyzer Include File ===================================*/

/*===========================================================================*/
/*  Please do not use global variables or arrays in the include file of      */
/*  instrument drivers that will be submitted for inclusion into the         */
/*  LabWindows Instrument Driver Library.                                    */
/*===========================================================================*/
     
#ifndef __RSZVB_HEADER
#define __RSZVB_HEADER

#include <visa.h>

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/*****************************************************************************/
/*= RSIB interface support ==================================================*/
/*                                                                           */
/* The RSIB interface is a R&S defined protocol for remote control of R&S    */
/* spectrum and network analyzers. In addition to the standard VISA          */
/* attributes, the RSIB passport supports the following manufacturer specific*/
/* attributes:                                                               */
/*                                                                           */
/*****************************************************************************/
#ifndef __RSVIRSIB_H__

#define RS_ATTR_RSIB_SRE     (0x3FFC0001UL)     /* Switch a device to local or remote */
#define RS_ATTR_RSIB_LOC     (0x3FFC0002UL)     /* Switch a device temporarily to local */
#define RS_ATTR_RSIB_VER     (0x3FFC0003UL)     /* Passport Release Version */

#endif /* __RSVIRSIB_H__ */

/*****************************************************************************/
/*= Instrument Driver Specific Error/Warning Codes ==========================*/
/*****************************************************************************/
#define VI_WARN_NSUP_ID_QUERY     (          0x3FFC0101L)
#define VI_WARN_NSUP_RESET        (          0x3FFC0102L)
#define VI_WARN_NSUP_SELF_TEST    (          0x3FFC0103L)
#define VI_WARN_NSUP_ERROR_QUERY  (          0x3FFC0104L)
#define VI_WARN_NSUP_REV_QUERY    (          0x3FFC0105L)

#define VI_ERROR_PARAMETER1       (_VI_ERROR+0x3FFC0001L)
#define VI_ERROR_PARAMETER2       (_VI_ERROR+0x3FFC0002L)
#define VI_ERROR_PARAMETER3       (_VI_ERROR+0x3FFC0003L)
#define VI_ERROR_PARAMETER4       (_VI_ERROR+0x3FFC0004L)
#define VI_ERROR_PARAMETER5       (_VI_ERROR+0x3FFC0005L)
#define VI_ERROR_PARAMETER6       (_VI_ERROR+0x3FFC0006L)
#define VI_ERROR_PARAMETER7       (_VI_ERROR+0x3FFC0007L)
#define VI_ERROR_PARAMETER8       (_VI_ERROR+0x3FFC0008L)
#define VI_ERROR_FAIL_ID_QUERY    (_VI_ERROR+0x3FFC0011L)
#define VI_ERROR_INV_RESPONSE     (_VI_ERROR+0x3FFC0012L)

#define VI_ERROR_INSTR_FILE_OPEN                (_VI_ERROR+0x3FFC0800L)
#define VI_ERROR_INSTR_FILE_WRITE               (_VI_ERROR+0x3FFC0801L)
#define VI_ERROR_INSTR_INTERPRETING_RESPONSE    (_VI_ERROR+0x3FFC0803L)
#define VI_ERROR_INSTR_PARAMETER9               (_VI_ERROR+0x3FFC0809L)
#define VI_ERROR_INSTR_PARAMETER10              (_VI_ERROR+0x3FFC080AL)
#define VI_ERROR_INSTR_PARAMETER11              (_VI_ERROR+0x3FFC080BL)
#define VI_ERROR_INSTR_PARAMETER12              (_VI_ERROR+0x3FFC080CL)
#define VI_ERROR_INSTR_PARAMETER13              (_VI_ERROR+0x3FFC080DL)
#define VI_ERROR_INSTR_PARAMETER14              (_VI_ERROR+0x3FFC080EL)
#define VI_ERROR_INSTR_PARAMETER15              (_VI_ERROR+0x3FFC080FL)

/*****************************************************************************/
/*= Define Instrument Specific Error/Warning Codes Here =====================*/
/*****************************************************************************/
#define VI_WARNING_INSTR_OFFSET                     (0x3FFC0900L)
#define VI_ERROR_INSTR_OFFSET                       (_VI_ERROR+0x3FFC0900L)

#define RSZVB_ERROR_INSTRUMENT_ERROR                (VI_ERROR_INSTR_OFFSET + 0xF0L)
#define RSZVB_ERROR_INVALID_CONFIGURATION           (VI_ERROR_INSTR_OFFSET + 0xF1L)
#define RSZVB_ERROR_INSTRUMENT_OPTION               (VI_ERROR_INSTR_OFFSET + 0xF2L)
#define RSZVB_ERROR_INSTRUMENT_DATA_NOT_AVAILABLE   (VI_ERROR_INSTR_OFFSET + 0xF3L)
#define RSZVB_ERROR_SETTINGS_CONFLICT               (VI_ERROR_INSTR_OFFSET + 0xF4L)
#define RSZVB_WARNING_SMALL_BUFFER                  (VI_WARNING_INSTR_OFFSET + 0xF5L)
#define RSZVB_ERROR_INSTRUMENT_NSUP_MODEL           (VI_ERROR_INSTR_OFFSET + 0xF6L)
#define RSZVB_ERROR_INSTRUMENT_IQ_OVERLOAD          (VI_ERROR_INSTR_OFFSET + 0xF7L)
#define RSZVB_ERROR_INSTRUMENT_NSUP_FIRMWARE        (VI_ERROR_INSTR_OFFSET + 0xF8L)
#define RSZVB_ERROR_NULL_POINTER_VALUE              (VI_ERROR_INSTR_OFFSET + 0xF9L)

/*****************************************************************************/
/*= Instrument specific defines =============================================*/
/*****************************************************************************/

/* --- File Format --------------------------------------------------------- */
#define RSZVB_EMF                                   0
#define RSZVB_BMP                                   1
#define RSZVB_JPG                                   2
#define RSZVB_PNG                                   3

/* --- Diagram Area -------------------------------------------------------- */
#define RSZVB_HCOPY_ALL                             0
#define RSZVB_HCOPY_ACTIVE                          1
#define RSZVB_HCOPY_SINGLE                          2

/* --- Page Orientation ---------------------------------------------------- */
#define RSZVB_PORTRAIT                              0
#define RSZVB_LANDSCAPE                             1

/* --- Operation to be Performed ------------------------------------------- */
#define RSZVB_FILE_MAN_CDRIVE                       0
#define RSZVB_FILE_MAN_CDIR                         1
#define RSZVB_FILE_MAN_MDIR                         2
#define RSZVB_FILE_MAN_RDIR                         3
#define RSZVB_FILE_MAN_COPY                         4
#define RSZVB_FILE_MAN_MOVE                         5
#define RSZVB_FILE_MAN_DELETE                       6
#define RSZVB_FILE_MAN_CDIR_DEF                     7

/* --- Out Mode ------------------------------------------------------------ */
#define RSZVB_SINGLE_ENDED                          0
#define RSZVB_DIFFERENTIAL                          1
#define RSZVB_COMMON                                2

/* --- Ratios -------------------------------------------------------------- */
#define RSZVB_RATIO_B2_A1_SRC_PORT_1                0
#define RSZVB_RATIO_B1_A1_SRC_PORT_1                1
#define RSZVB_RATIO_B2_B1_SRC_PORT_1                2
#define RSZVB_RATIO_B1_B2_SRC_PORT_1                3

/* --- Source Port --------------------------------------------------------- */
#define RSZVB_PORT_1                                1
#define RSZVB_PORT_2                                2
#define RSZVB_PORT_3                                3
#define RSZVB_PORT_4                                4

/* --- Power Meter --------------------------------------------------------- */
#define RSZVB_PWRM_1                                1
#define RSZVB_PWRM_2                                2

/* --- Numerator Type ------------------------------------------------------ */
#define RSZVB_A                                     0
#define RSZVB_B                                     1

/* --- Wave Quantities ----------------------------------------------------- */
#define RSZVB_WQUANTITY_A1_SRC_PORT_1               0
#define RSZVB_WQUANTITY_B1_SRC_PORT_1               1
#define RSZVB_WQUANTITY_B2_SRC_PORT_1               2
#define RSZVB_WQUANTITY_A2_SRC_PORT_2               3
#define RSZVB_WQUANTITY_B1_SRC_PORT_2               4
#define RSZVB_WQUANTITY_B2_SRC_PORT_2               5

/* --- Detectors ----------------------------------------------------------- */
#define RSZVB_DET_RMS                               0
#define RSZVB_DET_PEAK                              1
#define RSZVB_DET_AVG                               2

/* --- Stability Factor ---------------------------------------------------- */
#define RSZVB_SFACTOR_K                             0
#define RSZVB_SFACTOR_U1                            1
#define RSZVB_SFACTOR_U2                            2

/* --- DC Meas ------------------------------------------------------------- */
#define RSZVB_DC_MEAS_1V                            0
#define RSZVB_DC_MEAS_10V                           1

/* --- Test Model ---------------------------------------------------------- */
#define RSZVB_PAE_EXP_C10                           0
#define RSZVB_PAE_EXP_C1                            1
#define RSZVB_PAE_EXP_K101                          2
#define RSZVB_PAE_EXP_CK11                          3

/* --- Format--------------------------------------------------------------- */
#define RSZVB_DB_MAG                                0
#define RSZVB_PHASE                                 1
#define RSZVB_SMITH                                 2
#define RSZVB_POLAR                                 3
#define RSZVB_DELAY                                 4
#define RSZVB_SWR                                   5
#define RSZVB_LIN_MAG                               6
#define RSZVB_REAL                                  7
#define RSZVB_IMAG                                  8
#define RSZVB_ISMITH                                9
#define RSZVB_UPHASE                                10
#define RSZVB_DB_MAG_PHASE                          11
#define RSZVB_LIN_MAG_PHASE                         12
#define RSZVB_REAL_IMAG                             13
#define RSZVB_DEFAULT                               14
#define RSZVB_R_JX                                  15
#define RSZVB_G_JB                                  16

/* --- Sweep Type ---------------------------------------------------------- */
#define RSZVB_SWEEP_LIN                             0
#define RSZVB_SWEEP_LOG                             1
#define RSZVB_SWEEP_SEG                             2
#define RSZVB_SWEEP_POW                             3
#define RSZVB_SWEEP_TIM                             4
#define RSZVB_SWEEP_CW                              5
#define RSZVB_SWEEP_PULSE                           6
#define RSZVB_SWEEP_IAMP                            7
#define RSZVB_SWEEP_IPH                             8

/* --- Sweep Time Select --------------------------------------------------- */
#define RSZVB_SEG_TIME                              0
#define RSZVB_SEG_POINT                             1

/* --- Trigger On ---------------------------------------------------------- */
#define RSZVB_NEG                                   0
#define RSZVB_POS                                   1

/* --- Trigger Meas Sequence ----------------------------------------------- */
#define RSZVB_TRGSEQ_SWE                            0
#define RSZVB_TRGSEQ_SEGM                           1
#define RSZVB_TRGSEQ_POIN                           2
#define RSZVB_TRGSEQ_PPO                            3

/* --- Trigger Source ------------------------------------------------------ */
#define RSZVB_TRG_IMM                               0
#define RSZVB_TRG_EXT                               1
#define RSZVB_TRG_TIM                               2
#define RSZVB_TRG_MAN                               3
#define RSZVB_TRG_RFP                               4
#define RSZVB_TRG_PGE                               5

/* --- Single Sweep -------------------------------------------------------- */
#define RSZVB_SWEEP_SINGLE_CHAN                     0
#define RSZVB_SWEEP_ALL_CHAN                        1

/* --- Single Sweep -------------------------------------------------------- */
#define RSZVB_SWEEP_SINGLE                          0
#define RSZVB_SWEEP_CONT                            1

/* --- Spurious Avoidance -------------------------------------------------- */
#define RSZVB_AVOID_AUTO                            0
#define RSZVB_AVOID_POS                             1
#define RSZVB_AVOID_NEG                             2

/* --- Connector ----------------------------------------------------------- */
#define RSZVB_CONNECTOR_N50FEMALE                   0
#define RSZVB_CONNECTOR_N50MALE                     1
#define RSZVB_CONNECTOR_N75FEMALE                   2
#define RSZVB_CONNECTOR_N75MALE                     3
#define RSZVB_CONNECTOR_PC7                         4
#define RSZVB_CONNECTOR_PC35FEMALE                  5
#define RSZVB_CONNECTOR_PC35MALE                    6
#define RSZVB_CONNECTOR_PC292FEMALE                 7
#define RSZVB_CONNECTOR_PC292MALE                   8
#define RSZVB_CONNECTOR_UFEMALE1                    9
#define RSZVB_CONNECTOR_UMALE1                      10
#define RSZVB_CONNECTOR_UFEMALE2                    11
#define RSZVB_CONNECTOR_UMALE2                      12
#define RSZVB_CONNECTOR_SMAFEMALE                   13
#define RSZVB_CONNECTOR_SMAMALE                     14
#define RSZVB_CONNECTOR_PC1FEMALE                   15
#define RSZVB_CONNECTOR_PC1MALE                     16
#define RSZVB_CONNECTOR_PC185FEMALE                 17
#define RSZVB_CONNECTOR_PC185MALE                   18
#define RSZVB_CONNECTOR_PC24FEMALE                  19
#define RSZVB_CONNECTOR_PC24MALE                    20
    

/* --- Connector Kit ------------------------------------------------------- */
#define RSZVB_CONNECTOR_KIT_N50                     0
#define RSZVB_CONNECTOR_KIT_N75                     1
#define RSZVB_CONNECTOR_KIT_PC7                     2
#define RSZVB_CONNECTOR_KIT_PC35                    3
#define RSZVB_CONNECTOR_KIT_PC292                   4
#define RSZVB_CONNECTOR_KIT_USER1                   5
#define RSZVB_CONNECTOR_KIT_USER2                   6
#define RSZVB_CONNECTOR_KIT_SMA                     7

/* --- Parameters ---------------------------------------------------------- */
#define RSZVB_CALTYPE_REFL                          0
#define RSZVB_CALTYPE_RSH                           1
#define RSZVB_CALTYPE_FOP                           2
#define RSZVB_CALTYPE_FRTR                          3
#define RSZVB_CALTYPE_OPTP                          4
#define RSZVB_CALTYPE_TOSM                          5
#define RSZVB_CALTYPE_TOM                           6
#define RSZVB_CALTYPE_TRM                           7
#define RSZVB_CALTYPE_TRL                           8
#define RSZVB_CALTYPE_TNA                           9
#define RSZVB_CALTYPE_FNP                           10
#define RSZVB_CALTYPE_SFTP                          11
#define RSZVB_CALTYPE_UOSM                          12
#define RSZVB_CALTYPE_FTR                           13
#define RSZVB_CALTYPE_RTR                           14
#define RSZVB_CALTYPE_NMTR                          16
    
/* --- Standard ------------------------------------------------------------ */
#define RSZVB_CALCOLLSTD_THR                        0
#define RSZVB_CALCOLLSTD_OPEN1                      1
#define RSZVB_CALCOLLSTD_OPEN2                      2
#define RSZVB_CALCOLLSTD_OPEN12                     3
#define RSZVB_CALCOLLSTD_SHORT1                     4
#define RSZVB_CALCOLLSTD_SHORT2                     5
#define RSZVB_CALCOLLSTD_SHORT12                    6
#define RSZVB_CALCOLLSTD_MATCH1                     7
#define RSZVB_CALCOLLSTD_MATCH2                     8
#define RSZVB_CALCOLLSTD_MATCH12                    9
#define RSZVB_CALCOLLSTD_NET                        10
#define RSZVB_CALCOLLSTD_ATT                        11
#define RSZVB_CALCOLLSTD_REFL1                      12
#define RSZVB_CALCOLLSTD_REFL2                      13
#define RSZVB_CALCOLLSTD_LINE1                      14
#define RSZVB_CALCOLLSTD_LINE2                      15
#define RSZVB_CALCOLLSTD_M1O2                       16
#define RSZVB_CALCOLLSTD_O1M2                       17
#define RSZVB_CALCOLLSTD_M1S2                       18
#define RSZVB_CALCOLLSTD_S1M2                       19
#define RSZVB_CALCOLLSTD_OSH1                       20
#define RSZVB_CALCOLLSTD_OSH2                       21

/* --- Standard ------------------------------------------------------------ */
#define RSZVB_CALCOLLSTDGEN_THR                     0
#define RSZVB_CALCOLLSTDGEN_OPEN                    1
#define RSZVB_CALCOLLSTDGEN_SHORT                   2
#define RSZVB_CALCOLLSTDGEN_MATCH                   3
#define RSZVB_CALCOLLSTDGEN_NET                     4
#define RSZVB_CALCOLLSTDGEN_ATT                     5
#define RSZVB_CALCOLLSTDGEN_REFL                    6
#define RSZVB_CALCOLLSTDGEN_LINE                    7
#define RSZVB_CALCOLLSTDGEN_LINE_2                  8
#define RSZVB_CALCOLLSTDGEN_OSH                     9
#define RSZVB_CALCOLLSTDGEN_LINE_3                  10
#define RSZVB_CALCOLLSTDGEN_SLID                    11
#define RSZVB_CALCOLLSTDGEN_OSH_2                   12
#define RSZVB_CALCOLLSTDGEN_OSH_3                   13
#define RSZVB_CALCOLLSTDGEN_ISOL                    15

/* --- UTHR Standard ------------------------------------------------------------ */
#define RSZVB_CALCOLLSTDGEN_UTHR                    0
    
/* --- Operation to be Performed ------------------------------------------- */
#define RSZVB_CORR_MAN_COPY                         0
#define RSZVB_CORR_MAN_APPLY                        1
#define RSZVB_CORR_MAN_RESOLVE                      2
#define RSZVB_CORR_MAN_DELETE                       3
#define RSZVB_CORR_MAN_APPLY_ALL                    4
#define RSZVB_CORR_MAN_RESOLVE_ALL                  5
#define RSZVB_CORR_MAN_MERGE                        7

/* --- Connector Type ------------------------------------------------------ */
#define RSZVB_KIT_N50                               0
#define RSZVB_KIT_N75                               1
#define RSZVB_KIT_SMA                               2
#define RSZVB_KIT_PC7                               3
#define RSZVB_KIT_PC35                              4
#define RSZVB_KIT_USER1                             5
#define RSZVB_KIT_USER2                             6
#define RSZVB_KIT_PC292                             7

/* --- Approximation ------------------------------------------------------- */
#define RSZVB_OPEN                                  0
#define RSZVB_SHORT                                 1
#define RSZVB_MATCH                                 2
	
/* --- Diagram Area -------------------------------------------------------- */
#define RSZVB_RESTORE                               0
#define RSZVB_MAXIMIZE                              1

/* --- Preset Scope -------------------------------------------------------- */
#define RSZVB_PRESET_SINGLE                         0
#define RSZVB_PRESET_ALL                            1

/* --- Reference ----------------------------------------------------------- */
#define RSZVB_INT                                   0
#define RSZVB_EXT                                   1


/* --- Evaluation Range ---------------------------------------------------- */
#define RSZVB_FULL_SPAN                             0
#define RSZVB_RANGE_1                               1
#define RSZVB_RANGE_2                               2
#define RSZVB_RANGE_3                               3
#define RSZVB_RANGE_4                               4
#define RSZVB_RANGE_5                               5
#define RSZVB_RANGE_6                               6
#define RSZVB_RANGE_7                               7
#define RSZVB_RANGE_8                               8
#define RSZVB_RANGE_9                               9
#define RSZVB_RANGE_10                              10

/* --- Statistical Parameter ----------------------------------------------- */
#define RSZVB_ALL                                   0
#define RSZVB_MEAN                                  1
#define RSZVB_STDDEV                                2
#define RSZVB_MAX                                   3
#define RSZVB_MIN                                   4
#define RSZVB_RMS                                   5
#define RSZVB_PTPEAK                                6
#define RSZVB_ELENGTH                               7
#define RSZVB_PDELAY                                8
#define RSZVB_SLOPE                                 9
#define RSZVB_FLATNESS                              10
#define RSZVB_GAIN                                  11   

/* --- Data Format --------------------------------------------------------- */
#define RSZVB_UNFORMATTED                           0
#define RSZVB_FORMATTED                             1
#define RSZVB_UNFORMATTED_MATH                      2
#define RSZVB_PULSE_PROFILE                         3

/* --- Discrete Mode ------------------------------------------------------- */
#define RSZVB_CONTINUOUS                            0
#define RSZVB_DISCRETE                              1

/* --- Fixed Marker -------------------------------------------------------- */
#define RSZVB_NORMAL                                0
#define RSZVB_FIXED                                 1

/* --- Search -------------------------------------------------------------- */
#define RSZVB_MARKER_MAX                            0
#define RSZVB_MARKER_MIN                            1
#define RSZVB_MARKER_NEXT                           2
#define RSZVB_MARKER_RPEAK                          3
#define RSZVB_MARKER_LPEAK                          4

/* --- Search -------------------------------------------------------------- */
#define RSZVB_MARKER_TARGET                         0
#define RSZVB_MARKER_RTARGET                        1
#define RSZVB_MARKER_LTARGET                        2

/* --- Limit Line ---------------------------------------------------------- */
#define RSZVB_LIMIT_OFF                             0
#define RSZVB_LIMIT_UPPER                           1
#define RSZVB_LIMIT_LOWER                           2
#define RSZVB_LIMIT_ALL                             3

/* --- Error Term Parameters ----------------------------------------------- */
#define RSZVB_CAL_DATA_DIRECTIVITY                  0
#define RSZVB_CAL_DATA_SRCMATCH                     1
#define RSZVB_CAL_DATA_REFLTRACK                    2
#define RSZVB_CAL_DATA_ISOLATION                    3
#define RSZVB_CAL_DATA_LOADMATCH                    4
#define RSZVB_CAL_DATA_TRANSTRACK                   5
#define RSZVB_CAL_DATA_G11                          6
#define RSZVB_CAL_DATA_G12                          7
#define RSZVB_CAL_DATA_G21                          8
#define RSZVB_CAL_DATA_G22                          9
#define RSZVB_CAL_DATA_H11                          10
#define RSZVB_CAL_DATA_H12                          11
#define RSZVB_CAL_DATA_H21                          12
#define RSZVB_CAL_DATA_H22                          13

/* --- Display Update ------------------------------------------------------ */
#define RSZVB_DISP_UPDATE_OFF                       0
#define RSZVB_DISP_UPDATE_ON                        1
#define RSZVB_DISP_UPDATE_ONCE                      2

/* --- Display Colors ------------------------------------------------------ */
#define RSZVB_DBACKGROUND                           0
#define RSZVB_LBACKGROUND                           1
#define RSZVB_BW_LSTYLES                            2
#define RSZVB_BW_SOLID                              3

/* --- Domain -------------------------------------------------------------- */
#define RSZVB_FREQUENCY                             0
#define RSZVB_TIME                                  1

/* --- Time Axis Scaling --------------------------------------------------- */
#define RSZVB_DISTANCE                              0

/* --- Transformation Type ------------------------------------------------- */
#define RSZVB_TYPE_BPAS_IMP                         0
#define RSZVB_TYPE_LPAS_IMP                         1
#define RSZVB_TYPE_LPAS_STEP                        2

/* --- Time Domain Filter -------------------------------------------------- */
#define RSZVB_FILTER_RECT                           0
#define RSZVB_FILTER_HANN                           1
#define RSZVB_FILTER_HAMM                           2
#define RSZVB_FILTER_BOHM                           3
#define RSZVB_FILTER_DCH                            4

/* --- Time Gate Calculation Method ---------------------------------------- */
#define RSZVB_GRID_KFST                             0
#define RSZVB_GRID_KDFR                             1
#define RSZVB_GRID_KSDFR                            2

/* --- Time Gate Type ------------------------------------------------------ */
#define RSZVB_TGATE_TYPE_BPAS                       0
#define RSZVB_TGATE_TYPE_NOTCH                      1

/* --- Harmonic Measurement ------------------------------------------------ */
#define RSZVB_MEAS_FUNDAMENTAL                      0
#define RSZVB_MEAS_HARMONIC                         1

/* --- Calibration --------------------------------------------------------- */
#define RSZVB_CALSTATE_CAL                          0
#define RSZVB_CALSTATE_CAI                          1
#define RSZVB_CALSTATE_CA                           2
#define RSZVB_CALSTATE_CAV                          3
#define RSZVB_CALSTATE_CALOFF                       4
#define RSZVB_CALSTATE_NONE                         5

#define RSZVB_CALUNIT_STD_THR                       0
#define RSZVB_CALUNIT_STD_OPEN                      1
#define RSZVB_CALUNIT_STD_SHOR                      2
#define RSZVB_CALUNIT_STD_MATC                      3

/* --- Mixer Measurement --------------------------------------------------- */
#define RSZVB_MIX_MODE_MIXER                        0
#define RSZVB_MIX_MODE_FREQ_CONV_OFF                1
    
#define RSZVB_FUNDAMENTAL_TYPE_RF                   0
#define RSZVB_FUNDAMENTAL_TYPE_LO                   1
#define RSZVB_FUNDAMENTAL_TYPE_IF                   2
#define RSZVB_FUNDAMENTAL_TYPE_LO1                  3 
#define RSZVB_FUNDAMENTAL_TYPE_LO2                  4
#define RSZVB_FUNDAMENTAL_TYPE_AUX                  5 
    
#define RSZVB_CONVERSION_DCLOWER                    0
#define RSZVB_CONVERSION_DCUPPER                    1
#define RSZVB_CONVERSION_UCONVERSION                2
	
#define RSZVB_POWER_MODE_FIXED        				0
#define RSZVB_POWER_MODE_FUNDAMENTAL  				1


/* --- Power Calibration --------------------------------------------------- */
#define RSZVB_PWR_CAL_PORT                          0
#define RSZVB_PWR_CAL_GEN                           1
#define RSZVB_PWR_CAL_CONV                          2    
    
#define RSZVB_PWR_CAL_ASENSOR                       0
#define RSZVB_PWR_CAL_BSENSOR                       1   
    
#define RSZVB_PWR_CAL_OFFSET_ONLY                   0
#define RSZVB_PWR_CAL_OFFSET_CPADD                  1
    
#define RSZVB_PWR_CAL_AWAVE                         0
#define RSZVB_PWR_CAL_BWAVE                         1   
#define RSZVB_PWR_CAL_B1                            2
#define RSZVB_PWR_CAL_B2                            3
#define RSZVB_PWR_CAL_B3                            4
#define RSZVB_PWR_CAL_B4                            5
#define RSZVB_PWR_CAL_B5                            6
#define RSZVB_PWR_CAL_B6                            7
#define RSZVB_PWR_CAL_B7                            8
#define RSZVB_PWR_CAL_B8                            9

    
#define RSZVB_TGATE_SHAPE_MAX                       0
#define RSZVB_TGATE_SHAPE_WIDE                      1
#define RSZVB_TGATE_SHAPE_NORM                      2
#define RSZVB_TGATE_SHAPE_MIN                       3
    
#define RSZVB_SAW_SBAL                              0
    
#define RSZVB_LIMIT_RDOM_COMP_S                     0
#define RSZVB_LIMIT_RDOM_COMP_SINV                  1
#define RSZVB_LIMIT_RDOM_COMP_Y                     2
#define RSZVB_LIMIT_RDOM_COMP_Z                     3
#define RSZVB_LIMIT_RDOM_COMP_YREL                  4
#define RSZVB_LIMIT_RDOM_COMP_ZREL                  5
    
#define RSZVB_LIMIT_RDOM_FORM_COMP                  0
#define RSZVB_LIMIT_RDOM_FORM_MAGN                  1
#define RSZVB_LIMIT_RDOM_FORM_PHAS                  2
#define RSZVB_LIMIT_RDOM_FORM_REAL                  3
#define RSZVB_LIMIT_RDOM_FORM_IMAG                  4
#define RSZVB_LIMIT_RDOM_FORM_SWR                   5
#define RSZVB_LIMIT_RDOM_FORM_GDEL                  6
#define RSZVB_LIMIT_RDOM_FORM_L                     7
#define RSZVB_LIMIT_RDOM_FORM_C                     8
    
#define RSZVB_LIMIT_RDOM_SPAC_LIN                   0
#define RSZVB_LIMIT_RDOM_SPAC_LOG                   1
#define RSZVB_LIMIT_RDOM_SPAC_DB                    2
#define RSZVB_LIMIT_RDOM_SPAC_SIC                   3   
    
#define RSZVB_LIMIT_DOM_FLIN                        0
#define RSZVB_LIMIT_DOM_FLOG                        1
#define RSZVB_LIMIT_DOM_FSEG                        2
#define RSZVB_LIMIT_DOM_FSIN                        3
#define RSZVB_LIMIT_DOM_TLIN                        4
#define RSZVB_LIMIT_DOM_TLOG                        5
#define RSZVB_LIMIT_DOM_PLIN                        6
#define RSZVB_LIMIT_DOM_PLOG                        7
#define RSZVB_LIMIT_DOM_PSIN                        8
    
#define RSZVB_MATH_FUNC_NORM                        0
#define RSZVB_MATH_FUNC_ADD                         1
#define RSZVB_MATH_FUNC_SUB                         2
#define RSZVB_MATH_FUNC_MULT                        3
#define RSZVB_MATH_FUNC_DIV                         4   
    
#define RSZVB_CONV_S                                0
#define RSZVB_CONV_Y                                1
#define RSZVB_CONV_Z                                2

#define RSZVB_VNET_FUNC_DEEMBED                     0
#define RSZVB_VNET_FUNC_EMBED                       1
    
#define RSZVB_VNET_PARAM_C                          0
#define RSZVB_VNET_PARAM_L                          1
#define RSZVB_VNET_PARAM_R                          2   
    
#define RSZVB_BALANCED_CIRCUIT_FIMP                 0
#define RSZVB_BALANCED_CIRCUIT_STSL                 1
#define RSZVB_BALANCED_CIRCUIT_STSC                 2
#define RSZVB_BALANCED_CIRCUIT_SLST                 3
#define RSZVB_BALANCED_CIRCUIT_SCST                 4
#define RSZVB_BALANCED_CIRCUIT_CSSL                 5
#define RSZVB_BALANCED_CIRCUIT_LSSC                 6
#define RSZVB_BALANCED_CIRCUIT_CSSC                 7
#define RSZVB_BALANCED_CIRCUIT_LSSL                 8
#define RSZVB_BALANCED_CIRCUIT_SLCS                 9
#define RSZVB_BALANCED_CIRCUIT_SCLS                 10
#define RSZVB_BALANCED_CIRCUIT_SCCS                 11
#define RSZVB_BALANCED_CIRCUIT_SLLS                 12

#define RSZVB_SENDED_CIRCUIT_FIMP                   0
#define RSZVB_SENDED_CIRCUIT_CSL                    1
#define RSZVB_SENDED_CIRCUIT_LSC                    2
#define RSZVB_SENDED_CIRCUIT_CSC                    3
#define RSZVB_SENDED_CIRCUIT_LSL                    4
#define RSZVB_SENDED_CIRCUIT_SLC                    5
#define RSZVB_SENDED_CIRCUIT_SCL                    6
#define RSZVB_SENDED_CIRCUIT_SCC                    7
#define RSZVB_SENDED_CIRCUIT_SLL                    8
    
#define RSZVB_ELEMENT_BACKGROUND                    1
#define RSZVB_ELEMENT_TEXT                          2
#define RSZVB_ELEMENT_SELTEXT                       3
#define RSZVB_ELEMENT_GRID                          4
#define RSZVB_ELEMENT_REFLINE                       5
#define RSZVB_ELEMENT_ALLMAKERS                     6
#define RSZVB_ELEMENT_HLINE                         7
#define RSZVB_ELEMENT_DTITLE                        8
#define RSZVB_ELEMENT_LIMITFAILTRACE                9
#define RSZVB_ELEMENT_LIMITLINEOFF                  10
#define RSZVB_ELEMENT_LIMITLINEUPPER                11
#define RSZVB_ELEMENT_LIMITLINELOWER                12
#define RSZVB_ELEMENT_TRACE1                        13
#define RSZVB_ELEMENT_TRACE2                        14
#define RSZVB_ELEMENT_TRACE3                        15
#define RSZVB_ELEMENT_TRACE4                        16
#define RSZVB_ELEMENT_TRACE5                        17
#define RSZVB_ELEMENT_TRACE6                        18
#define RSZVB_ELEMENT_TRACE7                        19
#define RSZVB_ELEMENT_TRACE8                        20
#define RSZVB_ELEMENT_TRACE9                        21
#define RSZVB_ELEMENT_TRACE10                       22
#define RSZVB_ELEMENT_TRACE11                       23
#define RSZVB_ELEMENT_TRACE12                       24
#define RSZVB_ELEMENT_TRACE13                       25
#define RSZVB_ELEMENT_TRACE14                       26
#define RSZVB_ELEMENT_TRACE15                       27
#define RSZVB_ELEMENT_TRACE16                       28
    
#define RSZVB_TRACE_STYLE_SOLID                     0
#define RSZVB_TRACE_STYLE_DASHED                    1
#define RSZVB_TRACE_STYLE_DOTTED                    2
#define RSZVB_TRACE_STYLE_DDOTTED                   3
#define RSZVB_TRACE_STYLE_DDDOTTED                  4
    
#define RSZVB_CALSTD_MMTH                           0
#define RSZVB_CALSTD_FFTH                           1
#define RSZVB_CALSTD_MFTH                           2
#define RSZVB_CALSTD_MMLI                           3
#define RSZVB_CALSTD_FFLI                           4
#define RSZVB_CALSTD_MFLI                           5
#define RSZVB_CALSTD_OSH                            6   
#define RSZVB_CALSTD_MOSH                           7
#define RSZVB_CALSTD_FOSH                           8
#define RSZVB_CALSTD_MMAT                           9
#define RSZVB_CALSTD_FFAT                           10
#define RSZVB_CALSTD_MFAT                           11
#define RSZVB_CALSTD_MMSN                           12
#define RSZVB_CALSTD_FFSN                           13
#define RSZVB_CALSTD_MFSN                           14
#define RSZVB_CALSTD_MOP                            15
#define RSZVB_CALSTD_FOP                            16
#define RSZVB_CALSTD_MSH                            17
#define RSZVB_CALSTD_FSH                            18
#define RSZVB_CALSTD_MREF                           19
#define RSZVB_CALSTD_FREF                           20
#define RSZVB_CALSTD_MMTC                           21
#define RSZVB_CALSTD_FMTC                           22
#define RSZVB_CALSTD_MSM                            23
#define RSZVB_CALSTD_FSM                            24
#define RSZVB_CALSTD_MMLI_2                         25
#define RSZVB_CALSTD_FFLI_2                         26
#define RSZVB_CALSTD_MFLI_2                         27
#define RSZVB_CALSTD_MMLI_3                         28
#define RSZVB_CALSTD_FFLI_3                         29
#define RSZVB_CALSTD_MFLI_3                         30
#define RSZVB_CALSTD_MOSH_2                         31
#define RSZVB_CALSTD_FOSH_2                         32
#define RSZVB_CALSTD_MOSH_3                         33
#define RSZVB_CALSTD_FOSH_3                         34
    
#define RSZVB_VNET_PARAM_PMAIN                      0
#define RSZVB_VNET_PARAM_PSECOND                    1
    
#define RSZVB_CONNECTION_MODE_TEM                   0
#define RSZVB_CONNECTION_MODE_WGUIDE                1   
    
#define RSZVB_CONNECTION_CONNECTOR_GENDER           0
#define RSZVB_CONNECTION_CONNECTOR_NGENDER          1
    
#define RSZVB_RECEIVER                              0
#define RSZVB_SOURCE                                1

#define RSZVB_SWEEP_TYPE_SWEEP                      0
#define RSZVB_SWEEP_TYPE_FIXED                      1
    
#define RSZVB_SELECTIVITY_NORMAL                    0
#define RSZVB_SELECTIVITY_HIGH                      1
    
#define RSZVB_ATTEN_AREC                            0
#define RSZVB_ATTEN_BREC                            1
#define RSZVB_ATTEN_CREC                            2
#define RSZVB_ATTEN_DREC                            3
    
#define RSZVB_IF_GAIN_AUTO                          0
#define RSZVB_IF_GAIN_LNOISE                        1
#define RSZVB_IF_GAIN_LDIST                         2
    
#define RSZVB_TRACE_MDATA1                          0
#define RSZVB_TRACE_MDATA2                          1
#define RSZVB_TRACE_MDATA3                          2
#define RSZVB_TRACE_MDATA4                          3
#define RSZVB_TRACE_MDATA5                          4
#define RSZVB_TRACE_MDATA6                          5
#define RSZVB_TRACE_MDATA7                          6
#define RSZVB_TRACE_MDATA8                          7   

#define RSZVB_ALT_SWE_MODE_NORMAL                   0
#define RSZVB_ALT_SWE_MODE_ALTER                    1
    
#define RSZVB_CONNECTOR_GENDER_MALE                 0
#define RSZVB_CONNECTOR_GENDER_FEMALE               1
    
#define RSZVB_DISPLAY_RESULTS_EPD                   0
#define RSZVB_DISPLAY_RESULTS_MMPT                  1
#define RSZVB_DISPLAY_RESULTS_MSTD                  2
#define RSZVB_DISPLAY_RESULTS_RMS                   3
#define RSZVB_DISPLAY_RESULTS_SFL                   4
#define RSZVB_DISPLAY_RESULTS_COMP                  5
    
#define RSZVB_COMPLEX                               0
#define RSZVB_LINP                                  1
#define RSZVB_LOGP                                  2
    
#define RSZVB_PULSE_REC_A                           0
#define RSZVB_PULSE_REC_B                           1
    
#define RSZVB_PULSE_INTERFACE_GEN                   0
#define RSZVB_PULSE_INTERFACE_SRC                   1
    
#define RSZVB_PULSE_MODE_NORMAL                     0
#define RSZVB_PULSE_MODE_MEAN                       1
    
#define RSZVB_FORMAT_BORDER_SWAP                    0
#define RSZVB_FORMAT_BORDER_NORM                    1
    
#define RSZVB_TRACE_ZVR_CH1DATA                     0
#define RSZVB_TRACE_ZVR_CH2DATA                     1
#define RSZVB_TRACE_ZVR_CH3DATA                     2
#define RSZVB_TRACE_ZVR_CH4DATA                     3
#define RSZVB_TRACE_ZVR_CH1MEM                      4
#define RSZVB_TRACE_ZVR_CH2MEM                      5
#define RSZVB_TRACE_ZVR_CH3MEM                      6
#define RSZVB_TRACE_ZVR_CH4MEM                      7
#define RSZVB_TRACE_ZVR_MDATA1                      8
#define RSZVB_TRACE_ZVR_MDATA2                      9
#define RSZVB_TRACE_ZVR_MDATA3                      10
#define RSZVB_TRACE_ZVR_MDATA4                      11
#define RSZVB_TRACE_ZVR_MDATA5                      12
#define RSZVB_TRACE_ZVR_MDATA6                      13
#define RSZVB_TRACE_ZVR_MDATA7                      14
#define RSZVB_TRACE_ZVR_MDATA8                      15  
    
#define RSZVB_POWER_SENDED                          0
#define RSZVB_POWER_DCMODE                          1

#define RSZVB_FREQ_CONVERSION_RILI                  0
#define RSZVB_FREQ_CONVERSION_RILE                  1
                             
#define RSZVB_CHANNEL_TRACE_SINGLE                  0
#define RSZVB_CHANNEL_TRACE_ALL                     1
    
#define RSZVB_SAVE                                  0   
#define RSZVB_RECALL                                1   

#define RSZVB_POIN                                  0
#define RSZVB_COMM                                  1
    
#define RSZVB_SEM                                   0
#define RSZVB_TAB                                   2
#define RSZVB_SPAC                                  3
    
#define RSZVB_RENORMALIZATION_TWAV                  0
#define RSZVB_RENORMALIZATION_PWAV                  1
    
#define RSZVB_IMOD_SRC_NONE                         0
#define RSZVB_IMOD_SRC_PORT                         1
#define RSZVB_IMOD_SRC_GEN                          2
#define RSZVB_IMOD_SRC_EMB                          3
    
#define RSZVB_UTHR_AUTO                             0
#define RSZVB_UTHR_MAN                              1
    
#define RSZVB_LANG_SCPI                             0
#define RSZVB_LANG_PNA                              1
#define RSZVB_LANG_HP8510                           2
#define RSZVB_LANG_HP8720                           3
#define RSZVB_LANG_HP8753                           4
    
#define RSZVB_BWID_MODE_BPAS                        0
#define RSZVB_BWID_MODE_BST                         1
#define RSZVB_BWID_MODE_BPRM                        2
#define RSZVB_BWID_MODE_BSRM                        3
#define RSZVB_BWID_MODE_BPAB                        4
#define RSZVB_BWID_MODE_BSAB                        5
    
#define RSZVB_ATTEN_MODE_AUTO                       0
#define RSZVB_ATTEN_MODE_MAN                        1
#define RSZVB_ATTEN_MODE_LNO                        2
    
#define RSZVB_MIXER_LOAD_FILE                       0
#define RSZVB_MIXER_LOAD_DELAY                      1
    
#define RSZVB_IMOD_SOURCE_PORT                      0
#define RSZVB_IMOD_SOURCE_EDEV                      1
    
#define RSZVB_DISP_TRAC_DATA                        0
#define RSZVB_DISP_TRAC_MEM                         1
#define RSZVB_DISP_TRAC_SING                        2
    
#define RSZVB_HOLD_OFF                              0
#define RSZVB_HOLD_MAX                              1
#define RSZVB_HOLD_MIN                              2
    
#define RSZVB_PULS_TYPE_SING                        0
#define RSZVB_PULS_TYPE_TRAI                        1
#define RSZVB_PULS_TYPE_CHIG                        2
#define RSZVB_PULS_TYPE_CLOW                        3
    
#define RSZVB_PULS_POL_NORM                         0
#define RSZVB_PULS_POL_INV                          1
    
#define RSZVB_PULS_MODE_CSP                         0
#define RSZVB_PULS_MODE_CONT                        1
    
#define RSZVB_ASSIGN_G1M                            0
#define RSZVB_ASSIGN_G2M                            1
#define RSZVB_ASSIGN_G2M2                           2
#define RSZVB_ASSIGN_G1M3                           3
    
#define RSZVB_MIX_MODE_VMIXER                       0

#define RSZVB_GLOOP_CIRCUIT_FIMP                    0
#define RSZVB_GLOOP_CIRCUIT_SL                      1
#define RSZVB_GLOOP_CIRCUIT_SC                      2
    
#define RSZVB_LDEV_OFF                              0
#define RSZVB_LDEV_ON                               1
#define RSZVB_LDEV_TRAC                             2
    
#define RSZVB_NOISE_FIGURE_CAL_STEP_REC             0
#define RSZVB_NOISE_FIGURE_CAL_STEP_SRC             1
#define RSZVB_NOISE_FIGURE_CAL_STEP_ATT             2
    
#define RSZVB_MODE_PALL                             0
#define RSZVB_MODE_PSP                              1
    
#define RSZVB_PRIORITY_NORMAL                       0
#define RSZVB_PRIORITY_ABOVE_NORMAL                 1
#define RSZVB_PRIORITY_HIGH                         2
    
#define RSZVB_MDEL_LAN1                             1
#define RSZVB_MDEL_LAN2                             2
    
/* --- Set Trace Unit --------------------------------------------------- */
#define RSZVB_UNIT_POW  0
#define RSZVB_UNIT_VOLT 1

/* --- Set Type Of Advanced Power Transfer Model ------------------------ */    
#define RSZVB_CONVERTER_DSET  0
#define RSZVB_CONVERTER_LAPP  1
#define RSZVB_CONVERTER_ELEC  2
#define RSZVB_CONVERTER_NONE  3

/* --- Set Port Waveguide Attenuator  ----------------------------------- */    
#define RSZVB_CONVERTER_ATT_MECH  0
#define RSZVB_CONVERTER_ATT_EL    1

/* --- Correction Manager ----------------------------------------------- */    
#define RSZVB_CORR_TCO_LOAD        0
#define RSZVB_CORR_TCO_STORE       1

/* --- Set Power Sensor Position ---------------------------------------- */    
#define RSZVB_PS_POSITION_DEV 0
#define RSZVB_PS_POSITION_PWR 1
    
/* --- Set Power Loss List Coefficient ---------------------------------- */    
#define RSZVB_CORR_TCO_LIST_INSERT       0
#define RSZVB_CORR_TCO_LIST_APPEND       1

/* --- Set Restart Behavior --------------------------------------------- */    
#define RSZVB_RESTART_KEEP    0
#define RSZVB_RESTART_RESET   1
    
/* --- Set Calculation of Bandfilter Center Frequency ------------------- */
#define RSZVB_CALC_GEOM   0
#define RSZVB_CALC_ARIT   1

/* --- Set S-Parameter Detector ----------------------------------------- */
#define RSZVB_S_PARAMETER_DETECTOR_NORMAL           0
#define RSZVB_S_PARAMETER_DETECTOR_AVERAGE          1
    
/* --- Set Output Port Bits --------------------------------------------- */
#define RSZVB_PORT_BIT_A                            0
#define RSZVB_PORT_BIT_B                            1
#define RSZVB_PORT_BIT_C                            2
#define RSZVB_PORT_BIT_D                            3
#define RSZVB_PORT_BIT_E                            4
#define RSZVB_PORT_BIT_F                            5

/* --- Set RF Off Behavior ---------------------------------------------- */    
#define RSZVB_RF_OFF_BEHAVIOR_FAST                  0
#define RSZVB_RF_OFF_BEHAVIOR_LBN                   1
    
#define RSZVB_REF_POWER_A_WAVE  0
#define RSZVB_REF_POWER_NOMINAL 1
	
#define RSZVB_RENORMALIZATION_MODE_AUTO 0
#define RSZVB_RENORMALIZATION_MODE_EXPL 1
	
#define RSZVB_SPUR_AVOID_POSITIVE 0
#define RSZVB_SPUR_AVOID_NEGATIVE 1
#define RSZVB_SPUR_AVOID_AUTO     2
	
#define RSZVB_DIRECTION_IN  0
#define RSZVB_DIRECTION_OUT 1

#define RSZVB_MINIMUM_FREQUENCY_OFFSET_DIRECT    0
#define RSZVB_MINIMUM_FREQUENCY_OFFSET_BANDWIDTH 1

#define RSZVB_TRM_PMODULATOR 0
#define RSZVB_TRM_COMBINER   1
#define RSZVB_TRM_OUTPUT     2

#define RSZVB_TRM_SOURCE_OFF   0
#define RSZVB_TRM_SOURCE_G1INT 1
#define RSZVB_TRM_SOURCE_G2INT 2
#define RSZVB_TRM_SOURCE_G1EXT 3
#define RSZVB_TRM_SOURCE_G2EXT 4

#define RSZVB_CALTYPE_DEF 0

#define RSZVB_PWR_CAL_METHOD_POWER_METER_ONLY   0
#define RSZVB_PWR_CAL_METHOD_REF_RECEIVER_AFTER 1
#define RSZVB_PWR_CAL_METHOD_REF_RECEIVER_ONLY  2

#define RSZVB_CONVERTER_DATA_SET_FACTORY 0
#define RSZVB_CONVERTER_DATA_SET_USER    1

#define RSZVB_VMIX_MODE_BASE  0
#define RSZVB_VMIX_MODE_MIXER 1

#define RSZVB_MIXER_PARAM_AUTO 0
#define RSZVB_MIXER_PARAM_USER 1
    
/*****************************************************************************/
/*= GLOBAL USER-CALLABLE FUNCTION DECLARATIONS (Exportable Functions) =======*/
/*****************************************************************************/

ViStatus _VI_FUNC rszvb_init (ViRsrc resourceName, ViBoolean IDQuery,
                              ViBoolean resetDevice, ViSession* instrumentHandle);
ViStatus _VI_FUNC rszvb_ApplicationExample (ViSession instrumentHandle,
                                            ViInt32 channel,
                                            ViReal64 startFrequency,
                                            ViReal64 stopFrequency, ViReal64 power,
                                            ViInt32* noOfValues,
                                            ViReal64 _VI_FAR stimulusData[],
                                            ViReal64 _VI_FAR responseData[]);
ViStatus _VI_FUNC rszvb_WindowNew (ViSession instrumentHandle, ViString setupName);
ViStatus _VI_FUNC rszvb_WindowSelect (ViSession instrumentHandle,
                                      ViString setupName);
ViStatus _VI_FUNC rszvb_WindowClose (ViSession instrumentHandle,
                                     ViString setupName);
ViStatus _VI_FUNC rszvb_WindowList (ViSession instrumentHandle,
                                    ViChar _VI_FAR catalog[], ViInt32 bufferSize);
ViStatus _VI_FUNC rszvb_Print (ViSession instrumentHandle, ViString printerName);
ViStatus _VI_FUNC rszvb_PrinttoFile (ViSession instrumentHandle, ViString fileName,
                                     ViInt32 fileFormat, ViInt32 diagramArea,
                                     ViBoolean logo, ViBoolean dateAndTime,
                                     ViBoolean markerList);
ViStatus _VI_FUNC rszvb_PrintSetup (ViSession instrumentHandle, ViInt32 diagramArea,
                                    ViBoolean logo, ViBoolean dateAndTime,
                                    ViBoolean markerList, ViInt32 pageOrientation,
                                    ViReal64 leftMargin, ViReal64 rightMargin,
                                    ViReal64 topMargin, ViReal64 bottomMargin);
ViStatus _VI_FUNC rszvb_FileManager (ViSession instrumentHandle,
                                     ViInt32 operationToBePerformed,
                                     ViString source, ViString destination);
ViStatus _VI_FUNC rszvb_GetCurrentDirectory (ViSession instrumentHandle,
                                             ViChar _VI_FAR currentDirectory[]);
   rszvb_FileCatalog (ViSession instrumentHandle, ViString directory,
                                     ViChar _VI_FAR catalog[], ViInt32 bufferSize);
ViStatus _VI_FUNC rszvb_SetupSave (ViSession instrumentHandle, ViString fileName);
ViStatus _VI_FUNC rszvb_SetupRecall (ViSession instrumentHandle, ViString fileName);
ViStatus _VI_FUNC rszvb_readToFile (ViSession instrumentHandle, ViString source,
                                    ViString destination);
ViStatus _VI_FUNC rszvb_writeFromFile (ViSession instrumentHandle, ViString source,
                                       ViString destination);
ViStatus _VI_FUNC rszvb_SelectPowerMeter (ViSession instrumentHandle,
                                          ViInt32 channel, ViString traceName,
                                          ViInt32 powerMeter, ViInt32 outPort);
ViStatus _VI_FUNC rszvb_SelectSParameters (ViSession instrumentHandle,
                                           ViInt32 channel, ViString traceName,
                                           ViInt32 outPort, ViInt32 inPort);
ViStatus _VI_FUNC rszvb_SelectMoreSParameters (ViSession instrumentHandle,
                                               ViInt32 channel, ViString traceName,
                                               ViInt32 outMode, ViInt32 outPort,
                                               ViInt32 inMode, ViInt32 inPort);
ViStatus _VI_FUNC rszvb_SelectRatios (ViSession instrumentHandle, ViInt32 channel,
                                      ViString traceName, ViInt32 ratios);
ViStatus _VI_FUNC rszvb_SelectMoreRatios (ViSession instrumentHandle,
                                          ViInt32 channel, ViString traceName,
                                          ViInt32 sourcePort, ViInt32 numeratorType,
                                          ViInt32 numeratorPortNumber,
                                          ViInt32 denominatorType,
                                          ViInt32 denominatorPortNumber);
ViStatus _VI_FUNC rszvb_SelectMoreRatiosWithDetector (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViString traceName,
                                                      ViInt32 sourcePort,
                                                      ViInt32 numeratorType,
                                                      ViInt32 numeratorPortNumber,
                                                      ViInt32 denominatorType,
                                                      ViInt32 denominatorPortNumber,
                                                      ViInt32 detector,
                                                      ViReal64 observationTime);
ViStatus _VI_FUNC rszvb_SelectMoreRatiosGenerator (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViString traceName,
                                                   ViInt32 generatorNumber,
                                                   ViInt32 numeratorType,
                                                   ViInt32 numeratorPortNumber,
                                                   ViInt32 denominatorType,
                                                   ViInt32 denominatorPortNumber);
ViStatus _VI_FUNC rszvb_SelectMoreRatiosGeneratorWithDetector
             (ViSession instrumentHandle, ViInt32 channel, ViString traceName,
              ViInt32 generatorNumber, ViInt32 numeratorType,
              ViInt32 numeratorPortNumber, ViInt32 denominatorType,
              ViInt32 denominatorPortNumber, ViInt32 detector,
              ViReal64 observationTime);
ViStatus _VI_FUNC rszvb_SelectWaveQuantities (ViSession instrumentHandle,
                                              ViInt32 channel, ViString traceName,
                                              ViInt32 waveQuantities);
ViStatus _VI_FUNC rszvb_SelectMoreWaveQuantities (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViString traceName,
                                                  ViInt32 waveQuantityType,
                                                  ViInt32 waveQuantityPortNumber,
                                                  ViInt32 sourcePort);
ViStatus _VI_FUNC rszvb_SelectMoreWaveQuantitiesWithDetector
             (ViSession instrumentHandle, ViInt32 channel, ViString traceName,
              ViInt32 waveQuantityType, ViInt32 waveQuantityPortNumber,
              ViInt32 sourcePort, ViInt32 detector, ViReal64 observationTime);
ViStatus _VI_FUNC rszvb_SelectImpedances (ViSession instrumentHandle,
                                          ViInt32 channel, ViString traceName,
                                          ViInt32 outPort, ViInt32 inPort);
ViStatus _VI_FUNC rszvb_SelectMoreImpedances (ViSession instrumentHandle,
                                              ViInt32 channel, ViString traceName,
                                              ViInt32 outMode, ViInt32 outPort,
                                              ViInt32 inMode, ViInt32 inPort);
ViStatus _VI_FUNC rszvb_SelectAdmitances (ViSession instrumentHandle,
                                          ViInt32 channel, ViString traceName,
                                          ViInt32 outPort, ViInt32 inPort);
ViStatus _VI_FUNC rszvb_SelectMoreAdmitances (ViSession instrumentHandle,
                                              ViInt32 channel, ViString traceName,
                                              ViInt32 outMode, ViInt32 outPort,
                                              ViInt32 inMode, ViInt32 inPort);
ViStatus _VI_FUNC rszvb_SelectZParameters (ViSession instrumentHandle,
                                           ViInt32 channel, ViString traceName,
                                           ViInt32 outMode, ViInt32 outPort,
                                           ViInt32 inMode, ViInt32 inPort);
ViStatus _VI_FUNC rszvb_SelectYParameters (ViSession instrumentHandle,
                                           ViInt32 channel, ViString traceName,
                                           ViInt32 outMode, ViInt32 outPort,
                                           ViInt32 inMode, ViInt32 inPort);
ViStatus _VI_FUNC rszvb_SelectStabilityFactors (ViSession instrumentHandle,
                                                ViInt32 channel, ViString traceName,
                                                ViInt32 DUTOut, ViInt32 DUTIn,
                                                ViInt32 stabilityFactor);
ViStatus _VI_FUNC rszvb_SelectDCMeasurement (ViSession instrumentHandle,
                                             ViInt32 channel, ViString traceName,
                                             ViInt32 DCMeas);
ViStatus _VI_FUNC rszvb_SelectPAEMeasurement (ViSession instrumentHandle,
                                              ViInt32 channel, ViString traceName,
                                              ViInt32 DUTOut, ViInt32 DUTIn);
ViStatus _VI_FUNC rszvb_DefinePAEMeasurement (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViInt32 testModel, ViReal64 constantC,
                                              ViReal64 constantK);
ViStatus _VI_FUNC rszvb_SelectNoiseFigure (ViSession instrumentHandle,
                                           ViInt32 channel, ViString traceName,
                                           ViInt32 outPort, ViInt32 inPort);
ViStatus _VI_FUNC rszvb_CreateTrace (ViSession instrumentHandle, ViInt32 channel,
                                     ViString traceName, ViString parameter);
ViStatus _VI_FUNC rszvb_ConfigureMesurementParameters (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViString traceName,
                                                       ViString parameter);
ViStatus _VI_FUNC rszvb_QueryMesurementParameters (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViString traceName,
                                                   ViInt32 bufferSize,
                                                   ViChar _VI_FAR parameters[]);
ViStatus _VI_FUNC rszvb_SetTraceFormat (ViSession instrumentHandle,
                                        ViInt32 channel_Trace, ViInt32 format);
ViStatus _VI_FUNC rszvb_GetTraceFormat (ViSession instrumentHandle,
                                        ViInt32 channel_Trace, ViInt32* format);
ViStatus _VI_FUNC rszvb_SetTraceUnit (ViSession instrumentHandle,
                                      ViInt32 channel_Trace, ViInt32 format);
ViStatus _VI_FUNC rszvb_GetTraceUnit (ViSession instrumentHandle,
                                      ViInt32 channel_Trace, ViInt32* format);
ViStatus _VI_FUNC rszvb_SetApertureGroupDelaySteps (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 steps);
ViStatus _VI_FUNC rszvb_GetApertureGroupDelaySteps (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32* steps);
ViStatus _VI_FUNC rszvb_TraceAutoscale (ViSession instrumentHandle, ViInt32 window,
                                        ViInt32 window_Trace);
ViStatus _VI_FUNC rszvb_TraceAutoscaleByName (ViSession instrumentHandle,
                                              ViInt32 window, ViString traceName);
ViStatus _VI_FUNC rszvb_SetTraceBottom (ViSession instrumentHandle, ViInt32 window,
                                        ViInt32 window_Trace, ViReal64 bottom);
ViStatus _VI_FUNC rszvb_GetTraceBottom (ViSession instrumentHandle, ViInt32 window,
                                        ViInt32 window_Trace, ViReal64* bottom);
ViStatus _VI_FUNC rszvb_SetTraceScaleDivisions (ViSession instrumentHandle,
                                                ViInt32 window,
                                                ViInt32 window_Trace,
                                                ViReal64 scaleDivisions);
ViStatus _VI_FUNC rszvb_SetTraceScaleDivisionsByName (ViSession instrumentHandle,
                                                      ViInt32 window,
                                                      ViReal64 scaleDivisions,
                                                      ViString traceName);
ViStatus _VI_FUNC rszvb_GetTraceScaleDivisions (ViSession instrumentHandle,
                                                ViInt32 window,
                                                ViInt32 window_Trace,
                                                ViReal64* scaleDivisions);
ViStatus _VI_FUNC rszvb_SetTraceRefValue (ViSession instrumentHandle,
                                          ViInt32 window, ViInt32 window_Trace,
                                          ViReal64 referenceLevel);
ViStatus _VI_FUNC rszvb_SetTraceRefValueByName (ViSession instrumentHandle,
                                                ViInt32 window,
                                                ViReal64 referenceLevel,
                                                ViString traceName);
ViStatus _VI_FUNC rszvb_GetTraceRefValue (ViSession instrumentHandle,
                                          ViInt32 window, ViInt32 window_Trace,
                                          ViReal64* referenceLevel);
ViStatus _VI_FUNC rszvb_SetTraceRefPosition (ViSession instrumentHandle,
                                             ViInt32 window, ViInt32 window_Trace,
                                             ViReal64 referencePosition);
ViStatus _VI_FUNC rszvb_SetTraceRefPositionByName (ViSession instrumentHandle,
                                                   ViInt32 window,
                                                   ViReal64 referencePosition,
                                                   ViString traceName);
ViStatus _VI_FUNC rszvb_GetTraceRefPosition (ViSession instrumentHandle,
                                             ViInt32 window, ViInt32 window_Trace,
                                             ViReal64* referencePosition);
ViStatus _VI_FUNC rszvb_SetTraceTop (ViSession instrumentHandle, ViInt32 window,
                                     ViInt32 window_Trace, ViReal64 top);
ViStatus _VI_FUNC rszvb_GetTraceTop (ViSession instrumentHandle, ViInt32 window,
                                     ViInt32 window_Trace, ViReal64* top);
ViStatus _VI_FUNC rszvb_TraceAdd (ViSession instrumentHandle, ViInt32 channel,
                                  ViString traceName);
ViStatus _VI_FUNC rszvb_TraceAddMode (ViSession instrumentHandle, ViInt32 channel,
                                      ViString traceName, ViInt32 outMode,
                                      ViInt32 inMode);
ViStatus _VI_FUNC rszvb_SetTraceDisplayState (ViSession instrumentHandle,
                                              ViInt32 traceType,
                                              ViString singleTraceName,
                                              ViBoolean showTrace);
ViStatus _VI_FUNC rszvb_GetTraceDisplayState (ViSession instrumentHandle,
                                              ViInt32 traceType,
                                              ViString singleTraceName,
                                              ViBoolean* showTrace);
ViStatus _VI_FUNC rszvb_TraceAddSParameterGroup (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViInt32 numberOfLogicalPortNumbers,
                                                 ViInt32 _VI_FAR logicalPortNumber_s[]);
ViStatus _VI_FUNC rszvb_QueryTraceAddSParameterGroup (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 _VI_FAR logicalPortNumber_s[]);
ViStatus _VI_FUNC rszvb_TraceAddDiagramArea (ViSession instrumentHandle,
                                             ViInt32 window, ViInt32 window_Trace,
                                             ViInt32 channel, ViString traceName);
ViStatus _VI_FUNC rszvb_TraceAssignDiagramArea (ViSession instrumentHandle,
                                                ViInt32 window,
                                                ViInt32 window_Trace,
                                                ViString traceName);
ViStatus _VI_FUNC rszvb_TraceAssignWindowDiagramArea (ViSession instrumentHandle,
                                                      ViInt32 window,
                                                      ViString traceName);
ViStatus _VI_FUNC rszvb_TraceUnassignDiagramArea (ViSession instrumentHandle,
                                                  ViInt32 window,
                                                  ViInt32 window_Trace);
ViStatus _VI_FUNC rszvb_TraceSelect (ViSession instrumentHandle, ViInt32 channel,
                                     ViString traceName);
ViStatus _VI_FUNC rszvb_TraceDelete (ViSession instrumentHandle, ViInt32 channel,
                                     ViString traceName);
ViStatus _VI_FUNC rszvb_TraceDeleteAll (ViSession instrumentHandle,
                                        ViInt32 channel);
ViStatus _VI_FUNC rszvb_TraceDeleteAllChannels (ViSession instrumentHandle);
ViStatus _VI_FUNC rszvb_TraceList (ViSession instrumentHandle, ViInt32 channel,
                                   ViChar _VI_FAR catalog[], ViInt32 bufferSize);
ViStatus _VI_FUNC rszvb_TraceRename (ViSession instrumentHandle,
                                     ViString oldTraceName, ViString newTraceName);
ViStatus _VI_FUNC rszvb_ChannelTraceRename (ViSession instrumentHandle,
                                            ViInt32 channel, ViString traceName);
ViStatus _VI_FUNC rszvb_TraceListCatalog (ViSession instrumentHandle,
                                          ViChar _VI_FAR catalog[],
                                          ViInt32 bufferSize);
ViStatus _VI_FUNC rszvb_TraceGetTraceName (ViSession instrumentHandle,
                                           ViInt32 traceNumber,
                                           ViChar _VI_FAR traceName[]);
ViStatus _VI_FUNC rszvb_TraceGetTraceNumber (ViSession instrumentHandle,
                                             ViString traceName,
                                             ViInt32* traceNumber);
ViStatus _VI_FUNC rszvb_TraceGetChannelName (ViSession instrumentHandle,
                                             ViString traceName,
                                             ViChar _VI_FAR channelName[]);
ViStatus _VI_FUNC rszvb_TraceGetChannelNumber (ViSession instrumentHandle,
                                               ViString traceName,
                                               ViInt32* channelNumber);
ViStatus _VI_FUNC rszvb_TraceDataToMemory (ViSession instrumentHandle,
                                           ViInt32 channel_Trace);
ViStatus _VI_FUNC rszvb_TraceDataToMemoryTrace (ViSession instrumentHandle,
                                                ViString memoryTrace,
                                                ViString dataTrace);
ViStatus _VI_FUNC rszvb_TraceMathToMemoryTrace (ViSession instrumentHandle,
                                                ViString memoryTrace,
                                                ViString dataTrace);
ViStatus _VI_FUNC rszvb_DeleteMemoryTrace (ViSession instrumentHandle,
                                           ViInt32 memoryTrace);
ViStatus _VI_FUNC rszvb_TraceUserDefinedMath (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViString mathematicalExpression);
ViStatus _VI_FUNC rszvb_SetTraceMathState (ViSession instrumentHandle,
                                           ViInt32 channel_Trace,
                                           ViBoolean mathState);
ViStatus _VI_FUNC rszvb_GetTraceMathState (ViSession instrumentHandle,
                                           ViInt32 channel_Trace,
                                           ViBoolean* mathState);
ViStatus _VI_FUNC rszvb_SetTraceMathFunction (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViInt32 mathematicalFunction);
ViStatus _VI_FUNC rszvb_GetTraceMathFunction (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViInt32* mathematicalFunction);
ViStatus _VI_FUNC rszvb_SetTraceMathWaveQuantityState (ViSession instrumentHandle,
                                                       ViInt32 channel_Trace,
                                                       ViBoolean mathWaveQuantityState);
ViStatus _VI_FUNC rszvb_GetTraceMathWaveQuantityState (ViSession instrumentHandle,
                                                       ViInt32 channel_Trace,
                                                       ViBoolean* mathWaveQuantityState);
ViStatus _VI_FUNC rszvb_SetTraceTransformDomain (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViInt32 transformDomain);
ViStatus _VI_FUNC rszvb_GetTraceTransformDomain (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViInt32* transformDomain);
ViStatus _VI_FUNC rszvb_SetTraceTransformConversion (ViSession instrumentHandle,
                                                     ViInt32 channel_Trace,
                                                     ViInt32 conversion);
ViStatus _VI_FUNC rszvb_GetTraceTransformConversion (ViSession instrumentHandle,
                                                     ViInt32 channel_Trace,
                                                     ViInt32* conversion);
ViStatus _VI_FUNC rszvb_SetTimeDomainStartTime (ViSession instrumentHandle,
                                                ViInt32 channel_Trace,
                                                ViReal64 startTime);
ViStatus _VI_FUNC rszvb_GetTimeDomainStartTime (ViSession instrumentHandle,
                                                ViInt32 channel_Trace,
                                                ViReal64* startTime);
ViStatus _VI_FUNC rszvb_SetTimeDomainStopTime (ViSession instrumentHandle,
                                               ViInt32 channel_Trace,
                                               ViReal64 stopTime);
ViStatus _VI_FUNC rszvb_GetTimeDomainStopTime (ViSession instrumentHandle,
                                               ViInt32 channel_Trace,
                                               ViReal64* stopTime);
ViStatus _VI_FUNC rszvb_SetTimeDomainCenterTime (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViReal64 centerTime);
ViStatus _VI_FUNC rszvb_GetTimeDomainCenterTime (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViReal64* centerTime);
ViStatus _VI_FUNC rszvb_SetTimeDomainTimeSpan (ViSession instrumentHandle,
                                               ViInt32 channel_Trace,
                                               ViReal64 timeSpan);
ViStatus _VI_FUNC rszvb_GetTimeDomainTimeSpan (ViSession instrumentHandle,
                                               ViInt32 channel_Trace,
                                               ViReal64* timeSpan);
ViStatus _VI_FUNC rszvb_SetTimeDomainTimeAxisScaling (ViSession instrumentHandle,
                                                      ViInt32 channel_Trace,
                                                      ViInt32 timeAxisScaling);
ViStatus _VI_FUNC rszvb_GetTimeDomainTimeAxisScaling (ViSession instrumentHandle,
                                                      ViInt32 channel_Trace,
                                                      ViInt32* timeAxisScaling);
ViStatus _VI_FUNC rszvb_SetTimeDomainTransformationType (ViSession instrumentHandle,
                                                         ViInt32 channel_Trace,
                                                         ViInt32 transformationType);
ViStatus _VI_FUNC rszvb_GetTimeDomainTransformationType (ViSession instrumentHandle,
                                                         ViInt32 channel_Trace,
                                                         ViInt32* transformationType);
ViStatus _VI_FUNC rszvb_SetTimeDomainTransformationFilter
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViInt32 filterType);
ViStatus _VI_FUNC rszvb_GetTimeDomainTransformationFilter
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViInt32* filterType);
ViStatus _VI_FUNC rszvb_SetTimeDomainTransformationSidebandSuppression
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViReal64 sidebandSuppression);
ViStatus _VI_FUNC rszvb_GetTimeDomainTransformationSidebandSuppression
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViReal64* sidebandSuppression);
ViStatus _VI_FUNC rszvb_SetTimeDomainTransformationResolutionEfactor
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViReal64 resolution);
ViStatus _VI_FUNC rszvb_GetTimeDomainTransformationResolutionEfactor
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViReal64* resolution);
ViStatus _VI_FUNC rszvb_SetHarmonicGridAndKeep (ViSession instrumentHandle,
                                                ViInt32 channel_Trace,
                                                ViInt32 calculationMethod);
ViStatus _VI_FUNC rszvb_SetDCValue (ViSession instrumentHandle,
                                    ViInt32 channel_Trace, ViReal64 DCValue);
ViStatus _VI_FUNC rszvb_GetDCValue (ViSession instrumentHandle,
                                    ViInt32 channel_Trace, ViReal64* DCValue);
ViStatus _VI_FUNC rszvb_ExtrapolateDCValue (ViSession instrumentHandle,
                                            ViInt32 channel_Trace);
ViStatus _VI_FUNC rszvb_SetContinuousExtrapolation (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViBoolean continuousExtrapolation);
ViStatus _VI_FUNC rszvb_GetContinuousExtrapolation (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViBoolean* continuousExtrapolation);
ViStatus _VI_FUNC rszvb_CalculateHarmonicGrid (ViSession instrumentHandle,
                                               ViInt32 channel_Trace);
ViStatus _VI_FUNC rszvb_SetTimeGateState (ViSession instrumentHandle,
                                          ViInt32 channel_Trace,
                                          ViBoolean timeGate);
ViStatus _VI_FUNC rszvb_GetTimeGateState (ViSession instrumentHandle,
                                          ViInt32 channel_Trace,
                                          ViBoolean* timeGate);
ViStatus _VI_FUNC rszvb_SetTimeGateStartTime (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViReal64 startTime);
ViStatus _VI_FUNC rszvb_GetTimeGateStartTime (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViReal64* startTime);
ViStatus _VI_FUNC rszvb_SetTimeGateStopTime (ViSession instrumentHandle,
                                             ViInt32 channel_Trace,
                                             ViReal64 stopTime);
ViStatus _VI_FUNC rszvb_GetTimeGateStopTime (ViSession instrumentHandle,
                                             ViInt32 channel_Trace,
                                             ViReal64* stopTime);
ViStatus _VI_FUNC rszvb_SetTimeGateCenterTime (ViSession instrumentHandle,
                                               ViInt32 channel_Trace,
                                               ViReal64 centerTime);
ViStatus _VI_FUNC rszvb_GetTimeGateCenterTime (ViSession instrumentHandle,
                                               ViInt32 channel_Trace,
                                               ViReal64* centerTime);
ViStatus _VI_FUNC rszvb_SetTimeGateType (ViSession instrumentHandle,
                                         ViInt32 channel_Trace,
                                         ViInt32 timeGateType);
ViStatus _VI_FUNC rszvb_GetTimeGateType (ViSession instrumentHandle,
                                         ViInt32 channel_Trace,
                                         ViInt32* timeGateType);
ViStatus _VI_FUNC rszvb_SetTimeGateFilter (ViSession instrumentHandle,
                                           ViInt32 channel_Trace,
                                           ViInt32 filterType);
ViStatus _VI_FUNC rszvb_GetTimeGateFilter (ViSession instrumentHandle,
                                           ViInt32 channel_Trace,
                                           ViInt32* filterType);
ViStatus _VI_FUNC rszvb_SetTimeGateSidebandSuppression (ViSession instrumentHandle,
                                                        ViInt32 channel_Trace,
                                                        ViReal64 sidebandSuppression);
ViStatus _VI_FUNC rszvb_GetTimeGateSidebandSuppression (ViSession instrumentHandle,
                                                        ViInt32 channel_Trace,
                                                        ViReal64* sidebandSuppression);
ViStatus _VI_FUNC rszvb_SetTimeGateShape (ViSession instrumentHandle,
                                          ViInt32 channel_Trace,
                                          ViInt32 timeGateShape);
ViStatus _VI_FUNC rszvb_GetTimeGateShape (ViSession instrumentHandle,
                                          ViInt32 channel_Trace,
                                          ViInt32* timeGateShape);
ViStatus _VI_FUNC rszvb_SetTimeGateSpan (ViSession instrumentHandle,
                                         ViInt32 channel_Trace, ViReal64 span);
ViStatus _VI_FUNC rszvb_GetTimeGateSpan (ViSession instrumentHandle,
                                         ViInt32 channel_Trace, ViReal64* span);
ViStatus _VI_FUNC rszvb_SetTimeGateDisplayState (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViBoolean timeGateDisplay);
ViStatus _VI_FUNC rszvb_GetTimeGateDisplayState (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViBoolean* timeGateDisplay);
ViStatus _VI_FUNC rszvb_TraceEvaluationRange (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViInt32 evaluationRange,
                                              ViReal64 start, ViReal64 stop);
ViStatus _VI_FUNC rszvb_TraceStatisticalEvaluation (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 statisticalParameter,
                                                    ViBoolean infoField,
                                                    ViReal64 _VI_FAR responseValue_s[]);
ViStatus _VI_FUNC rszvb_SetTraceEvaluationRangeShow (ViSession instrumentHandle,
                                                     ViInt32 channel_Trace,
                                                     ViBoolean showRange);
ViStatus _VI_FUNC rszvb_GetTraceEvaluationRangeShow (ViSession instrumentHandle,
                                                     ViInt32 channel_Trace,
                                                     ViBoolean* showRange);
ViStatus _VI_FUNC rszvb_SetTraceCompressionValue (ViSession instrumentHandle,
                                                  ViInt32 channel_Trace,
                                                  ViReal64 compressionValue);
ViStatus _VI_FUNC rszvb_GetTraceCompressionValue (ViSession instrumentHandle,
                                                  ViInt32 channel_Trace,
                                                  ViReal64* compressionValue);
ViStatus _VI_FUNC rszvb_GetTraceCompressionPoint (ViSession instrumentHandle,
                                                  ViInt32 channel_Trace,
                                                  ViReal64* compressionPointIn,
                                                  ViReal64* compressionPointOut);
ViStatus _VI_FUNC rszvb_SetDisplayResultsState (ViSession instrumentHandle,
                                                ViInt32 channel_Trace,
                                                ViInt32 resultType,
                                                ViBoolean displayResults);
ViStatus _VI_FUNC rszvb_GetDisplayResultsState (ViSession instrumentHandle,
                                                ViInt32 channel_Trace,
                                                ViInt32 resultType,
                                                ViBoolean* displayResults);
ViStatus _VI_FUNC rszvb_SetTraceSmoothing (ViSession instrumentHandle,
                                           ViInt32 channel_Trace,
                                           ViBoolean smoothing, ViReal64 aperture);
ViStatus _VI_FUNC rszvb_GetTraceSmoothing (ViSession instrumentHandle,
                                           ViInt32 channel_Trace,
                                           ViBoolean* smoothing,
                                           ViReal64* aperture);
ViStatus _VI_FUNC rszvb_TraceResponseData (ViSession instrumentHandle,
                                           ViInt32 channel_Trace,
                                           ViInt32 dataFormat, ViInt32* noOfValues,
                                           ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_TraceResponseDataError (ViSession instrumentHandle,
                                                ViInt32 channel_Trace,
                                                ViInt32 errorTerm,
                                                ViInt32* noOfValues,
                                                ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_TraceResponseDataAll (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViInt32 dataFormat,
                                              ViInt32* noOfValues,
                                              ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_TraceComplexResponseData (ViSession instrumentHandle,
                                                  ViInt32 channel_Trace,
                                                  ViInt32 dataFormat,
                                                  ViInt32* noOfValues,
                                                  ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_TraceComplexResponseCatalog (ViSession instrumentHandle,
                                                     ViInt32 channel_Trace,
                                                     ViInt32 bufferSize,
                                                     ViChar _VI_FAR catalog[]);
ViStatus _VI_FUNC rszvb_TraceResponseDataAllData (ViSession instrumentHandle,
                                                  ViInt32 channel_Trace,
                                                  ViInt32 dataFormat,
                                                  ViInt32* noOfValues,
                                                  ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_TraceResponseSingleSweepData (ViSession instrumentHandle,
                                                      ViInt32 channel_Trace,
                                                      ViInt32 sweepNumber,
                                                      ViInt32* noOfValues,
                                                      ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_TraceResponseSingleSweepDataCount
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViInt32* sweepCount);
ViStatus _VI_FUNC rszvb_TraceResponseSingleSweepDataForward
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViInt32 sweepNumber, ViInt32* noOfValues,
              ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_TraceStimulusData (ViSession instrumentHandle,
                                           ViInt32 channel_Trace,
                                           ViInt32* noOfValues,
                                           ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_WriteMemoryTraceData (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViInt32 noOfPoints,
                                              ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_WriteMemoryTraceDataExt (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViInt32 dataFormat,
                                                 ViInt32 noOfPoints,
                                                 ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_SetTraceFormatZVR (ViSession instrumentHandle,
                                           ViInt32 dataFormat);
ViStatus _VI_FUNC rszvb_GetTraceFormatZVR (ViSession instrumentHandle,
                                           ViInt32* dataFormat);
ViStatus _VI_FUNC rszvb_TraceResponseDataZVR (ViSession instrumentHandle,
                                              ViInt32 dataFormat,
                                              ViInt32 valuesToReturn,
                                              ViInt32* noOfValues,
                                              ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_TraceStimulusDataZVR (ViSession instrumentHandle,
                                              ViInt32 dataFormat,
                                              ViInt32 valuesToReturn,
                                              ViInt32* noOfValues,
                                              ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_TraceResponseDataSParameterGroup (ViSession instrumentHandle,
                                                          ViInt32 channel_Trace,
                                                          ViInt32 dataFormat,
                                                          ViInt32 valuesToReturn,
                                                          ViInt32* noOfValues,
                                                          ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_TraceImportData (ViSession instrumentHandle,
                                         ViString traceName, ViString fileName);
ViStatus _VI_FUNC rszvb_TraceExportData (ViSession instrumentHandle,
                                         ViString traceName, ViString fileName);
ViStatus _VI_FUNC rszvb_TraceExportDataWithOptions (ViSession instrumentHandle,
                                                    ViString traceName,
                                                    ViString fileName,
                                                    ViInt32 exportFormat,
                                                    ViInt32 exportData);
ViStatus _VI_FUNC rszvb_TraceExportDataWithOptionsExt (ViSession instrumentHandle,
                                                       ViString traceName,
                                                       ViString fileName,
                                                       ViInt32 exportFormat,
                                                       ViInt32 exportData,
                                                       ViInt32 decimalSeparator,
                                                       ViInt32 fieldSeparator);
ViStatus _VI_FUNC rszvb_ChannelTraceExportData (ViSession instrumentHandle,
                                                ViInt32 selectChannel,
                                                ViInt32 channel_Trace,
                                                ViString fileName);
ViStatus _VI_FUNC rszvb_ChannelTraceExportDataWithOptions
             (ViSession instrumentHandle, ViInt32 selectChannel,
              ViInt32 channel_Trace, ViString fileName, ViInt32 exportFormat,
              ViInt32 exportData);
ViStatus _VI_FUNC rszvb_ChannelTraceExportDataWithOptionsExt
             (ViSession instrumentHandle, ViInt32 selectChannel,
              ViInt32 channel_Trace, ViString fileName, ViInt32 exportFormat,
              ViInt32 exportData, ViInt32 decimalSeparator, ViInt32 fieldSeparator);
ViStatus _VI_FUNC rszvb_TraceExportDataPorts (ViSession instrumentHandle,
                                              ViInt32 channel, ViString fileName,
                                              ViInt32 exportData, ViInt32 port1,
                                              ViInt32 port2, ViInt32 port3,
                                              ViInt32 port4);
ViStatus _VI_FUNC rszvb_TraceExportDataPortsIncomplete (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViString fileName,
                                                        ViInt32 exportData,
                                                        ViInt32 port1,
                                                        ViInt32 port2,
                                                        ViInt32 port3,
                                                        ViInt32 port4);
ViStatus _VI_FUNC rszvb_SetRenormalizationState (ViSession instrumentHandle,
                                                 ViBoolean state);
ViStatus _VI_FUNC rszvb_GetRenormalizationState (ViSession instrumentHandle,
                                                 ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetRenormalizationMode (ViSession instrumentHandle,
                                                ViInt32 mode);
ViStatus _VI_FUNC rszvb_GetRenormalizationMode (ViSession instrumentHandle,
                                                ViInt32* mode);
ViStatus _VI_FUNC rszvb_SetRenormalizationImpedance (ViSession instrumentHandle,
                                                     ViReal64 impedance);
ViStatus _VI_FUNC rszvb_GetRenormalizationImpedance (ViSession instrumentHandle,
                                                     ViReal64* impedance);
ViStatus _VI_FUNC rszvb_TraceShiftStimulusValue (ViSession instrumentHandle,
                                                 ViInt32 window,
                                                 ViInt32 window_Trace,
                                                 ViReal64 shiftStimulusValue);
ViStatus _VI_FUNC rszvb_TraceShiftResponseValue (ViSession instrumentHandle,
                                                 ViInt32 window,
                                                 ViInt32 window_Trace,
                                                 ViReal64 magnitude, ViReal64 phase,
                                                 ViReal64 real, ViReal64 imaginary);
ViStatus _VI_FUNC rszvb_SetHold (ViSession instrumentHandle, ViInt32 channel,
                                 ViInt32 hold);
ViStatus _VI_FUNC rszvb_GetHold (ViSession instrumentHandle, ViInt32 channel,
                                 ViInt32* hold);
ViStatus _VI_FUNC rszvb_LinearityDeviationManual (ViSession instrumentHandle,
                                                  ViInt32 channel, ViReal64 slope,
                                                  ViReal64 constant,
                                                  ViReal64 electricalLength);
ViStatus _VI_FUNC rszvb_LinearityDeviationAuto (ViSession instrumentHandle,
                                                ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetLinearityDeviationState (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 state);
ViStatus _VI_FUNC rszvb_GetLinearityDeviationState (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32* state);
ViStatus _VI_FUNC rszvb_SetLinearityDeviationSlope (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViReal64 slope);
ViStatus _VI_FUNC rszvb_GetLinearityDeviationSlope (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViReal64* slope);
ViStatus _VI_FUNC rszvb_SetLinearityDeviationConstant (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViReal64 constant);
ViStatus _VI_FUNC rszvb_GetLinearityDeviationConstant (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViReal64* constant);
ViStatus _VI_FUNC rszvb_SetLinearityDeviationElectricalLength
             (ViSession instrumentHandle, ViInt32 channel,
              ViReal64 electricalLength);
ViStatus _VI_FUNC rszvb_GetLinearityDeviationElectricalLength
             (ViSession instrumentHandle, ViInt32 channel,
              ViReal64* electricalLength);
ViStatus _VI_FUNC rszvb_SetMarkerState (ViSession instrumentHandle,
                                        ViInt32 channel_Trace, ViInt32 marker,
                                        ViBoolean markerState);
ViStatus _VI_FUNC rszvb_GetMarkerState (ViSession instrumentHandle,
                                        ViInt32 channel_Trace, ViInt32 marker,
                                        ViBoolean* markerState);
ViStatus _VI_FUNC rszvb_SetMarkerStimulus (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker,
                                           ViReal64 markerStimulus);
ViStatus _VI_FUNC rszvb_GetMarkerStimulus (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker,
                                           ViReal64* markerStimulus);
ViStatus _VI_FUNC rszvb_GetMarkerResponse (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker,
                                           ViReal64 _VI_FAR markerResponse[]);
ViStatus _VI_FUNC rszvb_SetReferenceMarkerState (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViInt32 marker,
                                                 ViBoolean referenceMarkerState);
ViStatus _VI_FUNC rszvb_GetReferenceMarkerState (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViInt32 marker,
                                                 ViBoolean* referenceMarkerState);
ViStatus _VI_FUNC rszvb_SetReferenceMarkerStimulus (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 marker,
                                                    ViReal64 referenceMarkerStimulus);
ViStatus _VI_FUNC rszvb_GetReferenceMarkerStimulus (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 marker,
                                                    ViReal64* referenceMarkerStimulus);
ViStatus _VI_FUNC rszvb_GetReferenceMarkerResponse (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 marker,
                                                    ViReal64* referenceMarkerResponse);
ViStatus _VI_FUNC rszvb_SetReferenceDiscreteMarker (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 marker, ViInt32 mode);
ViStatus _VI_FUNC rszvb_GetReferenceDiscreteMarker (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 marker, ViInt32* mode);
ViStatus _VI_FUNC rszvb_SetReferenceFixedMarker (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViInt32 marker, ViInt32 type);
ViStatus _VI_FUNC rszvb_GetReferenceFixedMarker (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViInt32 marker, ViInt32* type);
ViStatus _VI_FUNC rszvb_SetDeltaMarkerState (ViSession instrumentHandle,
                                             ViInt32 channel_Trace, ViInt32 marker,
                                             ViBoolean deltaMarkerState);
ViStatus _VI_FUNC rszvb_GetDeltaMarkerState (ViSession instrumentHandle,
                                             ViInt32 channel_Trace, ViInt32 marker,
                                             ViBoolean* deltaMarkerState);
ViStatus _VI_FUNC rszvb_SetCoupledMarkers (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker,
                                           ViBoolean markerCoupled);
ViStatus _VI_FUNC rszvb_GetCoupledMarkers (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker,
                                           ViBoolean* markerCoupled);
ViStatus _VI_FUNC rszvb_SetDiscreteMarker (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker,
                                           ViInt32 discreteMode);
ViStatus _VI_FUNC rszvb_GetDiscreteMarker (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker,
                                           ViInt32* discreteMode);
ViStatus _VI_FUNC rszvb_SetFixedMarker (ViSession instrumentHandle,
                                        ViInt32 channel_Trace, ViInt32 marker,
                                        ViInt32 fixedMarker);
ViStatus _VI_FUNC rszvb_GetFixedMarker (ViSession instrumentHandle,
                                        ViInt32 channel_Trace, ViInt32 marker,
                                        ViInt32* fixedMarker);
ViStatus _VI_FUNC rszvb_SetMarkerFormat (ViSession instrumentHandle,
                                         ViInt32 channel_Trace, ViInt32 marker,
                                         ViInt32 markerFormat);
ViStatus _VI_FUNC rszvb_GetMarkerFormat (ViSession instrumentHandle,
                                         ViInt32 channel_Trace, ViInt32 marker,
                                         ViInt32* markerFormat);
ViStatus _VI_FUNC rszvb_SetAllMarkersOff (ViSession instrumentHandle,
                                          ViInt32 channel_Trace);
ViStatus _VI_FUNC rszvb_SaveAllMarkers (ViSession instrumentHandle,
                                        ViString fileName);
ViStatus _VI_FUNC rszvb_MarkerSearch (ViSession instrumentHandle,
                                      ViInt32 channel_Trace, ViInt32 marker,
                                      ViInt32 search);
ViStatus _VI_FUNC rszvb_MarkerTargetSearch (ViSession instrumentHandle,
                                            ViInt32 channel_Trace, ViInt32 marker,
                                            ViInt32 search);
ViStatus _VI_FUNC rszvb_SetMarkerTargetValue (ViSession instrumentHandle,
                                              ViInt32 channel_Trace, ViInt32 marker,
                                              ViReal64 targetValue);
ViStatus _VI_FUNC rszvb_GetMarkerTargetValue (ViSession instrumentHandle,
                                              ViInt32 channel_Trace, ViInt32 marker,
                                              ViReal64* targetValue);
ViStatus _VI_FUNC rszvb_MarkerBandpassSearch (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViInt32 marker);
ViStatus _VI_FUNC rszvb_MarkerBandstopSearch (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViInt32 marker);
ViStatus _VI_FUNC rszvb_SetMarkerSearchMode (ViSession instrumentHandle,
                                             ViInt32 channel_Trace, ViInt32 marker,
                                             ViInt32 searchMode);
ViStatus _VI_FUNC rszvb_GetMarkerSearchMode (ViSession instrumentHandle,
                                             ViInt32 channel_Trace, ViInt32 marker,
                                             ViInt32* searchMode);
ViStatus _VI_FUNC rszvb_MarkerBandfilterTracking (ViSession instrumentHandle,
                                                  ViInt32 channel_Trace,
                                                  ViInt32 marker,
                                                  ViBoolean bandfilterTracking);
ViStatus _VI_FUNC rszvb_MarkerxdBBandwidth (ViSession instrumentHandle,
                                            ViInt32 channel_Trace, ViInt32 marker,
                                            ViReal64 xDBBandwidth);
ViStatus _VI_FUNC rszvb_MarkerBandfilterResults (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace,
                                                 ViInt32 marker,
                                                 ViReal64* bandwidth,
                                                 ViReal64* centerStimulus,
                                                 ViReal64* q, ViReal64* loss,
                                                 ViReal64* LBE, ViReal64* UBE);
ViStatus _VI_FUNC rszvb_MarkerxdBBandwidthZVR (ViSession instrumentHandle,
                                               ViInt32 channel_Trace,
                                               ViInt32 marker,
                                               ViReal64 xDBBandwidth);
ViStatus _VI_FUNC rszvb_MarkerBandfilterResultsZVR (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 marker,
                                                    ViReal64* bandwidth);
ViStatus _VI_FUNC rszvb_SetMarkerSearchResultState (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 marker,
                                                    ViBoolean searchResults);
ViStatus _VI_FUNC rszvb_GetMarkerSearchResultState (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 marker,
                                                    ViBoolean* searchResults);
ViStatus _VI_FUNC rszvb_SetMarkerTracking (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker,
                                           ViBoolean markerTracking);
ViStatus _VI_FUNC rszvb_GetMarkerTracking (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker,
                                           ViBoolean* markerTracking);
ViStatus _VI_FUNC rszvb_MarkerSearchRange (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker,
                                           ViInt32 searchRange, ViReal64 start,
                                           ViReal64 stop);
ViStatus _VI_FUNC rszvb_SetMarkerSearchRangeShow (ViSession instrumentHandle,
                                                  ViInt32 channel_Trace,
                                                  ViInt32 marker,
                                                  ViBoolean showRange);
ViStatus _VI_FUNC rszvb_GetMarkerSearchRangeShow (ViSession instrumentHandle,
                                                  ViInt32 channel_Trace,
                                                  ViInt32 marker,
                                                  ViBoolean* showRange);
ViStatus _VI_FUNC rszvb_MarkerSearchResults (ViSession instrumentHandle,
                                             ViInt32 channel_Trace, ViInt32 marker,
                                             ViReal64* markerStimulus,
                                             ViReal64 _VI_FAR markerResponse[]);
ViStatus _VI_FUNC rszvb_SetStartToMarker (ViSession instrumentHandle,
                                          ViInt32 channel_Trace, ViInt32 marker);
ViStatus _VI_FUNC rszvb_SetStopToMarker (ViSession instrumentHandle,
                                         ViInt32 channel_Trace, ViInt32 marker);
ViStatus _VI_FUNC rszvb_SetCenterToMarker (ViSession instrumentHandle,
                                           ViInt32 channel_Trace, ViInt32 marker);
ViStatus _VI_FUNC rszvb_ShowLimitLine (ViSession instrumentHandle,
                                       ViInt32 channel_Trace,
                                       ViBoolean displayLimitLine);
ViStatus _VI_FUNC rszvb_SetLimitCheck (ViSession instrumentHandle,
                                       ViInt32 channel_Trace, ViInt32 limitLine,
                                       ViBoolean limitCheck);
ViStatus _VI_FUNC rszvb_GetLimitCheck (ViSession instrumentHandle,
                                       ViInt32 channel_Trace, ViInt32 limitLine,
                                       ViBoolean* limitCheck);
ViStatus _VI_FUNC rszvb_SetLimitLineFailBeep (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViBoolean failBeep);
ViStatus _VI_FUNC rszvb_GetLimitLineFailBeep (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViBoolean* failBeep);
ViStatus _VI_FUNC rszvb_GetLimitCheckResult (ViSession instrumentHandle,
                                             ViInt32 channel_Trace,
                                             ViInt32* limitCheckResult);
ViStatus _VI_FUNC rszvb_AddLimitLineSegment (ViSession instrumentHandle,
                                             ViInt32 channel_Trace, ViInt32 segment,
                                             ViInt32 type, ViReal64 startStimulus,
                                             ViReal64 stopStimulus,
                                             ViReal64 startResponse,
                                             ViReal64 stopResponse);
ViStatus _VI_FUNC rszvb_EditLimitLineSegment (ViSession instrumentHandle,
                                              ViInt32 channel_Trace,
                                              ViInt32 segment, ViInt32 type,
                                              ViReal64 startStimulus,
                                              ViReal64 stopStimulus,
                                              ViReal64 startResponse,
                                              ViReal64 stopResponse);
ViStatus _VI_FUNC rszvb_ReadLimitLineSegmentList (ViSession instrumentHandle,
                                                  ViInt32 channel_Trace,
                                                  ViInt32 listSize,
                                                  ViInt32* segmentsCount,
                                                  ViInt32 _VI_FAR type[],
                                                  ViReal64 _VI_FAR startStimulus[],
                                                  ViReal64 _VI_FAR stopStimulus[],
                                                  ViReal64 _VI_FAR startResponse[],
                                                  ViReal64 _VI_FAR stopResponse[]);
ViStatus _VI_FUNC rszvb_WriteLimitLineSegmentList (ViSession instrumentHandle,
                                                   ViInt32 channel_Trace,
                                                   ViInt32 listSize, ViInt32 type,
                                                   ViReal64 _VI_FAR startStimulus[],
                                                   ViReal64 _VI_FAR stopStimulus[],
                                                   ViReal64 _VI_FAR startResponse[],
                                                   ViReal64 _VI_FAR stopResponse[]);
ViStatus _VI_FUNC rszvb_ShiftLimitLineSegmentList (ViSession instrumentHandle,
                                                   ViInt32 channel_Trace,
                                                   ViInt32 limitLineType,
                                                   ViReal64 stimulusOffset,
                                                   ViReal64 responseOffset);
ViStatus _VI_FUNC rszvb_DeleteLimitLineSegments (ViSession instrumentHandle,
                                                 ViInt32 channel_Trace);
ViStatus _VI_FUNC rszvb_RecallLimitLine (ViSession instrumentHandle,
                                         ViString traceName, ViString fileName);
ViStatus _VI_FUNC rszvb_RecallLimitLineWithOptions (ViSession instrumentHandle,
                                                    ViString traceName,
                                                    ViString fileName,
                                                    ViString sParameter,
                                                    ViReal64 xOffset,
                                                    ViReal64 yOffset, ViInt32 type);
ViStatus _VI_FUNC rszvb_SaveLimitLine (ViSession instrumentHandle,
                                       ViString traceName, ViString fileName);
ViStatus _VI_FUNC rszvb_ImportTraceasLimitLine (ViSession instrumentHandle,
                                                ViInt32 channel_Trace,
                                                ViInt32 limitLineType,
                                                ViReal64 stimulusOffset,
                                                ViReal64 responseOffset,
                                                ViString traceName);
ViStatus _VI_FUNC rszvb_SetLimitLineTTLOutPass (ViSession instrumentHandle,
                                                ViInt32 channel_Trace,
                                                ViInt32 outputNo,
                                                ViBoolean TTLOutput);
ViStatus _VI_FUNC rszvb_GetLimitLineTTLOutPass (ViSession instrumentHandle,
                                                ViInt32 channel_Trace,
                                                ViInt32 outputNo,
                                                ViBoolean* TTLOutput);
ViStatus _VI_FUNC rszvb_SetDisplayLine (ViSession instrumentHandle,
                                        ViInt32 channel_Trace,
                                        ViBoolean displayLine, ViReal64 position);
ViStatus _VI_FUNC rszvb_GetDisplayLine (ViSession instrumentHandle,
                                        ViInt32 channel_Trace,
                                        ViBoolean* displayLine, ViReal64* position);
ViStatus _VI_FUNC rszvb_SetLimitDomainUnits (ViSession instrumentHandle,
                                             ViInt32 channel_Trace,
                                             ViInt32 domainUnits);
ViStatus _VI_FUNC rszvb_SetLimitResponseDomainComplexUnits
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViInt32 responseUnits);
ViStatus _VI_FUNC rszvb_SetLimitResponseDomainFormatUnits
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViInt32 responseUnits);
ViStatus _VI_FUNC rszvb_SetLimitResponseDomainSpacingUnits
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViInt32 responseUnits);
ViStatus _VI_FUNC rszvb_SetRippleCheckOn (ViSession instrumentHandle,
                                          ViInt32 channel_Trace,
                                          ViBoolean limitCheck);
ViStatus _VI_FUNC rszvb_GetRippleCheckOn (ViSession instrumentHandle,
                                          ViInt32 channel_Trace,
                                          ViBoolean* limitCheck);
ViStatus _VI_FUNC rszvb_GetRippleLimitGlobalCheckResult (ViSession instrumentHandle,
                                                         ViInt32 channel_Trace,
                                                         ViInt32* rippleLimitCheckResult);
ViStatus _VI_FUNC rszvb_SetCheckRippleLimitRangeSegment (ViSession instrumentHandle,
                                                         ViInt32 channel_Trace,
                                                         ViInt32 segment,
                                                         ViBoolean limitCheck);
ViStatus _VI_FUNC rszvb_GetCheckRippleLimitRangeSegment (ViSession instrumentHandle,
                                                         ViInt32 channel_Trace,
                                                         ViInt32 segment,
                                                         ViBoolean* limitCheck);
ViStatus _VI_FUNC rszvb_GetRippleLimitCheckSegmentResult (ViSession instrumentHandle,
                                                          ViInt32 channel_Trace,
                                                          ViInt32 segment,
                                                          ViInt32* fail,
                                                          ViReal64* limitCheckResult);
ViStatus _VI_FUNC rszvb_SetRippleLimitsDisplayState (ViSession instrumentHandle,
                                                     ViInt32 channel_Trace,
                                                     ViBoolean displayLine);
ViStatus _VI_FUNC rszvb_GetRippleLimitsDisplayState (ViSession instrumentHandle,
                                                     ViInt32 channel_Trace,
                                                     ViBoolean* displayLine);
ViStatus _VI_FUNC rszvb_SetRippleFailBeepOn (ViSession instrumentHandle,
                                             ViInt32 channel_Trace,
                                             ViBoolean failBeep);
ViStatus _VI_FUNC rszvb_GetRippleFailBeepOn (ViSession instrumentHandle,
                                             ViInt32 channel_Trace,
                                             ViBoolean* failBeep);
ViStatus _VI_FUNC rszvb_AddRippleLimitLineRangesSegment (ViSession instrumentHandle,
                                                         ViInt32 channel_Trace,
                                                         ViInt32 noOfValues,
                                                         ViInt32 _VI_FAR type[],
                                                         ViReal64 _VI_FAR startStimulus[],
                                                         ViReal64 _VI_FAR stopStimulus[],
                                                         ViReal64 _VI_FAR limit[]);
ViStatus _VI_FUNC rszvb_EditRippleLimitLineSegment (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 segment,
                                                    ViReal64 startStimulus,
                                                    ViReal64 stopStimulus);
ViStatus _VI_FUNC rszvb_DeleteAllRippleLimitRanges (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace);
ViStatus _VI_FUNC rszvb_SetRippleLimitPhysicalUnits (ViSession instrumentHandle,
                                                     ViInt32 channel_Trace,
                                                     ViInt32 physicalUnits);
ViStatus _VI_FUNC rszvb_SetRippleLimitResponseDomainFormatUnits
             (ViSession instrumentHandle, ViInt32 channel_Trace,
              ViInt32 responseUnits);
ViStatus _VI_FUNC rszvb_GetNumberRippleLimitRanges (ViSession instrumentHandle,
                                                    ViInt32 channel_Trace,
                                                    ViInt32 segment,
                                                    ViInt32* number);
ViStatus _VI_FUNC rszvb_SetRippleLimitRange (ViSession instrumentHandle,
                                             ViInt32 channel_Trace, ViInt32 segment,
                                             ViReal64 limit);
ViStatus _VI_FUNC rszvb_GetRippleLimitRange (ViSession instrumentHandle,
                                             ViInt32 channel_Trace, ViInt32 segment,
                                             ViReal64* limit);
ViStatus _VI_FUNC rszvb_SaveRecallRippleLimit (ViSession instrumentHandle,
                                               ViInt32 operationToBePerformed,
                                               ViString traceName,
                                               ViString fileName);
ViStatus _VI_FUNC rszvb_SetStartFrequency (ViSession instrumentHandle,
                                           ViInt32 channel,
                                           ViReal64 startFrequency);
ViStatus _VI_FUNC rszvb_GetStartFrequency (ViSession instrumentHandle,
                                           ViInt32 channel,
                                           ViReal64* startFrequency);
ViStatus _VI_FUNC rszvb_SetStopFrequency (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64 stopFrequency);
ViStatus _VI_FUNC rszvb_GetStopFrequency (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64* stopFrequency);
ViStatus _VI_FUNC rszvb_SetCenterFrequency (ViSession instrumentHandle,
                                            ViInt32 channel,
                                            ViReal64 centerFrequency);
ViStatus _VI_FUNC rszvb_GetCenterFrequency (ViSession instrumentHandle,
                                            ViInt32 channel,
                                            ViReal64* centerFrequency);
ViStatus _VI_FUNC rszvb_SetFrequencySpan (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64 span);
ViStatus _VI_FUNC rszvb_GetFrequencySpan (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64* span);
ViStatus _VI_FUNC rszvb_SetPower (ViSession instrumentHandle, ViInt32 channel,
                                  ViReal64 power);
ViStatus _VI_FUNC rszvb_GetPower (ViSession instrumentHandle, ViInt32 channel,
                                  ViReal64* power);
ViStatus _VI_FUNC rszvb_SetCWFrequency (ViSession instrumentHandle, ViInt32 channel,
                                        ViReal64 CWFrequency);
ViStatus _VI_FUNC rszvb_GetCWFrequency (ViSession instrumentHandle, ViInt32 channel,
                                        ViReal64* CWFrequency);
ViStatus _VI_FUNC rszvb_SetStartPower (ViSession instrumentHandle, ViInt32 channel,
                                       ViReal64 startPower);
ViStatus _VI_FUNC rszvb_GetStartPower (ViSession instrumentHandle, ViInt32 channel,
                                       ViReal64* startPower);
ViStatus _VI_FUNC rszvb_SetStopPower (ViSession instrumentHandle, ViInt32 channel,
                                      ViReal64 stopPower);
ViStatus _VI_FUNC rszvb_GetStopPower (ViSession instrumentHandle, ViInt32 channel,
                                      ViReal64* stopPower);
ViStatus _VI_FUNC rszvb_SetSourcePort (ViSession instrumentHandle, ViInt32 channel,
                                       ViInt32 sourcePort);
ViStatus _VI_FUNC rszvb_GetSourcePort (ViSession instrumentHandle, ViInt32 channel,
                                       ViInt32* sourcePort);
ViStatus _VI_FUNC rszvb_ConfigurePowerBandwidthAverage (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViBoolean RFState,
                                                        ViReal64 measBandwidth,
                                                        ViBoolean averageState,
                                                        ViInt32 averageFactor);
ViStatus _VI_FUNC rszvb_SetReceiverStepAttenuators (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 analyzerPort,
                                                    ViReal64 attenuationFactor);
ViStatus _VI_FUNC rszvb_GetReceiverStepAttenuators (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 analyzerPort,
                                                    ViReal64* attenuationFactor);
ViStatus _VI_FUNC rszvb_SetGeneratorStepAttenuators (ViSession instrumentHandle,
                                                     ViInt32 channel, ViInt32 port,
                                                     ViReal64 attenuationFactor);
ViStatus _VI_FUNC rszvb_GetGeneratorStepAttenuators (ViSession instrumentHandle,
                                                     ViInt32 channel, ViInt32 port,
                                                     ViReal64* attenuationFactor);
ViStatus _VI_FUNC rszvb_SetAutomaticGeneratorAttenuator (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 port,
                                                         ViBoolean automaticAttenuation);
ViStatus _VI_FUNC rszvb_GetAutomaticGeneratorAttenuator (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 port,
                                                         ViBoolean* automaticAttenuation);
ViStatus _VI_FUNC rszvb_GetAutomaticGeneratorAttenuation (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 port,
                                                          ViReal64* attenuation);
ViStatus _VI_FUNC rszvb_SetGeneratorAttenuatorMode (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 port,
                                                    ViInt32 attenuationMode);
ViStatus _VI_FUNC rszvb_GetGeneratorAttenuatorMode (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 port,
                                                    ViInt32* attenuationMode);
ViStatus _VI_FUNC rszvb_SetRFState (ViSession instrumentHandle, ViBoolean RFState);
ViStatus _VI_FUNC rszvb_GetRFState (ViSession instrumentHandle, ViBoolean* RFState);
ViStatus _VI_FUNC rszvb_SetMeasBandwidth (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64 measBandwidth);
ViStatus _VI_FUNC rszvb_GetMeasBandwidth (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64* measBandwidth);
ViStatus _VI_FUNC rszvb_SetMeasBandwidthSelectivity (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 measBandwidthSelectivity);
ViStatus _VI_FUNC rszvb_GetMeasBandwidthSelectivity (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32* measBandwidthSelectivity);
ViStatus _VI_FUNC rszvb_SetMeasBandwidthReduction (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViBoolean reduction);
ViStatus _VI_FUNC rszvb_GetMeasBandwidthReduction (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViBoolean* reduction);
ViStatus _VI_FUNC rszvb_SetAverageState (ViSession instrumentHandle,
                                         ViInt32 channel, ViBoolean averageState);
ViStatus _VI_FUNC rszvb_GetAverageState (ViSession instrumentHandle,
                                         ViInt32 channel, ViBoolean* averageState);
ViStatus _VI_FUNC rszvb_SetAverageFactor (ViSession instrumentHandle,
                                          ViInt32 channel, ViInt32 averageFactor);
ViStatus _VI_FUNC rszvb_GetAverageFactor (ViSession instrumentHandle,
                                          ViInt32 channel, ViInt32* averageFactor);
ViStatus _VI_FUNC rszvb_GetCurrentSweep (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32* currentSweep);
ViStatus _VI_FUNC rszvb_RestartAverage (ViSession instrumentHandle,
                                        ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetPartialMeasurementResolutionBandwidthMode
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 bandwidthMode);
ViStatus _VI_FUNC rszvb_GetPartialMeasurementResolutionBandwidthMode
             (ViSession instrumentHandle, ViInt32 channel, ViInt32* bandwidthMode);
ViStatus _VI_FUNC rszvb_SetGeneratorPortResolutionBandwidth
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 generatorPort,
              ViReal64 resolutionBandwidth);
ViStatus _VI_FUNC rszvb_GetGeneratorPortResolutionBandwidth
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 generatorPort,
              ViReal64* resolutionBandwidth);
ViStatus _VI_FUNC rszvb_SetPhysicalPortResolutionBandwidth
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 analyzerPort,
              ViReal64 resolutionBandwidth);
ViStatus _VI_FUNC rszvb_GetPhysicalPortResolutionBandwidth
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 analyzerPort,
              ViReal64* resolutionBandwidth);
ViStatus _VI_FUNC rszvb_SetSweepType (ViSession instrumentHandle, ViInt32 channel,
                                      ViInt32 sweepType);
ViStatus _VI_FUNC rszvb_GetSweepType (ViSession instrumentHandle, ViInt32 channel,
                                      ViInt32* sweepType);
ViStatus _VI_FUNC rszvb_InsertNewSegment (ViSession instrumentHandle,
                                          ViInt32 channel, ViInt32 segment,
                                          ViReal64 startFrequency,
                                          ViReal64 stopFrequency,
                                          ViInt32 numberOfPoints, ViReal64 power,
                                          ViInt32 sweepTimeSelect, ViReal64 time,
                                          ViReal64 pointDelay,
                                          ViReal64 measBandwidth);
ViStatus _VI_FUNC rszvb_RedefineSegment (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 segment,
                                         ViReal64 startFrequency,
                                         ViReal64 stopFrequency,
                                         ViInt32 numberOfPoints, ViReal64 power,
                                         ViInt32 sweepTimeSelect, ViReal64 time,
                                         ViReal64 pointDelay,
                                         ViReal64 measBandwidth);
ViStatus _VI_FUNC rszvb_AddNewSegment (ViSession instrumentHandle, ViInt32 channel,
                                       ViInt32 segment);
ViStatus _VI_FUNC rszvb_DeleteSelectedSegment (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 segment);
ViStatus _VI_FUNC rszvb_DeleteAllSegments (ViSession instrumentHandle,
                                           ViInt32 channel);
ViStatus _VI_FUNC rszvb_GetSweepSegmentsCount (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32* count);
ViStatus _VI_FUNC rszvb_SetSweepSegmentState (ViSession instrumentHandle,
                                              ViInt32 channel, ViInt32 segment,
                                              ViBoolean state);
ViStatus _VI_FUNC rszvb_GetSweepSegmentState (ViSession instrumentHandle,
                                              ViInt32 channel, ViInt32 segment,
                                              ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetSweepSegmentStartFrequency (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 segment,
                                                       ViReal64 startFrequency);
ViStatus _VI_FUNC rszvb_GetSweepSegmentStartFrequency (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 segment,
                                                       ViReal64* startFrequency);
ViStatus _VI_FUNC rszvb_SetSweepSegmentStopFrequency (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 segment,
                                                      ViReal64 stopFrequency);
ViStatus _VI_FUNC rszvb_GetSweepSegmentStopFrequency (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 segment,
                                                      ViReal64* stopFrequency);
ViStatus _VI_FUNC rszvb_SetSweepSegmentNumberOfPoints (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 segment,
                                                       ViInt32 numberOfPoints);
ViStatus _VI_FUNC rszvb_GetSweepSegmentNumberOfPoints (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 segment,
                                                       ViInt32* numberOfPoints);
ViStatus _VI_FUNC rszvb_SetSweepSegmentName (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 segment,
                                             ViString name);
ViStatus _VI_FUNC rszvb_GetSweepSegmentName (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 segment,
                                             ViInt32 bufferSize,
                                             ViChar _VI_FAR name[]);
ViStatus _VI_FUNC rszvb_SetSweepSegmentPower (ViSession instrumentHandle,
                                              ViInt32 channel, ViInt32 segment,
                                              ViReal64 power);
ViStatus _VI_FUNC rszvb_GetSweepSegmentPower (ViSession instrumentHandle,
                                              ViInt32 channel, ViInt32 segment,
                                              ViReal64* power);
ViStatus _VI_FUNC rszvb_SetSweepSegmentIndependentPower (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 segment,
                                                         ViBoolean power);
ViStatus _VI_FUNC rszvb_GetSweepSegmentIndependentPower (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 segment,
                                                         ViBoolean* power);
ViStatus _VI_FUNC rszvb_SetSweepSegmentMeasBandwidth (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 segment,
                                                      ViReal64 measBandwidth);
ViStatus _VI_FUNC rszvb_GetSweepSegmentMeasBandwidth (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 segment,
                                                      ViReal64* measBandwidth);
ViStatus _VI_FUNC rszvb_SetSweepSegmentIndependentBandwidth
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 segment,
              ViBoolean measBandwidth);
ViStatus _VI_FUNC rszvb_GetSweepSegmentIndependentBandwidth
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 segment,
              ViBoolean* measBandwidth);
ViStatus _VI_FUNC rszvb_SetSweepSegmentSpurAvoid (ViSession instrumentHandle,
                                                  ViInt32 channel, ViInt32 segment,
                                                  ViInt32 spurAvoid);
ViStatus _VI_FUNC rszvb_GetSweepSegmentSpurAvoid (ViSession instrumentHandle,
                                                  ViInt32 channel, ViInt32 segment,
                                                  ViInt32* spurAvoid);
ViStatus _VI_FUNC rszvb_SetSweepSegmentIndependentSpurAvoid
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 segment,
              ViBoolean spurAvoid);
ViStatus _VI_FUNC rszvb_GetSweepSegmentIndependentSpurAvoid
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 segment,
              ViBoolean* spurAvoid);
ViStatus _VI_FUNC rszvb_SetSweepSegmentSelectivity (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 segment,
                                                    ViInt32 selectivity);
ViStatus _VI_FUNC rszvb_GetSweepSegmentSelectivity (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 segment,
                                                    ViInt32* selectivity);
ViStatus _VI_FUNC rszvb_SetSweepSegmentIndependentSelectivity
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 segment,
              ViBoolean selectivity);
ViStatus _VI_FUNC rszvb_GetSweepSegmentIndependentSelectivity
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 segment,
              ViBoolean* selectivity);
ViStatus _VI_FUNC rszvb_SetSweepSegmentSweepTime (ViSession instrumentHandle,
                                                  ViInt32 channel, ViInt32 segment,
                                                  ViReal64 time);
ViStatus _VI_FUNC rszvb_GetSweepSegmentSweepTime (ViSession instrumentHandle,
                                                  ViInt32 channel, ViInt32 segment,
                                                  ViReal64* time);
ViStatus _VI_FUNC rszvb_SetSweepSegmentIndependentTime (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 segment,
                                                        ViBoolean time);
ViStatus _VI_FUNC rszvb_GetSweepSegmentIndependentTime (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 segment,
                                                        ViBoolean* time);
ViStatus _VI_FUNC rszvb_SetSweepSegmentPointDelay (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 segment,
                                                   ViReal64 pointDelay);
ViStatus _VI_FUNC rszvb_GetSweepSegmentPointDelay (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 segment,
                                                   ViReal64* pointDelay);
ViStatus _VI_FUNC rszvb_SetSweepSegmentIndependentPointDelay
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 segment,
              ViBoolean pointDelay);
ViStatus _VI_FUNC rszvb_GetSweepSegmentIndependentPointDelay
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 segment,
              ViBoolean* pointDelay);
ViStatus _VI_FUNC rszvb_SetSweepSegmentTriggering (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 segment,
                                                   ViBoolean triggering);
ViStatus _VI_FUNC rszvb_GetSweepSegmentTriggering (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 segment,
                                                   ViBoolean* triggering);
ViStatus _VI_FUNC rszvb_SetSweepSelectiveSegmentTriggering
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean triggering);
ViStatus _VI_FUNC rszvb_GetSweepSelectiveSegmentTriggering
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean* triggering);
ViStatus _VI_FUNC rszvb_SetSweepSegmentBitsState (ViSession instrumentHandle,
                                                  ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetSweepSegmentBitsState (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetSweepSegmentBitValues (ViSession instrumentHandle,
                                                  ViInt32 channel, ViInt32 segment,
                                                  ViBoolean bit0, ViBoolean bit1,
                                                  ViBoolean bit2, ViBoolean bit3);
ViStatus _VI_FUNC rszvb_GetSweepSegmentBitValues (ViSession instrumentHandle,
                                                  ViInt32 channel, ViInt32 segment,
                                                  ViBoolean* bit0, ViBoolean* bit1,
                                                  ViBoolean* bit2, ViBoolean* bit3);
ViStatus _VI_FUNC rszvb_GetSweepSegmentCenterFrequency (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 segment,
                                                        ViReal64* centerFrequency);
ViStatus _VI_FUNC rszvb_GetSweepSegmentFrequencySpan (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 segment,
                                                      ViReal64* frequencySpan);
ViStatus _VI_FUNC rszvb_SaveSegment (ViSession instrumentHandle, ViInt32 channel,
                                     ViString fileName);
ViStatus _VI_FUNC rszvb_LoadSegment (ViSession instrumentHandle, ViInt32 channel,
                                     ViString fileName);
ViStatus _VI_FUNC rszvb_QueryOverlappingSweepSegments (ViSession instrumentHandle,
                                                       ViInt32 segment,
                                                       ViBoolean* overlapping);
ViStatus _VI_FUNC rszvb_QuerySumOfSweepSegmentsTime (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViReal64* sweepTime);
ViStatus _VI_FUNC rszvb_SetPulseTimeStart (ViSession instrumentHandle,
                                           ViInt32 channel, ViReal64 timeStart);
ViStatus _VI_FUNC rszvb_GetPulseTimeStart (ViSession instrumentHandle,
                                           ViInt32 channel, ViReal64* timeStart);
ViStatus _VI_FUNC rszvb_SetPulseTimeStop (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64 timeStop);
ViStatus _VI_FUNC rszvb_GetPulseTimeStop (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64* timeStop);
ViStatus _VI_FUNC rszvb_SetPulseTimeBandwidth (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViReal64 timeBandwidth);
ViStatus _VI_FUNC rszvb_GetPulseTimeBandwidth (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViReal64* timeBandwidth);
ViStatus _VI_FUNC rszvb_SetPulseCoupledSectionLimitLinesState
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean coupleLimits);
ViStatus _VI_FUNC rszvb_GetPulseCoupledSectionLimitLinesState
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean* coupleLimits);
ViStatus _VI_FUNC rszvb_SetPulseEvaluationMode (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViInt32 receiverType,
                                                ViInt32 recordNumber,
                                                ViInt32 interfaceType,
                                                ViInt32 generatorPortNumber,
                                                ViInt32 evaluationMode);
ViStatus _VI_FUNC rszvb_GetPulseEvaluationMode (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViInt32 receiverType,
                                                ViInt32 recordNumber,
                                                ViInt32 interfaceType,
                                                ViInt32 generatorPortNumber,
                                                ViInt32* evaluationMode);
ViStatus _VI_FUNC rszvb_SetPulseEvaluationSectionStart (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 receiverType,
                                                        ViInt32 recordNumber,
                                                        ViInt32 interfaceType,
                                                        ViInt32 generatorPortNumber,
                                                        ViReal64 evaluationStartTime);
ViStatus _VI_FUNC rszvb_GetPulseEvaluationSectionStart (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 receiverType,
                                                        ViInt32 recordNumber,
                                                        ViInt32 interfaceType,
                                                        ViInt32 generatorPortNumber,
                                                        ViReal64* evaluationStartTime);
ViStatus _VI_FUNC rszvb_SetPulseEvaluationSectionStop (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 receiverType,
                                                       ViInt32 recordNumber,
                                                       ViInt32 interfaceType,
                                                       ViInt32 generatorPortNumber,
                                                       ViReal64 evaluationStopTime);
ViStatus _VI_FUNC rszvb_GetPulseEvaluationSectionStop (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 receiverType,
                                                       ViInt32 recordNumber,
                                                       ViInt32 interfaceType,
                                                       ViInt32 generatorPortNumber,
                                                       ViReal64* evaluationStopTime);
ViStatus _VI_FUNC rszvb_SetPulseSectionLimitLinesState (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 receiverType,
                                                        ViInt32 recordNumber,
                                                        ViInt32 interfaceType,
                                                        ViInt32 generatorPortNumber,
                                                        ViBoolean limitLinesState);
ViStatus _VI_FUNC rszvb_GetPulseSectionLimitLinesState (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 receiverType,
                                                        ViInt32 recordNumber,
                                                        ViInt32 interfaceType,
                                                        ViInt32 generatorPortNumber,
                                                        ViBoolean* limitLinesState);
ViStatus _VI_FUNC rszvb_SetPulseShiftStimulus (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViInt32 receiverType,
                                               ViInt32 recordNumber,
                                               ViInt32 interfaceType,
                                               ViInt32 generatorPortNumber,
                                               ViReal64 shiftStimulus);
ViStatus _VI_FUNC rszvb_GetPulseShiftStimulus (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViInt32 receiverType,
                                               ViInt32 recordNumber,
                                               ViInt32 interfaceType,
                                               ViInt32 generatorPortNumber,
                                               ViReal64* shiftStimulus);
ViStatus _VI_FUNC rszvb_ReadTimeSamplesData (ViSession instrumentHandle,
                                             ViInt32 channel_Trace,
                                             ViInt32* noOfValues,
                                             ViReal64 _VI_FAR traceData[]);
ViStatus _VI_FUNC rszvb_SetSweepNumberOfPoints (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViInt32 numberOfPoints);
ViStatus _VI_FUNC rszvb_GetSweepNumberOfPoints (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViInt32* numberOfPoints);
ViStatus _VI_FUNC rszvb_SetFrequencyStepSize (ViSession instrumentHandle,
                                              ViInt32 channel, ViReal64 stepSize);
ViStatus _VI_FUNC rszvb_GetFrequencyStepSize (ViSession instrumentHandle,
                                              ViInt32 channel, ViReal64* stepSize);
ViStatus _VI_FUNC rszvb_SetSweepCount (ViSession instrumentHandle, ViInt32 channel,
                                       ViInt32 sweepCount);
ViStatus _VI_FUNC rszvb_GetSweepCount (ViSession instrumentHandle, ViInt32 channel,
                                       ViInt32* sweepCount);
ViStatus _VI_FUNC rszvb_ConfigureSweepTime (ViSession instrumentHandle,
                                            ViInt32 channel,
                                            ViBoolean autoSweepTime,
                                            ViReal64 sweepTime, ViReal64 measDelay);
ViStatus _VI_FUNC rszvb_SetSweepTime (ViSession instrumentHandle, ViInt32 channel,
                                      ViReal64 sweepTime);
ViStatus _VI_FUNC rszvb_GetSweepTime (ViSession instrumentHandle, ViInt32 channel,
                                      ViReal64* sweepTime);
ViStatus _VI_FUNC rszvb_SetSweepMeasDelay (ViSession instrumentHandle,
                                           ViInt32 channel, ViReal64 measDelay);
ViStatus _VI_FUNC rszvb_GetSweepMeasDelay (ViSession instrumentHandle,
                                           ViInt32 channel, ViReal64* measDelay);
ViStatus _VI_FUNC rszvb_SetSweepTimeAuto (ViSession instrumentHandle,
                                          ViInt32 channel, ViBoolean autoSweepTime);
ViStatus _VI_FUNC rszvb_GetSweepTimeAuto (ViSession instrumentHandle,
                                          ViInt32 channel,
                                          ViBoolean* autoSweepTime);
ViStatus _VI_FUNC rszvb_ConfigureTriggerFreeRun (ViSession instrumentHandle,
                                                 ViInt32 channel);
ViStatus _VI_FUNC rszvb_ConfigureTriggerExternal (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViInt32 triggerOn);
ViStatus _VI_FUNC rszvb_ConfigureTriggerPeriodic (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViReal64 triggerPeriod);
ViStatus _VI_FUNC rszvb_ConfigureTriggerRFPower (ViSession instrumentHandle,
                                                 ViInt32 channel);
ViStatus _VI_FUNC rszvb_ConfigureTriggerManual (ViSession instrumentHandle,
                                                ViInt32 channel);
ViStatus _VI_FUNC rszvb_ConfigureTriggerSettings (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViInt32 triggerMeasSequence,
                                                  ViReal64 triggerDelay);
ViStatus _VI_FUNC rszvb_SetTriggerSource (ViSession instrumentHandle,
                                          ViInt32 channel, ViInt32 triggerSource);
ViStatus _VI_FUNC rszvb_GetTriggerSource (ViSession instrumentHandle,
                                          ViInt32 channel, ViInt32* triggerSource);
ViStatus _VI_FUNC rszvb_SetTriggerDelay (ViSession instrumentHandle,
                                         ViInt32 channel, ViReal64 triggerDelay);
ViStatus _VI_FUNC rszvb_GetTriggerDelay (ViSession instrumentHandle,
                                         ViInt32 channel, ViReal64* triggerDelay);
ViStatus _VI_FUNC rszvb_SetPartialMeasurementTriggerMode (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 triggerMode);
ViStatus _VI_FUNC rszvb_GetPartialMeasurementTriggerMode (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32* triggerMode);
ViStatus _VI_FUNC rszvb_SetGeneratorPortTriggerDelay (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 generatorPort,
                                                      ViReal64 triggerDelay);
ViStatus _VI_FUNC rszvb_GetGeneratorPortTriggerDelay (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 generatorPort,
                                                      ViReal64* triggerDelay);
ViStatus _VI_FUNC rszvb_SetPhysicalPortTriggerDelay (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 analyzerPort,
                                                     ViReal64 triggerDelay);
ViStatus _VI_FUNC rszvb_GetPhysicalPortTriggerDelay (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 analyzerPort,
                                                     ViReal64* triggerDelay);
ViStatus _VI_FUNC rszvb_SetTriggeredMeasSequence (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViInt32 triggerMeasSequence);
ViStatus _VI_FUNC rszvb_GetTriggeredMeasSequence (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViInt32* triggerMeasSequence);
ViStatus _VI_FUNC rszvb_SetTriggerOn (ViSession instrumentHandle, ViInt32 channel,
                                      ViInt32 triggerOn);
ViStatus _VI_FUNC rszvb_GetTriggerOn (ViSession instrumentHandle, ViInt32 channel,
                                      ViInt32* triggerOn);
ViStatus _VI_FUNC rszvb_SetTriggerPeriod (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64 triggerPeriod);
ViStatus _VI_FUNC rszvb_GetTriggerPeriod (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64* triggerPeriod);
ViStatus _VI_FUNC rszvb_SendTrigger (ViSession instrumentHandle);
ViStatus _VI_FUNC rszvb_SendTriggerWaitOPC (ViSession instrumentHandle,
                                            ViInt32 timeout);
ViStatus _VI_FUNC rszvb_SendChannelTrigger (ViSession instrumentHandle,
                                            ViInt32 channel);
ViStatus _VI_FUNC rszvb_SendChannelTriggerWaitOPC (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViInt32 timeout);
ViStatus _VI_FUNC rszvb_SetSweepSingleAllChans (ViSession instrumentHandle,
                                                ViInt32 singleSweep);
ViStatus _VI_FUNC rszvb_GetSweepSingleAllChans (ViSession instrumentHandle,
                                                ViInt32* singleSweep);
ViStatus _VI_FUNC rszvb_SweepRestart (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetSweepSingle (ViSession instrumentHandle, ViInt32 channel,
                                        ViInt32 singleSweep);
ViStatus _VI_FUNC rszvb_GetSweepSingle (ViSession instrumentHandle, ViInt32 channel,
                                        ViInt32* singleSweep);
ViStatus _VI_FUNC rszvb_DefineGroupOfMeasuredPorts (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 group,
                                                    ViInt32 firstPort,
                                                    ViInt32 lastPort);
ViStatus _VI_FUNC rszvb_GetGroupOfMeasuredPorts (ViSession instrumentHandle,
                                                 ViInt32 channel, ViInt32 group,
                                                 ViInt32* firstPort,
                                                 ViInt32* lastPort);
ViStatus _VI_FUNC rszvb_DefineGroupOfAllMeasuredPorts (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 group,
                                                       ViInt32 numberOfPortsInGroup,
                                                       ViInt32 _VI_FAR ports[]);
ViStatus _VI_FUNC rszvb_GetGroupOfAllMeasuredPorts (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 group,
                                                    ViInt32* numberOfPortsInGroup,
                                                    ViInt32 _VI_FAR ports[]);
ViStatus _VI_FUNC rszvb_GetPortGroupsCount (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32* portGroups);
ViStatus _VI_FUNC rszvb_DeleteGroupOfMeasuredPorts (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 group);
ViStatus _VI_FUNC rszvb_DeleteAllGroupsOfMeasuredPorts (ViSession instrumentHandle,
                                                        ViInt32 channel);
ViStatus _VI_FUNC rszvb_DefineBalancedPort (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 logicalPort,
                                            ViInt32 physicalPort1,
                                            ViInt32 physicalPort2);
ViStatus _VI_FUNC rszvb_GetBalancedPort (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 logicalPort,
                                         ViInt32* physicalPort1,
                                         ViInt32* physicalPort2);
ViStatus _VI_FUNC rszvb_DeleteBalancedPort (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 logicalPort);
ViStatus _VI_FUNC rszvb_DeleteAllBalancedPorts (ViSession instrumentHandle,
                                                ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetDifferentialModeImpedance (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 logicalPort,
                                                      ViReal64 impedance);
ViStatus _VI_FUNC rszvb_GetDifferentialModeImpedance (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 logicalPort,
                                                      ViReal64* impedance);
ViStatus _VI_FUNC rszvb_SetCommonModeImpedance (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViInt32 logicalPort,
                                                ViReal64 impedance);
ViStatus _VI_FUNC rszvb_GetCommonModeImpedance (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViInt32 logicalPort,
                                                ViReal64* impedance);
ViStatus _VI_FUNC rszvb_DefinePortPair (ViSession instrumentHandle, ViInt32 channel,
                                        ViInt32 functionType, ViInt32 portPair,
                                        ViInt32 port1, ViInt32 port2);
ViStatus _VI_FUNC rszvb_DeletePortPair (ViSession instrumentHandle, ViInt32 channel,
                                        ViInt32 functionType, ViInt32 portPair);
ViStatus _VI_FUNC rszvb_SetDefaultConfigurationState (ViSession instrumentHandle,
                                                      ViBoolean defaultSettings);
ViStatus _VI_FUNC rszvb_GetDefaultConfigurationState (ViSession instrumentHandle,
                                                      ViBoolean* defaultSettings);
ViStatus _VI_FUNC rszvb_SetPortConfigration (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 portGroupA,
                                             ViInt32 portGroupB, ViInt32 portGroupC,
                                             ViInt32 portGroupD);
ViStatus _VI_FUNC rszvb_GetPortConfigration (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32* portGroupA,
                                             ViInt32* portGroupB,
                                             ViInt32* portGroupC,
                                             ViInt32* portGroupD);
ViStatus _VI_FUNC rszvb_SetConverterPowerOffset (ViSession instrumentHandle,
                                                 ViInt32 channel, ViInt32 port,
                                                 ViReal64 portPowerOffset,
                                                 ViInt32 offsetParameter);
ViStatus _VI_FUNC rszvb_GetConverterPowerOffset (ViSession instrumentHandle,
                                                 ViInt32 channel, ViInt32 port,
                                                 ViReal64* portPowerOffset,
                                                 ViInt32* offsetParameter);
ViStatus _VI_FUNC rszvb_SetConverterCalPowerOffset (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 converter,
                                                    ViReal64 calPowerOffset);
ViStatus _VI_FUNC rszvb_GetConverterCalPowerOffset (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 converter,
                                                    ViReal64* calPowerOffset);
ViStatus _VI_FUNC rszvb_SetAdvancedPowerTransferModelFrequencyState
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetAdvancedPowerTransferModelFrequencyState
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetSenseTypeOfPortTransferModel (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 port,
                                                         ViInt32 modelType);
ViStatus _VI_FUNC rszvb_GetSenseTypeOfPortTransferModel (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 port,
                                                         ViInt32* modelType);
ViStatus _VI_FUNC rszvb_SetSenseTypeOfAdvancedPowerTransferModel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 modelType);
ViStatus _VI_FUNC rszvb_GetSenseTypeOfAdvancedPowerTransferModel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32* modelType);
ViStatus _VI_FUNC rszvb_SetConverterDataSetType (ViSession instrumentHandle,
                                                 ViInt32 port, ViInt32 dataSetType);
ViStatus _VI_FUNC rszvb_GetConverterDataSetType (ViSession instrumentHandle,
                                                 ViInt32 port,
                                                 ViInt32* dataSetType);
ViStatus _VI_FUNC rszvb_SetConverterUserDataSetDirectory (ViSession instrumentHandle,
                                                          ViInt32 port,
                                                          ViString directory);
ViStatus _VI_FUNC rszvb_GetConverterUserDataSetDirectory (ViSession instrumentHandle,
                                                          ViInt32 port,
                                                          ViInt32 bufferSize,
                                                          ViChar _VI_FAR directory[]);
ViStatus _VI_FUNC rszvb_SetConverterPortAssignment (ViSession instrumentHandle,
                                                    ViInt32 port,
                                                    ViString serialNumber);
ViStatus _VI_FUNC rszvb_GetConverterPortAssignment (ViSession instrumentHandle,
                                                    ViInt32 port,
                                                    ViInt32 bufferSize,
                                                    ViChar _VI_FAR serialNumber[]);
ViStatus _VI_FUNC rszvb_SetPortTransferModelState (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 port,
                                                   ViBoolean state);
ViStatus _VI_FUNC rszvb_GetPortTransferModelState (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 port,
                                                   ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetPortWaveguideAttenuator (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 port,
                                                    ViInt32 waveguideAttenuator,
                                                    ViReal64 attenuation);
ViStatus _VI_FUNC rszvb_GetPortWaveguideAttenuatorType (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 port,
                                                        ViInt32* waveguideAttenuator);
ViStatus _VI_FUNC rszvb_GetPortWaveguideAttenuator (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 port,
                                                    ViInt32 waveguideAttenuator,
                                                    ViReal64* attenuation);
ViStatus _VI_FUNC rszvb_SetPortWaveguideAttenuatorSlope (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 port,
                                                         ViInt32 slope);
ViStatus _VI_FUNC rszvb_GetPortWaveguideAttenuatorSlope (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 port,
                                                         ViInt32* slope);
ViStatus _VI_FUNC rszvb_SetPortWaveguideAttenuatorOffset (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 port,
                                                          ViInt32 offset);
ViStatus _VI_FUNC rszvb_GetPortWaveguideAttenuatorOffset (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 port,
                                                          ViInt32* offset);
ViStatus _VI_FUNC rszvb_SetPortElectronicPowerTreshold (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 port,
                                                        ViReal64 threshold);
ViStatus _VI_FUNC rszvb_GetPortElectronicPowerTreshold (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 port,
                                                        ViReal64* threshold);
ViStatus _VI_FUNC rszvb_SetPortElectronicPowerReduction (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 port,
                                                         ViInt32 reduction);
ViStatus _VI_FUNC rszvb_GetPortElectronicPowerReduction (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 port,
                                                         ViInt32* reduction);
ViStatus _VI_FUNC rszvb_SetSimultaneousMeasurementOfPortsGroups
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetSimultaneousMeasurementOfPortsGroups
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetSimultaneousMeasurementFrequencyOffsetState
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetSimultaneousMeasurementFrequencyOffsetState
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetSimultaneousMeasurementMinimumFrequencyOffsetMode
             (ViSession instrumentHandle, ViInt32 channel,
              ViInt32 minimumFrequencyOffset);
ViStatus _VI_FUNC rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetMode
             (ViSession instrumentHandle, ViInt32 channel,
              ViInt32* minimumFrequencyOffset);
ViStatus 
    _VI_FUNC rszvb_SetSimultaneousMeasurementMinimumFrequencyOffsetBandwidthFactor
        (ViSession instrumentHandle, ViInt32 channel,
         ViInt32 minimumFrequencyOffset);
ViStatus 
    _VI_FUNC rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetBandwidthFactor
        (ViSession instrumentHandle, ViInt32 channel,
         ViInt32* minimumFrequencyOffset);
ViStatus 
    _VI_FUNC rszvb_SetSimultaneousMeasurementMinimumFrequencyOffsetDirect
        (ViSession instrumentHandle, ViInt32 channel,
         ViInt32 minimumFrequencyOffset);
ViStatus 
    _VI_FUNC rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetDirect
        (ViSession instrumentHandle, ViInt32 channel,
         ViInt32* minimumFrequencyOffset);
ViStatus 
    _VI_FUNC rszvb_GetSimultaneousMeasurementMinimumFrequencyOffsetOperatingMode
        (ViSession instrumentHandle, ViInt32 channel, ViInt32* operatingMode);
ViStatus _VI_FUNC rszvb_SetFrequencyConversion (ViSession instrumentHandle,
                                                ViInt32 measurementType,
                                                ViInt32 channel, ViInt32 port,
                                                ViInt32 numerator,
                                                ViInt32 denominator,
                                                ViReal64 offset, ViInt32 sweepType);
ViStatus _VI_FUNC rszvb_GetFrequencyConversion (ViSession instrumentHandle,
                                                ViInt32 measurementType,
                                                ViInt32 channel, ViInt32 port,
                                                ViInt32* numerator,
                                                ViInt32* denominator,
                                                ViReal64* offset,
                                                ViInt32* sweepType);
ViStatus _VI_FUNC rszvb_SetPowerMeterFrequencyConversion (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 powerMeterNumber,
                                                          ViInt32 numerator,
                                                          ViInt32 denominator,
                                                          ViReal64 offset,
                                                          ViInt32 sweepType);
ViStatus _VI_FUNC rszvb_GetPowerMeterFrequencyConversion (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 powerMeterNumber,
                                                          ViInt32* numerator,
                                                          ViInt32* denominator,
                                                          ViReal64* offset,
                                                          ViInt32* sweepType);
ViStatus _VI_FUNC rszvb_SetGeneratorFrequencyConversion (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 port,
                                                         ViInt32 generatorNumber,
                                                         ViBoolean state,
                                                         ViInt32 numerator,
                                                         ViInt32 denominator,
                                                         ViReal64 offset,
                                                         ViInt32 sweepType);
ViStatus _VI_FUNC rszvb_GetGeneratorFrequencyConversion (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 port,
                                                         ViInt32 generatorNumber,
                                                         ViBoolean* state,
                                                         ViInt32* numerator,
                                                         ViInt32* denominator,
                                                         ViReal64* offset,
                                                         ViInt32* sweepType);
ViStatus _VI_FUNC rszvb_SetConverterSourceFrequency (ViSession instrumentHandle,
                                                     ViInt32 channel, ViInt32 port,
                                                     ViInt32 numerator,
                                                     ViInt32 denominator,
                                                     ViReal64 offset,
                                                     ViInt32 sweepType);
ViStatus _VI_FUNC rszvb_GetConverterSourceFrequency (ViSession instrumentHandle,
                                                     ViInt32 channel, ViInt32 port,
                                                     ViInt32* numerator,
                                                     ViInt32* denominator,
                                                     ViReal64* offset,
                                                     ViInt32* sweepType);
ViStatus _VI_FUNC rszvb_SetMeasureAWavesState (ViSession instrumentHandle,
                                               ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetMeasureAWavesState (ViSession instrumentHandle,
                                               ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetLocalOscilatorAState (ViSession instrumentHandle,
                                                 ViInt32 channel, ViInt32 port,
                                                 ViBoolean state);
ViStatus _VI_FUNC rszvb_GetLocalOscilatorAState (ViSession instrumentHandle,
                                                 ViInt32 channel, ViInt32 port,
                                                 ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetLocalOscilatorBState (ViSession instrumentHandle,
                                                 ViInt32 channel, ViInt32 port,
                                                 ViBoolean state);
ViStatus _VI_FUNC rszvb_GetLocalOscilatorBState (ViSession instrumentHandle,
                                                 ViInt32 channel, ViInt32 port,
                                                 ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetLogicalPortCommonRefImpedance (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 port,
                                                          ViReal64 real,
                                                          ViReal64 imaginary);
ViStatus _VI_FUNC rszvb_GetLogicalPortCommonRefImpedance (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 port,
                                                          ViReal64* real,
                                                          ViReal64* imaginary);
ViStatus _VI_FUNC rszvb_SetLogicalPortDifferentialRefImpedance
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 port,
              ViReal64 real, ViReal64 imaginary);
ViStatus _VI_FUNC rszvb_GetLogicalPortDifferentialRefImpedance
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 port,
              ViReal64* real, ViReal64* imaginary);
ViStatus _VI_FUNC rszvb_SetPortImpedancesRenormalization (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 theory);
ViStatus _VI_FUNC rszvb_GetPortImpedancesRenormalization (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32* theory);
ViStatus _VI_FUNC rszvb_SetPhysicalPortRefImpedance (ViSession instrumentHandle,
                                                     ViInt32 channel, ViInt32 port,
                                                     ViReal64 real,
                                                     ViReal64 imaginary);
ViStatus _VI_FUNC rszvb_GetPhysicalPortRefImpedance (ViSession instrumentHandle,
                                                     ViInt32 channel, ViInt32 port,
                                                     ViReal64* real,
                                                     ViReal64* imaginary);
ViStatus _VI_FUNC rszvb_SetIFGain (ViSession instrumentHandle, ViInt32 channel,
                                   ViInt32 port, ViInt32 IFGain);
ViStatus _VI_FUNC rszvb_GetIFGain (ViSession instrumentHandle, ViInt32 channel,
                                   ViInt32 port, ViInt32* IFGain);
ViStatus _VI_FUNC rszvb_SetIFGainReferenceChannel (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 port,
                                                   ViInt32 IFGain);
ViStatus _VI_FUNC rszvb_GetIFGainReferenceChannel (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 port,
                                                   ViInt32* IFGain);
ViStatus _VI_FUNC rszvb_SetRFSignalSourceState (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViBoolean state);
ViStatus _VI_FUNC rszvb_GetRFSignalSourceState (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetPermanentSignalSourceState (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 port,
                                                       ViBoolean state);
ViStatus _VI_FUNC rszvb_GetPermanentSignalSourceState (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 port,
                                                       ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetPermanentSignalGeneratorState (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 port,
                                                          ViInt32 generatorNumber,
                                                          ViBoolean state);
ViStatus _VI_FUNC rszvb_GetPermanentSignalGeneratorState (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 port,
                                                          ViInt32 generatorNumber,
                                                          ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetPortPowerGeneratorOffset (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 portNumber,
                                                     ViInt32 generatorNumber,
                                                     ViReal64 portPowerOffset,
                                                     ViInt32 offsetParameter);
ViStatus _VI_FUNC rszvb_GetPortPowerGeneratorOffset (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 portNumber,
                                                     ViInt32 generatorNumber,
                                                     ViReal64* portPowerOffset,
                                                     ViInt32* offsetParameter);
ViStatus _VI_FUNC rszvb_SetSlope (ViSession instrumentHandle, ViInt32 channel,
                                  ViInt32 port, ViReal64 slope);
ViStatus _VI_FUNC rszvb_GetSlope (ViSession instrumentHandle, ViInt32 channel,
                                  ViInt32 port, ViReal64* slope);
ViStatus _VI_FUNC rszvb_SetSourceCombinerState (ViSession instrumentHandle,
                                                ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetSourceCombinerState (ViSession instrumentHandle,
                                                ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetFrequencyStimulus (ViSession instrumentHandle,
                                              ViInt32 channel,
                                              ViString frequencyStimulus);
ViStatus _VI_FUNC rszvb_GetFrequencyStimulus (ViSession instrumentHandle,
                                              ViInt32 channel,
                                              ViChar _VI_FAR frequencyStimulus[]);
ViStatus _VI_FUNC rszvb_SetPowerStimulus (ViSession instrumentHandle,
                                          ViInt32 channel, ViString powerStimulus);
ViStatus _VI_FUNC rszvb_GetPowerStimulus (ViSession instrumentHandle,
                                          ViInt32 channel,
                                          ViChar _VI_FAR powerStimulus[]);
ViStatus _VI_FUNC rszvb_SetTDIFState (ViSession instrumentHandle, ViInt32 channel,
                                      ViBoolean trueDifferentialModeState);
ViStatus _VI_FUNC rszvb_GetTDIFState (ViSession instrumentHandle, ViInt32 channel,
                                      ViBoolean* trueDifferentialModeState);
ViStatus _VI_FUNC rszvb_SetTDIFAmplitudeImbalanceLogicalPort
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 port);
ViStatus _VI_FUNC rszvb_GetTDIFAmplitudeImbalanceLogicalPort
             (ViSession instrumentHandle, ViInt32 channel, ViInt32* port);
ViStatus _VI_FUNC rszvb_SetTDIFAmplitudeImbalanceStartPower
             (ViSession instrumentHandle, ViInt32 channel, ViReal64 startPower);
ViStatus _VI_FUNC rszvb_GetTDIFAmplitudeImbalanceStartPower
             (ViSession instrumentHandle, ViInt32 channel, ViReal64* startPower);
ViStatus _VI_FUNC rszvb_SetTDIFAmplitudeImbalanceStopPower
             (ViSession instrumentHandle, ViInt32 channel, ViReal64 stopPower);
ViStatus _VI_FUNC rszvb_GetTDIFAmplitudeImbalanceStopPower
             (ViSession instrumentHandle, ViInt32 channel, ViReal64* stopPower);
ViStatus _VI_FUNC rszvb_SetTDIFPhaseImbalanceLogicalPort (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 port);
ViStatus _VI_FUNC rszvb_GetTDIFPhaseImbalanceLogicalPort (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32* port);
ViStatus _VI_FUNC rszvb_SetTDIFPhaseImbalanceStartPhase (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViReal64 startPhase);
ViStatus _VI_FUNC rszvb_GetTDIFPhaseImbalanceStartPhase (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViReal64* startPhase);
ViStatus _VI_FUNC rszvb_SetTDIFPhaseImbalanceStopPhase (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViReal64 stopPhase);
ViStatus _VI_FUNC rszvb_GetTDIFPhaseImbalanceStopPhase (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViReal64* stopPhase);
ViStatus _VI_FUNC rszvb_SetTDIFSourcePowerMode (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViInt32 sourcePowerMode);
ViStatus _VI_FUNC rszvb_GetTDIFSourcePowerMode (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViInt32* sourcePowerMode);
ViStatus _VI_FUNC rszvb_SetTDIFCompensationState (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViBoolean compensationState);
ViStatus _VI_FUNC rszvb_GetTDIFCompensationState (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViBoolean* compensationState);
ViStatus _VI_FUNC rszvb_SetTDIFReceiverFrequency (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViReal64 receiverFrequency);
ViStatus _VI_FUNC rszvb_GetTDIFReceiverFrequency (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViReal64* receiverFrequency);
ViStatus _VI_FUNC rszvb_SetPulseGeneratorState (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViBoolean pulseGeneratorState);
ViStatus _VI_FUNC rszvb_GetPulseGeneratorState (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViBoolean* pulseGeneratorState);
ViStatus _VI_FUNC rszvb_DefinePulseGenerator (ViSession instrumentHandle,
                                              ViInt32 channel, ViInt32 generator,
                                              ViInt32 pulseType,
                                              ViReal64 pulseWidth,
                                              ViReal64 singleTrainPulsePeriod,
                                              ViInt32 pulsePolarity,
                                              ViInt32 pulseMode);
ViStatus _VI_FUNC rszvb_DefinePulseTrainSegments (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViInt32 bufferSize,
                                                  ViInt32 _VI_FAR pulseTrainActive[],
                                                  ViReal64 _VI_FAR startTime[],
                                                  ViReal64 _VI_FAR stopTime[]);
ViStatus _VI_FUNC rszvb_ConfigureChoppedPulseProfile (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViBoolean choppedPulseProfileMode,
                                                      ViReal64 delayIncrement);
ViStatus _VI_FUNC rszvb_SetPulseGeneratorType (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 generator,
                                               ViInt32 pulseType);
ViStatus _VI_FUNC rszvb_GetPulseGeneratorType (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 generator,
                                               ViInt32* pulseType);
ViStatus _VI_FUNC rszvb_SetPulseGeneratorWidth (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 generator,
                                                ViReal64 pulseWidth);
ViStatus _VI_FUNC rszvb_GetPulseGeneratorWidth (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 generator,
                                                ViReal64* pulseWidth);
ViStatus _VI_FUNC rszvb_SetPulseGeneratorSinglePeriod (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViReal64 singlePulsePeriod);
ViStatus _VI_FUNC rszvb_GetPulseGeneratorSinglePeriod (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViReal64* singlePulsePeriod);
ViStatus _VI_FUNC rszvb_SetPulseGeneratorTrainPeriod (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViReal64 trainPulsePeriod);
ViStatus _VI_FUNC rszvb_GetPulseGeneratorTrainPeriod (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViReal64* trainPulsePeriod);
ViStatus _VI_FUNC rszvb_SetPulseGeneratorPolarity (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViInt32 generator,
                                                   ViInt32 pulsePolarity);
ViStatus _VI_FUNC rszvb_GetPulseGeneratorPolarity (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViInt32 generator,
                                                   ViInt32* pulsePolarity);
ViStatus _VI_FUNC rszvb_SetPulseGeneratorMode (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 pulseMode);
ViStatus _VI_FUNC rszvb_GetPulseGeneratorMode (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32* pulseMode);
ViStatus _VI_FUNC rszvb_SetPulseGeneratorMasterChannel (ViSession instrumentHandle,
                                                        ViInt32 masterChannel);
ViStatus _VI_FUNC rszvb_GetPulseGeneratorMasterChannel (ViSession instrumentHandle,
                                                        ViInt32* masterChannel);
ViStatus _VI_FUNC rszvb_GetPulseTrainSegments (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 bufferSize,
                                               ViInt32 _VI_FAR pulseTrainActive[],
                                               ViReal64 _VI_FAR startTime[],
                                               ViReal64 _VI_FAR stopTime[]);
ViStatus _VI_FUNC rszvb_SetPulseTrainSegmentState (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 segment,
                                                   ViBoolean segmentState);
ViStatus _VI_FUNC rszvb_GetPulseTrainSegmentState (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 segment,
                                                   ViBoolean* segmentState);
ViStatus _VI_FUNC rszvb_SetPulseTrainSegmentStart (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 segment,
                                                   ViReal64 segmentStart);
ViStatus _VI_FUNC rszvb_GetPulseTrainSegmentStart (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 segment,
                                                   ViReal64* segmentStart);
ViStatus _VI_FUNC rszvb_SetPulseTrainSegmentStop (ViSession instrumentHandle,
                                                  ViInt32 channel, ViInt32 segment,
                                                  ViReal64 segmentStop);
ViStatus _VI_FUNC rszvb_GetPulseTrainSegmentStop (ViSession instrumentHandle,
                                                  ViInt32 channel, ViInt32 segment,
                                                  ViReal64* segmentStop);
ViStatus _VI_FUNC rszvb_GetPulseTrainSegmentCount (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViInt32* segmentCount);
ViStatus _VI_FUNC rszvb_DeleteAllPulseTrainSegments (ViSession instrumentHandle,
                                                     ViInt32 channel);
ViStatus _VI_FUNC rszvb_SavePulseTrainFile (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 generator,
                                            ViString fileName);
ViStatus _VI_FUNC rszvb_LoadPulseTrainFile (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 generator,
                                            ViString fileName);
ViStatus _VI_FUNC rszvb_SetPulseGeneratorDelay (ViSession instrumentHandle,
                                                ViInt32 channel, ViReal64 delay);
ViStatus _VI_FUNC rszvb_GetPulseGeneratorDelay (ViSession instrumentHandle,
                                                ViInt32 channel, ViReal64* delay);
ViStatus _VI_FUNC rszvb_SetChoppedPulseProfileMode (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean choppedPulseProfileMode);
ViStatus _VI_FUNC rszvb_GetChoppedPulseProfileMode (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean* choppedPulseProfileMode);
ViStatus _VI_FUNC rszvb_SetChoppedPulseProfileDelayIncrement
             (ViSession instrumentHandle, ViInt32 channel, ViReal64 delayIncrement);
ViStatus _VI_FUNC rszvb_GetChoppedPulseProfileDelayIncrement
             (ViSession instrumentHandle, ViInt32 channel,
              ViReal64* delayIncrement);
ViStatus _VI_FUNC rszvb_ConfigureZVAXPath (ViSession instrumentHandle,
                                           ViInt32 channel, ViInt32 path,
                                           ViBoolean internalCombiner,
                                           ViBoolean harmonicFilter,
                                           ViBoolean pulseModulator);
ViStatus _VI_FUNC rszvb_ConfigurePulseGenerators (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViBoolean extSignalGeneratorInput,
                                                  ViBoolean extSignalGeneratorOutput,
                                                  ViInt32 assignment);
ViStatus _VI_FUNC rszvb_SetInternalCombiner (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViBoolean internalCombiner);
ViStatus _VI_FUNC rszvb_GetInternalCombiner (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViBoolean* internalCombiner);
ViStatus _VI_FUNC rszvb_SetHarmonicFilter (ViSession instrumentHandle,
                                           ViInt32 channel, ViInt32 path,
                                           ViBoolean harmonicFilter);
ViStatus _VI_FUNC rszvb_GetHarmonicFilter (ViSession instrumentHandle,
                                           ViInt32 channel, ViInt32 path,
                                           ViBoolean* harmonicFilter);
ViStatus _VI_FUNC rszvb_SetLNPreamplifier (ViSession instrumentHandle,
                                           ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetLNPreamplifier (ViSession instrumentHandle,
                                           ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetPulseModulator (ViSession instrumentHandle,
                                           ViInt32 channel, ViInt32 path,
                                           ViBoolean pulseModulator);
ViStatus _VI_FUNC rszvb_GetPulseModulator (ViSession instrumentHandle,
                                           ViInt32 channel, ViInt32 path,
                                           ViBoolean* pulseModulator);
ViStatus _VI_FUNC rszvb_SetExternalSignalGeneratorInput (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViBoolean extSignalGeneratorInput);
ViStatus _VI_FUNC rszvb_GetExternalSignalGeneratorInput (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViBoolean* extSignalGeneratorInput);
ViStatus _VI_FUNC rszvb_SetPulseGeneratorAssignment (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 assignment);
ViStatus _VI_FUNC rszvb_GetPulseGeneratorAssignment (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32* assignment);
ViStatus _VI_FUNC rszvb_SetExternalSignalGeneratorOutput (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViBoolean extSignalGeneratorOutput);
ViStatus _VI_FUNC rszvb_GetExternalSignalGeneratorOutput (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViBoolean* extSignalGeneratorOutput);
ViStatus _VI_FUNC rszvb_SetTRMMeasureInput (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 path,
                                            ViInt32 input);
ViStatus _VI_FUNC rszvb_GetTRMMeasureInput (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 path,
                                            ViInt32* input);
ViStatus _VI_FUNC rszvb_SetTRMCombinerState (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 path,
                                             ViBoolean combinerState);
ViStatus _VI_FUNC rszvb_GetTRMCombinerState (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 path,
                                             ViBoolean* combinerState);
ViStatus _VI_FUNC rszvb_SetTRMPowerAmplifierState (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 path,
                                                   ViBoolean powerAmplifierState);
ViStatus _VI_FUNC rszvb_GetTRMPowerAmplifierState (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 path,
                                                   ViBoolean* powerAmplifierState);
ViStatus _VI_FUNC rszvb_SetTRMPulseModulatorState (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 path,
                                                   ViBoolean pulseModulatorState);
ViStatus _VI_FUNC rszvb_GetTRMPulseModulatorState (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 path,
                                                   ViBoolean* pulseModulatorState);
ViStatus _VI_FUNC rszvb_SetTRMUserSourcePathExtensionState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 path,
              ViBoolean userSourcePathExtension);
ViStatus _VI_FUNC rszvb_GetTRMUserSourcePathExtensionState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 path,
              ViBoolean* userSourcePathExtension);
ViStatus _VI_FUNC rszvb_SetTRMUserMeasurementPathExtensionState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 path,
              ViBoolean userMeasurementPathExtension);
ViStatus _VI_FUNC rszvb_GetTRMUserMeasurementPathExtensionState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 path,
              ViBoolean* userMeasurementPathExtension);
ViStatus _VI_FUNC rszvb_SetTRMPulseModulatorSource (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 path,
                                                    ViInt32 pulseModulatorSource);
ViStatus _VI_FUNC rszvb_GetTRMPulseModulatorSource (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 path,
                                                    ViInt32* pulseModulatorSource);
ViStatus _VI_FUNC rszvb_SetTRMPulseGeneratorSource (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 extOut,
                                                    ViInt32 pulseGeneratorSource);
ViStatus _VI_FUNC rszvb_GetTRMPulseGeneratorSource (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 extOut,
                                                    ViInt32* pulseGeneratorSource);
ViStatus _VI_FUNC rszvb_SetTRMPulseGeneratorInvertSource (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 extOut,
                                                          ViBoolean invertSource);
ViStatus _VI_FUNC rszvb_GetTRMPulseGeneratorInvertSource (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 extOut,
                                                          ViBoolean* invertSource);
ViStatus _VI_FUNC rszvb_GetTRMNumberOfUnits (ViSession instrumentHandle,
                                             ViInt32* numberOfUnits);
ViStatus _VI_FUNC rszvb_GetTRMUnitDeviceID (ViSession instrumentHandle,
                                            ViInt32 bufferSize,
                                            ViChar _VI_FAR deviceID[]);
ViStatus _VI_FUNC rszvb_GetTRMUnitHardwareOptions (ViSession instrumentHandle,
                                                   ViInt32 bufferSize,
                                                   ViChar _VI_FAR optionList[]);
ViStatus _VI_FUNC rszvb_ConfigureHarmonicMeasurement (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 harmonicMeasurement,
                                                      ViBoolean relativeHarmonicMeasurement,
                                                      ViInt32 source,
                                                      ViInt32 harmonicMeasuredAt,
                                                      ViInt32 harmonicOrder);
ViStatus _VI_FUNC rszvb_SetHarmonicMeasurementState (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 harmonicMeasurement);
ViStatus _VI_FUNC rszvb_GetHarmonicMeasurementState (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32* harmonicMeasurement);
ViStatus _VI_FUNC rszvb_SetHarmonicOrder (ViSession instrumentHandle,
                                          ViInt32 channel, ViInt32 harmonicOrder);
ViStatus _VI_FUNC rszvb_GetHarmonicOrder (ViSession instrumentHandle,
                                          ViInt32 channel, ViInt32* harmonicOrder);
ViStatus _VI_FUNC rszvb_SetHarmonicSourcePort (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 port);
ViStatus _VI_FUNC rszvb_GetHarmonicSourcePort (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32* port);
ViStatus _VI_FUNC rszvb_SetHarmonicReceivePort (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port);
ViStatus _VI_FUNC rszvb_GetHarmonicReceivePort (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32* port);
ViStatus _VI_FUNC rszvb_SetHarmonicRelativeState (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViBoolean relativeHarmonicMeasurement);
ViStatus _VI_FUNC rszvb_GetHarmonicRelativeState (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViBoolean* relativeHarmonicMeasurement);
ViStatus _VI_FUNC rszvb_SetMixerMode (ViSession instrumentHandle, ViInt32 channel,
                                      ViInt32 mixerMode);
ViStatus _VI_FUNC rszvb_GetMixerMode (ViSession instrumentHandle, ViInt32 channel,
                                      ViInt32* mixerMode);
ViStatus _VI_FUNC rszvb_SetNumberOfStages (ViSession instrumentHandle,
                                           ViInt32 channel, ViInt32 numberOfStages);
ViStatus _VI_FUNC rszvb_GetNumberOfStages (ViSession instrumentHandle,
                                           ViInt32 channel,
                                           ViInt32* numberOfStages);
ViStatus _VI_FUNC rszvb_SetSignalSource (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 stage,
                                         ViInt32 source, ViInt32 portNumber);
ViStatus _VI_FUNC rszvb_GetSignalSource (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 stage,
                                         ViInt32* source, ViInt32* portNumber);
ViStatus _VI_FUNC rszvb_SetIFSignalPort (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 portNumber);
ViStatus _VI_FUNC rszvb_GetIFSignalPort (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32* portNumber);
ViStatus _VI_FUNC rszvb_SetRFSignalPort (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 portNumber);
ViStatus _VI_FUNC rszvb_GetRFSignalPort (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32* portNumber);
ViStatus _VI_FUNC rszvb_SetInternalSignalSource (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViInt32 internalSignalSource);
ViStatus _VI_FUNC rszvb_GetInternalSignalSource (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViInt32* internalSignalSource);
ViStatus _VI_FUNC rszvb_SetExternalSignalSource (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViInt32 externalSignalSource);
ViStatus _VI_FUNC rszvb_GetExternalSignalSource (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViInt32* externalSignalSource);
ViStatus _VI_FUNC rszvb_ConfigurePowerSettings (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViInt32 fundamentalPower,
                                                ViReal64 fixedPower);
ViStatus _VI_FUNC rszvb_SetFundamentalPowerSignal (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViInt32 fundamentalPower);
ViStatus _VI_FUNC rszvb_GetFundamentalPowerSignal (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViInt32* fundamentalPower);
ViStatus _VI_FUNC rszvb_SetFixedPower (ViSession instrumentHandle, ViInt32 channel,
                                       ViReal64 fixedPower);
ViStatus _VI_FUNC rszvb_GetFixedPower (ViSession instrumentHandle, ViInt32 channel,
                                       ViReal64* fixedPower);
ViStatus _VI_FUNC rszvb_SetFixedPowerToSignal (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 signal,
                                               ViReal64 fixedPower);
ViStatus _VI_FUNC rszvb_GetFixedPowerToSignal (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 signal,
                                               ViReal64* fixedPower);
ViStatus _VI_FUNC rszvb_SetSignalPowerMode (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 signal,
                                            ViInt32 mode);
ViStatus _VI_FUNC rszvb_GetSignalPowerMode (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 signal,
                                            ViInt32* mode);
ViStatus _VI_FUNC rszvb_ConfigureFrequencySettings (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 fundamentalFrequencySignal,
                                                    ViInt32 fixedFrequencySignal,
                                                    ViReal64 fixedFrequency,
                                                    ViInt32 frequencyConversionMode);
ViStatus _VI_FUNC rszvb_SetFundamentalFrequencySignal (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 fundamentalFrequency);
ViStatus _VI_FUNC rszvb_GetFundamentalFrequencySignal (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32* fundamentalFrequency);
ViStatus _VI_FUNC rszvb_SetFixedFrequencySignal (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViInt32 fixedFrequency);
ViStatus _VI_FUNC rszvb_GetFixedFrequencySignal (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViInt32* fixedFrequency);
ViStatus _VI_FUNC rszvb_SetFixedFrequencySignalStage2 (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 fixedFrequency);
ViStatus _VI_FUNC rszvb_GetFixedFrequencySignalStage2 (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32* fixedFrequency);
ViStatus _VI_FUNC rszvb_SetFixedFrequency (ViSession instrumentHandle,
                                           ViInt32 channel,
                                           ViReal64 fixedFrequency);
ViStatus _VI_FUNC rszvb_GetFixedFrequency (ViSession instrumentHandle,
                                           ViInt32 channel,
                                           ViReal64* fixedFrequency);
ViStatus _VI_FUNC rszvb_SetFixedFrequencyToSignal (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 signal,
                                                   ViReal64 fixedFrequency);
ViStatus _VI_FUNC rszvb_GetFixedFrequencyToSignal (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 signal,
                                                   ViReal64* fixedFrequency);
ViStatus _VI_FUNC rszvb_SetFrequencyConversionMode (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 frequencyConversionMode);
ViStatus _VI_FUNC rszvb_GetFrequencyConversionMode (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32* frequencyConversionMode);
ViStatus _VI_FUNC rszvb_SetFrequencyConversionModeStage2 (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 frequencyConversionMode);
ViStatus _VI_FUNC rszvb_GetFrequencyConversionModeStage2 (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32* frequencyConversionMode);
ViStatus _VI_FUNC rszvb_SetFrequencyHighAccuracy (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViBoolean highAccuracy);
ViStatus _VI_FUNC rszvb_GetFrequencyHighAccuracy (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViBoolean* highAccuracy);
ViStatus _VI_FUNC rszvb_SetFrequencyLOConversionFactor (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 stage,
                                                        ViInt32 numerator,
                                                        ViInt32 denominator);
ViStatus _VI_FUNC rszvb_GetFrequencyLOConversionFactor (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 stage,
                                                        ViInt32* numerator,
                                                        ViInt32* denominator);
ViStatus _VI_FUNC rszvb_SetFrequencyRFConversionFactor (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 numerator,
                                                        ViInt32 denominator);
ViStatus _VI_FUNC rszvb_GetFrequencyRFConversionFactor (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32* numerator,
                                                        ViInt32* denominator);
ViStatus _VI_FUNC rszvb_SetRFImageFrequency (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViBoolean RFImageFrequency);
ViStatus _VI_FUNC rszvb_GetRFImageFrequency (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViBoolean* RFImageFrequency);
ViStatus _VI_FUNC rszvb_SetExternalPowerMeter (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViInt32 numberOfExternalPowerMeter);
ViStatus _VI_FUNC rszvb_GetExternalPowerMeter (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViInt32* numberOfExternalPowerMeter);
ViStatus _VI_FUNC rszvb_RFSourceCalibration (ViSession instrumentHandle,
                                             ViInt32 channel);
ViStatus _VI_FUNC rszvb_IFReceiverCalibration (ViSession instrumentHandle,
                                               ViInt32 channel);
ViStatus _VI_FUNC rszvb_LOSourceCalibration (ViSession instrumentHandle,
                                             ViInt32 channel);
ViStatus _VI_FUNC rszvb_LOSourceCalibrationStage2 (ViSession instrumentHandle,
                                                   ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetMixerDelayMeasurementSetup (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 measurementSetup);
ViStatus _VI_FUNC rszvb_GetMixerDelayMeasurementSetup (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32* measurementSetup);
ViStatus _VI_FUNC rszvb_SetMixerDelayLANConnection (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 LANConnection);
ViStatus _VI_FUNC rszvb_GetMixerDelayLANConnection (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32* LANConnection);
ViStatus _VI_FUNC rszvb_DefineMixerDelayReceiver (ViSession instrumentHandle,
                                                  ViString measurementSetup);
ViStatus _VI_FUNC rszvb_ClearMixerDelayReceiverList (ViSession instrumentHandle);
ViStatus _VI_FUNC rszvb_StartMixerDelayCalibrationSweep (ViSession instrumentHandle,
                                                         ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetMixerDelayAperture (ViSession instrumentHandle,
                                               ViInt32 channel, ViReal64 aperture);
ViStatus _VI_FUNC rszvb_GetMixerDelayAperture (ViSession instrumentHandle,
                                               ViInt32 channel, ViReal64* aperture);
ViStatus _VI_FUNC rszvb_SetMixerDelayConstant (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViReal64 constantDelay);
ViStatus _VI_FUNC rszvb_GetMixerDelayConstant (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViReal64* constantDelay);
ViStatus _VI_FUNC rszvb_SetMixerDelayCombinerState (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean internalCombiner);
ViStatus _VI_FUNC rszvb_GetMixerDelayCombinerState (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean* internalCombiner);
ViStatus _VI_FUNC rszvb_SetMixerDelayDivisionByTwoEnabled
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean divisionByTwo);
ViStatus _VI_FUNC rszvb_GetMixerDelayDivisionByTwoEnabled
             (ViSession instrumentHandle, ViInt32 channel,
              ViBoolean* divisionByTwo);
ViStatus _VI_FUNC rszvb_SetMixerConstantDelayEnabled (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViBoolean constantDelay);
ViStatus _VI_FUNC rszvb_GetMixerConstantDelayEnabled (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViBoolean* constantDelay);
ViStatus _VI_FUNC rszvb_SetMixerDelayCorrection (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViBoolean correction);
ViStatus _VI_FUNC rszvb_GetMixerDelayCorrection (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViBoolean* correction);
ViStatus _VI_FUNC rszvb_SetMixerDelayUpperToneSource (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 source,
                                                      ViInt32 portNumber);
ViStatus _VI_FUNC rszvb_GetMixerDelayUpperToneSource (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32* source,
                                                      ViInt32* portNumber);
ViStatus _VI_FUNC rszvb_LoadMixerDelayValues (ViSession instrumentHandle,
                                              ViInt32 channel, ViInt32 type,
                                              ViString file);
ViStatus _VI_FUNC rszvb_LoadMixerDelayCalibrationData (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViString file);
ViStatus _VI_FUNC rszvb_StoreMixerDelayCalibrationData (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViString file);
ViStatus _VI_FUNC rszvb_SetVectorMixerMode (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 mixerMode);
ViStatus _VI_FUNC rszvb_GetVectorMixerMode (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32* mixerMode);
ViStatus _VI_FUNC rszvb_SetInternalSignalSourceAUX (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 internalSignalSource);
ViStatus _VI_FUNC rszvb_GetInternalSignalSourceAUX (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32* internalSignalSource);
ViStatus _VI_FUNC rszvb_SetExternalSignalSourceAUX (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 externalSignalSource);
ViStatus _VI_FUNC rszvb_GetExternalSignalSourceAUX (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32* externalSignalSource);
ViStatus _VI_FUNC rszvb_SetAUXMixerPort (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 portNumber);
ViStatus _VI_FUNC rszvb_GetAUXMixerPort (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32* portNumber);
ViStatus _VI_FUNC rszvb_SetAUXFixedPower (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64 fixedPower);
ViStatus _VI_FUNC rszvb_GetAUXFixedPower (ViSession instrumentHandle,
                                          ViInt32 channel, ViReal64* fixedPower);
ViStatus _VI_FUNC rszvb_AutomaticVectorMixerCalibration (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 mode,
                                                         ViBoolean dispersion,
                                                         ViInt32 mixerParameter,
                                                         ViReal64 delayPhase);
ViStatus _VI_FUNC rszvb_SetIMODLowerToneSource (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 source,
                                                ViInt32 sourceNumber);
ViStatus _VI_FUNC rszvb_GetIMODLowerToneSource (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32* source,
                                                ViInt32* sourceNumber);
ViStatus _VI_FUNC rszvb_SetIMODUpperToneSource (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 source,
                                                ViInt32 sourceNumber);
ViStatus _VI_FUNC rszvb_GetIMODUpperToneSource (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32* source,
                                                ViInt32* sourceNumber);
ViStatus _VI_FUNC rszvb_SetIMODToneDistance (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViReal64 toneDistance);
ViStatus _VI_FUNC rszvb_GetIMODToneDistance (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViReal64* toneDistance);
ViStatus _VI_FUNC rszvb_SetIMODReceiverPort (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 receiverPort);
ViStatus _VI_FUNC rszvb_GetIMODReceiverPort (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViInt32* receiverPort);
ViStatus _VI_FUNC rszvb_SetIMODMeasurementOrder (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViInt32 productOrder,
                                                 ViBoolean measurementState);
ViStatus _VI_FUNC rszvb_GetIMODMeasurementOrder (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViInt32 productOrder,
                                                 ViBoolean* measurementState);
ViStatus _VI_FUNC rszvb_SetIMODEnhancedWaveCorrection (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViBoolean state);
ViStatus _VI_FUNC rszvb_GetIMODEnhancedWaveCorrection (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetIMODInternalCombiner (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViBoolean internalCombiner);
ViStatus _VI_FUNC rszvb_GetIMODInternalCombiner (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViBoolean* internalCombiner);
ViStatus _VI_FUNC rszvb_SetIMODSpectrumMeasurement (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean spectrumMeasurement);
ViStatus _VI_FUNC rszvb_GetIMODSpectrumMeasurement (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean* spectrumMeasurement);
ViStatus _VI_FUNC rszvb_SetIMODMaxOrder (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 maxOrder);
ViStatus _VI_FUNC rszvb_GetIMODMaxOrder (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32* maxOrder);
ViStatus _VI_FUNC rszvb_SetIMODTwoToneOutput (ViSession instrumentHandle,
                                              ViInt32 channel,
                                              ViInt32 twoToneOutput);
ViStatus _VI_FUNC rszvb_GetIMODTwoToneOutput (ViSession instrumentHandle,
                                              ViInt32 channel,
                                              ViInt32* twoToneOutput);
ViStatus _VI_FUNC rszvb_StartIMODLowerToneSourcePowerCalibration
             (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_StartIMODUpperToneSourcePowerCalibration
             (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_StartIMODReceivePortSourcePowerCalibration
             (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_StartIMODLowerUpperTonePortsSourcePowerCalibration
             (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_StartIMODReceiverPortPowerCalibration
             (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_StartIMODReceiverPowerCalibration
             (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetIMODDistortionMeasurementCalibrationState
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetIMODDistortionMeasurementCalibrationState
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_DisableIMODMeasurement (ViSession instrumentHandle,
                                                ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetNoiseFigureDetectorMeasurementTime
             (ViSession instrumentHandle, ViInt32 channel, ViReal64 detectorTime);
ViStatus _VI_FUNC rszvb_GetNoiseFigureDetectorMeasurementTime
             (ViSession instrumentHandle, ViInt32 channel, ViReal64* detectorTime);
ViStatus _VI_FUNC rszvb_SetNoiseFigureMeasurementMode (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViBoolean measurementMode);
ViStatus _VI_FUNC rszvb_GetNoiseFigureMeasurementMode (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViBoolean* measurementMode);
ViStatus _VI_FUNC rszvb_SetNoiseFigureLOOscillator (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean LOOscillator);
ViStatus _VI_FUNC rszvb_GetNoiseFigureLOOscillator (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean* LOOscillator);
ViStatus _VI_FUNC rszvb_SetNoiseFigureNarowbandDUT (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean narowbandDUT);
ViStatus _VI_FUNC rszvb_GetNoiseFigureNarowbandDUT (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean* narowbandDUT);
ViStatus _VI_FUNC rszvb_SetNoiseFigureRFImageCorrection (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViBoolean RFImageCorrection);
ViStatus _VI_FUNC rszvb_GetNoiseFigureRFImageCorrection (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViBoolean* RFImageCorrection);
ViStatus _VI_FUNC rszvb_SetNoiseFigureCalibrationState (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViBoolean calibration);
ViStatus _VI_FUNC rszvb_GetNoiseFigureCalibrationState (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViBoolean* calibration);
ViStatus _VI_FUNC rszvb_GetNoiseFigureCalibrationStateLabel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 bufferSize,
              ViChar _VI_FAR label[]);
ViStatus _VI_FUNC rszvb_DefineNoiseFigureCalibrationSettings
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 port1,
              ViInt32 port2, ViBoolean externalAttenuator,
              ViReal64 sourceNoiseCalAttenuation,
              ViReal64 DUTMeasurementAttenuation);
ViStatus _VI_FUNC rszvb_StartNoiseFigureCalibration (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 calibrationStep);
ViStatus _VI_FUNC rszvb_TerminateNoiseFigureCalibration (ViSession instrumentHandle,
                                                         ViInt32 channel);
ViStatus _VI_FUNC rszvb_CompleteNoiseFigureCalibration (ViSession instrumentHandle,
                                                        ViInt32 channel);
ViStatus _VI_FUNC rszvb_OverwriteNoiseFigureChannelSettings
             (ViSession instrumentHandle, ViInt32 channel, ViString traceName);
ViStatus _VI_FUNC rszvb_SetVirtualTransformBalancedState (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 functionType,
                                                          ViInt32 logicalPortNumber,
                                                          ViBoolean state);
ViStatus _VI_FUNC rszvb_GetVirtualTransformBalancedState (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 functionType,
                                                          ViInt32 logicalPortNumber,
                                                          ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetVirtualTransformBalancedPort (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 functionType,
                                                         ViInt32 logicalPortNumber,
                                                         ViInt32 parameterType,
                                                         ViInt32 parameterNumber,
                                                         ViInt32 circuitModel,
                                                         ViReal64 value);
ViStatus _VI_FUNC rszvb_GetVirtualTransformBalancedPort (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 functionType,
                                                         ViInt32 logicalPortNumber,
                                                         ViInt32 parameterType,
                                                         ViInt32 parameterNumber,
                                                         ViInt32 circuitModel,
                                                         ViReal64* value);
ViStatus _VI_FUNC rszvb_SetVirtualTransformBalancedCircuitModel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 logicalPortNumber, ViInt32 circuitModel);
ViStatus _VI_FUNC rszvb_GetVirtualTransformBalancedCircuitModel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 logicalPortNumber, ViInt32* circuitModel);
ViStatus _VI_FUNC rszvb_LoadBalancedPortCircuitModelData (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 functionType,
                                                          ViInt32 logicalPortNumber,
                                                          ViString fileName,
                                                          ViInt32 parameter);
ViStatus _VI_FUNC rszvb_LoadAndInterchangeBalancedPortCircuitModelData
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 logicalPortNumber, ViString fileName, ViInt32 parameter);
ViStatus _VI_FUNC rszvb_SetVirtualTransformSingleEndedState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 physicalPortNumber, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetVirtualTransformSingleEndedState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 physicalPortNumber, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetVirtualTransformSingleEndedPort
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 physicalPortNumber, ViInt32 parameterType,
              ViInt32 parameterNumber, ViInt32 circuitModel, ViReal64 value);
ViStatus _VI_FUNC rszvb_GetVirtualTransformSingleEndedPort
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 physicalPortNumber, ViInt32 parameterType,
              ViInt32 parameterNumber, ViInt32 circuitModel, ViReal64* value);
ViStatus _VI_FUNC rszvb_SetVirtualTransformSingleEndedCircuitModel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 physicalPortNumber, ViInt32 circuitModel);
ViStatus _VI_FUNC rszvb_GetVirtualTransformSingleEndedCircuitModel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 physicalPortNumber, ViInt32* circuitModel);
ViStatus _VI_FUNC rszvb_LoadSingleEndedPortCircuitModelData
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 physicalPortNumber, ViString fileName);
ViStatus _VI_FUNC rszvb_LoadAndInterchangeSingleEndedPortCircuitModelData
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 physicalPortNumber, ViString fileName);
ViStatus _VI_FUNC rszvb_SetVirtualTransformGroundLoopState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViBoolean state);
ViStatus _VI_FUNC rszvb_GetVirtualTransformGroundLoopState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetVirtualTransformGroundLoop (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 functionType,
                                                       ViInt32 parameterType,
                                                       ViInt32 circuitModel,
                                                       ViReal64 groundLoopValue);
ViStatus _VI_FUNC rszvb_GetVirtualTransformGroundLoop (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 functionType,
                                                       ViInt32 parameterType,
                                                       ViInt32 circuitModel,
                                                       ViReal64* groundLoopValue);
ViStatus _VI_FUNC rszvb_SetVirtualTransformGroundLoopCircuitModel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 circuitModel);
ViStatus _VI_FUNC rszvb_GetVirtualTransformGroundLoopCircuitModel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32* circuitModel);
ViStatus _VI_FUNC rszvb_LoadGroundLoopCircuitModelData (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 functionType,
                                                        ViString fileName);
ViStatus _VI_FUNC rszvb_SetVirtualTransformPortPairState (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 functionType,
                                                          ViInt32 portPair,
                                                          ViBoolean state);
ViStatus _VI_FUNC rszvb_GetVirtualTransformPortPairState (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 functionType,
                                                          ViInt32 portPair,
                                                          ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetVirtualTransformPortPair (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 functionType,
                                                     ViInt32 portPair,
                                                     ViInt32 parameterType,
                                                     ViInt32 parameterNumber,
                                                     ViInt32 circuitModel,
                                                     ViReal64 value);
ViStatus _VI_FUNC rszvb_GetVirtualTransformPortPair (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 functionType,
                                                     ViInt32 portPair,
                                                     ViInt32 parameterType,
                                                     ViInt32 parameterNumber,
                                                     ViInt32 circuitModel,
                                                     ViReal64* value);
ViStatus _VI_FUNC rszvb_SetVirtualTransformPortPairCircuitModel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 portPair, ViInt32 circuitModel);
ViStatus _VI_FUNC rszvb_GetVirtualTransformPortPairCircuitModel
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 functionType,
              ViInt32 portPair, ViInt32* circuitModel);
ViStatus _VI_FUNC rszvb_LoadPortPairCircuitModelData (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 functionType,
                                                      ViInt32 portPair,
                                                      ViString fileName,
                                                      ViInt32 parameter,
                                                      ViBoolean interchangePortNumbers);
ViStatus _VI_FUNC rszvb_SetCoherentSignalState (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViBoolean coherentSignal);
ViStatus _VI_FUNC rszvb_GetCoherentSignalState (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViBoolean* coherentSignal);
ViStatus _VI_FUNC rszvb_SetCoherentSignalAmplitude (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 port,
                                                    ViReal64 amplitude);
ViStatus _VI_FUNC rszvb_GetCoherentSignalAmplitude (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 port,
                                                    ViReal64* amplitude);
ViStatus _VI_FUNC rszvb_SetCoherentSignalPhase (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViReal64 phase);
ViStatus _VI_FUNC rszvb_GetCoherentSignalPhase (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViReal64* phase);
ViStatus _VI_FUNC rszvb_SetCoherentSignalReferencePort (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 referencePort);
ViStatus _VI_FUNC rszvb_GetCoherentSignalReferencePort (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32* referencePort);
ViStatus _VI_FUNC rszvb_SetAlternateSweepMode (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViInt32 alternateSweepMode);
ViStatus _VI_FUNC rszvb_GetAlternateSweepMode (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViInt32* alternateSweepMode);
ViStatus _VI_FUNC rszvb_SetSpuriousAvoidance (ViSession instrumentHandle,
                                              ViInt32 channel,
                                              ViInt32 spuriousAvoidance);
ViStatus _VI_FUNC rszvb_GetSpuriousAvoidance (ViSession instrumentHandle,
                                              ViInt32 channel,
                                              ViInt32* spuriousAvoidance);
ViStatus _VI_FUNC rszvb_SetAutomaticLevelControlState (ViSession instrumentHandle,
                                                       ViBoolean ALCState);
ViStatus _VI_FUNC rszvb_GetAutomaticLevelControlState (ViSession instrumentHandle,
                                                       ViBoolean* ALCState);
ViStatus _VI_FUNC rszvb_SetIndividualALCPortState (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 port,
                                                   ViBoolean state);
ViStatus _VI_FUNC rszvb_GetIndividualALCPortState (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 port,
                                                   ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetALCPortState (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 port,
                                         ViBoolean state);
ViStatus _VI_FUNC rszvb_GetALCPortState (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 port,
                                         ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetALCPortClamp (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 port,
                                         ViBoolean clampState);
ViStatus _VI_FUNC rszvb_GetALCPortClamp (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 port,
                                         ViBoolean* clampState);
ViStatus _VI_FUNC rszvb_SetALCPortAUBWState (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViBoolean state);
ViStatus _VI_FUNC rszvb_GetALCPortAUBWState (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetALCPortBandwidth (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViReal64 bandwidth);
ViStatus _VI_FUNC rszvb_GetALCPortBandwidth (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViReal64* bandwidth);
ViStatus _VI_FUNC rszvb_SetALCPortCoupling (ViSession instrumentHandle,
                                            ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetALCPortCoupling (ViSession instrumentHandle,
                                            ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetALCChannelState (ViSession instrumentHandle,
                                            ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetALCChannelState (ViSession instrumentHandle,
                                            ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetALCLowPhaseNoiseMode (ViSession instrumentHandle,
                                                 ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetALCLowPhaseNoiseMode (ViSession instrumentHandle,
                                                 ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetALCPortOffsetState (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 port,
                                               ViBoolean state);
ViStatus _VI_FUNC rszvb_GetALCPortOffsetState (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 port,
                                               ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetALCPortControlRange (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViReal64 controlRange);
ViStatus _VI_FUNC rszvb_GetALCPortControlRange (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViReal64* controlRange);
ViStatus _VI_FUNC rszvb_SetALCPortStartOffset (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 port,
                                               ViReal64 startOffset);
ViStatus _VI_FUNC rszvb_GetALCPortStartOffset (ViSession instrumentHandle,
                                               ViInt32 channel, ViInt32 port,
                                               ViReal64* startOffset);
ViStatus _VI_FUNC rszvb_SetALCPortSettingTolerance (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 port,
                                                    ViReal64 settingTolerance);
ViStatus _VI_FUNC rszvb_GetALCPortSettingTolerance (ViSession instrumentHandle,
                                                    ViInt32 channel, ViInt32 port,
                                                    ViReal64* settingTolerance);
ViStatus _VI_FUNC rszvb_SetLowPhaseNoiseState (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViBoolean lowPhaseNoiseState);
ViStatus _VI_FUNC rszvb_GetLowPhaseNoiseState (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViBoolean* lowPhaseNoiseState);
ViStatus _VI_FUNC rszvb_ConfigurePortPIController (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 port,
                                                   ViInt32 PIControllerMode,
                                                   ViReal64 gain,
                                                   ViReal64 integrationTime);
ViStatus _VI_FUNC rszvb_ConfigureSAWMatchingNetwork (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViBoolean apply,
                                                     ViReal64 parallelL,
                                                     ViReal64 serialC,
                                                     ViReal64 differentialModeImpedance,
                                                     ViReal64 commonModeImpedance);
ViStatus _VI_FUNC rszvb_SetSAWState (ViSession instrumentHandle, ViInt32 channel,
                                     ViBoolean apply);
ViStatus _VI_FUNC rszvb_GetSAWState (ViSession instrumentHandle, ViInt32 channel,
                                     ViBoolean* apply);
ViStatus _VI_FUNC rszvb_SetSAWParallelL (ViSession instrumentHandle,
                                         ViInt32 channel, ViReal64 parallelL);
ViStatus _VI_FUNC rszvb_GetSAWParallelL (ViSession instrumentHandle,
                                         ViInt32 channel, ViReal64* parallelL);
ViStatus _VI_FUNC rszvb_SetSAWSerialC (ViSession instrumentHandle, ViInt32 channel,
                                       ViReal64 serialC);
ViStatus _VI_FUNC rszvb_GetSAWSerialC (ViSession instrumentHandle, ViInt32 channel,
                                       ViReal64* serialC);
ViStatus _VI_FUNC rszvb_SetSAWSimulationType (ViSession instrumentHandle,
                                              ViInt32 channel, ViInt32 type);
ViStatus _VI_FUNC rszvb_GetSAWSimulationType (ViSession instrumentHandle,
                                              ViInt32 channel, ViInt32* type);
ViStatus _VI_FUNC rszvb_SetPIControllerMode (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViInt32 PIControllerMode);
ViStatus _VI_FUNC rszvb_GetPIControllerMode (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViInt32* PIControllerMode);
ViStatus _VI_FUNC rszvb_SetPIControllerGain (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViReal64 gain);
ViStatus _VI_FUNC rszvb_GetPIControllerGain (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViReal64* gain);
ViStatus _VI_FUNC rszvb_SetPIControllerIntegrationTime (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 port,
                                                        ViReal64 integrationTime);
ViStatus _VI_FUNC rszvb_GetPIControllerIntegrationTime (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 port,
                                                        ViReal64* integrationTime);
ViStatus _VI_FUNC rszvb_ChannelAdd (ViSession instrumentHandle, ViInt32 channel,
                                    ViString channelName);
ViStatus _VI_FUNC rszvb_ChannelAddTrace (ViSession instrumentHandle, ViInt32 window,
                                         ViInt32 window_Trace, ViInt32 channel,
                                         ViString channelName, ViString traceName);
ViStatus _VI_FUNC rszvb_ChannelAddTraceDiagramArea (ViSession instrumentHandle,
                                                    ViInt32 window,
                                                    ViInt32 window_Trace,
                                                    ViInt32 channel,
                                                    ViString channelName,
                                                    ViString traceName);
ViStatus _VI_FUNC rszvb_ChannelDelete (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_ChannelList (ViSession instrumentHandle,
                                     ViChar _VI_FAR catalog[], ViInt32 bufferSize);
ViStatus _VI_FUNC rszvb_ChannelGetChannelName (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViChar _VI_FAR channelName[]);
ViStatus _VI_FUNC rszvb_ChannelGetChannelNumber (ViSession instrumentHandle,
                                                 ViString channelName,
                                                 ViInt32* channelNumber);
ViStatus _VI_FUNC rszvb_ChannelSetActive (ViSession instrumentHandle,
                                          ViInt32 channel);
ViStatus _VI_FUNC rszvb_ChannelGetActive (ViSession instrumentHandle,
                                          ViInt32* channel);
ViStatus _VI_FUNC rszvb_ChannelRename (ViSession instrumentHandle, ViInt32 channel,
                                       ViString channelName);
ViStatus _VI_FUNC rszvb_SetConnector (ViSession instrumentHandle, ViInt32 channel,
                                      ViInt32 port, ViInt32 connector);
ViStatus _VI_FUNC rszvb_GetConnector (ViSession instrumentHandle, ViInt32 channel,
                                      ViInt32 port, ViInt32* connector);
ViStatus _VI_FUNC rszvb_SetSameConnectorTypeAtAllPorts (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViBoolean sameConnectorAtAllPorts);
ViStatus _VI_FUNC rszvb_GetSameConnectorTypeAtAllPorts (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViBoolean* sameConnectorAtAllPorts);
ViStatus _VI_FUNC rszvb_SetSameConnectorGenderAtAllPorts (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViBoolean sameGenderAtAllPorts);
ViStatus _VI_FUNC rszvb_GetSameConnectorGenderAtAllPorts (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViBoolean* sameGenderAtAllPorts);
ViStatus _VI_FUNC rszvb_SetUserConnector (ViSession instrumentHandle,
                                          ViInt32 channel, ViInt32 port,
                                          ViString connector,
                                          ViInt32 connectorGender);
ViStatus _VI_FUNC rszvb_GetUserConnector (ViSession instrumentHandle,
                                          ViInt32 channel, ViInt32 port,
                                          ViChar _VI_FAR connector[],
                                          ViInt32* connectorGender);
ViStatus _VI_FUNC rszvb_SetSameSweepSetup (ViSession instrumentHandle,
                                           ViInt32 channel,
                                           ViBoolean sameSweepSetup);
ViStatus _VI_FUNC rszvb_GetSameSweepSetup (ViSession instrumentHandle,
                                           ViInt32 channel,
                                           ViBoolean* sameSweepSetup);
ViStatus _VI_FUNC rszvb_SetSParameterDetector (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViInt32 sParameterDetector);
ViStatus _VI_FUNC rszvb_GetSParameterDetector (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViInt32* sParameterDetector);
ViStatus _VI_FUNC rszvb_SelectCalibrationType (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViString calibrationName,
                                               ViInt32 parameters, ViInt32 port1,
                                               ViInt32 port2, ViInt32 port3,
                                               ViInt32 port4);
ViStatus _VI_FUNC rszvb_GetCalibrationType (ViSession instrumentHandle,
                                            ViInt32 channel,
                                            ViInt32* calibrationType,
                                            ViInt32* port1, ViInt32* port2,
                                            ViInt32* port3, ViInt32* port4);
ViStatus _VI_FUNC rszvb_StartCalibration (ViSession instrumentHandle,
                                          ViInt32 channel, ViInt32 standard,
                                          ViInt32 port1, ViInt32 port2);
ViStatus _VI_FUNC rszvb_StartCalibrationLine (ViSession instrumentHandle,
                                              ViInt32 channel, ViInt32 line,
                                              ViInt32 port1, ViInt32 port2);
ViStatus _VI_FUNC rszvb_StartCalibrationWithOptions (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 standard,
                                                     ViInt32 port1, ViInt32 port2,
                                                     ViBoolean dispersion,
                                                     ViInt32 delayPhase,
                                                     ViReal64 delayPhaseValue);
ViStatus _VI_FUNC rszvb_SetCalibrationReferencePlaneShift
             (ViSession instrumentHandle, ViInt32 channel,
              ViReal64 referencePlaneShift);
ViStatus _VI_FUNC rszvb_GetCalibrationReferencePlaneShift
             (ViSession instrumentHandle, ViInt32 channel,
              ViReal64* referencePlaneShift);
ViStatus _VI_FUNC rszvb_SetCalibrationReferencePlaneShiftSpecific
             (ViSession instrumentHandle, ViInt32 channel,
              ViReal64 referencePlaneShift, ViString calibrationName);
ViStatus _VI_FUNC rszvb_GetCalibrationReferencePlaneShiftSpecific
             (ViSession instrumentHandle, ViInt32 channel, ViString calibrationName,
              ViReal64* referencePlaneShift);
ViStatus _VI_FUNC rszvb_QueryCalibrationReferencePlaneShift
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibrationIndex,
              ViReal64* referencePlaneShift);
ViStatus _VI_FUNC rszvb_SaveCalibrationData (ViSession instrumentHandle,
                                             ViInt32 channel);
ViStatus _VI_FUNC rszvb_GenerateDefaultCalibrationData (ViSession instrumentHandle,
                                                        ViInt32 channel);
ViStatus _VI_FUNC rszvb_DeleteCalibrationData (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViString calibrationName);
ViStatus _VI_FUNC rszvb_DeleteAllCalibrationData (ViSession instrumentHandle,
                                                  ViInt32 channel);
ViStatus _VI_FUNC rszvb_ReadCalibrationData (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViInt32 errorTermParameters,
                                             ViInt32 port1, ViInt32 port2,
                                             ViReal64 _VI_FAR calibrationData[]);
ViStatus _VI_FUNC rszvb_WriteCalibrationData (ViSession instrumentHandle,
                                              ViInt32 channel,
                                              ViInt32 errorTermParameters,
                                              ViInt32 port1, ViInt32 port2,
                                              ViReal64 _VI_FAR calibrationData[]);
ViStatus _VI_FUNC rszvb_SetCorrectionState (ViSession instrumentHandle,
                                            ViInt32 channel,
                                            ViBoolean correctionState);
ViStatus _VI_FUNC rszvb_GetCorrectionState (ViSession instrumentHandle,
                                            ViInt32 channel,
                                            ViBoolean* correctionState);
ViStatus _VI_FUNC rszvb_AcquireSourcePowerCalibration (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 source,
                                                       ViInt32 portNumber);
ViStatus _VI_FUNC rszvb_InitiateSourcePowerCalibration (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 portNumber,
                                                        ViInt32 externalPowerMeter);
ViStatus _VI_FUNC rszvb_SetDummySourcePowerCalibrationState
             (ViSession instrumentHandle, ViBoolean dummySourcePowerCalibration);
ViStatus _VI_FUNC rszvb_GetDummySourcePowerCalibrationState
             (ViSession instrumentHandle, ViBoolean* dummySourcePowerCalibration);
ViStatus _VI_FUNC rszvb_SetSourcePowerCalibrationPortState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViBoolean portState);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationPortState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViBoolean* portState);
ViStatus _VI_FUNC rszvb_SetSourcePowerCalibrationGeneratorState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViBoolean generatorState);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationGeneratorState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViBoolean* generatorState);
ViStatus _VI_FUNC rszvb_SetVerificationSweepState (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViBoolean verificationSweep);
ViStatus _VI_FUNC rszvb_GetVerificationSweepState (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViBoolean* verificationSweep);
ViStatus _VI_FUNC rszvb_QueryVerificationSweepResults (ViSession instrumentHandle,
                                                       ViBoolean* calibrationPassed,
                                                       ViReal64* maxOffset);
ViStatus _VI_FUNC rszvb_GeneratorPowerCalibrationHarmonic
             (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetSourcePowerCalibrationState (ViSession instrumentHandle,
                                                        ViBoolean calibrationState);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationState (ViSession instrumentHandle,
                                                        ViBoolean* calibrationState);
ViStatus _VI_FUNC rszvb_SetReferenceReceiverCalibrationState
             (ViSession instrumentHandle, ViBoolean calibrationState);
ViStatus _VI_FUNC rszvb_GetReferenceReceiverCalibrationState
             (ViSession instrumentHandle, ViBoolean* calibrationState);
ViStatus _VI_FUNC rszvb_ModifySourcePowerCalibrationSettings
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViInt32 numberOfReadings, ViReal64 tolerance,
              ViBoolean otherSourcesState, ViReal64 portPowerOffset,
              ViInt32 offsetParameter, ViReal64 calibrationPowerOffset);
ViStatus _VI_FUNC rszvb_SetNumberOfReadings (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViInt32 numberOfReadings);
ViStatus _VI_FUNC rszvb_GetNumberOfReadings (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViInt32* numberOfReadings);
ViStatus _VI_FUNC rszvb_SetTolerance (ViSession instrumentHandle, ViInt32 channel,
                                      ViReal64 tolerance);
ViStatus _VI_FUNC rszvb_GetTolerance (ViSession instrumentHandle, ViInt32 channel,
                                      ViReal64* tolerance);
ViStatus _VI_FUNC rszvb_SetOtherSourcesState (ViSession instrumentHandle,
                                              ViInt32 channel,
                                              ViBoolean otherSources);
ViStatus _VI_FUNC rszvb_GetOtherSourcesState (ViSession instrumentHandle,
                                              ViInt32 channel,
                                              ViBoolean* otherSources);
ViStatus _VI_FUNC rszvb_SetPortPowerOffset (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 portNumber,
                                            ViReal64 portPowerOffset,
                                            ViInt32 offsetParameter);
ViStatus _VI_FUNC rszvb_GetPortPowerOffset (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 portNumber,
                                            ViReal64* portPowerOffset,
                                            ViInt32* offsetParameter);
ViStatus _VI_FUNC rszvb_SetCalibrationPowerOffset (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViInt32 portNumber,
                                                   ViReal64 calibrationPowerOffset);
ViStatus _VI_FUNC rszvb_GetCalibrationPowerOffset (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViInt32 portNumber,
                                                   ViReal64* calibrationPowerOffset);
ViStatus _VI_FUNC rszvb_SetCalibrationPowerGeneratorOffset
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViInt32 generatorNumber, ViReal64 calPowerGeneratorOffset);
ViStatus _VI_FUNC rszvb_GetCalibrationPowerGeneratorOffset
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViInt32 generatorNumber, ViReal64* calPowerGeneratorOffset);
ViStatus _VI_FUNC rszvb_SetReferenceReceiverAfterFirstCalSweep
             (ViSession instrumentHandle, ViBoolean fastSourcePowerCalibration);
ViStatus _VI_FUNC rszvb_GetReferenceReceiverAfterFirstCalSweep
             (ViSession instrumentHandle, ViBoolean* fastSourcePowerCalibration);
ViStatus _VI_FUNC rszvb_SetPowerCalibrationMethodSource (ViSession instrumentHandle,
                                                         ViInt32 methodSource);
ViStatus _VI_FUNC rszvb_GetPowerCalibrationMethodSource (ViSession instrumentHandle,
                                                         ViInt32* methodSource);
ViStatus _VI_FUNC rszvb_SetCalibrationPowerMeterReadings (ViSession instrumentHandle,
                                                          ViInt32 powerMeterReadings);
ViStatus _VI_FUNC rszvb_GetCalibrationPowerMeterReadings (ViSession instrumentHandle,
                                                          ViInt32* powerMeterReadings);
ViStatus _VI_FUNC rszvb_ReadSourcePowerCorrectionData (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 portNumber,
                                                       ViString calibratedWave,
                                                       ViInt32* numberOfValues,
                                                       ViReal64 _VI_FAR powerCorrectionValues[]);
ViStatus _VI_FUNC rszvb_WriteSourcePowerCorrectionData (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 portNumber,
                                                        ViString calibratedWave,
                                                        ViInt32 numberOfValues,
                                                        ViReal64 _VI_FAR powerCorrectionValues[]);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationNumberOfWaves
             (ViSession instrumentHandle, ViInt32 channel, ViInt32* numberOfWaves);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationParamaterWave
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibrationIndex,
              ViInt32 bufferSize, ViChar _VI_FAR calibratedWave[]);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationParamaterStart
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibrationIndex,
              ViReal64* start);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationParamaterStop
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibrationIndex,
              ViReal64* stop);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationParamaterPoints
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibrationIndex,
              ViInt32* points);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationParamaterType
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibrationIndex,
              ViInt32* type);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationParamaterAttenuation
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibrationIndex,
              ViReal64* attenuation);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationParamaterCWPower
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibrationIndex,
              ViReal64* CWPower);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationParamaterCWFrequency
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibrationIndex,
              ViReal64* CWFrequency);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationParamaterTimestamp
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibrationIndex,
              ViInt32 bufferSize, ViChar _VI_FAR timestamp[]);
ViStatus _VI_FUNC rszvb_SetSourcePowerCalibrationConvergenceFactor
             (ViSession instrumentHandle, ViReal64 convergenceFactor);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationConvergenceFactor
             (ViSession instrumentHandle, ViReal64* convergenceFactor);
ViStatus 
    _VI_FUNC rszvb_SetDummySourcePowerCalibrationSensitivityCorrectionRange
        (ViSession instrumentHandle, ViInt32 channel, ViInt32 frequencyRange);
ViStatus 
    _VI_FUNC rszvb_GetDummySourcePowerCalibrationSensitivityCorrectionRange
        (ViSession instrumentHandle, ViInt32 channel, ViInt32* frequencyRange);
ViStatus _VI_FUNC rszvb_SetSourcePowerCalibrationConverterState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 converter,
              ViBoolean calibrationConverter);
ViStatus _VI_FUNC rszvb_GetSourcePowerCalibrationConverterState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 converter,
              ViBoolean* calibrationConverter);
ViStatus _VI_FUNC rszvb_AcquireReceiverPowerCalibration (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 wave,
                                                         ViInt32 portNumber,
                                                         ViInt32 source,
                                                         ViInt32 sourceNumber,
                                                         ViInt32 referencePower);
ViStatus _VI_FUNC rszvb_SetAWaveReceiverPowerCalibrationState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViBoolean receiverPowerCalibration);
ViStatus _VI_FUNC rszvb_GetAWaveReceiverPowerCalibrationState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViBoolean* receiverPowerCalibration);
ViStatus _VI_FUNC rszvb_SetAWaveIdealPowerMeterMatchState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViBoolean state);
ViStatus _VI_FUNC rszvb_GetAWaveIdealPowerMeterMatchState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetBWaveReceiverPowerCalibrationState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViBoolean receiverPowerCalibration);
ViStatus _VI_FUNC rszvb_GetBWaveReceiverPowerCalibrationState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 portNumber,
              ViBoolean* receiverPowerCalibration);
ViStatus _VI_FUNC rszvb_ReadReceiverPowerCorrectionData (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 portNumber,
                                                         ViString calibratedWave,
                                                         ViInt32* numberOfValues,
                                                         ViReal64 _VI_FAR powerCorrectionValues[]);
ViStatus _VI_FUNC rszvb_WriteReceiverPowerCorrectionData (ViSession instrumentHandle,
                                                          ViInt32 channel,
                                                          ViInt32 portNumber,
                                                          ViString calibratedWave,
                                                          ViInt32 numberOfValues,
                                                          ViReal64 _VI_FAR powerCorrectionValues[]);
ViStatus _VI_FUNC rszvb_ReceiverPowerCalibrationHarmonic (ViSession instrumentHandle,
                                                          ViInt32 channel);
ViStatus _VI_FUNC rszvb_CorrectionManager (ViSession instrumentHandle,
                                           ViInt32 operationToBePerformed,
                                           ViString fileName,
                                           ViString loadParameter);
ViStatus _VI_FUNC rszvb_SetPowerSensorPosition (ViSession instrumentHandle,
                                                ViInt32 powerSensorPosition);
ViStatus _VI_FUNC rszvb_GetPowerSensorPosition (ViSession instrumentHandle,
                                                ViInt32* powerSensorPosition);
ViStatus _VI_FUNC rszvb_SetTwoPortTransmissionCoefficientsEnabled
             (ViSession instrumentHandle, ViBoolean twoPortEnabled);
ViStatus _VI_FUNC rszvb_GetTwoPortTransmissionCoefficientsEnabled
             (ViSession instrumentHandle, ViBoolean* twoPortEnabled);
ViStatus _VI_FUNC rszvb_GetLossListNumberOfValues (ViSession instrumentHandle,
                                                   ViInt32* numberOfValues);
ViStatus _VI_FUNC rszvb_SetPowerLossListCoefficient (ViSession instrumentHandle,
                                                     ViInt32 operationToBePerformed,
                                                     ViInt32 point,
                                                     ViReal64 frequency,
                                                     ViReal64 transmissionCoefficient);
ViStatus _VI_FUNC rszvb_GetPowerLossListCoefficient (ViSession instrumentHandle,
                                                     ViInt32 point,
                                                     ViReal64* frequency,
                                                     ViReal64* transmissionCoefficient);
ViStatus _VI_FUNC rszvb_DeleteAllPowerLossListPoints (ViSession instrumentHandle);
ViStatus _VI_FUNC rszvb_DeletePowerLossListSinglePoint (ViSession instrumentHandle,
                                                        ViInt32 point);
ViStatus _VI_FUNC rszvb_SetPowerLossListTrace (ViSession instrumentHandle,
                                               ViString traceName);
ViStatus _VI_FUNC rszvb_SetSourcePowerCorrectionState (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 portNumber,
                                                       ViBoolean sourcePowerCorrectionState);
ViStatus _VI_FUNC rszvb_GetSourcePowerCorrectionState (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 portNumber,
                                                       ViBoolean* sourcePowerCorrectionState);
ViStatus _VI_FUNC rszvb_SetReceiverPowerCorrectionState (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 portNumber,
                                                         ViBoolean receiverPowerCorrectionState);
ViStatus _VI_FUNC rszvb_GetReceiverPowerCorrectionState (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 portNumber,
                                                         ViBoolean* receiverPowerCorrectionState);
ViStatus _VI_FUNC rszvb_CalibrationManager (ViSession instrumentHandle,
                                            ViInt32 channel,
                                            ViInt32 operationToBePerformed,
                                            ViString fileName);
ViStatus _VI_FUNC rszvb_CalibrationAuto (ViSession instrumentHandle,
                                         ViInt32 channel,
                                         ViString calibrationKitName,
                                         ViInt32 analyzerPort1,
                                         ViInt32 analyzerPort2,
                                         ViInt32 analyzerPort3,
                                         ViInt32 analyzerPort4,
                                         ViInt32 calUnitPort1, ViInt32 calUnitPort2,
                                         ViInt32 calUnitPort3,
                                         ViInt32 calUnitPort4);
ViStatus _VI_FUNC rszvb_CalibrationAutoSimplified (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViString calibrationKitName,
                                                   ViInt32 analyzerPort1,
                                                   ViInt32 analyzerPort2,
                                                   ViInt32 analyzerPort3,
                                                   ViInt32 analyzerPort4);
ViStatus _VI_FUNC rszvb_CalibrationAutoType (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 parameters,
                                             ViString calibrationKitName,
                                             ViInt32 analyzerPort1,
                                             ViInt32 analyzerPort2,
                                             ViInt32 analyzerPort3,
                                             ViInt32 analyzerPort4,
                                             ViInt32 calUnitPort1,
                                             ViInt32 calUnitPort2,
                                             ViInt32 calUnitPort3,
                                             ViInt32 calUnitPort4);
ViStatus _VI_FUNC rszvb_CalibrationAutoTypeSimplified (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 parameters,
                                                       ViString calibrationKitName,
                                                       ViInt32 analyzerPort1,
                                                       ViInt32 analyzerPort2,
                                                       ViInt32 analyzerPort3,
                                                       ViInt32 analyzerPort4);
ViStatus _VI_FUNC rszvb_CalibrationRetainPortGroups (ViSession instrumentHandle,
                                                     ViBoolean retainPortGroups);
ViStatus _VI_FUNC rszvb_GetCalibrationConnection (ViSession instrumentHandle,
                                                  ViInt32 channel,
                                                  ViInt32* analyzerPort1,
                                                  ViInt32* analyzerPort2,
                                                  ViInt32* analyzerPort3,
                                                  ViInt32* analyzerPort4);
ViStatus _VI_FUNC rszvb_CalibrationAutoEx (ViSession instrumentHandle,
                                           ViInt32 channel,
                                           ViString calibrationKitName,
                                           ViInt32 analyzerPort1,
                                           ViInt32 analyzerPort2,
                                           ViInt32 analyzerPort3,
                                           ViInt32 analyzerPort4,
                                           ViInt32 calUnitPort1,
                                           ViInt32 calUnitPort2,
                                           ViInt32 calUnitPort3,
                                           ViInt32 calUnitPort4, ViInt32 timeout);
ViStatus _VI_FUNC rszvb_CalibrationAutoAssignmentType (ViSession instrumentHandle,
                                                       ViInt32 channel,
                                                       ViInt32 parameters,
                                                       ViString calibrationKitName);
ViStatus _VI_FUNC rszvb_CalibrationAutoAssignmentDefinition
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 assignment,
              ViInt32 analyzerPort1, ViInt32 analyzerPort2, ViInt32 analyzerPort3,
              ViInt32 analyzerPort4, ViInt32 calUnitPort1, ViInt32 calUnitPort2,
              ViInt32 calUnitPort3, ViInt32 calUnitPort4);
ViStatus _VI_FUNC rszvb_GetCalibrationAutoAssingnmentDefinition
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 assignment,
              ViInt32* analyzerPort1, ViInt32* analyzerPort2,
              ViInt32* analyzerPort3, ViInt32* analyzerPort4, ViInt32* calUnitPort1,
              ViInt32* calUnitPort2, ViInt32* calUnitPort3, ViInt32* calUnitPort4);
ViStatus _VI_FUNC rszvb_InitiateCalibrationAutoAssignment
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 assignment);
ViStatus _VI_FUNC rszvb_CalibrationAutoAssignmentSave (ViSession instrumentHandle,
                                                       ViInt32 channel);
ViStatus _VI_FUNC rszvb_CalibrationAutoAssingnmentDeleteAll
             (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetCalibrationDataCurrentState (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViBoolean keepMeasData);
ViStatus _VI_FUNC rszvb_GetCalibrationDataCurrentState (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViBoolean* keepMeasData);
ViStatus _VI_FUNC rszvb_SetCalibrationDataDefaultState (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViBoolean keepMeasData);
ViStatus _VI_FUNC rszvb_GetCalibrationDataDefaultState (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViBoolean* keepMeasData);
ViStatus _VI_FUNC rszvb_ExpCharDataTouchstoneFile (ViSession instrumentHandle,
                                                   ViString fileName);
ViStatus _VI_FUNC rszvb_ExportUserCharacterizationDataTouchstoneFile
             (ViSession instrumentHandle, ViString directoryName,
              ViString fileName);
ViStatus _VI_FUNC rszvb_SetCalibrationConnector (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViString connectorName,
                                                 ViInt32 propagationMode,
                                                 ViInt32 connectorType,
                                                 ViReal64 relativePermittivity,
                                                 ViReal64 impedance);
ViStatus _VI_FUNC rszvb_GetCalibrationConnector (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViString connectorName,
                                                 ViInt32* propagationMode,
                                                 ViInt32* connectorType,
                                                 ViReal64* relativePermittivity,
                                                 ViReal64* impedance);
ViStatus _VI_FUNC rszvb_CalibrationConnectorCatalog (ViSession instrumentHandle,
                                                     ViChar _VI_FAR catalog[],
                                                     ViInt32 bufferSize);
ViStatus _VI_FUNC rszvb_DeleteCalibrationConnector (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViString connectorName);
ViStatus _VI_FUNC rszvb_GetCalibrationDate (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 bufferSize,
                                            ViChar _VI_FAR calibrationDate[]);
ViStatus _VI_FUNC rszvb_GetCalibrationState (ViSession instrumentHandle,
                                             ViInt32 channel,
                                             ViInt32* calibrationState);
ViStatus _VI_FUNC rszvb_GetCalibrationLabel (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 bufferSize,
                                             ViChar _VI_FAR label[]);
ViStatus _VI_FUNC rszvb_GetCalibrationDataParameters (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViReal64* frequencyStart,
                                                      ViReal64* frequencyStop,
                                                      ViInt32* numberOfPoints,
                                                      ViReal64* internalSignalSourcePower,
                                                      ViInt32* sweepType);
ViStatus _VI_FUNC rszvb_GetCalibrationsNumber (ViSession instrumentHandle,
                                               ViInt32 channel,
                                               ViInt32* numberOfCalibrations);
ViStatus _VI_FUNC rszvb_GetCalibrationDataParametersMoreCalibrations
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibration,
              ViReal64* frequencyStart, ViReal64* frequencyStop,
              ViInt32* numberOfPoints, ViReal64* internalSignalSourcePower,
              ViInt32* sweepType);
ViStatus _VI_FUNC rszvb_GetCalibrationDataBandwidth (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 calibration,
                                                     ViReal64* bandwidth);
ViStatus _VI_FUNC rszvb_GetCalibrationDataPointDelay (ViSession instrumentHandle,
                                                      ViInt32 channel,
                                                      ViInt32 calibration,
                                                      ViReal64* pointDelay);
ViStatus _VI_FUNC rszvb_GetCalibrationDataReceiverAttenuation
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 calibration,
              ViInt32 arraySize, ViInt32 _VI_FAR calibrationPort[],
              ViReal64 _VI_FAR attenuation[], ViInt32* returnedValues);
ViStatus _VI_FUNC rszvb_GetCalibrationDataType (ViSession instrumentHandle,
                                                ViInt32 channel,
                                                ViInt32 calibration,
                                                ViInt32* calibrationType);
ViStatus _VI_FUNC rszvb_GetCalibrationDataPorts (ViSession instrumentHandle,
                                                 ViInt32 channel,
                                                 ViInt32 calibration,
                                                 ViInt32 arraySize,
                                                 ViInt32* calibrationPorts,
                                                 ViInt32* returnedValues);
ViStatus _VI_FUNC rszvb_GetCalibrationDataThroughs (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViInt32 calibration,
                                                    ViInt32 bufferSize,
                                                    ViChar _VI_FAR throughs[]);
ViStatus _VI_FUNC rszvb_GetCalibrationDataTimestamp (ViSession instrumentHandle,
                                                     ViInt32 channel,
                                                     ViInt32 calibration,
                                                     ViInt32 bufferSize,
                                                     ViChar _VI_FAR timestamp[]);
ViStatus _VI_FUNC rszvb_SetActiveCalibrationUnit (ViSession instrumentHandle,
                                                  ViString calibrationUnit);
ViStatus _VI_FUNC rszvb_GetActiveCalibrationUnit (ViSession instrumentHandle,
                                                  ViInt32 bufferSize,
                                                  ViChar _VI_FAR calibrationUnit[]);
ViStatus _VI_FUNC rszvb_SetAutomaticPowerReductionState (ViSession instrumentHandle,
                                                         ViBoolean automaticPowerReduction);
ViStatus _VI_FUNC rszvb_GetAutomaticPowerReductionState (ViSession instrumentHandle,
                                                         ViBoolean* automaticPowerReduction);
ViStatus _VI_FUNC rszvb_GetAllCalibrationUnits (ViSession instrumentHandle,
                                                ViInt32 bufferSize,
                                                ViChar _VI_FAR calibrationUnit[]);
ViStatus _VI_FUNC rszvb_ConfigureCalibrationUnitStandard (ViSession instrumentHandle,
                                                          ViInt32 standard,
                                                          ViInt32 port1,
                                                          ViInt32 port2);
ViStatus _VI_FUNC rszvb_SetFactoryCalibrationState (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean factoryCalibration);
ViStatus _VI_FUNC rszvb_GetFactoryCalibrationState (ViSession instrumentHandle,
                                                    ViInt32 channel,
                                                    ViBoolean* factoryCalibration);
ViStatus _VI_FUNC rszvb_SetEnhancedWaveCorrection (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViBoolean errorCorrection);
ViStatus _VI_FUNC rszvb_GetEnhancedWaveCorrection (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViBoolean* errorCorrection);
ViStatus _VI_FUNC rszvb_SetLoadMatchingCorrection (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViBoolean loadMatchingCorrection);
ViStatus _VI_FUNC rszvb_GetLoadMatchingCorrection (ViSession instrumentHandle,
                                                   ViInt32 channel,
                                                   ViBoolean* loadMatchingCorrection);
ViStatus _VI_FUNC rszvb_SetCalibrationCorrectionBaseFrequencyState
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean state);
ViStatus _VI_FUNC rszvb_GetCalibrationCorrectionBaseFrequencyState
             (ViSession instrumentHandle, ViInt32 channel, ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetCalibrationKit (ViSession instrumentHandle,
                                           ViInt32 connector,
                                           ViString calibrationKitName);
ViStatus _VI_FUNC rszvb_GetCalibrationKit (ViSession instrumentHandle,
                                           ViInt32 connector, ViInt32 bufferSize,
                                           ViChar _VI_FAR calibrationKitName[]);
ViStatus _VI_FUNC rszvb_SetCalibrationKitWithLabel (ViSession instrumentHandle,
                                                    ViInt32 connector,
                                                    ViString calibrationKitName,
                                                    ViString calibrationKitLabel);
ViStatus _VI_FUNC rszvb_SetCalibrationKitUserConnectorType
             (ViSession instrumentHandle, ViString connector,
              ViString calibrationKitName);
ViStatus _VI_FUNC rszvb_GetCalibrationKitUserConnectorType
             (ViSession instrumentHandle, ViString connector, ViInt32 bufferSize,
              ViChar _VI_FAR calibrationKitName[]);
ViStatus _VI_FUNC rszvb_SetCalibrationKitUserConnectorTypeWithLabel
             (ViSession instrumentHandle, ViString connectionType,
              ViString calibrationKitName, ViString calibrationKitLabel);
ViStatus _VI_FUNC rszvb_GetCalibrationKitUserConnectorTypeWithLabel
             (ViSession instrumentHandle, ViString connectionType,
              ViInt32 bufferSize, ViChar _VI_FAR calibrationKitData[]);
ViStatus _VI_FUNC rszvb_CalibrationKitCatalog (ViSession instrumentHandle,
                                               ViString connectorName,
                                               ViChar _VI_FAR catalog[],
                                               ViInt32 bufferSize);
ViStatus _VI_FUNC rszvb_CalibrationKitCatalogWithLabel (ViSession instrumentHandle,
                                                        ViString connectorName,
                                                        ViInt32 bufferSize,
                                                        ViChar _VI_FAR catalog[]);
ViStatus _VI_FUNC rszvb_ImportZVRCalibrationKit (ViSession instrumentHandle,
                                                 ViString calibrationKitName);
ViStatus _VI_FUNC rszvb_ConfigureCalibrationStandard (ViSession instrumentHandle,
                                                      ViInt32 connector,
                                                      ViInt32 standard,
                                                      ViString kit,
                                                      ViString serialNumber,
                                                      ViReal64 minFreqHz,
                                                      ViReal64 maxFreqHz,
                                                      ViReal64 lengthmm,
                                                      ViReal64 loss, ViReal64 c0L0,
                                                      ViReal64 c1L1, ViReal64 c2L2,
                                                      ViReal64 c3L3,
                                                      ViInt32 approximation);
ViStatus _VI_FUNC rszvb_ConfigureCalibrationStandardWithLabel
             (ViSession instrumentHandle, ViInt32 standard, ViString connector,
              ViString calkitName, ViString calkitLabel, ViString standardLabel,
              ViReal64 minFreqHz, ViReal64 maxFreqHz, ViReal64 electricalLength,
              ViReal64 loss, ViReal64 z0, ViReal64 _VI_FAR capacitances[],
              ViReal64 _VI_FAR residualInductances[], ViInt32 approximation);
ViStatus _VI_FUNC rszvb_CalibrationStandardsCatalog (ViSession instrumentHandle,
                                                     ViString calibrationKitName,
                                                     ViChar _VI_FAR catalog[],
                                                     ViInt32 bufferSize);
ViStatus _VI_FUNC rszvb_CalibrationStandardsCatalogWithLabel
             (ViSession instrumentHandle, ViString calibrationKitName,
              ViString calibrationKitLabel, ViInt32 bufferSize,
              ViChar _VI_FAR catalog[]);
ViStatus _VI_FUNC rszvb_SaveCalibrationKit (ViSession instrumentHandle,
                                            ViString fileName);
ViStatus _VI_FUNC rszvb_SaveCalibrationKitPorts (ViSession instrumentHandle,
                                                 ViString fileName,
                                                 ViInt32 parameters,
                                                 ViInt32 arraySize,
                                                 ViInt32 _VI_FAR VNAPorts[],
                                                 ViInt32 _VI_FAR calUnitPorts[]);
ViStatus _VI_FUNC rszvb_LoadCalibrationKit (ViSession instrumentHandle,
                                            ViString connectorName,
                                            ViString calibrationKitName,
                                            ViInt32 standard,
                                            ViString calibrationKitLabel,
                                            ViString fileName, ViInt32 portNumber1,
                                            ViInt32 portNumber2);
ViStatus _VI_FUNC rszvb_SetCalibrationKitLabel (ViSession instrumentHandle,
                                                ViString calibrationKitName,
                                                ViString label);
ViStatus _VI_FUNC rszvb_RenameCalibrationKit (ViSession instrumentHandle,
                                              ViString calibrationKitName,
                                              ViString label, ViString newLabel);
ViStatus _VI_FUNC rszvb_GetCalibrationKitLabel (ViSession instrumentHandle,
                                                ViString calibrationKitName,
                                                ViChar _VI_FAR label[]);
ViStatus _VI_FUNC rszvb_DeleteCalibrationKit (ViSession instrumentHandle,
                                              ViString calibrationKitName);
ViStatus _VI_FUNC rszvb_DeleteCalibrationKitWithLabel (ViSession instrumentHandle,
                                                       ViString calibrationKitName,
                                                       ViString calibrationKitLabel);
ViStatus _VI_FUNC rszvb_ImportKit (ViSession instrumentHandle, ViString fileName);
ViStatus _VI_FUNC rszvb_AdditionalDirectoryCalibrationKit
             (ViSession instrumentHandle, ViString directory);
ViStatus _VI_FUNC rszvb_ExportKit (ViSession instrumentHandle, ViString kitName,
                                   ViString fileName);
ViStatus _VI_FUNC rszvb_ExportKitWithLabel (ViSession instrumentHandle,
                                            ViString kitName, ViString kitLabel,
                                            ViString fileName);
ViStatus _VI_FUNC rszvb_ResetOffsets (ViSession instrumentHandle, ViInt32 channel);
ViStatus _VI_FUNC rszvb_QueryResetOffsets (ViSession instrumentHandle,
                                           ViInt32 channel, ViInt32* offsets);
ViStatus _VI_FUNC rszvb_SetElectricalLength (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViReal64 electricalLength);
ViStatus _VI_FUNC rszvb_GetElectricalLength (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViReal64* electricalLength);
ViStatus _VI_FUNC rszvb_ConfigureMechanicalLength (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 port,
                                                   ViReal64 mechanicalLength,
                                                   ViReal64 permittivity);
ViStatus _VI_FUNC rszvb_SetMechanicalLength (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViReal64 mechanicalLength);
ViStatus _VI_FUNC rszvb_GetMechanicalLength (ViSession instrumentHandle,
                                             ViInt32 channel, ViInt32 port,
                                             ViReal64* mechanicalLength);
ViStatus _VI_FUNC rszvb_SetPermittivity (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 port,
                                         ViReal64 permittivity);
ViStatus _VI_FUNC rszvb_GetPermittivity (ViSession instrumentHandle,
                                         ViInt32 channel, ViInt32 port,
                                         ViReal64* permittivity);
ViStatus _VI_FUNC rszvb_ConfigureLoss (ViSession instrumentHandle, ViInt32 channel,
                                       ViInt32 port, ViReal64 lossAtDC,
                                       ViReal64 lossAtFrequency,
                                       ViReal64 lossReferenceFrequency);
ViStatus _VI_FUNC rszvb_SetLossAtDC (ViSession instrumentHandle, ViInt32 channel,
                                     ViInt32 port, ViReal64 lossAtDC);
ViStatus _VI_FUNC rszvb_GetLossAtDC (ViSession instrumentHandle, ViInt32 channel,
                                     ViInt32 port, ViReal64* lossAtDC);
ViStatus _VI_FUNC rszvb_SetLossAtFrequency (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 port,
                                            ViReal64 lossAtFrequency);
ViStatus _VI_FUNC rszvb_GetLossAtFrequency (ViSession instrumentHandle,
                                            ViInt32 channel, ViInt32 port,
                                            ViReal64* lossAtFrequency);
ViStatus _VI_FUNC rszvb_SetLossReferenceFrequency (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 port,
                                                   ViReal64 lossReferenceFrequency);
ViStatus _VI_FUNC rszvb_GetLossReferenceFrequency (ViSession instrumentHandle,
                                                   ViInt32 channel, ViInt32 port,
                                                   ViReal64* lossReferenceFrequency);
ViStatus _VI_FUNC rszvb_SetDelay (ViSession instrumentHandle, ViInt32 channel,
                                  ViInt32 port, ViReal64 delay);
ViStatus _VI_FUNC rszvb_GetDelay (ViSession instrumentHandle, ViInt32 channel,
                                  ViInt32 port, ViReal64* delay);
ViStatus _VI_FUNC rszvb_QueryDirectFixtureCompensation (ViSession instrumentHandle,
                                                        ViInt32 channel,
                                                        ViInt32 port,
                                                        ViBoolean* directFixtureCompensation);
ViStatus _VI_FUNC rszvb_AutoLength (ViSession instrumentHandle, ViInt32 channel,
                                    ViInt32 port);
ViStatus _VI_FUNC rszvb_AutoLengthAndLoss (ViSession instrumentHandle,
                                           ViInt32 channel, ViInt32 port);
ViStatus _VI_FUNC rszvb_AcquireFixtureCompensationSweep (ViSession instrumentHandle,
                                                         ViInt32 channel,
                                                         ViInt32 standardType,
                                                         ViInt32 arraySize,
                                                         ViInt32 _VI_FAR ports[]);
ViStatus _VI_FUNC rszvb_StartFixtureCompensationSweep (ViSession instrumentHandle,
                                                       ViInt32 channel);
ViStatus _VI_FUNC rszvb_SaveFixtureCompensationData (ViSession instrumentHandle,
                                                     ViInt32 channel);
ViStatus _VI_FUNC rszvb_SetFixtureCompensationAutoLengthAndLossCalculation
             (ViSession instrumentHandle, ViBoolean autoLengthAndLoss);
ViStatus _VI_FUNC rszvb_GetFixtureCompensationAutoLengthAndLossCalculation
             (ViSession instrumentHandle, ViBoolean* autoLengthAndLoss);
ViStatus _VI_FUNC rszvb_SetFixtureCompensationDirectCompensation
             (ViSession instrumentHandle, ViBoolean directCompensation);
ViStatus _VI_FUNC rszvb_GetFixtureCompensationDirectCompensation
             (ViSession instrumentHandle, ViBoolean* directCompensation);
ViStatus _VI_FUNC rszvb_DiagramAreaAdd (ViSession instrumentHandle, ViInt32 window);
ViStatus _VI_FUNC rszvb_DiagramAreaDelete (ViSession instrumentHandle,
                                           ViInt32 window);
ViStatus _VI_FUNC rszvb_DiagramAreaMaximize (ViSession instrumentHandle,
                                             ViInt32 window, ViInt32 diagramArea);
ViStatus _VI_FUNC rszvb_DiagramAreaTitle (ViSession instrumentHandle,
                                          ViInt32 window, ViBoolean title,
                                          ViString titleString);
ViStatus _VI_FUNC rszvb_DiagramAreaName (ViSession instrumentHandle, ViInt32 window,
                                         ViString areaName);
ViStatus _VI_FUNC rszvb_DiagramAreaCatalog (ViSession instrumentHandle,
                                            ViInt32 window,
                                            ViChar _VI_FAR catalog[],
                                            ViInt32 bufferSize);
ViStatus _VI_FUNC rszvb_TraceDiagramAreaCatalog (ViSession instrumentHandle,
                                                 ViInt32 window,
                                                 ViChar _VI_FAR catalog[],
                                                 ViInt32 bufferSize);
ViStatus _VI_FUNC rszvb_SetColorScheme (ViSession instrumentHandle,
                                        ViInt32 colorScheme);
ViStatus _VI_FUNC rszvb_GetColorScheme (ViSession instrumentHandle,
                                        ViInt32* colorScheme);
ViStatus _VI_FUNC rszvb_SaveColorScheme (ViSession instrumentHandle,
                                         ViString fileName);
ViStatus _VI_FUNC rszvb_LoadColorScheme (ViSession instrumentHandle,
                                         ViString fileName);
ViStatus _VI_FUNC rszvb_SetFrequencyInfo (ViSession instrumentHandle,
                                          ViBoolean frequencyInfo);
ViStatus _VI_FUNC rszvb_GetFrequencyInfo (ViSession instrumentHandle,
                                          ViBoolean* frequencyInfo);
ViStatus _VI_FUNC rszvb_SetFontSize (ViSession instrumentHandle, ViInt32 fontSize);
ViStatus _VI_FUNC rszvb_GetFontSize (ViSession instrumentHandle, ViInt32* fontSize);
ViStatus _VI_FUNC rszvb_SetChannelInfo (ViSession instrumentHandle,
                                        ViBoolean channelInfo);
ViStatus _VI_FUNC rszvb_GetChannelInfo (ViSession instrumentHandle,
                                        ViBoolean* channelInfo);
ViStatus _VI_FUNC rszvb_SetMarkerColorState (ViSession instrumentHandle,
                                             ViBoolean sameColor);
ViStatus _VI_FUNC rszvb_GetMarkerColorState (ViSession instrumentHandle,
                                             ViBoolean* sameColor);
ViStatus _VI_FUNC rszvb_SetRGBColor (ViSession instrumentHandle, ViInt32 element,
                                     ViReal64 red, ViReal64 green, ViReal64 blue,
                                     ViInt32 traceStyle, ViInt32 traceWidth);
ViStatus _VI_FUNC rszvb_GetRGBColor (ViSession instrumentHandle, ViInt32 element,
                                     ViReal64* red, ViReal64* green, ViReal64* blue,
                                     ViInt32* traceStyle, ViInt32* traceWidth);
ViStatus _VI_FUNC rszvb_SetTraceColorState (ViSession instrumentHandle,
                                            ViBoolean traceColor);
ViStatus _VI_FUNC rszvb_GetTraceColorState (ViSession instrumentHandle,
                                            ViBoolean* traceColor);
ViStatus _VI_FUNC rszvb_TraceSetRGBColor (ViSession instrumentHandle,
                                          ViString traceName, ViReal64 red,
                                          ViReal64 green, ViReal64 blue,
                                          ViInt32 traceStyle, ViInt32 traceWidth);
ViStatus _VI_FUNC rszvb_TraceGetRGBColor (ViSession instrumentHandle,
                                          ViString traceName, ViReal64* red,
                                          ViReal64* green, ViReal64* blue,
                                          ViInt32* traceStyle, ViInt32* traceWidth);
ViStatus _VI_FUNC rszvb_SetPowerPortLimitState (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViBoolean limitState);
ViStatus _VI_FUNC rszvb_GetPowerPortLimitState (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViBoolean* limitState);
ViStatus _VI_FUNC rszvb_SetPowerPortLimitValue (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViReal64 limitValue);
ViStatus _VI_FUNC rszvb_GetPowerPortLimitValue (ViSession instrumentHandle,
                                                ViInt32 channel, ViInt32 port,
                                                ViReal64* limitValue);
ViStatus _VI_FUNC rszvb_SetPowerPortLimitDirectGeneratorAndReceiverState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 port,
              ViBoolean DRGAccessState);
ViStatus _VI_FUNC rszvb_GetPowerPortLimitDirectGeneratorAndReceiverState
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 port,
              ViBoolean* DRGAccessState);
ViStatus _VI_FUNC rszvb_SetPresets (ViSession instrumentHandle,
                                    ViInt32 presetScope);
ViStatus _VI_FUNC rszvb_GetPresets (ViSession instrumentHandle,
                                    ViInt32* presetScope);
ViStatus _VI_FUNC rszvb_SetPresetSettingsState (ViSession instrumentHandle,
                                                ViBoolean state);
ViStatus _VI_FUNC rszvb_GetPresetSettingsState (ViSession instrumentHandle,
                                                ViBoolean* state);
ViStatus _VI_FUNC rszvb_SetUserDefinedPresetState (ViSession instrumentHandle,
                                                   ViBoolean userDefinedPreset);
ViStatus _VI_FUNC rszvb_GetUserDefinedPresetState (ViSession instrumentHandle,
                                                   ViBoolean* userDefinedPreset);
ViStatus _VI_FUNC rszvb_SetUserDefinedPresetFile (ViSession instrumentHandle,
                                                  ViString userDefinedPresetFile);
ViStatus _VI_FUNC rszvb_GetUserDefinedPresetFile (ViSession instrumentHandle,
                                                  ViInt32 bufferSize,
                                                  ViChar _VI_FAR userDefinedPresetFile[]);
ViStatus _VI_FUNC rszvb_SetDisplayUpdate (ViSession instrumentHandle,
                                          ViInt32 displayUpdate);
ViStatus _VI_FUNC rszvb_GetDisplayUpdate (ViSession instrumentHandle,
                                          ViInt32* displayUpdate);
ViStatus _VI_FUNC rszvb_ImmediateSettingsUpdate (ViSession instrumentHandle);
ViStatus _VI_FUNC rszvb_QueryFrequencyRange (ViSession instrumentHandle,
                                             ViReal64* minimumFrequency,
                                             ViReal64* maximumFrequency);
ViStatus _VI_FUNC rszvb_SystemKeylock (ViSession instrumentHandle,
                                       ViBoolean lockout);
ViStatus _VI_FUNC rszvb_SetRemoteLanguage (ViSession instrumentHandle,
                                           ViInt32 language);
ViStatus _VI_FUNC rszvb_GetRemoteLanguage (ViSession instrumentHandle,
                                           ViInt32* language);
ViStatus _VI_FUNC rszvb_ConfigureExternalGenerator (ViSession instrumentHandle,
                                                    ViInt32 generatorNumber,
                                                    ViString generatorName,
                                                    ViString generatorType,
                                                    ViString interfaceType,
                                                    ViString interfaceAddress,
                                                    ViBoolean fastSweepMode,
                                                    ViBoolean _10MHzReferenceFrequency);
ViStatus _VI_FUNC rszvb_QueryExternalGenerator (ViSession instrumentHandle,
                                                ViInt32 generatorNumber,
                                                ViChar _VI_FAR generatorName[],
                                                ViChar _VI_FAR generatorType[],
                                                ViChar _VI_FAR interfaceType[],
                                                ViChar _VI_FAR interfaceAddress[],
                                                ViBoolean* fastSweepMode,
                                                ViBoolean* _10MHzReferenceFrequency);
ViStatus _VI_FUNC rszvb_QueryExternalGeneratorCount (ViSession instrumentHandle,
                                                     ViInt32* generatorCount);
ViStatus _VI_FUNC rszvb_QueryExternalGeneratorNumbers (ViSession instrumentHandle,
                                                       ViInt32 arraySize,
                                                       ViChar _VI_FAR generatorNumbers[]);
ViStatus _VI_FUNC rszvb_DeleteExternalGenerator (ViSession instrumentHandle);
ViStatus _VI_FUNC rszvb_ConfigureExternalPowerMeter (ViSession instrumentHandle,
                                                     ViInt32 powerMeterNumber,
                                                     ViString powerMeterName,
                                                     ViString powerMeterType,
                                                     ViString interfaceType,
                                                     ViString interfaceAddress);
ViStatus _VI_FUNC rszvb_QueryExternalPowerMeter (ViSession instrumentHandle,
                                                 ViInt32 powerMeterNumber,
                                                 ViChar _VI_FAR powerMeterName[],
                                                 ViChar _VI_FAR powerMeterType[],
                                                 ViChar _VI_FAR interfaceType[],
                                                 ViChar _VI_FAR interfaceAddress[]);
ViStatus _VI_FUNC rszvb_QueryExternalPowerMeterCount (ViSession instrumentHandle,
                                                      ViInt32* powerMeterCount);
ViStatus _VI_FUNC rszvb_QueryExternalPowerMeterNumbers (ViSession instrumentHandle,
                                                        ViInt32 bufferSize,
                                                        ViChar _VI_FAR powerMeterNumber[]);
ViStatus _VI_FUNC rszvb_AutoZeroingExternalPowerMeter (ViSession instrumentHandle,
                                                       ViInt32 powerMeterNumber);
ViStatus _VI_FUNC rszvb_SetAutoConfigNRPZxx (ViSession instrumentHandle,
                                             ViInt32 powerMeterNumber,
                                             ViBoolean autoConfig);
ViStatus _VI_FUNC rszvb_GetAutoConfigNRPZxx (ViSession instrumentHandle,
                                             ViInt32 powerMeterNumber,
                                             ViBoolean* autoConfig);
ViStatus _VI_FUNC rszvb_DeleteExternalPowerMeter (ViSession instrumentHandle);
ViStatus _VI_FUNC rszvb_SetAlarmSoundsState (ViSession instrumentHandle,
                                             ViBoolean alarmSounds);
ViStatus _VI_FUNC rszvb_GetAlarmSoundsState (ViSession instrumentHandle,
                                             ViBoolean* alarmSounds);
ViStatus _VI_FUNC rszvb_SetRestartBehavior (ViSession instrumentHandle,
                                            ViInt32 restartBehavior);
ViStatus _VI_FUNC rszvb_GetRestartBehavior (ViSession instrumentHandle,
                                            ViInt32* restartBehavior);
ViStatus _VI_FUNC rszvb_SetStatusSoundsState (ViSession instrumentHandle,
                                              ViBoolean statusSounds);
ViStatus _VI_FUNC rszvb_GetStatusSoundsState (ViSession instrumentHandle,
                                              ViBoolean* statusSounds);
ViStatus _VI_FUNC rszvb_SetDataTransfer (ViSession instrumentHandle,
                                         ViInt32 dataTransfer);
ViStatus _VI_FUNC rszvb_GetDataTransfer (ViSession instrumentHandle,
                                         ViInt32* dataTransfer);
ViStatus _VI_FUNC rszvb_SetErrorDisplayState (ViSession instrumentHandle,
                                              ViBoolean errorDisplay);
ViStatus _VI_FUNC rszvb_GetErrorDisplayState (ViSession instrumentHandle,
                                              ViBoolean* errorDisplay);
ViStatus _VI_FUNC rszvb_SetFrequencyConversionType (ViSession instrumentHandle,
                                                    ViString converterType);
ViStatus _VI_FUNC rszvb_GetFrequencyConversionType (ViSession instrumentHandle,
                                                    ViInt32 bufferSize,
                                                    ViChar _VI_FAR converterType[]);
ViStatus _VI_FUNC rszvb_SetFrequencyConversionSource (ViSession instrumentHandle,
                                                      ViInt32 conversionSource);
ViStatus _VI_FUNC rszvb_GetFrequencyConversionSource (ViSession instrumentHandle,
                                                      ViInt32* conversionSource);
ViStatus _VI_FUNC rszvb_SetFastMultiportCorrection (ViSession instrumentHandle,
                                                    ViBoolean fastMultiportCorrection);
ViStatus _VI_FUNC rszvb_GetFastMultiportCorrection (ViSession instrumentHandle,
                                                    ViBoolean* fastMultiportCorrection);
ViStatus _VI_FUNC rszvb_SetPowerCoeficients (ViSession instrumentHandle,
                                             ViInt32 port,
                                             ViReal64 _VI_FAR coeficient[]);
ViStatus _VI_FUNC rszvb_GetPowerCoeficients (ViSession instrumentHandle,
                                             ViInt32 port,
                                             ViReal64 _VI_FAR coeficients[]);
ViStatus _VI_FUNC rszvb_SetPowerCoeficientsDefault (ViSession instrumentHandle,
                                                    ViBoolean defaultCoeficients);
ViStatus _VI_FUNC rszvb_GetPowerCoeficientsDefault (ViSession instrumentHandle,
                                                    ViBoolean* defaultCoeficients);
ViStatus _VI_FUNC rszvb_QueryExtensionUnitDeviceID (ViSession instrumentHandle,
                                                    ViInt32 bufferSize,
                                                    ViChar _VI_FAR deviceID[]);
ViStatus _VI_FUNC rszvb_QueryExtensionUnitHardwareOptions
             (ViSession instrumentHandle, ViInt32 bufferSize,
              ViChar _VI_FAR options[]);
ViStatus _VI_FUNC rszvb_SetNWAApplicationPriority (ViSession instrumentHandle,
                                                   ViInt32 priority);
ViStatus _VI_FUNC rszvb_GetNWAApplicationPriority (ViSession instrumentHandle,
                                                   ViInt32* priority);
ViStatus _VI_FUNC rszvb_SystemShutdown (ViSession instrumentHandle);
ViStatus _VI_FUNC rszvb_GenerateSystemReport (ViSession instrumentHandle,
                                              ViString fileName);
ViStatus _VI_FUNC rszvb_SetCalculationOfBandfilterCenterFrequency
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 marker,
              ViInt32 centerFrequencyCalculation);
ViStatus _VI_FUNC rszvb_GetCalculationOfBandfilterCenterFrequency
             (ViSession instrumentHandle, ViInt32 channel, ViInt32 marker,
              ViInt32* centerFrequencyCalculation);
ViStatus _VI_FUNC rszvb_SetRFOffBehavior (ViSession instrumentHandle,
                                          ViInt32 RFOffBehavior);
ViStatus _VI_FUNC rszvb_GetRFOffBehavior (ViSession instrumentHandle,
                                          ViInt32* RFOffBehavior);
ViStatus _VI_FUNC rszvb_SetRemoteDisplayTitle (ViSession instrumentHandle,
                                               ViString title);
ViStatus _VI_FUNC rszvb_GetRemoteDisplayTitle (ViSession instrumentHandle,
                                               ViInt32 bufferSize,
                                               ViChar _VI_FAR title[]);
ViStatus _VI_FUNC rszvb_SetAnalyzerHostname (ViSession instrumentHandle,
                                             ViString hostName);
ViStatus _VI_FUNC rszvb_GetAnalyzerHostname (ViSession instrumentHandle,
                                             ViInt32 bufferSize,
                                             ViChar _VI_FAR hostName[]);
ViStatus _VI_FUNC rszvb_SetSoftKeyLabel (ViSession instrumentHandle,
                                         ViInt32 keyNumber, ViString label);
ViStatus _VI_FUNC rszvb_GetPressedSoftKey (ViSession instrumentHandle,
                                           ViInt32* keyNumber, ViInt32 bufferSize,
                                           ViChar _VI_FAR label[]);
ViStatus _VI_FUNC rszvb_SetOutputPortBits (ViSession instrumentHandle,
                                           ViInt32 outputPort, ViInt32 portBits);
ViStatus _VI_FUNC rszvb_GetOutputPortBits (ViSession instrumentHandle,
                                           ViInt32 outputPort, ViInt32* portBits);
ViStatus _VI_FUNC rszvb_SetChannelBits (ViSession instrumentHandle,
                                        ViInt32 channelBits);
ViStatus _VI_FUNC rszvb_GetChannelBits (ViSession instrumentHandle,
                                        ViInt32* channelBits);
ViStatus _VI_FUNC rszvb_SetUIDirection (ViSession instrumentHandle, ViInt32 port,
                                        ViInt32 direction);
ViStatus _VI_FUNC rszvb_GetUIDirection (ViSession instrumentHandle, ViInt32 port,
                                        ViInt32* direction);
ViStatus _VI_FUNC rszvb_SetUIData (ViSession instrumentHandle, ViInt32 port,
                                   ViInt32 data);
ViStatus _VI_FUNC rszvb_GetUIData (ViSession instrumentHandle, ViInt32 port,
                                   ViInt32* data);
ViStatus _VI_FUNC rszvb_SetUISignalPin20 (ViSession instrumentHandle,
                                          ViBoolean pin20);
ViStatus _VI_FUNC rszvb_GetUISignalPin20 (ViSession instrumentHandle,
                                          ViBoolean* pin20);
ViStatus _VI_FUNC rszvb_SetUISignalPin21 (ViSession instrumentHandle,
                                          ViBoolean pin21);
ViStatus _VI_FUNC rszvb_GetUISignalPin21 (ViSession instrumentHandle,
                                          ViBoolean* pin21);
ViStatus _VI_FUNC rszvb_SetUIPortBinaryData (ViSession instrumentHandle,
                                             ViInt32 port, ViInt32 data);
ViStatus _VI_FUNC rszvb_GetUIPortBinaryData (ViSession instrumentHandle,
                                             ViInt32 port, ViInt32* data);
ViStatus _VI_FUNC rszvb_SetUIPortNextState (ViSession instrumentHandle,
                                            ViInt32 port, ViInt32 nextState);
ViStatus _VI_FUNC rszvb_GetUIPortNextState (ViSession instrumentHandle,
                                            ViInt32 port, ViInt32* nextState);
ViStatus _VI_FUNC rszvb_RestoreUIDefaultStates (ViSession instrumentHandle);
ViStatus _VI_FUNC rszvb_setStatusRegister (ViSession instrumentHandle,
                                           ViInt32 registerOperation,
                                           ViInt32 questionableRegister,
                                           ViInt32 enable, ViInt32 PTransition,
                                           ViInt32 NTransition);
ViStatus _VI_FUNC rszvb_getStatusRegister (ViSession instrumentHandle,
                                           ViInt32 statusRegistersQuery,
                                           ViInt32* registerValue);
ViStatus _VI_FUNC rszvb_setTimeOut (ViSession instrumentHandle, ViInt32 timeout);
ViStatus _VI_FUNC rszvb_getTimeOut (ViSession instrumentHandle, ViInt32* timeout);
ViStatus _VI_FUNC rszvb_errorCheckState (ViSession instrumentHandle,
                                         ViBoolean stateChecking);
ViStatus _VI_FUNC rszvb_setCheckOption (ViSession instrumentHandle,
                                        ViBoolean optionChecking);
ViStatus _VI_FUNC rszvb_setCheckRange (ViSession instrumentHandle,
                                       ViBoolean rangeChecking);
ViStatus _VI_FUNC rszvb_writeInstrData (ViSession instrumentHandle,
                                        ViString writeBuffer);
ViStatus _VI_FUNC rszvb_readInstrData (ViSession instrumentHandle,
                                       ViInt32 numberBytesToRead,
                                       ViChar _VI_FAR readBuffer[],
                                       ViInt32* numBytesRead);
ViStatus _VI_FUNC rszvb_reset (ViSession instrumentHandle);
ViStatus _VI_FUNC rszvb_self_test (ViSession instrumentHandle,
                                   ViInt16* selfTestResult,
                                   ViChar _VI_FAR selfTestMessage[]);
ViStatus _VI_FUNC rszvb_error_query (ViSession instrumentHandle, ViInt32* errorCode,
                                     ViChar _VI_FAR errorMessage[]);
ViStatus _VI_FUNC rszvb_error_message (ViSession instrumentHandle,
                                       ViStatus statusCode,
                                       ViChar _VI_FAR message[]);
ViStatus _VI_FUNC rszvb_revision_query (ViSession instrumentHandle,
                                        ViChar _VI_FAR instrumentDriverRevision[],
                                        ViChar _VI_FAR firmwareRevision[]);
ViStatus _VI_FUNC rszvb_close (ViSession instrumentHandle);

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif

/*****************************************************************************/
/*=== END INCLUDE FILE ======================================================*/
/*****************************************************************************/

#endif
