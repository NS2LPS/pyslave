import numpy as np

class rszvb:
    """Common class for R&S ZVA,ZVB and ZND network analyzers
    """
    def SetStartFrequency(self, startFrequency, channel=1):
        """This function defines the start frequency for a frequency sweep which
        is equal to the left edge of a Cartesian diagram.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:STARt

        :param startFrequency: This control defines the start frequency for a frequency sweep which is equal to the left edge of a Cartesian diagram.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:FREQ:STAR {startFrequency}")

    def GetStartFrequency(self, channel=1):
        """This function queries the start frequency for a frequency sweep which
        is equal to the left edge of a Cartesian diagram.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:STARt?

        :param channel: Channel number, defaults to 1
        :return: startFrequency"""
        return float(self.query(f"SENS{channel}:FREQ:STAR?"))

    def SetStopFrequency(self, stopFrequency, channel=1):
        """This function defines the stop frequency for a frequency sweep which
        is equal to the right edge of a Cartesian diagram.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:STOP 

        :param stopFrequency: This control defines the stop frequency for afrequency sweep which is equal to the right edge of a Cartesiandiagram.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:FREQ:STOP {stopFrequency}")

    def GetStopFrequency(self, channel=1):
        """This function queries the stop frequency for a frequency sweep which
        is equal to the right edge of a Cartesian diagram.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:STOP?

        :param channel: Channel number, defaults to 1
        :return: stopFrequency"""
        return float(self.query(f"SENS{channel}:FREQ:STOP?"))

    def SetCenterFrequency(self, centerFrequency, channel=1):
        """This function defines the center of the measurement and display range
        for a frequency sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CENTer 

        :param centerFrequency: This control defines the center of themeasurement and display range for a frequency sweep.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:FREQ:CEN {centerFrequency}")

    def GetCenterFrequency(self, channel=1):
        """This function queries the center of the measurement and display range
        for a frequency sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CENTer?    

        :param channel: Channel number, defaults to 1
        :return: centerFrequency"""
        return float(self.query(f"SENS{channel}:FREQ:CEN?"))

    def SetFrequencySpan(self, span, channel=1):
        """This function defines the width of the measurement and display range
        for a frequency sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:SPAN
        
        :param span: This control defines the width of the measurement anddisplay range for a frequency sweep.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:FREQ:SPAN {span}")

    def GetFrequencySpan(self, channel=1):
        """This function queries the width of the measurement and display range
        for a frequency sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:SPAN?   
        
        :param channel: Channel number, defaults to 1
        :return: span"""
        return float(self.query(f"SENS{channel}:FREQ:SPAN?"))

    def SetPower(self, power, channel=1):
        """This function defines the power of the internal signal source.
        
        Note(s):
        (1) The setting is valid for all sweep types except power sweep.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate][:AMPlitude]
        
        :param power: This control defines the power of the internal signalsource.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SOUR{channel}:POW {power}")

    def GetPower(self, channel=1):
        """This function queries the power of the internal signal source.
        
        Note(s):
        (1) The setting is valid for all sweep types except power sweep.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate][:AMPlitude]?

        :param channel: Channel number, defaults to 1
        :return: power"""
        return float(self.query(f"SOUR{channel}:POW?"))

    def SetCWFrequency(self, CWFrequency, channel=1):
        """This function defines the fixed (Continuous Wave, CW) frequency for
        all sweep types operating at fixed frequency (power sweep, time sweep,
        CW mode sweep).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CW

        :param channel: Channel number, defaults to 1
        :param CWFrequency: This control defines the fixed (Continuous Wave,CW) frequency for all sweep types operating at fixed frequency (powersweep, time sweep, CW mode sweep)."""
        self.write(f"SENS{channel}:FREQ:CW {CWFrequency}")

    def GetCWFrequency(self, channel=1):
        """This function queries the fixed (Continuous Wave, CW) frequency for
        all sweep types operating at fixed frequency (power sweep, time sweep,
        CW mode sweep).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CW?   

        :param channel: Channel number, defaults to 1
        :return: CWFrequency"""
        return float(self.query(f"SENS{channel}:FREQ:CW?"))

    def SetStartPower(self, startPower, channel=1):
        """This function defines the start power for a power sweep which is equal
        to the left edge of a Cartesian diagram.
        
        Note(s):
        (1) A power sweep must be active ([SENSe<Ch>:]SWEep:TYPE POWer) before this command can be used.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:STARt
        
        :param startPower: This control defines the start power for a powersweep which is equal to the left edge of a Cartesian diagram.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:POW:START {startPower}")

    def GetStartPower(self, channel=1):
        """This function queries the start power for a power sweep which is equal
        to the left edge of a Cartesian diagram.
        
        Note(s):
        (1) A power sweep must be active ([SENSe<Ch>:]SWEep:TYPE POWer) before this command can be used.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:STARt?
  
        :param channel: Channel number, defaults to 1
        :return: startPower"""
        self.write(f"SENS{channel}:FREQ:STOP {stopFrequency}")

    def SetStopPower(self, stopPower, channel=1):
        """This function defines the stop power for a power sweep which is equal
        to the right edge of a Cartesian diagram.
        
        Note(s):
        (1) A power sweep must be active ([SENSe<Ch>:]SWEep:TYPE POWer) before this command can be used.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:STOP

        :param stopPower: This control defines the stop power for a powersweep which is equal to the right edge of a Cartesian diagram.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:POW:STOP {stopPower}")

    def GetStopPower(self, channel=1):
        """This function queries the stop power for a power sweep which is equal
        to the right edge of a Cartesian diagram.
        
        Note(s):
        (1) A power sweep must be active ([SENSe<Ch>:]SWEep:TYPE POWer) before this command can be used.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:STOP?

        :param channel: Channel number, defaults to 1
        :return: stopPower"""
        return float(self.query(f"SOUR{channel}:POW:STOP?"))

    def SetRFState(self, RFState):
        """This function turns the internal source power at all ports on or off.
        
        Remote-control command(s):
        DIAGnostic:SERVice:RFPower

        :param RFState: This control turns the internal source power at all ports on or off."""
        self.write(f"DIAG:SERV:RFP {'ON' if RFState else 'OFF'}")

    def GetRFState(self):
        """This function queries the state of the internal source power at all
        ports.
        
        Remote-control command(s):
        DIAGnostic:SERVice:RFPower?

        :return: RFState"""
        return self.query(f"DIAG:SERV:RFP?").strip()

    def SetMeasBandwidth(self, measBandwidth, channel=1):
        """This function defines the resolution bandwidth of the analyzer.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth[:RESolution]

        :param measBandwidth: This control defines the resolution bandwidthof the analyzer (Meas. Bandwidth).
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:BAND {measBandwidth}")

    def GetMeasBandwidth(self, channel=1):
        """This function queries the resolution bandwidth of the analyzer.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth[:RESolution]?

        :param channel: Channel number, defaults to 1
        :return: measBandwidth"""
        return float(self.query(f"SENS{channel}:BAND?"))

    def SetMeasBandwidthSelectivity(self, measBandwidthSelectivity, channel=1):
        """This function defines the selectivity of the IF filter for an
        unsegmented sweep. The value is also used for all segments of a
        segmented sweep, provided that separate selectivity setting is
        disabled ([SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]:CONTrol OFF).
        
        Note(s):
        
        (1) This function can be used only with R&S ZVA and R&S ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:SELect NORMal | HIGH

        :param measBandwidthSelectivity: This control defines the selectivity of the IF filter for an unsegmented sweep.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:BAND:SEL {measBandwidthSelectivity}")

    def GetMeasBandwidthSelectivity(self, channel=1):
        """This function returns the selectivity of the IF filter for an
        unsegmented sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:SELect?"""
        return self.query(f"SENS{channel}:BAND:SEL?").strip()
    
    def SetAverageState(self, averageState, channel=1):
        """This function enables or disables the sweep average.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage[:STATe]
        
        :param averageState: This control enables or disables the sweepaverage.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:AVER {1 if averageState else 0}")

    def GetAverageState(self, channel=1):
        """This function queries the state of the sweep average.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage[:STATe]?

        :param channel: Channel number, defaults to 1
        :return: averageState """   
        return bool(self.query(f"SENS{channel}:AVER:STAT?"))      

    def SetAverageFactor(self, averageFactor, channel=1):
        """This function defines the number of consecutive sweeps to be combined
        for the sweep average.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage:COUNt

        :param averageFactor: This control defines the number of consecutivesweeps to be combined for the sweep average.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:AVER:COUN {averageFactor}")

    def GetAverageFactor(self, channel=1):
        """This function queries the number of consecutive sweeps to be combined
        for the sweep average.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage:COUNt?
        
        :param channel: Channel number, defaults to 1
        :return: averageFactor"""
        return int(self.query(f"SENS{channel}:AVER:COUN?"))   

    def GetCurrentSweep(self, channel=1):
        """Queries the number of the sweep which is currently measured. Use this
        command to monitor the progress of sweep averaging.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage:COUNt:CURRent?

        :param channel: Channel number, defaults to 1
        :return: currentSweep"""
        return int(self.query(f"SENS{channel}:AVER:CURR?"))   

    def RestartAverage(self, channel=1):
        """This function starts a new average cycle, clearing all previous
        results and thus eliminating their effect on the new cycle.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage:CLEar 

        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:AVER:CLE")

    def SetSweepType(self, sweepType, channel=1):
        """This function selects the sweep type, i.e. the sweep variable
        (frequency/power/time) and the position of the sweep points across the
        sweep range.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TYPE LINear | LOGarithmic | SEGMent | POWer | CW |
        POINt | PULSe | IAMPlitude | IPHase

        :param sweepType: This control selects the sweep type, i.e. the sweepvariable (frequency/power/time) and the position of the sweep pointsacross the sweep range.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:SWE:TYPE {sweepType}")

    def GetSweepType(self, channel=1):
        """This function queries the sweep type, i.e. the sweep variable
        (frequency/power/time) and the position of the sweep points across the
        sweep range.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TYPE?

        :param channel: Channel number, defaults to 1
        :return: sweepType"""
        return self.query(f"SENS{channel}:SWE:TYPE?").strip()   

    def TraceResponseData(self, channel=1):
        """This function reads the current response values of the active data
        trace or memory trace.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:DATA? SDAT

        :param channel: Channel number used to identify the active trace, defaults to 1
        :return: S data as complex values"""
        data = self.instrument.query_binary_values(f'CALC{channel}:DATA? SDAT',container=np.ndarray)
        return data.view(np.complex128)

    def TraceResponseSingleSweepData(self, sweepNumber, channel=1):
        """This function reads the response values of a trace acquired in single
        sweep mode (INITiate<Ch>:CONTinuous OFF).
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:DATA:NSWeep? SDATa,<sweepNumber>

        :param sweepNumber: Number of sweep to be read. 1 denotes the first sweep acquired, 2 denotes the second and so forth.
        :param channel: Channel number used to identify the active trace, defaults to 1
        :return: S data as complex values"""
        data = self.instrument.query_binary_values(f'CALC{channel}:DATA:NSW? SDAT,{sweepNumber}',container=np.ndarray)
        return data.view(np.complex128)

    def TraceResponseSingleSweepDataCount(self, channel=1):
        """This function reads the number of completed sweeps in single sweep
        mode (INITiate<Ch>:CONTinuous OFF). The trace can be any of the traces
        acquired during the single sweep cycle.
        
        Remote-control command(s):
        CALCulate<Chn>:DATA:NSWeep:COUNt?
        
        :param channel_Trace: Channel number used to identify the active trace.
        :return: sweepCount"""
        return int(self.query(f"CALC{channel}:DATA:NSW:COUN?"))   

    def TraceResponseSingleSweepDataForward(self, forwardCount, channel=1):
        """This function reads the response values of a trace acquired in single
        sweep mode (INITiate<Ch>:CONTinuous OFF).
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:DATA:NSWeep:FIRSt? SDATa,<forwardCount>
  
        :param forwardCount: Number of sweep to be read. 
        :param channel: Channel number used to identify the active trace, defaults to 1
        :return: S data as complex values"""
        data = self.instrument.query_binary_values(f'CALC{channel}:DATA:NSW:FIRS? SDAT,{forwardCount}',container=np.ndarray)
        return data.view(np.complex128)

    def SetSweepNumberOfPoints(self, numberOfPoints, channel=1):
        """This function defines the total number of measurement points per
        sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:POINts 

        :param channel: Channel number, defaults to 1
        :param numberOfPoints: This control defines the total number ofmeasurement points per sweep."""
        self.write(f"SENS{channel}:SWE:POIN {numberOfPoints}")

    def GetSweepNumberOfPoints(self, channel=1):
        """This function queries the total number of measurement points per
        sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:POINts?

        :param channel: Channel number, defaults to 1
        :return: numberOfPoints"""
        return int(self.query(f"SENS{channel}:SWE:POIN?"))   

    def SetFrequencyStepSize(self, stepSize, channel=1):
        """This function sets the distance between two consecutive sweep points.
        
        Note(s):
        
        (1) This setting is valid for sweep types with equidistant sweep
        points only. It does not apply to logarithmic and segmented sweeps.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:STEP <step_size>       

        :param stepSize: This control defines the stimulus step size.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:SWE:STEP {stepSize}")

    def GetFrequencyStepSize(self, channel=1):
        """This function gets the distance between two consecutive sweep points.
        
        Note(s):
        
        (1) This setting is valid for sweep types with equidistant sweep
        points only. It does not apply to logarithmic and segmented sweeps.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:STEP?      

        :param channel: Channel number, defaults to 1
        :return: stepSize"""
        return float(self.query(f"SENS{channel}:SWE:STEP?"))   

    def SetSweepCount(self, sweepCount, channel=1):
        """This function defines the number of sweeps to be measured in single
        sweep mode.
        
        Remote-control command(s):
        SENSe<Ch>:]SWEep:COUNt <No_of_Sweeps>

        :param channel: Channel number, defaults to 1
        :param sweepCount: Defines the number of consecutive sweeps to be measured."""
        self.write(f"SENS{channel}:SWE:COUN {sweepCount}")

    def GetSweepCount(self, channel=1):
        """This function returns the number of sweeps to be measured in single
        sweep mode.
        
        Remote-control command(s):
        SENSe<Ch>:]SWEep:COUNt?
        
        :param channel: Channel number, defaults to 1
        :return: sweepCount"""
        return int(self.query(f"SENS{channel}:SWE:COUN?"))   

    def ConfigureSweepTime(self, autoSweepTime, sweepTime, measDelay, channel=1):
        """This function sets the measurement time for a sweep or delay the start
        of each sweep.
        
        Note(s):
        
        The sweep duration is ignored for the sweep types Time and CW Mode.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TIME:AUTO <Boolean>
        [SENSe<Ch>:]SWEep:TIME <numeric_value>
        [SENSe<Ch>:]SWEep:DWELl <numeric_value>
        
        :param measDelay: Meas. delay sets a delay time allowing the DUT to settle before the hardware settings of the analyzer are changed and anew partial measurement is started.
        :param sweepTime: Sets the duration of the sweep (Sweep Time).
        :param autoSweepTime: When enabled, the (minimum) sweep duration iscalculated internally using the other channel settings and zero delay.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:SWE:TIME AUTO {1 if autoSweepTime else 0}")
        self.write(f"SENS{channel}:SWE:TIME {sweepTime}")
        self.write(f"SENS{channel}:SWE:DWEL {measDelay}")

    def SetSweepTime(self, sweepTime, channel=1):
        """This function sets the duration of the sweep (Sweep Time). Setting a
        duration disables the automatic calculation of the (minimum) sweep
        time; see [SENSe<Ch>:]SWEep:TIME:AUTO.
        
        Note(s):
        
        The sweep duration is ignored for the sweep types Time and CW Mode.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TIME <numeric_value>    

        :param sweepTime: Sets the duration of the sweep (Sweep Time).
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:SWE:TIME {sweepTime}")

    def GetSweepTime(self, channel=1):
        """This function returns the duration of the sweep (Sweep Time).
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TIME?
        
        :param channel: Channel number, defaults to 1
        :return: sweepTime"""
        return float(self.query(f"SENS{channel}:SWE:TIME?"))   

    def SetSweepMeasDelay(self, measDelay, channel=1):
        """This function defines the Meas. Delay time for each partial
        measurement. Setting a delay disables the automatic calculation of the
        (minimum) sweep time; see [SENSe<Ch>:]SWEep:TIME:AUTO.
        
        Note(s):
        
        The sweep duration is ignored for the sweep types Time and CW Mode.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:DWELl <numeric_value>
        
        :param measDelay: Meas. delay before each partial measurement.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:SWE:DWEL {measDelay}")

    def GetSweepMeasDelay(self, channel=1):
        """This function returns the Meas. Delay time for each partial
        measurement.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:DWELl?
        
        :param channel: Channel number, defaults to 1
        :return: measDelay"""
        return float(self.query(f"SENS{channel}:SWE:DWEL?"))   

    def SetSweepTimeAuto(self, autoSweepTime, channel=1):
        """This function when enabled, the (minimum) sweep duration is calculated
        internally using the other channel settings and zero delay
        ([SENSe<Ch>:]SWEep:DWELl).
        
        Note(s):
        
        The automatically calculated sweep duration is ignored for the sweep
        types Time and CW Mode.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TIME:AUTO <Boolean>

        :param autoSweepTime: When enabled, the (minimum) sweep duration iscalculated internally using the other channel settings and zero delay.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:SWE:TIME:AUTO {1 if autoSweepTime else 0}")

    def GetSweepTimeAuto(self, channel=1):
        """This function returns if the (minimum) sweep duration is calculated
        internally using the other channel settings and zero delay
        ([SENSe<Ch>:]SWEep:DWELl) or not.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TIME:AUTO?
        
        :param channel: Channel number, defaults to 1
        :return: autoSweepTime"""
        return bool(self.query(f"SENS{channel}:SWE:TIME:AUTO?"))   

    def ConfigureTriggerFreeRun(self, channel=1):
        """This function configures free run measurement without waiting for
        trigger events.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce IMMediate
        
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:SOUR IMM")

    def ConfigureTriggerExternal(self, triggerOn, channel=1):
        """This function configures the external trigger mode. In External
        trigger mode the measurement is triggered by a low-voltage (3.3 V)
        external TTL signal applied either to the BNC connector EXT TRIGGER or
        to pin 2 of the USER CONTROL connector at the rear panel. The two
        trigger inputs are equivalent; nor additional setting for signal
        routing is required.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce EXTernal
        TRIGger<Ch>[:SEQuence]:SLOPe POSitive | NEGative
        
        :param triggerOn: This control qualifies whether the trigger eventoccurs on the rising or on the falling edge of the external TTLtrigger signal.
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:SOUR EXT")
        self.write(f"TRIG{channel}:SLOP {triggerOn}")

    def ConfigureTriggerPeriodic(self, triggerPeriod, channel=1):
        """This function configures the periodic trigger mode. In Periodic
        trigger mode the measurement is triggered by the periodic signal of an
        internal clock generator.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce TIMer
        TRIGger<Ch>[:SEQuence]:TIMer
        
        :param triggerPeriod: This control sets the period of the internalperiodic signal that can be used as a trigger source.
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:SOUR TIM")
        self.write(f"TRIG{channel}:TIM {triggerPeriod}")

    def ConfigureTriggerRFPower(self, channel=1):
        """This function configures the RF Power trigger mode. In RF Power
        trigger mode the trigger signal is generated from one of the generated
        or measured RF signals.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce RFPower
        
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:SOUR RFP")

    def ConfigureTriggerManual(self, channel=1):
        """This function configures the manual trigger mode. In Manual trigger
        mode the trigger signal is generated on pressing the Manual Trigger
        softkey or sending *TRG remote command (function rszvb_SendTrigger).
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce MANual
        
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:SOUR MAN")

    def ConfigureTriggerSettings(self, triggerMeasSequence, triggerDelay, channel=1):
        """This function configures the trigger settings.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:LINK 'POINT' | 'SWEEP' | 'PPOINT' | 'SEGMENT'
        TRIGger<Ch>[:SEQuence]:HOLDoff

        :param triggerMeasSequence: This control selects the Triggered Meas.Sequence.
        :param channel: Channel number, defaults to 1
        :param triggerDelay: This control defines a delay time between the trigger event and the start of the measurement."""
        self.write(f"TRIG{channel}:LINK {triggerMeasSequence}")
        self.write(f"TRIG{channel}:HOLD {triggerDelay}")

    def SetTriggerSource(self, triggerSource, channel=1):
        """This function selects the source for the events that the analyzer uses
        to start a sweep.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce IMMediate | EXTernal | TIMer | MANual |
        RFPower | PGENerator
        
        :param triggerSource: This control selects the source for the eventsthat the analyzer uses to start a sweep.
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:SOUR {triggerSource}")

    def GetTriggerSource(self, channel=1):
        """This function queries selected source for the events that the analyzer
        uses to start a sweep.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce?    

        :param channel: Channel number, defaults to 1
        :return: triggerSource"""
        return self.query()

    def SetTriggerDelay(self, triggerDelay, channel=1):
        """This function defines a delay time between the trigger event and the
        start of the measurement.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff
        
        :param triggerDelay: This control defines a delay time between thetrigger event and the start of the measurement.
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:HOLD {triggerDelay}")

    def GetTriggerDelay(self, channel=1):
        """This function queries a delay time between the trigger event and the
        start of the measurement.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff?   

        :param channel: Channel number, defaults to 1
        :return: triggerDelay"""
        return float(self.query(f"TRIG{channel}:SEQ:HOLD?"))   

    def SetPartialMeasurementTriggerMode(self, triggerMode, channel=1):
        """Qualifies whether the trigger delay is valid for all physical ports
        (including external generator) or source port-specific. This setting
        is available if the triggered measurement sequence is a partial
        measurement.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff:MODE PALL | PSPecific 

        :param triggerMode: Qualifies whether the trigger delay is valid forall physical ports (including external generator) or source port-specific.
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:HOLD:MODE {triggerMode}")

    def GetPartialMeasurementTriggerMode(self, channel=1):
        """Queries whether the trigger delay is valid for all physical ports
        (including external generator) or source port-specific.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff:MODE?
        
        :param channel: Channel number, defaults to 1
        :return: triggerMode"""
        return self.query(f"TRIG{channel}:HOLD:MODE?").strip()   

    def SetTriggeredMeasSequence(self, triggerMeasSequence, channel=1):
        """This function selects the Triggered Meas. Sequence.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:LINK 'POINT' | 'SWEEP' | 'PPOINT' | 'SEGMENT'
        
        :param triggerMeasSequence: This control selects the Triggered Meas.Sequence.
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:LINK {triggerMeasSequence}")

    def GetTriggeredMeasSequence(self, channel=1):
        """This function queries selected Triggered Meas. Sequence.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:LINK?
        
        :param channel: Channel number, defaults to 1
        :return: triggerMeasSequence"""
        return self.query(f"TRIG{channel}:SEQ:LINK?").strip()

    def SetTriggerOn(self, triggerOn, channel=1):
        """This function qualifies whether the trigger event occurs on the rising
        or on the falling edge of the external TTL trigger signal.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SLOPe POSitive | NEGative

        :param triggerOn: This control qualifies whether the trigger eventoccurs on the rising or on the falling edge of the external TTLtrigger signal.
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:SLOP {triggerOn}")

    def GetTriggerOn(self, channel=1):
        """This function queries whether the trigger event occurs on the rising
        or on the falling edge of the external TTL trigger signal.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SLOPe?
        
        :param channel: Channel number, defaults to 1
        :return: triggerOn"""
        return self.query(f"TRIG{channel}:SEQ:SLOP?").strip() 

    def SetTriggerPeriod(self, triggerPeriod, channel=1):
        """This function sets the period of the internal periodic signal that can
        be used as a trigger source.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:TIMer    

        :param triggerPeriod: This control sets the period of the internalperiodic signal that can be used as a trigger source.
        :param channel: Channel number, defaults to 1"""
        self.write(f"TRIG{channel}:TIM {triggerPeriod}")

    def GetTriggerPeriod(self, channel=1):
        """This function queries the period of the internal periodic signal that
        can be used as a trigger source.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:TIMer?      

        :param channel: Channel number, defaults to 1
        :return: triggerPeriod"""
        return float(self.query(f"TRIG{channel}:SEQ:TIM?"))   

    def SendTrigger(self):
        """This function triggers all actions waiting for a trigger event.
        Generates a manual trigger signal (Manual Trigger).
        
        Remote-control command(s):
        *TRG
        """
        self.write("*TRG")

    def SendTriggerWaitOPC(self):
        """This function triggers all actions waiting for a trigger event in the
        selected window and waits for operation completed (OPC).
        
        Remote-control command(s):
        \*TRG;\*OPC?
        """
        self.write("*TRG")
        self.query("*OPC?")

    def WaitOPC(self):
        """This function waits for operation completed (OPC).
        
        Remote-control command(s):
        \*OPC?
        """
        self.query("*OPC?")
        
    def SendChannelTrigger(self, channel=1):
        """This function starts a new single sweep sequence. This function is
        available in single sweep mode only (INITiate<Ch>:CONTinuous OFF).
        
        Note(s):
        
        (1) In contrast to all other functions of the analyzer,
        INITiate<Ch>[:IMMediate] has been implemented to prevent overlapped
        execution.
        
        (2) The data of the last sweep can be read using
        CALCulate<Ch>:DATA:NSWeep? SDATa, <history_count>.
        
        Remote-control command(s):
        INITiate<Ch>[:IMMediate]

        :param channel: Channel number, defaults to 1"""
        self.write(f"INIT{channel}:IMM")

    def SendChannelTriggerWaitOPC(self, channel=1):
        """This function starts a new single sweep sequence and waits for
        operation completed (OPC) before returning the status code. This
        function is available in single sweep mode only
        (INITiate<Ch>:CONTinuous OFF).
        
        Note(s):
        
        (1) In contrast to all other functions of the analyzer,
        INITiate<Ch>[:IMMediate] has been implemented to prevent overlapped
        execution.
        
        (2) The data of the last sweep can be read using
        CALCulate<Ch>:DATA:NSWeep? SDATa, <history_count>.
        
        Remote-control command(s):
        INITiate<Ch>[:IMMediate];\*OPC?

        :param channel: Channel number, defaults to 1"""
        self.write(f"INIT{channel}:IMM")
        self.query("*OPC?")

    def SetSweepSingleAllChans(self, singleSweep):
        """This function selects the scope of the single sweep sequence.
        
        Note(s):
        
        (1) The setting is applied in single sweep mode only.
        
        Remote-control command(s):
        INITiate<Ch>[:IMMediate]:SCOPe ALL | SINGle
        
        :param singleSweep: This control selects the scopeof the single sweep sequence."""
        self.write(f"INIT{channel}:SCOP {singleSweep}")

    def GetSweepSingleAllChans(self, ):
        """This function queries the scope of the single sweep sequence.
        
        Remote-control command(s):
        INITiate<Ch>[:IMMediate]:SCOPe?

        :return: singleSweep"""
        return self.query(f"INIT{channel}:SCOP?").strip()   

    def SweepRestart(self, channel=1):
        """This function starts a new single sweep sequence.
        
        Note(s):
        
        (1) This function is available in single sweep mode only.
        
        Remote-control command(s):
        INITiate<Ch>[:IMMediate]

        :param channel: Channel number, defaults to 1"""
        self.write(f"INIT{channel}:IMM")

    def SetSweepSingle(self, singleSweep, channel=1):
        """This function qualifies whether the analyzer measures in single sweep
        or in continuous sweep mode.
        
        Remote-control command(s):
        INITiate<Ch>:CONTinuous OFF | ON
        
        :param channel: Channel number, defaults to 1
        :param singleSweep: This control qualifies whether the analyzermeasures in single sweep or in continuous sweep mode."""
        self.write(f"INIT{channel}:CONT {singleSweep}")

    def GetSweepSingle(self, channel=1):
        """This function queries whether the analyzer measures in single sweep or
        in continuous sweep mode.
        
        Remote-control command(s):
        INITiate<Ch>:CONTinuous?
        
        :param channel: Channel number, defaults to 1
        :return: singleSweep"""
        return bool(self.query(f"INIT{channel}:CONT?"))   

    def SetAlternateSweepMode(self, alternateSweepMode, channel=1):
        """This function activates normal or alternate sweep mode.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]COUPle ALL | NONE
        
        :param alternateSweepMode: This control activates normal or alternatesweep mode.
        :param channel: Channel number, defaults to 1"""
        self.write(f"SENS{channel}:COUPLE {alternateSweepMode}")


    def GetAlternateSweepMode(self, channel=1):
        """This function returns the state of the alternate sweep mode.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]COUPle?
        
        :param channel: Channel number, defaults to 1
        :return: alternateSweepMode"""
        return bool(self.query(f"SENS{channel}:COUP?"))   
   
    def SystemShutdown(self, ):
        """Switches the analyzer to the standby state.
        
        Remote-control command(s):
        SYSTem:SHUTdown"""
        self.write("SYST:SHUT")
        

