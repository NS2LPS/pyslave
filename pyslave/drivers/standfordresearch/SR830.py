"""Filename: srs830.py

Original author: Steven Casagrande (stevencasagrande@gmail.com)
2012

This work is released under the Creative Commons Attribution-Sharealike 3.0 license.
See http://creativecommons.org/licenses/by-sa/3.0/ or the included license/LICENSE.TXT file for more information.

Attribution requirements can be found in license/ATTRIBUTION.TXT"""

# VISA resource manager
try:
    from pyslave.instruments import __visa_rm__
except:
    __visa_rm__ = None

if __visa_rm__ is None:
    try:
        import pyvisa as visa
        __visa_rm__ = visa.ResourceManager()
    except:
        __visa_rm__ = None



class SR830:
    """StandfordResearch SR830 instrument driver.
    Direct call to the instrument invokes the outp method.
    """
    __inst_id__ = 'Stanford_Research_Systems SR830'
    __inst_type__ = 'lockin'
    def __init__(self, resource, *args, **kwargs):
        self.instrument = __visa_rm__.open_resource(resource, *args, **kwargs)
        self.write('OUTX 1') # Set the device responce port to GPIB
        self.__class__.__call__ = self.__class__.outp

    # Set Frequency Source
    def setFreqSource(self,source):
        """Function sets the frequency source to either the internal reference clock, or an external reference.

        :param source: {EXTernal|INTernal}
        :type source: string
        
        SCPI : FREQ source
        """
        if not isinstance(source,str):
            raise Exception('Parameter must be a string.')

        source = source.lower()

        valid1 = ['ext','int']
        valid2 = ['external','internal']
        if source in valid1:
            source = valid1.index(source)
        elif source in valid2:
            source = valid2.index(source)
        else:
            raise Exception('Only "external" and "internal" are valid freq sources.')

        self.write( 'FREQ ' + str(source) )

    # Set Frequency
    def setFreq(self,freq):
        """Function sets the internal reference frequency. This command only
        works if the lock-in is set to use the internal reference.

        :param freq: Desired frequency. Rounded to 5 digits or 0.0001Hz, whichever is larger.
        :type freq: float
        
        SCPI : FREQ freq
        """
        if not isinstance(freq,int) and not isinstance(freq,float):
            raise Exception('Freq parameter must be an integer or a float.')

        # Ensure that lock-in is not set to external freq ref
        if( int(self.query('FMOD?')) == 0 ):
            raise Exception('SRS830 set to external freq source, cannot change internal freq.')

        self.write( 'FREQ ' + str(freq) )

    # Set Phase
    def setPhase(self,phase):
        """
        Function sets the phase of the internal reference signal.

        :param phase: Desired phase
        :type phase: <-360...+729.99>, float
        
        SCPI : PHAS phase
        """
        if not isinstance(phase,int) and not isinstance(phase,float):
            raise Exception('Phase parameter must be an integer or a float.')

        if ( (phase >= 730) or (phase < -360) ):
            raise Exception('Phase must be -360 <= phase < +730 .')

        self.write( 'PHAS ' + str(phase) )

    # Set Amplitude
    def setAmplitude(self,amplitude):
        """
        Function sets the amplitude of the internal reference signal.

        :param amplitude: Desired peak-to-peak voltage
        :type amplitude: <0.004...5>,float

        SCPI : SLVL amplitude
        """
        if not isinstance(amplitude,int) and not isinstance(amplitude,float):
            raise Exception('Amplitude parameter must be an integer or a float.')

        if ( (amplitude > 5) or (amplitude < 0.004) ):
            raise Exception('Amplitude must be +0.004 <= amplitude <= +5 .')

        self.write( 'SLVL ' + str(amplitude) )

    # Set Input Shield Grounding
    def setInputGround(self,grounding):
        """
        Function sets the input shield grounding to either 'float' or 'ground'
        
        :param grounding: Desired input shield grounding
        :type grounding: {float|ground},string
        
        SCPI : IGND grounding
        """
        if not isinstance(grounding,str):
            raise Exception('Parameter "grounding" must be a string.')

        grounding = grounding.lower()

        valid = ['float','ground']
        if grounding in valid:
            grounding = str( valid.index(grounding) )
        else:
            raise Exception('Only "float" and "ground" are valid grounding input ground settings.')

        self.write( 'IGND ' + grounding )

    # Set Input Coupling
    def setInputCoupling(self,coupling):
        """
        Function sets the input coupling to either 'ac' or 'dc'

        :param coupling: Desired input coupling mode
        :type coupling: {ac|dc},string
        
        SCPI : ICPL coupling
        """
        if not isinstance(coupling,str):
            raise Exception('Parameter "coupling" must be a string.')

        coupling = coupling.lower()

        valid = ['ac','dc']
        if coupling in valid:
            coupling = str( valid.index(coupling) )
        else:
            raise Exception('Only "ac" and "dc" are valid input coupling settings.')

        self.write( 'ICPL ' + coupling )

    # Set Data Sample Rate
    def setSampleRate(self,sampleRate):
        """
        Function sets the data sampling rate of the lock-in

        :param sampleRate: The sampling rate, in Hz as a float, or the string 'trigger'. When specifying the rate in Hz, acceptable values are integer powers of 2. This means 2^n, n={-4...+9}
        :type sampleRate: {<freq> float,TRIGGER}
        
        SCPI : SRAT sampleRate
        """
        if isinstance(sampleRate,str):
            sampleRate = sampleRate.lower()

        valid = [0.0625,0.125,0.25,0.5,1,2,4,8,16,32,64,128,256,512,'trigger']
        if sampleRate in valid:
            sampleRate = str( valid.index(sampleRate) )
        else:
            raise Exception('Data sample rate parameter can only  be 2^n, n={-4..+9} or "trigger".')

        self.write( 'SRAT ' + sampleRate )

    # Set End of Buffer Mode
    def setEndOfBufferMode(self,mode):
        """
        Function sets the end of buffer mode

        :param mode: Desired end of buffer mode
        :type mode: {1SHOT,LOOP},string
        
        SCPI : SEND mode
        """
        if not isinstance(mode,str):
            raise Exception('Parameter "mode" must be a string.')

        mode = mode.lower()
        valid = ['1shot','loop']

        if mode in valid:
            mode = str( valid.index(mode) )
        else:
            raise Exception('Only "1shot" and "loop" are valid end of buffer modes.')

        self.write( 'SEND ' + mode )

    # Set Channel Display
    def setChannelDisplay(self,channel,display,ratio):
        """
        Function sets the display of the two channels.
        Channel 1 can display X, R, X Noise, Aux In 1, Aux In 2
        Channel 2 can display Y, Theta, Y Noise, Aux In 3, Aux In 4

        Channel 1 can have ratio of None, Aux In 1, Aux In 2
        Channel 2 can have ratio of None, Aux In 3, Aux In 4

        :param channel: {CH1|CH2|1|2},string/int
        :param display: {X|Y|R|THETA|XNOISE|YNOISE|AUX1|AUX2|AUX3|AUX4},string
        :param ratio: {NONE|AUX1|AUX2|AUX3|AUX4},string
        
        SCPI : DDEF channel, display, ratio
        """
        if not isinstance(channel,str) and not isinstance(channel,int):
            raise Exception('Parameter "channel" must be a string or integer.')
        if not isinstance(display,str):
            raise Exception('Parameter "display" must be a string.')
        if not isinstance(ratio,str):
            raise Exception('Parameter "ratio" must be a string.')

        if type(channel) == type(str()):
            channel = channel.lower()
        display = display.lower()
        ratio = ratio.lower()

        if channel == 'ch1' or channel == '1' or channel == 1:
            channel = '1'
            valid = ['x','r','xnoise','aux1','aux2']
            if display in valid:
                display = str( valid.index(display) )
            else:
                raise Exception('Only "x" , "r" , "xnoise" , "aux1" and "aux2" are valid displays for channel 1.')

            valid = ['none','aux1','aux2']
            if ratio in valid:
                ratio = str( valid.index(ratio) )
            else:
                raise Exception('Only "none" , "aux1" and "aux2" are valid ratios for channel 1.')

        elif channel == 'ch2' or channel == '2' or channel == 2:
            channel = '2'
            valid = ['y','theta','ynoise','aux3','aux4']
            if display in valid:
                display = str( valid.index(display) )
            else:
                raise Exception('Only "y" , "theta" , "ynoise" , "aux3" and "aux4" are valid displays for channel 2.')

            valid = ['none','aux3','aux4']
            if ratio in valid:
                ratio = str( valid.index(ratio) )
            else:
                raise Exception('Only "none" , "aux3" and "aux4" are valid ratios for channel 2.')

        else:
            raise Exception('Only "ch1" and "ch2" are valid channels.')

        self.write( 'DDEF %s,%s,%s' % (channel,display,ratio) )

    # Set the Channel Offset and Expand
    def setOffsetExpand(self,mode,offset,expand):
        """
        Function sets the channel offset and expand parameters.
        Offset is a percentage, and expand is given as a multiplication
        factor of 1, 10, or 100.

        :param mode: The channel mode that you wish to change.
        :type mode: {X|Y|R},sting
        :param offset: Offset of the mode, given as a percent
        :type offset: <-105...+105>,float
        :param expand: Expansion factor for the measurement
        :type expand: {1|10|100},integer
        
        SCPI : OEXP mode,offset,expand
        """
        if not isinstance(mode,str):
            raise Exception('Parameter "mode" must be a string.')

        mode = mode.lower()

        valid = ['x','y','r']
        if mode in valid:
            mode = valid.index(mode) + 1
        else:
            raise Exception('Only "x" , "y" and "r" are valid modes for setting the offset & expand.')

        if type(offset) != type(int()) or type(offset) != type(float()):
            raise Exception('Offset parameter must be an integer or a float.')
        if type(expand) != type(int()) or type(expand) != type(float()):
            raise Exception('Expand parameter must be an integer or a float.')

        if offset > 105 or offset < -105:
            raise Exception('Offset mustbe -105 <= offset <= +105 .')

        valid = [1,10,100]
        if expand in valid:
            expand = valid.index(expand)
        else:
            raise Exception('Expand must be 1, 10, 100.')

        self.write( 'OEXP %s,%s,%s' % (mode,offset,expand) )

    # Enable Auto Offset
    def autoOffset(self,mode):
        """
        Function sets a specific channel mode to auto offset. This is the
        same as pressing the auto offset key on the display.
        It sets the offset of the mode specified to zero.

        :param mode: Mode who's offset will be set to zero.
        :type mode: {X|Y|R},string
        
        SCPI : AOFF mode
        """
        if not isinstance(mode,str):
            raise Exception('Parameter "mode" must be a string.')

        mode = mode.lower()

        valid = ['x','y','r']
        if mode in valid:
            mode = str( valid.index(mode) + 1 )
        else:
            raise Exception('Only "x" , "y" and "r" are valid modes for setting the auto offset.')

        self.write( 'AOFF ' + mode )

    # Enable Auto Phase
    def autoPhase(self):
        """
        Function sets the lock-in to auto phase.
        This does the same thing as pushing the auto phase button.
        Do not send this message again without waiting the correct amount
        of time for the lock-in to finish.
        
        SCPI : APHS
        """
        self.write('APHS')

    # Set Data Transfer on/off
    def dataTransfer(self,mode):
        """
        Function used to turn the data transfer from the lockin on or off

        :param mode: {ON|OFF},string
        
        SCPI : FAST mode
        """
        if not isinstance(mode,str):
            raise Exception('Parameter "mode" must be a string.')

        mode = mode.lower()

        if mode == 'off':
            mode = '0'
        elif mode == 'on':
            mode = '2'
        else:
            raise Exception('Only "on" and "off" are valid parameters for setDataTransfer.')

        self.write( 'FAST ' + mode )

    # Start Scan
    def startScan(self):
        '''
        After setting the data transfer on via the dataTransfer function,
        this is used to start the scan. The scan starts after a delay of
        0.5 seconds.
        
        SCPI : STRD
        '''
        self.write('STRD')

    # Pause Data Capture
    def pause(self):
        '''
        Has the instrument pause data capture.
        
        SCPI : PAUS
        '''
        self.write('PAUS')

    # Start Data Transfer (wrapper)
    def init(self,sampleRate,EoBMode):
        '''
        Wrapper function to prepare the srs830 for measurement.
        Sets both the data sampling rate and the end of buffer mode

        :param sampleRate: The sampling rate in Hz, or the string "trigger". When specifying the rate in Hz, acceptable values are integer powers of 2. This means 2^n, n={-4...+9}.
        :type sampleRate: {<freq>|TRIGGER}
        :param EoBMode: {1SHOT|LOOP},string
        '''
        self.clearDataBuffer()
        self.setSampleRate(sampleRate)
        self.setEndOfBufferMode(EoBMode)

    # Take Data Snapshot (wrapper)
    def startDataTransfer(self):
        '''
        Wrapper function to start the actual data transfer.
        Sets the transfer mode to FAST2, and triggers the data transfer
        to start after a delay of 0.5 seconds.
        '''
        self.dataTransfer('on')
        self.startScan()

    def dataSnap(self,mode1,mode2):
        '''
        Function takes a snapshot of the current parameters are defined
        by variables mode1 and mode2.
        For combinations (X,Y) and (R,THETA) , they are taken at the same
        instant. All other combinations are done sequentially, and may
        not represent values taken from the same timestamp.

        Returns a list of floats, arranged in the order that they are
        given in the function input parameters.

        :param mode: {X|Y|R|THETA|AUX1|AUX2|AUX3|AUX4|REF|CH1|CH2},string
        
        SCPI : SNAP? mode1,mode2
        '''
        if not isinstance(mode1,str):
            raise Exception('Parameter "mode1" must be a string.')
        if not isinstance(mode2,str):
            raise Exception('Parameter "mode2" must be a string.')

        mode1 = mode1.lower()
        mode2 = mode2.lower()

        if mode1 == mode2:
            raise Exception('Both parameters for teh data snapshot are the same.')

        valid = ['x','y','r','theta','aux1','aux2','aux3','aux4','ref','ch1','ch2']
        if mode1 in valid:
            mode1 = valid.index(mode1) + 1
        else:
            raise Exception('Only "x" , "y" , "r" , "theta" , "aux1" , "aux2" , "aux3" , "aux4" , "ref" , "ch1" and "ch2" are valid snapshot parameters.')

        if mode2 in valid:
            mode2 = valid.index(mode2) + 1
        else:
            raise Exception('Only "x" , "y" , "r" , "theta" , "aux1" , "aux2" , "aux3" , "aux4" , "ref" , "ch1" and "ch2" are valid snapshot parameters.')

        result = self.query( 'SNAP? %s,%s' % (mode1,mode2) )
        return list(map( float, result.split(',') ))

    def outp(self, mode='x'):
        '''
        Read one value. Mode can x, y, r, or theta.
        
        SCPI : OUTP? mode
        '''
        valid = ['x','y','r','theta']
        if mode in valid:
            mode = valid.index(mode) + 1
        else:
            raise Exception('Only "x" , "y" , "r" , "theta" are valid parameters.')
        result = self.query( 'OUTP? %s' % (mode) )
        return float(result)

    def outr(self, mode='ch1'):
        '''
        Read one value. Mode can be ch1 or ch2.
        
        SCPI : OUTR? mode
        '''
        valid = ['ch1','ch2']
        if mode in valid:
            mode = valid.index(mode) + 1
        else:
            raise Exception('Only "ch1" , "ch2" are valid parameters.')
        result = self.query( 'OUTR? %s' % (mode) )
        return float(result)

    def auxv(self, voltage, aux=1):
        '''Set auxiliary output voltage.
        
        SCPI : AUXVaux,voltage'''
        self.write('AUXV{0},{1}'.format(aux, voltage))

    def oaux(self, aux=1):
        '''Read auxiliary input.
        
        SCPI : OAUX?aux'''
        return float(self.query('OAUX?{0}'.format(aux)))

    # Read Data Buffer
    def readDataBuffer(self,channel):
        '''
        Function reads the entire data buffer for a specific channel.
        Transfer is done in ASCII mode. Although binary would be faster,
        I haven't yet figured out how to get that to work.

        Returns a list of floats containing instrument's measurements.

        :param channel: Channel data buffer to read from
        :type channel: {CH1|CH2|1|2},string/integer
        
        SCPI : TRCA?channel,0,
        '''
        if not isinstance(channel,str) and not isinstance(channel,int):
            raise Exception('Parameter "channel" must be a string or an integer.')

        if isinstance(channel,str):
            channel = channel.lower()

        if channel == 'ch1' or channel == '1' or channel == 1:
            channel = 1
        elif channel == 'ch2' or channel == '2' or channel == 2:
            channel = 2
        else:
            raise Exception('Only "ch1" and "ch2" are valid channels.')

        N = self.numDataPoints() - 1 # Retrieve number of data points stored

        # Query device for entire buffer, returning in ASCII, then
        # converting to an array of doubles before returning to the
        # calling method
        return     map( float, self.query( 'TRCA?%s,0,%s' % (channel,N) ).split(',') )

    # Check number of data sets in buffer
    def numDataPoints(self):
        '''
        Function checks number of data sets in SRS830 buffer.
        Returns an integer.
        '''
        return int( self.query('SPTS?') )

    # Clear data (channel) buffer
    def clearDataBuffer(self):
        '''
        Clears the data buffer of the SRS830.
        '''
        self.write('REST')

    def write(self, str):
        self.instrument.write(str)

    def query(self, str):
        return self.instrument.query(str)

    def close(self):
        self.instrument.close()