#     def CreateTrace(self, traceName, parameter, channel=1):
#         """This function creates a trace and assigns a channel number, a name and
#         a measurement parameter to it. The trace
#         becomes the active trace in the channel but is not displayed.
        
#         Remote-control command(s):
#         CALCulate<Ch>:PARameter:SDEFine

#         :param parameter: Configures the measurement parameter.
#         :param traceName: Define trace name.
#         :param channel: Channel number, defaults to 1"""

#     def ConfigureMesurementParameters(self, traceName, parameter, channel=1):
#         """This function assigns a measurement parameter to an existing trace.
        
#         Remote-control command(s):
#         CALCulate<Ch>:PARameter:MEASure

#         :param parameter: Configures the measurement parameter Valid Values: not checked
#         :param traceName: Define trace name."""

#     def QueryMesurementParameters(self, traceName, bufferSize, parameters, channel=1):
#         """This function queries a measurement parameter of an existing trace.
        
#         Remote-control command(s):
#         CALCulate<Ch>:PARameter:MEASure? '<string>'

#         :param bufferSize: Defines the allocated size of Function Parameters.
#         :param parameters: Returns the defined measurementparameterSee see list of parameters in the CALCulate<Ch>:PARameter:SDEFinecommand description.
#         :param channel: Channel number, defaults to 1
#         :param traceName: Define trace name."""
        
#     def TraceAdd(self, traceName, channel=1):
#         """This function creates a new trace in the current diagram area and
#         assigns it to the selected channel. The new trace is created with the
#         default trace and channel settings. Trace is not displayed.
        
#         Remote-control command(s):
#         CALCulate<Ch>:PARameter:SDEFine '<string>', 'S21'"""

#     def TraceSelect(self, traceName, channel=1):
#         """This function selects an existing trace as the active trace of the
#         channel. All trace commands without explicit reference to the trace
#         name act on the active trace (e.g. CALCulate<Ch>:FORMat).
        
#         Remote-control command(s):
#         CALCulate<Ch>:PARameter:SELect '<string>'    

#         :param channel: Channel number, defaults to 1
#         :param traceName: Define trace name."""

#     def TraceDelete(self, traceName, channel=1):
#         """This function deletes a trace with a specified trace name and channel.
        
#         Remote-control command(s):
#         CALCulate<Ch>:PARameter:DELete '<string>'

#         :param channel: Channel number, defaults to 1
#         :param traceName: Define trace name."""

#     def TraceDeleteAll(self, channel=1):
#         """This function deletes all traces in specified channel.
        
#         Remote-control command(s):
#         CALCulate<Ch>:PARameter:DELete:CALL
        
#         :param channel: Channel number, defaults to 1"""

#     def TraceDeleteAllChannels(self):
#         """This function deletes all traces in all channels of the active setup,
#         including the default trace Trc1 in channel no. 1.
        
#         Remote-control command(s):
#         CALCulate<Ch>:PARameter:DELete:ALL"""

#     def TraceList(self, catalog, bufferSize, channel=1):
#         """This function returns the trace names and measurement parameters of
#         all traces assigned to a particular channel.
        
#         Remote-control command(s):
#         CALCulate<Ch>:PARameter:CATalog?

#         :param catalog: Response is a string parameter with comma-separatedlist of trace names and measurement parameters, e.g.'CH4TR1,S11,CH4TR2,S12'. The measurement parameters are returnedaccording to the naming convention of CALCulate<Ch>:PARameter:SDEFine.The order of traces in the list reflects their creation time: Theoldest trace is the first, the newest trace is the last trace in thelist.
#         :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.
#         :param channel: Channel number, defaults to 1"""

#     def TraceRename(self, oldTraceName, newTraceName):
#         """This function assigns a new name to a trace. The trace does not have
#         to be the active trace.
        
#         Remote-control command(s):
#         CONFigure:TRACe:REName '<old_trace_name>','<new_trace_name>'
        
#         :param oldTraceName: Define old trace name name.
#         :param newTraceName: Define new trace name."""

#     def ChannelTraceRename(self, traceName, channel=1):
#         """This function assigns a new name to the active trace in channel <ch>.
        
#         Remote-control command(s):
#         CONFigure:CHANnel<Ch>TRACe:REName '<trace_name>'

#         :param channel: Channel number, defaults to 1
#         :param traceName: Define new trace name."""

#     def TraceListCatalog(self, catalog, bufferSize):
#         """This function returns the numbers and names of all traces in the
#         current setup.
        
#         Remote-control command(s):
#         CONFigure:TRACe<Trc>:CATalog?
   
#         :param catalog: Returns string with comma-separated list of trace numbers and names. If all traces have beendeleted the response is an empty string ("").
#         :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter."""

#     def TraceGetTraceName(self, traceNumber, traceName):
#         """This function returns the trace <Trc> name.
        
#         Remote-control command(s):
#         CONFigure:TRACe<Trc>:NAME?
        
#         :param traceName: Returns the trace name.
#         :param traceNumber: Trace number."""

#     def TraceGetTraceNumber(self, traceName):
#         """This function returns the trace number (numeric suffix) of a trace
#         with known trace name.
        
#         Remote-control command(s):
#         CONFigure:TRACe:NAME:ID? '<Trc_name>'
        
#         :param traceName: Sets the trace name.
#         :return: traceNumber"""

#     def TraceGetChannelName(self, traceName, channelName):
#         """This function returns the channel name for an existing trace named
#         '<Trc_name>'.
        
#         Remote-control command(s):
#         CONFigure:TRACe:CHANnel:NAME? '<Trc_name>'

#         :param channelName: Returns the channel namefor an existing trace.
#         :param traceName: Sets the trace name."""

#     def TraceGetChannelNumber(self, traceName):
#         """This function returns channel number (numeric suffix) for an existing
#         trace named '<Trc_name>'.
        
#         Remote-control command(s):
#         CONFigure:TRACe:CHANnel:NAME:ID? '<Trc_name>'"""

#     def SetTimeDomainStartTime(self, startTime, channel=1):
#         """This function defines the start time of the diagram in time domain.
        
#         Remote-control command(s):
#         CALCulate<Ch/Tr>:TRANsform:TIME:STARt    

#         :param channel_Trace: Channel number used toidentify the active trace.
#         :param startTime: This control defines start time of the diagram in time domain."""

#     def GetTimeDomainStartTime(self, channel=1):
#         """This function queries the start time of the diagram in time domain.
        
#         Remote-control command(s):
#         CALCulate<Ch/Tr>:TRANsform:TIME:STARt?

#         :param channel_Trace: Channel number used toidentify the active trace.
#         :return: startTime"""

#     def SetTimeDomainStopTime(self, stopTime, channel=1):
#         """This function defines the stop time of the diagram in time domain.
        
#         Remote-control command(s):
#         CALCulate<Ch/Tr>:TRANsform:TIME:STOP
        
#         :param channel_Trace: Channel number used toidentify the active trace.
#         :param stopTime: This control defines stop time of the diagram intime domain."""

#     def GetTimeDomainStopTime(self, channel=1):
#         """This function queries the stop time of the diagram in time domain.
        
#         Remote-control command(s):
#         CALCulate<Ch/Tr>:TRANsform:TIME:STOP?
        
#         :param channel_Trace: Channel number used toidentify the active trace.
#         :return: stopTime"""

#     def SetTimeDomainCenterTime(self, centerTime, channel=1):
#         """This function defines the center time of the diagram in time domain.
        
#         Remote-control command(s):
#         CALCulate<Ch/Tr>:TRANsform:TIME:CENTer  

#         :param channel_Trace: Channel number used toidentify the active trace.
#         :param centerTime: This control defines center time of the diagram intime domain."""

#     def GetTimeDomainCenterTime(self, channel=1):
#         """This function queries the center time of the diagram in time domain.
        
#         Remote-control command(s):
#         CALCulate<Ch/Tr>:TRANsform:TIME:CENTer?  

#         :param channel_Trace: Channel number used toidentify the active trace.
#         :return: centerTime"""

#     def SetTimeDomainTimeSpan(self, timeSpan, channel=1):
#         """This function defines the time span of the diagram in time domain.
        
#         Remote-control command(s):
#         CALCulate<Ch/Tr>:TRANsform:TIME:SPAN

#         :param channel_Trace: Channel number used toidentify the active trace.
#         :param timeSpan: This control defines time span of the diagram intime domain."""

#     def GetTimeDomainTimeSpan(self, channel=1):
#         """This function queries the time span of the diagram in time domain.
        
#         Remote-control command(s):
#         CALCulate<Ch/Tr>:TRANsform:TIME:SPAN?

#         :param channel_Trace: Channel number used toidentify the active trace.
#         :return: timeSpan"""

#      def GetMarkerResponse(self, marker, markerResponse, channel=1):
#         """This function returns the response (in Cartesian diagrams: y-axis)
#         value of marker no. <Mk>. The marker must be created before using
#         CALCulate<Ch/Tr>:MARKer<Mk>[:STATe] ON.
        
#         Remote-control command(s):
#         CALCulate<Ch/Tr>:MARKer<Mk>:Y?
        
#         :param marker: Marker number.
#         :param markerResponse: Response value(s) of marker no. <Mk>. Unitis depending on the marker format; seeCALCulate<Ch/Tr>:MARKer<Mk>:FORMat.
#         :param channel_Trace: Channel number used toidentify the active trace."""

#     def GetReferenceMarkerResponse(self, marker, channel=1):
#         """This function returns the response (in Cartesian diagrams: y-axis)
#         value of the reference marker. The reference marker must be created
#         before using CALCulate<Ch/Tr>:MARKer<Mk>:REFerence[:STATe] ON.
        
#         Remote-control command(s):
#         CALCulate<Ch/Tr>:MARKer<Mk>:REFerence:Y?
        
#         :param marker: Marker number.
#         :param channel_Trace: Channel number used toidentify the active trace.
#         :return: referenceMarkerResponse"""

#     def InsertNewSegment(self, segment, startFrequency, stopFrequency, numberOfPoints, power, sweepTimeSelect, time, pointDelay, measBandwidth, channel=1):
#         """This function inserts a new sweep segment with specific channel
#         settings. The new segment must not overlap with any of the existing
#         segments.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:INSert
#         [SENSe<Ch>:]SEGMent<Seg>:INSert:SELect SWTime | DWELl
        
#         :param power: This control defines the power of the internal signalsource in segment.
#         :param measBandwidth: This control defines theresolution bandwidth of the analyzer (Meas. Bandwidth).
#         :param time: This control sets theduration of the sweep in sweep segment no. <Segment>. At the sametime, the command activates separate sweep time setting in all sweepsegments.
#         :param sweepTimeSelect: This control defines whether the sweep time ofa new segment, i.e. numeric parameter no. 9 of the function, isentered as a segment sweep time or as a meas. delay.
#         :param startFrequency:  control defines theStart frequency of sweep segment no. <Segment>.
#         :param numberOfPoints: This control defines thetotal number of measurement Points in sweep segment no. <Segment>.
#         :param pointDelay: This control definesthe delay time for each partial measurement in sweep segment no.<Segment>.
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :param stopFrequency: This control defines theStop frequency of sweep segment no. <Segment>."""

#     def RedefineSegment(self, segment, startFrequency, stopFrequency, numberOfPoints, power, sweepTimeSelect, time, pointDelay, measBandwidth, channel=1):
#         """This function re-defines a sweep segment with specific channel
#         settings (Insert New Segment). The segment replaces an existing
#         segment <Segment> in the segment list. The modified segment must not
#         overlap with any of the existing segments.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:DEFine
#         [SENSe<Ch>:]SEGMent<Seg>:INSert:SELect SWTime | DWELl

#         :param power: This control defines the power of the internal signalsource in segment.
#         :param measBandwidth: This control defines theresolution bandwidth of the analyzer (Meas. Bandwidth).
#         :param time: This control sets theduration of the sweep in sweep segment no. <Segment>. At the sametime, the command activates separate sweep time setting in all sweepsegments.
#         :param sweepTimeSelect: This control defines whether the sweep time ofa new segment, i.e. numeric parameter no. 9 of the function, isentered as a segment sweep time or as a meas. delay.
#         :param startFrequency: This control defines theStart frequency of sweep segment no. <Segment>.
#         :param numberOfPoints: This control defines thetotal number of measurement Points in sweep segment no. <Segment>.
#         :param pointDelay: This control definesthe delay time for each partial measurement in sweep segment no.<Segment>.
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :param stopFrequency: This control defines theStop frequency of sweep segment no. <Segment>."""

#     def AddNewSegment(self, segment, channel=1):
#         """This function inserts a new sweep segment using default channel
#         settings). The added segment covers the frequency interval between the
#         maximum frequency of the existing sweep segments and the stop
#         frequency of the entire sweep range.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:ADD
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1"""

#     def DeleteSelectedSegment(self, segment, channel=1):
#         """This function deletes the specified (single) sweep segment.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:DELete

#    :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#    :param channel: Channel number, defaults to 1"""

#     def DeleteAllSegments(self, channel=1):
#         """This function deletes all sweep segments in the channel.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent:DELete:ALL

#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentsCount(self, channel=1):
#         """This function queries the number of sweep segments in the channel
#         including all segments that are switched off.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:COUNt?   

#         :param channel: Channel number, defaults to 1
#         :return: count"""

#     def SetSweepSegmentState(self, segment, state, channel=1):
#         """This function activates or deactivates the sweep segment <Segment>.
#         Sweep points belonging to inactive segments only are not measured.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>[:STATe]

#         :param state: This control activates or deactivatesthe sweep segment <Segment>.
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentState(self, segment, channel=1):
#         """This function queries the state of the sweep segment <Segment>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>[:STATe]?

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: state"""

#     def SetSweepSegmentStartFrequency(self, segment, startFrequency, channel=1):
#         """This function defines the Start frequency of sweep segment no.
#         <Segment>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:FREQuency:STARt

#         :param startFrequency: This control defines theStart frequency of sweep segment no. <Segment>.
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentStartFrequency(self, segment, channel=1):
#         """This function queries the Start frequency of sweep segment no.<Segment>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:FREQuency:STARt?
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: startFrequency"""

#     def SetSweepSegmentStopFrequency(self, segment, stopFrequency, channel=1):
#         """This function defines the Stop frequency of sweep segment no.
#         <Segment>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:FREQuency:STOP     

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :param stopFrequency: This control defines the Stopfrequency of sweep segment no. <Segment>."""

#     def GetSweepSegmentStopFrequency(self, segment, channel=1):
#         """This function queries the Stop frequency of sweep segment no.
#         <Segment>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:FREQuency:STOP? 

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: stopFrequency"""

#     def SetSweepSegmentNumberOfPoints(self, segment, numberOfPoints, channel=1):
#         """This function defines the total number of measurement Points in sweep
#         segment no. <Segment>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:POINts
  
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :param numberOfPoints: This control defines the totalnumber of measurement Points in sweep segment no. <Segment>."""

#     def GetSweepSegmentNumberOfPoints(self, segment, channel=1):
#         """This function queries the total number of measurement Points in sweep
#         segment no. <Segment>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:POINts?
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: numberOfPoints"""

#     def SetSweepSegmentName(self, segment, name, channel=1):
#         """This function defines the Name of the sweep segment no. <Seg>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:NAME '<segment_name>'
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param name: This control defines the segment name.
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentName(self, segment, bufferSize, name, channel=1):
#         """This function returns the Name of the sweep segment no. <Seg>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:NAME?

#         :param bufferSize: This control defines the size ofarray passed to argument 'Name'.
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param name: This control returns the segment name.
#         :param channel: Channel number, defaults to 1"""

#     def SetSweepSegmentPower(self, segment, power, channel=1):
#         """This function defines the Power of the internal signal source in sweep
#         segment no. <Segment>. At the same time, the command activates
#         separate power control in all sweep segments.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:POWer[:LEVel]
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param power: This control defines the Power of theinternal signal source in sweep segment no. <Segment>.
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentPower(self, segment, channel=1):
#         """This function queries the Power of the internal signal source in sweep
#         segment no. <Segment>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:POWer[:LEVel]?
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: power"""

#     def SetSweepSegmentIndependentPower(self, segment, power, channel=1):
#         """This function defines whether or not the Power can be set
#         independently for each sweep segment.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:POWer[:LEVel]:CONTrol 

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param power: This control defines whether or notthe Power can be set independently for each sweep segment.
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentIndependentPower(self, segment, channel=1):
#         """This function queries whether or not the Power can be set
#         independently for each sweep segment.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:POWer[:LEVel]:CONTrol?

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: power"""

#     def SetSweepSegmentMeasBandwidth(self, segment, measBandwidth, channel=1)
#         """This function defines the resolution bandwidth of the analyzer in
#         sweep segment no. <Segment>. At the same time, the command activates
#         separate bandwidth setting in all sweep segments.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]

#         :param measBandwidth: This control defines theresolution bandwidth of the analyzer (Meas. Bandwidth).
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentMeasBandwidth(self, segment, channel=1):
#         """This function queries the resolution bandwidth of the analyzer in
#         sweep segment no. <Segment>. At the same time, the command activates
#         separate bandwidth setting in all sweep segments.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]?

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: measBandwidth"""

#     def SetSweepSegmentIndependentBandwidth(self, segment, measBandwidth, channel=1):
#         """This function defines whether or not the Meas. Bandwidth can be set
#         independently for each sweep segment.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]:CONTrol    

#         :param measBandwidth: This control defines whetheror not the Meas. Bandwidth can be set independently for each sweepsegment.
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentIndependentBandwidth(self, segment, channel=1):
#         """This function queries whether or not the Meas. Bandwidth can be set
#         independently for each sweep segment.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]:CONTrol?

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: measBandwidth"""

#     def SetSweepSegmentSweepTime(self, segment, time, channel=1):
#         """This function sets the duration of the sweep in sweep segment no.
#         <Segment>. At the same time, the command activates separate sweep time setting in all sweep segments.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME   

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :param time: This control sets the duration of thesweep in sweep segment no. <Segment>. At the same time, the commandactivates separate sweep time setting in all sweep segments."""

#     def GetSweepSegmentSweepTime(self, segment, channel=1):
#         """This function queries the duration of the sweep in sweep segment no.
#         <Segment>. At the same time, the command activates separate sweep time
#         setting in all sweep segments.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME?

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: time"""

#     def SetSweepSegmentIndependentTime(self, segment, time, channel=1):
#         """This function defines whether or not the Sweep Time can be set
#         independently for each sweep segment.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME:CONTrol

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :param time: This control defines whether or notthe Sweep Time can be set independently for each sweep segment."""

#     def GetSweepSegmentIndependentTime(self, segment, channel=1):
#         """This function queries whether or not the Sweep Time can be set
#         independently for each sweep segment.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME:CONTrol?

#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: time"""

#     def SetSweepSegmentPointDelay(self, segment, pointDelay, channel=1):
#         """This function defines the delay time for each partial measurement in
#         sweep segment no. <Segment>
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:DWELl

#         :param pointDelay: This control defines the delaytime for each partial measurement in sweep segment no. <Segment>.
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentPointDelay(self, segment, channel=1):
#         """This function queries the delay time for each partial measurement in
#         sweep segment no. <Segment>
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:DWELl?
 
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: pointDelay"""

#     def SetSweepSegmentIndependentPointDelay(self, segment, pointDelay, channel=1):
#         """This function defines whether or not the Point Delay can be set
#         independently for each sweep segment.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:DWELl:CONTrol

#         :param pointDelay: This control defines whether ornot the Point Delay can be set independently for each sweep segment.
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentIndependentPointDelay(self, segment, channel=1):
#         """This function queries whether or not the Point Delay can be set
#         independently for each sweep segment.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:DWELl:CONTrol?
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: pointDelay"""

#     def SetSweepSegmentTriggering(self, segment, triggering, channel=1):
#         """This function deactivates/activates triggering for segment <Seg>. This
#         setting only takes effect if:
        
#         1. The analyzer is not in Free Run mode (see rszvb_SetTriggerSource)
        
#         2. Selective segment triggering is enabled
#         (rszvb_SetSweepSelectiveSegmentTriggering set to ON)
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:TRIGger:STATe
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param triggering: This controldeactivates/activates triggering.
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSegmentTriggering(self, segment, channel=1):
#         """This function returns the state of the triggering for segment <Seg>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:TRIGger:STATe?
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: triggering"""

#     def SetSweepSelectiveSegmentTriggering(self, triggering, channel=1):
#         """This function enables/disables selective segment triggering (configured using rszvb_SetSweepSegmentTriggering).
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:TRIGger:CONTrol

#         :param triggering: This control enables/disables selective segmenttriggeringValid Values:VI_FALSE (0) - OffVI_TRUE (1) - On
#         :param channel: Channel number, defaults to 1"""

#     def GetSweepSelectiveSegmentTriggering(self, channel=1):
#         """This function returns the state of the selective segment triggering
#         (configured using rszvb_SetSweepSegmentTriggering).
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:TRIGger:CONTrol?
  
#         :param channel: Channel number, defaults to 1
#         :return: triggering"""

#     def GetSweepSegmentCenterFrequency(self, segment, channel=1):
#         """This function queries the center frequency of sweep segment no.
#         <Segment>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:FREQuency:CENTer?
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: centerFrequency"""

#     def GetSweepSegmentFrequencySpan(self, segment, channel=1):
#         """This function queries the width of the frequency range of sweep
#         segment no. <Segment>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:FREQuency:SPAN?
        
#         :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
#         :param channel: Channel number, defaults to 1
#         :return: frequencySpan"""

#     def QuerySumOfSweepSegmentsTime(self, channel=1):
#         """Returns the total duration of the segmented sweep, calculated as the
#         sum of the sweep times of the individual segments
#         ([SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME).
        
#         Remote-control command(s):
#         [SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME:SUM?      
        
#         :param channel: Channel number, defaults to 1
#         :return: sweepTime"""

#     def SetPulseTimeStart(self, timeStart, channel=1):
#         """This function sets the start time of the displayed time range relative
#         to the trigger time.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]PULSe:TIME:STARt <start>

#         :param timeStart: This control sets the start time of the displayedtime range relative to the trigger time.
#         :param channel: Channel number, defaults to 1"""

#     def GetPulseTimeStart(self, channel=1):
#         """This function gets the start time of the displayed time range relative
#         to the trigger time.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]PULSe:TIME:STARt?

#         :param channel: Channel number, defaults to 1
#         :return: timeStart"""

#     def SetPulseTimeStop(self, timeStop, channel=1):
#         """This function sets the stop time of the displayed time range relative
#         to the trigger time.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]PULSe:TIME:STOP <stop>
        
#         :param timeStop: This control sets the stop time of the displayedtime range relative to the trigger time.
#         :param channel: Channel number, defaults to 1"""

#     def GetPulseTimeStop(self, channel=1)
#         """This function gets the stop time of the displayed time range relative
#         to the trigger time.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]PULSe:TIME:STOP?   

#         :param channel: Channel number, defaults to 1
#         :return: timeStop"""

#     def SetPulseTimeBandwidth(self, timeBandwidth, channel=1):
#         """This function sets the IF bandwidth for pulse profile measurements.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]PULSe:TIME:BWIDth[:RESolution] <bandwidth>

#         :param channel: Channel number, defaults to 1
#         :param timeBandwidth: This control sets the IF bandwidth for pulseprofile measurements."""

#     def GetPulseTimeBandwidth(self, channel=1):
#         """This function gets the IF bandwidth for pulse profile measurements.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]PULSe:TIME:BWIDth[:RESolution]?  

#         :param channel: Channel number, defaults to 1
#         :return: timeBandwidth"""

#     def SetCorrectionState(self, correctionState, channel=1):
#         """This function enables or disables the system error correction for
#         channel <Ch>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection[:STATe] ON | OFF
        
#         :param correctionState: This control enables (ON) or disables (OFF)the correction.
#         :param channel: Channel number, defaults to 1"""

#     def GetCorrectionState(self, channel=1):
#         """This function returns the state of the system error correction for
#         channel <Ch>.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection[:STATe]?
        
#         :param channel: Channel number, defaults to 1
#         :return: correctionState"""

#     def ResetOffsets(self, channel=1):
#         """This function resets the offset parameters for all test ports to zero.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:OFFSet<port_no>:STATe OFF
        
#         :param channel: Channel number, defaults to 1"""

#     def QueryResetOffsets(self, channel=1):
#         """This function queries whether any of the offset parameters are
#         different from zero.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:OFFSet<port_no>:STATe?
        
#         :param channel: Channel number, defaults to 1
#         :return: offsets"""

#     def SetElectricalLength(self, port, electricalLength, channel=1):
#         """This function defines the offset parameter for test port <Port> as an
#         electrical length.
        
#         Note(s):
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:EDELay<port_no>:ELENgth
        
#         :param electricalLength: This control defines the offset parameterfor test port <Port> as an electrical length.
#         :param port: Port number of the analyzer.
#         :param channel: Channel number, defaults to 1"""

#     def GetElectricalLength(self, port, channel=1):
#         """This function queries the offset parameter for test port <Port> as an
#         electrical length.
        
#         Note(s):
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:EDELay<port_no>:ELENgth?
    
#         :param port: Port number of the analyzer.
#         :param channel: Channel number, defaults to 1
#         :return: electricalLength"""

#     def ConfigureMechanicalLength(self, port, mechanicalLength, permittivity, channel=1):
#         """This function configures parameters of mechanical length.
        
#         Note(s):
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:EDELay<port_no>:DISTance
#         [SENSe<Ch>:]CORRection:EDELay<port_no>:DIELectric
        
#         :param permittivity: This control defines thepermittivity for the offset correction at test port <Port>.
#         :param port: Port number of the analyzer.
#         :param channel: Channel number, defaults to 1
#         :param mechanicalLength: This control defines the offset parameterfor test port <Port> as a mechanical length."""

#     def SetMechanicalLength(self, port, mechanicalLength, channel=1):
#         """This function defines the offset parameter for test port <Port> as a
#         mechanical length.
        
#         Note(s):
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:EDELay<port_no>:DISTance

#         :param port: Port number of the analyzer.
#         :param channel: Channel number, defaults to 1
#         :param mechanicalLength: This control defines the offset parameterfor test port <Port> as a mechanical length."""

#     def GetMechanicalLength(self, port, channel=1):
#         """This function queries the offset parameter for test port <Port> as a
#         mechanical length.
        
#         Note(s):
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:EDELay<port_no>:DISTance? 

#         :param port: Port number of the analyzer.
#         :param channel: Channel number, defaults to 1
#         :return: mechanicalLength"""

#     def SetPermittivity(self, port, permittivity, channel=1):
#         """This function defines the permittivity for the offset correction at
#         test port <Port>.
        
#         Note(s):
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:EDELay<port_no>:DIELectric
        
#         :param port: Port number of the analyzer.
#         :param channel: Channel number, defaults to 1
#         :param permittivity: This control defines the permittivity for theoffset correction at test port <Port>."""

#     def GetPermittivity(self, port, channel=1):
#         """This function returns the permittivity for the offset correction at
#         test port <Port>.
        
#         Note(s):
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:EDELay<port_no>:DIELectric? 

#         :param port: Port number of the analyzer.
#         :param channel: Channel number, defaults to 1
#         :return: permittivity"""

#     def ConfigureLoss(self, port, lossAtDC, lossAtFrequency, lossReferenceFrequency, channel=1):
#         """This function configures parameters of One-way Loss.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:LOSS<port_no> <DC_loss>
#         [SENSe<Ch>:]CORRection:LOSS<port_no>:OFFSet <ref_loss>
#         [SENSe<Ch>:]CORRection:LOSS<port_no>:FREQuency <ref_frequency>    

#         :param lossReferenceFrequency: This control defines the reference frequency.
#         :param lossAtDC: This control defines the frequency-independent part(DC value) of the offset loss.
#         :param lossAtFrequency: This control defines the offset loss at the reference frequency.
#         :param port: Port number of the analyzer.
#         :param channel: Channel number of the offset-corrected channel."""

#     def SetLossAtDC(self, port, lossAtDC, channel=1):
#         """This function defines the frequency-independent part (DC value) of the
#         offset loss.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:LOSS<port_no> <DC_loss>

#         :param lossAtDC: This control defines the frequency-independent part(DC value) of the offset loss.
#         :param port: Port number of the analyzer.
#         :param channel: Channel number of the offset-corrected channel."""

#     def GetLossAtDC(self, port, channel=1):
#         """This function returns the frequency-independent part (DC value) of the
#         offset loss.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:LOSS<port_no>?
        
#         :param port: Port number of the analyzer.
#         :param channel: Channel number of the offset-corrected channel.
#         :return: lossAtDC"""

#     def SetLossAtFrequency(self, port, lossAtFrequency, channel=1):
#         """This function defines the offset loss at the reference frequency
#         ([SENSe<Ch>:]CORRection:LOSS<port_no>:FREQuency).
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:LOSS<port_no>:OFFSet <ref_loss>
        
#         :param lossAtFrequency: This control defines the offset loss at thereference frequency.
#         :param port: Port number of the analyzer.
#         :param channel: Channel number of the offset-corrected channel."""

#     def GetLossAtFrequency(self, port, channel=1):
#         """This function returns the offset loss at the reference frequency
#         ([SENSe<Ch>:]CORRection:LOSS<port_no>:FREQuency).
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:LOSS<port_no>:OFFSet?
        
#         :param port: Port number of the analyzer.
#         :param channel: Channel number of the offset-corrected channel.
#         :return: lossAtFrequency"""

#     def SetLossReferenceFrequency(self, port, lossReferenceFrequency, channel=1):
#         """This function defines the reference frequency for the frequency-
#         dependent part of the offset loss
#         ([SENSe<Ch>:]CORRection:LOSS<port_no>:OFFSet).
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:LOSS<port_no>:FREQuency <ref_frequency>     

#         :param lossReferenceFrequency: This control defines the referencefrequency.
#         :param port: Port number of the analyzer.
#         :param channel: Channel number of the offset-corrected channel."""

#     def GetLossReferenceFrequency(self, port, channel=1):
#         """This function returns the reference frequency for the frequency-
#         dependent part of the offset loss
#         ([SENSe<Ch>:]CORRection:LOSS<port_no>:OFFSet).
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:LOSS<port_no>:FREQuency?   

#         :param port: Port number of the analyzer.
#         :param channel: Channel number of the offset-corrected channel.
#         :return: lossReferenceFrequency"""

#     def SetDelay(self, port, delay, channel=1):
#         """This function defines the offset parameter for test port <Port> as a
#         delay time.
        
#         Note(s):
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:EDELay<port_no>[:TIME]
        
#         :param delay: This control defines the offset parameter for test port <Port> as a delay time.
#         :param port: Port number of the analyzer.
#         :param channel: Channel number, defaults to 1"""

#     def GetDelay(self, port, channel=1):
#         """This function queries the offset parameter for test port <Port> as a
#         delay time.
        
#         Note(s):
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:EDELay<port_no>[:TIME]? 

#         :param port: Port number of the analyzer.
#         :param channel: Channel number, defaults to 1
#         :return: delay"""

#     def QueryDirectFixtureCompensation(self, port, channel=1):
#         """Returns whether a direct fixture compensation has been carried out at
#         port no. <port_no>. A direct fixture compensation resets the offset
#         parameters to zero, the analyzer uses calculated transmission factors
#         instead.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:OFFSet<port_no>:DFComp[:STATe]?
        
#         :param port: Port number.
#         :param channel: Channel number, defaults to 1
#         :return: directFixtureCompensation"""

#     def AutoLength(self, port, channel=1):
#         """This function defines the offset parameter for the active test port such that the residual delay of the active trace is minimized across
#         the entire sweep range.
        
#         Note(s):
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:EDELay<port_no>:AUTO ONCE
        
#         :param port: Port number of the analyzer.
#         :param channel: Channel number, defaults to 1"""

#     def AutoLengthAndLoss(self, port, channel=1):
#         """This function determines all offset parameters such that the residual
#         group delay of the active trace (defined as the negative derivative of
#         the phase response) is minimized and the measured loss is minimized as
#         far as possible across the entire sweep range.
        
#         Remote-control command(s):
#         [SENSe<Ch>:]CORRection:LOSS<port_no>:AUTO ONCE
        
#         :param port: Port number of the analyzer.
#         :param channel: Channel number of the offset-corrected channel."""


