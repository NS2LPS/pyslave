.. method:: ApplicationExample(self, channel=1, startFrequency, stopFrequency, power, stimulusData, responseData)
           
        This is an simple example of how to use instrument driver functions to
        run S21-parameter measurement is separate test set.
        
        Following functions are performed:
        
        - Window New (rszvb_WindowNew)
        - Trace Add (rszvb_TraceAdd)
        - Trace Assign Diagram Area (rszvb_TraceAssignDiagramArea)
        - Set Sweep Number Of Points (rszvb_SetSweepNumberOfPoints)
        - Set Sweep Single (rszvb_SetSweepSingle)
        - Set Sweep Count (rszvb_SetSweepCount)
        - Set Sweep Type (rszvb_SetSweepType)
        - Set Start Frequency (rszvb_SetStartFrequency)
        - Set Stop Frequency (rszvb_SetStopFrequency)
        - Set Power (rszvb_SetPower)
        - Select S-Parameters (rszvb_SelectSParameters)
        - Set Trace Format (rszvb_SetTraceFormat)
        - Send Channel Trigger and Wait for OPC
        (SendChannelTriggerWaitOPC)
        - Trace Autoscale (rszvb_TraceAutoscale)
        - Trace Stimulus Data (rszvb_TraceStimulusData)
        - Trace Response Data (rszvb_TraceResponseData)
        - Window Close (rszvb_WindowClose)
        
        Note:
        
        When this function stops the execution, active test setup is closed
        (device display do not show measurement result).
        
        
        

   :param responseData: Returns array of the current response valuesof the active data trace or memory trace.
   :param power: This control defines the power of the internal signalsource.
   :param startFrequency: This control defines the start frequency for afrequency sweep which is equal to the left edge of a Cartesiandiagram.
   :param stimulusData: Returns array of the current stimnulus valuesof the active data trace or memory trace.
   :param channel: Channel number.
   :param stopFrequency: This control defines the stop frequency for afrequency sweep which is equal to the right edge of a Cartesiandiagram.
   :return: noOfValues

.. method:: WindowNew(self, setupName)
           
        This function creates a new setup <setup_name> using default settings
        for the traces, channels and diagram areas. The created setup becomes
        the active setup.
        
        Remote-control command(s):
        MEMory:DEFine '<setup_name>'
        
        

   :param setupName: String parameter to specify thename of the created setup.

.. method:: WindowSelect(self, setupName)
           
        This function selects a setup as the active setup.
        
        Remote-control command(s):
        MEMory:SELect '<setup_name>'
        
        

   :param setupName: String parameter to specify thesetup.

.. method:: WindowClose(self, setupName)
           
        This function closes the specified setup. If <Setup Name> is not
        specified (NULL), all existing setups are closed.
        
        Remote-control command(s):
        MEMory:DELete:ALL
        MEMory:DELete[:NAME] '<file_name>'
        
        

   :param setupName: String parameter to specify thename of the setup to be closed.

.. method:: WindowList(self, catalog, bufferSize)
           
        This function returns the names of all loaded setups.
        
        Remote-control command(s):
        MEMory:CATalog?
        
        

   :param catalog: This indicator returns the namesof all loaded setups as comma separated strings, for example:
   :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.

.. method:: Print(self, printerName)
           
        This function prints the active setup on selected printer.
        
        Note(s):
        
        Use Standard Windows Print dialog box to, specify the range of pages
        to be printed, the number of copies, the destination printer, and
        other printer setup options.
        
        Remote-control command(s):
        HCOPy:DESTination <string>
        HCOPy[:IMMediate]
        
        

   :param printerName: Define printer name, stringvariable. One of the printers accessible from your instrument.

.. method:: PrinttoFile(self, fileName, fileFormat, diagramArea, logo, dateAndTime, markerList)
           
        This function specify how the screen contents are stored to a file.
        
        Defines a name for a file which can be used to store the printer
        output. The file is created when it is selected as a printer
        destination (HCOPy:DESTination 'MMEM').
        
        Remote-control command(s):
        MMEMory:NAME '<file_name>'
        HCOPy:DESTination 'MMEM'
        HCOPy:ITEM:ALL
        HCOPy:MITem:LOGO[:STATe] <Boolean>
        HCOPy:ITEM:MLISt[:STATe] <Boolean>
        HCOPy:MITem:TIME[:STATe] <Boolean>
        HCOPy:MPAGe:WINDow ALL | ACTive | SINGle
        HCOPy:DEVice:LANGuage EMF | EWMF | BMP | PNG | JPG
        HCOPy[:IMMediate]
        
        

   :param dateAndTime: Qualifies whether or not the printed outputcontains the current date and time.
   :param markerList: Qualifies whether or not the printed outputcontains the information in the marker info field (marker list).
   :param fileName: Specifies a file name to savethe screen contents.
   :param diagramArea: Defines the number of diagram areas per printedpage.
   :param logo: Qualifies whether or not the printed output containsthe logo. The default R&S logo (file Logo.gif) is stored in theResources\Images subdirectory of the NWA program directory and can bereplaced by another logo.
   :param fileFormat: Selects a file format for printer files. Selectingthe format is recommended to ensure that the file defined viaMMEMory:NAME can be read or imported by an external application.

.. method:: PrintSetup(self, diagramArea, logo, dateAndTime, markerList, pageOrientation, leftMargin, rightMargin, topMargin, bottomMargin)
           
        This function Provides options to specify how the document should be
        printed.
        
        Remote-control command(s):
        HCOPy:ITEM:ALL
        HCOPy:ITEM:LOGO[:STATe] <Boolean>
        HCOPy:ITEM:MLISt[:STATe] <Boolean>
        HCOPy:ITEM:TIME[:STATe] <Boolean>
        HCOPy:PAGE:MARGin:LEFT <numeric_value>
        HCOPy:PAGE:MARGin:RIGHt <numeric_value>
        HCOPy:PAGE:MARGin:TOP <numeric_value>
        HCOPy:PAGE:MARGin:BOTTom <numeric_value>
        HCOPy:PAGE:ORIentation PORTrait | LANDscape
        HCOPy:PAGE:WINDow ALL | SINGle | ACTive
        
        

   :param topMargin: Defines the distance between the top of the pageand the top of the printed information.
   :param dateAndTime: Qualifies whether or not the printed outputcontains the current date and time.
   :param markerList: Qualifies whether or not the printed outputcontains the information in the marker info field (marker list).
   :param rightMargin: Defines the distance between the right edge ofthe page and the right edge of the printed information.
   :param diagramArea: Defines the number of diagramareas per printed page.
   :param logo: Qualifies whether or not the printed output containsthe logo. The default R&S logo (file Logo.gif) is stored in theResources\Images subdirectory of the NWA program directory and can bereplaced by another logo.
   :param pageOrientation: Defines the orientation of the printed page.Switching between LANDscape and PORTrait rotates the hardcopy resultby 90 degrees. No other settings are changed.
   :param bottomMargin: Defines the distance between the bottom of thepage and the bottom of the printed information.
   :param leftMargin: Defines the distance between the left edge of thepage and the left edge of the printed information.

.. method:: FileManager(self, operationToBePerformed, source, destination)
           
        This function provides operations which allows to do basic file
        operations on the storage media of the instrument. It consists from
        the following operations:
        
        Change Drive
        Change Current Directory
        Create Directory
        Delete Directory
        Copy File
        Move File
        Delete File
        
        Remote-control command(s):
        MMEMory:MSIS '<device>'
        MMEMory:CDIRectory '<directory_name>' | DEFault
        MMEMory:MDIRectory '<directory_name>'
        MMEMory:RDIRectory '<directory_name>'
        MMEMory:COPY '<file_source>','<file_destination>'
        MMEMory:MOVE '<file_source>','<file_destination>'
        MMEMory:DELete '<file_name>'
        
        

   :param source: This control specifies the source of the operation tobe performed. If the operation requires a single parameter, thiscontrol specifies that parameter.
   :param destination: This control specifies the destination of theoperation to be performed.
   :param operationToBePerformed: This controlselects the type of operation to be performed.

.. method:: GetCurrentDirectory(self, currentDirectory)
           
        This function returns the default directory for mass memory storage
        (current directory).
        
        Remote-control command(s):
        MMEMory:CDIRectory?
        
        

   :param currentDirectory: Returns the currentdirectory.

.. method:: SetupSave(self, fileName)
           
        This function Stores the configuration data of the current setup to a
        specified setup file.
        
        Remote-control command(s):
        MMEMory:STORe:STATe <numeric_value>,'<file_name>'
        
        

   :param fileName: String parameter to specify thename and directory of the created setup file. The default extension(manual control) for setup files is *.zvx, although other extensionsare allowed. If no path is specified the analyzer uses the currentdirectory, to be queried with MMEMory:CDIRectory?.

.. method:: SetupRecall(self, fileName)
           
        This function loads configuration data from a specified setup file and
        sets the analyzer to the corresponding instrument state.
        
        Remote-control command(s):
        MMEMory:LOAD:STATe <numeric_value>,'<file_name>'
        
        

   :param fileName: String parameter to specify thename and directory of the setup file to be loaded. The defaultextension (manual control) for setup files is *.zvx, although otherextensions are allowed. If no path is specified the analyzer searchesthe current directory, to be queried with MMEMory:CDIRectory?.

.. method:: readToFile(self, source, destination)
           
        This function is used to read data from the instrument and write it to
        a user specified file on the host computer.
        
        Remote-control command(s):
        MMEMory:DATA? '<file_name>'
        
        

   :param source: This control selects file for thedata transfer from instrument to control computer.
   :param destination: This control defines destination file to whichthe data transfer from instrument to control computer applies.

.. method:: writeFromFile(self, source, destination)
           
        This function is used to read data from the host computer and write it
        to a user specified file in the instrument.
        
        Remote-control command(s):
        SYSTem:COMMunicate:GPIB[:SELF]:RTERminator LFEOI | EOI
        MMEMory:DATA '<file_name>', <data>
        
        

   :param source: This control selects file for thedata transfer from control computer to instrument.
   :param destination: This control defines destination file to whichthe data transfer from control computer to instrument applies.

.. method:: SelectPowerMeter(self, channel=1, traceName, powerMeter, outPort)
           
        This function selects one of two powermeters for the given drive ports
        into the given trace to prepare a power calibration.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'Pmtr1D1' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'Pmtr1D1' | ...
        
        

   :param powerMeter: Y-S-parameters are expressed as Y-S<out><in>, where<out> and <in> denote the output and input port numbers of the DUT.
   :param outPort: Y-S-parameters are expressed as Y-S<out><in>, where<out> and <in> denote the output and input port numbers of the DUT.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectSParameters(self, channel=1, traceName, outPort, inPort)
           
        This function select one of the four elements of the standard 2-port
        scattering matrix (S-parameters) or select S-parameters for multiport
        measurements.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The S-parameters are the basic measured quantities of a network
        analyzer. They describe how the DUT modifies a signal that is
        transmitted or reflected in forward or reverse direction. S-parameters
        are expressed as S<out><in>, where <out> and <in> denote the output
        and input port numbers of the DUT.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'S11' | 'S12' | 'S21' |
        'S22' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'S11' | 'S12' | 'S21' |
        'S22' | ...
        
        

   :param outPort: S-parameters are expressed as S<out><in>, where <out>and <in> denote the output and input port numbers of the DUT.
   :param inPort: S-parameters are expressed as S<out><in>, where <out>and <in> denote the output and input port numbers of the DUT.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectMoreSParameters(self, channel=1, traceName, outMode, outPort, inMode, inPort)
           
        This function select S-parameters for multiport measurements
        (including the 2-port S-parameters) or mixed mode S-parameters. All
        possible combinations of mixed mode parameters (e.g. Sss, Scs, Sds,
        Sdd,...) are provided.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        Mixed mode parameters are used to distinguish the following three port
        modes:
        
        Single-ended (for unbalanced ports)
        Differential mode (for balanced ports)
        Common mode (for balanced ports)
        
        The notation of a general S-parameter is S<mout><min><out><in>, where
        <mout> and <min> denote the output and input port modes, <out> and
        <in> denote the output and input port numbers.
        
        The selected modes must be compatible with the port configuration. If
        an attempt is made to select an incompatible parameter (e.g. a single-
        ended parameter for a balanced port), the analyzer displays an error
        message.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'S11' | 'S12' | 'S21' |
        'S22' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'S11' | 'S12' | 'S21' |
        'S22' | ...
        
        

   :param outPort: S-parameters are expressed as S<out><in>, where <out>and <in> denote the output and input port numbers of the DUT.
   :param inMode: Define port mode.
   :param inPort: S-parameters are expressed as S<out><in>, where <out>and <in> denote the output and input port numbers of the DUT.
   :param outMode: Define port mode.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectRatios(self, channel=1, traceName, ratios)
           
        This function select predefined complex ratios of the standard 2-port
        wave quantities a1, a2, b1, and b2.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The predefined wave quantities are all obtained with the same test set
        configuration, port 1 providing the stimulus signal (source port 1,
        forward measurement if the stimulus signal is fed to the input of the
        DUT).
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'B2D1/A1D1' | 'B1D1/A1D1'
        | 'B2D1/B1D1' | 'B1D1/B2D1'
        CALCulate<Ch>:PARameter:MEASure '<string>', 'B2D1/A1D1' | 'B1D1/A1D1'
        | 'B2D1/B1D1' | 'B1D1/B2D1'
        
        

   :param ratios: Select predefined complex ratios of the standard 2-portwave quantities a1, a2, b1, and b2.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectMoreRatios(self, channel=1, traceName, sourcePort, numeratorType, numeratorPortNumber, denominatorType, denominatorPortNumber)
           
        This function select arbitrary ratios of wave quantities, e.g. for
        different detectors and source ports or more than 2 ports.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The notation for ratios and the functionality of the More Ratios
        dialog is analogous to the definition of S-parameters.
        
        Ratio of wave quantities with port numbers and source port numbers
        (D<no> for drive port; the source port for the numerator and the
        denominator can be equal or different).
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'B2D1/A1D1' | 'B1D1/A1D1'
        | 'B2D1/B1D1' | 'B1D1/B2D1' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'B2D1/A1D1' | 'B1D1/A1D1'
        | 'B2D1/B1D1' | 'B1D1/B2D1' | ...
        
        

   :param numeratorPortNumber: Port number assignment. The input(stimulus) or output (response) port number is selected. The range ofoutput and input port numbers depends on the analyzer model.
   :param denominatorPortNumber: Port number assignment. The input(stimulus) or output (response) port number is selected. The range ofoutput and input port numbers depends on the analyzer model.
   :param numeratorType: Selects the type of the wave that forms thenumerator of the ratio.
   :param denominatorType: Selects the type of the wave that forms thedenominator of the ratio.
   :param sourcePort: Source Port selects one of the available test portsof the analyzer as a source of the stimulus signal.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectMoreRatiosWithDetector(self, channel=1, traceName, sourcePort, numeratorType, numeratorPortNumber, denominatorType, denominatorPortNumber, detector, observationTime)
           
        This function select arbitrary ratios of wave quantities with
        detector, e.g. for different detectors and source ports or more than 2
        ports.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The notation for ratios and the functionality of the More Ratios
        dialog is analogous to the definition of S-parameters.
        
        Ratio of wave quantities with port numbers and source port numbers
        (D<no> for drive port; the source port for the numerator and the
        denominator can be equal or different).
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'B2D1/A1D1SAM' |
        'B1D1/A1D1RMS' | 'B2D1/B1D1PEAK' | 'B1D1/B2D1SAM' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'B2D1/A1D1SAM' |
        'B1D1/A1D1RMS' | 'B2D1/B1D1PEAK' | 'B1D1/B2D1SAM' | ...
        [SENSe<Ch>:]SWEep:DETector:TIME
        
        

   :param numeratorPortNumber: Port number assignment. The input(stimulus) or output (response) port number is selected. The range ofoutput and input port numbers depends on the analyzer model.
   :param denominatorPortNumber: Port number assignment. The input(stimulus) or output (response) port number is selected. The range ofoutput and input port numbers depends on the analyzer model.
   :param numeratorType: Selects the type of the wave that forms thenumerator of the ratio.
   :param observationTime: This control sets the detector observationtime ratios and wave quantities if a Peak or RMS detector is active.
   :param denominatorType: Selects the type of the wave that forms thedenominator of the ratio.
   :param sourcePort: Source Port selects one of the available test portsof the analyzer as a source of the stimulus signal.
   :param detector: Selects the algorithm that is used to calculate thedisplayed measurement points from the raw data.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectMoreRatiosGenerator(self, channel=1, traceName, generatorNumber, numeratorType, numeratorPortNumber, denominatorType, denominatorPortNumber)
           
        This function select arbitrary ratios of wave quantities, e.g. for
        different detectors and external generator.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The notation for ratios and the functionality of the More Ratios
        dialog is analogous to the definition of S-parameters.
        
        Ratio of wave quantities with port numbers and external generator
        providing the stimulus signal.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'B2G1/A1G1' | 'B1G1/A1G1'
        | 'B2G1/B1G1' | 'B1G1/B2G1' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'B2G1/A1G1' | 'B1G1/A1G1'
        | 'B2G1/B1G1' | 'B1G1/B2G1' | ...
        
        

   :param numeratorPortNumber: Port number assignment. The input(stimulus) or output (response) port number is selected. The range ofoutput and input port numbers depends on the analyzer model.
   :param generatorNumber: Source Port selects one of the available testports of the analyzer as a source of the stimulus signal.
   :param denominatorPortNumber: Port number assignment. The input(stimulus) or output (response) port number is selected. The range ofoutput and input port numbers depends on the analyzer model.
   :param numeratorType: Selects the type of the wave that forms thenumerator of the ratio.
   :param denominatorType: Selects the type of the wave that forms thedenominator of the ratio.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectMoreRatiosGeneratorWithDetector(self, channel=1, traceName, generatorNumber, numeratorType, numeratorPortNumber, denominatorType, denominatorPortNumber, detector, observationTime)
           
        This function select arbitrary ratios of wave quantities with
        detector, e.g. for different detectors and external generator.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The notation for ratios and the functionality of the More Ratios
        dialog is analogous to the definition of S-parameters.
        
        Ratio of wave quantities with port numbers and external generator
        providing the stimulus signal.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'B2G1/A1G1SAM' |
        'B1G1/A1G1RMS' | 'B2G1/B1G1PEAK' | 'B1G1/B2G1SAM' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'B2G1/A1G1SAM' |
        'B1G1/A1G1RMS' | 'B2G1/B1G1PEAK' | 'B1G1/B2G1SAM' | ...
        [SENSe<Ch>:]SWEep:DETector:TIME
        
        

   :param numeratorPortNumber: Port number assignment. The input(stimulus) or output (response) port number is selected. The range ofoutput and input port numbers depends on the analyzer model.
   :param generatorNumber: Source Port selects one of the available testports of the analyzer as a source of the stimulus signal.
   :param denominatorPortNumber: Port number assignment. The input(stimulus) or output (response) port number is selected. The range ofoutput and input port numbers depends on the analyzer model.
   :param numeratorType: Selects the type of the wave that forms thenumerator of the ratio.
   :param observationTime: This control sets the detector observationtime ratios and wave quantities if a Peak or RMS detector is active.
   :param denominatorType: Selects the type of the wave that forms thedenominator of the ratio.
   :param detector: Selects the algorithm that is used to calculate thedisplayed measurement points from the raw data.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectWaveQuantities(self, channel=1, traceName, waveQuantities)
           
        This function select the standard 2-port wave quantities a1, a2, b1,
        and b2 for different source ports.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The predefined wave quantities are obtained with different source
        ports. a1 Src Port 1, b1 Src Port 1 and b1 Src Port 2 are measured at
        Port 1 of the analyzer. a2 Src Port 2, b2 Src Port 1 and b2 Src Port 2
        are measured at Port 2 of the analyzer.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'A1D1' | 'B1D1' | 'B2D1' |
        'A2D2' | 'B1D2' | 'B2D2'
        CALCulate<Ch>:PARameter:MEASure '<string>', 'A1D1' | 'B1D1' | 'B2D1' |
        'A2D2' | 'B1D2' | 'B2D2'
        
        

   :param waveQuantities: Select the standard 2-port wave quantities a1,a2, b1, and b2 for different source ports.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectMoreWaveQuantities(self, channel=1, traceName, waveQuantityType, waveQuantityPortNumber, sourcePort)
           
        This function select arbitrary wave quantities, e.g. for different
        detectors and source ports or more than 2 ports, frequency offsets, or
        mixed mode measurements.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The notation for wave quantities and the functionality of the More
        Wave Quantities is analogous to the definition of S-parameters.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'A1D1' | 'B1D1' | 'B2D1' |
        'A2D2' | 'B1D2' | 'B2D2' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'A1D1' | 'B1D1' | 'B2D1' |
        'A2D2' | 'B1D2' | 'B2D2' | ...
        
        

   :param sourcePort: Source Port selects one of the available test portsof the analyzer as a source of the stimulus signal. The analyzerplaces no restriction on the combination of source ports and portnumbers of the measured wave quantity, so it is even possible tomeasure a2 while the source port is port 1 (e.g. in order to estimatethe directivity of the coupler).
   :param waveQuantityPortNumber: Port number assignment. The input(stimulus) or output (response) port number is selected. The range ofoutput and input port numbers depends on the analyzer model.
   :param waveQuantityType: Selects the type of the wave quantity.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectMoreWaveQuantitiesWithDetector(self, channel=1, traceName, waveQuantityType, waveQuantityPortNumber, sourcePort, detector, observationTime)
           
        This function select arbitrary wave quantities with detector, e.g. for
        different detectors and source ports or more than 2 ports, frequency
        offsets, or mixed mode measurements.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The notation for wave quantities and the functionality of the More
        Wave Quantities is analogous to the definition of S-parameters.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'A1D1SAM' | 'B1D1RMS' |
        'B2D1PEAK' | 'A2D2SAM' | 'B1D2RMS' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'A1D1SAM' | 'B1D1RMS' |
        'B2D1PEAK' | 'A2D2SAM' | 'B1D2RMS' | ...
        [SENSe<Ch>:]SWEep:DETector:TIME
        
        

   :param waveQuantityType: Selects the type of the wave quantity.
   :param observationTime: This control sets the detector observationtime ratios and wave quantities if a Peak or RMS detector is active.
   :param sourcePort: Source Port selects one of the available test portsof the analyzer as a source of the stimulus signal. The analyzerplaces no restriction on the combination of source ports and portnumbers of the measured wave quantity, so it is even possible tomeasure a2 while the source port is port 1 (e.g. in order to estimatethe directivity of the coupler).
   :param detector: Selects the algorithm that is used to calculate thedisplayed measurement points from the raw data.
   :param waveQuantityPortNumber: Port number assignment. The input(stimulus) or output (response) port number is selected. The range ofoutput and input port numbers depends on the analyzer model.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectImpedances(self, channel=1, traceName, outPort, inPort)
           
        This function select the 2-port (or more ports) matched-circuit,
        converted impedances. The parameters describe the impedances of a
        2-port (or more ports) DUT, obtained in forward and reverse
        transmission and reflection measurements:
        
        Z11 is the input impedance of a 2-port DUT that is terminated at its
        output with the reference impedance Z0 (matched-circuit impedance
        measured in a forward reflection measurement).
        
        Z22 is the output impedance of a 2-port DUT that is terminated at its
        input with the reference impedance Z0 (matched-circuit impedance
        measured in a reverse reflection measurement).
        
        Z12 and Z21 denote the forward and reverse transfer impedances,
        respectively.
        
        The analyzer can also provide matched-circuit impedances for more
        drive ports or balanced port configurations.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The notation for converted impedance parameters and the functionality
        is analogous to the definition of S-parameters.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'Z-S11' | 'Z-S12' |
        'Z-S21' | 'Z-S22' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'Z-S11' | 'Z-S12' |
        'Z-S21' | 'Z-S22' | ...
        
        

   :param outPort: Z-S-parameters are expressed as Z-S<out><in>, where<out> and <in> denote the output and input port numbers of the DUT.
   :param inPort: Z-S-parameters are expressed as Z-S<out><in>, where<out> and <in> denote the output and input port numbers of the DUT.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectMoreImpedances(self, channel=1, traceName, outMode, outPort, inMode, inPort)
           
        This function select converted, matched-circuit impedance parameters
        for more ports or balanced port measurements. All possible
        combinations of mixed mode parameters (e.g. Z-Sss, Z-Scs, Z-Sds,
        Z-Sdd,...) are provided.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        Mixed mode parameters are used to distinguish the following three port
        modes:
        
        Single-ended (for unbalanced ports)
        Differential mode (for balanced ports)
        Common mode (for balanced ports)
        
        The notation of a general Z-S-parameter is Z-S<mout><min><out><in>,
        where <mout> and <min> denote the output and input port modes, <out>
        and <in> denote the output and input port numbers.
        
        The selected modes must be compatible with the port configuration. If
        an attempt is made to select an incompatible parameter (e.g. a single-
        ended parameter for a balanced port), the analyzer displays an error
        message.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'Z-S11' | 'Z-S12' |
        'Z-S21' | 'Z-S22' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'Z-S11' | 'Z-S12' |
        'Z-S21' | 'Z-S22' | ...
        
        

   :param outPort: Z-S-parameters are expressed as Z-S<out><in>, where<out> and <in> denote the output and input port numbers of the DUT.
   :param inMode: Define port mode.
   :param inPort: Z-S-parameters are expressed as Z-S<out><in>, where<out> and <in> denote the output and input port numbers of the DUT.
   :param outMode: Define port mode.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectAdmitances(self, channel=1, traceName, outPort, inPort)
           
        This function select the 2-port (or more ports) converted matched-
        circuit admittance parameters. The parameters describe the admittances
        of a 2-port (or more ports) DUT, obtained in forward and reverse
        transmission and reflection measurements:
        
        Y11 is the input admittance of a 2-port DUT that is terminated at its
        output with the reference impedance Z0 (matched-circuit admittance
        measured in a forward reflection measurement).
        
        Y22 is the output admittance of a 2-port DUT that is terminated at its
        input with the reference impedance Z0 (matched-circuit admittance
        measured in a reverse reflection measurement).
        
        Y12 and Y21 denote the forward and reverse transfer admittances,
        respectively.
        
        The analyzer can also provide matched-circuit admittances for more
        drive ports or balanced port configurations.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The notation for converted admittance parameters and the functionality
        is analogous to the definition of S-parameters.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'Y-S11' | 'Y-S12' |
        'Y-S21' | 'Y-S22' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'Y-S11' | 'Y-S12' |
        'Y-S21' | 'Y-S22' | ...
        
        

   :param outPort: Y-S-parameters are expressed as Y-S<out><in>, where<out> and <in> denote the output and input port numbers of the DUT.
   :param inPort: Y-S-parameters are expressed as Y-S<out><in>, where<out> and <in> denote the output and input port numbers of the DUT.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectMoreAdmitances(self, channel=1, traceName, outMode, outPort, inMode, inPort)
           
        This function select converted, matched-circuit admittance parameters
        for more ports or balanced port measurements. All possible
        combinations of mixed mode parameters (e.g. Y-Sss, Y-Scs, Y-Sds,
        Y-Sdd,...) are provided.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        Mixed mode parameters are used to distinguish the following three port
        modes:
        
        Single-ended (for unbalanced ports)
        Differential mode (for balanced ports)
        Common mode (for balanced ports)
        
        The notation of a general Y-S-parameter is Y-S<mout><min><out><in>,
        where <mout> and <min> denote the output and input port modes, <out>
        and <in> denote the output and input port numbers.
        
        The selected modes must be compatible with the port configuration. If
        an attempt is made to select an incompatible parameter (e.g. a single-
        ended parameter for a balanced port), the analyzer displays an error
        message.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'Y-S11' | 'Y-S12' |
        'Y-S21' | 'Y-S22' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'Y-S11' | 'Y-S12' |
        'Y-S21' | 'Y-S22' | ...
        
        

   :param outPort: Y-S-parameters are expressed as Y-S<out><in>, where<out> and <in> denote the output and input port numbers of the DUT.
   :param inMode: Define port mode.
   :param inPort: Y-S-parameters are expressed as Y-S<out><in>, where<out> and <in> denote the output and input port numbers of the DUT.
   :param outMode: Define port mode.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectZParameters(self, channel=1, traceName, outMode, outPort, inMode, inPort)
           
        This function select open-circuit Z-parameters for multiport
        measurements (including the 2-port Z-parameters) or mixed mode
        Z-parameters. All possible combinations of mixed mode parameters (e.g.
        Zss, Zcs, Zds, Zdd,...) are provided.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        Mixed mode parameters are used to distinguish the following three port
        modes:
        
        Single-ended (for unbalanced ports)
        Differential mode (for balanced ports)
        Common mode (for balanced ports)
        
        The notation of a general Z-parameter is Z<mout><min><out><in>, where
        <mout> and <min> denote the output and input port modes, <out> and
        <in> denote the output and input port numbers.
        
        The selected modes must be compatible with the port configuration. If
        an attempt is made to select an incompatible parameter (e.g. a single-
        ended parameter for a balanced port), the analyzer displays an error
        message.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'Z11' | 'Z12' | 'Z21' |
        'Z22' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'Z11' | 'Z12' | 'Z21' |
        'Z22' | ...
        
        

   :param outPort: Z-parameters are expressed as Z<out><in>, where <out>and <in> denote the output and input port numbers of the DUT.
   :param inMode: Define port mode.
   :param inPort: Z-parameters are expressed as Z<out><in>, where <out>and <in> denote the output and input port numbers of the DUT.
   :param outMode: Define port mode.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectYParameters(self, channel=1, traceName, outMode, outPort, inMode, inPort)
           
        This function select short-circuit Y-parameters for multiport
        measurements (including the 2-port Y-parameters) or mixed mode
        Y-parameters. All possible combinations of mixed mode parameters (e.g.
        Yss, Ycs, Yds, Ydd,...) are provided.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        Mixed mode parameters are used to distinguish the following three port
        modes:
        
        Single-ended (for unbalanced ports)
        Differential mode (for balanced ports)
        Common mode (for balanced ports)
        
        The notation of a general Y-parameter is Y<mout><min><out><in>, where
        <mout> and <min> denote the output and input port modes, <out> and
        <in> denote the output and input port numbers.
        
        The selected modes must be compatible with the port configuration. If
        an attempt is made to select an incompatible parameter (e.g. a single-
        ended parameter for a balanced port), the analyzer displays an error
        message.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'Y11' | 'Y12' | 'Y21' |
        'Y22' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'Y11' | 'Y12' | 'Y21' |
        'Y22' | ...
        
        

   :param outPort: Y-parameters are expressed as Y<out><in>, where <out>and <in> denote the output and input port numbers of the DUT.
   :param inMode: Define port mode.
   :param inPort: Y-parameters are expressed as Y<out><in>, where <out>and <in> denote the output and input port numbers of the DUT.
   :param outMode: Define port mode.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectStabilityFactors(self, channel=1, traceName, DUTOut, DUTIn, stabilityFactor)
           
        This function select one of the three two port stability factors K, u1
        or u2.
        
        Stability factors are calculated as functions of the frequency or
        another stimulus parameter. They provide criteria for linear stability
        of two-ports such as amplifiers. A linear circuit is said to be
        unconditionally stable if no combination of passive source or load can
        cause the circuit to oscillate.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        Stability factors can be calculated for unbalanced ports only. If a
        balanced port configuration is selected, the analyzer generates an
        error message.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'KFAC21' | 'MUF121' |
        'MUF221' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'KFAC21' | 'MUF121' |
        'MUF221' | ...
        
        

   :param DUTIn: Selects the test port number of the analyzer to beconnected to the input (DUT Input) and the output of the DUT (DUTOutput). The ports can be arbitrary, however, the stability factorcalculation is based on 2-port reflection and transmissionS-parameters so that the input and output port numbers must bedifferent.
   :param stabilityFactor: Selects the stability factor to be calculated.
   :param DUTOut: Selects the test port number of the analyzer to beconnected to the input (DUT Input) and the output of the DUT (DUTOutput). The ports can be arbitrary, however, the stability factorcalculation is based on 2-port reflection and transmissionS-parameters so that the input and output port numbers must bedifferent.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectDCMeasurement(self, channel=1, traceName, DCMeas)
           
        This function select the DC voltages fed to the DC MEAS input
        connectors as measured quantities. The input connectors are located at
        the rear panel of the instrument.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'DC+1V' | 'DC+10V'
        CALCulate<Ch>:PARameter:MEASure '<string>', 'DC+1V' | 'DC+10V'
        
        

   :param DCMeas: Select the DC voltages fed to the DC MEAS inputconnectors as measured quantities.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SelectPAEMeasurement(self, channel=1, traceName, DUTOut, DUTIn)
           
        This function select the Power Added Efficiency (PAE) of an active
        2-port device as measured quantity and to define the parameters for
        the PAE measurement.
        
        The Power Added Efficiency (PAE) is the ratio of the added RF power
        generated by an active two-port device (e.g. an amplifier) to the
        supplied DC power PDC. The added RF power can be expressed as the
        difference between the power of the outgoing wave b2 at the output of
        the DUT and the power of the incident wave a1 at the input of the DUT.
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        To obtain reasonable results, the test model and the respective
        Constant must be selected in accordance to the test setup.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'PAE21' | 'PAE12' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'PAE21' | 'PAE12' | ...
        
        

   :param DUTIn: Selects the analyzer port providing the input signal a1(DUT Input) and the receiver port for the output signal b2 (DUTOutput). The input and output port numbers must be different.
   :param DUTOut: Selects the analyzer port providing the input signal a1(DUT Input) and the receiver port for the output signal b2 (DUTOutput). The input and output port numbers must be different.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: DefinePAEMeasurement(self, channel_Trace, testModel, constantC, constantK)
           
        This function select the test model and the parameters for measuring
        the DC power PDC supplied to the DUT.
        
        The power PDC supplied to the DUT can be measured using either one of
        the DC inputs DC MEAS +/-10V (for large voltages), DC MEAS +/-1V (for
        small voltages) or both inputs. Define DC Power Measurement in the PAE
        measurement suggests different models involving different test setups
        and approximations.
        
        Remote-control command(s):
        [SENSe<Ch/Tr>:]PAE:EXPRession C10 | C1 | K101 | CK11
        [SENSe<Ch/Tr>:]PAE:C <numeric_value>
        [SENSe<Ch/Tr>:]PAE:K <numeric_value>
        
        

   :param constantK: Defines the constant k for the PAE measurement.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param testModel: Selects the test model for the PAE measurement.
   :param constantC: Defines the constant c for the PAE measurement.

.. method:: SelectNoiseFigure(self, channel=1, traceName, outPort, inPort)
           
        This function select one of the four elements of the Noise Figure
        2-port scattering matrix (NF-parameters).
        
        Assigns a measurement parameter to an existing trace or creates a
        trace and assigns a channel number, a name and a measurement parameter
        to it. The trace is not displayed.
        
        The NF-parameters are the basic measured quantities of a network
        analyzer. They denote the output and input port numbers of the DUT.
        NF-parameters are expressed as NF<out><in>, where <out> and <in>
        denote the output and input port numbers of the DUT.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'NF11' | 'NF12' | 'NF21' |
        'NF22' | ...
        CALCulate<Ch>:PARameter:MEASure '<string>', 'NF11' | 'NF12' | 'NF21' |
        'NF22' | ...
        
        

   :param outPort: S-parameters are expressed as S<out><in>, where <out>and <in> denote the output and input port numbers of the DUT.
   :param inPort: S-parameters are expressed as S<out><in>, where <out>and <in> denote the output and input port numbers of the DUT.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: CreateTrace(self, channel=1, traceName, parameter)
           
        This function creates a trace and assigns a channel number, a name and
        a measurement parameter to it. The trace
        becomes the active trace in the channel but is not displayed.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine
        
        

   :param parameter: Configures the measurement parameter.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: ConfigureMesurementParameters(self, channel=1, traceName, parameter)
           
        This function assigns a measurement parameter to an existing trace.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:MEASure
        
        

   :param parameter: Configures the measurement parameter Valid Values: not checked
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: QueryMesurementParameters(self, channel=1, traceName, bufferSize, parameters)
           
        This function queries a measurement parameter of an existing trace.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:MEASure? '<string>'
        
        

   :param bufferSize: Defines the allocated size of Function Parameters.
   :param parameters: Returns the defined measurementparameterSee see list of parameters in the CALCulate<Ch>:PARameter:SDEFinecommand description.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SetTraceFormat(self, channel_Trace, format)
           
        This function defines how the measured result at any sweep point is
        post-processed and presented in the graphical display.
        
        Note(s):
        
        The analyzer allows arbitrary combinations of display formats and
        measured quantities. Nevertheless, it is advisable to check which
        display formats are generally appropriate for an analysis of a
        particular measured quantity.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FORMat MLINear | MLOGarithmic | PHASe | UPHase |
        POLar | SMITh | ISMith | GDELay | REAL | IMAGinary | SWR | COMPlex |
        MAGNitude
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param format: Defines how the measured data is presented in thegraphical display.

.. method:: GetTraceFormat(self, channel_Trace)
           
        This function returns how the measured result at any sweep point is
        post-processed and presented in the graphical display.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FORMat?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: format

.. method:: SetTraceUnit(self, channel_Trace, format)
           
        This function selects the physical unit of the displayed trace.
        
        Remote-control command(s):
        CALCulate<Chn>:FORMat:WQUType POWer | VOLTage
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param format: Defines power or voltage units.

.. method:: GetTraceUnit(self, channel_Trace)
           
        This function returns the physical unit of the displayed trace.
        
        Remote-control command(s):
        CALCulate<Chn>:FORMat:WQUType?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: format

.. method:: SetApertureGroupDelaySteps(self, channel_Trace, steps)
           
        This function defines an aperture for the calculation of the group
        delay as an integer number of frequency sweep steps.
        
        Remote-control command(s):
        CALCulate<Chn>:GDAPerture:SCOunt
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param steps: Defines an aperture for the calculation of the groupdelay as an integer number of frequency sweep steps.

.. method:: GetApertureGroupDelaySteps(self, channel_Trace)
           
        This function returns an aperture for the calculation of the group
        delay as an integer number of frequency sweep steps.
        
        Remote-control command(s):
        CALCulate<Chn>:GDAPerture:SCOunt?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: steps

.. method:: TraceAutoscale(self, window, window_Trace)
           
        This function adjusts the Scale Divisions and the Ref. Value in order
        to display the entire active trace in the diagram area, leaving an
        appropriate display margin.
        
        In Cartesian diagrams, the analyzer re-calculates the values of the
        vertical divisions so that the trace fits onto 80% of the vertical
        grid. The reference value is chosen to center the trace in the
        diagram.
        
        In circular diagrams (Polar, Smith, Inverted Smith), the analyzer re-
        calculates the values of the radial divisions so that the diagram is
        confined to approx. 80% of the outer circumference. The reference
        value is set to the value of the outer circumference.
        
        Autoscale does not affect the stimulus values and the horizontal axis.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        (3) The trace is be referenced by its number <WndTr>.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:AUTO ONCE
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.

.. method:: TraceAutoscaleByName(self, window, traceName)
           
        This function adjusts the Scale Divisions and the Ref. Value in order
        to display the entire active trace in the diagram area, leaving an
        appropriate display margin.
        
        In Cartesian diagrams, the analyzer re-calculates the values of the
        vertical divisions so that the trace fits onto 80% of the vertical
        grid. The reference value is chosen to center the trace in the
        diagram.
        
        In circular diagrams (Polar, Smith, Inverted Smith), the analyzer re-
        calculates the values of the radial divisions so that the diagram is
        confined to approx. 80% of the outer circumference. The reference
        value is set to the value of the outer circumference.
        
        Autoscale does not affect the stimulus values and the horizontal axis.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        (3) The trace is referenced by its name <trace_name>.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe:Y[:SCALe]:AUTO ONCE[, '<trace_name>']
        
        

   :param window: Number of the diagram area.
   :param traceName: This control sets the trace name.

.. method:: SetTraceBottom(self, window, window_Trace, bottom)
           
        This function sets the lower (minimum) edge of the diagram area <Wnd>.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:BOTTom <lower_value>
        
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :param bottom: Value for the lower (minimum) edge of the diagram area<Wnd>.

.. method:: GetTraceBottom(self, window, window_Trace)
           
        This function returns the lower (minimum) edge of the diagram area
        <Wnd>.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:BOTTom?
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :return: bottom

.. method:: SetTraceScaleDivisions(self, window, window_Trace, scaleDivisions)
           
        This function sets the value of the vertical diagram divisions in
        Cartesian diagrams.
        
        Scale /Div corresponds to the increment between two consecutive grid
        lines. The unit depends on the display format: dB for display format
        dB Mag, degrees for Phase and Unwrapped Phase, ns for Delay, U (units)
        for all other (dimensionless) formats.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:PDIVision <numeric_value>
        
        

   :param scaleDivisions: Value for the vertical diagram divisions.
   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.

.. method:: SetTraceScaleDivisionsByName(self, window, scaleDivisions, traceName)
           
        This function sets the value of the vertical diagram divisions in
        Cartesian diagrams.
        
        Scale /Div corresponds to the increment between two consecutive grid
        lines. The unit depends on the display format: dB for display format
        dB Mag, degrees for Phase and Unwrapped Phase, ns for Delay, U (units)
        for all other (dimensionless) formats.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        (3) The trace is referenced by its name <trace_name>.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:PDIVision
        <numeric_value>[,'<trace_name>']
        
        

   :param scaleDivisions: Value for the vertical diagram divisions.
   :param window: Number of the diagram area.
   :param traceName: This control sets the trace name.

.. method:: GetTraceScaleDivisions(self, window, window_Trace)
           
        This function returns the value of the vertical diagram divisions in
        Cartesian diagrams.
        
        Scale /Div corresponds to the increment between two consecutive grid
        lines. The unit depends on the display format: dB for display format
        dB Mag, degrees for Phase and Unwrapped Phase, ns for Delay, U (units)
        for all other (dimensionless) formats.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:PDIVision?
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :return: scaleDivisions

.. method:: SetTraceRefValue(self, window, window_Trace, referenceLevel)
           
        This function sets the reference level (or reference value) for a
        particular displayed trace. Setting a new reference level does not
        affect the value of PDIVision.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:RLEVel <numeric_value>
        
        

   :param referenceLevel: Reference level value.
   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.

.. method:: SetTraceRefValueByName(self, window, referenceLevel, traceName)
           
        This function sets the reference level (or reference value) for a
        particular displayed trace. Setting a new reference level does not
        affect the value of PDIVision.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        (3) The trace is referenced by its name <trace_name>.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:RLEVel
        <numeric_value>[,'<trace_name>']
        
        

   :param referenceLevel: Reference level value.
   :param window: Number of the diagram area.
   :param traceName: This control sets the trace name.

.. method:: GetTraceRefValue(self, window, window_Trace)
           
        This function returns the reference level (or reference value) for a
        particular displayed trace.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:RLEVel?
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :return: referenceLevel

.. method:: SetTraceRefPosition(self, window, window_Trace, referencePosition)
           
        This function sets the point on the y-axis to be used as the reference
        position as a percentage of the length of the y-axis. The reference
        position is the point on the y-axis which should equal the RLEVel.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:RPOSition <numeric_value>
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :param referencePosition: Value of the reference position in percent.The top of the y-axis is defined to have a reference position of 100%,while the bottom of the y-axis is defined to have a reference positionof 0%.

.. method:: SetTraceRefPositionByName(self, window, referencePosition, traceName)
           
        This function sets the point on the y-axis to be used as the reference
        position as a percentage of the length of the y-axis. The reference
        position is the point on the y-axis which should equal the RLEVel.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        (3) The trace is referenced by its name <trace_name>.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:RPOSition
        <numeric_value>[,'<trace_name>']
        
        

   :param window: Number of the diagram area.
   :param traceName: This control sets the trace name.
   :param referencePosition: Value of the reference position in percent.The top of the y-axis is defined to have a reference position of 100%,while the bottom of the y-axis is defined to have a reference positionof 0%.

.. method:: GetTraceRefPosition(self, window, window_Trace)
           
        This function returns the point on the y-axis used as the reference
        position as a percentage of the length of the y-axis. The reference
        position is the point on the y-axis which should equal the RLEVel.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:RPOSition?
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :return: referencePosition

.. method:: SetTraceTop(self, window, window_Trace, top)
           
        This function sets the upper (maximum) edge of the diagram area <Wnd>.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:TOP <upper_value>
        
        

   :param window: Number of the diagram area.
   :param top: Value for the upper (maximum) edge of the diagram area<Wnd>.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.

.. method:: GetTraceTop(self, window, window_Trace)
           
        This function returns the upper (maximum) edge of the diagram area
        <Wnd>.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y[:SCALe]:TOP?
        
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :return: top

.. method:: TraceAdd(self, channel=1, traceName)
           
        This function creates a new trace in the current diagram area and
        assigns it to the selected channel. The new trace is created with the
        default trace and channel settings. Trace is not displayed.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'S21'
        
        

   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: TraceAddMode(self, channel=1, traceName, outMode, inMode)
           
        This function creates a new trace in the current diagram area and
        assigns it to the selected channel. The new trace is created with the
        default trace and channel settings. Trace is not displayed.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine
        
        

   :param outMode: Define port mode.
   :param inMode: Define port mode.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: SetTraceDisplayState(self, traceType, singleTraceName, showTrace)
           
        Displays or hides an existing trace, identified by its trace name
        (CALCulate<Ch>:PARameter:SDEFine <Trace_Name>), or a group of traces.
        
        Remote-control command(s):
        DISPlay[:WINDow<Wnd>]:TRACe<WndTr>:SHOW DALL | MALL | '<trace_name>',
        <Boolean>
        
        
        

   :param traceType: This control selects the type oftrace.
   :param singleTraceName: Define tracename.
   :param showTrace: This control displays or hidestrace(s).

.. method:: GetTraceDisplayState(self, traceType, singleTraceName)
           
        This function returns whether the trace is shown or not.
        
        Remote-control command(s):
        DISPlay[:WINDow<Wnd>]:TRACe<WndTr>:SHOW? DALL | MALL | '<trace_name>'
        
        
        

   :param traceType: This control selects the type oftrace.
   :param singleTraceName: Define tracename.
   :return: showTrace

.. method:: TraceAddSParameterGroup(self, channel=1, numberOfLogicalPortNumbers, logicalPortNumber_s)
           
        This function creates the traces for all S-parameters associated with
        a group of logical ports (S-parameter group).
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:DEFine:SGRoup <log_port1>[, <log_port2>,...]
        
        

   :param numberOfLogicalPortNumbers: This control sets teh number oflogical port numbers used.
   :param logicalPortNumber_s: Define logical(balanced or unbalanced) port numbers. The port numbers must be inascending order, their number is limited by the test ports of theanalyzer.
   :param channel: Channel number. Channel may beused to reference a previously defined channel. If channel does notexist, it is generated with default channel settings.

.. method:: QueryTraceAddSParameterGroup(self, channel=1, logicalPortNumber_s)
           
        This function returns a group of logical ports (S-parameter group).
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:DEFine:SGRoup?
        
        

   :param logicalPortNumber_s: Returns logical (balanced or unbalanced)port numbers. The port numbers are in ascending order, their number islimited by the test ports of the analyzer.
   :param channel: Channel number. Channel may beused to reference a previously defined channel. If channel does notexist, it is generated with default channel settings.

.. method:: TraceAddDiagramArea(self, window, window_Trace, channel=1, traceName)
           
        This function creates a new trace in a new diagram area and assigns
        the trace to the selected channel. The new trace is created with the
        default trace and channel settings and displayed in the new diagram
        area.
        
        Note(s):
        
        A trace can be assigned to a diagram only once. If a attempt is made
        to assign the same trace a second time an error message -114,"Header
        suffix out of range" is generated.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'S21'
        DISPlay:WINDow<Wnd>:STATe ON
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED '<string>'
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: TraceAssignDiagramArea(self, window, window_Trace, traceName)
           
        This function assigns the active trace to another diagram area.
        Selecting one of the existing area numbers assigns the active trace to
        the existing diagram area: The active trace is removed from the
        previous area and displayed in the new diagram area.
        
        Note(s):
        
        A trace can be assigned to a diagram only once. If a attempt is made
        to assign the same trace a second time an error message -114,"Header
        suffix out of range" is generated.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:STATe ON
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED '<string>'
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :param traceName: Define trace name.

.. method:: TraceAssignWindowDiagramArea(self, window, traceName)
           
        This function assigns an existing trace to a diagram area, and
        displays the trace. Use DISPlay[:WINDow<Wnd>]:TRACe<WndTr>:FEED to
        assign the trace to a diagram area using a numeric suffix
        
        Note(s):
        
        (1) You can open the trace manager (DISPlay:MENU:KEY:EXECute 'Trace
        Manager') to obtain an overview of all channels and traces, including
        the traces that are not displayed.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:STATe ON
        DISPlay:WINDow<Wnd>:TRACe:EFEed '<string>'
        
        

   :param window: Number of the diagram area.
   :param traceName: Define trace name.

.. method:: TraceUnassignDiagramArea(self, window, window_Trace)
           
        This function releases the assignment between a trace and a diagram
        area, as defined by means of DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED
        <Trace_Name> and expressed by the <WndTr> suffix. The trace itself is
        not deleted; this must be done via CALCulate<Ch>:PARameter:DELete
        <Trace_Name>.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:DELete
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.

.. method:: TraceSelect(self, channel=1, traceName)
           
        This function selects an existing trace as the active trace of the
        channel. All trace commands without explicit reference to the trace
        name act on the active trace (e.g. CALCulate<Ch>:FORMat).
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:SELect '<string>'
        
        

   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: TraceDelete(self, channel=1, traceName)
           
        This function deletes a trace with a specified trace name and channel.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:DELete '<string>'
        
        

   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: TraceDeleteAll(self, channel=1)
           
        This function deletes all traces in specified channel.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:DELete:CALL
        
        

   :param channel: Channel number.

.. method:: TraceDeleteAllChannels(self, )
           
        This function deletes all traces in all channels of the active setup,
        including the default trace Trc1 in channel no. 1.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:DELete:ALL
        
        


.. method:: TraceList(self, channel=1, catalog, bufferSize)
           
        This function returns the trace names and measurement parameters of
        all traces assigned to a particular channel.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:CATalog?
        
        

   :param catalog: Response is a string parameter with comma-separatedlist of trace names and measurement parameters, e.g.'CH4TR1,S11,CH4TR2,S12'. The measurement parameters are returnedaccording to the naming convention of CALCulate<Ch>:PARameter:SDEFine.The order of traces in the list reflects their creation time: Theoldest trace is the first, the newest trace is the last trace in thelist.
   :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.
   :param channel: Channel number.

.. method:: TraceRename(self, oldTraceName, newTraceName)
           
        This function assigns a new name to a trace. The trace does not have
        to be the active trace.
        
        Remote-control command(s):
        CONFigure:TRACe:REName '<old_trace_name>','<new_trace_name>'
        
        
        

   :param oldTraceName: Define old trace name name.
   :param newTraceName: Define new trace name.

.. method:: ChannelTraceRename(self, channel=1, traceName)
           
        This function assigns a new name to the active trace in channel <ch>.
        
        Remote-control command(s):
        CONFigure:CHANnel<Ch>TRACe:REName '<trace_name>'
        
        

   :param channel: Channel number.
   :param traceName: Define new trace name.

.. method:: TraceListCatalog(self, catalog, bufferSize)
           
        This function returns the numbers and names of all traces in the
        current setup.
        
        Remote-control command(s):
        CONFigure:TRACe<Trc>:CATalog?
        
        

   :param catalog: Returns string with comma-separated list of trace numbers and names. If all traces have beendeleted the response is an empty string ("").
   :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.

.. method:: TraceGetTraceName(self, traceNumber, traceName)
           
        This function returns the trace <Trc> name.
        
        Remote-control command(s):
        CONFigure:TRACe<Trc>:NAME?
        
        

   :param traceName: Returns the trace name.
   :param traceNumber: Trace number.

.. method:: TraceGetTraceNumber(self, traceName)
           
        This function returns the trace number (numeric suffix) of a trace
        with known trace name.
        
        Remote-control command(s):
        CONFigure:TRACe:NAME:ID? '<Trc_name>'
        
        

   :param traceName: Sets the trace name.
   :return: traceNumber

.. method:: TraceGetChannelName(self, traceName, channelName)
           
        This function returns the channel name for an existing trace named
        '<Trc_name>'.
        
        Remote-control command(s):
        CONFigure:TRACe:CHANnel:NAME? '<Trc_name>'
        
        
        

   :param channelName: Returns the channel namefor an existing trace.
   :param traceName: Sets the trace name.

.. method:: TraceGetChannelNumber(self, traceName)
           
        This function returns channel number (numeric suffix) for an existing
        trace named '<Trc_name>'.
        
        Remote-control command(s):
        CONFigure:TRACe:CHANnel:NAME:ID? '<Trc_name>'
        
        

   :param traceName: Sets the trace name.
   :return: channelNumber

.. method:: TraceDataToMemory(self, channel_Trace)
           
        This function copies the current state of the active data trace to a
        memory trace. If a mathematical trace is active, the data trace
        associated with the mathematical trace is copied. The memory trace is
        named Mem<n>[<Data_Trace>] where <n> counts all data and memory traces
        in the active setup in chronological order, and <Data_Trace> is the
        name of the associated (copied) data trace.
        
        The exact function of the command depends on the number of memory
        traces associated to the active data trace:
        
        - If no memory trace is associated to the active trace, a new memory
        trace is generated.
        
        - If several memory traces are associated to the active trace, the
        current measurement data overwrites the last generated or changed
        memory trace.
        
        Note(s):
        
        To copy a trace to the memory without overwriting an existing memory
        trace or define a memory trace name, use TRACe:COPY
        <memory_trc>,<data_trc>. To copy an active mathematical trace use
        TRACe:COPY:MATH <memory_trc>,<data_trc>.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MATH:MEMorize
        
        

   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: TraceDataToMemoryTrace(self, memoryTrace, dataTrace)
           
        This function copies a data trace to a memory trace. The trace to be
        copied is specified as a trace with a name (string variable). The
        created memory trace is specified as a memory trace with an arbitrary
        name (string variable). An existing memory trace with the same name is
        overwritten.
        
        Note(s):
        
        The copied trace is the data trace which is not modified by any
        mathematical operations. To copy a mathematical trace to a memory
        trace, use TRACe:COPY:MATH. To copy the active trace to the memory
        using an automatic memory trace name, use
        CALCulate<Ch/Tr>:MATH:MEMorize.
        
        Remote-control command(s):
        TRACe:COPY '<memory_trc>','<data_trc>'
        
        

   :param dataTrace: Name of the data trace.
   :param memoryTrace: Name of the memory trace.

.. method:: TraceMathToMemoryTrace(self, memoryTrace, dataTrace)
           
        This function copies a mathematical trace to a memory trace. The trace
        to be copied is specified as a trace with a name (string variable).
        The created memory trace is specified as a memory trace with an
        arbitrary name (string variable). An existing memory trace with the
        same name is overwritten.
        
        Note(s):
        
        To copy a data trace which is not modified by any mathematical
        operations, use TRACe:COPY.
        
        Remote-control command(s):
        TRACe:COPY:MATH '<memory_trc>','<data_trc>'
        
        

   :param dataTrace: Name of the data trace.
   :param memoryTrace: Name of the memory trace.

.. method:: DeleteMemoryTrace(self, memoryTrace)
           
        This function deletes one of the memory traces Mem<n>[Trc<m>], where n
        = 1, ... 8.
        
        Remote-control command(s):
        TRACe:CLEar MDATA1 | MDATA2 | MDATA3 | MDATA4 | MDATA5 | MDATA6 |
        MDATA7 | MDATA8
        
        

   :param memoryTrace: Deletes one of the memorytraces Mem<n>[Trc<m>], where n = 1, ... 8.

.. method:: TraceUserDefinedMath(self, channel_Trace, mathematicalExpression)
           
        This function activates the mathematical mode where the active data
        trace is divided by the last generated memory trace. The division is
        calculated on a point-to-point basis: Each measurement point of the
        active trace is divided by the corresponding measurement point of the
        memory trace. The result of the division is a mathematical trace and
        replaces the active data trace in the diagram area. The mathematical
        trace is updated as the measurement goes on and the analyzer provides
        new active trace data.
        
        This function is disabled unless a memory trace is coupled to the
        active data trace. Trace coupling ensures that the two traces have the
        same number of points so that the mathematical trace Data/Mem.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MATH[:EXPRession]:SDEFine '<string>'
        CALCulate<Ch/Tr>:MATH:STATe ON
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param mathematicalExpression: String parameter for the mathematicalexpression, enclosed in brackets. Defines a general mathematicalrelation between traces.

.. method:: SetTraceMathState(self, channel_Trace, mathState)
           
        This function activates or deactivates the mathematical mode where the
        mathematical trace defined via
        CALCulate<Ch/Tr>:MATH[:EXPRession]:SDEFine is calculated and displayed
        instead of the active data trace.
        
        Note(s):
        
        This function is not valid for mathematical traces calculated via
        CALCulate<Ch/Tr>:MATH:FUNCtion.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MATH:STATe <Boolean>
        
        

   :param mathState: Activates or deactivates the mathematical mode (ON- Display the active data trace, OFF - Display the mathematicaltrace).
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetTraceMathState(self, channel_Trace)
           
        This function returns state of the mathematical mode where the
        mathematical trace is calculated and displayed instead of the active
        data trace.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MATH:STATe?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: mathState

.. method:: SetTraceMathFunction(self, channel_Trace, mathematicalFunction)
           
        This function defines a simple mathematical relation between the
        active trace and the active memory trace to calculate a new
        mathematical trace and displays the mathematical trace.
        
        Notes:
        
        (1) This command places some restrictions on the mathematical
        expression and the operands. Use
        CALCulate<Chn>:MATH[:EXPRession]:SDEFine to define general
        expressions.
        
        Remote-control command(s):
        CALCulate<Chn>:MATH:FUNCtion NORMal | ADD | SUBTract | MULTiply |
        DIVide
        
        

   :param mathematicalFunction: This control defines a simplemathematical relation between the active trace and the active memorytrace to calculate a new mathematical trace and displays themathematical trace.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetTraceMathFunction(self, channel_Trace)
           
        This function returns a simple mathematical relation between the
        active trace and the active memory trace to calculate a new
        mathematical trace and displays the mathematical trace.
        
        Remote-control command(s):
        CALCulate<Chn>:MATH:FUNCtion?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: mathematicalFunction

.. method:: SetTraceMathWaveQuantityState(self, channel_Trace, mathWaveQuantityState)
           
        This function controls the conversion and formatting of the mathematic
        expression defined via CALCulate<Chn>:MATH[:EXPRession]:SDEFine.
        
        Remote-control command(s):
        CALCulate<Chn>:MATH:WUNit[:STATe] <Boolean>
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param mathWaveQuantityState: Controls the conversion and formattingof the mathematic expression.

.. method:: GetTraceMathWaveQuantityState(self, channel_Trace)
           
        This function returns the state of the conversion and formatting of
        the mathematic expression defined via
        CALCulate<Chn>:MATH[:EXPRession]:SDEFine.
        
        Remote-control command(s):
        CALCulate<Chn>:MATH:WUNit[:STATe]?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: mathWaveQuantityState

.. method:: SetTraceTransformDomain(self, channel_Trace, transformDomain)
           
        This function selects the domain for active trace representation.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:STATe ON | OFF
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param transformDomain: This control selects the domain for activetrace representation.

.. method:: GetTraceTransformDomain(self, channel_Trace)
           
        This function queries the domain for active trace representation.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:STATe?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: transformDomain

.. method:: SetTraceTransformConversion(self, channel_Trace, conversion)
           
        This function converts S-parameters into matched-circuit (converted)
        Y-parameters or Z-parameters and vice versa.
        
        Remote-control command(s):
        CALCulate<Chn>:TRANsform:COMPlex S | Y | Z
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param conversion: This control converts S-parameters into matched-circuit (converted) Y-parameters or Z-parameters and vice versa.

.. method:: GetTraceTransformConversion(self, channel_Trace)
           
        This function returns the conversion type.
        
        Remote-control command(s):
        CALCulate<Chn>:TRANsform:COMPlex?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: conversion

.. method:: SetTimeDomainStartTime(self, channel_Trace, startTime)
           
        This function defines the start time of the diagram in time domain.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:STARt
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param startTime: This control defines start time of the diagram intime domain.

.. method:: GetTimeDomainStartTime(self, channel_Trace)
           
        This function queries the start time of the diagram in time domain.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:STARt?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: startTime

.. method:: SetTimeDomainStopTime(self, channel_Trace, stopTime)
           
        This function defines the stop time of the diagram in time domain.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:STOP
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param stopTime: This control defines stop time of the diagram intime domain.

.. method:: GetTimeDomainStopTime(self, channel_Trace)
           
        This function queries the stop time of the diagram in time domain.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:STOP?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: stopTime

.. method:: SetTimeDomainCenterTime(self, channel_Trace, centerTime)
           
        This function defines the center time of the diagram in time domain.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:CENTer
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param centerTime: This control defines center time of the diagram intime domain.

.. method:: GetTimeDomainCenterTime(self, channel_Trace)
           
        This function queries the center time of the diagram in time domain.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:CENTer?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: centerTime

.. method:: SetTimeDomainTimeSpan(self, channel_Trace, timeSpan)
           
        This function defines the time span of the diagram in time domain.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:SPAN
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param timeSpan: This control defines time span of the diagram intime domain.

.. method:: GetTimeDomainTimeSpan(self, channel_Trace)
           
        This function queries the time span of the diagram in time domain.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:SPAN?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: timeSpan

.. method:: SetTimeDomainTimeAxisScaling(self, channel_Trace, timeAxisScaling)
           
        This function switches over between the x-axis scaling in time units
        or distance units.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:XAXis TIME | DISTance
        
        

   :param timeAxisScaling: This control switches over between the x-axisscaling in time units or distance units.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetTimeDomainTimeAxisScaling(self, channel_Trace)
           
        This function queries the state of the x-axis scaling in time units or
        distance units.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:XAXis?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: timeAxisScaling

.. method:: SetTimeDomainTransformationType(self, channel_Trace, transformationType)
           
        This function defines time domain transformation type.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME[:TYPE] BPASs | LPASs
        CALCulate<Ch/Tr>:TRANsform:TIME:STIMulus STEP | IMPulse
        
        

   :param transformationType: This control defines time domaintransformation type.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetTimeDomainTransformationType(self, channel_Trace)
           
        This function queries the time domain transformation type.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME[:TYPE]?
        CALCulate<Ch/Tr>:TRANsform:TIME:STIMulus?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: transformationType

.. method:: SetTimeDomainTransformationFilter(self, channel_Trace, filterType)
           
        This function selects the window type for filtering the data in the
        frequency domain prior to the time domain transformation.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:WINDow RECT | HAMMing | HANN | BOHMan
        | DCHebyshev
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param filterType: This control defines time domain transformationfilter.

.. method:: GetTimeDomainTransformationFilter(self, channel_Trace)
           
        This function queries the window type for filtering the data in the
        frequency domain prior to the time domain transformation.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:WINDow?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: filterType

.. method:: SetTimeDomainTransformationSidebandSuppression(self, channel_Trace, sidebandSuppression)
           
        This function sets the sideband suppression for the Dolph-Chebyshev
        window. The command is only available if a Dolph-Chebyshev window is
        active.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:DCHebyshev
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param sidebandSuppression: This control sets the sidebandsuppression for the Dolph-Chebyshev window. The command is onlyavailable if a Dolph-Chebyshev window is active.

.. method:: GetTimeDomainTransformationSidebandSuppression(self, channel_Trace)
           
        This function queries the sideband suppression for the Dolph-Chebyshev
        window. The command is only available if a Dolph-Chebyshev window is
        active.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:DCHebyshev?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: sidebandSuppression

.. method:: SetTimeDomainTransformationResolutionEfactor(self, channel_Trace, resolution)
           
        This function sets the resolution enhancement factor for time domain.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:RESolution:EFACtor
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param resolution: This control sets the resolution enhancementfactor.

.. method:: GetTimeDomainTransformationResolutionEfactor(self, channel_Trace)
           
        This function queries the resolution enhancement factor for time
        domain.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:RESolution:EFACtor?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: resolution

.. method:: SetHarmonicGridAndKeep(self, channel_Trace, calculationMethod)
           
        This function calculates the harmonic grid for low pass time domain
        transforms according to one of the three alternative algorithms.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:LPASs KFSTop | KDFRequency |
        KSDFrequency
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param calculationMethod: This control selects the calculation method.

.. method:: SetDCValue(self, channel_Trace, DCValue)
           
        This function sets the DC value for low pass transforms. The function
        is enabled only if the sweep points are on a harmonic grid (to be set
        explicitly or using CALCulate<Ch/Tr>:TRANsform:TIME:LPASs).
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:LPASs:DCSParam
        
        

   :param DCValue: This control sets the DC value for low passtransforms.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetDCValue(self, channel_Trace)
           
        This function queries the DC value for low pass transforms.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:LPASs:DCSParam?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: DCValue

.. method:: ExtrapolateDCValue(self, channel_Trace)
           
        This function extrapolates the measured trace towards f = 0 and
        overwrites the current DC value
        (CALCulate<Ch/Tr>:TRANsform:TIME:LPASs:DCSParam). The function is
        relevant for low pass time domain transforms.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:LPASs:DCSParam:EXTRapolate
        
        

   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: SetContinuousExtrapolation(self, channel_Trace, continuousExtrapolation)
           
        This function determines whether continuous extrapolation for the DC
        value is enabled.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:LPASs:DCSParam:CONTinuous ON | OFF
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param continuousExtrapolation: This control determines whethercontinuous extrapolation for the DC value is enabled.

.. method:: GetContinuousExtrapolation(self, channel_Trace)
           
        This function queries whether continuous extrapolation for the DC
        value is enabled.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:LPASs:DCSParam:CONTinuous?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: continuousExtrapolation

.. method:: CalculateHarmonicGrid(self, channel_Trace)
           
        This function calculates the harmonic grid for low pass time domain
        transforms, keeping the stop frequency and the number of points.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:TRANsform:TIME:LPFRequency
        
        

   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: SetTimeGateState(self, channel_Trace, timeGate)
           
        This function determines whether the time gate for trace no. <Ch/Tr>
        is enabled.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:STATe ON | OFF
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param timeGate: This control determines whether the time gate fortrace no. <Ch/Tr> is enabled.

.. method:: GetTimeGateState(self, channel_Trace)
           
        This function queries whether the time gate for trace no. <Ch/Tr> is
        enabled.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:STATe?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: timeGate

.. method:: SetTimeGateStartTime(self, channel_Trace, startTime)
           
        This function defines the start time of the time gate.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:STARt
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param startTime: This control defines the start time of the timegate.

.. method:: GetTimeGateStartTime(self, channel_Trace)
           
        This function queries the start time of the time gate.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:STARt?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: startTime

.. method:: SetTimeGateStopTime(self, channel_Trace, stopTime)
           
        This function defines the stop time of the time gate.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:STOP
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param stopTime: This control defines the stop time of the time gate.

.. method:: GetTimeGateStopTime(self, channel_Trace)
           
        This function queries the stop time of the time gate.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:STOP?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: stopTime

.. method:: SetTimeGateCenterTime(self, channel_Trace, centerTime)
           
        This function defines the center time of the time gate.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:CENTer
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param centerTime: This control defines the center time of the timegate.

.. method:: GetTimeGateCenterTime(self, channel_Trace)
           
        This function queries the center time of the time gate.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:CENTer?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: centerTime

.. method:: SetTimeGateType(self, channel_Trace, timeGateType)
           
        This function defines time gate type.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME[:TYPE] BPASs | NOTCh
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param timeGateType: This control defines time gate type.

.. method:: GetTimeGateType(self, channel_Trace)
           
        This function queries time gate type.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME[:TYPE]?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: timeGateType

.. method:: SetTimeGateFilter(self, channel_Trace, filterType)
           
        This function defines time gate filter type, defining what occurs to
        the data in the specific time region.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:WINDow RECT | HAMMing | HANN |
        BOHMan | DCHebyshev
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param filterType: This control defines time gate filter type,defining what occurs to the data in the specific time region.

.. method:: GetTimeGateFilter(self, channel_Trace)
           
        This function queries time gate filter type.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:WINDow?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: filterType

.. method:: SetTimeGateSidebandSuppression(self, channel_Trace, sidebandSuppression)
           
        This function sets the sideband suppression for the Dolph-Chebyshev
        time gate. The command is only available if a Dolph-Chebyshev time
        gate is active.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:DCHebyshev
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param sidebandSuppression: This control sets the sidebandsuppression for the Dolph-Chebyshev time gate. The command is onlyavailable if a Dolph-Chebyshev time gate is active.

.. method:: GetTimeGateSidebandSuppression(self, channel_Trace)
           
        This function queries the sideband suppression for the Dolph-Chebyshev
        time gate.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:DCHebyshev?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: sidebandSuppression

.. method:: SetTimeGateShape(self, channel_Trace, timeGateShape)
           
        This function selects the time gate to be applied to the time domain
        transform.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:SHAPe MAXimum | WIDE | NORMal |
        MINimum
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param timeGateShape: This control selects the time gate to be appliedto the time domain transform.

.. method:: GetTimeGateShape(self, channel_Trace)
           
        This function returns the time gate applied to the time domain
        transform.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:SHAPe?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: timeGateShape

.. method:: SetTimeGateSpan(self, channel_Trace, span)
           
        This function defines the span of the time gate.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:SPAN
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param span: This control defines the span of the time gate.

.. method:: GetTimeGateSpan(self, channel_Trace)
           
        This function returns the span of the time gate.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:SPAN?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: span

.. method:: SetTimeGateDisplayState(self, channel_Trace, timeGateDisplay)
           
        This function determines whether the time gate limits for trace no.
        <Ch/Tr> are displayed permanently.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:STATe ON | OFF
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param timeGateDisplay: This control determines whether the timegate limits for trace no. <Ch/Tr> are displayed permanently.

.. method:: GetTimeGateDisplayState(self, channel_Trace)
           
        This function returns whether the time gate limits for trace no.
        <Ch/Tr> are displayed permanently.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:FILTer[:GATE]:TIME:STATe?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: timeGateDisplay

.. method:: TraceEvaluationRange(self, channel_Trace, evaluationRange, start, stop)
           
        This function define the range for the statistical and phase
        evaluation. The evaluation range is a continuous interval of the sweep
        variable.
        
        It is possible to define and select up to ten different evaluation
        ranges for each setup. Full Span means that the search range is equal
        to the sweep range. The statistical and phase evaluation takes into
        account all measurement points with stimulus values xi between the
        Start and Stop value of the evaluation range:
        
        Start <= xi <= Stop
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:STATistics:DOMain:USER <numeric_value>
        CALCulate<Ch/Tr>:STATistics:DOMain:USER:STARt <numeric_value>
        CALCulate<Ch/Tr>:STATistics:DOMain:USER:STOP <numeric_value>
        
        

   :param start: Defines the start value of the selected evaluationrange.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param stop: Defines the stop value of the selected evaluation range.
   :param evaluationRange: Selects one out of 10 evaluation ranges.

.. method:: TraceStatisticalEvaluation(self, channel_Trace, statisticalParameter, infoField, responseValue_s)
           
        This function selects how to evaluate and display statistical and
        phase information of the entire trace or of a specific evaluation
        range.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:STATistics[:STATe] <Boolean>
        CALCulate<Ch/Tr>:STATistics:RESult? MEAN | STDDev | MAX | MIN | RMS |
        PTPeak | ELENgth | PDELay | ALL | SLOPe | FLATness | GAIN
        
        

   :param infoField: Displays or hides all statistical results in the diagramarea of trace no. <Ch/Tr>.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param responseValue_s: The data is returned as a list of realnumbers. The unit is the default unit of the measured parameter.
   :param statisticalParameter: Define statistical parameter.

.. method:: SetTraceEvaluationRangeShow(self, channel_Trace, showRange)
           
        Displays or hides range limit lines for the evaluation range.
        
        Remote-control command(s):
        CALCulate<Chn>:STATistics:DOMain:USER:SHOW
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param showRange: Displays or hides range limit lines for theevaluation range.

.. method:: GetTraceEvaluationRangeShow(self, channel_Trace)
           
        Queries whether range limit lines for the evaluation range is
        displayed
        
        Remote-control command(s):
        CALCulate<Chn>:STATistics:DOMain:USER:SHOW?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: showRange

.. method:: SetTraceCompressionValue(self, channel_Trace, compressionValue)
           
        This function defines the compression value x for the x-dB compression
        point measurement.
        
        Remote-control command(s):
        CALCulate<Chn>:STATistics:NLINear:COMP:LEVel
        
        

   :param compressionValue: Defines the compression value x for the x-dBcompression point measurement.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetTraceCompressionValue(self, channel_Trace)
           
        This function returns the compression value x for the x-dB compression
        point measurement.
        
        Remote-control command(s):
        CALCulate<Chn>:STATistics:NLINear:COMP:LEVel?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: compressionValue

.. method:: GetTraceCompressionPoint(self, channel_Trace)
           
        This function returns the x-dB compression point of an S-parameter or
        ratio measured in a power sweep. The compression value x is set via
        rszvb_SetTraceCompressionValue
        (CALCulate<Chn>:STATistics:NLINear:COMP:LEVel).
        
        Note(s):
        
        (1) An execution error message (error no. -200) is returned if no
        compression point is found.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:STATistics:NLINear:COMP:RESult?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: compressionPointIn
   :return: compressionPointOut

.. method:: SetDisplayResultsState(self, channel_Trace, resultType, displayResults)
           
        This function displays or hides the Phase Delay/El Length, Min/Max
        /Peak-Peak, Mean/Std Dev, RMS, Gain/Slope/Flatness or Compression
        Point results in the diagram area of trace no. <Chn>.
        
        Remote-control command(s):
        CALCulate<Chn>:STATistics:EPDelay[:STATe] <Boolean>
        CALCulate<Chn>:STATistics:MMPTpeak[:STATe] <Boolean>
        CALCulate<Chn>:STATistics:MSTDdev[:STATe] <Boolean>
        CALCulate<Chn>:STATistics:RMS[:STATe] <Boolean>
        CALCulate<Chn>:STATistics:SFLatness[:STATe] <Boolean>
        CALCulate<Chn>:STATistics:NLINear:COMP[:STATe] <Boolean>
        
        

   :param resultType: This control selects the reuslt type.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param displayResults: Thiscontrol displays or hides the Phase Delay/El Length, Min/Max/Peak-Peak, Mean/Std Dev, RMS, Gain/Slope/Flatness or Compression Pointresults in the diagram area of trace no. <Chn>.

.. method:: GetDisplayResultsState(self, channel_Trace, resultType)
           
        This function returns the Phase Delay/El Length, Min/Max/Peak-Peak,
        Mean/Std Dev, RMS, Gain/Slope/Flatness or Compression Point results
        state.
        
        Remote-control command(s):
        CALCulate<Chn>:STATistics:EPDelay[:STATe]?
        CALCulate<Chn>:STATistics:MMPTpeak[:STATe]?
        CALCulate<Chn>:STATistics:MSTDdev[:STATe]?
        CALCulate<Chn>:STATistics:RMS[:STATe]?
        CALCulate<Chn>:STATistics:SFLatness[:STATe]?
        CALCulate<Chn>:STATistics:NLINear:COMP[:STATe]?
        
        

   :param resultType: This control selects the reuslt type.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: displayResults

.. method:: SetTraceSmoothing(self, channel_Trace, smoothing, aperture)
           
        This function activates the smoothing function for the active trace,
        which may be a data or a memory trace. With active smoothing function,
        each measurement point is replaced by the arithmetic mean value of all
        measurement points located in a symmetric interval centered on the
        stimulus value. The width of the smoothing interval is referred to as
        the Smoothing Apertureand can be adjusted according to the properties
        of the trace.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:SMOothing[:STATe] <Boolean>
        CALCulate<Ch/Tr>:SMOothing:APERture <numeric_value>
        
        

   :param aperture: Defines how many measurement points are averaged tosmooth the trace.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param smoothing: Enables or disables smoothing for trace no.<Ch/Tr>.

.. method:: GetTraceSmoothing(self, channel_Trace)
           
        This function returns state of the smoothing function parameters.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:SMOothing[:STATe]?
        CALCulate<Ch/Tr>:SMOothing:APERture?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: smoothing
   :return: aperture

.. method:: TraceResponseData(self, channel_Trace, dataFormat, traceData)
           
        This function reads the current response values of the active data
        trace or memory trace.
        
        Remote-control command(s):
        FORMat[:DATA] REAL ,32
        CALCulate<Ch/Tr>:DATA? FDATa | SDATa | MDATa | TSData
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param dataFormat: Selects trace data format.
   :param traceData: Returns array of the current response values ofthe active data trace or memory trace.
   :return: noOfValues

.. method:: TraceResponseDataError(self, channel_Trace, errorTerm, traceData)
           
        This function reads the current response values of the active data
        trace or memory trace.
        
        Remote-control command(s):
        FORMat[:DATA] REAL ,32
        CALCulate<Ch/Tr>:DATA? SCORr1 | ... | SCORr27
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param errorTerm: Denotes the error terms generated during acalibration.
   :param traceData: Returns array of the current response values ofthe active data trace or memory trace.
   :return: noOfValues

.. method:: TraceResponseDataAll(self, channel_Trace, dataFormat, traceData)
           
        This function reads the current response values of all traces of the
        current test setup.
        
        Remote-control command(s):
        FORMat[:DATA] REAL ,32
        CALCulate<Ch>:DATA:ALL? FDATa | SDATa | MDATa
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param dataFormat: Selects trace data format.
   :param traceData: Returns the current response values of all tracesof the current test setup.
   :return: noOfValues

.. method:: TraceComplexResponseData(self, channel_Trace, dataFormat, traceData)
           
        Reads the current response values of all S-parameter data traces in
        channel no. <Ch>. If a full n-port system error correction (TOSM, TOM,
        TRL ...) is active in the referenced channel, the command reads the
        full nxn S-matrix of the calibrated ports (there is no need to create
        or display the S-parameter traces). Use
        rszvb_TraceComplexResponseCatalog to query the available traces.
        
        Remote-control command(s):
        FORMat[:DATA] REAL ,32
        CALCulate<Ch>:DATA:CALL? FDATa | SDATa | MDATa
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param dataFormat: Selects trace data format.
   :param traceData: Returns the current response values of allS-parameter data traces in channel no. <Ch>.
   :return: noOfValues

.. method:: TraceComplexResponseCatalog(self, channel_Trace, bufferSize, catalog)
           
        Returns all traces which are available for
        rszvb_TraceComplexResponseData in channel no. <Ch>.
        
        Remote-control command(s):
        CALCulate<Ch>:DATA:CALL:CATalog?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.
   :param catalog: Returns string of values of all S-parameter datatraces in channel no. <Ch>.

.. method:: TraceResponseDataAllData(self, channel_Trace, dataFormat, traceData)
           
        Reads the current response values of all data traces of the current
        test setup.
        
        Remote-control command(s):
        FORMat[:DATA] REAL ,32
        CALCulate<Chn>:DATA:DALL? FDATa | SDATa | MDATa
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param dataFormat: Selects trace data format.
   :param traceData: Returns the current response values of all tracesof the current test setup.
   :return: noOfValues

.. method:: TraceResponseSingleSweepData(self, channel_Trace, sweepNumber, traceData)
           
        This function reads the response values of a trace acquired in single
        sweep mode (INITiate<Ch>:CONTinuous OFF).
        
        Remote-control command(s):
        FORMat[:DATA] REAL ,32
        CALCulate<Ch/Tr>:DATA:NSWeep? SDATa,<Trace_Hist_Count>
        
        

   :param sweepNumber: Number of sweep to be read.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param traceData: Returns array of the response values of a traceacquired in single sweep mode.
   :return: noOfValues

.. method:: TraceResponseSingleSweepDataCount(self, channel_Trace)
           
        This function reads the number of completed sweeps in single sweep
        mode (INITiate<Ch>:CONTinuous OFF). The trace can be any of the traces
        acquired during the single sweep cycle.
        
        Remote-control command(s):
        CALCulate<Chn>:DATA:NSWeep:COUNt?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: sweepCount

.. method:: TraceResponseSingleSweepDataForward(self, channel_Trace, sweepNumber, traceData)
           
        This function reads the response values of a trace acquired in single
        sweep mode (INITiate<Ch>:CONTinuous OFF).
        
        Remote-control command(s):
        FORMat[:DATA] REAL ,32
        CALCulate<Ch/Tr>:DATA:NSWeep:FIRSt? SDATa,<Forward_Count>
        
        

   :param sweepNumber: Number of sweep to be read. 1 denotes the firstsweep acquired, 2 denotes the second and so forth.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param traceData: Returns array of the response values of a traceacquired in single sweep mode.
   :return: noOfValues

.. method:: TraceStimulusData(self, channel_Trace, traceData)
           
        This function reads the stimulus values of the active data or memory
        trace.
        
        Remote-control command(s):
        FORMat[:DATA] REAL ,32
        CALCulate<Ch/Tr>:DATA:STIMulus?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param traceData: Returns array of the current stimnulus values ofthe active data trace or memory trace.
   :return: noOfValues

.. method:: WriteMemoryTraceData(self, channel_Trace, noOfPoints, traceData)
           
        This function writes a memory trace data to the instrument.
        
        Remote-control command(s):
        CALCulate<Chn>:DATA SDATa, <data>
        FORMat ASCII
        FORMat REAL,64
        SYSTem:COMMunicate:GPIB:SELF:RTERminator EOI
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param noOfPoints: Sets the number of trace points to be written tothe instrument.
   :param traceData: Trace data array.

.. method:: WriteMemoryTraceDataExt(self, channel_Trace, dataFormat, noOfPoints, traceData)
           
        This function writes a memory trace data to the instrument.
        
        Remote-control command(s):
        CALCulate<Chn>:DATA FDATa | SDATa | MDATa, <data>
        FORMat ASCII
        FORMat REAL,64
        SYSTem:COMMunicate:GPIB:SELF:RTERminator EOI
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param dataFormat: Selects trace data format.
   :param noOfPoints: Sets the number of trace points to bewritten to the instrument.
   :param traceData: Trace data array.

.. method:: SetTraceFormatZVR(self, dataFormat)
           
        This function defines the format for traces retrieved with the ZVR-
        compatible command TRACe[:DATA][:RESPonse][:ALL]?
        
        Note(s):
        
        (1) This function is ZVR compatible.
        
        Remote-control command(s):
        FORMat:DEXPort:SOURce FDATa | SDATa | MDATa
        
        

   :param dataFormat: Selects trace data format.

.. method:: GetTraceFormatZVR(self, )
           
        This function returns the format for traces retrieved with the ZVR-
        compatible command TRACe[:DATA][:RESPonse][:ALL]?
        
        Remote-control command(s):
        FORMat:DEXPort:SOURce?
        
        

   :return: dataFormat

.. method:: TraceResponseDataZVR(self, dataFormat, valuesToReturn, traceData)
           
        This function returns the response values of the active data trace or
        memory trace.
        
        Note(s):
        
        (1) This function is ZVR compatible.
        
        Remote-control command(s):
        FORMat[:DATA] REAL ,32
        TRACe[:DATA][:RESPonse][:ALL]? CH1DATA | CH2DATA | CH3DATA | CH4DATA |
        CH1MEM | CH2MEM | CH3MEM | CH4MEM | MDATA1 | MDATA2 | MDATA3 | MDATA4
        | MDATA5 | MDATA6 | MDATA7 | MDATA8
        
        

   :param traceData: Returns array of the current response values ofthe active data trace or memory trace.
   :param dataFormat: Selects trace data format.
   :param valuesToReturn: This control sets how much values should bereturned.
   :return: noOfValues

.. method:: TraceStimulusDataZVR(self, dataFormat, valuesToReturn, traceData)
           
        This function returns the stimulus values of the active data trace or
        memory trace.
        
        Note(s):
        
        (1) This function is ZVR compatible.
        
        Remote-control command(s):
        FORMat[:DATA] REAL,64
        TRACe[:DATA]:STIMulus[:ALL]? CH1DATA | CH2DATA | CH3DATA | CH4DATA |
        CH1MEM | CH2MEM | CH3MEM | CH4MEM | MDATA1 | MDATA2 | MDATA3 | MDATA4
        | MDATA5 | MDATA6 | MDATA7 | MDATA8
        
        

   :param traceData: Returns array of the current response values ofthe active data trace or memory trace.
   :param dataFormat: Selects trace data format.
   :param valuesToReturn: This control sets how much values should bereturned.
   :return: noOfValues

.. method:: TraceResponseDataSParameterGroup(self, channel_Trace, dataFormat, valuesToReturn, traceData)
           
        This function reads the current response values of all S-parameters
        associated to a group of logical ports (S-parameter group). The
        S-parameter group must be created before using
        CALCulate<Ch>:PARameter:DEFine:SGRoup.
        
        Remote-control command(s):
        FORMat[:DATA] REAL ,32
        CALCulate<Ch>:DATA:SGRoup? FDATa | SDATa | MDATa
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param dataFormat: Selects trace data format.
   :param valuesToReturn: This control sets how much valuesshould be returned.
   :param traceData: Returns array of the current response values ofall S-parameters associated to a group of logical ports (S-parametergroup).
   :return: noOfValues

.. method:: TraceImportData(self, traceName, fileName)
           
        This function loads trace data from a specified trace file and assigns
        it to a trace with a specified name.
        
        Note(s):
        
        Traces are created using the CALCulte<Ch>:PARameter:SDEFine...
        command.
        
        Remote-control command(s):
        MMEMory:LOAD:TRACe '<trc_name>','<file_name>'[,'<parameter_name>']
        
        

   :param fileName: String parameter to specify the name and directoryof the trace file to be loaded. Several file formats for trace filesare supported. If no path is specified the analyzer searches thecurrent directory, to be queried with MMEMory:CDIRectory?.
   :param traceName: Name of an existing data tracein the active setup (string parameter). The trace data is loaded intoa memory trace associated with the specified data trace. If one ormore memory traces are already associated with the specified datatrace, the last generated memory trace is overwritten.

.. method:: TraceExportData(self, traceName, fileName)
           
        This function stores the trace data of a specified trace to a trace
        file.
        
        Note(s):
        
        Traces are created using the CALCulte<Ch>:PARameter:SDEFine...
        command.
        
        *.s<n>p touchstone files (<n> = 2, 3, 4) are intended for a complete
        set of <n>-port S-parameters. Data export fails if the active channel
        does not contain the full set of <n>^2 traces. If the necessary trace
        are available, '<trc_name>' can be the name of any of the traces.
        
        Remote-control command(s):
        MMEMory:STORe:TRACe '<trc_name>','<file_name>'
        
        

   :param fileName: String parameter to specify the name and directoryof the created trace file. Several file formats for trace files aresupported. If no path is specified the analyzer uses theC:\Rohde&Schwarz\NWA\Traces directory.
   :param traceName: Name of an existing data tracein the active setup (string parameter).

.. method:: TraceExportDataWithOptions(self, traceName, fileName, exportFormat, exportData)
           
        This function stores the trace data of a specified trace to a trace
        file.
        
        Note(s):
        
        Traces are created using the CALCulte<Ch>:PARameter:SDEFine...
        command.
        
        *.s<n>p touchstone files (<n> = 2, 3, 4) are intended for a complete
        set of <n>-port S-parameters. Data export fails if the active channel
        does not contain the full set of <n>^2 traces. If the necessary trace
        are available, '<trc_name>' can be the name of any of the traces.
        
        Remote-control command(s):
        MMEMory:STORe:TRACe '<trc_name>','<file_name>'[,UNFormatted |
        FORMatted, COMPlex | LINPhase | LOGPhase]
        
        

   :param exportData: This control selects the export data.
   :param fileName: String parameter to specify the name and directoryof the created trace file. Several file formats for trace files aresupported. If no path is specified the analyzer uses theC:\Rohde&Schwarz\NWA\Traces directory.
   :param exportFormat: This control selects the export format.
   :param traceName: Name of an existing data tracein the active setup (string parameter).

.. method:: TraceExportDataWithOptionsExt(self, traceName, fileName, exportFormat, exportData, decimalSeparator, fieldSeparator)
           
        This function stores the trace data of a specified trace to a trace
        file.
        
        Note(s):
        
        Traces are created using the CALCulte<Ch>:PARameter:SDEFine...
        command.
        
        *.s<n>p touchstone files (<n> = 2, 3, 4) are intended for a complete
        set of <n>-port S-parameters. Data export fails if the active channel
        does not contain the full set of <n>^2 traces. If the necessary trace
        are available, '<trc_name>' can be the name of any of the traces.
        
        Remote-control command(s):
        MMEMory:STORe:TRACe '<trc_name>','<file_name>'[,UNFormatted |
        FORMatted, COMPlex | LINPhase | LOGPhase, POINt | COMMa, SEMicolon |
        COMMa | TABulator | SPACe]
        
        

   :param exportFormat: This control selects the export format.
   :param decimalSeparator: This controlselects the decimal separator.
   :param fieldSeparator: This controlselects the field separator.
   :param exportData: This control selects the export data.
   :param fileName: String parameter to specify the name and directoryof the created trace file. Several file formats for trace files aresupported. If no path is specified the analyzer uses theC:\Rohde&Schwarz\NWA\Traces directory.
   :param traceName: Name of an existing data tracein the active setup (string parameter).

.. method:: ChannelTraceExportData(self, selectChannel, channel_Trace, fileName)
           
        This function stores the trace data of all data traces in the
        specified channel to a trace file.
        
        Note(s):
        
        Traces are created using the CALCulte<Ch>:PARameter:SDEFine...
        command.
        
        *.s<n>p Touchstone files (<n> = 1, 2, 3, ...) are intended for a
        complete set of <n>-port S-parameters. Data export fails if the active
        channel does not contain the full set of <n>^2 traces.
        
        
        Remote-control command(s):
        MMEMory:STORe:TRACe:CHANnel <ch_number> | ALL,'<file_name>'
        
        

   :param channel_Trace: Channel number used to identify the active trace.
   :param selectChannel: This control selects thechannel in the active setup.
   :param fileName: String parameter to specify the name and directoryof the created trace file. Several file formats for trace files aresupported. If no path is specified the analyzer uses theC:\Rohde&Schwarz\NWA\Traces directory.

.. method:: ChannelTraceExportDataWithOptions(self, selectChannel, channel_Trace, fileName, exportFormat, exportData)
           
        This function stores the trace data of all data traces in the
        specified channel to a trace file.
        
        Note(s):
        
        Traces are created using the CALCulte<Ch>:PARameter:SDEFine...
        command.
        
        *.s<n>p Touchstone files (<n> = 1, 2, 3, ...) are intended for a
        complete set of <n>-port S-parameters. Data export fails if the active
        channel does not contain the full set of <n>^2 traces.
        
        
        Remote-control command(s):
        MMEMory:STORe:TRACe:CHANnel <ch_number> |
        ALL,'<file_name>'[,UNFormatted | FORMatted, COMPlex | LINPhase |
        LOGPhase]
        
        

   :param exportData: This control selects the export data.
   :param channel_Trace: Channel number used to identify the active trace.
   :param exportFormat: This control selects the export format.
   :param selectChannel: This control selects thechannel in the active setup.
   :param fileName: String parameter to specify the name and directoryof the created trace file. Several file formats for trace files aresupported. If no path is specified the analyzer uses theC:\Rohde&Schwarz\NWA\Traces directory.

.. method:: ChannelTraceExportDataWithOptionsExt(self, selectChannel, channel_Trace, fileName, exportFormat, exportData, decimalSeparator, fieldSeparator)
           
        This function stores the trace data of all data traces in the
        specified channel to a trace file.
        
        Note(s):
        
        Traces are created using the CALCulte<Ch>:PARameter:SDEFine...
        command.
        
        *.s<n>p Touchstone files (<n> = 1, 2, 3, ...) are intended for a
        complete set of <n>-port S-parameters. Data export fails if the active
        channel does not contain the full set of <n>^2 traces.
        
        
        Remote-control command(s):
        MMEMory:STORe:TRACe:CHANnel <ch_number> |
        ALL,'<file_name>'[,UNFormatted | FORMatted, COMPlex | LINPhase |
        LOGPhase, POINt | COMMa, SEMicolon | COMMa | TABulator | SPACe]
        
        

   :param decimalSeparator: This controlselects the decimal separator.
   :param selectChannel: This control selects thechannel in the active setup.
   :param fileName: String parameter to specify the name and directoryof the created trace file. Several file formats for trace files aresupported. If no path is specified the analyzer uses theC:\Rohde&Schwarz\NWA\Traces directory.
   :param channel_Trace: Channel number used to identify the active trace.
   :param fieldSeparator: This controlselects the field separator.
   :param exportData: This control selects the export data.
   :param exportFormat: This control selects the export format.

.. method:: TraceExportDataPorts(self, channel=1, fileName, exportData, port1, port2, port3, port4)
           
        This function stores the trace data to a Touchstone file for the
        specified ports. The Touchstone file (.s<n>p where <n> is the number
        of ports) contains a full set of <n>2 single-ended S-parameters for
        the selected ports.
        
        Note(s):
        
        (1) Traces are created using the CALCulte<Ch>:PARameter:SDEFine...
        command.
        
        (2) The function fails unless the following conditions are met:
        
        - For a one-port Touchstone file, the reflection coefficient for the
        specified port (e.g. S11 for port no. 1) must be measured. If a full
        one-port system error correction is available for the specified port,
        it is also possible to export transmission parameters that are related
        to the calibrated port (e.g. S12 or S21 for port no. 1).
        
        - For a multiport Touchstone file, a full multiport system error
        correction must be available. It is not necessary to measure the full
        set of S-parameters. Moreover, if the port configuration contains
        balanced ports, the Touchstone file will contain the converted single-
        ended S-parameters.
        
        Remote-control command(s):
        MMEMory:STORe:TRACe:PORTs
        
        

   :param fileName: String parameter to specify the name and directoryof the created trace file. Several file formats for trace files aresupported. If no path is specified the analyzer uses theC:\Rohde&Schwarz\NWA\Traces directory.
   :param exportData: This control selects the export data.
   :param port4: Forth port number.
   :param port2: Second port number.
   :param port3: Third port number.
   :param channel: Channel number used to identifythe active trace.
   :param port1: First port number.

.. method:: TraceExportDataPortsIncomplete(self, channel=1, fileName, exportData, port1, port2, port3, port4)
           
        This function exports a (possibly) incomplete, uncalibrated set of
        S-parameters to an n-port Touchstone file (n > 1).
        The missing S-parameter columns are filled by zeros (Replace Missing
        Values by 0).
        
        Remote-control command(s):
        MMEMory:STORe:TRACe:PORTs:INComplete
        
        

   :param fileName: String parameter to specify the name and directoryof the created trace file. Several file formats for trace files aresupported. If no path is specified the analyzer uses theC:\Rohde&Schwarz\NWA\Traces directory.
   :param exportData: This control selects the export data.
   :param port4: Forth port number.
   :param port2: Second port number.
   :param port3: Third port number.
   :param channel: Channel number used to identifythe active trace.
   :param port1: First port number.

.. method:: SetRenormalizationState(self, state)
           
        Enables or disables renormalization during Touchstone file export and
        import.
        
        Remote-control command(s):
        MMEMory:SETTings:RENorm:STATe
        
        

   :param state: Enables or disablesrenormalization during Touchstone file export and import.

.. method:: GetRenormalizationState(self, )
           
        Returns state of renormalization during Touchstone file export and
        import.
        
        Remote-control command(s):
        MMEMory:SETTings:RENorm:STATe?
        
        

   :return: state

.. method:: SetRenormalizationMode(self, mode)
           
        This function controls the renormalization rules for data export and
        import globally.
        
        Remote-control command(s):
        MMEMory:SETTings:RENorm:MODE
        
        

   :param mode: Controls the renormalization rulesfor data export and import globally.

.. method:: GetRenormalizationMode(self, )
           
        This function returns the renormalization rules for data export and
        import globally.
        
        Remote-control command(s):
        MMEMory:SETTings:RENorm:MODE?
        
        

   :return: mode

.. method:: SetRenormalizationImpedance(self, impedance)
           
        Defines the target reference impedance for S-matrix export. The value
        is written into the file header of the generated Touchstone file. If
        renormalization is enabled (rszvb_SetRenormalizationState is set to
        On), it is also used for renormalization.
        
        Remote-control command(s):
        MMEMory:SETTings:RENorm:RIMPedance
        
        

   :param impedance: Defines the target referenceimpedance for S-matrix export.

.. method:: GetRenormalizationImpedance(self, )
           
        Returns the target reference impedance for S-matrix export.
        
        Remote-control command(s):
        MMEMory:SETTings:RENorm:RIMPedance?
        
        

   :return: impedance

.. method:: TraceShiftStimulusValue(self, window, window_Trace, shiftStimulusValue)
           
        This function shifts the active trace in horizontal direction, leaving
        the positions of all markers unchanged. The positive or negative
        offset value for the stimulus variable is entered into an input field.
        The unit depends on the sweep type.
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:X:OFFSet <numeric_value>
        
        

   :param window: Number of the diagram area.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :param shiftStimulusValue: Stimulus offset value.

.. method:: TraceShiftResponseValue(self, window, window_Trace, magnitude, phase, real, imaginary)
           
        This function modifies all points of the trace <WndTr> by means of an
        added and/or a multiplied complex constant. The response values M of
        the trace are transformed according to:
        
        M_new = M_old * 10^(<Magnitude> / 20dB) * a * e^(j <Phase> / 180Deg) +
        <Real> + j <Imaginary>
        
        Note(s):
        
        (1) Window:
        Number of an existing diagram area (defined by means of
        DISPlay:WINDow<Wnd>:STATe ON).
        
        (2) Window (Trace):
        Existing trace number, assigned by means of
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:Y:OFFSet <Magnitude>[,<Phase>,
        <Real>, <Imaginary>]
        
        

   :param real: The real added constant shifts a real trace in verticaldirection, leaving the imaginary part unchanged.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :param window: Number of the diagram area.
   :param magnitude: The magnitude factor shifts a dB Mag trace invertical direction, leaving the phase of a complex parameterunchanged.
   :param phase: The phase factor rotates a trace that is displayed in apolar diagram around the origin, leaving the magnitude unchanged.
   :param imaginary: The imaginary added constant shifts a imaginary trace in vertical direction, leaving the real part unchanged.

.. method:: SetHold(self, channel=1, hold)
           
        This function enables, disables, or restarts the max hold and the min
        hold functions
        
        Remote-control command(s):
        CALCulate<Chn>:PHOLd MIN | MAX | OFF
        
        

   :param hold: Enables, disables, or restarts the max hold and the minhold functions
   :param channel: Channel number.

.. method:: GetHold(self, channel=1)
           
        This function returns the state of the max hold and the min hold
        functions
        
        Remote-control command(s):
        CALCulate<Chn>:PHOLd?
        
        

   :param channel: Channel number.
   :return: hold

.. method:: LinearityDeviationManual(self, channel=1, slope, constant, electricalLength)
           
        This function is used for manual entry of the correction factors.
        
        Note(s):
        
        (1) Electrical length is available if the active trace format is Phase
        or Unwrapped Phase, or if a mixer delay is measured.
        
        Remote-control command(s):
        CALCulate<Chn>:LDEViation:SLOPe
        CALCulate<Chn>:LDEViation:CONStant
        CALCulate<Chn>:LDEViation:ELENgth
        
        

   :param slope: This control defines the slope of the regression linefor the linearity deviation calculation.
   :param electricalLength: This control definesthe electrical length for the linearity deviation calculation. Thiscontrol is available if the active trace format is Phase or UnwrappedPhase, or if a mixer delay is measured.
   :param constant: This control defines theconstant value for the linearity deviation calculation.
   :param channel: Channel number.

.. method:: LinearityDeviationAuto(self, channel=1)
           
        This function initiates a (re-)calculation of the linearity deviation
        correction factors and applies them to the active trace.
        
        Remote-control command(s):
        CALCulate<Chn>:LDEViation:AUTO ONCE
        
        

   :param channel: Channel number.

.. method:: SetLinearityDeviationState(self, channel=1, state)
           
        This function applies /discards the correction factors or re-
        calculates them for each trace (Tracking).
        
        Remote-control command(s):
        CALCulate<Chn>:LDEViation:MODE ON | OFF | TRACking
        
        

   :param state: This control applies /discards the correction factors orre-calculates them for each trace (Tracking).
   :param channel: Channel number.

.. method:: GetLinearityDeviationState(self, channel=1)
           
        This function returns the state of the linearity deviation.
        
        Remote-control command(s):
        CALCulate<Chn>:LDEViation:MODE?
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetLinearityDeviationSlope(self, channel=1, slope)
           
        This function defines the slope of the regression line for the
        linearity deviation calculation.
        
        Remote-control command(s):
        CALCulate<Chn>:LDEViation:SLOPe
        
        

   :param slope: This control defines the slope of the regression linefor the linearity deviation calculation.
   :param channel: Channel number.

.. method:: GetLinearityDeviationSlope(self, channel=1)
           
        This function returns the slope of the regression line for the
        linearity deviation calculation.
        
        Remote-control command(s):
        CALCulate<Chn>:LDEViation:SLOPe?
        
        

   :param channel: Channel number.
   :return: slope

.. method:: SetLinearityDeviationConstant(self, channel=1, constant)
           
        This function defines the constant value for the linearity deviation
        calculation.
        
        Remote-control command(s):
        CALCulate<Chn>:LDEViation:CONStant
        
        

   :param constant: This control defines the constant value for thelinearity deviation calculation.
   :param channel: Channel number.

.. method:: GetLinearityDeviationConstant(self, channel=1)
           
        This function returns the constant value for the linearity deviation
        calculation.
        
        Remote-control command(s):
        CALCulate<Chn>:LDEViation:CONStant?
        
        

   :param channel: Channel number.
   :return: constant

.. method:: SetLinearityDeviationElectricalLength(self, channel=1, electricalLength)
           
        This function defines the electrical length for the linearity
        deviation calculation.
        
        Note(s):
        
        (1) Electrical length is available if the active trace format is Phase
        or Unwrapped Phase, or if a mixer delay is measured.
        
        Remote-control command(s):
        CALCulate<Chn>:LDEViation:ELENgth
        
        

   :param electricalLength: This control defines the electrical lengthfor the linearity deviation calculation.
   :param channel: Channel number.

.. method:: GetLinearityDeviationElectricalLength(self, channel=1)
           
        This function returns the electrical length for the linearity
        deviation calculation.
        
        Note(s):
        
        (1) Electrical length is available if the active trace format is Phase
        or Unwrapped Phase, or if a mixer delay is measured.
        
        Remote-control command(s):
        CALCulate<Chn>:LDEViation:ELENgth?
        
        

   :param channel: Channel number.
   :return: electricalLength

.. method:: SetMarkerState(self, channel_Trace, marker, markerState)
           
        This function creates the marker numbered <Mk> and assigns it to trace
        no. <Ch/Tr>.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>[:STATe] <Boolean>
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param markerState: Creates or removes the marker.

.. method:: GetMarkerState(self, channel_Trace, marker)
           
        This function returns if the marker numbered <Mk> is assigned to trace
        no. <Ch/Tr>.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>[:STATe]?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: markerState

.. method:: SetMarkerStimulus(self, channel_Trace, marker, markerStimulus)
           
        This function defines the stimulus (in Cartesian diagrams: x-axis)
        value of the marker no. <Mk>, which can (but doesn't have to) be
        created using CALCulate<Ch/Tr>:MARKer<Mk>[:STATe] ON.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:X <numeric_value>
        
        

   :param marker: Marker number.
   :param markerStimulus: Stimulus value of marker no. <Mk>.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetMarkerStimulus(self, channel_Trace, marker)
           
        This function returns the stimulus (in Cartesian diagrams: x-axis)
        value of the marker no. <Mk>, which can (but doesn't have to) be
        created using CALCulate<Ch/Tr>:MARKer<Mk>[:STATe] ON.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:X?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: markerStimulus

.. method:: GetMarkerResponse(self, channel_Trace, marker, markerResponse)
           
        This function returns the response (in Cartesian diagrams: y-axis)
        value of marker no. <Mk>. The marker must be created before using
        CALCulate<Ch/Tr>:MARKer<Mk>[:STATe] ON.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:Y?
        
        

   :param marker: Marker number.
   :param markerResponse: Response value(s) of marker no. <Mk>. Unitis depending on the marker format; seeCALCulate<Ch/Tr>:MARKer<Mk>:FORMat.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: SetReferenceMarkerState(self, channel_Trace, marker, referenceMarkerState)
           
        This function creates the reference marker and assigns it to trace no.
        <Ch/Tr>.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:REFerence[:STATe] <Boolean>
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param referenceMarkerState: Creates or removes the referencemarker.

.. method:: GetReferenceMarkerState(self, channel_Trace, marker)
           
        This function returns if the reference marker numbered <Mk> is
        assigned to trace no. <Ch/Tr>.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:REFerence[:STATe]?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: referenceMarkerState

.. method:: SetReferenceMarkerStimulus(self, channel_Trace, marker, referenceMarkerStimulus)
           
        This function defines the stimulus (in Cartesian diagrams: x-axis)
        value of the reference marker, which can (but doesn't have to) be
        displayed using CALCulate<Ch/Tr>:MARKer<Mk>:REFerence[:STATe] ON.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:REFerence:X <numeric_value>
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param referenceMarkerStimulus: Stimulus value of reference marker no. <Mk>.

.. method:: GetReferenceMarkerStimulus(self, channel_Trace, marker)
           
        This function returns the stimulus (in Cartesian diagrams: x-axis)
        value of the reference marker, which can (but doesn't have to) be
        displayed using CALCulate<Ch/Tr>:MARKer<Mk>:REFerence[:STATe] ON.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:REFerence:X?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: referenceMarkerStimulus

.. method:: GetReferenceMarkerResponse(self, channel_Trace, marker)
           
        This function returns the response (in Cartesian diagrams: y-axis)
        value of the reference marker. The reference marker must be created
        before using CALCulate<Ch/Tr>:MARKer<Mk>:REFerence[:STATe] ON.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:REFerence:Y?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: referenceMarkerResponse

.. method:: SetReferenceDiscreteMarker(self, channel_Trace, marker, mode)
           
        Sets the reference marker to continuous or discrete mode. The marker doesn't have to be created before
        (CALCulate<Chn>:MARKer<Mk>:REFerence[:STATe] ON), the mode can be
        assigned in advance.
        
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:REFerence:MODE CONTinuous | DISCrete
        
        

   :param marker: Marker number
   :param channel_Trace: Channel number used toidentify the active trace.
   :param mode: Sets marker no. <Mk> to continuous or discrete mode.

.. method:: GetReferenceDiscreteMarker(self, channel_Trace, marker)
           
        Gets the reference marker mode.
        
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:REFerence:MODE?
        
        
        

   :param marker: Marker number
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: mode

.. method:: SetReferenceFixedMarker(self, channel_Trace, marker, type)
           
        Sets the reference to normal or fixed mode. The marker must be created
        before using CALCulate<Chn>:MARKer<Mk>:REFerence[:STATe] ON.
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:REFerence:TYPE NORMal | FIXed
        
        

   :param marker: Marker number
   :param channel_Trace: Channel number used toidentify the active trace.
   :param type: Sets marker no. <Mk> to normal or fixed mode.

.. method:: GetReferenceFixedMarker(self, channel_Trace, marker)
           
        Gets the reference marker type.
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:REFerence:TYPE?
        
        

   :param marker: Marker number
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: type

.. method:: SetDeltaMarkerState(self, channel_Trace, marker, deltaMarkerState)
           
        This function switches the delta mode for marker <Mk> on trace no.
        <Ch/Tr> on or off. The marker must be created before using
        CALCulate<Ch/Tr>:MARKer<Mk>[:STATe] ON. If the active trace contains
        no reference marker, the command also creates a reference marker.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:DELTa[:STATe] <Boolean>
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param deltaMarkerState: Enables or disables the delta mode.

.. method:: GetDeltaMarkerState(self, channel_Trace, marker)
           
        This function returns if the delta mode for marker <Mk> on trace no.
        <Ch/Tr> is on or off.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:DELTa[:STATe]?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: deltaMarkerState

.. method:: SetCoupledMarkers(self, channel_Trace, marker, markerCoupled)
           
        This function couples the markers of all traces in the active setup to
        the markers of trace no. <Ch/Tr>, provided that they have the same
        sweep type (SENSe<Ch/Tr>:FUNCtion).
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:COUPled[:STATe] <Boolean>
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param markerCoupled: Enables or disables marker coupling.

.. method:: GetCoupledMarkers(self, channel_Trace, marker)
           
        This function returns if the markers of all traces in the active setup
        are coupled to the markers of trace no. <Ch/Tr>.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:COUPled[:STATe]?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: markerCoupled

.. method:: SetDiscreteMarker(self, channel_Trace, marker, discreteMode)
           
        This function sets marker no. <Mk> to continuous or discrete mode. The
        marker doesn't have to be created before
        (CALCulate<Ch/Tr>:MARKer<Mk>[:STATe] ON), the mode can be assigned in
        advance.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:MODE CONTinuous | DISCrete
        
        

   :param marker: Marker number.
   :param discreteMode: Sets marker no. <Mk> to continuous or discretemode.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetDiscreteMarker(self, channel_Trace, marker)
           
        This function returns if marker no. <Mk> is set to continuous or
        discrete mode.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:MODE?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: discreteMode

.. method:: SetFixedMarker(self, channel_Trace, marker, fixedMarker)
           
        This function sets marker no. <Mk> to normal or fixed mode. The marker must be created before using CALCulate<Ch/Tr>:MARKer<Mk>[:STATe] ON.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:TYPE NORMal | FIXed
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param fixedMarker: Sets marker no. <Mk> to normal or fixed mode.

.. method:: GetFixedMarker(self, channel_Trace, marker)
           
        This function returns if marker no. <Mk> is set to normal or fixed
        mode.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:TYPE?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: fixedMarker

.. method:: SetMarkerFormat(self, channel_Trace, marker, markerFormat)
           
        This function defines the output format for the (complex) value of
        marker <Mk> on trace no. <Ch/Tr>.
        
        Note(s):
        
        The formats of the markers assigned to a trace are independent of each
        other and of the trace format settings; see CALCulate<Ch/Tr>:FORMat.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FORMat MLINear | MLOGarithmic | PHASe |
        POLar | COMPlex | GDELay | REAL | IMAGinary | SWR | LINPhase |
        LOGPhase | IMPedance | ADMittance | MDB | MLPHas | MDPHase
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param markerFormat: The formats of the markers assigned to a traceare independent of each other and of the trace format settings.

.. method:: GetMarkerFormat(self, channel_Trace, marker)
           
        This function returns the output format of the (complex) value of
        marker <Mk> on trace no. <Ch/Tr>.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FORMat?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: markerFormat

.. method:: SetAllMarkersOff(self, channel_Trace)
           
        This function removes all markers from all traces of the active setup.
        The removed markers remember their properties (stimulus value, format,
        delta mode, number) when they are restored (CALC<Ch/Tr>:MARK<Mk> ON).
        The marker properties are definitely lost if the associated trace is
        deleted.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:AOFF
        
        

   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: SaveAllMarkers(self, fileName)
           
        This function saves the values of all markers to a ASCII file.
        
        Remote-control command(s):
        MMEMory:STORe:MARKer '<file_name>'
        
        

   :param fileName: This control specifies the nameand directory of the created ASCII file. The default extension (manualcontrol) for marker files is *.txt, although other extensions areallowed. If no path is specified the analyzer uses the currentdirectory, to be queried with MMEMory:CDIRectory?.

.. method:: MarkerSearch(self, channel_Trace, marker, search)
           
        This function search with the active marker for specific points on the
        trace.
        
        Note(s):
        
        The marker must be created before using
        CALCulate<Ch/Tr>:MARKer<Mk>[:STATe] ON.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:EXECute MAXimum | MINimum | NPEak
        | RPEak | LPEak
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param search: Sets the active marker to specific points on the trace.

.. method:: MarkerTargetSearch(self, channel_Trace, marker, search)
           
        This function search with the active marker for target value on the
        trace.
        
        Note(s):
        
        The marker must be created before using
        CALCulate<Ch/Tr>:MARKer<Mk>[:STATe] ON.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:EXECute TARGet | RTARget |
        LTARget
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param search: Sets the active marker to specific points on the trace.

.. method:: SetMarkerTargetValue(self, channel_Trace, marker, targetValue)
           
        This function defines the target value for the target search of marker no. <Mk>, which can be activated using
        CALCulate<Ch/Tr>:MARKer<Mk>:FUCTion:EXECute TARGet.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:TARGet <numeric_value>
        
        

   :param marker: Marker number.
   :param targetValue: Defines the target value for the target search.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetMarkerTargetValue(self, channel_Trace, marker)
           
        This function returns the target value for the target search of marker no. <Mk>, which can be activated using
        CALCulate<Ch/Tr>:MARKer<Mk>:FUCTion:EXECute TARGet.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:TARGet?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: targetValue

.. method:: MarkerBandpassSearch(self, channel_Trace, marker)
           
        This function activates the search for a bandpass region on the active
        trace. A bandpass region is the tallest peak in the search range with
        a minimum excursion specified by means of the x dB Bandwidth
        parameter.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:BWIDth:MODE BPASs
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:EXECute BFILter
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: MarkerBandstopSearch(self, channel_Trace, marker)
           
        This function activates the search for a bandstop region on the active
        trace. A bandstop region is the lowest peak (local minimum) in the
        search range with a minimum excursion that is specified by means of
        the x dB Bandwidth parameter.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:BWIDth:MODE BSTOP
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:EXECute BFILter
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: SetMarkerSearchMode(self, channel_Trace, marker, searchMode)
           
        This function selects the bandfilter search mode.
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:FUNCtion:BWIDth:MODE
        BPASs | BSTop | BPRMarker | BSRMarker | BPABsolute | BSABsolute
        
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param searchMode: This control selects the bandfilter search mode.

.. method:: GetMarkerSearchMode(self, channel_Trace, marker)
           
        This function returns the bandfilter search mode.
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:FUNCtion:BWIDth:MODE?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: searchMode

.. method:: MarkerBandfilterTracking(self, channel_Trace, marker, bandfilterTracking)
           
        This function causes the bandfilter search to be repeated after each
        sweep: When tracking mode is active the markers typically change their
        horizontal and their vertical positions as the measurement goes on.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:EXECute BFILter
        CALCulate<Ch/Tr>:MARKer<Mk>:SEARch:TRACking <Boolean>
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param bandfilterTracking: Enables or disables the bandfiltertracking mode.

.. method:: MarkerxdBBandwidth(self, channel_Trace, marker, xDBBandwidth)
           
        This function defines the bandfilter level, i.e. the minimum excursion
        for the bandpass and bandstop peaks.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:BWIDth <x_dB_Bandwidth>
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param xDBBandwidth: Defines x dB Bandwidth parameter. The x dBBandwidth is the difference between the band edges and the centerresponse value of a bandfilter peak; it must be negative for abandpass search and positive for a bandstop search.

.. method:: MarkerBandfilterResults(self, channel_Trace, marker)
           
        This function returns the results of a bandpass or a bandstop filter
        search. Result is only available after a bandfilter search has been
        executed.
        
        Note(s):
        
        Units of the result values depends on the sweep type and the marker format; see CALCulate<Ch/Tr>:MARKer<Mk>:FORMat.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:BWIDth?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: bandwidth
   :return: centerStimulus
   :return: q
   :return: loss
   :return: LBE
   :return: UBE

.. method:: MarkerxdBBandwidthZVR(self, channel_Trace, marker, xDBBandwidth)
           
        This function defines the bandfilter level, i.e. the minimum excursion
        for the bandpass and bandstop peaks.
        
        Note(s):
        
        (1) This function is ZVR compatible.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:BWIDth <x_dB_Bandwidth>
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param xDBBandwidth: Defines x dB Bandwidth parameter.

.. method:: MarkerBandfilterResultsZVR(self, channel_Trace, marker)
           
        This function returns the results of a bandpass or a bandstop filter
        search.
        
        Note(s):
        
        (1) This function is ZVR compatible.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:BWIDth?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: bandwidth

.. method:: SetMarkerSearchResultState(self, channel_Trace, marker, searchResults)
           
        This function shows or hides the bandfilter search results in the
        diagram area.
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:FUNCtion:EXECute BFILter
        CALCulate<Chn>:MARKer<Mk>:SEARch:BFILter:RESult[:STATe] <Boolean>
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param searchResults: Shows or hides the bandfilter search resultsin the diagram area.

.. method:: GetMarkerSearchResultState(self, channel_Trace, marker)
           
        This function returns the bandfilter search results state.
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:SEARch:BFILter:RESult[:STATe]?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: searchResults

.. method:: SetMarkerTracking(self, channel_Trace, marker, markerTracking)
           
        This function enables or disables the marker tracking mode for marker no. <Mk>. Tracking mode causes the active minimum/maximum or target
        search of the active marker to be repeated after each sweep.
        
        Note(s):
        
        (1) A marker must be created and a search mode must be active
        (CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:EXECute ...) to use this
        function.
        
        (2) If the current search mode is a bandfilter search this function
        enables or disables bandfilter tracking.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:SEARch:TRACking <Boolean>
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param markerTracking: Enables or disables the marker tracking mode.

.. method:: GetMarkerTracking(self, channel_Trace, marker)
           
        This function returns whether the marker tracking mode for marker no.
        <Mk> is enabled or disabled. Tracking mode causes the active
        minimum/maximum or target search of the active marker to be repeated
        after each sweep.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:SEARch:TRACking?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: markerTracking

.. method:: MarkerSearchRange(self, channel_Trace, marker, searchRange, start, stop)
           
        This function defines search ranges for the maximum/minimum or target
        search. Assigns a search range to marker and define the start and stop values.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:DOMain:USER <numeric_value>
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:DOMain:USER:STARt <numeric_value>
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:DOMain:USER:STOP <numeric_value>
        
        

   :param marker: Marker number.
   :param searchRange: Selects one out of 10 search ranges.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param stop: Defines the stop value of the selected search range.
   :param start: Defines the start value of the selected search range.

.. method:: SetMarkerSearchRangeShow(self, channel_Trace, marker, showRange)
           
        Displays or hides range limit lines for the search range.
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:FUNCtion:DOMain:USER:SHOW
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param showRange: Displays or hides range limit lines for the searchrange.

.. method:: GetMarkerSearchRangeShow(self, channel_Trace, marker)
           
        Queries whether range limit lines for the search range are displayed.
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:FUNCtion:DOMain:USER:SHOW?
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: showRange

.. method:: MarkerSearchResults(self, channel_Trace, marker, markerResponse)
           
        This function Returns the result (stimulus and response value) of a
        search started by means of
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:EXECute. The search must be
        executed before the command is enabled.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:RESult?
        
        

   :param marker: Marker number.
   :param markerResponse: Response value(s) of marker no. <Mk>. Unitis depending on the marker format; seeCALCulate<Ch/Tr>:MARKer<Mk>:FORMat.
   :param channel_Trace: Channel number used toidentify the active trace.
   :return: markerStimulus

.. method:: SetStartToMarker(self, channel_Trace, marker)
           
        This function sets the beginning (start) of the sweep range equal to
        the stimulus value of the marker <Mk> on trace no. <Ch/Tr>.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:STARt
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: SetStopToMarker(self, channel_Trace, marker)
           
        This function sets the end (stop) of the sweep range equal to the
        stimulus value of the marker <Mk> on trace no. <Ch/Tr>.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:STOP
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: SetCenterToMarker(self, channel_Trace, marker)
           
        This function sets the center of the sweep range equal to the stimulus
        value of the marker <Mk> on trace no. <Ch/Tr>.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:MARKer<Mk>:FUNCtion:CENTer
        
        

   :param marker: Marker number.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: ShowLimitLine(self, channel_Trace, displayLimitLine)
           
        This function displays or hides the entire limit line (including all
        segments) associated to the active trace.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:DISPlay[:STATe] <Boolean>
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param displayLimitLine: Displays or hides the entire limit line.

.. method:: SetLimitCheck(self, channel_Trace, limitLine, limitCheck)
           
        This function switches the limit check (or individual upper and lower
        limits) on or off.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:STATe <Boolean>
        CALCulate<Ch/Tr>:LIMit:LOWer:STATe <Boolean>
        CALCulate<Ch/Tr>:LIMit:UPPer:STATe <Boolean>
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param limitLine: Select limit line.
   :param limitCheck: Switches the limit check on or off.

.. method:: GetLimitCheck(self, channel_Trace, limitLine)
           
        This function returns if the limit check (or individual upper and
        lower limits) is switched on or off.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:STATe?
        CALCulate<Ch/Tr>:LIMit:LOWer:STATe?
        CALCulate<Ch/Tr>:LIMit:UPPer:STATe?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param limitLine: Select limit line.
   :return: limitCheck

.. method:: SetLimitLineFailBeep(self, channel_Trace, failBeep)
           
        This function switches the acoustic signal (fail beep) on or off. The
        fail beep is generated each time the analyzer detects an exceeded
        limit.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:SOUNd[:STATe] <Boolean>
        
        

   :param failBeep: Fail beep on or off.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetLimitLineFailBeep(self, channel_Trace)
           
        This function returns if the acoustic signal (fail beep) is switched
        on or off. The fail beep is generated each time the analyzer detects
        an exceeded limit.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:SOUNd[:STATe]?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: failBeep

.. method:: GetLimitCheckResult(self, channel_Trace)
           
        This function returns a 0 or 1, to indicate whether the LIMit test has
        failed or not. Sweep must be initiated before reading the result when
        in single sweep mode.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:FAIL?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: limitCheckResult

.. method:: AddLimitLineSegment(self, channel_Trace, segment, type, startStimulus, stopStimulus, startResponse, stopResponse)
           
        This function adds a new segment to the limit line list. In each
        segment the limit line is defined as a straight line connecting two
        points.
        
        Note(s):
        
        This function does not overwrite existing limit line segments. The
        defined segment is appended to the segment list as new segment.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:DATA <type>, <start_stim>, <stop_stim>,
        <start_resp>, <stop_resp>
        
        

   :param startResponse: Start Response is the response (y-axis) valueof the first point of the segment.
   :param stopResponse: Stop Response is the response (y-axis) value ofthe last point of the segment.
   :param segment: Segment number.
   :param startStimulus: Start Stimulus is the stimulus (x-axis) valueof the first point of the segment (not necessarily smaller than StopStimulus).
   :param channel_Trace: Channel number used toidentify the active trace.
   :param stopStimulus: Stop Stimulus is the stimulus (x-axis) value ofthe last point of the segment (not necessarily larger than StartStimulus).
   :param type: Type indicates whether the segment belongs to an Upper ora Lower limit line, or if the limit check at the segment is switchedOff. Switching off the limit check does not delete the segment.

.. method:: EditLimitLineSegment(self, channel_Trace, segment, type, startStimulus, stopStimulus, startResponse, stopResponse)
           
        This function edits existing segment of the limit line segments list.
        
        Note(s):
        
        A segment must be created first to enable this function.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:SEGMent<Seg>:TYPE LMIN | LMAX | OFF
        CALCulate<Ch/Tr>:LIMit:SEGMent<Seg>:STIMulus:STARt <numeric_value>
        CALCulate<Ch/Tr>:LIMit:SEGMent<Seg>:STIMulus:STOP <numeric_value>
        CALCulate<Ch/Tr>:LIMit:SEGMent<Seg>:AMPLitude:STARt <numeric_value>
        CALCulate<Ch/Tr>:LIMit:SEGMent<Seg>:AMPLitude:STOP <numeric_value>
        
        

   :param startResponse: Changes the start response value (i.e. theresponse value assigned to the start stimulus value) of a limit linesegment.
   :param stopResponse: Changes the stop response value (i.e. theresponse value assigned to the stop stimulus value) of a limit linesegment.
   :param segment: Segment number.
   :param startStimulus: Changes the start stimulus value (i.e. thelargest or smallest stimulus value) of a limit line segment.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param stopStimulus: Changes the stop stimulus value (i.e. thelargest or smallest stimulus value) of a limit line segment.
   :param type: Selects the limit line type for a limit line segment.

.. method:: ReadLimitLineSegmentList(self, channel_Trace, listSize, type, startStimulus, stopStimulus, startResponse, stopResponse)
           
        This function returns entire limit line segment list. The limit line
        segment is calculated as a straight line connecting the two points
        (<Start Stimulus>, <Start Response>) and (<Stop Stimulus>, <Stop
        Response>).
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:DATA?
        
        

   :param startResponse: Start Response is the response (y-axis) valueof the first point of the segment.
   :param stopResponse: Stop Response is the response (y-axis) valueof the last point of the segment.
   :param listSize: Pass the maximum number of segments (segments listsize) to be taken out of the segments list.
   :param startStimulus: Start Stimulus is the stimulus (x-axis) valueof the first point of the segment (not necessarily smaller than StopStimulus).
   :param channel_Trace: Channel number used toidentify the active trace.
   :param stopStimulus: Stop Stimulus is the stimulus (x-axis) valueof the last point of the segment (not necessarily larger than StartStimulus).
   :param type: Type indicates whether the segment belongs to an Upperor a Lower limit line, or if the limit check at the segment isswitched Off.
   :return: segmentsCount

.. method:: WriteLimitLineSegmentList(self, channel_Trace, listSize, type, startStimulus, stopStimulus, startResponse, stopResponse)
           
        This function defines the stimulus values of the limit line and/or
        creates new limit line segments. It also defines the response (y-axis)
        values of the lower (upper) limit line.
        
        Note(s):
        
        (1) This function use a fixed numbering scheme for limit line
        segments: Upper limit line segments are assigned odd numbers (1, 3,
        5,...), lower limit line segments are assigned even numbers (2, 4,
        6,...).
        
        (2) Rules for creating segments:
        The following rules apply to an active trace with n existing upper and
        n existing lower limit line segments:
        
        An odd number of values is rejected; an error message -109,"Missing
        parameter..." is generated.
        
        An even number of 2*k values updates or generates k lower limit line
        segments.
        
        For n > k the response values of all existing lower limit line
        segments no. 2, 4, ...,2*k are updated, the existing upper and lower
        limit line segments no. 2*k+1, ..., 2*n are deleted. The existing
        upper limit line segments no. 1, 3, 2*k-1 are not affected.
        
        For n < k the response values of the lower limit line segments no. 2,
        4 to 2*n are updated, the lower limit line segments 2*n+2, 2*n+4,...,
        2*k are generated with default stimulus values (see
        CALCulate<Ch/Tr>:LIMit:CONTrol[:DATA] . In addition, the missing upper
        limit line segments 2*n+1, 2*n+3,..., 2*k-1 are generated with default
        stimulus and response values
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:CONTrol[:DATA]
        <numeric_value>,<numeric_value>{,<numeric_value>,<numeric_value>}
        CALCulate<Ch/Tr>:LIMit:LOWer[:DATA]
        <numeric_value>,<numeric_value>{,<numeric_value>,<numeric_value>}
        CALCulate<Ch/Tr>:LIMit:UPPer[:DATA]
        <numeric_value>,<numeric_value>{,<numeric_value>,<numeric_value>}
        
        

   :param startResponse: Start Response is the response (y-axis) valueof the first point of the segment(s).
   :param stopResponse: Stop Response is the response (y-axis) valueof the last point of the segment(s).
   :param listSize: Pass the number of segments (segments list size).
   :param startStimulus: Start Stimulus is the stimulus (x-axis) valueof the first point of the segment(s) (not necessarily smaller thanStop Stimulus).
   :param channel_Trace: Channel number used toidentify the active trace.
   :param stopStimulus: Stop Stimulus is the stimulus (x-axis) valueof the last point of the segment(s) (not necessarily larger than StartStimulus).
   :param type: Selects the limit line type.

.. method:: ShiftLimitLineSegmentList(self, channel_Trace, limitLineType, stimulusOffset, responseOffset)
           
        This function shifts the limit line in horizontal direction (stimulus
        values) and also shifts all lower and upper limit line segments
        assigned to the active trace in vertical direction (response values).
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:CONTrol:SHIFt <numeric_value>
        CALCulate<Ch/Tr>:LIMit:LOWer:SHIFt <numeric_value>
        CALCulate<Ch/Tr>:LIMit:UPPer:SHIFt <numeric_value>
        
        

   :param channel_Trace: Channel number used toidentify the active trace. This trace provides the stimulus data forthe limit line unless another trace <trace_name> is specified.
   :param responseOffset: Response offset value, used to shift limitline segments in vertical direction.
   :param limitLineType: Select limit line type.
   :param stimulusOffset: Stimulus offset value, used to shift limitline segments in horizontal direction.

.. method:: DeleteLimitLineSegments(self, channel_Trace)
           
        This function deletes all limit line segments.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:DELete:ALL
        
        

   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: RecallLimitLine(self, traceName, fileName)
           
        This function loads a limit line definition from a specified file and
        assigns it to a trace with a specified name. Limit lines are created
        using the CALCulte<Ch/Tr>:LIMit... commands.
        
        Remote-control command(s):
        MMEMory:LOAD:LIMit '<trc_name>','<file_name>'
        
        

   :param fileName: String parameter to specify the name and directoryof the limit line file to be loaded. The default extension (manualcontrol) for limit line files is *.limit, although other extensionsare allowed. If no path is specified the analyzer searches the currentdirectory, to be queried with MMEMory:CDIRectory?.
   :param traceName: Name of an existing trace inthe active setup (string parameter). The imported limit line isassigned to this trace, irrespective of the trace information in thelimit line file.

.. method:: RecallLimitLineWithOptions(self, traceName, fileName, sParameter, xOffset, yOffset, type)
           
        This function loads a limit line definition from a specified file and
        assigns it to a trace with a specified name. Limit lines are created
        using the CALCulte<Ch/Tr>:LIMit... commands.
        
        Remote-control command(s):
        MMEMory:LOAD:LIMit '<trc_name>','<file_name>'[,'<param_name>',
        <x_offset>, <y_offset>, <type>]
        
        

   :param yOffset: This control sets theresponse offset for limit lines loaded from a Touchstone file. A 1 dBoffset shifts the limit line by 1 dB in (positive) vertical direction.
   :param sParameter: This control selects an S-parameter from aTouchstone file.The parameter must be compatible with the file type (e.g. for oneportTouchstone files *.s1p, only the parameter name 'S11' isallowed).
   :param fileName: String parameter to specify the name and directoryof the limit line file to be loaded. The default extension (manualcontrol) for limit line files is *.limit, although other extensionsare allowed. If no path is specified the analyzer searches the currentdirectory, to be queried with MMEMory:CDIRectory?.
   :param type: Selects the limit line type for a limit line segment.
   :param xOffset: This control sets the stimulusoffset for limit lines loaded from a Touchstone file. A 1 GHz offsetshifts the limit line by 1 GHz in (positive) horizontal direction.
   :param traceName: Name of an existing trace inthe active setup (string parameter). The imported limit line isassigned to this trace, irrespective of the trace information in thelimit line file.

.. method:: SaveLimitLine(self, traceName, fileName)
           
        This function saves the limit lines associated to a specified trace to
        a limit line file. Limit lines are created using the
        CALCulte<Ch/Tr>:LIMit... commands.
        
        Remote-control command(s):
        MMEMory:STORe:LIMit '<trc_name>','<file_name>'
        
        

   :param fileName: String parameter to specify the name and directoryof the created limit line file. The default extension (manual control)for limit line files is *.limit, although other extensions areallowed. If no path is specified the analyzer uses the currentdirectory, to be queried with MMEMory:CDIRectory?.
   :param traceName: Name of an existing trace inthe active setup (string parameter) for which a limit line definitionexists.

.. method:: ImportTraceasLimitLine(self, channel_Trace, limitLineType, stimulusOffset, responseOffset, traceName)
           
        This function generates an lower (upper) limit line using the stimulus
        values of a data or memory trace and specified offset values.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:LOWer:FEED
        <stimulus_offset>,<response_offset>[,<trace_name>]
        CALCulate<Ch/Tr>:LIMit:UPPer:FEED
        <stimulus_offset>,<response_offset>[,<trace_name>]
        
        

   :param channel_Trace: Channel number used toidentify the active trace. This trace provides the stimulus data forthe limit line unless another trace <trace_name> is specified.
   :param traceName: Name of the selected trace as used e.g. inCALCulate<Ch>:PARameter:SDEFine. If no trace name is specified theanalyzer uses the active trace no. <Ch/Tr>.
   :param responseOffset: Response offset value, used to shift allimported limit line segments in vertical direction.
   :param limitLineType: Select limit line type.
   :param stimulusOffset: Stimulus offset value, used to shift allimported limit line segments in horizontal direction.

.. method:: SetLimitLineTTLOutPass(self, channel_Trace, outputNo, TTLOutput)
           
        This function switches the TTL pass/fail signals on or off. The
        signals are applied to the USER CONTROL connector as long as the
        active trace <Ch/Tr> is within limits.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:TTLout<Output_no>[:STATe] <Boolean>
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param TTLOutput: Sets TTL output signal on or off.
   :param outputNo: Select TTL output.

.. method:: GetLimitLineTTLOutPass(self, channel_Trace, outputNo)
           
        This function returns if the TTL pass/fail signals is switched on or
        off. The signals are applied to the USER CONTROL connector as long as
        the active trace <Ch/Tr> is within limits.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:TTLout<Output_no>[:STATe]?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param outputNo: Select TTL output.
   :return: TTLOutput

.. method:: SetDisplayLine(self, channel_Trace, displayLine, position)
           
        This function shows or hides the display line associated to the active
        trace in a Cartesian diagram area.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:DLINe:STATe <Boolean>
        CALCulate<Ch/Tr>:DLINe <numeric_value>
        
        

   :param position: Defines the position (response value) of the displayline.
   :param channel_Trace: Channel number used toidentify the active trace.
   :param displayLine: Switches the display line on or off.

.. method:: GetDisplayLine(self, channel_Trace)
           
        This function returns if the display line associated to the active
        trace in a Cartesian diagram area is active or not and returns its
        position.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:DLINe:STATe?
        CALCulate<Ch/Tr>:DLINe?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: displayLine
   :return: position

.. method:: SetLimitDomainUnits(self, channel_Trace, domainUnits)
           
        This function deletes the existing limit line and (re-)defines the
        physical units of the stimulus values of the limit line.
        
        Remote-control command(s):
        CALCulate<Chn>:LIMit:CONTrol:DOMain FLIN | FLOG | FSEG | FSINgle |
        TLIN | TLOG | PLIN | PLOG | PSINgle
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param domainUnits: Selects the keywords for the units of the stimulusvalues.

.. method:: SetLimitResponseDomainComplexUnits(self, channel_Trace, responseUnits)
           
        This function deletes the existing limit line and (re-)defines the
        physical units of the response values of the limit line.
        
        Notes:
        
        (1) This command is complemented by
        CALCulate<Chn>:LIMit:RDOMain:FORMat and
        CALCulate<Chn>:LIMit:RDOMain:SPACing.
        
        Remote-control command(s):
        CALCulate<Chn>:LIMit:RDOMain:COMPlex S | SINV | Y | Z | YREL | ZREL
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param responseUnits: Selects the keywords for the units of theresponse values.

.. method:: SetLimitResponseDomainFormatUnits(self, channel_Trace, responseUnits)
           
        This function deletes the existing limit line and (re-)defines the
        physical units of the response values of the limit line.
        
        Notes:
        
        (1) This command is complemented by
        CALCulate<Chn>:LIMit:RDOMain:COMPlex and
        CALCulate<Chn>:LIMit:RDOMain:SPACing.
        
        Remote-control command(s):
        CALCulate<Chn>:LIMit:RDOMain:FORMat COMPlex | MAGNitude | PHASe | REAL
        | IMAGinary | SWR | GDELay | L | C
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param responseUnits: Selects the keywords for the units of theresponse values.

.. method:: SetLimitResponseDomainSpacingUnits(self, channel_Trace, responseUnits)
           
        This function deletes the existing limit line and (re-)defines the
        physical units of the response values of the limit line.
        
        Notes:
        
        (1) This command is complemented by
        CALCulate<Chn>:LIMit:RDOMain:COMPlex and
        CALCulate<Chn>:LIMit:RDOMain:FORMat.
        
        (2) The analyzer uses dB units, irrespective of the parameter
        selected.
        
        Remote-control command(s):
        CALCulate<Chn>:LIMit:RDOMain:SPACing LINear | LOGarithmic | dB | SIC
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param responseUnits: Selects the keywords for the units of theresponse values.

.. method:: SetRippleCheckOn(self, channel_Trace, limitCheck)
           
        This function switches the global ripple limit check on or off. This
        check covers all traces in the active setup.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:STATe <Boolean>
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param limitCheck: Switches the limit check on or off.

.. method:: GetRippleCheckOn(self, channel_Trace)
           
        This function returns the global ripple limit check.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:STATe?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: limitCheck

.. method:: GetRippleLimitGlobalCheckResult(self, channel_Trace)
           
        This function returns a 0 or 1, to indicate whether or not the global
        ripple limit check has failed.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:FAIL?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: rippleLimitCheckResult

.. method:: SetCheckRippleLimitRangeSegment(self, channel_Trace, segment, limitCheck)
           
        This function enables or disables the limit check in the ripple limit
        range no. <Seg>.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:SEGMent<Seg>[:STATe] <Boolean>
        
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param segment: Segment number.
   :param limitCheck: Switches the limit check on or off.

.. method:: GetCheckRippleLimitRangeSegment(self, channel_Trace, segment)
           
        This function returns the limit check in the ripple limit range no.
        <Seg>.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:SEGMent<Seg>[:STATe]?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param segment: Segment number.
   :return: limitCheck

.. method:: GetRippleLimitCheckSegmentResult(self, channel_Trace, segment)
           
        This function returns the result of the ripple limit check in the
        previously defined limit range no. <Seg>.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:SEGMent<Seg>:RESult?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param segment: Segment number.
   :return: fail
   :return: limitCheckResult

.. method:: SetRippleLimitsDisplayState(self, channel_Trace, displayLine)
           
        This function displays or hides all ripple limit lines (including all
        ranges) associated to the active trace.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:DISPlay[:STATe] <Boolean>
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param displayLine: Switches the display line on or off.

.. method:: GetRippleLimitsDisplayState(self, channel_Trace)
           
        This function returns limits display state.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:DISPlay[:STATe]?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: displayLine

.. method:: SetRippleFailBeepOn(self, channel_Trace, failBeep)
           
        This function switches the acoustic signal (fail beep) on or off. The
        fail beep is generated each time the analyzer detects an exceeded
        limit.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:SOUNd[:STATe] <Boolean>
        
        

   :param failBeep: Switches the fail beep on or off.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: GetRippleFailBeepOn(self, channel_Trace)
           
        This function returns the acoustic signal state.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:SOUNd[:STATe]?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :return: failBeep

.. method:: AddRippleLimitLineRangesSegment(self, channel_Trace, noOfValues, type, startStimulus, stopStimulus, limit)
           
        This function adds and enables/disables an arbitrary number of ripple
        limit ranges, assigning the stimulus values and the ripple limits.
        
        Note(s):
        
        This function does not overwrite existing ripple limit ranges. The
        defined ranges are appended to the range list as new ranges.
        
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:DATA <type>, <start_stim>, <stop_stim>,
        <limit>{,<type>, <start_stim>, <stop_stim>, <limit>}
        
        

   :param noOfValues: Set number of values for controls Type, StartStimulus, Stop Stimulus, Limit.
   :param startStimulus: Start Stimulus is the stimulus (x-axis) value of the firstpoint of the segment (not necessarily smaller than Stop Stimulus).
   :param channel_Trace: Channel number used toidentify the active trace.
   :param limit: Limit value, to be defined in accordance with the selectedformat (CALCulate<Chn>:RIPPle:RDOMain:FORMat).
   :param stopStimulus: Stop Stimulus is the stimulus (x-axis) value of the lastpoint of the segment (not necessarily larger than Start Stimulus).
   :param type: Type indicates whether the segment belongs to an Upperor a Lower limit line, or if the limit check at the segment isswitched Off. Switching off the limit check does not delete thesegment.

.. method:: EditRippleLimitLineSegment(self, channel_Trace, segment, startStimulus, stopStimulus)
           
        This function edits existing segment of the ripple limit line segments
        list.
        
        Note(s):
        
        (1) To define several ripple limit ranges with a single command
        use CALCulate<Chn>:RIPPle
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:SEGMent<Seg>:STIMulus:STARt <numeric_value>
        CALCulate<Chn>:RIPPle:SEGMent<Seg>:STIMulus:STOP <numeric_value>
        
        
        

   :param startStimulus: Changes the start stimulus value (i.e. thesmallest stimulus value) of a ripple limit range. A range must becreated first to enable this command (e.g CALCulate<Chn>:RIPPle:DATA).
   :param channel_Trace: Channel number used toidentify the active trace.
   :param segment: Segment number.
   :param stopStimulus: Changes the stop stimulus value (i.e. thelargest stimulus value) of a ripple limit range. A range must becreated first to enable this command (e.g CALCulate<Chn>:RIPPle:DATA).

.. method:: DeleteAllRippleLimitRanges(self, channel_Trace)
           
        This function deletes all limit line segments.
        
        Remote-control command(s):
        CALCulate<Ch/Tr>:LIMit:DELete:ALL
        
        

   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: SetRippleLimitPhysicalUnits(self, channel_Trace, physicalUnits)
           
        This function deletes the existing ripple limit ranges and
        (re-)defines the physical units of the stimulus values of the ripple
        limit lines. The unit of the ripple limit is defined via
        CALCulate<Chn>:RIPPle:RDOMain:FORMat
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:CONTrol:DOMain
        FLIN | FLOG | FSEG | FSINgle | TLIN | TLOG | PLIN | PLOG | PSINgle
        
        

   :param physicalUnits: Selects the keywords for the units of thestimulus values.
   :param channel_Trace: Channel number used toidentify the active trace.

.. method:: SetRippleLimitResponseDomainFormatUnits(self, channel_Trace, responseUnits)
           
        This function deletes the existing ripple limit ranges and
        (re-)defines the physical unit of the ripple limit.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:RDOMain:FORMat COMPlex | MAGNitude | PHASe |
        REAL | IMAGinary | SWR | GDELay | L | C
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param responseUnits: Selects the keywords for the units of theresponse values.

.. method:: GetNumberRippleLimitRanges(self, channel_Trace, segment)
           
        This function queries the number of ripple limit ranges.
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:SEGMent<Seg>:COUNt?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param segment: Segment number.
   :return: number

.. method:: SetRippleLimitRange(self, channel_Trace, segment, limit)
           
        This function defines the ripple limit for ripple limit range no.
        <Seg>.
        
        Notes:
        
        (1) A range must be created first to enable this command (e.g
        CALCulate<Chn>:RIPPle:DATA).
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:SEGMent<Seg>:LIMit
        
        

   :param limit: Limit value, to be defined in accordance with theselected format (CALCulate<Chn>:RIPPle:RDOMain:FORMat).
   :param channel_Trace: Channel number used toidentify the active trace.
   :param segment: Segment number.

.. method:: GetRippleLimitRange(self, channel_Trace, segment)
           
        This function returns the ripple limit for ripple limit range no.
        <Seg>.
        
        Notes:
        
        (1) A range must be created first to enable this command (e.g
        CALCulate<Chn>:RIPPle:DATA).
        
        Remote-control command(s):
        CALCulate<Chn>:RIPPle:SEGMent<Seg>:LIMit?
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param segment: Segment number.
   :return: limit

.. method:: SaveRecallRippleLimit(self, operationToBePerformed, traceName, fileName)
           
        This function saves or recalls the ripple limits associated with a
        specified trace.
        
        Remote-control command(s):
        MMEMory:LOAD:RIPPle 'Trc_name','file_name'
        MMEMory:STORe:RIPPle 'Trc_name','file_name'
        
        

   :param fileName: String parameter to specify the name and directoryof the created ripple limit file.
   :param operationToBePerformed: This controlselects the type of operation to be performed.
   :param traceName: Name of an existing trace in the active setup(string parameter) for which a ripple limit definition exists.

.. method:: SetStartFrequency(self, channel=1, startFrequency)
           
        This function defines the start frequency for a frequency sweep which
        is equal to the left edge of a Cartesian diagram.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:STARt
        
        

   :param startFrequency: This control defines the start frequency for afrequency sweep which is equal to the left edge of a Cartesiandiagram.
   :param channel: Channel number.

.. method:: GetStartFrequency(self, channel=1)
           
        This function queries the start frequency for a frequency sweep which
        is equal to the left edge of a Cartesian diagram.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:STARt?
        
        

   :param channel: Channel number.
   :return: startFrequency

.. method:: SetStopFrequency(self, channel=1, stopFrequency)
           
        This function defines the stop frequency for a frequency sweep which
        is equal to the right edge of a Cartesian diagram.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:STOP
        
        

   :param channel: Channel number.
   :param stopFrequency: This control defines the stop frequency for afrequency sweep which is equal to the right edge of a Cartesiandiagram.

.. method:: GetStopFrequency(self, channel=1)
           
        This function queries the stop frequency for a frequency sweep which
        is equal to the right edge of a Cartesian diagram.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:STOP?
        
        

   :param channel: Channel number.
   :return: stopFrequency

.. method:: SetCenterFrequency(self, channel=1, centerFrequency)
           
        This function defines the center of the measurement and display range
        for a frequency sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CENTer
        
        

   :param centerFrequency: This control defines the center of themeasurement and display range for a frequency sweep.
   :param channel: Channel number.

.. method:: GetCenterFrequency(self, channel=1)
           
        This function queries the center of the measurement and display range
        for a frequency sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CENTer?
        
        

   :param channel: Channel number.
   :return: centerFrequency

.. method:: SetFrequencySpan(self, channel=1, span)
           
        This function defines the width of the measurement and display range
        for a frequency sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:SPAN
        
        

   :param span: This control defines the width of the measurement anddisplay range for a frequency sweep.
   :param channel: Channel number.

.. method:: GetFrequencySpan(self, channel=1)
           
        This function queries the width of the measurement and display range
        for a frequency sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:SPAN?
        
        

   :param channel: Channel number.
   :return: span

.. method:: SetPower(self, channel=1, power)
           
        This function defines the power of the internal signal source.
        
        Note(s):
        (1) The setting is valid for all sweep types except power sweep.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate][:AMPlitude]
        
        

   :param power: This control defines the power of the internal signalsource.
   :param channel: Channel number.

.. method:: GetPower(self, channel=1)
           
        This function queries the power of the internal signal source.
        
        Note(s):
        (1) The setting is valid for all sweep types except power sweep.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate][:AMPlitude]?
        
        

   :param channel: Channel number.
   :return: power

.. method:: SetCWFrequency(self, channel=1, CWFrequency)
           
        This function defines the fixed (Continuous Wave, CW) frequency for
        all sweep types operating at fixed frequency (power sweep, time sweep,
        CW mode sweep).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CW
        
        

   :param channel: Channel number.
   :param CWFrequency: This control defines the fixed (Continuous Wave,CW) frequency for all sweep types operating at fixed frequency (powersweep, time sweep, CW mode sweep).

.. method:: GetCWFrequency(self, channel=1)
           
        This function queries the fixed (Continuous Wave, CW) frequency for
        all sweep types operating at fixed frequency (power sweep, time sweep,
        CW mode sweep).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CW?
        
        

   :param channel: Channel number.
   :return: CWFrequency

.. method:: SetStartPower(self, channel=1, startPower)
           
        This function defines the start power for a power sweep which is equal
        to the left edge of a Cartesian diagram.
        
        Note(s):
        (1) A power sweep must be active ([SENSe<Ch>:]SWEep:TYPE POWer) before
        this command can be used.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:STARt
        
        

   :param startPower: This control defines the start power for a powersweep which is equal to the left edge of a Cartesian diagram.
   :param channel: Channel number.

.. method:: GetStartPower(self, channel=1)
           
        This function queries the start power for a power sweep which is equal
        to the left edge of a Cartesian diagram.
        
        Note(s):
        (1) A power sweep must be active ([SENSe<Ch>:]SWEep:TYPE POWer) before
        this command can be used.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:STARt?
        
        

   :param channel: Channel number.
   :return: startPower

.. method:: SetStopPower(self, channel=1, stopPower)
           
        This function defines the stop power for a power sweep which is equal
        to the right edge of a Cartesian diagram.
        
        Note(s):
        (1) A power sweep must be active ([SENSe<Ch>:]SWEep:TYPE POWer) before
        this command can be used.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:STOP
        
        

   :param stopPower: This control defines the stop power for a powersweep which is equal to the right edge of a Cartesian diagram.
   :param channel: Channel number.

.. method:: GetStopPower(self, channel=1)
           
        This function queries the stop power for a power sweep which is equal
        to the right edge of a Cartesian diagram.
        
        Note(s):
        (1) A power sweep must be active ([SENSe<Ch>:]SWEep:TYPE POWer) before
        this command can be used.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:STOP?
        
        

   :param channel: Channel number.
   :return: stopPower

.. method:: SetSourcePort(self, channel=1, sourcePort)
           
        This function selects a source port for the stimulus signal (Drive
        Port). The setting acts on the active trace. The effect of the drive
        port selection depends on the measurement parameter associated to the
        active trace.
        
        Note(s):
        
        (1) If an S-parameter S<out><in> is measured, the second port number
        index <in> (input port of the DUT = drive port of the analyzer) is set
        equal to the selected drive port: Drive port selection affects the
        measured quantity.
        
        (2) If a wave quantity or a ratio is measured, the drive port is
        independent from the measured quantity:
        
        Remote-control command(s):
        [SENSe<Chn>:]SWEep:SRCPort 1 | 2 | 3 | 4
        
        

   :param sourcePort: This control defines the test port number of theanalyzer.
   :param channel: Channel number.

.. method:: GetSourcePort(self, channel=1)
           
        This function selects a source port for the stimulus signal (Drive
        Port). The setting acts on the active trace. The effect of the drive
        port selection depends on the measurement parameter associated to the
        active trace.
        
        Note(s):
        
        (1) If an S-parameter S<out><in> is measured, the second port number
        index <in> (input port of the DUT = drive port of the analyzer) is set
        equal to the selected drive port: Drive port selection affects the
        measured quantity.
        
        (2) If a wave quantity or a ratio is measured, the drive port is
        independent from the measured quantity:
        
        Remote-control command(s):
        [SENSe<Chn>:]SWEep:SRCPort 1 | 2 | 3 | 4
        
        

   :param channel: Channel number.
   :return: sourcePort

.. method:: ConfigurePowerBandwidthAverage(self, channel=1, RFState, measBandwidth, averageState, averageFactor)
           
        This function configures the power bandwidth average.
        
        Remote-control command(s):
        DIAGnostic:SERVice:RFPower
        [SENSe<Ch>:]BANDwidth[:RESolution]
        [SENSe<Ch>:]AVERage[:STATe]
        [SENSe<Ch>:]AVERage:COUNt
        
        

   :param RFState: This control turns the internal source power at allports on or off.
   :param averageState: This control enables or disables the sweepaverage.
   :param measBandwidth: This control defines the resolution bandwidthof the analyzer (Meas. Bandwidth).
   :param averageFactor: This control defines the number of consecutivesweeps to be combined for the sweep average.
   :param channel: Channel number.

.. method:: SetReceiverStepAttenuators(self, channel=1, analyzerPort, attenuationFactor)
           
        This function sets an attenuation factor for the wave received at test
        port no. The generated wave is attenuated automatically if step
        attenuators are available.
        
        Remote-control command(s):
        [SENSe<Ch>:]POWer:ATTenuation ARECeiver | BRECeiver | CRECeiver |
        DRECeiver, <numeric_value>
        
        

   :param attenuationFactor: This control defines the attenuation factorfor the received wave.
   :param analyzerPort: This control selects the test port of theanalyzer.
   :param channel: Channel number.

.. method:: GetReceiverStepAttenuators(self, channel=1, analyzerPort)
           
        This function returns an attenuation factor for the wave received at
        test port no. <Pt>. The generated wave is attenuated automatically if
        step attenuators are available.
        
        Remote-control command(s):
        [SENSe<Ch>:]POWer:ATTenuation? ARECeiver | BRECeiver | CRECeiver |
        DRECeiver
        
        

   :param analyzerPort: This control selects the test port of theanalyzer.
   :param channel: Channel number.
   :return: attenuationFactor

.. method:: SetGeneratorStepAttenuators(self, channel=1, port, attenuationFactor)
           
        This function sets a fixed attenuation factor for the generated wave
        at test port no. <Pt>.
        
        Note(s):
        
        (1) This function can be used only with R&S ZVA and ZVB instruments.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ATTenuation <numeric_value>
        
        

   :param attenuationFactor: This control defines the attenuation factorfor the generated wave.
   :param port: This control defines the test port number.
   :param channel: Channel number.

.. method:: GetGeneratorStepAttenuators(self, channel=1, port)
           
        This function gets a fixed attenuation factor for the generated wave
        at test port no. <Pt>.
        
        Note(s):
        
        (1) This function can be used only with R&S ZVA and ZVB instruments.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ATTenuation?
        
        

   :param port: This control defines the test port number.
   :param channel: Channel number.
   :return: attenuationFactor

.. method:: SetAutomaticGeneratorAttenuator(self, channel=1, port, automaticAttenuation)
           
        This function sets whether the attenuation factor for the generated
        wave at test port no. <Pt> is set manually or automatically.
        
        Note(s):
        
        (1) This function can be used only with R&S ZVA and ZVB instruments.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ATTenuation:AUTO ON | OFF
        
        

   :param port: This control defines the test port number.
   :param channel: Channel number.
   :param automaticAttenuation: This control selects whether theattenuation factor for the generated wave at test port no. <Pt> is setmanually or automatically.

.. method:: GetAutomaticGeneratorAttenuator(self, channel=1, port)
           
        This function gets whether the attenuation factor for the generated
        wave at test port no. <Pt> is set manually or automatically.
        
        Note(s):
        
        (1) This function can be used only with R&S ZVA and ZVB instruments.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ATTenuation:AUTO?
        
        

   :param port: This control defines the test port number.
   :param channel: Channel number.
   :return: automaticAttenuation

.. method:: GetAutomaticGeneratorAttenuation(self, channel=1, port)
           
        This function queries the attenuation for the generated wave at test
        port <Pt> in channel <Ch>. If no generator step attenuator is present
        at port <Pt>, the analyzer generates an "option not available" error.
        This function is particularly useful if the generator attenuator
        setting is currently selected by the
        analyzer firmware (rszvb_SetGeneratorAttenuatorMode Automatic or Low
        Noise). In manual mode (rszvb_SetGeneratorAttenuatorMode Manual) it
        returns the attenuation factor specified using
        rszvb_SetReceiverStepAttenuators, just as
        rszvb_GetReceiverStepAttenuators would do.
        
        Note(s):
        
        (1) This function can be used only with R&S ZVA and ZVB instruments.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ATTenuation:AUTO:VALue?
        
        

   :param port: This control defines the test port number.
   :param channel: Channel number.
   :return: attenuation

.. method:: SetGeneratorAttenuatorMode(self, channel=1, port, attenuationMode)
           
        This function defines how the attenuation factor for the generated
        wave at test port no. <Pt> is set.
        
        Note(s):
        
        (1) This function can be used only with R&S ZVA and ZVB instruments.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ATTenuation:MODE AUTO | MANual | LNOise
        
        

   :param port: This control defines the test port number.
   :param channel: Channel number.
   :param attenuationMode: This control defines how the attenuationfactor for the generated wave at test port no. <Pt> is set.

.. method:: GetGeneratorAttenuatorMode(self, channel=1, port)
           
        This function returns the mode of the attenuation factor for the
        generated wave at test port no. <Pt>.
        
        Note(s):
        
        (1) This function can be used only with R&S ZVA and ZVB instruments.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ATTenuation:MODE?
        
        

   :param port: This control defines the test port number.
   :param channel: Channel number.
   :return: attenuationMode

.. method:: SetRFState(self, RFState)
           
        This function turns the internal source power at all ports on or off.
        
        Remote-control command(s):
        DIAGnostic:SERVice:RFPower
        
        

   :param RFState: This control turns the internalsource power at all ports on or off.

.. method:: GetRFState(self, )
           
        This function queries the state of the internal source power at all
        ports.
        
        Remote-control command(s):
        DIAGnostic:SERVice:RFPower?
        
        

   :return: RFState

.. method:: SetMeasBandwidth(self, channel=1, measBandwidth)
           
        This function defines the resolution bandwidth of the analyzer.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth[:RESolution]
        
        

   :param measBandwidth: This control defines the resolution bandwidthof the analyzer (Meas. Bandwidth).
   :param channel: Channel number.

.. method:: GetMeasBandwidth(self, channel=1)
           
        This function queries the resolution bandwidth of the analyzer.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth[:RESolution]?
        
        

   :param channel: Channel number.
   :return: measBandwidth

.. method:: SetMeasBandwidthSelectivity(self, channel=1, measBandwidthSelectivity)
           
        This function defines the selectivity of the IF filter for an
        unsegmented sweep. The value is also used for all segments of a
        segmented sweep, provided that separate selectivity setting is
        disabled ([SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]:CONTrol OFF).
        
        Note(s):
        
        (1) This function can be used only with R&S ZVA and R&S ZVT
        instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:SELect NORMal | HIGH
        
        

   :param measBandwidthSelectivity: This control defines the selectivityof the IF filter for an unsegmented sweep.
   :param channel: Channel number.

.. method:: GetMeasBandwidthSelectivity(self, channel=1)
           
        This function returns the selectivity of the IF filter for an
        unsegmented sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:SELect?
        
        

   :param channel: Channel number.
   :return: measBandwidthSelectivity

.. method:: SetMeasBandwidthReduction(self, channel=1, reduction)
           
        This function enables or disables dynamic bandwidth reduction at low
        frequencies.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:DREDuction
        
        

   :param reduction: This control enable or disable dynamic bandwidthreductionValid Values:VI_FALSE (0) - OffVI_TRUE (1) - On
   :param channel: Channel number.

.. method:: GetMeasBandwidthReduction(self, channel=1)
           
        This function returns state of dynamic bandwidth reduction at low
        frequencies.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:DREDuction?
        
        

   :param channel: Channel number.
   :return: reduction

.. method:: SetAverageState(self, channel=1, averageState)
           
        This function enables or disables the sweep average.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage[:STATe]
        
        

   :param averageState: This control enables or disables the sweepaverage.
   :param channel: Channel number.

.. method:: GetAverageState(self, channel=1)
           
        This function queries the state of the sweep average.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage[:STATe]?
        
        

   :param channel: Channel number.
   :return: averageState

.. method:: SetAverageFactor(self, channel=1, averageFactor)
           
        This function defines the number of consecutive sweeps to be combined
        for the sweep average.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage:COUNt
        
        

   :param averageFactor: This control defines the number of consecutivesweeps to be combined for the sweep average.
   :param channel: Channel number.

.. method:: GetAverageFactor(self, channel=1)
           
        This function queries the number of consecutive sweeps to be combined
        for the sweep average.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage:COUNt?
        
        

   :param channel: Channel number.
   :return: averageFactor

.. method:: GetCurrentSweep(self, channel=1)
           
        Queries the number of the sweep which is currently measured. Use this
        command to monitor the progress of sweep averaging.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage:COUNt:CURRent?
        
        

   :param channel: Channel number.
   :return: currentSweep

.. method:: RestartAverage(self, channel=1)
           
        This function starts a new average cycle, clearing all previous
        results and thus eliminating their effect on the new cycle.
        
        Remote-control command(s):
        [SENSe<Ch>:]AVERage:CLEar
        
        

   :param channel: Channel number.

.. method:: SetPartialMeasurementResolutionBandwidthMode(self, channel=1, bandwidthMode)
           
        Selects global or a port-specific resolution bandwidths.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:MODE PALL | PSPecific
        
        

   :param channel: Channel number.
   :param bandwidthMode: Selects global or a port-specific resolutionbandwidths.

.. method:: GetPartialMeasurementResolutionBandwidthMode(self, channel=1)
           
        Queries resolution bandwidth mode.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:MODE?
        
        

   :param channel: Channel number.
   :return: bandwidthMode

.. method:: SetGeneratorPortResolutionBandwidth(self, channel=1, generatorPort, resolutionBandwidth)
           
        Defines the resolution bandwidth of the analyzer for all partial
        measurements where an external generator <Gen> is used as a source.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:GENerator<Gen>
        
        

   :param resolutionBandwidth: This control defines resolutionbandwidth.
   :param channel: Channel number.
   :param generatorPort: Generator port number.

.. method:: GetGeneratorPortResolutionBandwidth(self, channel=1, generatorPort)
           
        Queries the resolution bandwidth of the analyzer for all partial
        measurements where an external generator <Gen> is used as a source.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:GENerator<Gen>?
        
        

   :param channel: Channel number.
   :param generatorPort: Generator port number.
   :return: resolutionBandwidth

.. method:: SetPhysicalPortResolutionBandwidth(self, channel=1, analyzerPort, resolutionBandwidth)
           
        Defines the resolution bandwidth of the analyzer for all partial
        measurements where an analyzer source port <Pt> is used.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:PORT<Pt>
        
        

   :param resolutionBandwidth: This control defines resolutionbandwidth.
   :param analyzerPort: Physical analyzer port number.
   :param channel: Channel number.

.. method:: GetPhysicalPortResolutionBandwidth(self, channel=1, analyzerPort)
           
        Queries the resolution bandwidth of the analyzer for all partial
        measurements where an analyzer source port <Pt> is used.
        
        Remote-control command(s):
        [SENSe<Ch>:]BANDwidth|BWIDth[:RESolution]:PORT<Pt>?
        
        

   :param analyzerPort: Physical analyzer port number.
   :param channel: Channel number.
   :return: resolutionBandwidth

.. method:: SetSweepType(self, channel=1, sweepType)
           
        This function selects the sweep type, i.e. the sweep variable
        (frequency/power/time) and the position of the sweep points across the
        sweep range.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TYPE LINear | LOGarithmic | SEGMent | POWer | CW |
        POINt | PULSe | IAMPlitude | IPHase
        
        

   :param sweepType: This control selects the sweep type, i.e. the sweepvariable (frequency/power/time) and the position of the sweep pointsacross the sweep range.
   :param channel: Channel number.

.. method:: GetSweepType(self, channel=1)
           
        This function queries the sweep type, i.e. the sweep variable
        (frequency/power/time) and the position of the sweep points across the
        sweep range.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TYPE?
        
        

   :param channel: Channel number.
   :return: sweepType

.. method:: InsertNewSegment(self, channel=1, segment, startFrequency, stopFrequency, numberOfPoints, power, sweepTimeSelect, time, pointDelay, measBandwidth)
           
        This function inserts a new sweep segment with specific channel
        settings. The new segment must not overlap with any of the existing
        segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:INSert
        [SENSe<Ch>:]SEGMent<Seg>:INSert:SELect SWTime | DWELl
        
        

   :param power: This control defines the power of the internal signalsource in segment.
   :param measBandwidth: This control defines theresolution bandwidth of the analyzer (Meas. Bandwidth).
   :param time: This control sets theduration of the sweep in sweep segment no. <Segment>. At the sametime, the command activates separate sweep time setting in all sweepsegments.
   :param sweepTimeSelect: This control defines whether the sweep time ofa new segment, i.e. numeric parameter no. 9 of the function, isentered as a segment sweep time or as a meas. delay.
   :param startFrequency: This control defines theStart frequency of sweep segment no. <Segment>.
   :param numberOfPoints: This control defines thetotal number of measurement Points in sweep segment no. <Segment>.
   :param pointDelay: This control definesthe delay time for each partial measurement in sweep segment no.<Segment>.
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :param stopFrequency: This control defines theStop frequency of sweep segment no. <Segment>.

.. method:: RedefineSegment(self, channel=1, segment, startFrequency, stopFrequency, numberOfPoints, power, sweepTimeSelect, time, pointDelay, measBandwidth)
           
        This function re-defines a sweep segment with specific channel
        settings (Insert New Segment). The segment replaces an existing
        segment <Segment> in the segment list. The modified segment must not
        overlap with any of the existing segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:DEFine
        [SENSe<Ch>:]SEGMent<Seg>:INSert:SELect SWTime | DWELl
        
        

   :param power: This control defines the power of the internal signalsource in segment.
   :param measBandwidth: This control defines theresolution bandwidth of the analyzer (Meas. Bandwidth).
   :param time: This control sets theduration of the sweep in sweep segment no. <Segment>. At the sametime, the command activates separate sweep time setting in all sweepsegments.
   :param sweepTimeSelect: This control defines whether the sweep time ofa new segment, i.e. numeric parameter no. 9 of the function, isentered as a segment sweep time or as a meas. delay.
   :param startFrequency: This control defines theStart frequency of sweep segment no. <Segment>.
   :param numberOfPoints: This control defines thetotal number of measurement Points in sweep segment no. <Segment>.
   :param pointDelay: This control definesthe delay time for each partial measurement in sweep segment no.<Segment>.
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :param stopFrequency: This control defines theStop frequency of sweep segment no. <Segment>.

.. method:: AddNewSegment(self, channel=1, segment)
           
        This function inserts a new sweep segment using default channel
        settings). The added segment covers the frequency interval between the
        maximum frequency of the existing sweep segments and the stop
        frequency of the entire sweep range.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:ADD
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.

.. method:: DeleteSelectedSegment(self, channel=1, segment)
           
        This function deletes the specified (single) sweep segment.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:DELete
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.

.. method:: DeleteAllSegments(self, channel=1)
           
        This function deletes all sweep segments in the channel.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent:DELete:ALL
        
        

   :param channel: Channel number.

.. method:: GetSweepSegmentsCount(self, channel=1)
           
        This function queries the number of sweep segments in the channel
        including all segments that are switched off.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:COUNt?
        
        

   :param channel: Channel number.
   :return: count

.. method:: SetSweepSegmentState(self, channel=1, segment, state)
           
        This function activates or deactivates the sweep segment <Segment>.
        Sweep points belonging to inactive segments only are not measured.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>[:STATe]
        
        

   :param state: This control activates or deactivatesthe sweep segment <Segment>.
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.

.. method:: GetSweepSegmentState(self, channel=1, segment)
           
        This function queries the state of the sweep segment <Segment>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>[:STATe]?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: state

.. method:: SetSweepSegmentStartFrequency(self, channel=1, segment, startFrequency)
           
        This function defines the Start frequency of sweep segment no.
        <Segment>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:FREQuency:STARt
        
        

   :param startFrequency: This control defines theStart frequency of sweep segment no. <Segment>.
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.

.. method:: GetSweepSegmentStartFrequency(self, channel=1, segment)
           
        This function queries the Start frequency of sweep segment no.
        <Segment>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:FREQuency:STARt?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: startFrequency

.. method:: SetSweepSegmentStopFrequency(self, channel=1, segment, stopFrequency)
           
        This function defines the Stop frequency of sweep segment no.
        <Segment>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:FREQuency:STOP
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :param stopFrequency: This control defines the Stopfrequency of sweep segment no. <Segment>.

.. method:: GetSweepSegmentStopFrequency(self, channel=1, segment)
           
        This function queries the Stop frequency of sweep segment no.
        <Segment>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:FREQuency:STOP?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: stopFrequency

.. method:: SetSweepSegmentNumberOfPoints(self, channel=1, segment, numberOfPoints)
           
        This function defines the total number of measurement Points in sweep
        segment no. <Segment>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:POINts
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :param numberOfPoints: This control defines the totalnumber of measurement Points in sweep segment no. <Segment>.

.. method:: GetSweepSegmentNumberOfPoints(self, channel=1, segment)
           
        This function queries the total number of measurement Points in sweep
        segment no. <Segment>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:POINts?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: numberOfPoints

.. method:: SetSweepSegmentName(self, channel=1, segment, name)
           
        This function defines the Name of the sweep segment no. <Seg>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:NAME '<segment_name>'
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param name: This control defines the segment name.
   :param channel: Channel number.

.. method:: GetSweepSegmentName(self, channel=1, segment, bufferSize, name)
           
        This function returns the Name of the sweep segment no. <Seg>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:NAME?
        
        

   :param bufferSize: This control defines the size ofarray passed to argument 'Name'.
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param name: This control returns the segment name.
   :param channel: Channel number.

.. method:: SetSweepSegmentPower(self, channel=1, segment, power)
           
        This function defines the Power of the internal signal source in sweep
        segment no. <Segment>. At the same time, the command activates
        separate power control in all sweep segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:POWer[:LEVel]
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param power: This control defines the Power of theinternal signal source in sweep segment no. <Segment>.
   :param channel: Channel number.

.. method:: GetSweepSegmentPower(self, channel=1, segment)
           
        This function queries the Power of the internal signal source in sweep
        segment no. <Segment>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:POWer[:LEVel]?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: power

.. method:: SetSweepSegmentIndependentPower(self, channel=1, segment, power)
           
        This function defines whether or not the Power can be set
        independently for each sweep segment.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:POWer[:LEVel]:CONTrol
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param power: This control defines whether or notthe Power can be set independently for each sweep segment.
   :param channel: Channel number.

.. method:: GetSweepSegmentIndependentPower(self, channel=1, segment)
           
        This function queries whether or not the Power can be set
        independently for each sweep segment.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:POWer[:LEVel]:CONTrol?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: power

.. method:: SetSweepSegmentMeasBandwidth(self, channel=1, segment, measBandwidth)
           
        This function defines the resolution bandwidth of the analyzer in
        sweep segment no. <Segment>. At the same time, the command activates
        separate bandwidth setting in all sweep segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]
        
        

   :param measBandwidth: This control defines theresolution bandwidth of the analyzer (Meas. Bandwidth).
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.

.. method:: GetSweepSegmentMeasBandwidth(self, channel=1, segment)
           
        This function queries the resolution bandwidth of the analyzer in
        sweep segment no. <Segment>. At the same time, the command activates
        separate bandwidth setting in all sweep segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: measBandwidth

.. method:: SetSweepSegmentIndependentBandwidth(self, channel=1, segment, measBandwidth)
           
        This function defines whether or not the Meas. Bandwidth can be set
        independently for each sweep segment.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]:CONTrol
        
        

   :param measBandwidth: This control defines whetheror not the Meas. Bandwidth can be set independently for each sweepsegment.
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.

.. method:: GetSweepSegmentIndependentBandwidth(self, channel=1, segment)
           
        This function queries whether or not the Meas. Bandwidth can be set
        independently for each sweep segment.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]:CONTrol?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: measBandwidth

.. method:: SetSweepSegmentSpurAvoid(self, channel=1, segment, spurAvoid)
           
        This function defines the position of the local oscillator frequency
        LO relative to the RF frequency (sideband, Spur Avoid) in sweep
        segment no. <Seg>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SBANd
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param spurAvoid: This control defines the positionof the local oscillator frequency LO relative to the RF frequency(sideband, Spur Avoid) in sweep segment no. <Seg>.
   :param channel: Channel number.

.. method:: GetSweepSegmentSpurAvoid(self, channel=1, segment)
           
        This function returns the position of the local oscillator frequency
        LO relative to the RF frequency (sideband, Spur Avoid) in sweep
        segment no. <Seg>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SBANd
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: spurAvoid

.. method:: SetSweepSegmentIndependentSpurAvoid(self, channel=1, segment, spurAvoid)
           
        This function selects common or independent LO sideband (Spur Avoid)
        settings for the sweep segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SBANd:CONTrol
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param spurAvoid: This control selects common orindependent LO sideband (Spur Avoid) settings for the sweep segments.
   :param channel: Channel number.

.. method:: GetSweepSegmentIndependentSpurAvoid(self, channel=1, segment)
           
        This function returns common or independent LO sideband (Spur Avoid)
        settings for the sweep segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SBANd:CONTrol
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: spurAvoid

.. method:: SetSweepSegmentSelectivity(self, channel=1, segment, selectivity)
           
        This function defines the Selectivity in sweep segment no. <Seg>. At
        the same time, the command activates separate selectivity setting in
        all sweep segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]:SELect NORMal | HIGH
        
        

   :param selectivity: This control selects theselectivity in sweep segment no. <Seg>.
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.

.. method:: GetSweepSegmentSelectivity(self, channel=1, segment)
           
        This function returns the Selectivity in sweep segment no. <Seg>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]:SELect?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: selectivity

.. method:: SetSweepSegmentIndependentSelectivity(self, channel=1, segment, selectivity)
           
        This function defines whether or not the selectivity can be set
        independently for each sweep segment.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]:SELect:CONTrol
        
        

   :param selectivity: This control defines whether ornot the selectivity can be set independently for each sweep segment.
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.

.. method:: GetSweepSegmentIndependentSelectivity(self, channel=1, segment)
           
        This function queries whether or not the selectivity can be set
        independently for each sweep segment.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:BWIDth[:RESolution]:SELect:CONTrol?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: selectivity

.. method:: SetSweepSegmentSweepTime(self, channel=1, segment, time)
           
        This function sets the duration of the sweep in sweep segment no.
        <Segment>. At the same time, the command activates separate sweep time setting in all sweep segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :param time: This control sets the duration of thesweep in sweep segment no. <Segment>. At the same time, the commandactivates separate sweep time setting in all sweep segments.

.. method:: GetSweepSegmentSweepTime(self, channel=1, segment)
           
        This function queries the duration of the sweep in sweep segment no.
        <Segment>. At the same time, the command activates separate sweep time
        setting in all sweep segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: time

.. method:: SetSweepSegmentIndependentTime(self, channel=1, segment, time)
           
        This function defines whether or not the Sweep Time can be set
        independently for each sweep segment.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME:CONTrol
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :param time: This control defines whether or notthe Sweep Time can be set independently for each sweep segment.

.. method:: GetSweepSegmentIndependentTime(self, channel=1, segment)
           
        This function queries whether or not the Sweep Time can be set
        independently for each sweep segment.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME:CONTrol?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: time

.. method:: SetSweepSegmentPointDelay(self, channel=1, segment, pointDelay)
           
        This function defines the delay time for each partial measurement in
        sweep segment no. <Segment>
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:DWELl
        
        

   :param pointDelay: This control defines the delaytime for each partial measurement in sweep segment no. <Segment>.
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.

.. method:: GetSweepSegmentPointDelay(self, channel=1, segment)
           
        This function queries the delay time for each partial measurement in
        sweep segment no. <Segment>
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:DWELl?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: pointDelay

.. method:: SetSweepSegmentIndependentPointDelay(self, channel=1, segment, pointDelay)
           
        This function defines whether or not the Point Delay can be set
        independently for each sweep segment.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:DWELl:CONTrol
        
        

   :param pointDelay: This control defines whether ornot the Point Delay can be set independently for each sweep segment.
   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.

.. method:: GetSweepSegmentIndependentPointDelay(self, channel=1, segment)
           
        This function queries whether or not the Point Delay can be set
        independently for each sweep segment.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:DWELl:CONTrol?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: pointDelay

.. method:: SetSweepSegmentTriggering(self, channel=1, segment, triggering)
           
        This function deactivates/activates triggering for segment <Seg>. This
        setting only takes effect if:
        
        1. The analyzer is not in Free Run mode (see rszvb_SetTriggerSource)
        
        2. Selective segment triggering is enabled
        (rszvb_SetSweepSelectiveSegmentTriggering set to ON)
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:TRIGger:STATe
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param triggering: This controldeactivates/activates triggering.
   :param channel: Channel number.

.. method:: GetSweepSegmentTriggering(self, channel=1, segment)
           
        This function returns the state of the triggering for segment <Seg>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:TRIGger:STATe?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: triggering

.. method:: SetSweepSelectiveSegmentTriggering(self, channel=1, triggering)
           
        This function enables/disables selective segment triggering (configured using rszvb_SetSweepSegmentTriggering).
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:TRIGger:CONTrol
        
        

   :param triggering: This control enables/disables selective segmenttriggeringValid Values:VI_FALSE (0) - OffVI_TRUE (1) - On
   :param channel: Channel number.

.. method:: GetSweepSelectiveSegmentTriggering(self, channel=1)
           
        This function returns the state of the selective segment triggering
        (configured using rszvb_SetSweepSegmentTriggering).
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:TRIGger:CONTrol?
        
        

   :param channel: Channel number.
   :return: triggering

.. method:: SetSweepSegmentBitsState(self, channel=1, state)
           
        This function enables or disables segment bits for the sweep segments
        in channel no. <Ch>.
        
        Remote-control command(s):
        OUTPut<Ch>:UPORt:SEGMent<Seg>:STATe ON | OFF
        
        

   :param state: This control enables or disables segment bits for thesweep segments in channel no. <Ch>.
   :param channel: Channel number.

.. method:: GetSweepSegmentBitsState(self, channel=1)
           
        This function returns the state of the segment bits for the sweep
        segments in channel no. <Ch>.
        
        Remote-control command(s):
        OUTPut<Ch>:UPORt:SEGMent<Seg>:STATe?
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetSweepSegmentBitValues(self, channel=1, segment, bit0, bit1, bit2, bit3)
           
        This function sets four independent output signals at the USER CONTROL
        connector (lines 8, 9, 10, 11). The output signals are 3.3 V TTL
        signals which can be used to differentiate between up to 16
        independent analyzer states for each channel.
        
        OUTPut<Ch>:UPORt:SEGMent<Seg>[:VALue]
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :param bit3: This control sets the bit 3 - output signal at pin 11.
   :param bit2: This control sets the bit 2 - output signal at pin 10.
   :param bit1: This control sets the bit 1 - output signal at pin 9.
   :param bit0: This control sets the bit 0 - outputsignal at pin 8.

.. method:: GetSweepSegmentBitValues(self, channel=1, segment)
           
        This function returns four independent output signals at the USER
        CONTROL connector (lines 8, 9, 10, 11).
        
        OUTPut<Ch>:UPORt:SEGMent<Seg>[:VALue]?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: bit0
   :return: bit1
   :return: bit2
   :return: bit3

.. method:: GetSweepSegmentCenterFrequency(self, channel=1, segment)
           
        This function queries the center frequency of sweep segment no.
        <Segment>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:FREQuency:CENTer?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: centerFrequency

.. method:: GetSweepSegmentFrequencySpan(self, channel=1, segment)
           
        This function queries the width of the frequency range of sweep
        segment no. <Segment>.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:FREQuency:SPAN?
        
        

   :param segment: Sweep segment number. Segment numbers must besequential. The specified segment number must be smaller or equal tothe number of existing segments plus 1. Moreover, segment numbers mustselected such that the corresponding frequency ranges are in ascendingorder.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :param channel: Channel number.
   :return: frequencySpan

.. method:: SaveSegment(self, channel=1, fileName)
           
        This function saves the sweep segment definition of a specified
        channel to a sweep segment file.
        
        Remote-control command(s):
        MMEMory:STORe:SEGMent <Ch>, '<file_name>'
        
        

   :param channel: Channel number.
   :param fileName: This control specifies the name and directory of thecreated sweep segment file. The default extension (manual control) forsweep segment files is *.seglist, although other extensions areallowed. If no path is specified the analyzer uses the currentdirectory, to be queried with MMEMory:CDIRectory?.

.. method:: LoadSegment(self, channel=1, fileName)
           
        This function loads a sweep segment definition from a specified file
        and assigns it to a specified channel.
        
        Remote-control command(s):
        MMEMory:LOAD:SEGMent <Ch>,'<file_name>'
        
        

   :param channel: Channel number.
   :param fileName: This control specifies the name and directory of thesweep segment file to be loaded. The default extension (manualcontrol) for sweep segment files is *.seglist, although otherextensions are allowed. If no path is specified the analyzer searchesthe current directory, to be queried with MMEMory:CDIRectory?.

.. method:: QueryOverlappingSweepSegments(self, segment)
           
        This function queries whether the analyzer supports overlapping sweep
        segments.
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:OVERlap?
        
        

   :param segment: Sweep segment number. Segmentnumbers must be sequential. The specified segment number must besmaller or equal to the number of existing segments plus 1. Moreover,segment numbers must selected such that the corresponding frequencyranges are in ascending order.If one or more sweep segments with segment numbers <Segment> or largerexist in the current channel, then all these existing segment numbersare incremented by 1 and the new segment is inserted as segment no.<Segment>.
   :return: overlapping

.. method:: QuerySumOfSweepSegmentsTime(self, channel=1)
           
        Returns the total duration of the segmented sweep, calculated as the
        sum of the sweep times of the individual segments
        ([SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME).
        
        Remote-control command(s):
        [SENSe<Ch>:]SEGMent<Seg>:SWEep:TIME:SUM?
        
        

   :param channel: Channel number.
   :return: sweepTime

.. method:: SetPulseTimeStart(self, channel=1, timeStart)
           
        This function sets the start time of the displayed time range relative
        to the trigger time.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:TIME:STARt <start>
        
        

   :param timeStart: This control sets the start time of the displayedtime range relative to the trigger time.
   :param channel: Channel number.

.. method:: GetPulseTimeStart(self, channel=1)
           
        This function gets the start time of the displayed time range relative
        to the trigger time.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:TIME:STARt?
        
        

   :param channel: Channel number.
   :return: timeStart

.. method:: SetPulseTimeStop(self, channel=1, timeStop)
           
        This function sets the stop time of the displayed time range relative
        to the trigger time.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:TIME:STOP <stop>
        
        

   :param timeStop: This control sets the stop time of the displayedtime range relative to the trigger time.
   :param channel: Channel number.

.. method:: GetPulseTimeStop(self, channel=1)
           
        This function gets the stop time of the displayed time range relative
        to the trigger time.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:TIME:STOP?
        
        

   :param channel: Channel number.
   :return: timeStop

.. method:: SetPulseTimeBandwidth(self, channel=1, timeBandwidth)
           
        This function sets the IF bandwidth for pulse profile measurements.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:TIME:BWIDth[:RESolution] <bandwidth>
        
        

   :param channel: Channel number.
   :param timeBandwidth: This control sets the IF bandwidth for pulseprofile measurements.

.. method:: GetPulseTimeBandwidth(self, channel=1)
           
        This function gets the IF bandwidth for pulse profile measurements.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:TIME:BWIDth[:RESolution]?
        
        

   :param channel: Channel number.
   :return: timeBandwidth

.. method:: SetPulseCoupledSectionLimitLinesState(self, channel=1, coupleLimits)
           
        This function couples the section limits for averaging (and the
        section limit lines) for all receivers and source ports and in all
        channels.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:COUPled[:STATe] <Boolean>
        
        

   :param coupleLimits: This control selects the limits coupled oruncoupled.
   :param channel: Channel number.

.. method:: GetPulseCoupledSectionLimitLinesState(self, channel=1)
           
        This function returns the state of coupling the section limits for
        averaging (and the section limit lines) for all receivers and source
        ports and in all channels.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:COUPled[:STATe]?
        
        

   :param channel: Channel number.
   :return: coupleLimits

.. method:: SetPulseEvaluationMode(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber, evaluationMode)
           
        This function specifies whether the wave quantity is displayed as
        measured or whether it is averaged.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:GENerator<gen_no>:EVALuation:MODE
        NORMal | MEAN
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:SRCPort<port_no>:EVALuation:MODE
        NORMal | MEAN
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:GENerator<gen_no>:EVALuation:MODE
        NORMal | MEAN
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:SRCPort<port_no>:EVALuation:MODE
        NORMal | MEAN
        
        

   :param generatorPortNumber: This control defines the number of a previously configuredexternal generator or number of the analyzer source port (this dependson the selection of the interface type).
   :param receiverType: This control selects the receiver type.
   :param evaluationMode: This control specifies whetherthe wave quantity is displayed as measured or whether it is averaged.
   :param interfaceType: This control selects theinterface type.
   :param recordNumber: This controldefines the number of the reference receiver (= port number of theanalyzer)
   :param channel: Channel number.

.. method:: GetPulseEvaluationMode(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber)
           
        This function returns whether the wave quantity is displayed as
        measured or whether it is averaged.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:GENerator<gen_no>:EVALuation:MODE
        ?
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:SRCPort<port_no>:EVALuation:MODE?
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:GENerator<gen_no>:EVALuation:MODE
        ?
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:SRCPort<port_no>:EVALuation:MODE?
        
        

   :param interfaceType: This control selects theinterface type.
   :param generatorPortNumber: This control defines the number of a previously configuredexternal generator or number of the analyzer source port (this dependson the selection of the interface type).
   :param receiverType: This control selects the receiver type.
   :param recordNumber: This controldefines the number of the reference receiver (= port number of theanalyzer)
   :param channel: Channel number.
   :return: evaluationMode

.. method:: SetPulseEvaluationSectionStart(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber, evaluationStartTime)
           
        This function defines the start time of the averaging section for the
        wave quantity.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:GENerator<gen_no>:EVALuation:STAR
        t <section_start>
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:SRCPort<port_no>:EVALuation:STARt
        <section_start>
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:GENerator<gen_no>:EVALuation:STAR
        t <section_start>
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:SRCPort<port_no>:EVALuation:STARt
        <section_start>
        
        

   :param generatorPortNumber: This control defines the number of a previously configuredexternal generator or number of the analyzer source port (this dependson the selection of the interface type).
   :param receiverType: This control selects the receiver type.
   :param interfaceType: This control selects theinterface type.
   :param evaluationStartTime: This control sets thestart time of the averaging section.
   :param recordNumber: This controldefines the number of the reference receiver (= port number of theanalyzer)
   :param channel: Channel number.

.. method:: GetPulseEvaluationSectionStart(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber)
           
        This function returns the start time of the averaging section for the
        wave quantity.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:GENerator<gen_no>:EVALuation:STAR
        t?
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:SRCPort<port_no>:EVALuation:STARt
        ?
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:GENerator<gen_no>:EVALuation:STAR
        t?
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:SRCPort<port_no>:EVALuation:STARt
        ?
        
        

   :param interfaceType: This control selects theinterface type.
   :param generatorPortNumber: This control defines the number of a previously configuredexternal generator or number of the analyzer source port (this dependson the selection of the interface type).
   :param receiverType: This control selects the receiver type.
   :param recordNumber: This controldefines the number of the reference receiver (= port number of theanalyzer)
   :param channel: Channel number.
   :return: evaluationStartTime

.. method:: SetPulseEvaluationSectionStop(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber, evaluationStopTime)
           
        This function defines the stop time of the averaging section for the
        wave quantity.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:GENerator<gen_no>:EVALuation:STOP
        <section_stop>
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:SRCPort<port_no>:EVALuation:STOP
        <section_stop>
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:GENerator<gen_no>:EVALuation:STOP
        <section_stop>
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:SRCPort<port_no>:EVALuation:STOP
        <section_stop>
        
        

   :param generatorPortNumber: This control defines the number of a previously configuredexternal generator or number of the analyzer source port (this dependson the selection of the interface type).
   :param receiverType: This control selects the receiver type.
   :param interfaceType: This control selects theinterface type.
   :param evaluationStopTime: This control sets thestop time of the averaging section.
   :param recordNumber: This controldefines the number of the reference receiver (= port number of theanalyzer)
   :param channel: Channel number.

.. method:: GetPulseEvaluationSectionStop(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber)
           
        This function returns the stop time of the averaging section for the
        wave quantity.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:GENerator<gen_no>:EVALuation:STOP
        ?
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:SRCPort<port_no>:EVALuation:STOP?
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:GENerator<gen_no>:EVALuation:STOP
        ?
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:SRCPort<port_no>:EVALuation:STOP?
        
        

   :param interfaceType: This control selects theinterface type.
   :param generatorPortNumber: This control defines the number of a previously configuredexternal generator or number of the analyzer source port (this dependson the selection of the interface type).
   :param receiverType: This control selects the receiver type.
   :param recordNumber: This controldefines the number of the reference receiver (= port number of theanalyzer)
   :param channel: Channel number.
   :return: evaluationStopTime

.. method:: SetPulseSectionLimitLinesState(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber, limitLinesState)
           
        This function displays or hides the limit lines of the averaging
        section for the wave quantity.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:GENerator<gen_no>:LINEs[:STATe]
        <Boolean>
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:SRCPort<port_no>:LINEs[:STATe]
        <Boolean>
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:GENerator<gen_no>:LINEs[:STATe]
        <Boolean>
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:SRCPort<port_no>:LINEs[:STATe]
        <Boolean>
        
        

   :param generatorPortNumber: This control defines the number of a previously configuredexternal generator or number of the analyzer source port (this dependson the selection of the interface type).
   :param receiverType: This control selects the receiver type.
   :param interfaceType: This control selects theinterface type.
   :param channel: Channel number.
   :param recordNumber: This controldefines the number of the reference receiver (= port number of theanalyzer)
   :param limitLinesState: This control displays orhides the limit lines of the averaging section for the wave quantity.

.. method:: GetPulseSectionLimitLinesState(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber)
           
        This function returns the limit lines state of the averaging section
        for the wave quantity.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:GENerator<gen_no>:LINEs[:STATe]?
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:SRCPort<port_no>:LINEs[:STATe]?
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:GENerator<gen_no>:LINEs[:STATe]?
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:SRCPort<port_no>:LINEs[:STATe]?
        
        

   :param interfaceType: This control selects theinterface type.
   :param generatorPortNumber: This control defines the number of a previously configuredexternal generator or number of the analyzer source port (this dependson the selection of the interface type).
   :param receiverType: This control selects the receiver type.
   :param recordNumber: This controldefines the number of the reference receiver (= port number of theanalyzer)
   :param channel: Channel number.
   :return: limitLinesState

.. method:: SetPulseShiftStimulus(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber, shiftStimulus)
           
        This function defines an offset time (shift stimulus) for the wave
        quantity.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:GENerator<gen_no>:TRIGger:DELay
        <shift_stimulus>
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:SRCPort<port_no>:TRIGger:DELay
        <shift_stimulus>
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:GENerator<gen_no>:TRIGger:DELay
        <shift_stimulus>
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:SRCPort<port_no>:TRIGger:DELay
        <shift_stimulus>
        
        

   :param shiftStimulus: This control sets the offsettime.
   :param generatorPortNumber: This control defines the number of a previously configuredexternal generator or number of the analyzer source port (this dependson the selection of the interface type).
   :param receiverType: This control selects the receiver type.
   :param interfaceType: This control selects theinterface type.
   :param recordNumber: This controldefines the number of the reference receiver (= port number of theanalyzer)
   :param channel: Channel number.

.. method:: GetPulseShiftStimulus(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber)
           
        This function returns an offset time (shift stimulus) for the wave
        quantity.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:GENerator<gen_no>:TRIGger:DELay?
        [SENSe<Ch>:]PULSe:RECeiver:A<rec_no>:SRCPort<port_no>:TRIGger:DELay?
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:GENerator<gen_no>:TRIGger:DELay?
        [SENSe<Ch>:]PULSe:RECeiver:B<rec_no>:SRCPort<port_no>:TRIGger:DELay?
        
        

   :param interfaceType: This control selects theinterface type.
   :param generatorPortNumber: This control defines the number of a previously configuredexternal generator or number of the analyzer source port (this dependson the selection of the interface type).
   :param receiverType: This control selects the receiver type.
   :param recordNumber: This controldefines the number of the reference receiver (= port number of theanalyzer)
   :param channel: Channel number.
   :return: shiftStimulus

.. method:: ReadTimeSamplesData(self, channel_Trace, traceData)
           
        This function reads the SSRAM Data in Pulse Profile Mode. Only for
        traces with wave quantities (a- or b- waves)
        
        Remote-control command(s):
        CALCulate<Ch>:DATA? TSData
        
        

   :param channel_Trace: Channel number used toidentify the active trace.
   :param traceData: Returns the SSRAM Data in Pulse Profile Mode.
   :return: noOfValues

.. method:: SetSweepNumberOfPoints(self, channel=1, numberOfPoints)
           
        This function defines the total number of measurement points per
        sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:POINts
        
        

   :param channel: Channel number.
   :param numberOfPoints: This control defines the total number ofmeasurement points per sweep.

.. method:: GetSweepNumberOfPoints(self, channel=1)
           
        This function queries the total number of measurement points per
        sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:POINts?
        
        

   :param channel: Channel number.
   :return: numberOfPoints

.. method:: SetFrequencyStepSize(self, channel=1, stepSize)
           
        This function sets the distance between two consecutive sweep points.
        
        Note(s):
        
        (1) This setting is valid for sweep types with equidistant sweep
        points only. It does not apply to logarithmic and segmented sweeps.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:STEP <step_size>
        
        

   :param stepSize: This control defines the stimulus step size.
   :param channel: Channel number.

.. method:: GetFrequencyStepSize(self, channel=1)
           
        This function gets the distance between two consecutive sweep points.
        
        Note(s):
        
        (1) This setting is valid for sweep types with equidistant sweep
        points only. It does not apply to logarithmic and segmented sweeps.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:STEP?
        
        

   :param channel: Channel number.
   :return: stepSize

.. method:: SetSweepCount(self, channel=1, sweepCount)
           
        This function defines the number of sweeps to be measured in single
        sweep mode.
        
        Remote-control command(s):
        SENSe<Ch>:]SWEep:COUNt <No_of_Sweeps>
        
        

   :param channel: Channel number.
   :param sweepCount: Defines the number of consecutive sweeps to bemeasured.

.. method:: GetSweepCount(self, channel=1)
           
        This function returns the number of sweeps to be measured in single
        sweep mode.
        
        Remote-control command(s):
        SENSe<Ch>:]SWEep:COUNt?
        
        

   :param channel: Channel number.
   :return: sweepCount

.. method:: ConfigureSweepTime(self, channel=1, autoSweepTime, sweepTime, measDelay)
           
        This function sets the measurement time for a sweep or delay the start
        of each sweep.
        
        Note(s):
        
        The sweep duration is ignored for the sweep types Time and CW Mode.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TIME:AUTO <Boolean>
        [SENSe<Ch>:]SWEep:TIME <numeric_value>
        [SENSe<Ch>:]SWEep:DWELl <numeric_value>
        
        

   :param measDelay: Meas. delay sets a delay time allowing the DUT tosettle before the hardware settings of the analyzer are changed and anew partial measurement is started.
   :param sweepTime: Sets the duration of the sweep (Sweep Time).
   :param autoSweepTime: When enabled, the (minimum) sweep duration iscalculated internally using the other channel settings and zero delay.
   :param channel: Channel number.

.. method:: SetSweepTime(self, channel=1, sweepTime)
           
        This function sets the duration of the sweep (Sweep Time). Setting a
        duration disables the automatic calculation of the (minimum) sweep
        time; see [SENSe<Ch>:]SWEep:TIME:AUTO.
        
        Note(s):
        
        The sweep duration is ignored for the sweep types Time and CW Mode.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TIME <numeric_value>
        
        

   :param sweepTime: Sets the duration of the sweep (Sweep Time).
   :param channel: Channel number.

.. method:: GetSweepTime(self, channel=1)
           
        This function returns the duration of the sweep (Sweep Time).
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TIME?
        
        

   :param channel: Channel number.
   :return: sweepTime

.. method:: SetSweepMeasDelay(self, channel=1, measDelay)
           
        This function defines the Meas. Delay time for each partial
        measurement. Setting a delay disables the automatic calculation of the
        (minimum) sweep time; see [SENSe<Ch>:]SWEep:TIME:AUTO.
        
        Note(s):
        
        The sweep duration is ignored for the sweep types Time and CW Mode.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:DWELl <numeric_value>
        
        

   :param measDelay: Meas. delay before each partial measurement.
   :param channel: Channel number.

.. method:: GetSweepMeasDelay(self, channel=1)
           
        This function returns the Meas. Delay time for each partial
        measurement.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:DWELl?
        
        

   :param channel: Channel number.
   :return: measDelay

.. method:: SetSweepTimeAuto(self, channel=1, autoSweepTime)
           
        This function when enabled, the (minimum) sweep duration is calculated
        internally using the other channel settings and zero delay
        ([SENSe<Ch>:]SWEep:DWELl).
        
        Note(s):
        
        The automatically calculated sweep duration is ignored for the sweep
        types Time and CW Mode.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TIME:AUTO <Boolean>
        
        

   :param autoSweepTime: When enabled, the (minimum) sweep duration iscalculated internally using the other channel settings and zero delay.
   :param channel: Channel number.

.. method:: GetSweepTimeAuto(self, channel=1)
           
        This function returns if the (minimum) sweep duration is calculated
        internally using the other channel settings and zero delay
        ([SENSe<Ch>:]SWEep:DWELl) or not.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:TIME:AUTO?
        
        

   :param channel: Channel number.
   :return: autoSweepTime

.. method:: ConfigureTriggerFreeRun(self, channel=1)
           
        This function configures free run measurement without waiting for
        trigger events.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce IMMediate
        
        

   :param channel: Channel number.

.. method:: ConfigureTriggerExternal(self, channel=1, triggerOn)
           
        This function configures the external trigger mode. In External
        trigger mode the measurement is triggered by a low-voltage (3.3 V)
        external TTL signal applied either to the BNC connector EXT TRIGGER or
        to pin 2 of the USER CONTROL connector at the rear panel. The two
        trigger inputs are equivalent; nor additional setting for signal
        routing is required.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce EXTernal
        TRIGger<Ch>[:SEQuence]:SLOPe POSitive | NEGative
        
        

   :param triggerOn: This control qualifies whether the trigger eventoccurs on the rising or on the falling edge of the external TTLtrigger signal.
   :param channel: Channel number.

.. method:: ConfigureTriggerPeriodic(self, channel=1, triggerPeriod)
           
        This function configures the periodic trigger mode. In Periodic
        trigger mode the measurement is triggered by the periodic signal of an
        internal clock generator.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce TIMer
        TRIGger<Ch>[:SEQuence]:TIMer
        
        

   :param triggerPeriod: This control sets the period of the internalperiodic signal that can be used as a trigger source.
   :param channel: Channel number.

.. method:: ConfigureTriggerRFPower(self, channel=1)
           
        This function configures the RF Power trigger mode. In RF Power
        trigger mode the trigger signal is generated from one of the generated
        or measured RF signals.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce RFPower
        
        

   :param channel: Channel number.

.. method:: ConfigureTriggerManual(self, channel=1)
           
        This function configures the manual trigger mode. In Manual trigger
        mode the trigger signal is generated on pressing the Manual Trigger
        softkey or sending *TRG remote command (function rszvb_SendTrigger).
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce MANual
        
        

   :param channel: Channel number.

.. method:: ConfigureTriggerSettings(self, channel=1, triggerMeasSequence, triggerDelay)
           
        This function configures the trigger settings.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:LINK 'POINT' | 'SWEEP' | 'PPOINT' | 'SEGMENT'
        TRIGger<Ch>[:SEQuence]:HOLDoff
        
        

   :param triggerMeasSequence: This control selects the Triggered Meas.Sequence.
   :param channel: Channel number.
   :param triggerDelay: This control defines a delay time between the trigger eventand the start of the measurement.

.. method:: SetTriggerSource(self, channel=1, triggerSource)
           
        This function selects the source for the events that the analyzer uses
        to start a sweep.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce IMMediate | EXTernal | TIMer | MANual |
        RFPower | PGENerator
        
        

   :param triggerSource: This control selects the source for the eventsthat the analyzer uses to start a sweep.
   :param channel: Channel number.

.. method:: GetTriggerSource(self, channel=1)
           
        This function queries selected source for the events that the analyzer
        uses to start a sweep.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SOURce?
        
        

   :param channel: Channel number.
   :return: triggerSource

.. method:: SetTriggerDelay(self, channel=1, triggerDelay)
           
        This function defines a delay time between the trigger event and the
        start of the measurement.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff
        
        

   :param triggerDelay: This control defines a delay time between thetrigger event and the start of the measurement.
   :param channel: Channel number.

.. method:: GetTriggerDelay(self, channel=1)
           
        This function queries a delay time between the trigger event and the
        start of the measurement.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff?
        
        

   :param channel: Channel number.
   :return: triggerDelay

.. method:: SetPartialMeasurementTriggerMode(self, channel=1, triggerMode)
           
        Qualifies whether the trigger delay is valid for all physical ports
        (including external generator) or source port-specific. This setting
        is available if the triggered measurement sequence is a partial
        measurement.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff:MODE PALL | PSPecific
        
        

   :param triggerMode: Qualifies whether the trigger delay is valid forall physical ports (including external generator) or source port-specific.
   :param channel: Channel number.

.. method:: GetPartialMeasurementTriggerMode(self, channel=1)
           
        Queries whether the trigger delay is valid for all physical ports
        (including external generator) or source port-specific.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff:MODE?
        
        

   :param channel: Channel number.
   :return: triggerMode

.. method:: SetGeneratorPortTriggerDelay(self, channel=1, generatorPort, triggerDelay)
           
        Defines the trigger delay for a generator port <Gen>. The setting
        takes effect when a port-specific trigger delay is selected
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff:GENerator<Gen>
        
        

   :param triggerDelay: This control defines a delay time between thetrigger event and the start of the measurement.
   :param channel: Channel number.
   :param generatorPort: Generator port number.

.. method:: GetGeneratorPortTriggerDelay(self, channel=1, generatorPort)
           
        Queries the trigger delay for a generator port <Gen>.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff:GENerator<Gen>?
        
        

   :param channel: Channel number.
   :param generatorPort: Generator port number.
   :return: triggerDelay

.. method:: SetPhysicalPortTriggerDelay(self, channel=1, analyzerPort, triggerDelay)
           
        Defines the trigger delay for a physical analyzer port <Pt>. The
        setting takes effect when a port-specific trigger delay is selected.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff:PORT<Pt>
        
        

   :param analyzerPort: Physical analyzer port number.
   :param triggerDelay: This control defines a delay time between thetrigger event and the start of the measurement.
   :param channel: Channel number.

.. method:: GetPhysicalPortTriggerDelay(self, channel=1, analyzerPort)
           
        Queries the trigger delay for a physical analyzer port <Pt>.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:HOLDoff:PORT<Pt>?
        
        

   :param analyzerPort: Physical analyzer port number.
   :param channel: Channel number.
   :return: triggerDelay

.. method:: SetTriggeredMeasSequence(self, channel=1, triggerMeasSequence)
           
        This function selects the Triggered Meas. Sequence.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:LINK 'POINT' | 'SWEEP' | 'PPOINT' | 'SEGMENT'
        
        

   :param triggerMeasSequence: This control selects the Triggered Meas.Sequence.
   :param channel: Channel number.

.. method:: GetTriggeredMeasSequence(self, channel=1)
           
        This function queries selected Triggered Meas. Sequence.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:LINK?
        
        

   :param channel: Channel number.
   :return: triggerMeasSequence

.. method:: SetTriggerOn(self, channel=1, triggerOn)
           
        This function qualifies whether the trigger event occurs on the rising
        or on the falling edge of the external TTL trigger signal.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SLOPe POSitive | NEGative
        
        

   :param triggerOn: This control qualifies whether the trigger eventoccurs on the rising or on the falling edge of the external TTLtrigger signal.
   :param channel: Channel number.

.. method:: GetTriggerOn(self, channel=1)
           
        This function queries whether the trigger event occurs on the rising
        or on the falling edge of the external TTL trigger signal.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:SLOPe?
        
        

   :param channel: Channel number.
   :return: triggerOn

.. method:: SetTriggerPeriod(self, channel=1, triggerPeriod)
           
        This function sets the period of the internal periodic signal that can
        be used as a trigger source.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:TIMer
        
        

   :param triggerPeriod: This control sets the period of the internalperiodic signal that can be used as a trigger source.
   :param channel: Channel number.

.. method:: GetTriggerPeriod(self, channel=1)
           
        This function queries the period of the internal periodic signal that
        can be used as a trigger source.
        
        Remote-control command(s):
        TRIGger<Ch>[:SEQuence]:TIMer?
        
        

   :param channel: Channel number.
   :return: triggerPeriod

.. method:: SendTrigger(self, )
           
        This function triggers all actions waiting for a trigger event.
        Generates a manual trigger signal (Manual Trigger).
        
        Remote-control command(s):
        *TRG
        
        


.. method:: SendTriggerWaitOPC(self, timeout)
           
        This function triggers all actions waiting for a trigger event in the
        selected window and waits for operation completed (OPC) before
        returning the status code.
        
        Remote-control command(s):
        *TRG
        *OPC?
        
        

   :param timeout: Sets the timeout for thetriggering routine to be finished. If the length of time required fortriggering exceeds the timeout value, then the function will returnwith a timeout error.

.. method:: SendChannelTrigger(self, channel=1)
           
        This function starts a new single sweep sequence. This function is
        available in single sweep mode only (INITiate<Ch>:CONTinuous OFF).
        
        Note(s):
        
        (1) In contrast to all other functions of the analyzer,
        INITiate<Ch>[:IMMediate] has been implemented to prevent overlapped
        execution.
        
        (2) The data of the last sweep can be read using
        CALCulate<Ch>:DATA:NSWeep? SDATa, <history_count>.
        
        Remote-control command(s):
        INITiate<Ch>[:IMMediate]
        
        

   :param channel: Channel number.

.. method:: SendChannelTriggerWaitOPC(self, channel=1, timeout)
           
        This function starts a new single sweep sequence and waits for
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
        INITiate<Ch>[:IMMediate]
        *OPC?
        
        

   :param timeout: Sets the timeout for the triggering routine to befinished. If the length of time required for triggering exceeds thetimeout value, then the function will return with a timeout error.
   :param channel: Channel number.

.. method:: SetSweepSingleAllChans(self, singleSweep)
           
        This function selects the scope of the single sweep sequence.
        
        Note(s):
        
        (1) The setting is applied in single sweep mode only.
        
        Remote-control command(s):
        INITiate<Ch>[:IMMediate]:SCOPe ALL | SINGle
        
        

   :param singleSweep: This control selects the scopeof the single sweep sequence.

.. method:: GetSweepSingleAllChans(self, )
           
        This function queries the scope of the single sweep sequence.
        
        Remote-control command(s):
        INITiate<Ch>[:IMMediate]:SCOPe?
        
        

   :return: singleSweep

.. method:: SweepRestart(self, channel=1)
           
        This function starts a new single sweep sequence.
        
        Note(s):
        
        (1) This function is available in single sweep mode only.
        
        Remote-control command(s):
        INITiate<Ch>[:IMMediate]
        
        

   :param channel: Channel number.

.. method:: SetSweepSingle(self, channel=1, singleSweep)
           
        This function qualifies whether the analyzer measures in single sweep
        or in continuous sweep mode.
        
        Remote-control command(s):
        INITiate<Ch>:CONTinuous OFF | ON
        
        

   :param channel: Channel number.
   :param singleSweep: This control qualifies whether the analyzermeasures in single sweep or in continuous sweep mode.

.. method:: GetSweepSingle(self, channel=1)
           
        This function queries whether the analyzer measures in single sweep or
        in continuous sweep mode.
        
        Remote-control command(s):
        INITiate<Ch>:CONTinuous?
        
        

   :param channel: Channel number.
   :return: singleSweep

.. method:: DefineGroupOfMeasuredPorts(self, channel=1, group, firstPort, lastPort)
           
        This function defines a group of measured ports numbered <Group>
        containing a continuous range of logical ports <First Port> and <Last
        Port>.
        
        Remote-control command(s):
        SOURce<Ch>:GROup<group_no>
        
        

   :param lastPort: This control defines the last port of definedgroup.
   :param firstPort: This control defines the first portof defined group.
   :param group: Port group number.
   :param channel: Channel number.

.. method:: GetGroupOfMeasuredPorts(self, channel=1, group)
           
        This function queries <First Port> and <Last Port> of group of
        measured ports numbered <Group>.
        
        Remote-control command(s):
        SOURce<Ch>:GROup<group_no>?
        
        

   :param group: Port group number.
   :param channel: Channel number.
   :return: firstPort
   :return: lastPort

.. method:: DefineGroupOfAllMeasuredPorts(self, channel=1, group, numberOfPortsInGroup, ports)
           
        This function defines a port group numbered <group_no> containing an
        arbitrary selection of logical ports. The ports do not have to be
        numbered continuously (as for port groups defined via
        SOURce<Ch>:GROup<group_no>).
        
        Note(s):
        
        (1) It is not possible to create more than one port group with
        arbitrary ports. To avoid errors, use the setting command only while
        the channel contains a single port group (e.g. after a *RST). You can
        use the query to read out the ports for an arbitrary number of port
        groups created via SOURce<Ch>:GROup<group_no>.
        
        Remote-control command(s):
        SOURce<Ch>:GROup<group_no>:PORTs <log_port1>{,<log_port2> ...}
        
        

   :param numberOfPortsInGroup: This control sets thenumber of ports of defined group.
   :param group: Port group number.
   :param ports: This control defines all ports of defined group.
   :param channel: Channel number.

.. method:: GetGroupOfAllMeasuredPorts(self, channel=1, group, ports)
           
        This function returns a port group numbered <group_no> containing an
        arbitrary selection of logical ports.
        
        Remote-control command(s):
        SOURce<Ch>:GROup<group_no>:PORTs?
        
        

   :param group: Port group number.
   :param ports: This control returnsall ports of defined group.
   :param channel: Channel number.
   :return: numberOfPortsInGroup

.. method:: GetPortGroupsCount(self, channel=1)
           
        This function queries the number of port groups in channel no. <Ch>.
        
        Note(s):
        
        (1) Port group no 1 is always present and can not be dissolved. After
        a *RST or after SOURce<Ch>:GROup<group_no>:CLEar ALL, port group no. 1
        contains all ports of the analyzer.
        
        Remote-control command(s):
        SOURce<Ch>:GROup<group_no>:COUNt?
        
        

   :param channel: Channel number.
   :return: portGroups

.. method:: DeleteGroupOfMeasuredPorts(self, channel=1, group)
           
        This function dissolves a group of measured ports.
        
        Remote-control command(s):
        SOURce<Ch>:GROup<group_no>:CLEar
        
        

   :param group: Port group number.
   :param channel: Channel number.

.. method:: DeleteAllGroupsOfMeasuredPorts(self, channel=1)
           
        This function dissolves all groups of measured ports.
        
        Remote-control command(s):
        SOURce<Ch>:GROup<group_no>:CLEar ALL
        
        

   :param channel: Channel number.

.. method:: DefineBalancedPort(self, channel=1, logicalPort, physicalPort1, physicalPort2)
           
        This function defines a balanced port numbered <Logicalog Port>,
        combining two physical ports <Physical Port 1> and <Physical Port 2>.
        
        Remote-control command(s):
        SOURce<Ch>:LPORt<log_port>
        
        

   :param physicalPort2: This control defines the port number.
   :param physicalPort1: This control defines the portnumber.
   :param channel: Channel number.
   :param logicalPort: Logical port number used to number balanced ports.

.. method:: GetBalancedPort(self, channel=1, logicalPort)
           
        This function queries a balanced port numbered <Logicalog Port>,
        combining two physical ports <Physical Port 1> and <Physical Port 2>.
        
        Remote-control command(s):
        SOURce<Ch>:LPORt<log_port>?
        
        

   :param channel: Channel number.
   :param logicalPort: Logical port number used to number balanced ports.
   :return: physicalPort1
   :return: physicalPort2

.. method:: DeleteBalancedPort(self, channel=1, logicalPort)
           
        This function dissolves selected balanced port.
        
        Remote-control command(s):
        SOURce<Ch>:LPORt<log_port>:CLEar
        
        

   :param channel: Channel number.
   :param logicalPort: Logical port number used to number balanced ports.

.. method:: DeleteAllBalancedPorts(self, channel=1)
           
        This function dissolves all balanced ports.
        
        Remote-control command(s):
        SOURce<Ch>:LPORt<log_port>:CLEar ALL
        
        

   :param channel: Channel number.

.. method:: SetDifferentialModeImpedance(self, channel=1, logicalPort, impedance)
           
        This function defines the differential mode impedance for selected
        balanced port.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:BALun:DZConversion:BPORt<logical_port>:ZDIFfe
        rent[:R]
        
        

   :param impedance: This control defines thedifferential mode impedance for the selected balanced port.
   :param channel: Channel number.
   :param logicalPort: Logical port number.

.. method:: GetDifferentialModeImpedance(self, channel=1, logicalPort)
           
        This function queries the differential mode impedance for selected
        balanced port.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:BALun:DZConversion:BPORt<logical_port>:ZDIFfe
        rent[:R]?
        
        

   :param channel: Channel number.
   :param logicalPort: Logical port number.
   :return: impedance

.. method:: SetCommonModeImpedance(self, channel=1, logicalPort, impedance)
           
        This function defines the common mode impedance for selected balanced
        port.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:BALun:DZConversion:BPORt<logical_port>:ZCOMmo
        n[:R]
        
        

   :param impedance: This control defines the commonmode impedance for the selected balanced port.
   :param channel: Channel number.
   :param logicalPort: Logical port number.

.. method:: GetCommonModeImpedance(self, channel=1, logicalPort)
           
        This function queries the common mode impedance for selected balanced
        port.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:BALun:DZConversion:BPORt<logical_port>:ZCOMmo
        n[:R]?
        
        

   :param channel: Channel number.
   :param logicalPort: Logical port number.
   :return: impedance

.. method:: DefinePortPair(self, channel=1, functionType, portPair, port1, port2)
           
        Defines a list of port pairs for port pair deembedding/embedding. The
        command can be used repeatedly to extend or overwrite the list.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>:DEFine
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>:DEFine
        
        
        

   :param port2: Second port number.
   :param portPair: Currentnumber of a port pair in the list.
   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :param port1: First port number.

.. method:: DeletePortPair(self, channel=1, functionType, portPair)
           
        Deletes the previously defined list of port pairs for port pair
        embedding/deembedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>:DELete
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>:DELete
        
        
        

   :param portPair: Currentnumber of a port pair in the list.
   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.

.. method:: SetDefaultConfigurationState(self, defaultSettings)
           
        This function overwrites the current settings of the multiport test
        set with the settings stored in the configuration file matrix.mtx. The
        file is stored in the directory C:\Program Files\Rohde&Schwarz\Network
        Analyzer\resources\extdev.
        
        Remote-control command(s):
        ROUTe<Ch>:CFILe ON | OFF
        
        

   :param defaultSettings: This control overwritesthe current settings of the multiport test set with the settingsstored in the configuration file.

.. method:: GetDefaultConfigurationState(self, )
           
        This function returns the default configuration state
        
        Remote-control command(s):
        ROUTe<Ch>:CFILe?
        
        

   :return: defaultSettings

.. method:: SetPortConfigration(self, channel=1, portGroupA, portGroupB, portGroupC, portGroupD)
           
        This function configures the internal signal paths of the multiport
        test set R&S ZV-Z83 for channel no. <Ch>.
        
        Remote-control command(s):
        ROUTe<Ch>:PORTs
        
        

   :param portGroupA: This control defines the "output" port number forgroup A.
   :param portGroupB: Thiscontrol defines the "output" port number for group B.
   :param portGroupC: Thiscontrol defines the "output" port number for group C.
   :param portGroupD: Thiscontrol defines the "output" port number for group D.
   :param channel: Channel number.

.. method:: GetPortConfigration(self, channel=1)
           
        This function returns the internal signal paths of the multiport test
        set R&S ZV-Z83 for channel no. <Ch>.
        
        Remote-control command(s):
        ROUTe<Ch>:PORTs?
        
        

   :param channel: Channel number.
   :return: portGroupA
   :return: portGroupB
   :return: portGroupC
   :return: portGroupD

.. method:: SetConverterPowerOffset(self, channel=1, port, portPowerOffset, offsetParameter)
           
        This function defines a source power or a power offset relative to the
        channel power (SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate][:AMPlitude])
        for a frequency converter port <Pt>. The command is available for
        converters with electronic attenuators (R&S ZVA-ZxxxE). An additional
        Cal Power Offset can be defined via
        SOURce<Ch>:POWer<Pt>:CORRection:LEVel:OFFSet.
        
        
        Notes:
        
        (1) This command is available for frequency converters with electronic
        attenuators R&S ZVA-ZxxxE.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:OFFSet <numeric_value>, ONLY | CPADd
        
        

   :param offsetParameter: This control sets the offsetparameter.
   :param portPowerOffset: This control sets the port-specific power offset.
   :param port: Test port number of the analyzer
   :param channel: Channel number.

.. method:: GetConverterPowerOffset(self, channel=1, port)
           
        This function returns a source power or a power offset relative to the
        channel power for a frequency converter port <Pt>. An additional Cal
        Power Offset can be defined via
        SOURce<Ch>:POWer<Pt>:CORRection:LEVel:OFFSet.
        
        Notes:
        
        (1) This command is available for frequency converters with electronic
        attenuators R&S ZVA-ZxxxE.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:OFFSet?
        
        

   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :return: portPowerOffset
   :return: offsetParameter

.. method:: SetConverterCalPowerOffset(self, channel=1, converter, calPowerOffset)
           
        This function specifies a gain (positive values) or an attenuation
        (negative values) in the signal path between the converter source port
        <Con> and the calibrated reference plane (Cal Power Offset). The value
        has no impact on the source power.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:CONVerter<Con>:LEVel:OFFSet
        
        

   :param calPowerOffset: This control specifies a gain (positivevalues) or an attenuation (negative values) in the signal path betweenthe converter source port <Con> and the calibrated reference plane(Cal Power Offset). The value has no impact on the source power.
   :param converter: Converter number.
   :param channel: Channel number.

.. method:: GetConverterCalPowerOffset(self, channel=1, converter)
           
        This function returns the offset in the signal path between the
        converter source port <Con> and the calibrated reference plane (Cal
        Power Offset).
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:CONVerter<Con>:LEVel:OFFSet?
        
        

   :param converter: Converter number.
   :param channel: Channel number.
   :return: calPowerOffset

.. method:: SetAdvancedPowerTransferModelFrequencyState(self, channel=1, state)
           
        This function enables or disables the advanced power transfer model
        for frequency converters.
        
        Note(s):This function overwrites the port specific power transfer
        model selection; see SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:AMODel.
        
        Remote-control command(s):
        [SENSe<Ch>:]CONVerter:AMODel <Boolean>
        
        

   :param state: This control enables or disables the advanced powertransfer model for frequency converters.
   :param channel: Channel number.

.. method:: GetAdvancedPowerTransferModelFrequencyState(self, channel=1)
           
        This function returns the advanced power transfer model for frequency
        converters state.
        
        Remote-control command(s):
        [SENSe<Ch>:]CONVerter:AMODel?
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetSenseTypeOfPortTransferModel(self, channel=1, port, modelType)
           
        This function selects the type of advanced power transfer model for
        the converter port <Pt>.
        
        Note(s):This function overwrites by the general power transfer model
        settings; see [SENSe<Ch>:]CONVerter:DESCription.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:DESCription NONE | ELECtronic
        | DSET | LAPProx
        
        

   :param modelType: Type of advanced power transfermodel for the converter port <Pt>.
   :param port: Test port number of the analyzer
   :param channel: Channel number.

.. method:: GetSenseTypeOfPortTransferModel(self, channel=1, port)
           
        This function returns the type of advanced power transfer model for
        the converter port <Pt>.
        
        Note(s):This function overwrites by the general power transfer model
        settings; see [SENSe<Ch>:]CONVerter:DESCription.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:DESCription?
        
        

   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :return: modelType

.. method:: SetSenseTypeOfAdvancedPowerTransferModel(self, channel=1, modelType)
           
        This function selects the type of advanced power transfer model.
        
        Note(s):This function overwrites the port specific setting; see
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:DESCription.
        
        Remote-control command(s):
        [SENSe<Ch>:]CONVerter:DESCription NONE | ELECtronic | DSET | LAPProx
        
        

   :param modelType: Type of advanced power transfer model.
   :param channel: Channel number.

.. method:: GetSenseTypeOfAdvancedPowerTransferModel(self, channel=1)
           
        This function returns the type of advanced power transfer model.
        
        Remote-control command(s):
        [SENSe<Ch>:]CONVerter:DESCription?
        
        

   :param channel: Channel number.
   :return: modelType

.. method:: SetConverterDataSetType(self, port, dataSetType)
           
        This function specifies whether factory data or a user-defined data
        set shall be used.
        
        Note(s):
        
        (1) Use function rszvb_SetSenseTypeOfPortTransferModel to set the Data
        Set mode.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:DSET FACTory | USER
        
        

   :param dataSetType: Selects the data set type.
   :param port: Converter port number

.. method:: GetConverterDataSetType(self, port)
           
        This function returns whether factory data or a user-defined data was
        used.
        
        Note(s):
        
        (1) Use function rszvb_SetSenseTypeOfPortTransferModel to set the Data
        Set mode.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:DSET?
        
        

   :param port: Converter port number
   :return: dataSetType

.. method:: SetConverterUserDataSetDirectory(self, port, directory)
           
        This function specifies the user data directory for the Data Set power
        control method.
        
        Note(s):
        
        (1) Use function rszvb_SetSenseTypeOfPortTransferModel to set the Data
        Set mode.
        
        (2) Use function rszvb_SetConverterDataSetType to set the User Data
        Set type.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:PATH
        
        

   :param directory: Sets the user data directory forthe Data Set power control method.
   :param port: Converter port number

.. method:: GetConverterUserDataSetDirectory(self, port, bufferSize, directory)
           
        This function returns the user data directory for the Data Set power
        control method.
        
        Note(s):
        
        (1) Use function rszvb_SetSenseTypeOfPortTransferModel to set the Data
        Set mode.
        
        (2) Use function rszvb_SetConverterDataSetType to set the User Data
        Set type.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:PATH?
        
        

   :param directory: Gets the user data directory for the Data Set power control method.
   :param bufferSize: This control defines size ofbuffer in 'title' argument.
   :param port: Converter port number

.. method:: SetConverterPortAssignment(self, port, serialNumber)
           
        This function assigns a R&S ZCxxx converter to port no. <Port>
        
        Note(s):
        
        (1) The adequate converter type and test setup have to be set
        beforehand using
        rszvb_SetFrequencyConversionType and
        rszvb_SetFrequencyConversionSource, respectively.
        
        Remote-control command(s):
        [SENSe<Ch>:]CONVerter:ASSign<Port>
        
        

   :param serialNumber: This control sets the serialnumber of the converter. For converters of the R&S ZCxxx family thisvalue should be set correctly. For converters of the ZVA-Zxxx familyit should be set to the empty string.
   :param port: Test port number of the analyzer

.. method:: GetConverterPortAssignment(self, port, bufferSize, serialNumber)
           
        This function returns the assigned R&S ZCxxx converter to port no.
        <Port>
        
        Remote-control command(s):
        [SENSe<Ch>:]CONVerter:ASSign<Port>?
        
        

   :param bufferSize: This control defines size ofbuffer in 'title' argument.
   :param port: Test port number of the analyzer
   :param serialNumber: This control gets the serialnumber of the converter.

.. method:: SetPortTransferModelState(self, channel=1, port, state)
           
        This function enables or disables the advanced power transfer model
        for the converter port <Pt>.
        
        Notes:
        (1) This command is overwritten by the general power transfer model
        settings; see [SENSe<Ch>:]CONVerter:AMODel.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:AMODel <Boolean>
        
        

   :param state: This control enables or disables theadvanced power transfer model for the converter port <Pt>.
   :param port: Test port number of the analyzer
   :param channel: Channel number.

.. method:: GetPortTransferModelState(self, channel=1, port)
           
        This function returns the advanced power transfer model for the
        converter port <Pt> state.
        
        Notes:
        (1) This command is overwritten by the general power transfer model
        settings; see [SENSe<Ch>:]CONVerter:AMODel.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:AMODel?
        
        

   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :return: state

.. method:: SetPortWaveguideAttenuator(self, channel=1, port, waveguideAttenuator, attenuation)
           
        This function selects the waveguide attenuator type of the converter
        port <Pt> and attenuation for a converter with electronic or
        mechanical attenuators at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:ATTenuator MECHanical |
        ELECtronic
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:ELECtronic:MATTenuation
        <attenuation>
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:MECHanical:ATTenuation
        <attenuation>
        
        

   :param waveguideAttenuator: Selects the waveguideattenuator type of the converter port <Pt>.
   :param attenuation: Thiscontrol specifies the attenuation factor for a converter withmechanical or electronic adjustment screw at port <Pt>.
   :param port: Test port number of the analyzer
   :param channel: Channel number.

.. method:: GetPortWaveguideAttenuatorType(self, channel=1, port)
           
        This function returns the waveguide attenuator type of the converter
        port <Pt> and attenuation for a converter with electronic or
        mechanical attenuators at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:ATTenuator?
        
        

   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :return: waveguideAttenuator

.. method:: GetPortWaveguideAttenuator(self, channel=1, port, waveguideAttenuator)
           
        This function returns the waveguide attenuator type of the converter
        port <Pt> and attenuation for a converter with electronic or
        mechanical attenuators at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:ELECtronic:MATTenuation?
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:MECHanical:ATTenuation?
        
        

   :param waveguideAttenuator: Selects the waveguideattenuator type of the converter port <Pt>.
   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :return: attenuation

.. method:: SetPortWaveguideAttenuatorSlope(self, channel=1, port, slope)
           
        This function specifies the slope for the linear power transfer model
        with 0 dB waveguide attenuation.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:SLOPe <slope>
        
        

   :param slope: This control specifies the slope forthe linear power transfer model with 0 dB waveguide attenuation.
   :param port: Test port number of the analyzer
   :param channel: Channel number.

.. method:: GetPortWaveguideAttenuatorSlope(self, channel=1, port)
           
        This function returns the slope for the linear power transfer model
        with 0 dB waveguide attenuation.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:SLOPe?
        
        

   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :return: slope

.. method:: SetPortWaveguideAttenuatorOffset(self, channel=1, port, offset)
           
        This function specifies the offset factor for the linear power
        transfer model with 0 dB waveguide attenuation.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:OFFSet <offset>
        
        

   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :param offset: This control specifies the Offsetfactor for the linear power transfer model with 0 dB waveguideattenuation.

.. method:: GetPortWaveguideAttenuatorOffset(self, channel=1, port)
           
        This function returns the offset factor for the linear power transfer
        model with 0 dB waveguide attenuation.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:OFFSet?
        
        

   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :return: offset

.. method:: SetPortElectronicPowerTreshold(self, channel=1, port, threshold)
           
        This function specifies the converter output power threshold for a
        converter with electronic attenuators at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:ELECtronic:LIMit <threshold>
        
        

   :param threshold: Converter output power below whichthe waveguide attenuator is used.
   :param port: Test port number of the analyzer
   :param channel: Channel number.

.. method:: GetPortElectronicPowerTreshold(self, channel=1, port)
           
        This function returns the converter output power threshold for a
        converter with electronic attenuators at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:ELECtronic:LIMit?
        
        

   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :return: threshold

.. method:: SetPortElectronicPowerReduction(self, channel=1, port, reduction)
           
        This function specifies the percentage of power reduction for a
        converter with electronic attenuators at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:ELECtronic:REDuction
        <percentage>
        
        

   :param reduction: Percentage of power reduction dueto the waveguide attenuator
   :param port: Test port number of the analyzer
   :param channel: Channel number.

.. method:: GetPortElectronicPowerReduction(self, channel=1, port)
           
        This function returns the percentage of power reduction for a
        converter with electronic attenuators at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CONVerter:TRANsfer:ELECtronic:REDuction?
        
        

   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :return: reduction

.. method:: SetSimultaneousMeasurementOfPortsGroups(self, channel=1, state)
           
        This function activates/deactivates simultaneous measurement of port
        groups. Please note that setting this flag does not change the port
        group setup.
        
        
        Note(s):
        
        (1) Simultaneous Measurement of Port Groups is not available in any
        one of the following situations:
        
        - Less than two port groups are defined
        - Frequency Converter mode is active
        - True Differential Mode or Defined Coherence Mode is active
        - In a frequency converting measurement where Measure Source Port
        Waves at: Source Frequency is chosen in the Port Configuration.
        
        Remote-control command(s):
        SOURce<Ch>:GROup:SIMultaneous:STATe
        
        

   :param state: This control activates/deactivates simultaneousmeasurement of port groups.
   :param channel: Channel number.

.. method:: GetSimultaneousMeasurementOfPortsGroups(self, channel=1)
           
        This function returns the state of simultaneous measurement of port
        groups.
        
        Remote-control command(s):
        SOURce<Ch>:GROup:SIMultaneous:STATe?
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetSimultaneousMeasurementFrequencyOffsetState(self, channel=1, state)
           
        This function activates/deactivates the Simultaneous Measurement with
        Frequency Offset which performs measurements within different port
        groups in parallel while applying different frequency offsets to the
        measurements in different port groups.
        
        Remote-control command(s):
        SOURce<Ch>:GROup:SIMultaneous:FOFFset[:STATe]
        
        

   :param state: This control activates/deactivates the SimultaneousMeasurement with Frequency Offset.
   :param channel: Channel number.

.. method:: GetSimultaneousMeasurementFrequencyOffsetState(self, channel=1)
           
        This function returns the state of the Simultaneous Measurement with
        Frequency Offset.
        
        Remote-control command(s):
        SOURce<Ch>:GROup:SIMultaneous:FOFFset[:STATe]?
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetSimultaneousMeasurementMinimumFrequencyOffsetMode(self, channel=1, minimumFrequencyOffset)
           
        This function defines how the minimum frequency offset between
        different port groups is determined for Simultaneous Measurement with
        Frequency Offset.
        
        Remote-control command(s):
        SOURce<Ch>:GROup:SIMultaneous:FOFFset:MOFFset:MODE DIRect | BANDwidth
        
        

   :param minimumFrequencyOffset: This control defines how the minimumfrequency offset between different port groups is determined forSimultaneous Measurement with Frequency Offset.
   :param channel: Channel number.

.. method:: GetSimultaneousMeasurementMinimumFrequencyOffsetMode(self, channel=1)
           
        This function queries how the minimum frequency offset between
        different port groups is determined for Simultaneous Measurement with
        Frequency Offset.
        
        Remote-control command(s):
        SOURce<Ch>:GROup:SIMultaneous:FOFFset:MOFFset:MODE?
        
        

   :param channel: Channel number.
   :return: minimumFrequencyOffset

.. method:: SetFrequencyConversion(self, measurementType, channel=1, port, numerator, denominator, offset, sweepType)
           
        This function defines the receiver frequency or the port-specific
        source frequency for frequency-converting measurements. The
        receiver/source frequency is either a range (for frequency sweeps) or
        a CW frequency (for power, time and CW Mode sweeps). The receiver
        frequency is valid for all ports.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:ARBitrary <numerator>, <denominator>,
        <offset>, CW | FIXed | SWEep
        SOURce<Ch>:FREQuency<Pt>:CONVersion:ARBitrary:IFRequency <numerator>,
        <denominator>, <offset>, CW | FIXed | SWEep
        
        

   :param denominator: This control defines the denominator.
   :param numerator: This control defines the numerator.
   :param offset: This control defines the offset.
   :param sweepType: This control select the sweep type.
   :param measurementType: This control selects themeasurement type.
   :param port: This control defines the port number.
   :param channel: Channel number.

.. method:: GetFrequencyConversion(self, measurementType, channel=1, port)
           
        This function queries the receiver frequency or the port-specific
        source frequency for frequency-converting measurements. The
        receiver/source frequency is either a range (for frequency sweeps) or
        a CW frequency (for power, time and CW Mode sweeps). The receiver
        frequency is valid for all ports.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:ARBitrary?
        SOURce<Ch>:FREQuency<Pt>:CONVersion:ARBitrary:IFRequency?
        
        

   :param measurementType: This control selects themeasurement type.
   :param port: This control defines the port number.
   :param channel: Channel number.
   :return: numerator
   :return: denominator
   :return: offset
   :return: sweepType

.. method:: SetPowerMeterFrequencyConversion(self, channel=1, powerMeterNumber, numerator, denominator, offset, sweepType)
           
        This function defines the receiver frequency for frequency-converting
        measurements. The receiver frequency is either a range (for frequency
        sweeps) or a CW frequency (for power, time and CW Mode sweeps). The
        receiver frequency is valid for all ports.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:ARBitrary:PMETer<Mtr> <numerator>,
        <denominator>, <offset>, CW | FIXed | SWEep
        
        

   :param denominator: This control defines the denominator.
   :param numerator: This control defines the numerator.
   :param offset: This control defines the offset.
   :param powerMeterNumber: This control sets the number of theconfigured power meter. Power meters must be numbered in ascendingorder, starting with 1. If a number is re-used, the previous powermeter configuration is overwritten.
   :param sweepType: This control select the sweep type.
   :param channel: Channel number.

.. method:: GetPowerMeterFrequencyConversion(self, channel=1, powerMeterNumber)
           
        This function returns the receiver frequency for frequency-converting
        measurements. The receiver frequency is either a range (for frequency
        sweeps) or a CW frequency (for power, time and CW Mode sweeps). The
        receiver frequency is valid for all ports.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:ARBitrary:PMETer<Mtr>?
        
        

   :param powerMeterNumber: This control sets the number of theconfigured power meter. Power meters must be numbered in ascendingorder, starting with 1. If a number is re-used, the previous powermeter configuration is overwritten.
   :param channel: Channel number.
   :return: numerator
   :return: denominator
   :return: offset
   :return: sweepType

.. method:: SetGeneratorFrequencyConversion(self, channel=1, port, generatorNumber, state, numerator, denominator, offset, sweepType)
           
        This function defines an external generator frequency for frequency-
        converting measurements. The external generator frequency is either a
        range (for frequency sweeps) or a CW frequency (for power, time and CW
        Mode sweeps).
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency<Pt>:CONVersion:ARBitrary:EFRequency<Gen>
        <Boolean>, <numerator>, <denominator>, <offset>, CW | FIXed | SWEep
        
        

   :param generatorNumber: This control sets the numberof the configured generator. Generators must be numbered in ascendingorder, starting with 1. If a number is re-used, the previous generatorconfiguration is overwritten.
   :param denominator: This control defines the denominator.
   :param numerator: This control defines thenumerator.
   :param state: This control switch the generator on or off.
   :param offset: This control defines the offset.
   :param sweepType: This control select the sweep type.
   :param port: This control defines the port number.
   :param channel: Channel number.

.. method:: GetGeneratorFrequencyConversion(self, channel=1, port, generatorNumber)
           
        This function returns an external generator frequency for frequency-
        converting measurements. The external generator frequency is either a
        range (for frequency sweeps) or a CW frequency (for power, time and CW
        Mode sweeps).
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency<Pt>:CONVersion:ARBitrary:EFRequency<Gen>?
        
        

   :param port: This control defines the port number.
   :param channel: Channel number.
   :param generatorNumber: This control sets the numberof the configured generator. Generators must be numbered in ascendingorder, starting with 1. If a number is re-used, the previous generatorconfiguration is overwritten.
   :return: state
   :return: numerator
   :return: denominator
   :return: offset
   :return: sweepType

.. method:: SetConverterSourceFrequency(self, channel=1, port, numerator, denominator, offset, sweepType)
           
        Defines the converter source frequency at the converter port <Pt>.
        
        Notes:
        
        (1) This command is available for frequency converters with electronic
        attenuators R&S ZVA-ZxxxE.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency<Pt>:CONVersion:ARBitrary:CFRequency <numerator>,
        <denominator>, <offset>, CW | FIXed | SWEep
        
        

   :param denominator: Denominator of the frequency formula. The sourcefrequency fs is calculated according tofs = <numerator>/<denominator>*fb. + <offset>
   :param numerator: Numerator of the frequency formula.The source frequency fs is calculated according tofs = <numerator>/<denominator>*fb. + <offset>
   :param offset: Offset of the frequency formula. Thesource frequency fs is calculated according tofs = <numerator>/<denominator>*fb. + <offset>
   :param sweepType: This control select the sweep type.
   :param port: Test port number of the analyzer
   :param channel: Channel number.

.. method:: GetConverterSourceFrequency(self, channel=1, port)
           
        This function returns the converter source frequency at the converter
        port <Pt>.
        
        Notes:
        
        (1) This command is available for frequency converters with electronic
        attenuators R&S ZVA-ZxxxE.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency<Pt>:CONVersion:ARBitrary:CFRequency?
        
        

   :param port: Test port number of the analyzer
   :param channel: Channel number.
   :return: numerator
   :return: denominator
   :return: offset
   :return: sweepType

.. method:: SetMeasureAWavesState(self, channel=1, state)
           
        This function defines whether a waves are measured at the source or at
        the receiver frequency. The setting is relevant for all frequency-
        converting measurements.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:AWReceiver[:STATe] <Boolean>
        
        

   :param state: This control defines whether a waves are measured atthe source or at the receiver frequency.
   :param channel: Channel number.

.. method:: GetMeasureAWavesState(self, channel=1)
           
        This function queries whether a waves are measured at the source or at
        the receiver frequency. The setting is relevant for all frequency-
        converting measurements.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:AWReceiver[:STATe]?
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetLocalOscilatorAState(self, channel=1, port, state)
           
        This function switches the Local Oscillator amplifier for the
        reference channel a on or off.
        
        Remote-control command(s):
        [SENSe<Ch>:]LOReference<Pt>[:STATe] <Boolean>
        
        

   :param state: This control switches the LocalOscillator amplifier for the reference channel a on or off.
   :param port: This control defines the port number.
   :param channel: Channel number.

.. method:: GetLocalOscilatorAState(self, channel=1, port)
           
        This function returns the state of the Local Oscillator amplifier for
        the reference channel a.
        
        Remote-control command(s):
        [SENSe<Ch>:]LOReference<Pt>[:STATe]?
        
        

   :param port: This control defines the port number.
   :param channel: Channel number.
   :return: state

.. method:: SetLocalOscilatorBState(self, channel=1, port, state)
           
        This function switches the Local Oscillator amplifier for the
        reference channel b on or off.
        
        Remote-control command(s):
        [SENSe<Ch>:]LOMeasure<Pt>[:STATe] <Boolean>
        
        

   :param state: This control switches the LocalOscillator amplifier for the reference channel b on or off.
   :param port: This control defines the port number.
   :param channel: Channel number.

.. method:: GetLocalOscilatorBState(self, channel=1, port)
           
        This function returns the state of the Local Oscillator amplifier for
        the reference channel b.
        
        Remote-control command(s):
        [SENSe<Ch>:]LOMeasure<Pt>[:STATe]?
        
        

   :param port: This control defines the port number.
   :param channel: Channel number.
   :return: state

.. method:: SetLogicalPortCommonRefImpedance(self, channel=1, port, real, imaginary)
           
        This function specifies the complex common mode reference impedance
        for the balanced (logical) port numbered <log_port>.
        
        Remote-control command(s):
        [SENSe<Ch>:]LPORt<log_port>:ZCOMmon <real>[, <imaginary>]
        
        

   :param real: This control defines the real part of the port impedance.
   :param imaginary: This control defines theimaginary part of the port impedance.
   :param port: This control defines the logical port number.
   :param channel: Channel number.

.. method:: GetLogicalPortCommonRefImpedance(self, channel=1, port)
           
        This function returns the complex common mode reference impedance for
        the balanced (logical) port numbered <log_port>.
        
        Remote-control command(s):
        [SENSe<Ch>:]LPORt<log_port>:ZCOMmon?
        
        

   :param port: This control defines the logical port number.
   :param channel: Channel number.
   :return: real
   :return: imaginary

.. method:: SetLogicalPortDifferentialRefImpedance(self, channel=1, port, real, imaginary)
           
        This function specifies the complex differential mode reference
        impedance for the balanced (logical) port numbered <log_port>.
        
        Remote-control command(s):
        [SENSe<Ch>:]LPORt<log_port>:ZDIFferent <real>[, <imaginary>]
        
        

   :param real: This control defines the real part of the port impedance.
   :param imaginary: This control defines theimaginary part of the port impedance.
   :param port: This control defines the logical port number.
   :param channel: Channel number.

.. method:: GetLogicalPortDifferentialRefImpedance(self, channel=1, port)
           
        This function returns the complex differential mode reference
        impedance for the balanced (logical) port numbered <log_port>.
        
        Remote-control command(s):
        [SENSe<Ch>:]LPORt<log_port>:ZDIFferent?
        
        

   :param port: This control defines the logical port number.
   :param channel: Channel number.
   :return: real
   :return: imaginary

.. method:: SetPortImpedancesRenormalization(self, channel=1, theory)
           
        This function selects the theory for the renormalization of port
        impedances. The selection has an impact on the conversion formulas for
        wave quantities and S-parameters.
        
        Remote-control command(s):
        CALCulate<Chn>:TRANsform:IMPedance:RNORmal TWAVes | PWAVes
        
        

   :param theory: This control selects the theory for the renormalizationof port impedances. The selection has an impact on the conversionformulas for wave quantities and S-parameters.
   :param channel: Channel number.

.. method:: GetPortImpedancesRenormalization(self, channel=1)
           
        This function returns the theory for the renormalization of port
        impedances.
        
        Remote-control command(s):
        CALCulate<Chn>:TRANsform:IMPedance:RNORmal?
        
        

   :param channel: Channel number.
   :return: theory

.. method:: SetPhysicalPortRefImpedance(self, channel=1, port, real, imaginary)
           
        This function specifies the complex reference impedance for the
        physical port numbered <phys_port>.
        
        Remote-control command(s):
        [SENSe<Ch>:]PORT<phys_port>:ZREFerence <real>[, <imaginary>]
        
        

   :param real: This control defines the real part of the port impedance.
   :param imaginary: This control defines theimaginary part of the port impedance.
   :param port: This control defines the logical port number.
   :param channel: Channel number.

.. method:: GetPhysicalPortRefImpedance(self, channel=1, port)
           
        This function returns the complex reference impedance for the physical
        port numbered <phys_port>.
        
        Remote-control command(s):
        [SENSe<Ch>:]PORT<phys_port>:ZREFerence?
        
        

   :param port: This control defines the logical port number.
   :param channel: Channel number.
   :return: real
   :return: imaginary

.. method:: SetIFGain(self, channel=1, port, IFGain)
           
        This function selects the IF gain in the measurement channel b.
        
        Remote-control command(s):
        [SENSe<Ch>:]POWer:IFGain<Pt>:MEASure AUTO | LNOise | LDIStortion
        
        

   :param IFGain: This control selects the IF gain inthe measurement channel b.
   :param port: This control defines the port number.
   :param channel: Channel number.

.. method:: GetIFGain(self, channel=1, port)
           
        This function returns the IF gain in the measurement channel b.
        
        Remote-control command(s):
        [SENSe<Ch>:]POWer:IFGain<Pt>:MEASure?
        
        

   :param port: This control defines the port number.
   :param channel: Channel number.
   :return: IFGain

.. method:: SetIFGainReferenceChannel(self, channel=1, port, IFGain)
           
        This function selects the IF gain in the reference channel a.
        
        Remote-control command(s):
        [SENSe<Ch>:]POWer:IFGain<Pt>:REFerence AUTO | LNOise | LDIStortion
        
        

   :param IFGain: This control selects the IF gain inthe reference channel a.
   :param port: This control defines the port number.
   :param channel: Channel number.

.. method:: GetIFGainReferenceChannel(self, channel=1, port)
           
        This function returns the IF gain in the reference channel a.
        
        Remote-control command(s):
        [SENSe<Ch>:]POWer:IFGain<Pt>:REFerence?
        
        

   :param port: This control defines the port number.
   :param channel: Channel number.
   :return: IFGain

.. method:: SetRFSignalSourceState(self, channel=1, port, state)
           
        This function turns the RF source power at a specified test port on or
        off.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:STATe <Boolean>
        
        

   :param state: This control turns the RF source power at a specifiedtest port on or off.
   :param port: Port numbers of the analyzer.
   :param channel: Channel number.

.. method:: GetRFSignalSourceState(self, channel=1, port)
           
        This function returns the RF source power state at a specified test
        port.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:STATe?
        
        

   :param port: Port numbers of the analyzer.
   :param channel: Channel number.
   :return: state

.. method:: SetPermanentSignalSourceState(self, channel=1, port, state)
           
        This function defines whether the source power is permanently on.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:PERManent[:STATe] <Boolean>
        
        

   :param state: This control defines whether the source power ispermanently on.
   :param port: Port numbers of the analyzer.
   :param channel: Channel number.

.. method:: GetPermanentSignalSourceState(self, channel=1, port)
           
        This function checks if the source power is permanently on.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:PERManent[:STATe]?
        
        

   :param port: Port numbers of the analyzer.
   :param channel: Channel number.
   :return: state

.. method:: SetPermanentSignalGeneratorState(self, channel=1, port, generatorNumber, state)
           
        This function defines whether the external generator power is
        permanently on.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:GENerator<Gen>:PERManent[:STATe] <Boolean>
        
        

   :param state: This control defines whether the external generatorpower is permanently on.
   :param port: Port numbers of the analyzer.
   :param channel: Channel number.
   :param generatorNumber: This control sets the number of the configuredgenerator. Generators must be numbered in ascending order, startingwith 1. If a number is re-used, the previous generator configurationis overwritten.

.. method:: GetPermanentSignalGeneratorState(self, channel=1, port, generatorNumber)
           
        This function queries whether the external generator power is
        permanently on.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:GENerator<Gen>:PERManent[:STATe]?
        
        

   :param port: Port numbers of the analyzer.
   :param channel: Channel number.
   :param generatorNumber: This control sets the number of the configuredgenerator. Generators must be numbered in ascending order, startingwith 1. If a number is re-used, the previous generator configurationis overwritten.
   :return: state

.. method:: SetPortPowerGeneratorOffset(self, channel=1, portNumber, generatorNumber, portPowerOffset, offsetParameter)
           
        This function defines the power of an external generator or its power
        offset relative to the channel power.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:GENerator<Gen>:OFFSet <numeric_value>, ONLY |
        CPADd
        
        

   :param offsetParameter: This control sets the offsetparameter.
   :param portPowerOffset: This control sets the port-specific poweroffset.
   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.
   :param generatorNumber: This control sets the numberof the configured generator. Generators must be numbered in ascendingorder, starting with 1. If a number is re-used, the previous generatorconfiguration is overwritten.

.. method:: GetPortPowerGeneratorOffset(self, channel=1, portNumber, generatorNumber)
           
        This function queries the power of an external generator or its power
        offset relative to the channel power.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:GENerator<Gen>:OFFSet?
        
        

   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.
   :param generatorNumber: This control sets the numberof the configured generator. Generators must be numbered in ascendingorder, starting with 1. If a number is re-used, the previous generatorconfiguration is overwritten.
   :return: portPowerOffset
   :return: offsetParameter

.. method:: SetSlope(self, channel=1, port, slope)
           
        This function defines a linear factor to modify the internal source
        power at port <Pt> as a function of the stimulus frequency.
        
        Note(s):
        
        (1) The value can be set for frequency sweeps only.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]:SLOPe <numeric_value>
        
        

   :param slope: This control defines a linear factor to modify the internalsource power at port <Pt> as a function of the stimulus frequency.
   :param port: This control defines the logical port number.
   :param channel: Channel number.

.. method:: GetSlope(self, channel=1, port)
           
        This function returns a linear factor to modify the internal source
        power at port <Pt> as a function of the stimulus frequency.
        
        Note(s):
        
        (1) The value can be set for frequency sweeps only.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]:SLOPe?
        
        

   :param port: This control defines the logical port number.
   :param channel: Channel number.
   :return: slope

.. method:: SetSourceCombinerState(self, channel=1, state)
           
        This function switches the source combiner for reference channel on or
        off.
        
        
        Notes:
        
        (1) This function is available only with hardware option B11.
        
        Remote-control command(s):
        SOURce<Ch>:POWer:COMBiner ON | OFF
        
        

   :param state: This control switches the source combiner forreference channel on or off.
   :param channel: Channel number.

.. method:: GetSourceCombinerState(self, channel=1)
           
        This function returns the source combiner for reference channel.
        
        
        Notes:
        
        (1) This function is available only with hardware option B11.
        
        Remote-control command(s):
        SOURce<Ch>:POWer:COMBiner?
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetFrequencyStimulus(self, channel=1, frequencyStimulus)
           
        This function selects the stimulus signal that is used for the
        definition of the frequency sweep range or CW frequency.
        
        Note(s):
        
        (1) This command is particularly useful in arbitrary mode (with option
        R&S ZVA-K4), where the frequencies and source powers at the ports are
        independent.
        
        (2) For R&S ZVA and ZVT analyzers without option R&S ZVA-K4, all
        powers are coupled so that this selection has no effect.
        
        (3) For R&S ZVB analyzers, all frequencies are coupled so that this
        selection has no effect.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:AXIS:FREQuency '<frequency_ref>'
        
        

   :param frequencyStimulus: This control selects the stimulus signalthat is used for the definition of the frequency sweep range or CWfrequency.
   :param channel: Channel number.

.. method:: GetFrequencyStimulus(self, channel=1, frequencyStimulus)
           
        This function returns the stimulus signal that is used for the
        definition of the frequency sweep range or CW frequency.
        
        Note(s):
        
        (1) This command is particularly useful in arbitrary mode (with option
        R&S ZVA-K4), where the frequencies and source powers at the ports are
        independent.
        
        (2) For R&S ZVA and ZVT analyzers without option R&S ZVA-K4, all
        powers are coupled so that this selection has no effect.
        
        (3) For R&S ZVB analyzers, all frequencies are coupled so that this
        selection has no effect.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:AXIS:FREQuency?
        
        

   :param frequencyStimulus: This control returns the stimulus signalthat is used for the definition of the frequency sweep range or CWfrequency.
   :param channel: Channel number.

.. method:: SetPowerStimulus(self, channel=1, powerStimulus)
           
        This function selects the stimulus signal that is used for the
        definition of the power sweep range or fixed power.
        
        Note(s):
        
        (1) This command is particularly useful in arbitrary mode (with option
        R&S ZVA-K4), where the frequencies and source powers at the ports are
        independent.
        
        (2) For R&S ZVA and ZVT analyzers without option R&S ZVA-K4, all
        powers are coupled so that this selection has no effect.
        
        (3) For R&S ZVB analyzers, all frequencies are coupled so that this
        selection has no effect.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:AXIS:POWer '<power_ref>'
        
        

   :param powerStimulus: This control selects the stimulus signal thatis used for the definition of the power sweep range or fixed power.
   :param channel: Channel number.

.. method:: GetPowerStimulus(self, channel=1, powerStimulus)
           
        This function returns the stimulus signal that is used for the
        definition of the power sweep range or fixed power.
        
        Note(s):
        
        (1) This command is particularly useful in arbitrary mode (with option
        R&S ZVA-K4), where the frequencies and source powers at the ports are
        independent.
        
        (2) For R&S ZVA and ZVT analyzers without option R&S ZVA-K4, all
        powers are coupled so that this selection has no effect.
        
        (3) For R&S ZVB analyzers, all frequencies are coupled so that this
        selection has no effect.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:AXIS:POWer?
        
        

   :param powerStimulus: This control returns the stimulus signal thatis used for the definition of the power sweep range or fixed power.
   :param channel: Channel number.

.. method:: SetTDIFState(self, channel=1, trueDifferentialModeState)
           
        This function switches the true differential mode on or off. This
        command is available only if a suitable balanced port configuration is
        active.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF[:STATe] <Boolean>
        
        

   :param trueDifferentialModeState: This control switches the truedifferential mode on or off.
   :param channel: Channel number.

.. method:: GetTDIFState(self, channel=1)
           
        This function returns the state of the true differential mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF[:STATe]?
        
        

   :param channel: Channel number.
   :return: trueDifferentialModeState

.. method:: SetTDIFAmplitudeImbalanceLogicalPort(self, channel=1, port)
           
        This function selects a logical (balanced) port for the amplitude
        imbalance sweep in true differential mode. A balanced port configuration must be defined and an amplitude imbalance sweep must be
        active to use this function.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:AMPLitude:LPORt <log_port>
        
        

   :param port: This control selects a logical (balanced) port for theamplitude imbalance sweep in true differential mode.
   :param channel: Channel number.

.. method:: GetTDIFAmplitudeImbalanceLogicalPort(self, channel=1)
           
        This function returns a logical (balanced) port for the amplitude
        imbalance sweep in true differential mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:AMPLitude:LPORt?
        
        

   :param channel: Channel number.
   :return: port

.. method:: SetTDIFAmplitudeImbalanceStartPower(self, channel=1, startPower)
           
        This function defines the start power for an amplitude imbalance
        sweep, which is equal to the left edge of a Cartesian diagram. A
        balanced port configuration must be defined and an amplitude imbalance
        sweep must be active to use this function.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:AMPLitude:STARt <start_power>
        
        

   :param startPower: This control defines the start power for anamplitude imbalance sweep, which is equal to the left edge of aCartesian diagram.
   :param channel: Channel number.

.. method:: GetTDIFAmplitudeImbalanceStartPower(self, channel=1)
           
        This function returns the start power for an amplitude imbalance
        sweep, which is equal to the left edge of a Cartesian diagram.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:AMPLitude:STARt?
        
        

   :param channel: Channel number.
   :return: startPower

.. method:: SetTDIFAmplitudeImbalanceStopPower(self, channel=1, stopPower)
           
        This function defines the stop power for an amplitude imbalance sweep,
        which is equal to the right edge of a Cartesian diagram. A balanced
        port configuration must be defined and an amplitude imbalance sweep
        must be active to use this function.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:AMPLitude:STOP <stop_power>
        
        

   :param stopPower: This control defines the stop power for anamplitude imbalance sweep, which is equal to the right edge of aCartesian diagram.
   :param channel: Channel number.

.. method:: GetTDIFAmplitudeImbalanceStopPower(self, channel=1)
           
        This function returns the stop power for an amplitude imbalance sweep,
        which is equal to the right edge of a Cartesian diagram.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:AMPLitude:STOP?
        
        

   :param channel: Channel number.
   :return: stopPower

.. method:: SetTDIFPhaseImbalanceLogicalPort(self, channel=1, port)
           
        This function selects a logical (balanced) port for the phase
        imbalance sweep in true differential mode. A balanced port configuration must be defined and an amplitude imbalance sweep must be
        active to use this function.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:PHASe:LPORt <log_port>
        
        

   :param port: This control selects a logical (balanced) port for thephase imbalance sweep in true differential mode.
   :param channel: Channel number.

.. method:: GetTDIFPhaseImbalanceLogicalPort(self, channel=1)
           
        This function returns a logical (balanced) port for the phase
        imbalance sweep in true differential mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:PHASe:LPORt?
        
        

   :param channel: Channel number.
   :return: port

.. method:: SetTDIFPhaseImbalanceStartPhase(self, channel=1, startPhase)
           
        This function defines the start phase for a phase imbalance sweep,
        which is equal to the left edge of a Cartesian diagram. A balanced
        port configuration must be defined and an amplitude imbalance sweep
        must be active to use this function.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:PHASe:STARt <start_phase>
        
        

   :param startPhase: This control defines the start phase for a phaseimbalance sweep, which is equal to the left edge of a Cartesiandiagram.
   :param channel: Channel number.

.. method:: GetTDIFPhaseImbalanceStartPhase(self, channel=1)
           
        This function returns the start phase for a phase imbalance sweep,
        which is equal to the left edge of a Cartesian diagram.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:PHASe:STARt?
        
        

   :param channel: Channel number.
   :return: startPhase

.. method:: SetTDIFPhaseImbalanceStopPhase(self, channel=1, stopPhase)
           
        This function defines the stop phase for a phase imbalance sweep,
        which is equal to the right edge of a Cartesian diagram. A balanced
        port configuration must be defined and an amplitude imbalance sweep
        must be active to use this function.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:PHASe:STOP <stop_phase>
        
        

   :param stopPhase: This control defines the stop phase for a phaseimbalance sweep, which is equal to the right edge of a Cartesiandiagram.
   :param channel: Channel number.

.. method:: GetTDIFPhaseImbalanceStopPhase(self, channel=1)
           
        This function returns the stop phase for a phase imbalance sweep,
        which is equal to the right edge of a Cartesian diagram.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:IMBalance:PHASe:STOP?
        
        

   :param channel: Channel number.
   :return: stopPhase

.. method:: SetTDIFSourcePowerMode(self, channel=1, sourcePowerMode)
           
        This function qualifies whether the source power
        (SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate][:AMPlitude]) is equal to the
        power of each single-ended wave or to the balanced waves in true
        differential mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6 and ZVT
        instrument.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:WAVes SENDed | DCMode
        
        

   :param sourcePowerMode: This control selects the power of each single-ended wave or the balanced waves in true differential mode.
   :param channel: Channel number.

.. method:: GetTDIFSourcePowerMode(self, channel=1)
           
        This function returns source power mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6 and ZVT
        instrument.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:WAVes?
        
        

   :param channel: Channel number.
   :return: sourcePowerMode

.. method:: SetTDIFCompensationState(self, channel=1, compensationState)
           
        This function selects the calculation method for S-parameters, ratios
        and derived quantities during an amplitude imbalance or phase
        imbalance sweep.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6 and ZVT
        instrument.
        
        Remote-control command(s):
        CALCulate<Ch>:TDIF:IMBalance:COMPensation[:STATe] <Boolean>
        
        

   :param compensationState: This control switches the compensationstate.
   :param channel: Channel number.

.. method:: GetTDIFCompensationState(self, channel=1)
           
        This function returns the calculation method state.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6 and ZVT
        instrument.
        
        Remote-control command(s):
        CALCulate:TDIF:IMBalance:COMPensation[:STATe]?
        
        

   :param channel: Channel number.
   :return: compensationState

.. method:: SetTDIFReceiverFrequency(self, channel=1, receiverFrequency)
           
        This function defines the receiver frequency for true differential
        source adjustment. The setting is relevant in frequency converter mode
        only.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6 and ZVT
        instrument.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:CRFRequency
        
        

   :param receiverFrequency: This control defines the receiver frequencyfor true differential source adjustment. The setting is relevant infrequency converter mode only.
   :param channel: Channel number.

.. method:: GetTDIFReceiverFrequency(self, channel=1)
           
        This function returns the receiver frequency for true differential
        source adjustment.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K6 and ZVT
        instrument.
        
        Remote-control command(s):
        SOURce<Ch>:TDIF:CRFRequency?
        
        

   :param channel: Channel number.
   :return: receiverFrequency

.. method:: SetPulseGeneratorState(self, channel=1, pulseGeneratorState)
           
        This function turns the pulse generator on or off.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>[:STATe]
        
        

   :param pulseGeneratorState: This control turns the pulse generatoron or off.
   :param channel: Channel number.

.. method:: GetPulseGeneratorState(self, channel=1)
           
        This function returns the pulse generator state.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>[:STATe]?
        
        

   :param channel: Channel number.
   :return: pulseGeneratorState

.. method:: DefinePulseGenerator(self, channel=1, generator, pulseType, pulseWidth, singleTrainPulsePeriod, pulsePolarity, pulseMode)
           
        This function defines the properties of the pulse generator signals.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TYPE SINGle | TRAin | CHIGh | CLOW
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:WIDTh
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:PERiod
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:PERiod
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:POLarity NORMal | INVerted
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:MODE CSPecific | CONTinuous
        
        

   :param pulseMode: Selects thechannel-specific or continuous pulse mode.
   :param singleTrainPulsePeriod: Defines thepulse period of the (single) pulse generator signal.
   :param generator: Number of the pulse generator signal.
   :param pulseType: Selects the pulse type of the pulsegenerator signal <gen_no>.
   :param pulsePolarity: Selects the polarityof the pulse generator signal <gen_no>.
   :param pulseWidth: Definesthe pulse width of the pulse generator signal <gen_no>.
   :param channel: Channel number.

.. method:: DefinePulseTrainSegments(self, channel=1, bufferSize, pulseTrainActive, startTime, stopTime)
           
        This function adds and enables/disables an arbitrary number of pulse
        train segments. Each segment consists of a single pulse of definite
        width and position which may be active or inactive.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:DATA <Active>, <Start High>,
        <Stop High>{, <Active>, <Start High>, <Stop High>}
        
        

   :param startTime: Start time of the segment (pulse).
   :param bufferSize: This control sets the buffer size for the controlsPulse Train State, Start High and Stop High.
   :param stopTime: Stop time of the segment (pulse).
   :param pulseTrainActive: Identifier for the stateof the pulse train segment.
   :param channel: Channel number.

.. method:: ConfigureChoppedPulseProfile(self, channel=1, choppedPulseProfileMode, delayIncrement)
           
        This function defines the properties of the chopped pulse profile.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:CPPRofile
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:DINCrement
        
        

   :param delayIncrement: Defines a delay increment for the sync signalin chopped pulse profile mode. The delay increment defines thedistance between two measurement intervals (sweep points). For sweeppoint no. n, the total delay of thhe sync signal relative to the pulsegenerator signal is <Delay> + n * <Increment>.
   :param choppedPulseProfileMode: This control enables or disables thechopped pulse profile mode
   :param channel: Channel number.

.. method:: SetPulseGeneratorType(self, channel=1, generator, pulseType)
           
        This function selects the pulse type of the pulse generator signal
        <gen_no>.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TYPE SINGle | TRAin | CHIGh | CLOW
        
        

   :param pulseType: Selects the pulse type of the pulsegenerator signal <gen_no>.
   :param generator: Number of the pulse generator signal.
   :param channel: Channel number.

.. method:: GetPulseGeneratorType(self, channel=1, generator)
           
        This function returns the pulse type of the pulse generator signal
        <gen_no>.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TYPE?
        
        

   :param generator: Number of the pulse generator signal.
   :param channel: Channel number.
   :return: pulseType

.. method:: SetPulseGeneratorWidth(self, channel=1, generator, pulseWidth)
           
        This function defines the pulse width of the pulse generator signal
        <gen_no>.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:WIDTh
        
        

   :param pulseWidth: Defines the pulse width of thepulse generator signal <gen_no>.
   :param generator: Number of the pulse generator signal.
   :param channel: Channel number.

.. method:: GetPulseGeneratorWidth(self, channel=1, generator)
           
        This function returns the pulse width of the pulse generator signal
        <gen_no>.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:WIDTh?
        
        

   :param generator: Number of the pulse generator signal.
   :param channel: Channel number.
   :return: pulseWidth

.. method:: SetPulseGeneratorSinglePeriod(self, channel=1, singlePulsePeriod)
           
        This function defines the pulse period of the single pulse generator
        signal.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:PERiod
        
        

   :param singlePulsePeriod: Defines the pulse period of the (single)pulse generator signal.
   :param channel: Channel number.

.. method:: GetPulseGeneratorSinglePeriod(self, channel=1)
           
        This function returns the pulse period of the single pulse generator
        signal.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:PERiod?
        
        

   :param channel: Channel number.
   :return: singlePulsePeriod

.. method:: SetPulseGeneratorTrainPeriod(self, channel=1, trainPulsePeriod)
           
        This function defines the pulse period of the (single) pulse generator
        signal.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:PERiod
        
        

   :param trainPulsePeriod: Defines the pulse period of the (single)pulse generator signal.
   :param channel: Channel number.

.. method:: GetPulseGeneratorTrainPeriod(self, channel=1)
           
        This function returns the pulse period of the (single) pulse generator
        signal.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:PERiod?
        
        

   :param channel: Channel number.
   :return: trainPulsePeriod

.. method:: SetPulseGeneratorPolarity(self, channel=1, generator, pulsePolarity)
           
        This function selects the polarity of the pulse generator signal
        <gen_no>.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:POLarity NORMal | INVerted
        
        

   :param pulsePolarity: Selects the polarity of thepulse generator signal <gen_no>.
   :param generator: Number of the pulse generator signal.
   :param channel: Channel number.

.. method:: GetPulseGeneratorPolarity(self, channel=1, generator)
           
        This function returns the polarity of the pulse generator signal
        <gen_no>.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:POLarity?
        
        

   :param generator: Number of the pulse generator signal.
   :param channel: Channel number.
   :return: pulsePolarity

.. method:: SetPulseGeneratorMode(self, channel=1, pulseMode)
           
        This function selects the channel-specific or continuous pulse mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:MODE CSPecific | CONTinuous
        
        

   :param pulseMode: Selects the channel-specific or continuous pulsemode.
   :param channel: Channel number.

.. method:: GetPulseGeneratorMode(self, channel=1)
           
        This function returns the channel-specific or continuous pulse mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:MODE?
        
        

   :param channel: Channel number.
   :return: pulseMode

.. method:: SetPulseGeneratorMasterChannel(self, masterChannel)
           
        This function selects the master channel for CONTinuous pulse mode
        (rszvb_SetPulseGeneratorMode).
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:MCHannel
        
        

   :param masterChannel: This control sets the masterchannel. The settings of the master channel are used for all channels.Channel-specific pulse generator settings for other channels are notoverwritten. If Mode is changed to CSP they are used again.

.. method:: GetPulseGeneratorMasterChannel(self, )
           
        This function returns the master channel for CONTinuous pulse mode
        (rszvb_SetPulseGeneratorMode).
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:MCHannel?
        
        

   :return: masterChannel

.. method:: GetPulseTrainSegments(self, channel=1, bufferSize, pulseTrainActive, startTime, stopTime)
           
        This function returns the pulse train segments. Each segment consists
        of a single pulse of definite width and position which may be active
        or inactive.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:DATA?
        
        

   :param startTime: Returns the Start times of the segment (pulse).
   :param bufferSize: This control sets the buffer size for the controlsPulse Train State, Start High and Stop High.
   :param stopTime: Returns the Stop times of the segment (pulse).
   :param pulseTrainActive: Returns the states of thepulse train segments.
   :param channel: Channel number.

.. method:: SetPulseTrainSegmentState(self, channel=1, segment, segmentState)
           
        This function set the pulse train segment no. <Seg> active or inactive
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:SEGMent<Seg>[:STATe]
        
        

   :param segmentState: This control set the pulse train segment no.<Seg> active or inactive.
   :param segment: Segment number.
   :param channel: Channel number.

.. method:: GetPulseTrainSegmentState(self, channel=1, segment)
           
        This function returns the state of the pulse train segment.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:SEGMent<Seg>[:STATe]?
        
        

   :param segment: Segment number.
   :param channel: Channel number.
   :return: segmentState

.. method:: SetPulseTrainSegmentStart(self, channel=1, segment, segmentStart)
           
        This function changes the start time of a pulse train segment. A range
        must be created first to enable this function
        (rszvb_DefinePulseTrainSegments).
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:SEGMent<Seg>:STARt
        
        

   :param segment: Segment number.
   :param segmentStart: This control changes the start time of a pulsetrain segment.
   :param channel: Channel number.

.. method:: GetPulseTrainSegmentStart(self, channel=1, segment)
           
        This function returns the start time of a pulse train segment.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:SEGMent<Seg>:STARt?
        
        

   :param segment: Segment number.
   :param channel: Channel number.
   :return: segmentStart

.. method:: SetPulseTrainSegmentStop(self, channel=1, segment, segmentStop)
           
        This function changes the stop time of a pulse train segment. A range
        must be created first to enable this function
        (rszvb_DefinePulseTrainSegments).
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:SEGMent<Seg>:STOP
        
        

   :param segmentStop: This control changes the stop time of a pulsetrain segment.
   :param segment: Segment number.
   :param channel: Channel number.

.. method:: GetPulseTrainSegmentStop(self, channel=1, segment)
           
        This function returns the stop time of a pulse train segment.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:SEGMent<Seg>:STOP?
        
        

   :param segment: Segment number.
   :param channel: Channel number.
   :return: segmentStop

.. method:: GetPulseTrainSegmentCount(self, channel=1)
           
        This function queries the number of pulse train segments.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:SEGMent<Seg>:COUNt?
        
        

   :param channel: Channel number.
   :return: segmentCount

.. method:: DeleteAllPulseTrainSegments(self, channel=1)
           
        This function deletes all pulse train segments..
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:TRAin:DELete:ALL
        
        

   :param channel: Channel number.

.. method:: SavePulseTrainFile(self, channel=1, generator, fileName)
           
        This function saves a pulse train definition associated with a
        specified channel to a pulse train file.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        MMEMory:STORe:PTRain <Channel>, <Generator>, '<file_name>'
        
        

   :param generator: Generator number.
   :param channel: Channel number.
   :param fileName: String parameter to specify the name and directory of thecreated pulse train file. The default extension (manual control) forpulse train files is *.train, although other extensions are allowed.If no path is specified the analyzer uses the current directory

.. method:: LoadPulseTrainFile(self, channel=1, generator, fileName)
           
        This function loads a pulse train definition from a specified file and
        assigns it to a channel with a specified number.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        MMEMory:LOAD:PTRain <Channel>, <Generator>, '<file_name>'
        
        

   :param generator: Generator number.
   :param channel: Channel number.
   :param fileName: String parameter to specify the name and directory of thepulse train file to be loaded. The default extension (manual control)for pulse train files is *.train, although other extensions areallowed. If no path is specified the analyzer searches the currentdirectory.

.. method:: SetPulseGeneratorDelay(self, channel=1, delay)
           
        This function defines the delay of the sync signal relative to the
        pulse generator signal.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:DELay
        
        

   :param delay: Defines the delay of the sync signal relative to thepulse generator signal.
   :param channel: Channel number.

.. method:: GetPulseGeneratorDelay(self, channel=1)
           
        This function returns the delay of the sync signal relative to the
        pulse generator signal.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:DELay?
        
        

   :param channel: Channel number.
   :return: delay

.. method:: SetChoppedPulseProfileMode(self, channel=1, choppedPulseProfileMode)
           
        This function enables or disables the chopped pulse profile mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:CPPRofile
        
        

   :param choppedPulseProfileMode: This control enables or disables thechopped pulse profile mode
   :param channel: Channel number.

.. method:: GetChoppedPulseProfileMode(self, channel=1)
           
        This function returns the state of the chopped pulse profile mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:CPPRofile?
        
        

   :param channel: Channel number.
   :return: choppedPulseProfileMode

.. method:: SetChoppedPulseProfileDelayIncrement(self, channel=1, delayIncrement)
           
        This function defines a delay increment for the sync signal in chopped
        pulse profile mode. The delay increment defines the distance between
        two measurement intervals (sweep points). For sweep point no. n, the
        total delay of thhe sync signal relative to the pulse generator signal
        is <Delay> + n * <Increment>.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:DINCrement
        
        

   :param delayIncrement: Defines a delay increment for the sync signalin chopped pulse profile mode.
   :param channel: Channel number.

.. method:: GetChoppedPulseProfileDelayIncrement(self, channel=1)
           
        This function returns a delay increment for the sync signal in chopped
        pulse profile mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVA-K27.
        
        Remote-control command(s):
        [SENSe<Ch>:]PULSe:GENerator<gen_no>:DINCrement?
        
        

   :param channel: Channel number.
   :return: delayIncrement

.. method:: ConfigureZVAXPath(self, channel=1, path, internalCombiner, harmonicFilter, pulseModulator)
           
        This function configures the different signal paths in the Extension
        Unit R&S ZVAX24.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:COMBiner[:STATe]
        [SENSe<Ch>:]EUNit:HFILter<Path>[:STATe]
        [SENSe<Ch>:]EUNit:PMODulator<Path>[:STATe]
        
        

   :param pulseModulator: This control loops pulse modulators into theRF signal paths no. <Path>. Paths no. 1 and 3 in the extension unitare source paths, path no. 2 is a receiver path.
   :param path: Signal path number.
   :param internalCombiner: This control switchesthe internal combiner in-between the RF signal paths no. 1 and 3(source path).
   :param harmonicFilter: This control loops harmonicfilters into the RF signal paths no. <Path>. Paths no. 1 and 3 in theextension unit are source paths, path no. 2 is a receiver path.
   :param channel: Channel number.

.. method:: ConfigurePulseGenerators(self, channel=1, extSignalGeneratorInput, extSignalGeneratorOutput, assignment)
           
        This function defines the source and the output of the pulse generator
        signals and assigns pulse generator signals to the pulse modulators of
        the Extension Unit R&S ZVAXxx.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:PGENerator:INPut:EXTernal
        [SENSe<Ch>:]EUNit:PGENerator:ASSignment G1Mall | G2Mall | G1M2 | G1M3
        [SENSe<Ch>:]EUNit:PGENerator:OUTPut:EXTernal
        
        

   :param assignment: This control defines the assignment between pulse generator signalsand pulse modulators.
   :param extSignalGeneratorInput: This control selects the R&S ZVA oran external pulse generator as a source for the pulse generatorsignals.
   :param channel: Channel number.
   :param extSignalGeneratorOutput: This control routes either the R&SZVA pulse generator signals or the external pulse generator signals tothe PULSE GENERATOR OUT connector.

.. method:: SetInternalCombiner(self, channel=1, internalCombiner)
           
        This function switches the internal combiner in-between the RF signal
        paths no. 1 and 3 (source path).
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:COMBiner[:STATe]
        
        

   :param internalCombiner: This control switches the internal combinerin-between the RF signal paths no. 1 and 3 (source path).
   :param channel: Channel number.

.. method:: GetInternalCombiner(self, channel=1)
           
        This function returns the internal combiner in-between the RF signal
        paths no. 1 and 3 (source path).
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:COMBiner[:STATe]?
        
        

   :param channel: Channel number.
   :return: internalCombiner

.. method:: SetHarmonicFilter(self, channel=1, path, harmonicFilter)
           
        This function loops harmonic filters into the RF signal paths no.
        <Path>. Paths no. 1 and 3 in the extension unit are source paths, path no. 2 is a receiver path.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:HFILter<Path>[:STATe]
        
        

   :param path: Signal path number.
   :param harmonicFilter: This control loopsharmonic filters into the RF signal paths no. <Path>. Paths no. 1 and3 in the extension unit are source paths, path no. 2 is a receiverpath.
   :param channel: Channel number.

.. method:: GetHarmonicFilter(self, channel=1, path)
           
        This function returns the state of the harmonic filters.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:HFILter<Path>[:STATe]?
        
        

   :param path: Signal path number.
   :param channel: Channel number.
   :return: harmonicFilter

.. method:: SetLNPreamplifier(self, channel=1, state)
           
        This function loops the low noise preamplifier into the RF receiver
        path no. 2.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:LNAMplifier[:STATe]
        
        

   :param state: This control loops the low noise preamplifier into theRF receiver path no. 2.
   :param channel: Channel number.

.. method:: GetLNPreamplifier(self, channel=1)
           
        This function returns the state of the low noise preamplifier.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:LNAMplifier[:STATe]?
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetPulseModulator(self, channel=1, path, pulseModulator)
           
        This function loops pulse modulators into the RF signal paths no.
        <Path>. Paths no. 1 and 3 in the extension unit are source paths, path no. 2 is a receiver path.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:PMODulator<Path>[:STATe]
        
        

   :param pulseModulator: This control loopspulse modulators into the RF signal paths no. <Path>. Paths no. 1 and3 in the extension unit are source paths, path no. 2 is a receiverpath.
   :param path: Signal path number.
   :param channel: Channel number.

.. method:: GetPulseModulator(self, channel=1, path)
           
        This function returns the state of the pulse modulators.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:PMODulator<Path>[:STATe]?
        
        

   :param path: Signal path number.
   :param channel: Channel number.
   :return: pulseModulator

.. method:: SetExternalSignalGeneratorInput(self, channel=1, extSignalGeneratorInput)
           
        This function selects the R&S ZVA or an external pulse generator as a
        source for the pulse generator signals.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:PGENerator:INPut:EXTernal
        
        

   :param extSignalGeneratorInput: This control selects the R&S ZVA oran external pulse generator as a source for the pulse generatorsignals.
   :param channel: Channel number.

.. method:: GetExternalSignalGeneratorInput(self, channel=1)
           
        This function returns the R&S ZVA or an external pulse generator as a
        source for the pulse generator signals.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:PGENerator:INPut:EXTernal?
        
        

   :param channel: Channel number.
   :return: extSignalGeneratorInput

.. method:: SetPulseGeneratorAssignment(self, channel=1, assignment)
           
        This function defines the assignment between pulse generator signals
        and pulse modulators.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:PGENerator:ASSignment G1Mall | G2Mall | G1M2 | G1M3
        
        

   :param assignment: This control defines the assignment between pulsegenerator signals and pulse modulators.
   :param channel: Channel number.

.. method:: GetPulseGeneratorAssignment(self, channel=1)
           
        This function returns the assignment between pulse generator signals
        and pulse modulators.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:PGENerator:ASSignment?
        
        

   :param channel: Channel number.
   :return: assignment

.. method:: SetExternalSignalGeneratorOutput(self, channel=1, extSignalGeneratorOutput)
           
        This function routes either the R&S ZVA pulse generator signals or the
        external pulse generator signals to the PULSE GENERATOR OUT connector.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:PGENerator:OUTPut:EXTernal
        
        

   :param channel: Channel number.
   :param extSignalGeneratorOutput: This control routes either the R&SZVA pulse generator signals or the external pulse generator signals tothe PULSE GENERATOR OUT connector.

.. method:: GetExternalSignalGeneratorOutput(self, channel=1)
           
        This function returns either the R&S ZVA pulse generator signals or
        the external pulse generator signals to the PULSE GENERATOR OUT
        connector.
        
        Remote-control command(s):
        [SENSe<Ch>:]EUNit:PGENerator:OUTPut:EXTernal?
        
        

   :param channel: Channel number.
   :return: extSignalGeneratorOutput

.. method:: SetTRMMeasureInput(self, channel=1, path, input)
           
        This function selects the input for the a-wave (REF) receiver at paths
        no. 1-4.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:AMONitor<Path>
        
        

   :param path: Signal path.
   :param channel: Channel number.
   :param input: Selects the input for the a-wave (REF) receiver at pathsno. 1-4.

.. method:: GetTRMMeasureInput(self, channel=1, path)
           
        This function returns the input for the a-wave (REF) receiver at paths
        no. 1-4.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:AMONitor<Path>?
        
        

   :param path: Signal path.
   :param channel: Channel number.
   :return: input

.. method:: SetTRMCombinerState(self, channel=1, path, combinerState)
           
        This function switches the internal combiner in-between RF signal
        paths 1 and 3 or 2 and 4 (source path).
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:COMBiner<Path>[:STATe]
        
        

   :param path: Signal path.
   :param combinerState: Switches the internal combiner in-between RFsignal paths 1 and 3 or 2 and 4 (source path).
   :param channel: Channel number.

.. method:: GetTRMCombinerState(self, channel=1, path)
           
        This function returns the state of the internal combiner in-between RF
        signal paths 1 and 3 or 2 and 4 (source path).
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:COMBiner<Path>[:STATe]?
        
        

   :param path: Signal path.
   :param channel: Channel number.
   :return: combinerState

.. method:: SetTRMPowerAmplifierState(self, channel=1, path, powerAmplifierState)
           
        This function loops an internal power amplifier into one of the RF
        signal paths (source paths).
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:PAMPlifier<Path>[:STATe]
        
        

   :param path: Signal path.
   :param powerAmplifierState: Loops an internal power amplifier intoone of the RF signal paths (source paths).
   :param channel: Channel number.

.. method:: GetTRMPowerAmplifierState(self, channel=1, path)
           
        This function returns the state of the internal power amplifier.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:PAMPlifier<Path>[:STATe]?
        
        

   :param path: Signal path.
   :param channel: Channel number.
   :return: powerAmplifierState

.. method:: SetTRMPulseModulatorState(self, channel=1, path, pulseModulatorState)
           
        This function loops a pulse modulator into the RF signal path no.
        <Path>.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:PMODulator<Path>[:STATe]
        
        

   :param path: Signal path.
   :param pulseModulatorState: Loops a pulse modulator into the RFsignal path no. <Path>.
   :param channel: Channel number.

.. method:: GetTRMPulseModulatorState(self, channel=1, path)
           
        This function returns the state of the a pulse modulator.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:PMODulator<Path>[:STATe]?
        
        

   :param path: Signal path.
   :param channel: Channel number.
   :return: pulseModulatorState

.. method:: SetTRMUserSourcePathExtensionState(self, channel=1, path, userSourcePathExtension)
           
        This function enables/disables the user source path extension for RF
        signal path <Path>.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:USOurce<Path>[:STATe]
        
        

   :param path: Signal path.
   :param channel: Channel number.
   :param userSourcePathExtension: Enables/disables the user sourcepath extension for RF signal path <Path>.

.. method:: GetTRMUserSourcePathExtensionState(self, channel=1, path)
           
        This function returns the state of the user source path extension for
        RF signal path <Path>.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:USOurce<Path>[:STATe]?
        
        

   :param path: Signal path.
   :param channel: Channel number.
   :return: userSourcePathExtension

.. method:: SetTRMUserMeasurementPathExtensionState(self, channel=1, path, userMeasurementPathExtension)
           
        This function enables/disables the user measurement path extension for
        RF signal path <Path>.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:UMEas<Path>[:STATe]
        
        

   :param path: Signal path.
   :param userMeasurementPathExtension: Enables/disables the usermeasurement path extension for RF signal path <Path>.
   :param channel: Channel number.

.. method:: GetTRMUserMeasurementPathExtensionState(self, channel=1, path)
           
        This function returns the state of the user measurement path extension
        for RF signal path <Path>.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:UMEas<Path>[:STATe]?
        
        

   :param path: Signal path.
   :param channel: Channel number.
   :return: userMeasurementPathExtension

.. method:: SetTRMPulseModulatorSource(self, channel=1, path, pulseModulatorSource)
           
        This function selects the source (i.e. the pulse generator) for the
        pulse modulator at RF path <Path>.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:PMODulator<Path>:SOURce
        
        

   :param path: Signal path.
   :param channel: Channel number.
   :param pulseModulatorSource: Selects the source (i.e. the pulsegenerator) for the pulse modulator at RF path <Path>.

.. method:: GetTRMPulseModulatorSource(self, channel=1, path)
           
        This function returns the source (i.e. the pulse generator) for the
        pulse modulator at RF path <Path>.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:PMODulator<Path>:SOURce?
        
        

   :param path: Signal path.
   :param channel: Channel number.
   :return: pulseModulatorSource

.. method:: SetTRMPulseGeneratorSource(self, channel=1, extOut, pulseGeneratorSource)
           
        This function defines the source signal for pulse generator output
        <No> of the R&S ZVAX-TRM.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:REAR<No>:SOURce
        
        

   :param extOut: External out.
   :param pulseGeneratorSource: Defines the source signal for pulsegenerator output <No> of the R&S ZVAX-TRM.
   :param channel: Channel number.

.. method:: GetTRMPulseGeneratorSource(self, channel=1, extOut)
           
        This function returns the source signal for pulse generator output
        <No> of the R&S ZVAX-TRM.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:REAR<No>:SOURce?
        
        

   :param extOut: External out.
   :param channel: Channel number.
   :return: pulseGeneratorSource

.. method:: SetTRMPulseGeneratorInvertSource(self, channel=1, extOut, invertSource)
           
        This function defines whether the signal at the pulse generator output
        no. <No> shall be inverted.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:REAR<No>:INVert
        
        

   :param extOut: External out.
   :param channel: Channel number.
   :param invertSource: Defines whether the signal at the pulsegenerator output no. <No> shall be inverted.

.. method:: GetTRMPulseGeneratorInvertSource(self, channel=1, extOut)
           
        This function returns whether the signal at the pulse generator output
        no. <No> shall be inverted.
        
        Remote-control command(s):
        [SENSe<Ch>:]TEUNit:REAR<No>:INVert?
        
        

   :param extOut: External out.
   :param channel: Channel number.
   :return: invertSource

.. method:: GetTRMNumberOfUnits(self, )
           
        This function queries the number of connected extension units R&S
        ZVAX-TRM.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:TEUNit:COUNt?
        
        

   :return: numberOfUnits

.. method:: GetTRMUnitDeviceID(self, bufferSize, deviceID)
           
        This function queries the device ID of a connected extension unit R&S
        ZVAX-TRM.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:TEUNit:IDN?
        
        

   :param bufferSize: This control sets the buffersize for the control Device ID.
   :param deviceID: Returns the manufacturer, type ofthe extension unit, 10-digit order number, serial number.

.. method:: GetTRMUnitHardwareOptions(self, bufferSize, optionList)
           
        This function queries the hardware options of a detected extension
        unit R&S ZVAX-TRM.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:TEUNit:OPT?
        
        

   :param bufferSize: This control sets the buffersize for the control Option List.
   :param optionList: Returns a comma-separated list ofoptions.

.. method:: ConfigureHarmonicMeasurement(self, channel=1, harmonicMeasurement, relativeHarmonicMeasurement, source, harmonicMeasuredAt, harmonicOrder)
           
        This function configures the harmonic measurement on selected channel.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion FUNDamental | HARMonic
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:ORDer
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:SPORt
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:RPORt
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:RELative ON | OFF
        
        

   :param relativeHarmonicMeasurement: This control enables or disables the relative harmonicmeasurement where the harmonic is divided by the fundamental wave.
   :param harmonicOrder: This control defines the orderof the harmonic, integer multiple of the fundamental frequencymeasured.
   :param harmonicMeasuredAt: This control defines thereceive port number.
   :param source: This control defines the source port number.
   :param harmonicMeasurement: This control enables the measurement of aharmonic or the fundamental signal for selected channel.
   :param channel: Channel number.

.. method:: SetHarmonicMeasurementState(self, channel=1, harmonicMeasurement)
           
        This function enables the measurement of a harmonic or the fundamental
        signal for selected channel.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion FUNDamental | HARMonic
        
        

   :param harmonicMeasurement: This control enables the measurement of aharmonic or the fundamental signal for selected channel.
   :param channel: Channel number.

.. method:: GetHarmonicMeasurementState(self, channel=1)
           
        This function queries the state of the measurement of a harmonic or
        the fundamental signal for selected channel.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion?
        
        

   :param channel: Channel number.
   :return: harmonicMeasurement

.. method:: SetHarmonicOrder(self, channel=1, harmonicOrder)
           
        This function selects the order of the harmonic measured if a harmonic
        measurement is enabled.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:ORDer
        
        

   :param harmonicOrder: This control defines the order of the harmonic,integer multiple of the fundamental frequency measured.
   :param channel: Channel number.

.. method:: GetHarmonicOrder(self, channel=1)
           
        This function queries the order of the harmonic measured if a harmonic
        measurement is enabled.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:ORDer?
        
        

   :param channel: Channel number.
   :return: harmonicOrder

.. method:: SetHarmonicSourcePort(self, channel=1, port)
           
        This function selects the source port for the harmonic measurement.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:SPORt
        
        

   :param port: This control defines the source port number.
   :param channel: Channel number.

.. method:: GetHarmonicSourcePort(self, channel=1)
           
        This function queries the source port for the harmonic measurement.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:SPORt
        
        

   :param channel: Channel number.
   :return: port

.. method:: SetHarmonicReceivePort(self, channel=1, port)
           
        This function selects the receive port for the harmonic measurement.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:RPORt
        
        

   :param port: This control defines the receive port number.
   :param channel: Channel number.

.. method:: GetHarmonicReceivePort(self, channel=1)
           
        This function queries the receive port for the harmonic measurement.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:RPORt?
        
        

   :param channel: Channel number.
   :return: port

.. method:: SetHarmonicRelativeState(self, channel=1, relativeHarmonicMeasurement)
           
        This function enables or disables the relative harmonic measurement
        where the harmonic is divided by the fundamental wave.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:RELative ON | OFF
        
        

   :param relativeHarmonicMeasurement: This control enables or disablesthe relative harmonic measurement where the harmonic is divided by thefundamental wave.
   :param channel: Channel number.

.. method:: GetHarmonicRelativeState(self, channel=1)
           
        This function queries the relative harmonic measurement state.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:HARMonic:RELative?
        
        

   :param channel: Channel number.
   :return: relativeHarmonicMeasurement

.. method:: SetMixerMode(self, channel=1, mixerMode)
           
        This function toggle between the (frequency-converting) mixer mode and
        normal operation, where the analyzer measures the unconverted
        fundamental wave.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion MIXer | FUNDamental
        
        

   :param mixerMode: This control toggle between the (frequency-converting) mixer mode and normal operation, where the analyzermeasures the unconverted fundamental wave.
   :param channel: Channel number.

.. method:: GetMixerMode(self, channel=1)
           
        This function returns the (frequency-converting) mixer mode or normal
        operation, where the analyzer measures the unconverted fundamental
        wave.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion?
        
        

   :param channel: Channel number.
   :return: mixerMode

.. method:: SetNumberOfStages(self, channel=1, numberOfStages)
           
        Selects the number of converter/mixer stages for scalar mixer
        measurements and intermodulation distortion measurements.
        
        Notes:
        
        For mixer delay measurements and vector mixer measurements (options
        R&S ZVA-K5, R&S ZVAK9, R&S ZVA-K10), a single mixer stage is supported
        only.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:STAGes <mixers>
        
        

   :param channel: Channel number.
   :param numberOfStages: This control sets the number of converter/mixerstages.

.. method:: GetNumberOfStages(self, channel=1)
           
        This function returns an external generator as a signal source for the
        LO signal (external source).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:LOEXternal?
        
        

   :param channel: Channel number.
   :return: numberOfStages

.. method:: SetSignalSource(self, channel=1, stage, source, portNumber)
           
        This function selects an analyzer or an external generator port as a
        signal source for the LO 1 or L0 2 signal.
        
        Notes:
        
        (1) For mixer delay measurements and vector mixer measurements
        (options R&S ZVA-K5, R&S ZVAK9, R&S ZVA-K10), ports 1 and 2 are
        reserved for the RF and IF signals, respectively. Only a
        single mixer stage (<Stg> = 1) is supported.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:LOPort<Stg> NONE | EMBedded |
        PORT, <port_number> | GENerator, <gen_number>
        
        

   :param source: LO 1 or L0 2 signal source.
   :param portNumber: This control sets port number of an analyzer orexternal generator signal source.
   :param channel: Channel number.
   :param stage: Stage number, switches between LO 1 and LO 2 signal .

.. method:: GetSignalSource(self, channel=1, stage)
           
        This function returns an analyzer or an external generator port as a
        signal source for the LO 1 or L0 2 signal.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:LOPort<Stg>?
        
        

   :param channel: Channel number.
   :param stage: Stage number, switches between LO 1 and LO 2 signal .
   :return: source
   :return: portNumber

.. method:: SetIFSignalPort(self, channel=1, portNumber)
           
        This function selects an analyzer port as receive port for the IF
        signal.
        
        Notes:
        
        (1) For mixer delay measurements and vector mixer measurements
        (options R&S ZVA-K5, R&S ZVA-K9, R&S ZVA-K10), the IF signal must be
        measured at port 2.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:IFPort <port_number>
        
        

   :param portNumber: Analyzer port number (physical port).
   :param channel: Channel number.

.. method:: GetIFSignalPort(self, channel=1)
           
        This function returns an analyzer port as receive port for the IF
        signal.
        
        Notes:
        
        (1) For mixer delay measurements and vector mixer measurements
        (options R&S ZVA-K5, R&S ZVA-K9, R&S ZVA-K10), the IF signal must be
        measured at port 2.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:IFPort <port_number>
        
        

   :param channel: Channel number.
   :return: portNumber

.. method:: SetRFSignalPort(self, channel=1, portNumber)
           
        This function selects an analyzer port as receive port for the RF
        signal.
        
        Notes:
        
        (1) For mixer delay measurements and vector mixer measurements
        (options R&S ZVA-K5, R&S ZVA-K9, R&S ZVA-K10), the IF signal must be
        measured at port 1.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:RFPort <port_number>
        
        

   :param portNumber: Analyzer port number (physical port).
   :param channel: Channel number.

.. method:: GetRFSignalPort(self, channel=1)
           
        This function returns an analyzer port as receive port for the RF
        signal.
        
        Notes:
        
        (1) For mixer delay measurements and vector mixer measurements
        (options R&S ZVA-K5, R&S ZVA-K9, R&S ZVA-K10), the IF signal must be
        measured at port 1.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:RFPort <port_number>
        
        

   :param channel: Channel number.
   :return: portNumber

.. method:: SetInternalSignalSource(self, channel=1, internalSignalSource)
           
        This function sets an analyzer port as a signal source for the LO
        signal (internal source).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:LOINternal NONE | <port_number>
        
        

   :param internalSignalSource: This control sets an analyzer port as asignal source for the LO signal (internal source).
   :param channel: Channel number.

.. method:: GetInternalSignalSource(self, channel=1)
           
        This function returns an analyzer port as a signal source for the LO
        signal (internal source).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:LOINternal?
        
        

   :param channel: Channel number.
   :return: internalSignalSource

.. method:: SetExternalSignalSource(self, channel=1, externalSignalSource)
           
        This function sets an external generator as a signal source for the LO
        signal (external source).
        
        Notes:
        
        (1) Generators must be configured explicitly in the System - System
        Config - Configure External Generators function.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:LOEXternal NONE | <port_number>
        
        

   :param externalSignalSource: This control sets an external generatoras a signal source for the LO signal (external source).
   :param channel: Channel number.

.. method:: GetExternalSignalSource(self, channel=1)
           
        This function returns an external generator as a signal source for the
        LO signal (external source).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:LOEXternal?
        
        

   :param channel: Channel number.
   :return: externalSignalSource

.. method:: ConfigurePowerSettings(self, channel=1, fundamentalPower, fixedPower)
           
        This function configures the power settings for the mixer measurement.
        
        Remote-control command(s):
        SOURce<Ch>:]FREQuency:CONVersion:MIXer:FUNDamental RF | LO
        SOURce<Ch>:FREQuency:CONVersion:MIXer:PFIXed <fixed_power>
        
        

   :param fundamentalPower: This control selects the mixer input signalwhich is at the fundamental power.
   :param fixedPower: Thiscontrol defines a fixed power, to be assigned either to the RF or tothe LO signal.
   :param channel: Channel number.

.. method:: SetFundamentalPowerSignal(self, channel=1, fundamentalPower)
           
        This function selects the mixer input signal which is at the
        fundamental power.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency:CONVersion:MIXer:FUNDamental RF | LO
        
        

   :param fundamentalPower: This control selects the mixer input signalwhich is at the fundamental power.
   :param channel: Channel number.

.. method:: GetFundamentalPowerSignal(self, channel=1)
           
        This function returns the mixer input signal which is at the
        fundamental power.
        
        Remote-control command(s):
        SOURce<Ch>:]FREQuency:CONVersion:MIXer:FUNDamental?
        
        

   :param channel: Channel number.
   :return: fundamentalPower

.. method:: SetFixedPower(self, channel=1, fixedPower)
           
        This function defines a fixed power, to be assigned either to the RF
        or to the LO signal.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency:CONVersion:MIXer:PFIXed <fixed_power>
        
        

   :param fixedPower: This control defines a fixed power, to be assignedeither to the RF or to the LO signal.
   :param channel: Channel number.

.. method:: GetFixedPower(self, channel=1)
           
        This function returns a fixed power, assigned either to the RF or to
        the LO signal.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency:CONVersion:MIXer:PFIXed?
        
        

   :param channel: Channel number.
   :return: fixedPower

.. method:: SetFixedPowerToSignal(self, channel=1, signal, fixedPower)
           
        This function assigns a fixed power to the RF, LO 1, LO 2, Aux LO, or
        to the IF signal.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency<Pt>:CONVersion:MIXer:PMFixed RF | LO | LO1 | LO2
        | AUXLo | IF, <fixed_power>
        
        

   :param signal: This control selects the mixer input or output signal.
   :param fixedPower: Thiscontrol defines a fixed power, to be assigned either to the RF, LO 1,LO 2, Aux LO, or to the IF signal.
   :param channel: Channel number.

.. method:: GetFixedPowerToSignal(self, channel=1, signal)
           
        This function queries a fixed power for the RF, LO 1, LO 2, Aux LO, or
        to the IF signal.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency<Pt>:CONVersion:MIXer:PMFixed? RF | LO | LO1 | LO2
        | AUXLo | IF
        
        

   :param signal: This control selects the mixer input or output signal.
   :param channel: Channel number.
   :return: fixedPower

.. method:: SetSignalPowerMode(self, channel=1, signal, mode)
           
        This function sets the RF, LO 1, LO 2, Aux LO, or the IF signal ports
        to fixed power or to the channel base power.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency<Pt>:CONVersion:MIXer:PMODe RF | LO | LO1 | LO2 |
        AUXLo | IF, FIXed | FUNDamental
        
        

   :param signal: This control selects the mixer input or output signal.
   :param mode: Selectsfixed power or base power (fundamental).
   :param channel: Channel number.

.. method:: GetSignalPowerMode(self, channel=1, signal)
           
        This function queries if the RF, LO 1, LO 2, Aux LO, or the IF signal ports are set to fixed power or to the channel base power.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency<Pt>:CONVersion:MIXer:PMODe? RF | LO | LO1 | LO2 |
        AUXLo | IF
        
        

   :param signal: This control selects the mixer input or output signal.
   :param channel: Channel number.
   :return: mode

.. method:: ConfigureFrequencySettings(self, channel=1, fundamentalFrequencySignal, fixedFrequencySignal, fixedFrequency, frequencyConversionMode)
           
        This function configures the frequency settings for the mixer
        measurement.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FUNDamental RF | LO | IF
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FIXed RF | LO | IF
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FFIXed <fixed_frequency>
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:TFRequency DCLower | DCUPper |
        UCONversion
        
        

   :param frequencyConversionMode: Thiscontrol selects the frequency conversion mode of the IF signal.
   :param fixedFrequency: This control defines a fixed frequency, to be assigned either to theRF, the LO, or the IF signal.
   :param fixedFrequencySignal: This control selects the mixer input or output signal which isat the fixed frequency.
   :param channel: Channel number.
   :param fundamentalFrequencySignal: This control selects the mixerinput or output signal which is at the fundamental frequency .

.. method:: SetFundamentalFrequencySignal(self, channel=1, fundamentalFrequency)
           
        This function selects the mixer input or output signal which is at the
        fundamental frequency.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FUNDamental RF | IF | LO1 | LO2
        
        

   :param fundamentalFrequency: This control selects the mixer input oroutput signal which is at the fundamental frequency.
   :param channel: Channel number.

.. method:: GetFundamentalFrequencySignal(self, channel=1)
           
        This function returns the mixer input or output signal which is at the
        fundamental frequency .
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FUNDamental?
        
        

   :param channel: Channel number.
   :return: fundamentalFrequency

.. method:: SetFixedFrequencySignal(self, channel=1, fixedFrequency)
           
        This function selects the mixer input or output signal which is at the
        fixed frequency.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FIXed RF | LO | IF
        
        

   :param fixedFrequency: This control selects the mixer input or outputsignal which is at the fixed frequency.
   :param channel: Channel number.

.. method:: GetFixedFrequencySignal(self, channel=1)
           
        This function returns the mixer input or output signal which is at the
        fixed frequency.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FIXed?
        
        

   :param channel: Channel number.
   :return: fixedFrequency

.. method:: SetFixedFrequencySignalStage2(self, channel=1, fixedFrequency)
           
        This function selects the mixer input or output signal which is at the
        fixed frequency of second stage.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FIXed2 RF | LO | IF | LO1 | LO2
        
        

   :param fixedFrequency: This control selects the mixer input or outputsignal which is at the fixed frequency.
   :param channel: Channel number.

.. method:: GetFixedFrequencySignalStage2(self, channel=1)
           
        This function returns the mixer input or output signal which is at the
        fixed frequency of second stage.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FIXed2?
        
        

   :param channel: Channel number.
   :return: fixedFrequency

.. method:: SetFixedFrequency(self, channel=1, fixedFrequency)
           
        This function defines a fixed frequency, to be assigned either to the
        RF, the LO, or the IF signal.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FFIXed <fixed_frequency>
        
        

   :param fixedFrequency: This control defines a fixed frequency, to beassigned either to the RF, the LO, or the IF signal.
   :param channel: Channel number.

.. method:: GetFixedFrequency(self, channel=1)
           
        This function returns a fixed frequency, assigned either to the RF,
        the LO, or the IF signal.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:FFIXed?
        
        

   :param channel: Channel number.
   :return: fixedFrequency

.. method:: SetFixedFrequencyToSignal(self, channel=1, signal, fixedFrequency)
           
        This function assigns a fixed frequency to the RF, LO 1, LO 2, or to
        the IF signal. The fixed frequency setting becomes active if the port
        is selected as a port with fixed frequency.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:MFFixed RF | LO1 | LO2 | IF,
        <fixed_frequency>
        
        

   :param signal: This control selects the mixer input or output signal which is at the fixed frequency.
   :param fixedFrequency: This control defines a fixed frequency, to be assigned either to theRF, the LO 1 | LO 2, or the IF signal.
   :param channel: Channel number.

.. method:: GetFixedFrequencyToSignal(self, channel=1, signal)
           
        This function returns a fixed frequency at selected signal type (RF,
        LO 1, LO 2, or the IF signal).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:MFFixed? RF | LO | LO1 | LO2 |
        IF
        
        

   :param signal: This control selects the mixer input or output signal which is at the fixed frequency.
   :param channel: Channel number.
   :return: fixedFrequency

.. method:: SetFrequencyConversionMode(self, channel=1, frequencyConversionMode)
           
        This function selects the frequency conversion mode of the IF signal.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:TFRequency DCLower | DCUPper |
        UCONversion
        
        

   :param frequencyConversionMode: This control selects the frequencyconversion mode of the IF signal.
   :param channel: Channel number.

.. method:: GetFrequencyConversionMode(self, channel=1)
           
        This function returns the frequency conversion mode of the IF signal.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:TFRequency?
        
        

   :param channel: Channel number.
   :return: frequencyConversionMode

.. method:: SetFrequencyConversionModeStage2(self, channel=1, frequencyConversionMode)
           
        This function selects the frequency conversion mode of the IF signal
        for second stage.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:TFRequency2 DCLower | DCUPper |
        UCONversion
        
        

   :param frequencyConversionMode: This control selects the frequencyconversion mode of the IF signal.
   :param channel: Channel number.

.. method:: GetFrequencyConversionModeStage2(self, channel=1)
           
        This function returns the frequency conversion mode of the IF signal
        of second stage.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:TFRequency2?
        
        

   :param channel: Channel number.
   :return: frequencyConversionMode

.. method:: SetFrequencyHighAccuracy(self, channel=1, highAccuracy)
           
        This function selects the mixer measurement with highest accuracy or
        with maximum speed.
        
        Note(s):
        
        (1) This function can be used only with R&S ZVB instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:HACCuracy ON | OFF
        
        

   :param channel: Channel number.
   :param highAccuracy: This control selects the mixer measurement withhighest accuracy or with maximum speed.

.. method:: GetFrequencyHighAccuracy(self, channel=1)
           
        This function returns whether the mixer measurement is set to highest
        accuracy or to maximum speed.
        
        Note(s):
        
        (1) This function can be used only with R&S ZVB instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:HACCuracy?
        
        

   :param channel: Channel number.
   :return: highAccuracy

.. method:: SetFrequencyLOConversionFactor(self, channel=1, stage, numerator, denominator)
           
        This function sets the frequency conversion factors for the LO 1 or L0
        2 signal.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:LOMultiplier<Stg>
        <numerator>,<denominator>
        
        

   :param denominator: Denominator of the conversionfactor.
   :param numerator: Numerator of the conversion factor.
   :param channel: Channel number.
   :param stage: Number of converter/mixer stage.

.. method:: GetFrequencyLOConversionFactor(self, channel=1, stage)
           
        This function queries the frequency conversion factors for the LO 1 or
        L0 2 signal.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:LOMultiplier<Stg>?
        
        

   :param channel: Channel number.
   :param stage: Number of converter/mixer stage.
   :return: numerator
   :return: denominator

.. method:: SetFrequencyRFConversionFactor(self, channel=1, numerator, denominator)
           
        This function sets the frequency conversion factors for the RF signal.
        
        Notes:
        
        The frequency conversion factors for vector mixer measurements
        (options R&S ZVA-K5) must be equal to 1.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:RFMultiplier
        <numerator>,<denominator>
        
        

   :param denominator: Denominator of the conversionfactor.
   :param numerator: Numerator of the conversion factor.
   :param channel: Channel number.

.. method:: GetFrequencyRFConversionFactor(self, channel=1)
           
        This function queries the frequency conversion factors for the RF
        signal.
        
        Notes:
        
        The frequency conversion factors for vector mixer measurements
        (options R&S ZVA-K5) must be equal to 1.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:RFMultiplier?
        
        

   :param channel: Channel number.
   :return: numerator
   :return: denominator

.. method:: SetRFImageFrequency(self, channel=1, RFImageFrequency)
           
        Prepares an additional mixer measurement at the second RF frequency
        (range) that the mixer converts to the selected IF frequency (RF Image
        Frequency).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:PRFimage
        
        
        

   :param RFImageFrequency: This control enable or disable RF imagemeasurement.
   :param channel: Channel number.

.. method:: GetRFImageFrequency(self, channel=1)
           
        Returns the state of the RF image measurement.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:PRFimage?
        
        
        

   :param channel: Channel number.
   :return: RFImageFrequency

.. method:: SetExternalPowerMeter(self, channel=1, numberOfExternalPowerMeter)
           
        This function selects an external power meter for the source power
        calibration.
        
        Notes:
        
        (1) The command cannot be used unless a power meter is connected via
        GPIB bus, USB or LAN interface and configured with System - System
        Config - Configure External Power Meter.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:PMETer:ID <pmeter_no>
        
        
        

   :param numberOfExternalPowerMeter: This control selects an externalpower meter for the source power calibration.
   :param channel: Channel number.

.. method:: GetExternalPowerMeter(self, channel=1)
           
        This function returns an external power meter for the source power
        calibration.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:PMETer:ID?
        
        

   :param channel: Channel number.
   :return: numberOfExternalPowerMeter

.. method:: RFSourceCalibration(self, channel=1)
           
        This function starts the RF source calibration (1st power calibration
        step for mixer measurements), stores and applies the calibration data.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:MIXer:RF[:ACQuire]
        
        
        

   :param channel: Channel number.

.. method:: IFReceiverCalibration(self, channel=1)
           
        This function starts the IF receiver calibration (2nd power
        calibration step for mixer measurements), stores and applies the
        calibration data.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>:MIXer:IF:ACQuire
        
        
        

   :param channel: Channel number.

.. method:: LOSourceCalibration(self, channel=1)
           
        This function starts the LO source calibration (3rd power calibration
        step for mixer measurements), stores and applies the calibration data.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:MIXer:LO[:ACQuire]
        
        

   :param channel: Channel number.

.. method:: LOSourceCalibrationStage2(self, channel=1)
           
        This function starts the LO 2 source calibration (3rd power
        calibration step for mixer measurements), stores and applies the
        calibration data.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:MIXer:LO2[:ACQuire]
        
        

   :param channel: Channel number.

.. method:: SetMixerDelayMeasurementSetup(self, channel=1, measurementSetup)
           
        Selects the measurement setup/receiver configuration for the mixer
        delay measurement.
        
        Notes:
        
        (1) This mode requires options R&S ZVA-K9 and R&S ZVA-K4
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:RECeiver INTernal | EXTernal
        
        
        

   :param measurementSetup: Selects the measurement setup/receiverconfiguration for the mixer delay measurement.
   :param channel: Channel number.

.. method:: GetMixerDelayMeasurementSetup(self, channel=1)
           
        Queries the measurement setup/receiver configuration for the mixer
        delay measurement.
        
        Notes:
        
        (1) This mode requires options R&S ZVA-K9 and R&S ZVA-K4
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:RECeiver?
        
        
        

   :param channel: Channel number.
   :return: measurementSetup

.. method:: SetMixerDelayLANConnection(self, channel=1, LANConnection)
           
        Selects the LAN connection for the mixer delay measurement with
        external receiver. The function has no effect if a single analyzer
        (internal receiver) is used.
        
        Notes:
        
        (1) This mode requires options R&S ZVA-K9 and R&S ZVA-K4
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:RECeiver:USE
        
        

   :param LANConnection: Selects the LAN connection for the mixer delaymeasurement with external receiver.
   :param channel: Channel number.

.. method:: GetMixerDelayLANConnection(self, channel=1)
           
        Queries the LAN connection for the mixer delay measurement with
        external receiver.
        
        Notes:
        
        (1) This mode requires options R&S ZVA-K9 and R&S ZVA-K4
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:RECeiver:USE?
        
        

   :param channel: Channel number.
   :return: LANConnection

.. method:: DefineMixerDelayReceiver(self, measurementSetup)
           
        Configures a network analyzer as an external receiver for the mixer
        delay measurement and adds it to the list of available receivers.
        
        Notes:
        
        (1) This mode requires options R&S ZVA-K9 and R&S ZVA-K4
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:RECeiver:DEFine
        
        

   :param measurementSetup: Defines IP address ofexternal receiver.

.. method:: ClearMixerDelayReceiverList(self, )
           
        Clears the configuration table for external receivers for the mixer
        delay measurement.
        
        Notes:
        
        (1) This mode requires options R&S ZVA-K9 and R&S ZVA-K4
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:RECeiver:DELete
        
        


.. method:: StartMixerDelayCalibrationSweep(self, channel=1)
           
        Starts a calibration sweep for the mixer delay measurement.
        
        Notes:
        
        (1) This mode requires options R&S ZVA-K9 and R&S ZVA-K4
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:ACQuire
        
        
        

   :param channel: Channel number.

.. method:: SetMixerDelayAperture(self, channel=1, aperture)
           
        Sets the frequency difference between the upper and lower tone
        (aperture).
        
        Notes:
        
        (1) This function requires options R&S ZVA-K9, R&S ZVA-K4 and
        ZVT20-B11.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:APERture
        
        
        

   :param aperture: Defines the frequency difference between the upperand lower tone (aperture).
   :param channel: Channel number.

.. method:: GetMixerDelayAperture(self, channel=1)
           
        Returns the frequency difference between the upper and lower tone
        (aperture).
        
        Notes:
        
        (1) This function requires options R&S ZVA-K9, R&S ZVA-K4 and
        ZVT20-B11.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:APERture?
        
        

   :param channel: Channel number.
   :return: aperture

.. method:: SetMixerDelayConstant(self, channel=1, constantDelay)
           
        Defines a constant mixer delay value, to be used as a reference for a
        mixer delay measurement calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:CDELay
        
        
        

   :param constantDelay: Defines a constant mixer delay value.
   :param channel: Channel number.

.. method:: GetMixerDelayConstant(self, channel=1)
           
        Returns a constant mixer delay value, to be used as a reference for a
        mixer delay measurement calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:CDELay?
        
        
        

   :param channel: Channel number.
   :return: constantDelay

.. method:: SetMixerDelayCombinerState(self, channel=1, internalCombiner)
           
        Enables or disables the internal combiner (for R&S ZVT analyzers with
        option R&S ZVT20-B11 or R&S ZVA analyzers with an Extension Unit R&S
        ZVAXxx and option R&S ZVAXxx-B11). The internal combiner requires the
        following port configuration: Lower Tone: Port 1, Upper Tone: Port 3.
        The two-tone signal is available at port 1.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:COMBiner[:STATe]
        
        
        

   :param internalCombiner: State of combiner.
   :param channel: Channel number.

.. method:: GetMixerDelayCombinerState(self, channel=1)
           
        Returns the state of the internal combiner (for R&S ZVT analyzers with
        option R&S ZVT20-B11 or R&S ZVA analyzers with an Extension Unit R&S
        ZVAXxx and option R&S ZVAXxx-B11). The internal combiner requires the
        following port configuration: Lower Tone: Port 1, Upper Tone: Port 3.
        The two-tone signal is available at port 1.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:COMBiner[:STATe]?
        
        

   :param channel: Channel number.
   :return: internalCombiner

.. method:: SetMixerDelayDivisionByTwoEnabled(self, channel=1, divisionByTwo)
           
        Enables or disables the division of loaded mixer delay calibration
        data by two.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:DIVide ON | OFF
        
        
        

   :param divisionByTwo: State of the division of loaded mixer delaycalibration data by two.
   :param channel: Channel number.

.. method:: GetMixerDelayDivisionByTwoEnabled(self, channel=1)
           
        Returns the division state of loaded mixer delay calibration data by
        two.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:DIVide?
        
        

   :param channel: Channel number.
   :return: divisionByTwo

.. method:: SetMixerConstantDelayEnabled(self, channel=1, constantDelay)
           
        Selects constant or variable delay for the mixer delay calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:CDMode ON|OFF
        
        
        

   :param constantDelay: Select constant or variable delay for themixer delay calibration.
   :param channel: Channel number.

.. method:: GetMixerConstantDelayEnabled(self, channel=1)
           
        Returns constant or variable delay for the mixer delay calibration
        state.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:CDMode?
        
        
        

   :param channel: Channel number.
   :return: constantDelay

.. method:: SetMixerDelayCorrection(self, channel=1, correction)
           
        Qualifies whether the analyzer applies the current mixer delay meas.
        calibration data.
        
        Notes:
        
        (1) This function requires options R&S ZVA-K9 and R&S ZVA-K4.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:CORRection[:STATe]
        
        
        

   :param correction: Apply or ignore current mixer delay calibrationdata.
   :param channel: Channel number.

.. method:: GetMixerDelayCorrection(self, channel=1)
           
        Gets state of applying current mixer delay meas. calibration data.
        
        Notes:
        
        (1) This function requires options R&S ZVA-K9 and R&S ZVA-K4.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:CORRection[:STATe]?
        
        
        

   :param channel: Channel number.
   :return: correction

.. method:: SetMixerDelayUpperToneSource(self, channel=1, source, portNumber)
           
        Selects the source for the upper tone signal that is used for the
        mixer delay measurement.
        
        Notes:
        
        (1) This function requires options R&S ZVA-K9 and R&S ZVA-K4.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:UTONe NONE | PORT | GENerator,
        <source_no>
        
        
        

   :param source: Upper tone source.
   :param portNumber: Number of the port for the internal source or ofthe generator (to be omitted for source: NONE)
   :param channel: Channel number.

.. method:: GetMixerDelayUpperToneSource(self, channel=1)
           
        Returns the source for the upper tone signal that is used for the
        mixer delay measurement.
        
        Notes:
        
        (1) This function requires options R&S ZVA-K9 and R&S ZVA-K4.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:MDELay:UTONe? PORT | GENerator
        
        
        

   :param channel: Channel number.
   :return: source
   :return: portNumber

.. method:: LoadMixerDelayValues(self, channel=1, type, file)
           
        Loads the known delay values of a calibration mixer, to be used as a
        reference for a mixer delay measurement calibration. Mixer delay
        measurements are controlled using the SENSe<Ch>:FREQuency:MDELay...
        commands.
        
        Remote-control command(s):
        MMEMory:LOAD:MDAData <Channel>, '<file_name>' | CDELay
        
        
        

   :param type: Type of delay values
   :param file: String parameter tospecify the name and directory of the loaded file. The defaultextension (manual control) for files containing known delays is *.csv,although other extensions are allowed. If no path is specified theanalyzer searches the current directory, to be queried withMMEMory:CDIRectory.
   :param channel: Channel number.

.. method:: LoadMixerDelayCalibrationData(self, channel=1, file)
           
        Loads correction data for a mixer delay measurement calibration from a
        specified file and assigns it to a channel with a specified number.
        Mixer delay measurements are controlled using the
        SENSe<Ch>:FREQuency:MDELay... commands.
        
        Remote-control command(s):
        MMEMory:LOAD:MDCData <Channel>, '<file_name>'
        
        
        

   :param file: String parameter to specify the name and directory ofthe calibration file to be loaded. The default extension (manualcontrol) for mixer delay calibration files is *.mcal, although otherextensions are allowed. If no path is specified the analyzer searchesthe current directory, to be queried with MMEMory:CDIRectory?.
   :param channel: Channel number.

.. method:: StoreMixerDelayCalibrationData(self, channel=1, file)
           
        Stores the correction data for a mixer delay measurement calibration
        to a specified file. Mixer delay measurements are controlled using the
        SENSe<Ch>:FREQuency:MDELay... commands.
        
        Remote-control command(s):
        MMEMory:STORe:MDCData <Channel>, '<file_name>'
        
        
        

   :param file: String parameter to specify the name and directory ofthe created calibration file. The default extension (manual control)for mixer delay calibration files is *.mcal, although other extensionsare allowed. If no path is specified the analyzer uses the currentdirectory, to be queried with MMEMory:CDIRectory?.
   :param channel: Channel number.

.. method:: SetVectorMixerMode(self, channel=1, mixerMode)
           
        This function toggle between the (frequency-converting) vector mixer
        mode and normal operation, where the analyzer measures the unconverted
        fundamental wave.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion VMIXer | FUNDamental
        
        

   :param mixerMode: This control toggle between the (frequency-converting) vector mixer mode and normal operation, where the analyzermeasures the unconverted fundamental wave.
   :param channel: Channel number.

.. method:: GetVectorMixerMode(self, channel=1)
           
        This function returns the (frequency-converting) vector mixer mode or
        normal operation, where the analyzer measures the unconverted
        fundamental wave.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion?
        
        

   :param channel: Channel number.
   :return: mixerMode

.. method:: SetInternalSignalSourceAUX(self, channel=1, internalSignalSource)
           
        Selects an analyzer port as a signal source for the Aux LO signal in a
        vector mixer measurement (option R&S ZVA-K5). The Aux LO signal is fed
        to the MEAS and REF mixers.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:AINTernal NONE | <port_number>
        
        

   :param internalSignalSource: Selects an analyzer port as a signalsource for the Aux LO signal in a vector mixer measurement.
   :param channel: Channel number.

.. method:: GetInternalSignalSourceAUX(self, channel=1)
           
        Queries analyzer port as a signal source for the Aux LO signal in a
        vector mixer measurement (option R&S ZVA-K5).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:AINTernal?
        
        

   :param channel: Channel number.
   :return: internalSignalSource

.. method:: SetExternalSignalSourceAUX(self, channel=1, externalSignalSource)
           
        Selects an external generator as a signal source for the Aux LO signal
        in a vector mixer measurement (option R&S ZVA-K5). The Aux LO signal
        is fed to the MEAS and REF mixers.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:AEXTernal NONE | <port_number>
        
        

   :param externalSignalSource: Selects an external generator as a signalsource for the Aux LO signal in a vector mixer measurement.
   :param channel: Channel number.

.. method:: GetExternalSignalSourceAUX(self, channel=1)
           
        Queries an external generator as a signal source for the Aux LO signal
        in a vector mixer measurement (option R&S ZVA-K5). The Aux LO signal
        is fed to the MEAS and REF mixers.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:AEXTernal?
        
        

   :param channel: Channel number.
   :return: externalSignalSource

.. method:: SetAUXMixerPort(self, channel=1, portNumber)
           
        Selects the Aux Mixer port (and thus the basic test setup) for vector
        mixer measurements (option R&S ZVA-K5).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:APORt
        
        

   :param portNumber: Selects the Aux Mixer port (and thus the basic testsetup) for vector mixer measurements (option R&S ZVA-K5).
   :param channel: Channel number.

.. method:: GetAUXMixerPort(self, channel=1)
           
        Queries the Aux Mixer port (and thus the basic test setup) for vector
        mixer measurements (option R&S ZVA-K5).
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:MIXer:APORt?
        
        

   :param channel: Channel number.
   :return: portNumber

.. method:: SetAUXFixedPower(self, channel=1, fixedPower)
           
        Defines a fixed power for the Aux LO signal in a vector mixer
        measurement (option R&S ZVA-K5). The Aux LO signal is fed to the MEAS
        and REF mixers.
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency:CONVersion:MIXer:PAFixed
        
        

   :param fixedPower: Defines a fixed power for the Aux LO signal in avector mixer measurement (option R&S ZVA-K5). The Aux LO signal is fedto the MEAS and REF mixers.
   :param channel: Channel number.

.. method:: GetAUXFixedPower(self, channel=1)
           
        Queries a fixed power for the Aux LO signal in a vector mixer
        measurement (option R&S ZVA-K5).
        
        Remote-control command(s):
        SOURce<Ch>:FREQuency:CONVersion:MIXer:PAFixed?
        
        

   :param channel: Channel number.
   :return: fixedPower

.. method:: AutomaticVectorMixerCalibration(self, channel=1, mode, dispersion, mixerParameter, delayPhase)
           
        This function allows the automatic vector mixer calibration using a
        calibration unit. It is only available in Vector Mixer Mode.
        
        Note(s):
        
        (1) The first part of the calibration (acquisition of one-port
        correction data using the calibration unit) is performed using
        :SENSE<Ch>:CORRECTION:COLLECT:AUTO:VMIXer:ACQuire BASE. Like in manual
        operation, the assignment between analyzer and calibration unit ports
        must be 1:1, i.e. analyzer ports 1 and 2 must be connected to
        calibration unit ports 1 and 2, respectively.
        
        (2) After connecting the reciprocal calibration mixer, the second part
        (acquisition of 2-port correction data) is performed using
        :SENSE<Ch>:CORRECTION:COLLECT:AUTO:VMIXer:ACQuire MIXer [,
        <Dispersion>, AUTO | <delay | phase>].
        
        (3) Finally, to apply the resulting error terms to the related
        channel, use the rszvb_CalibrationAutoAssignmentSave function.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:VMIXer:ACQuire BASE | MIXer [,
        <Dispersion>, AUTO | <delay | phase>]
        
        

   :param dispersion: Statusparameter of the mixer.
   :param mixerParameter: The missing mixer parameter caneither be calculated automatically (AUTO) or specified by the user.
   :param delayPhase: The missing mixer parameter can bespecified by the user (<delay | phase>). If Mixer Parameter is not setto AUTO, this parameter is interpreted as:- delay(in picoseconds) if Dispersion is FALSE- phase (in degrees) if Dispersion is TRUE
   :param mode: This control selects the calibration mode.
   :param channel: Channel number.

.. method:: SetIMODLowerToneSource(self, channel=1, source, sourceNumber)
           
        This function selects the source for the lower tone signal that is
        used for the intermodulation measurement.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:LTONe PORT | GENerator, <source_no>
        
        

   :param source: This control selects the source for the lower tonesignal that is used for the intermodulation measurement.
   :param sourceNumber: This control selects the number of the port for the internal source orof the generator.
   :param channel: Channel number.

.. method:: GetIMODLowerToneSource(self, channel=1)
           
        This function returns the source for the lower tone signal that is
        used for the intermodulation measurement.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:LTONe?
        
        

   :param channel: Channel number.
   :return: source
   :return: sourceNumber

.. method:: SetIMODUpperToneSource(self, channel=1, source, sourceNumber)
           
        This function selects the source for the upper tone signal that is
        used for the intermodulation measurement.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:UTONe PORT | GENerator, <source_no>
        
        

   :param source: This control selects the source for the upper tonesignal that is used for the intermodulation measurement.
   :param sourceNumber: This control selects the number of the port for the internal source orof the generator.
   :param channel: Channel number.

.. method:: GetIMODUpperToneSource(self, channel=1)
           
        This function returns the source for the upper tone signal that is
        used for the intermodulation measurement.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:UTONe?
        
        

   :param channel: Channel number.
   :return: source
   :return: sourceNumber

.. method:: SetIMODToneDistance(self, channel=1, toneDistance)
           
        This function defines the tone distance (frequency offset) between the
        upper and the lower tone.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:TDIStance
        
        

   :param toneDistance: This control sets the tone distance (frequencyoffset) between the upper and the lower tone (Upper tone frequencyminus lower tone frequency)
   :param channel: Channel number.

.. method:: GetIMODToneDistance(self, channel=1)
           
        This function returns the tone distance (frequency offset) between the
        upper and the lower tone.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:TDIStance?
        
        

   :param channel: Channel number.
   :return: toneDistance

.. method:: SetIMODReceiverPort(self, channel=1, receiverPort)
           
        This function selects the receiver port for the intermodulation
        measurement.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:RECeiver
        
        

   :param receiverPort: This control selects the receiver port for theintermodulation measurement.
   :param channel: Channel number.

.. method:: GetIMODReceiverPort(self, channel=1)
           
        This function returns the receiver port for the intermodulation
        measurement.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:RECeiver?
        
        

   :param channel: Channel number.
   :return: receiverPort

.. method:: SetIMODMeasurementOrder(self, channel=1, productOrder, measurementState)
           
        This function enables or disables the measurement of the
        intermodulation products of order <IM order>.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:ORDer<Im>[:STATe] ON | OFF
        
        

   :param measurementState: This control enables ordisables measurement.
   :param channel: Channel number.
   :param productOrder: This control selects the order of IM products

.. method:: GetIMODMeasurementOrder(self, channel=1, productOrder)
           
        This function returns the state of the measurement of the
        intermodulation products of order <IM order>.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:ORDer<Im>[:STATe]?
        
        

   :param channel: Channel number.
   :param productOrder: This control selects the order of IM products
   :return: measurementState

.. method:: SetIMODEnhancedWaveCorrection(self, channel=1, state)
           
        This function switches the preparation for an enhanced wave correction
        of an intermodulation measurement on or off.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:PEWCorr[:STATe]
        
        

   :param state: This control enables or disables preparation for anenhanced wave correction.
   :param channel: Channel number.

.. method:: GetIMODEnhancedWaveCorrection(self, channel=1)
           
        This function queries the state of the preparation for an enhanced
        wave correction of an intermodulation measurement.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:PEWCorr[:STATe]?
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetIMODInternalCombiner(self, channel=1, internalCombiner)
           
        This function enables or disables the internal combiner. The internal
        combiner requires the following port configuration: Lower Tone: Port
        1, Upper Tone: Port 3.
        
        Note(s):
        
        (1) This function requires option R&S ZVT20-B11.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:COMBiner[:STATe] ON | OFF
        
        

   :param internalCombiner: This control enables or disables theinternal combiner.
   :param channel: Channel number.

.. method:: GetIMODInternalCombiner(self, channel=1)
           
        This function returns the internal combiner.
        
        Note(s):
        
        (1) This function requires option R&S ZVT20-B11.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:COMBiner[:STATe]?
        
        

   :param channel: Channel number.
   :return: internalCombiner

.. method:: SetIMODSpectrumMeasurement(self, channel=1, spectrumMeasurement)
           
        This function enables or disables the measurement of the
        intermodulation spectrum without creating a new channel.
        
        Note(s):
        
        (1) If a new channel is desired, it must be created by other means -
        use command CALC:PAR:SDEF 'name','order' (function
        rszvb_ChannelAddTrace)
        
        (2) This function is not available for R&S ZVB instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:SPECtrum[:STATe] ON | OFF
        
        

   :param spectrumMeasurement: This control enables or disables themeasurement of the intermodulation spectrum without creating a newchannel.
   :param channel: Channel number.

.. method:: GetIMODSpectrumMeasurement(self, channel=1)
           
        This function returns the state of the measurement of the
        intermodulation spectrum without creating a new channel.
        
        Note(s):
        
        (1) This function is not available for R&S ZVB instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:SPECtrum[:STATe]?
        
        

   :param channel: Channel number.
   :return: spectrumMeasurement

.. method:: SetIMODMaxOrder(self, channel=1, maxOrder)
           
        This function defines the maximum order of intermodulation products
        for the intermodulation spectrum measurement.
        
        Note(s):
        
        (1) This function is not available for R&S ZVB instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:SPECtrum:MORDer
        
        

   :param maxOrder: This control selects the maximum order of IM products
   :param channel: Channel number.

.. method:: GetIMODMaxOrder(self, channel=1)
           
        This function returns the maximum order of intermodulation products
        for the intermodulation spectrum measurement.
        
        Note(s):
        
        (1) This function is not available for R&S ZVB instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:SPECtrum:MORDer?
        
        

   :param channel: Channel number.
   :return: maxOrder

.. method:: SetIMODTwoToneOutput(self, channel=1, twoToneOutput)
           
        Selects the source for the two tone output signal for intermodulation
        measurements.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:TTOutput PORT | EDEVice
        
        

   :param twoToneOutput: Selects the source for the two tone outputsignal for intermodulation measurements.
   :param channel: Channel number.

.. method:: GetIMODTwoToneOutput(self, channel=1)
           
        Returns the source for the two tone output signal for intermodulation
        measurements.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:TTOutput?
        
        

   :param channel: Channel number.
   :return: twoToneOutput

.. method:: StartIMODLowerToneSourcePowerCalibration(self, channel=1)
           
        This function starts the source calibration for the lower tone (1st
        power calibration step for intermodulation measurements), stores and
        applies the calibration data.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:IMODulation:LTONe[:ACQuire]
        
        

   :param channel: Channel number.

.. method:: StartIMODUpperToneSourcePowerCalibration(self, channel=1)
           
        This function starts the source calibration for the upper tone (2nd
        power calibration step for intermodulation measurements), stores and
        applies the calibration data.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:IMODulation:UTONe[:ACQuire]
        
        

   :param channel: Channel number.

.. method:: StartIMODReceivePortSourcePowerCalibration(self, channel=1)
           
        This function starts a source power calibration for the receive port
        of the intermodulation measurement (2nd power
        calibration step for intermodulation measurements), stores and applies
        the calibration data.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:IMODulation:RPORt[:ACQuire]
        
        

   :param channel: Channel number.

.. method:: StartIMODLowerUpperTonePortsSourcePowerCalibration(self, channel=1)
           
        This function starts the source calibration for the lower and upper
        tone ports (1st power calibration step for
        intermodulation measurements), stores and applies the calibration
        data.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:IMODulation:SPORt[:ACQuire]
        
        

   :param channel: Channel number.

.. method:: StartIMODReceiverPortPowerCalibration(self, channel=1)
           
        This function starts the receiver calibration (2nd power calibration
        step for intermodulation measurements), stores and applies the
        calibration data.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>:IMODulation:RPORt:ACQuire
        
        

   :param channel: Channel number.

.. method:: StartIMODReceiverPowerCalibration(self, channel=1)
           
        This function starts the receiver calibration (2nd power calibration
        step for intermodulation measurements), stores and applies the
        calibration data.
        
        Note(s):
        
        (1) The receiver calibration relies on the source power calibration
        acquired in step no. 1. Use this function after using
        rszvb_StartIMODLowerToneSourcePowerCalibration and
        rszvb_StartIMODUpperToneSourcePowerCalibration functions.
        
        (2) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>:IMODulation:ACQuire
        
        

   :param channel: Channel number.

.. method:: SetIMODDistortionMeasurementCalibrationState(self, channel=1, state)
           
        This function activates or deactivates calibrations (system error
        correction) at all selected intermodulation frequency
        ranges.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:IMODulation[:STATe]
        
        

   :param state: Activates or deactivates calibrations (system errorcorrection) at all selected intermodulation frequency ranges.
   :param channel: Channel number.

.. method:: GetIMODDistortionMeasurementCalibrationState(self, channel=1)
           
        This function queries the state of calibrations (system error
        correction) at all selected intermodulation frequency
        ranges.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:IMODulation[:STATe]?
        
        

   :param channel: Channel number.
   :return: state

.. method:: DisableIMODMeasurement(self, channel=1)
           
        This function disables the intermodulation measurement and switches
        back to normal (non frequency-converting) mode.
        
        Note(s):
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:IMODulation:CONVersion OFF
        
        

   :param channel: Channel number.

.. method:: SetNoiseFigureDetectorMeasurementTime(self, channel=1, detectorTime)
           
        This function sets the time that the analyzer uses to acquire data
        with each of the detector settings.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:DETector:TIME
        
        

   :param detectorTime: This control sets the time that the analyzeruses to acquire data with each of the detector settings
   :param channel: Channel number.

.. method:: GetNoiseFigureDetectorMeasurementTime(self, channel=1)
           
        This function returns the time that the analyzer uses to acquire data
        with each of the detector settings.
        
        
        Remote-control command(s):
        [SENSe<Ch>:]SWEep:DETector:TIME?
        
        

   :param channel: Channel number.
   :return: detectorTime

.. method:: SetNoiseFigureMeasurementMode(self, channel=1, measurementMode)
           
        This function selects sequential or simultaneous measurement mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]NFIGure:SEQuential ON | OFF
        
        

   :param measurementMode: This control selects sequential orsimultaneous measurement mode.
   :param channel: Channel number.

.. method:: GetNoiseFigureMeasurementMode(self, channel=1)
           
        This function returns sequential or simultaneous measurement mode.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]NFIGure:SEQuential?
        
        

   :param channel: Channel number.
   :return: measurementMode

.. method:: SetNoiseFigureLOOscillator(self, channel=1, LOOscillator)
           
        This function sets whether the analyzer assumes an ideal T0 source
        noise.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]NFIGure:ISNoise ON | OFF
        
        

   :param LOOscillator: This control switches the LO oscillator on oroff.
   :param channel: Channel number.

.. method:: GetNoiseFigureLOOscillator(self, channel=1)
           
        This function returns whether the analyzer assumes an ideal T0 source
        noise.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]NFIGure:ISNoise?
        
        

   :param channel: Channel number.
   :return: LOOscillator

.. method:: SetNoiseFigureNarowbandDUT(self, channel=1, narowbandDUT)
           
        This function configures the noise figure measurement for a narrowband
        DUT.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]NFIGure:NDUT
        
        

   :param narowbandDUT: This control switches the narowband DUT on oroff.
   :param channel: Channel number.

.. method:: GetNoiseFigureNarowbandDUT(self, channel=1)
           
        This function returns the state of the moise figure narowband DUT.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]NFIGure:NDUT?
        
        

   :param channel: Channel number.
   :return: narowbandDUT

.. method:: SetNoiseFigureRFImageCorrection(self, channel=1, RFImageCorrection)
           
        This function enables or disables the RF image correction for mixer
        noise figure measurements.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]NFIGure:RFICorr
        
        

   :param RFImageCorrection: This control enables or disables the RFimage correction for mixer noise figure measurements.
   :param channel: Channel number.

.. method:: GetNoiseFigureRFImageCorrection(self, channel=1)
           
        This function returns state of the RF image correction for mixer noise
        figure measurements.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]NFIGure:RFICorr?
        
        

   :param channel: Channel number.
   :return: RFImageCorrection

.. method:: SetNoiseFigureCalibrationState(self, channel=1, calibration)
           
        This function disables or enables the Noise Figure Calibration for the
        active channel <Ch>.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:NFIGure[:STATe] ON | OFF
        
        

   :param channel: Channel number.
   :param calibration: This control disables or enables the NoiseFigure Calibration for the active channel <Ch>.

.. method:: GetNoiseFigureCalibrationState(self, channel=1)
           
        This function returns the state of the Noise Figure Calibration for
        the active channel <Ch>.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:NFIGure[:STATe]?
        
        

   :param channel: Channel number.
   :return: calibration

.. method:: GetNoiseFigureCalibrationStateLabel(self, channel=1, bufferSize, label)
           
        Returns the noise figure calibration state label of active trace in
        channel <Chn>. The active trace must be a noise figure trace,
        otherwise an empty string is returned.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:NSTate?
        
        

   :param bufferSize: This control defines the size of array passed toargument 'Label'.
   :param channel: Channel number.
   :param label: This control returns the noisefigure calibration state label.

.. method:: DefineNoiseFigureCalibrationSettings(self, channel=1, port1, port2, externalAttenuator, sourceNoiseCalAttenuation, DUTMeasurementAttenuation)
           
        This function defines the calibration settings (port assignment,
        attenuations) for a noise figure calibration.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:NFIGure:STARt
        
        

   :param externalAttenuator: This control indicateswhether an external attenuator is used
   :param sourceNoiseCalAttenuation: Thiscontrol sets the attenuation of the source level during the sourcenoise calibration.
   :param channel: Channel number of the correctedchannel.
   :param port2: This control defines the port number ofthe DUT output.
   :param DUTMeasurementAttenuation: This controlsets the attenuation of the source level during the measurement (i.e.after calibration).
   :param port1: This control defines the port number of the DUT input.

.. method:: StartNoiseFigureCalibration(self, channel=1, calibrationStep)
           
        This function starts a noise figure calibration sweep for the NWA
        receiver, NWA source, or an external attenuator.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        (2) A noise figure calibration must be terminated with one of the
        following functions, to be sent immediately after the sequence of
        ...[:ACQuire] commands:
        
        rszvb_TerminateNoiseFigureCalibration - terminate calibration,
        discarding the acquired calibration data (the active channel is not
        calibrated)
        
        rszvb_CompleteNoiseFigureCalibration - terminate calibration, applying
        the acquired calibration data (the active channel is calibrated)
        
        These functions ensure that the analyzer is able to start a new
        measurement sweep.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:NFIGure[:ACQuire] RECeiver | SOURce |
        ATTenuator
        
        

   :param calibrationStep: This control defines the calibration step, tobe performed in the order RECeiver -> SOURce -> ATTenuator (optional,only if an external attenuator is used).
   :param channel: Channel number of the correctedchannel.

.. method:: TerminateNoiseFigureCalibration(self, channel=1)
           
        This function terminates a noise figure calibration, discarding the
        acquired data
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:NFIGure:END
        
        

   :param channel: Channel number of the correctedchannel.

.. method:: CompleteNoiseFigureCalibration(self, channel=1)
           
        This function completes a noise figure calibration, storing and
        applying the acquired data
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:NFIGure:SAVE
        
        

   :param channel: Channel number of the correctedchannel.

.. method:: OverwriteNoiseFigureChannelSettings(self, channel=1, traceName)
           
        This function overwrites the current channel settings with the ones
        that were used during the active (previously performed) noise figure
        calibration. The referenced trace must show the noise figure of a
        device.
        
        Note(s):
        
        (1) This function is available only with option R&S ZVAB-K30.
        
        Remote-control command(s):
        CALCulate<Ch>:PARameter:NFIGure:CSETtings
        
        

   :param channel: Channel number of the correctedchannel.
   :param traceName: Name of a noise figure trace.

.. method:: SetVirtualTransformBalancedState(self, channel=1, functionType, logicalPortNumber, state)
           
        This function enables or disables the deembedding/embedding function
        for balanced ports.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:DEEMbedding<Log_pt>[:STATe]
        <Boolean>
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:EMBedding<Log_pt>[:STATe]
        <Boolean>
        
        
        

   :param state: This control enables or disables the deembeddingfunction for balanced ports.
   :param functionType: Function type, deembedding or embedding.
   :param logicalPortNumber: Logical port number.
   :param channel: Channel number.

.. method:: GetVirtualTransformBalancedState(self, channel=1, functionType, logicalPortNumber)
           
        This function queries the state of the deembedding/embedding function
        for balanced ports.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:DEEMbedding<Log_pt>[:STATe]
        ?
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:EMBedding<Log_pt>[:STATe]?
        
        
        

   :param functionType: Function type, deembedding or embedding.
   :param logicalPortNumber: Logical port number.
   :param channel: Channel number.
   :return: state

.. method:: SetVirtualTransformBalancedPort(self, channel=1, functionType, logicalPortNumber, parameterType, parameterNumber, circuitModel, value)
           
        This function specifies the capacitance, inductance or resistance
        values C1, C2, C3, L1, L2, L3 or R1, R2, R3 in the different circuit
        models for balanced port deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:DEEMbedding<Log_pt>:PARamet
        ers:C<no> STSC | SCST | CSSL | LSSC | CSSC | SLCS | SCLS |
        SCCS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:DEEMbedding<Log_pt>:PARamet
        ers:L<no> STSL | SLST | CSSL | LSSC | LSSL | SLCS | SCLS |
        SLLS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:DEEMbedding<Log_pt>:PARamet
        ers:R<no> STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS
        | SCLS | SCCS | SLLS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:EMBedding<Log_pt>:PARameter
        s:C<no> STSC | SCST | CSSL | LSSC | CSSC | SLCS | SCLS |
        SCCS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:EMBedding<Log_pt>:PARameter
        s:L<no> STSL | SLST | CSSL | LSSC | LSSL | SLCS | SCLS |
        SLLS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:EMBedding<Log_pt>:PARameter
        s:R<no> STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS |
        SCLS | SCCS | SLLS,<numeric_value>
        
        

   :param parameterType: Parameter type, capacitance, inductance orresistance.
   :param functionType: Function type, deembedding or embedding.
   :param value: Capacitance C<no>, Inductance L<no> or Resistance R<no>for the specified circuit model.
   :param parameterNumber: Numberof capacitances, inductances or resistances in circuit model.
   :param logicalPortNumber: Logical port number.
   :param circuitModel: This control definesthe possible circuit model.
   :param channel: Channel number.

.. method:: GetVirtualTransformBalancedPort(self, channel=1, functionType, logicalPortNumber, parameterType, parameterNumber, circuitModel)
           
        This function returns the capacitance, inductance or resistance values
        C1, C2, C3, L1, L2, L3 or R1, R2, R3 in the different circuit models
        for balanced port deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:DEEMbedding<Log_pt>:PARamet
        ers:C<no>? STSC | SCST | CSSL | LSSC | CSSC | SLCS | SCLS | SCCS
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:DEEMbedding<Log_pt>:PARamet
        ers:L<no>? STSL | SLST | CSSL | LSSC | LSSL | SLCS | SCLS | SLLS
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:DEEMbedding<Log_pt>:PARamet
        ers:R<no>? STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL |
        SLCS | SCLS | SCCS | SLLS
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:EMBedding<Log_pt>:PARameter
        s:C<no>? STSC | SCST | CSSL | LSSC | CSSC | SLCS | SCLS | SCCS
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:EMBedding<Log_pt>:PARameter
        s:L<no>? STSL | SLST | CSSL | LSSC | LSSL | SLCS | SCLS | SLLS
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:EMBedding<Log_pt>:PARameter
        s:R<no>? STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS
        | SCLS | SCCS | SLLS
        
        

   :param parameterType: Parameter type, capacitance, inductance orresistance.
   :param functionType: Function type, deembedding or embedding.
   :param parameterNumber: Numberof capacitances, inductances or resistances in circuit model.
   :param logicalPortNumber: Logical port number.

   :param circuitModel: This control definesthe possible circuit model.
   :param channel: Channel number.
   :return: value

.. method:: SetVirtualTransformBalancedCircuitModel(self, channel=1, functionType, logicalPortNumber, circuitModel)
           
        This function selects the circuit model for balanced port
        deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:DEEMbedding<Log_pt>:TNDefin
        ition
        FIMPort | STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS
        | SCLS | SCCS | SLLS
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:EMBedding<Log_pt>:TNDefinit
        ion
        FIMPort | STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS
        | SCLS | SCCS | SLLS
        
        

   :param circuitModel: This control defines the possible circuit model.
   :param functionType: Function type, deembedding or embedding.
   :param logicalPortNumber: Logical port number.

   :param channel: Channel number.

.. method:: GetVirtualTransformBalancedCircuitModel(self, channel=1, functionType, logicalPortNumber)
           
        This function returns the circuit model for balanced port
        deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:DEEMbedding<Log_pt>:TNDefin
        ition?
        CALCulate<Ch>:TRANsform:VNETworks:BALanced:EMBedding<Log_pt>:TNDefinit
        ion?
        
        
        
        
        

   :param functionType: Function type, deembedding or embedding.
   :param logicalPortNumber: Logical port number.

   :param channel: Channel number.
   :return: circuitModel

.. method:: LoadBalancedPortCircuitModelData(self, channel=1, functionType, logicalPortNumber, fileName, parameter)
           
        This function loads data from a specified Touchstone file defining the
        characteristics of the current embedded/deembedded balanced port
        circuit model. A balanced port circuit model involving file import
        must be selected before using this function.
        
        Remote-control command(s):
        MMEMory:LOAD:VNETworks<Ch>:BALanced:EMBedding<Log_pt> '<file_name>',
        PMAin | PSECondary
        MMEMory:LOAD:VNETworks<Ch>:BALanced:DEEMbedding<Log_pt> '<file_name>',
        PMAin | PSECondary
        
        
        

   :param parameter: Port assignment for two 2-port (*.s2p) files.

   :param functionType: Function type, deembedding or embedding.
   :param logicalPortNumber: Logical port number.

   :param channel: Channel number.
   :param fileName: This control specifies the name and directory of theloaded Touchstone file. The balanced port circuit models STSL | STSC |SLST | SCST require two 2-port (*.s2p) files, to be assigned to thedifferent ports PMAin and PSECondary; the FIMPort model requires asingle 4-port (*.s4p) file but no additional port assignment.

.. method:: LoadAndInterchangeBalancedPortCircuitModelData(self, channel=1, functionType, logicalPortNumber, fileName, parameter)
           
        This function loads data from a specified Touchstone file defining the
        characteristics of the current embedded/deembedded balanced port
        circuit model. A balanced port circuit model involving file import
        must be selected before using this function.
        
        Remote-control command(s):
        MMEMory:LOAD:VNETworks<Ch>:BALanced:EMBedding<Log_pt> '<file_name>',
        PMAin | PSECondary
        MMEMory:LOAD:VNETworks<Ch>:BALanced:DEEMbedding<Log_pt> '<file_name>',
        PMAin | PSECondary
        
        
        

   :param parameter: Port assignment for two 2-port (*.s2p) files.

   :param functionType: Function type, deembedding or embedding.
   :param logicalPortNumber: Logical port number.

   :param channel: Channel number.
   :param fileName: This control specifies the name and directory of theloaded Touchstone file. The balanced port circuit models STSL | STSC |SLST | SCST require two 2-port (*.s2p) files, to be assigned to thedifferent ports PMAin and PSECondary; the FIMPort model requires asingle 4-port (*.s4p) file but no additional port assignment.

.. method:: SetVirtualTransformSingleEndedState(self, channel=1, functionType, physicalPortNumber, state)
           
        This function enables or disables the deembedding/embedding function
        for single ended ports.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:DEEMbedding<Ph_pt>[:STATe]
        <Boolean>
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:EMBedding<Ph_pt>[:STATe]
        <Boolean>
        
        

   :param state: This control enables or disables the deembeddingfunction for single ended ports.
   :param physicalPortNumber: Physical port number.

   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.

.. method:: GetVirtualTransformSingleEndedState(self, channel=1, functionType, physicalPortNumber)
           
        This function queries the state of the deembedding/embedding function
        for single ended ports.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:DEEMbedding<Ph_pt>[:STATe]?
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:EMBedding<Ph_pt>[:STATe]?
        
        

   :param physicalPortNumber: Physical port number.

   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :return: state

.. method:: SetVirtualTransformSingleEndedPort(self, channel=1, functionType, physicalPortNumber, parameterType, parameterNumber, circuitModel, value)
           
        This function specifies the capacitance, inductance or resistance
        values C1, C2, L1, L2 or R1, R2 in the different circuit models for
        single ended port deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:DEEMbedding<Ph_pt>:PARameters
        :C<no> CSL | LSC | CSC | SLC | SCL | SCC,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:DEEMbedding<Ph_pt>:PARameters
        :L<no> CSL | LSC | LSL | SLC | SCL | SLL,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:DEEMbedding<Ph_pt>:PARameters
        :R<no> CSL | LSC | CSC | LSL | SLC | SCL | SCC | SLL,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:EMBedding<Ph_pt>:PARameters:C
        <no> CSL | LSC | CSC | SLC | SCL | SCC,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:EMBedding<Ph_pt>:PARameters:L
        <no> CSL | LSC | LSL | SLC | SCL | SLL,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:EMBedding<Ph_pt>:PARameters:R
        <no> CSL | LSC | CSC | LSL | SLC | SCL | SCC | SLL,<numeric_value>
        
        

   :param parameterType: Parameter type, capacitance, inductance orresistance.
   :param physicalPortNumber: Physical port number.

   :param functionType: Function type, deembedding or embedding.
   :param value: Capacitance C<no>, Inductance L<no> or Resistance R<no>for the specified circuit model.
   :param parameterNumber: Numberof capacitances, inductances or resistances in circuit model.
   :param circuitModel: This control defines thepossible circuit model.
   :param channel: Channel number.

.. method:: GetVirtualTransformSingleEndedPort(self, channel=1, functionType, physicalPortNumber, parameterType, parameterNumber, circuitModel)
           
        This function returns the capacitance, inductance or resistance values
        C1, C2, L1, L2 or R1, R2 in the different circuit models for single
        ended port deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:DEEMbedding<Ph_pt>:PARameters
        :C<no>? CSL | LSC | CSC | SLC | SCL | SCC
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:DEEMbedding<Ph_pt>:PARameters
        :L<no>? CSL | LSC | LSL | SLC | SCL | SLL
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:DEEMbedding<Ph_pt>:PARameters
        :R<no>? CSL | LSC | CSC | LSL | SLC | SCL | SCC | SLL
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:EMBedding<Ph_pt>:PARameters:C
        <no> CSL? | LSC | CSC | SLC | SCL | SCC
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:EMBedding<Ph_pt>:PARameters:L
        <no> CSL? | LSC | LSL | SLC | SCL | SLL
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:EMBedding<Ph_pt>:PARameters:R
        <no> CSL? | LSC | CSC | LSL | SLC | SCL | SCC | SLL
        
        

   :param parameterType: Parameter type, capacitance, inductance orresistance.
   :param physicalPortNumber: Physical port number.

   :param functionType: Function type, deembedding or embedding.
   :param parameterNumber: Numberof capacitances, inductances or resistances in circuit model.
   :param circuitModel: This control defines thepossible circuit model.
   :param channel: Channel number.
   :return: value

.. method:: SetVirtualTransformSingleEndedCircuitModel(self, channel=1, functionType, physicalPortNumber, circuitModel)
           
        This function selects the circuit model for single ended port
        deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:DEEMbedding<Ph_pt>:TNDefiniti
        on
        FIMPort | CSL | LSC | CSC | LSL | SLC | SCL | SCC | SLL
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:EMBedding<Ph_pt>:TNDefinition
        FIMPort | CSL | LSC | CSC | LSL | SLC | SCL | SCC | SLL
        
        
        

   :param circuitModel: This control defines the possible circuit model.
   :param physicalPortNumber: Physical port number.

   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.

.. method:: GetVirtualTransformSingleEndedCircuitModel(self, channel=1, functionType, physicalPortNumber)
           
        This function returns the circuit model for single ended port
        deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:DEEMbedding<Ph_pt>:TNDefiniti
        on?
        CALCulate<Ch>:TRANsform:VNETworks:SENDed:EMBedding<Ph_pt>:TNDefinition
        ?
        
        

   :param physicalPortNumber: Physical port number.

   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :return: circuitModel

.. method:: LoadSingleEndedPortCircuitModelData(self, channel=1, functionType, physicalPortNumber, fileName)
           
        This function loads data from a specified two-port (*.sp2) Touchstone
        file defining the characteristics of the current embedded/deembedded
        single ended port circuit model. The single ended port circuit model
        involving file import (FIMPort) must be selected before using this
        function.
        
        Remote-control command(s):
        MMEMory:LOAD:VNETworks<Ch>:SENDed:EMBedding<Ph_pt> '<file_name>'
        MMEMory:LOAD:VNETworks<Ch>:SENDed:DEEMbedding<Ph_pt> '<file_name>'
        
        
        

   :param physicalPortNumber: Physical port number.

   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :param fileName: This control specifies the name and directory of theloaded Touchstone file. If no path is specified the analyzer searchesthe current directory, to be queried with MMEMory:CDIRectory?.

.. method:: LoadAndInterchangeSingleEndedPortCircuitModelData(self, channel=1, functionType, physicalPortNumber, fileName)
           
        This function loads data from a specified two-port (*.sp2) Touchstone
        file defining the characteristics of the current embedded/deembedded
        single ended port circuit model. The single ended port circuit model
        involving file import (FIMPort) must be selected before using this
        function.
        
        Remote-control command(s):
        MMEMory:LOAD:VNETworks<Ch>:SENDed:EMBedding<Ph_pt> '<file_name>',IPORt
        MMEMory:LOAD:VNETworks<Ch>:SENDed:DEEMbedding<Ph_pt>
        '<file_name>',IPORt
        
        

   :param physicalPortNumber: Physical port number.

   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :param fileName: This control specifies the name and directory of theloaded Touchstone file. If no path is specified the analyzer searchesthe current directory, to be queried with MMEMory:CDIRectory?.

.. method:: SetVirtualTransformGroundLoopState(self, channel=1, functionType, state)
           
        This function enables or disables the deembedding/embedding function
        for ground loops. It is allowed to change the circuit model and its
        parameters while deembedding is enabled.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:DEEMbedding[:STATe] ON | OFF
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:EMBedding[:STATe] ON | OFF
        
        

   :param state: Thiscontrol enables or disables the deembedding function for ground loop.
   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.

.. method:: GetVirtualTransformGroundLoopState(self, channel=1, functionType)
           
        This function returns the state of the deembedding/embedding function
        for ground loops. It is allowed to change the circuit model and its
        parameters while deembedding is enabled.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:DEEMbedding[:STATe]?
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:EMBedding[:STATe]?
        
        

   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :return: state

.. method:: SetVirtualTransformGroundLoop(self, channel=1, functionType, parameterType, circuitModel, groundLoopValue)
           
        This function specifies the capacitance C, inductance L or resistance
        R value in the different circuit models for ground loop
        deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:C SC,
        <capacitance>
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:L SL,
        <inductance>
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:R SC |
        SL, <resistance>
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:EMBedding:PARameters:C
        SC,<capacitance>
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:EMBedding:PARameters:L SL,
        <inductance>
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:EMBedding:PARameters:R SC |
        SL,<resistance>
        
        

   :param parameterType: Parameter type, capacitance, inductance or resistance.

   :param circuitModel: Thiscontrol defines the possible circuit model.
   :param functionType: Function type, deembedding or embedding.
   :param groundLoopValue: Capacitance C, Inductance L or Resistance Rfor the specified circuit model.
   :param channel: Channel number.

.. method:: GetVirtualTransformGroundLoop(self, channel=1, functionType, parameterType, circuitModel)
           
        This function returns the capacitance C, inductance L or resistance R
        value in the different circuit models for ground loop
        deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:C? SC
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:L? SL
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:R? SC |
        SL
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:EMBedding:PARameters:C? SC
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:EMBedding:PARameters:L? SL
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:EMBedding:PARameters:R? SC |
        SL
        
        

   :param parameterType: Parameter type, capacitance, inductance or resistance.

   :param circuitModel: Thiscontrol defines the possible circuit model.
   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :return: groundLoopValue

.. method:: SetVirtualTransformGroundLoopCircuitModel(self, channel=1, functionType, circuitModel)
           
        This function selects the circuit model for ground loop
        deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:DEEMbedding:TNDefinition
        FIMPort | SL | SC
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:EMBedding:TNDefinition FIMPort
        | SL | SC
        
        
        

   :param circuitModel: Thiscontrol defines the possible circuit model.
   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.

.. method:: GetVirtualTransformGroundLoopCircuitModel(self, channel=1, functionType)
           
        This function returns the circuit model for ground loop
        deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:DEEMbedding:TNDefinition?
        CALCulate<Ch>:TRANsform:VNETworks:GLOop:EMBedding:TNDefinition?
        
        
        

   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :return: circuitModel

.. method:: LoadGroundLoopCircuitModelData(self, channel=1, functionType, fileName)
           
        This function loads data from a specified one-port (*.s1p) Touchstone
        file defining the characteristics of the current embedded/deembedded
        ground loop circuit model. The ground loop circuit model involving
        file import (FIMPort) must be selected before using this function.
        
        Remote-control command(s):
        MMEMory:LOAD:VNETworks<Ch>:GLOop:DEEMbedding<Ph_pt> '<file_name>'
        MMEMory:LOAD:VNETworks<Ch>:GLOop:EMBedding<Ph_pt> '<file_name>'
        
        

   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :param fileName: Thiscontrol specifies the name and directory of the loaded Touchstonefile. If no path is specified the analyzer searches the currentdirectory, to be queried with MMEMory:CDIRectory?.

.. method:: SetVirtualTransformPortPairState(self, channel=1, functionType, portPair, state)
           
        This function enables or disables the deembedding/embedding function
        for for port pairs.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>[:STATe]
        <Boolean>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>[:STATe]
        <Boolean>
        
        
        

   :param portPair: Currentnumber of a port pair in the list.
   :param state: This control enables or disables the deembeddingfunction for port pair.
   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.

.. method:: GetVirtualTransformPortPairState(self, channel=1, functionType, portPair)
           
        This function queries the state of the deembedding/embedding function
        for for port pairs.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>[:STATe]?
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>[:STATe]?
        
        
        

   :param portPair: Currentnumber of a port pair in the list.
   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :return: state

.. method:: SetVirtualTransformPortPair(self, channel=1, functionType, portPair, parameterType, parameterNumber, circuitModel, value)
           
        This function specifies the capacitance, inductance or resistance
        values C1, C2, C3, L1, L2, L3 or R1, R2, R3 in the different circuit
        models for port pair deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>:PARamete
        rs:C<no> STSC | SCST | CSSL | LSSC | CSSC | SLCS | SCLS |
        SCCS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>:PARamete
        rs:L<no> STSL | SLST | CSSL | LSSC | LSSL | SLCS | SCLS |
        SLLS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>:PARamete
        rs:R<no> STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS
        | SCLS | SCCS | SLLS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>:PARameters
        :C<no> STSC | SCST | CSSL | LSSC | CSSC | SLCS | SCLS |
        SCCS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>:PARameters
        :L<no> STSL | SLST | CSSL | LSSC | LSSL | SLCS | SCLS |
        SLLS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>:PARameters
        :R<no> STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS |
        SCLS | SCCS | SLLS,<numeric_value>
        
        

   :param parameterType: Parameter type, capacitance,inductance or resistance.
   :param functionType: Function type, deembedding or embedding.
   :param value: Capacitance C<no>, Inductance L<no> or Resistance R<no>for the specified circuit model.
   :param portPair: Currentnumber of a port pair in the list.
   :param parameterNumber: Numberof capacitances, inductances or resistances in circuit model.
   :param circuitModel: This control definesthe possible circuit model.
   :param channel: Channel number.

.. method:: GetVirtualTransformPortPair(self, channel=1, functionType, portPair, parameterType, parameterNumber, circuitModel)
           
        This function queries the capacitance, inductance or resistance values
        C1, C2, C3, L1, L2, L3 or R1, R2, R3 in the different circuit models
        for port pair deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>:PARamete
        rs:C<no>? STSC | SCST | CSSL | LSSC | CSSC | SLCS | SCLS |
        SCCS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>:PARamete
        rs:L<no>? STSL | SLST | CSSL | LSSC | LSSL | SLCS | SCLS |
        SLLS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>:PARamete
        rs:R<no>? STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS
        | SCLS | SCCS | SLLS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>:PARameters
        :C<no>? STSC | SCST | CSSL | LSSC | CSSC | SLCS | SCLS |
        SCCS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>:PARameters
        :L<no>? STSL | SLST | CSSL | LSSC | LSSL | SLCS | SCLS |
        SLLS,<numeric_value>
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>:PARameters
        :R<no>? STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS |
        SCLS | SCCS | SLLS,<numeric_value>
        
        

   :param parameterType: Parameter type, capacitance,inductance or resistance.
   :param functionType: Function type, deembedding or embedding.
   :param portPair: Currentnumber of a port pair in the list.
   :param parameterNumber: Numberof capacitances, inductances or resistances in circuit model.
   :param circuitModel: This control definesthe possible circuit model.
   :param channel: Channel number.
   :return: value

.. method:: SetVirtualTransformPortPairCircuitModel(self, channel=1, functionType, portPair, circuitModel)
           
        This function selects the circuit model for port pair
        deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>:TNDefini
        tion
        FIMPort | STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS
        | SCLS | SCCS | SLLS
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>:TNDefiniti
        on
        FIMPort | STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS
        | SCLS | SCCS | SLLS
        
        

   :param portPair: Currentnumber of a port pair in the list.
   :param circuitModel: This control defines thepossible circuit model.
   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.

.. method:: GetVirtualTransformPortPairCircuitModel(self, channel=1, functionType, portPair)
           
        This function queries the circuit model for port pair
        deembedding/embedding.
        
        Remote-control command(s):
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:DEEMbedding<List_idx>:TNDefini
        tion?
        FIMPort | STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS
        | SCLS | SCCS | SLLS
        CALCulate<Ch>:TRANsform:VNETworks:PPAir:EMBedding<List_idx>:TNDefiniti
        on?
        FIMPort | STSL | STSC | SLST | SCST | CSSL | LSSC | CSSC | LSSL | SLCS
        | SCLS | SCCS | SLLS
        
        

   :param portPair: Currentnumber of a port pair in the list.
   :param functionType: Function type, deembedding or embedding.
   :param channel: Channel number.
   :return: circuitModel

.. method:: LoadPortPairCircuitModelData(self, channel=1, functionType, portPair, fileName, parameter, interchangePortNumbers)
           
        This function loads data from a specified Touchstone file defining the
        characteristics of the current embedded/deembedded port pair circuit
        model. A balanced port circuit model involving file import must be
        selected before using this function.
        
        Remote-control command(s):
        MMEMory:LOAD:VNETworks<Ch>:PPAir:EMBedding<List_idx> '<file_name>',
        PMAin | PSECondary
        MMEMory:LOAD:VNETworks<Ch>:PPAir:DEEMbedding<List_idx> '<file_name>',
        PMAin | PSECondary
        
        
        

   :param interchangePortNumbers: Interchange port numbers of loaded*.s2p file. If the parameter is omitted, the port numbers are notinterchanged. The parameter must not be used for 4-port files.
   :param functionType: Function type, deembedding or embedding.
   :param fileName: This control specifies the name anddirectory of the loaded Touchstone file. The balanced port circuitmodels STSL | STSC | SLST | SCST require two 2-port (*.s2p) files, tobe assigned to the different ports PMAin and PSECondary; the FIMPortmodel requires a single 4-port (*.s4p) file but no additional portassignment.
   :param portPair: Currentnumber of a port pair in the list.
   :param parameter: Port assignment for two 2-port (*.s2p) files.

   :param channel: Channel number.

.. method:: SetCoherentSignalState(self, channel=1, port, coherentSignal)
           
        This function qualifies whether the signal at port no. <Pt> is a
        coherent or a non-coherent signal.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        SOURce<Ch>:CMODe:PORT<Pt>[:STATe] ON | OFF
        
        

   :param coherentSignal: This control sets the coherent or non-coherent signal at port no. <Pt>.
   :param port: Port numbers of the analyzer.
   :param channel: Channel number.

.. method:: GetCoherentSignalState(self, channel=1, port)
           
        This function returns whether the signal at port no. <Pt> is a
        coherent or a non-coherent signal.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        SOURce<Ch>:CMODe:PORT<Pt>[:STATe]?
        
        

   :param port: Port numbers of the analyzer.
   :param channel: Channel number.
   :return: coherentSignal

.. method:: SetCoherentSignalAmplitude(self, channel=1, port, amplitude)
           
        This function defines the amplitude for the coherent signal at port no. <Pt> relative to the amplitude of the reference signal
        (SOURce<Ch>:CMODe:RPORt). The amplitude replaces the port amplitude as
        long as the port signal is selected as a coherent signal
        (SOURce<Ch>:CMODe:PORT<Pt>[:STATe] ON).
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        SOURce<Ch>:CMODe:PORT<Pt>:AMPLitude
        
        

   :param amplitude: This control defines the amplitude for the coherentsignal at port no. <Pt>
   :param port: Port numbers of the analyzer.
   :param channel: Channel number.

.. method:: GetCoherentSignalAmplitude(self, channel=1, port)
           
        This function returns the amplitude for the coherent signal at port no. <Pt> relative to the amplitude of the reference signal.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        SOURce<Ch>:CMODe:PORT<Pt>:AMPLitude?
        
        

   :param port: Port numbers of the analyzer.
   :param channel: Channel number.
   :return: amplitude

.. method:: SetCoherentSignalPhase(self, channel=1, port, phase)
           
        This function defines the phase for the coherent signal at port no.
        <Pt> relative to the phase of the reference signal
        (SOURce<Ch>:CMODe:RPORt).
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        SOURce<Ch>:CMODe:PORT<Pt>:PHASe
        
        

   :param phase: This control defines the phase for the coherent signalat port no. <Pt>
   :param port: Port numbers of the analyzer.
   :param channel: Channel number.

.. method:: GetCoherentSignalPhase(self, channel=1, port)
           
        This function returns the phase for the coherent signal at port no.
        <Pt> relative to the phase of the reference signal
        (SOURce<Ch>:CMODe:RPORt).
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        SOURce<Ch>:CMODe:PORT<Pt>:PHASe?
        
        

   :param port: Port numbers of the analyzer.
   :param channel: Channel number.
   :return: phase

.. method:: SetCoherentSignalReferencePort(self, channel=1, referencePort)
           
        This function selects the reference port for the Defined Coherence
        Mode.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        SOURce<Ch>:CMODe:RPORt
        
        

   :param channel: Channel number.
   :param referencePort: This control selects the reference port for theDefined Coherence Mode.

.. method:: GetCoherentSignalReferencePort(self, channel=1)
           
        This function returns the reference port of the Defined Coherence
        Mode.
        
        Note(s):
        
        (1) This function is only availably for ZVA or ZVT instruments.
        
        Remote-control command(s):
        SOURce<Ch>:CMODe:RPORt?
        
        

   :param channel: Channel number.
   :return: referencePort

.. method:: SetAlternateSweepMode(self, channel=1, alternateSweepMode)
           
        This function activates normal or alternate sweep mode.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]COUPle ALL | NONE
        
        

   :param alternateSweepMode: This control activates normal or alternatesweep mode.
   :param channel: Channel number.

.. method:: GetAlternateSweepMode(self, channel=1)
           
        This function returns the state of the alternate sweep mode.
        
        Note(s):
        
        (1) This function is available only on R&S ZVA instrument.
        
        Remote-control command(s):
        [SENSe<Ch>:]COUPle?
        
        

   :param channel: Channel number.
   :return: alternateSweepMode

.. method:: SetSpuriousAvoidance(self, channel=1, spuriousAvoidance)
           
        This function defines whether the analyzer measures with a local
        oscillator frequency LO below or above the RF input frequency.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:SBANd POSitive | NEGative | AUTO
        
        

   :param spuriousAvoidance: This control defines whether the analyzermeasures with a local oscillator frequency LO below or above the RFinput frequency..
   :param channel: Channel number.

.. method:: GetSpuriousAvoidance(self, channel=1)
           
        This function queries whether the analyzer measures with a local
        oscillator frequency LO below or above the RF input frequency.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:SBANd?
        
        

   :param channel: Channel number.
   :return: spuriousAvoidance

.. method:: SetAutomaticLevelControlState(self, ALCState)
           
        This function enables or disables the Automatic Level Control for all
        channels.
        
        Remote-control command(s):
        DIAGnostic:ALC:SETTings[:STATe] ON | OFF
        
        

   :param ALCState: This control enables ordisables the Automatic Level Control for all channels.

.. method:: GetAutomaticLevelControlState(self, )
           
        This function returns the state of the Automatic Level Control for all
        channels.
        
        Remote-control command(s):
        DIAGnostic:ALC:SETTings[:STATe]?
        
        

   :return: ALCState

.. method:: SetIndividualALCPortState(self, channel=1, port, state)
           
        Enables or disables individual ALC (Automatic Level Control) settings
        at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:CONTrol
        
        
        

   :param state: Enables (ON) or disables (OFF) individual ALCsettings.
   :param port: Port number
   :param channel: Channel number.

.. method:: GetIndividualALCPortState(self, channel=1, port)
           
        Returns the state of individual ALC (Automatic Level Control) settings
        at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:CONTrol?
        
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: state

.. method:: SetALCPortState(self, channel=1, port, state)
           
        Enables or disables ALC (Automatic Level Control) at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC[:STATe]
        
        
        

   :param state: Enables (ON) or disables (OFF) ALC.
   :param port: Port number
   :param channel: Channel number.

.. method:: GetALCPortState(self, channel=1, port)
           
        Returns the state of ALC (Automatic Level Control) at port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC[:STATe]?
        
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: state

.. method:: SetALCPortClamp(self, channel=1, port, clampState)
           
        Suspends the ALC mechanism at source port <Pt> while the analyzer
        acquires measurement data (Clamp ALC during Measurement).
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:CLAMp
        
        
        

   :param clampState: Suspends the ALC mechanism at source port <Pt>while the analyzer acquires measurement data (Clamp ALC duringMeasurement).
   :param port: Port number
   :param channel: Channel number.

.. method:: GetALCPortClamp(self, channel=1, port)
           
        Queries state of clamp ALC during Measurement.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:CLAMp?
        
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: clampState

.. method:: SetALCPortAUBWState(self, channel=1, port, state)
           
        Enables or disables automatic bandwidth setting for port <Pt> in
        channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:AUBW
        
        
        

   :param state: Enables or disables automatic bandwidth setting forport <Pt> in channel <Ch>.
   :param port: Port number
   :param channel: Channel number.

.. method:: GetALCPortAUBWState(self, channel=1, port)
           
        Queries automatic bandwidth setting for port <Pt> in channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:AUBW?
        
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: state

.. method:: SetALCPortBandwidth(self, channel=1, port, bandwidth)
           
        Selects the bandwidth in the ALC control loop for port <Pt> in channel
        <Ch>. The setting takes effect
        when automatic bandwidth setting is disabled (using
        rszvb_SetALCPortAUBWState).
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:BANDwidth
        
        
        

   :param bandwidth: Selects the bandwidth in the ALC control loop forport <Pt> in channel <Ch>.
   :param port: Port number
   :param channel: Channel number.

.. method:: GetALCPortBandwidth(self, channel=1, port)
           
        Returns the bandwidth in the ALC control loop for port <Pt> in channel
        <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:BANDwidth?
        
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: bandwidth

.. method:: SetALCPortCoupling(self, channel=1, state)
           
        Enforces identical ALC settings for the individual ports in channel
        <Ch>
        
        Remote-control command(s):
        SOURce<Ch>:POWer:ALC:COUPle
        
        
        

   :param state: Enforces identical settings (ON) or enables port-specific ALC settings (OFF).
   :param channel: Channel number.

.. method:: GetALCPortCoupling(self, channel=1)
           
        Returns the port coupling state.
        
        Remote-control command(s):
        SOURce<Ch>:POWer:ALC:COUPle?
        
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetALCChannelState(self, channel=1, state)
           
        Enables or disables ALC (Automatic Level Control) for channel <Ch>
        (ALC Off item in Power Bandwidth Average menu)
        
        Remote-control command(s):
        SOURce<Ch>:POWer:ALC:CSTate
        
        
        

   :param state: Enables (ON) or disables (OFF) ALC for channel <Ch>.
   :param channel: Channel number.

.. method:: GetALCChannelState(self, channel=1)
           
        Returns the ALC channel state.
        
        Remote-control command(s):
        SOURce<Ch>:POWer:ALC:CSTate?
        
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetALCLowPhaseNoiseMode(self, channel=1, state)
           
        Defines whether Low Phase Noise Mode shall be activated whenever ALC
        is used on a port in channel <Ch>
        
        Remote-control command(s):
        SOURce<Ch>:POWer:ALC:LPNoise
        
        
        

   :param state: Enables (ON) or disables (OFF) automatic activation ofLow Phase Noise Mode.
   :param channel: Channel number.

.. method:: GetALCLowPhaseNoiseMode(self, channel=1)
           
        Returns state of automatic activation of Low Phase Noise Mode.
        
        Remote-control command(s):
        SOURce<Ch>:POWer:ALC:LPNoise?
        
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetALCPortOffsetState(self, channel=1, port, state)
           
        Causes the analyzer to use the ALC of the previous measurement as an
        ALC start offset value for port <Pt> in channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:POFFset
        
        
        

   :param state: Use ALC Offset ... on or off.
   :param port: Port number
   :param channel: Channel number.

.. method:: GetALCPortOffsetState(self, channel=1, port)
           
        Causes the analyzer to use the ALC of the previous measurement as an
        ALC start offset value for port <Pt> in channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:POFFset
        
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: state

.. method:: SetALCPortControlRange(self, channel=1, port, controlRange)
           
        Defines the maximum change of the source signal level due to the ALC
        (Control Range in ALC Config dialog) for port <Pt> in channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:RANGe
        
        
        

   :param controlRange: Defines the maximum change of the source signallevel due to the ALC (Control Range in ALC Config dialog) for port <Pt> in channel <Ch>.
   :param port: Port number
   :param channel: Channel number.

.. method:: GetALCPortControlRange(self, channel=1, port)
           
        Returns the maximum change of the source signal level due to the ALC
        (Control Range in ALC Config dialog) for port <Pt> in channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:RANGe?
        
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: controlRange

.. method:: SetALCPortStartOffset(self, channel=1, port, startOffset)
           
        Defines the signal level before the ALC loop is started (Start Value >
        Offset in ALC Config dialog) for port <Pt> in channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:SOFFset
        
        
        

   :param startOffset: Sets the signal level before the ALC loop isstarted (Start Value > Offset in ALC Configdialog) for port <Pt> in channel <Ch>.
   :param port: Port number
   :param channel: Channel number.

.. method:: GetALCPortStartOffset(self, channel=1, port)
           
        Returns the signal level before the ALC loop is started (Start Value >
        Offset in ALC Config dialog) for port <Pt> in channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:SOFFset?
        
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: startOffset

.. method:: SetALCPortSettingTolerance(self, channel=1, port, settingTolerance)
           
        Defines the variation of the ALC-controlled source signal level
        (Settling Tolerance in ALC Config dialog) for port <Pt> in channel
        <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:STOLerance
        
        
        

   :param settingTolerance: Defines the variation of the ALC-controlledsource signal level (Settling Tolerance in ALC Config dialog) for port <Pt> in channel <Ch>.
   :param port: Port number
   :param channel: Channel number.

.. method:: GetALCPortSettingTolerance(self, channel=1, port)
           
        Returns the variation of the ALC-controlled source signal level
        (Settling Tolerance in ALC Config dialog) for port <Pt> in channel
        <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:STOLerance?
        
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: settingTolerance

.. method:: SetLowPhaseNoiseState(self, channel=1, lowPhaseNoiseState)
           
        This function enables or disables the Low Phase Noise function.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:LPNoise <Boolean>
        
        

   :param lowPhaseNoiseState: This control enables or disables the LowPhase Noise function.
   :param channel: Channel number.

.. method:: GetLowPhaseNoiseState(self, channel=1)
           
        This function returns the state of the Low Phase Noise function.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:LPNoise <Boolean>
        
        

   :param channel: Channel number.
   :return: lowPhaseNoiseState

.. method:: ConfigurePortPIController(self, channel=1, port, PIControllerMode, gain, integrationTime)
           
        Configures PI controller parameters at source port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:PIParameter
        SOURce<Ch>:POWer<Pt>:ALC:PIParameter:GAIN
        SOURce<Ch>:POWer<Pt>:ALC:PIParameter:ITIMe
        
        

   :param PIControllerMode: Enables automatic or manual setting of the PIcontroller parameters at source port <Pt>.
   :param integrationTime: Defines the integrationtime of the PI controller at source port <Pt>. This setting takeseffect when manual setting of the controller parameters is enabled
   :param port: Port number
   :param channel: Channel number.
   :param gain: Defines theproportional gain of the PI controller at source port <Pt>. Thissetting takes effect when manual setting of the controller parametersis enabled.

.. method:: ConfigureSAWMatchingNetwork(self, channel=1, apply, parallelL, serialC, differentialModeImpedance, commonModeImpedance)
           
        This function configures SAW Matching Network parameters.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:STATe ON | OFF
        CALCulate<Ch>:FSIMulator:BALun:DMCircuit:BPORt2:PARameters:L
        CALCulate<Ch>:FSIMulator:BALun:DMCircuit:BPORt2:PARameters:C
        CALCulate<Ch>:FSIMulator:BALun:DZConversion:BPORt2:ZDIFferent[:R]
        CALCulate<Ch>:FSIMulator:BALun:DZConversion:BPORt2:ZCOMmon[:R]
        
        

   :param differentialModeImpedance: Thiscontrol defines the differential mode impedance for the selectedbalanced port.
   :param commonModeImpedance: This control defines the common modeimpedance for the selected balanced port.
   :param serialC: This control defines theserial capacitance for the matching network.
   :param apply: This control activates or deactivates the virtualmatching network.
   :param parallelL: This control defines a delay time between thetrigger event and the start of the measurement.
   :param channel: Channel number.

.. method:: SetSAWState(self, channel=1, apply)
           
        This function activates or deactivates the virtual matching network.
        When the network is activated, port 1 serves as an unbalanced port,
        the physical ports no. 2 and 3 of the analyzer are combined to a
        logical (balanced) port no. 2.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:STATe ON | OFF
        
        

   :param apply: This control activates or deactivates the virtualmatching network.
   :param channel: Channel number.

.. method:: GetSAWState(self, channel=1)
           
        This function queries the state of the virtual matching network.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:STATe?
        
        

   :param channel: Channel number.
   :return: apply

.. method:: SetSAWParallelL(self, channel=1, parallelL)
           
        This function defines the parallel inductance for the matching
        network.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:BALun:DMCircuit:BPORt2:PARameters:L
        
        

   :param parallelL: This control defines a delay time between thetrigger event and the start of the measurement.
   :param channel: Channel number.

.. method:: GetSAWParallelL(self, channel=1)
           
        This function queries the parallel inductance for the matching
        network.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:BALun:DMCircuit:BPORt2:PARameters:L?
        
        

   :param channel: Channel number.
   :return: parallelL

.. method:: SetSAWSerialC(self, channel=1, serialC)
           
        This function defines the serial capacitance for the matching network.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:BALun:DMCircuit:BPORt2:PARameters:C
        
        

   :param serialC: This control defines the serial capacitance for thematching network.
   :param channel: Channel number.

.. method:: GetSAWSerialC(self, channel=1)
           
        This function queries the serial capacitance for the matching network.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:BALun:DMCircuit:BPORt2:PARameters:C?
        
        

   :param channel: Channel number.
   :return: serialC

.. method:: SetSAWSimulationType(self, channel=1, type)
           
        This function selects the type of matching network to be simulated.
        The present firmware version provides a virtual matching network for
        DUTs with a single-ended and a balanced port.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:BALun:DEVice SBALanced
        
        

   :param type: This control selects the type of matching network to besimulated.
   :param channel: Channel number.

.. method:: GetSAWSimulationType(self, channel=1)
           
        This function returns the type of matching network to be simulated.
        The present firmware version provides a virtual matching network for
        DUTs with a single-ended and a balanced port.
        
        Remote-control command(s):
        CALCulate<Ch>:FSIMulator:BALun:DEVice?
        
        

   :param channel: Channel number.
   :return: type

.. method:: SetPIControllerMode(self, channel=1, port, PIControllerMode)
           
        Enables automatic or manual setting of the PI controller parameters at
        source port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:PIParameter
        
        

   :param PIControllerMode: Enables automatic or manual setting of the PIcontroller parameters at source port <Pt>.
   :param port: Port number
   :param channel: Channel number.

.. method:: GetPIControllerMode(self, channel=1, port)
           
        Queries the mode of the PI controller parameters at source port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:PIParameter?
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: PIControllerMode

.. method:: SetPIControllerGain(self, channel=1, port, gain)
           
        Defines the proportional gain of the PI controller at source port <Pt>. This setting takes effect when manual setting of the controller
        parameters is enabled.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:PIParameter:GAIN
        
        

   :param port: Port number
   :param channel: Channel number.
   :param gain: Defines the proportional gain of the PI controller atsource port <Pt>. This setting takes effect when manual setting of thecontroller parameters is enabled.

.. method:: GetPIControllerGain(self, channel=1, port)
           
        Queries the proportional gain of the PI controller at source port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:PIParameter:GAIN?
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: gain

.. method:: SetPIControllerIntegrationTime(self, channel=1, port, integrationTime)
           
        Defines the integration time of the PI controller at source port <Pt>.
        This setting takes effect when manual setting of the controller
        parameters is enabled
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:PIParameter:ITIMe
        
        

   :param integrationTime: Defines the integration time of the PIcontroller at source port <Pt>. This setting takes effect when manualsetting of the controller parameters is enabled
   :param port: Port number
   :param channel: Channel number.

.. method:: GetPIControllerIntegrationTime(self, channel=1, port)
           
        Returns the integration time of the PI controller at source port <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:ALC:PIParameter:ITIMe?
        
        

   :param port: Port number
   :param channel: Channel number.
   :return: integrationTime

.. method:: ChannelAdd(self, channel=1, channelName)
           
        This function creates channel and selects it as the active channel. It
        also assigns a name to channel number.
        
        Note(s):
        
        A channel created with CONFigure:CHANnel<Ch>[:STATe] ON can be
        configured but has no trace assigned so that no measurement can be
        initiated. Use CALCulate<Ch>:PARameter:SDEFine
        "<Trace_name>,"<Parameter>" to create a new channel and a new trace.
        
        Remote-control command(s):
        CONFigure:CHANnel<Ch>[:STATe] ON
        CONFigure:CHANnel<Ch>:NAME '<string>'
        
        

   :param channelName: Define channel name.
   :param channel: Channel number.

.. method:: ChannelAddTrace(self, window, window_Trace, channel=1, channelName, traceName)
           
        This function creates a new channel and a new trace, which is
        displayed in the selected existing diagram area. The new channel
        settings (including a possible channel calibration) is preset to the
        default settings; the trace is created with the default trace
        settings.
        
        Remote-control command(s):
        CONFigure:CHANnel<Ch>[:STATe] ON
        CONFigure:CHANnel<Ch>:NAME '<string>'
        CALCulate<Ch>:PARameter:SDEFine '<string>','S21'
        DISPlay:WINDow<Wnd>:STATe ON
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED '<string>'
        
        

   :param window: Number of the diagram area.
   :param channelName: Define channel name.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: ChannelAddTraceDiagramArea(self, window, window_Trace, channel=1, channelName, traceName)
           
        This function creates a new channel and a new trace, which is
        displayed in a new diagram area. The new channel settings (including a
        possible channel calibration) is preset to the default settings; the
        trace is created with the default trace settings.
        
        Remote-control command(s):
        CONFigure:CHANnel<Ch>[:STATe] ON
        CONFigure:CHANnel<Ch>:NAME '<string>'
        CALCulate<Ch>:PARameter:SDEFine '<string>', 'S21'
        DISPlay:WINDow<Wnd>:STATe ON
        DISPlay:WINDow<Wnd>:TRACe<WndTr>:FEED '<string>'
        
        

   :param window: Number of the diagram area.
   :param channelName: Define channel name.
   :param window_Trace: Trace number used to distinguish the traces ofthe same diagram area <Wnd>.
   :param channel: Channel number.
   :param traceName: Define trace name.

.. method:: ChannelDelete(self, channel=1)
           
        This function deletes the current channel including all traces
        assigned to the channel and removes all display elements related to
        the channel from the diagram area.
        
        Remote-control command(s):
        CONFigure:CHANnel<Ch>[:STATe] OFF
        
        

   :param channel: Channel number.

.. method:: ChannelList(self, catalog, bufferSize)
           
        This function returns the numbers and names of all channels in the
        current setup.
        
        Remote-control command(s):
        CONFigure:CHANnel<Ch>:CATalog?
        
        

   :param catalog: Returns string with comma-separated list of channel numbers and names. If all channels have beendeleted the response is an empty string ("").
   :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.

.. method:: ChannelGetChannelName(self, channel=1, channelName)
           
        This function returns the channel <ch> name.
        
        Remote-control command(s):
        CONFigure:CHANnel<Ch>:NAME?
        
        

   :param channelName: Returns the channel name.
   :param channel: Channel number.

.. method:: ChannelGetChannelNumber(self, channelName)
           
        This function returns the channel number (numeric suffix) of a channel
        with known channel name. A channel name must be assigned before.
        
        Remote-control command(s):
        CONFigure:CHANnel:NAME:ID? '<Ch_name>'
        
        

   :param channelName: Sets the channel name.
   :return: channelNumber

.. method:: ChannelSetActive(self, channel=1)
           
        This function selects a channel <Ch> as the active channel.
        
        Remote-control command(s):
        INSTrument:NSELect <Ch>
        
        

   :param channel: Channel number.

.. method:: ChannelGetActive(self, )
           
        This function returns a channel <Ch> as the active channel.
        
        Remote-control command(s):
        INSTrument:NSELect?
        
        

   :return: channel

.. method:: ChannelRename(self, channel=1, channelName)
           
        This function assigns a name to channel number. The channel must be
        created before. Moreover it is not possible to assign the same name to
        two different channels.
        
        Remote-control command(s):
        CONFigure:CHANnel<Ch>:NAME '<Ch_name>'
        
        

   :param channelName: Assigns a name to channel number.
   :param channel: Channel number.

.. method:: SetConnector(self, channel=1, port, connector)
           
        This function selects a connector type at a specified port <Port> and
        its gender.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:CONNection<port_no> N50FEMALE | N50MALE
        | N75FEMALE | N75MALE | PC7 | PC35FEMALE | PC35MALE | PC292FEMALE |
        PC292MALE | UFEMALE1 | UMALE1 | UFEMALE2 | UMALE2 | SMAFEMALE |
        SMAMALE | PC1FEMALE | PC1MALE | PC185FEMALE | PC185MALE | PC24FEMALE |
        PC24MALE
        
        

   :param connector: This control selects a connector type at a specifiedport <Port> and its gender.
   :param port: Port numbers of the analyzer.
   :param channel: Channel number.

.. method:: GetConnector(self, channel=1, port)
           
        This function queries a connector type at a specified port <Port> and
        its gender.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:CONNection<port_no>?
        
        

   :param port: Port numbers of the analyzer.
   :param channel: Channel number.
   :return: connector

.. method:: SetSameConnectorTypeAtAllPorts(self, channel=1, sameConnectorAtAllPorts)
           
        This function qualifies whether the connector types at the analyzer
        ports (but not their gender) are equal or independent.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:CONNection:PORTs ALL | SINGle
        
        

   :param sameConnectorAtAllPorts: This control qualifies whether theconnector types at the analyzer ports (but not their gender) are equalor independent.
   :param channel: Channel number.

.. method:: GetSameConnectorTypeAtAllPorts(self, channel=1)
           
        This function queries whether the connector types at the analyzer
        ports (but not their gender) are equal or independent.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:CONNection:PORTs?
        
        

   :param channel: Channel number.
   :return: sameConnectorAtAllPorts

.. method:: SetSameConnectorGenderAtAllPorts(self, channel=1, sameGenderAtAllPorts)
           
        This function qualifies whether the connector genders at the analyzer
        ports (but not their types) are equal or independent.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:CONNection:GENDers ALL | SINGle
        
        

   :param sameGenderAtAllPorts: This control qualifies whether theconnector genders at the analyzer ports (but not their types) areequal or independent.
   :param channel: Channel number.

.. method:: GetSameConnectorGenderAtAllPorts(self, channel=1)
           
        This function quries whether the connector genders at the analyzer
        ports (but not their types) are equal or independent.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:CONNection:GENDers?
        
        

   :param channel: Channel number.
   :return: sameGenderAtAllPorts

.. method:: SetUserConnector(self, channel=1, port, connector, connectorGender)
           
        This function selects a user-defined connector type at a specified
        port <Port> and its gender.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:SCONnection<port_no> '<conn_name>',
        MALE | FEMale
        
        

   :param connector: This control selects a connector type at aspecified port <Port> and gender.
   :param connectorGender: This control selects theconnector gender.
   :param port: Port numbers of the analyzer.
   :param channel: Channel number.

.. method:: GetUserConnector(self, channel=1, port, connector)
           
        This function retuns a user-defined connector type at a specified port <Port> and its gender.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:SCONnection<port_no>?
        
        

   :param connector: This control returns a connector type at aspecified port <Port> and gender. connectorGender ViInt32 This controlreturns the connector gender.
   :param port: Port numbers of the analyzer.
   :param channel: Channel number.
   :return: connectorGender

.. method:: SetSameSweepSetup(self, channel=1, sameSweepSetup)
           
        This function selects the sweep setup for the calibration sweeps. This
        setting is valid for manual and automatic calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:CSETup
        
        

   :param sameSweepSetup: This control selects the sweep setup for thecalibration sweeps.
   :param channel: Channel number.

.. method:: GetSameSweepSetup(self, channel=1)
           
        This function returns the sweep setup for the calibration sweeps.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:CSETup?
        
        

   :param channel: Channel number.
   :return: sameSweepSetup

.. method:: SetSParameterDetector(self, channel=1, sParameterDetector)
           
        This function selects the S-parameter detector type during the
        calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:DETector NORMal | AVERage
        
        

   :param sParameterDetector: This control selects a S-parameterdetector.
   :param channel: Channel number.

.. method:: GetSParameterDetector(self, channel=1)
           
        This function selects the S-parameter detector type during the
        calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:DETector?
        
        

   :param channel: Channel number.
   :return: sParameterDetector

.. method:: SelectCalibrationType(self, channel=1, calibrationName, parameters, port1, port2, port3, port4)
           
        This function selects a one-port, two-port, three-port or four-port
        calibration type at arbitrary analyzer ports.
        
        Note(s):
        
        (1) For an n-port calibration type (n = 1 to 4), n port numbers must
        be specified. If more than n numbers are defined, the spare numbers
        (the last in the list) are ignored.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:METHod:DEFine '<cal_name>', REFL |
        RSHort | FOPort | FRTRans | OPTPort | TOSM | TOM | TRM | TRL | TNA,
        UOSM, FTRans, RTRans <port_no>[,<port_no>][,<port_no>][,<port_no>]
        
        

   :param port4: Port number.
   :param parameters: This control selects acalibration type.
   :param calibrationName: This control defines the name of thecalibration (string parameter). The name serves as a reference todelete a particular set of system correction data.
   :param port2: Port number.
   :param port3: Port number.
   :param channel: Channel number.
   :param port1: Port number.

.. method:: GetCalibrationType(self, channel=1)
           
        This function returns the current calibration type. Returns the
        calibration type and the port numbers valid for that calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:METHod:DEFine?
        
        

   :param channel: Channel number.
   :return: calibrationType
   :return: port1
   :return: port2
   :return: port3
   :return: port4

.. method:: StartCalibration(self, channel=1, standard, port1, port2)
           
        This function starts a calibration measurement in order to acquire
        measurement data for the selected standards. The
        standards are reflection or transmission standards and can be
        connected to arbitrary analyzer ports.
        
        Note(s):
        
        (1) OSHort: Available with firmware version 2.10 and higher.
        
        (2) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        (3) LINE3 adn SLIDe: Available with firmware version 2.40 and higher.
        
        (4)ISOLation: Available with firmware version 2.78 and higher.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect[:ACQuire]:SELected THRough | OPEN |
        SHORt | MATCh | NET | ATT | REFL | LINE | LINE2 | OSHort | LINE3 |
        SLIDe | OSHORT2 | OSHORT3 | ISOLation,<port_no>[,<port_no>]
        
        

   :param port1: Port number.
   :param port2: Port number.
   :param channel: Channel number.
   :param standard: This control selects a standard from the selectedcalibration kit.

.. method:: StartCalibrationLine(self, channel=1, line, port1, port2)
           
        This function starts a calibration measurement in order to acquire
        measurement data for the selected line.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect[:ACQuire]:SELected LINEN,<line>
        <port_no>[,<port_no>]
        
        

   :param line: Selects line.
   :param port2: Port number.
   :param channel: Channel number.
   :param port1: Port number.

.. method:: StartCalibrationWithOptions(self, channel=1, standard, port1, port2, dispersion, delayPhase, delayPhaseValue)
           
        This function starts a calibration measurement in order to acquire
        measurement data for the selected standards. The
        standards are reflection or transmission standards and can be
        connected to arbitrary analyzer ports.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        (2) This function is available with firmware version 2.40 and higher.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect[:ACQuire]:SELected
        UTHRough,<port_no>,<port_no>[,<Dispersion>,AUTO | <delay | phase>]
        
        
        

   :param delayPhase: This controle selects automaticor manual settings of delay time and phase.
   :param delayPhaseValue: This control sets the delay time or phase,depending on the Dispersion settings.
   :param standard: This control selects a standard from the selectedcalibration kit.
   :param dispersion: This control selects if unknownthrough standard is non-dispersive or dispersive.
   :param port2: Port number.
   :param channel: Channel number.
   :param port1: Port number.

.. method:: SetCalibrationReferencePlaneShift(self, channel=1, referencePlaneShift)
           
        This function specifies the reference plane shift to be applied to the
        result of a NIST Multiline TRL calibration. The <value> is entered as
        a mechanical length, where positive values denote a transformation
        towards the DUT, and negative values towards the connector.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:RPSHift
        
        

   :param referencePlaneShift: This control sets the reference planeshift in meters (mechanical length).
   :param channel: Channel number.

.. method:: GetCalibrationReferencePlaneShift(self, channel=1)
           
        This function returns the reference plane shift to be applied to the
        result of a NIST Multiline TRL calibration. The <value> is entered as
        a mechanical length, where positive values denote a transformation
        towards the DUT, and negative values towards the connector.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:RPSHift?
        
        

   :param channel: Channel number.
   :return: referencePlaneShift

.. method:: SetCalibrationReferencePlaneShiftSpecific(self, channel=1, referencePlaneShift, calibrationName)
           
        This function specifies the reference plane shift that is applied to
        the specified calibration only.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:RPSHift
        
        

   :param calibrationName: This control defines thename of the calibration (string parameter).
   :param referencePlaneShift: This control sets the reference planeshift in meters (mechanical length).
   :param channel: Channel number.

.. method:: GetCalibrationReferencePlaneShiftSpecific(self, channel=1, calibrationName)
           
        This function returns the reference plane shift to be used for the
        specified calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:RPSHift?
        
        

   :param calibrationName: This control defines the name of thecalibration (string parameter).
   :param channel: Channel number.
   :return: referencePlaneShift

.. method:: QueryCalibrationReferencePlaneShift(self, channel=1, calibrationIndex)
           
        This function returns the reference plane shift to be applied to the
        result of a NIST Multiline TRL calibration. The <value> is entered as
        a mechanical length, where positive values denote a transformation
        towards the DUT, and negative values towards the connector.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter<Cal>? RPSHift
        
        

   :param calibrationIndex: This control sets the calibration index.
   :param channel: Channel number.
   :return: referencePlaneShift

.. method:: SaveCalibrationData(self, channel=1)
           
        This function calculates the system error correction data from the
        acquired one or two-port measurement results (rszvb_StartCalibration),
        stores them and applies them to the calibrated channel. To avoid
        incompatibilities, older system error correction data is deleted
        unless it has been transferred into a cal pool
        (MMEMory:STORe:CORRection <Ch>, '<file_name>').
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:SAVE:SELected
        
        

   :param channel: Channel number.

.. method:: GenerateDefaultCalibrationData(self, channel=1)
           
        This function generates a set of default system error correction data
        for the selected ports and calibration type. The default data set
        corresponds to a test setup which does not introduce any systematic
        errors.
        
        Note(s):
        
        (1) The main purpose of the default correction data set is to provide
        a dummy system error correction which you can replace with your own,
        external correction data. You may have acquired the external data in a
        previous session or even on an other instrument. If you want to use
        the external correction data on the analyzer, simply generate the
        default data set corresponding to your port configuration and
        calibration type and overwrite the default data
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:SAVE:SELected:DEFault
        
        

   :param channel: Channel number.

.. method:: DeleteCalibrationData(self, channel=1, calibrationName)
           
        This function deletes system error correction data generated and
        stored previously.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:DELete
        
        

   :param calibrationName: This control defines the name of thecalibration (string parameter) defined together with calibration type.If nothingis specified the analyzer deletes the last system error correctionstored by means of rszvb_SaveCalibrationData
   :param channel: Channel number.

.. method:: DeleteAllCalibrationData(self, channel=1)
           
        This function deletes all system error correction data generated and
        stored previously.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:DELete ALL
        
        

   :param channel: Channel number.

.. method:: ReadCalibrationData(self, channel=1, errorTermParameters, port1, port2, calibrationData)
           
        This function reads system error correction data for a specific
        channel, calibration method, and port combination <Port 1>, <Port 2>.
        
        Remote-control command(s):
        FORMat ASCII
        FORMat REAL,64
        SYSTem:COMMunicate:GPIB:SELF:RTERminator EOI
        [SENSe<Ch>:]CORRection:CDATa?
        
        

   :param errorTermParameters: This control sets the error termsparameters.
   :param port2: Port number.
   :param calibrationData: This control returns thecalibration data. For each sweep point (set byrszvb_SetSweepNumberOfPoints) real and imaginary part should beprovided.
   :param channel: Channel number.
   :param port1: Port number.

.. method:: WriteCalibrationData(self, channel=1, errorTermParameters, port1, port2, calibrationData)
           
        This function writes system error correction data for a specific
        channel, calibration method, and port combination <Port 1>, <Port 2>.
        
        Remote-control command(s):
        FORMat ASCII
        FORMat REAL,64
        SYSTem:COMMunicate:GPIB:SELF:RTERminator EOI
        [SENSe<Ch>:]CORRection:CDATa
        
        

   :param errorTermParameters: This control sets the error termsparameters.
   :param port2: Port number.
   :param calibrationData: This control defines thecalibration data. For each sweep point (set byrszvb_SetSweepNumberOfPoints) real and imaginary part should beprovided.
   :param channel: Channel number.
   :param port1: Port number.

.. method:: SetCorrectionState(self, channel=1, correctionState)
           
        This function enables or disables the system error correction for
        channel <Ch>.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection[:STATe] ON | OFF
        
        

   :param correctionState: This control enables (ON) or disables (OFF)the correction.
   :param channel: Channel number.

.. method:: GetCorrectionState(self, channel=1)
           
        This function returns the state of the system error correction for
        channel <Ch>.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection[:STATe]?
        
        

   :param channel: Channel number.
   :return: correctionState

.. method:: AcquireSourcePowerCalibration(self, channel=1, source, portNumber)
           
        This function selects the source for the source power calibration,
        starts and applies the source power calibration.
        
        Note(s):
        
        (1) The function cannot be used unless a power meter is connected via
        GPIB bus, USB or LAN interface and configured in the System - System
        Config - Configure External Power Meter
        
        (2) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection[:ACQuire] PORT | GENerator |
        CONVerter,<port_number>
        
        

   :param source: This control toggle between the analyzer port andexternal generator.
   :param portNumber: This control sets theanalyzer port, generator, or converter number.
   :param channel: Channel number.

.. method:: InitiateSourcePowerCalibration(self, channel=1, portNumber, externalPowerMeter)
           
        This function initiates a source power calibration for the source port
        <pt> using an external power meter no. 1 or 2.
        
        Notes:
        
        (1) The function cannot be used unless a power meter is connected via
        GPIB bus, USB or LAN interface and configured in the System - System
        Config - Configure External Power Meter
        
        (2) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect[:ACQuire] ASENsor | BSENsor
        
        

   :param externalPowerMeter: This control sets theexternal power meter.
   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.

.. method:: SetDummySourcePowerCalibrationState(self, dummySourcePowerCalibration)
           
        This function enables the analyzer to create a set of default source
        power calibration data. The analyzer uses the reference channel power
        to acquire the default calibration data. No external power meter is
        required.
        
        Notes:
        
        (1) The main purpose of the default calibration data set is to provide
        a dummy power calibration which you can replace with your own,
        external power calibration data. You may have acquired the external
        data in a previous session or even on an other instrument. If you want
        to use the external power calibration data on the analyzer, generate
        the default data set first and overwrite it with the external data.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DEFault ON | OFF
        
        

   :param dummySourcePowerCalibration: This controlenables (ON) or disables (OFF) the dummy source power calibration forport number <Pt>. OFF means that a real source power calibration isperformed, for which an external power meter must be connected to theanalyzer.

.. method:: GetDummySourcePowerCalibrationState(self, )
           
        This function returns whether dummy or real source power calibration
        is selected
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DEFault?
        
        

   :return: dummySourcePowerCalibration

.. method:: SetSourcePowerCalibrationPortState(self, channel=1, portNumber, portState)
           
        This function enables or disables the source power calibration for
        channel <Ch> and for port number <Pt>.
        
        Notes:
        
        (1) The command is disabled unless a source power calibration for the
        analyzer port has been performed
        (rszvb_InitiateSourcePowerCalibration).
        
        (2) To enable or disable a source power calibration for an external
        generator use SOURce<Ch>:POWer<Pt>:CORRection:GENerator[:STATe].
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection[:STATe] ON | OFF
        
        

   :param portNumber: This control sets the calibrated port number.
   :param portState: This control enables (ON) ordisables (OFF) the source power calibration for port number.
   :param channel: Channel number.

.. method:: GetSourcePowerCalibrationPortState(self, channel=1, portNumber)
           
        This function returns the state of the source power calibration for
        channel <Ch> and for port number <Pt>.
        
        Notes:
        
        (1) The command is disabled unless a source power calibration for the
        analyzer port has been performed
        (rszvb_InitiateSourcePowerCalibration).
        
        (2) To enable or disable a source power calibration for an external
        generator use SOURce<Ch>:POWer<Pt>:CORRection:GENerator[:STATe].
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection[:STATe]?
        
        

   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.
   :return: portState

.. method:: SetSourcePowerCalibrationGeneratorState(self, channel=1, portNumber, generatorState)
           
        This function enables or disables the source power calibration for
        channel <Ch> and for an external generator number <Pt>.
        
        Notes:
        
        (1) The command is disabled unless a source power calibration for the
        external generator has been performed
        (rszvb_AcquireSourcePowerCalibration).
        
        (2) To enable or disable a source power calibration for an analyzer
        port use (rszvb_SetSourcePowerCalibrationPortState).
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:GENerator[:STATe] ON | OFF
        
        

   :param generatorState: This control enables (ON) ordisables (OFF) the source power calibration for an external generator.
   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.

.. method:: GetSourcePowerCalibrationGeneratorState(self, channel=1, portNumber)
           
        This function returns the state of the source power calibration for
        channel <Ch> and for an external generator number <Pt>.
        
        Notes:
        
        (1) The command is disabled unless a source power calibration for the
        external generator has been performed
        (rszvb_AcquireSourcePowerCalibration).
        
        (2) To enable or disable a source power calibration for an analyzer
        port use (rszvb_SetSourcePowerCalibrationPortState).
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:GENerator[:STATe]?
        
        

   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.
   :return: generatorState

.. method:: SetVerificationSweepState(self, channel=1, verificationSweep)
           
        This function enables or disables a verification sweep that the
        analyzer performs after the source power calibration. The command is
        valid for all ports and external generators.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect[:ACQuire]:VERification[:STATe]
        ON | OFF
        
        

   :param verificationSweep: This control enables (ON) or disables(OFF) the verification sweep.
   :param channel: Channel number.

.. method:: GetVerificationSweepState(self, channel=1)
           
        This function returns the verification sweep state. The command is
        valid for all ports and external generators.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect[:ACQuire]:VERification[:STATe]
        ?
        
        

   :param channel: Channel number.
   :return: verificationSweep

.. method:: QueryVerificationSweepResults(self, )
           
        This function returns the result of the last verification sweep.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        (2) This function requires an enabled verification sweep - set with
        function rszvb_SetVerificationSweepState.
        
        (3) If no verification sweep result is available, the function returns
        RSZVB_ERROR_INSTRUMENT_DATA_NOT_AVAILABLE.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection[:ACQuire]:VERification:RESult?
        
        

   :return: calibrationPassed
   :return: maxOffset

.. method:: GeneratorPowerCalibrationHarmonic(self, channel=1)
           
        This function starts the source calibration (1st power calibration
        step for harmonic measurements), stores and applies the calibration
        data.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        (2) This function is available only on R&S ZVA and ZVT instrument with
        K4 option installed.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer:CORRection:HARMonic[:ACQuire]
        
        

   :param channel: Channel number.

.. method:: SetSourcePowerCalibrationState(self, calibrationState)
           
        This function enables or disables the source power calibration.
        
        Notes:
        
        (1) It is not possible to disable flatness calibration and the
        reference receiver calibration simultaneously.
        
        Remote-control command(s):
        SOURce<Ch>:POWer:CORRection:COLLect:FLATness ON | OFF
        
        
        

   :param calibrationState: This control enables(ON) or disables (OFF) the flatness calibration. With disabledflatness calibration, only one calibration sweep is performed in orderto calibrate the reference receiver; the previous source calibrationdata is not overwritten.

.. method:: GetSourcePowerCalibrationState(self, )
           
        This function returns the state of the source power calibration.
        
        
        Notes:
        
        (1) It is not possible to disable flatness calibration and the
        reference receiver calibration simultaneously.
        
        Remote-control command(s):
        SOURce<Ch>:POWer:CORRection:COLLect:FLATness?
        
        

   :return: calibrationState

.. method:: SetReferenceReceiverCalibrationState(self, calibrationState)
           
        This function enables or disables calibration of the reference
        receiver together with the source power calibration.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer:CORRection:COLLect:RRECeiver ON | OFF
        
        

   :param calibrationState: This control enables(ON) or disables (OFF) reference receiver calibration.

.. method:: GetReferenceReceiverCalibrationState(self, )
           
        This function returns the state of the reference receiver calibration.
        
        Remote-control command(s):
        SOURce<Ch>:POWer:CORRection:COLLect:RRECeiver?
        
        

   :return: calibrationState

.. method:: ModifySourcePowerCalibrationSettings(self, channel=1, portNumber, numberOfReadings, tolerance, otherSourcesState, portPowerOffset, offsetParameter, calibrationPowerOffset)
           
        This function configures the source power calibration settings
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:NREadings <readings>
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:AVERage:NTOLerance <tolerance>
        SOURce<Ch>:POWer<Pt>:CORRection:OSOurces[:STATe] ON | OFF
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]:OFFSet <numeric_value>, ONLY
        | CPADd
        SOURce<Ch>:POWer<Pt>:CORRection:LEVel:OFFSet <numeric_value>
        
        

   :param calibrationPowerOffset: This control sets the calibration power offset.
   :param numberOfReadings: This control sets the numberof readings.
   :param portPowerOffset: This control setsthe port-specific power offset.
   :param offsetParameter: This control sets the offsetparameter.
   :param otherSourcesState: This control switches offall other sources during the calibration sweep for channel <Ch>.
   :param portNumber: This control sets the calibrated port number.
   :param tolerance: This control sets the tolerance value.
   :param channel: Channel number.

.. method:: SetNumberOfReadings(self, channel=1, numberOfReadings)
           
        This function sets a limit for the number of calibration sweeps in the
        source power calibration. The command is valid for all ports and
        external generators. Equivalent command:
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:AVERage[:COUNt].
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:NREadings <readings>
        
        

   :param numberOfReadings: This control sets the number of readings.
   :param channel: Channel number.

.. method:: GetNumberOfReadings(self, channel=1)
           
        This function returns a limit for the number of calibration sweeps in
        the source power calibration. The command is valid for all ports and
        external generators. Equivalent command:
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:AVERage[:COUNt]?.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:NREadings?
        
        

   :param channel: Channel number.
   :return: numberOfReadings

.. method:: SetTolerance(self, channel=1, tolerance)
           
        This function specifies the maximum deviation of the measured power
        from the target power of the calibration.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:AVERage:NTOLerance <tolerance>
        
        

   :param tolerance: This control sets the tolerance value.
   :param channel: Channel number.

.. method:: GetTolerance(self, channel=1)
           
        This function returns the maximum deviation of the measured power from
        the target power of the calibration.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:AVERage:NTOLerance?
        
        

   :param channel: Channel number.
   :return: tolerance

.. method:: SetOtherSourcesState(self, channel=1, otherSources)
           
        This function switches off all other sources during the calibration
        sweep for channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:OSOurces[:STATe] ON | OFF
        
        

   :param otherSources: This control switches off all other sourcesduring the calibration sweep for channel <Ch>.
   :param channel: Channel number.

.. method:: GetOtherSourcesState(self, channel=1)
           
        This function returns the state of all other sources during the
        calibration sweep for channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:OSOurces[:STATe]?
        
        

   :param channel: Channel number.
   :return: otherSources

.. method:: SetPortPowerOffset(self, channel=1, portNumber, portPowerOffset, offsetParameter)
           
        This function defines a port-specific source power or a power offset
        relative to the channel power.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]:OFFSet <numeric_value>, ONLY
        | CPADd
        
        

   :param offsetParameter: This control sets the offsetparameter.
   :param portPowerOffset: This control sets the port-specific power offset.
   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.

.. method:: GetPortPowerOffset(self, channel=1, portNumber)
           
        This function returns a port-specific source power or a power offset
        relative to the channel power.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]:OFFSet <numeric_value>, ONLY
        | CPADd
        
        

   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.
   :return: portPowerOffset
   :return: offsetParameter

.. method:: SetCalibrationPowerOffset(self, channel=1, portNumber, calibrationPowerOffset)
           
        This function specifies a gain (positive values) or an attenuation
        (negative values) in the signal path between the source port and the
        calibrated reference plane. The value has no impact on the source
        power.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:LEVel:OFFSet <numeric_value>
        
        

   :param calibrationPowerOffset: This control sets thecalibration power offset.
   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.

.. method:: GetCalibrationPowerOffset(self, channel=1, portNumber)
           
        This function returns a gain (positive values) or an attenuation
        (negative values) in the signal path between the source port and the
        calibrated reference plane.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:LEVel:OFFSet?
        
        

   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.
   :return: calibrationPowerOffset

.. method:: SetCalibrationPowerGeneratorOffset(self, channel=1, portNumber, generatorNumber, calPowerGeneratorOffset)
           
        This function specifies a gain (positive values) or an attenuation
        (negative values) in the signal path between the external generator
        and the calibrated reference plane. The value has no impact on the
        generator power.
        
        Note(s):
        
        (1) This function is available only with R&S ZVA and ZVT instrument.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:GENerator<Gen>:LEVel:OFFSet <offset>
        
        

   :param calPowerGeneratorOffset: This control sets the calibrationpower generator offset (Gain or attenuation value).
   :param portNumber: This control sets the calibrated port number. Thissuffix is ignored; the generator is selected via <Gen>.
   :param channel: Calibrated channel number.
   :param generatorNumber: This control sets thegenerator number.

.. method:: GetCalibrationPowerGeneratorOffset(self, channel=1, portNumber, generatorNumber)
           
        This function returns a gain (positive values) or an attenuation
        (negative values) in the signal path between the external generator
        and the calibrated reference plane.
        
        Note(s):
        
        (1) This function is available only with R&S ZVA and ZVT instrument.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:GENerator<Gen>:LEVel:OFFSet?
        
        

   :param portNumber: This control sets the calibrated port number. Thissuffix is ignored; the generator is selected via <Gen>.
   :param channel: Calibrated channel number.
   :param generatorNumber: This control sets thegenerator number.
   :return: calPowerGeneratorOffset

.. method:: SetReferenceReceiverAfterFirstCalSweep(self, fastSourcePowerCalibration)
           
        This function enables or disables a fast source power calibration,
        where the external power meter is used for the first calibration sweep
        only.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:FAST ON | OFF
        
        

   :param fastSourcePowerCalibration: This controlenables or disables a fast source power calibration, where theexternal power meter is used for the first calibration sweep only.

.. method:: GetReferenceReceiverAfterFirstCalSweep(self, )
           
        This function returns the state of the fast source power calibration,
        where the external power meter is used for the first calibration sweep
        only.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:FAST?
        
        

   :return: fastSourcePowerCalibration

.. method:: SetPowerCalibrationMethodSource(self, methodSource)
           
        This function selects the source power calibration method.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:METHod
        
        

   :param methodSource: This control selects thesource power calibration method.

.. method:: GetPowerCalibrationMethodSource(self, )
           
        This function returns the source power calibration method.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:METHod?
        
        

   :return: methodSource

.. method:: SetCalibrationPowerMeterReadings(self, powerMeterReadings)
           
        This function selects the number of power meter readings for source
        power calibration method
        rszvb_SetPowerCalibrationMethodSource set to RRAFter.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:PMReadings
        
        

   :param powerMeterReadings: Number of power meterreadings.

.. method:: GetCalibrationPowerMeterReadings(self, )
           
        This function returns the number of power meter readings.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:PMReadings?
        
        

   :return: powerMeterReadings

.. method:: ReadSourcePowerCorrectionData(self, channel=1, portNumber, calibratedWave, powerCorrectionValues)
           
        This function reads source power correction data sets.
        
        Note(s):
        
        (1) A power correction data set contains n real values. Each value
        corresponds to the ratio of the actual power at the reference plane
        (value provided by the used source) to the uncalibrated power in dB.
        
        (2) The number of values is equal to the number of sweep points.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA? '<src_string>'
        
        

   :param calibratedWave: This control sets theidentifier for the source of the calibrated wave.
   :param powerCorrectionValues: This control returns the powercorrection values.
   :param portNumber: This control sets the port number.
   :param channel: Channel number.
   :return: numberOfValues

.. method:: WriteSourcePowerCorrectionData(self, channel=1, portNumber, calibratedWave, numberOfValues, powerCorrectionValues)
           
        This function writes source power correction data sets.
        
        Note(s):
        
        (1) A power correction data set contains n real values. Each value
        corresponds to the ratio of the actual power at the reference plane
        (value provided by the used source) to the uncalibrated power in dB.
        
        (2) The number n is equal to the number of sweep points.
        
        (3) Writing correction data fails if the number of transferred values
        is not equal to the number of sweep points.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA '<src_string>',
        <numeric_value>...
        
        

   :param calibratedWave: This control sets theidentifier for the source of the calibrated wave.
   :param numberOfValues: This control sets the numberof power correction values.
   :param portNumber: This control sets the port number.
   :param powerCorrectionValues: This control sets the powercorrection values.
   :param channel: Channel number.

.. method:: GetSourcePowerCalibrationNumberOfWaves(self, channel=1)
           
        This function returns the number of calibrated waves of the active
        source and receiver power calibrations for channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA:PARameter:COUNt?
        
        
        
        
        

   :param channel: Channel number.
   :return: numberOfWaves

.. method:: GetSourcePowerCalibrationParamaterWave(self, channel=1, calibrationIndex, bufferSize, calibratedWave)
           
        This function returns the calibrated wave of the active source and
        receiver power calibrations for channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA:PARameter<Cal_index>? WAVE
        
        
        
        

   :param calibrationIndex: This control sets the calibration index.
   :param calibratedWave: Calibrated wave: a1 Gendenotes the source power at port 1, Ext Gen1 the source power of anexternal generator, a1 Rec or b1 Rec the receiver power at port 1 etc.
   :param bufferSize: This control defines the size ofarray passed to argument 'Throughs'.
   :param channel: Channel number.

.. method:: GetSourcePowerCalibrationParamaterStart(self, channel=1, calibrationIndex)
           
        This function returns start frequency or power (or CW frequency, if no
        frequency or power sweep is active).
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA:PARameter<Cal_index>? STAR
        
        
        
        

   :param calibrationIndex: This control sets the calibration index.
   :param channel: Channel number.
   :return: start

.. method:: GetSourcePowerCalibrationParamaterStop(self, channel=1, calibrationIndex)
           
        This function returns stop frequency or power (or CW frequency, if no
        frequency or power sweep is active).
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA:PARameter<Cal_index>? STOP
        
        
        
        

   :param calibrationIndex: This control sets the calibration index.
   :param channel: Channel number.
   :return: stop

.. method:: GetSourcePowerCalibrationParamaterPoints(self, channel=1, calibrationIndex)
           
        This function returns number of points of the active source and
        receiver power calibrations for channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA:PARameter<Cal_index>? POIN
        
        
        
        

   :param calibrationIndex: This control sets the calibration index.
   :param channel: Channel number.
   :return: points

.. method:: GetSourcePowerCalibrationParamaterType(self, channel=1, calibrationIndex)
           
        This function returns sweep type or grid (LIN, LOG, SEGM)
        of the active source and receiver power calibrations for channel <Ch>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA:PARameter<Cal_index>? STYP
        
        
        
        

   :param calibrationIndex: This control sets the calibration index.
   :param channel: Channel number.
   :return: type

.. method:: GetSourcePowerCalibrationParamaterAttenuation(self, channel=1, calibrationIndex)
           
        This function returns source or receiver attenuation of the active
        source and receiver power calibrations for channel <Ch>.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA:PARameter<Cal_index>? ATT
        
        
        
        

   :param calibrationIndex: This control sets the calibration index.
   :param channel: Channel number.
   :return: attenuation

.. method:: GetSourcePowerCalibrationParamaterCWPower(self, channel=1, calibrationIndex)
           
        This function returns CW power (for frequency sweeps; returns -200 for
        power sweeps) of the active source and receiver power calibrations for
        channel <Ch>.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA:PARameter<Cal_index>? CPOW
        
        
        
        

   :param calibrationIndex: This control sets the calibration index.
   :param channel: Channel number.
   :return: CWPower

.. method:: GetSourcePowerCalibrationParamaterCWFrequency(self, channel=1, calibrationIndex)
           
        This function returns CW frequency (for power sweeps, not available
        for frequency sweeps) of the active source and receiver power
        calibrations for channel <Ch>.
        
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA:PARameter<Cal_index>? CFR
        
        
        
        

   :param calibrationIndex: This control sets the calibration index.
   :param channel: Channel number.
   :return: CWFrequency

.. method:: GetSourcePowerCalibrationParamaterTimestamp(self, channel=1, calibrationIndex, bufferSize, timestamp)
           
        This function queries the timestamp of the power calibration in
        24-hour clock.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:DATA:PARameter<Cal_index>? TSTamp
        
        
        
        

   :param calibrationIndex: This control sets the calibration index.
   :param timestamp: Timestamp of the calibration in24-hour clock, returned as a comma-separated list of integers<Year>,<Month>,<Day>,<Hour>,<Minute>,<Second>
   :param bufferSize: This control defines the size ofarray passed to argument 'Timestamp'.
   :param channel: Channel number.

.. method:: SetSourcePowerCalibrationConvergenceFactor(self, convergenceFactor)
           
        Specifies the convergence factor for a source power calibration.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:CFACtor
        
        
        

   :param convergenceFactor: Convergence factor.

.. method:: GetSourcePowerCalibrationConvergenceFactor(self, )
           
        Returns the convergence factor for a source power calibration.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:COLLect:CFACtor?
        
        
        

   :return: convergenceFactor

.. method:: SetSourcePowerCalibrationConverterState(self, channel=1, converter, calibrationConverter)
           
        This function enables or disables the source power calibration for
        channel <Ch> and for an external frequency converter number <Con>. The
        converter must be equipped with an electronic attenuator (R&S
        ZVAZxxxE).
        The command is disabled unless a source power calibration for the
        external converter has been performed
        (SOURce<Ch>:POWer<Pt>:CORRection[:ACQuire] CONVerter,
        <source_pt>). To enable or disable a source power calibration for an
        analyzer port use SOURce<Ch>:POWer<Pt>:CORRection[:STATe].
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:CONVerter<Con>[:STATe] <Boolean>
        
        

   :param calibrationConverter: This control enables or disables thesource power calibration for the converter <Con>.
   :param converter: Converter number.
   :param channel: Channel number.

.. method:: GetSourcePowerCalibrationConverterState(self, channel=1, converter)
           
        This function returns the source power calibration for channel <Ch>
        and for an external frequency converter number <Con> state.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:CONVerter<Con>[:STATe]?
        
        

   :param converter: Converter number.
   :param channel: Channel number.
   :return: calibrationConverter

.. method:: AcquireReceiverPowerCalibration(self, channel=1, wave, portNumber, source, sourceNumber, referencePower)
           
        This function selects the wave quantity and the source for the
        receiver power calibration, starts the calibration sweep, and applies
        the receiver power correction.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>:ACQuire AWAVe | BWAVe | B1 | B2
        | B3 | B4 | B5 | B6 | B7 | B8[,<cal_port>, PORT | GENerator |
        CONVerter, <source_no>,AWAVe | NOMinal]
        
        

   :param wave: This control selects the wave.
   :param source: This control toggle between theanalyzer port and external generator.
   :param referencePower: Select the reference receivervalue (a-wave) of the calibration source or its nominal power as areference power value for the calibration.
   :param portNumber: Thiscontrol sets the port number.
   :param sourceNumber: This control sets theNumber of the port for the internal source or of the generator.
   :param channel: Channel number.

.. method:: SetAWaveReceiverPowerCalibrationState(self, channel=1, portNumber, receiverPowerCalibration)
           
        This function enables or disables the receiver power calibration for
        channel <Ch> and for the reference waves An.
        
        Notes:
        
        (1) The function is disabled unless the reference waves have been
        power calibrated (rszvb_AcquireReceiverPowerCalibration - AWAVe,...).
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>:AWAVe[:STATe] ON | OFF
        
        

   :param portNumber: This control sets the port number.
   :param receiverPowerCalibration: This controlenables (ON) or disables (OFF) the receiver power calibration for thereference waves An.
   :param channel: Channel number.

.. method:: GetAWaveReceiverPowerCalibrationState(self, channel=1, portNumber)
           
        This function returns the state of the receiver power calibration for
        channel <Ch> and for the reference waves An.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>:AWAVe[:STATe]?
        
        

   :param portNumber: This control sets the port number.
   :param channel: Channel number.
   :return: receiverPowerCalibration

.. method:: SetAWaveIdealPowerMeterMatchState(self, channel=1, portNumber, state)
           
        This function enables or disables the assumption of an ideal power
        meter match when system error correction data and
        power calibration data are combined for the enhanced wave correction.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>:AWAVe:IPMMatch[:STATe]
        
        

   :param state: This control enables (ON) or disables(OFF) the assumption of ideal power meter match.
   :param portNumber: This control sets the port number.
   :param channel: Channel number.

.. method:: GetAWaveIdealPowerMeterMatchState(self, channel=1, portNumber)
           
        This function queries the state of the assumption of an ideal power
        meter match when system error correction data and
        power calibration data are combined for the enhanced wave correction.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>:AWAVe:IPMMatch[:STATe]?
        
        

   :param portNumber: This control sets the port number.
   :param channel: Channel number.
   :return: state

.. method:: SetBWaveReceiverPowerCalibrationState(self, channel=1, portNumber, receiverPowerCalibration)
           
        This function enables or disables the receiver power calibration for
        channel <Ch> and for the received waves Bn.
        
        Notes:
        
        (1) The function is disabled unless the reference waves have been
        power calibrated (rszvb_AcquireReceiverPowerCalibration - BWAVe,...).
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>[:STATe] ON | OFF
        
        

   :param portNumber: This control sets the port number.
   :param receiverPowerCalibration: This controlenables (ON) or disables (OFF) the receiver power calibration for thereference waves Bn.
   :param channel: Channel number.

.. method:: GetBWaveReceiverPowerCalibrationState(self, channel=1, portNumber)
           
        This function returns the state of the receiver power calibration for
        channel <Ch> and for the received waves Bn.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>[:STATe]?
        
        

   :param portNumber: This control sets the port number.
   :param channel: Channel number.
   :return: receiverPowerCalibration

.. method:: ReadReceiverPowerCorrectionData(self, channel=1, portNumber, calibratedWave, powerCorrectionValues)
           
        This function reads receiver power correction data sets.
        
        Note(s):
        
        (1) A power correction data set contains n real values. Each value
        corresponds to the ratio of the actual power at the receiver input
        (value provided by the used source) to the uncalibrated power in dB.
        
        (2) The number n is equal to the number of sweep points.
        
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>:DATA? '<wave_string>'
        
        

   :param calibratedWave: This control identifier forthe calibrated wave.
   :param powerCorrectionValues: This control returns the powercorrection values.
   :param portNumber: This control sets the port number.
   :param channel: Channel number.
   :return: numberOfValues

.. method:: WriteReceiverPowerCorrectionData(self, channel=1, portNumber, calibratedWave, numberOfValues, powerCorrectionValues)
           
        This function writes receiver power correction data sets.
        
        Note(s):
        
        (1) A power correction data set contains n real values. Each value
        corresponds to the ratio of the actual power at the receiver input
        (value provided by the used source) to the uncalibrated power in dB.
        
        (2) The number n is equal to the number of sweep points.
        
        (3) Writing correction data fails if the number of transferred values
        is not equal to the number of sweep points.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<port_no>:DATA '<wave_string>',
        <numeric_value>...
        
        

   :param calibratedWave: This control identifier forthe calibrated wave.
   :param numberOfValues: This control sets the number of powercorrection values.
   :param portNumber: This control sets the port number.
   :param powerCorrectionValues: This control sets the powercorrection values.
   :param channel: Channel number.

.. method:: ReceiverPowerCalibrationHarmonic(self, channel=1)
           
        This function starts the receiver calibration (2nd power calibration
        step for harmonic measurements), stores and applies the calibration
        data.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        (2) This function is available only on R&S ZVA and ZVT instrument with
        K4 option installed.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer:HARMonic:ACQuire
        
        
        

   :param channel: Channel number.

.. method:: CorrectionManager(self, operationToBePerformed, fileName, loadParameter)
           
        This function provides operations which allows to loads trace data
        from a specified power meter correction file or trace file and assigns
        it to a trace with a specified name. Traces are created using the
        CALCulate<Ch>:PARameter:SDEFine... command. Or saves the current power
        loss list to a specified power meter correction list file.
        
        Remote-control command(s):
        MMEMory:STORe:CORRection:TCOefficient '<file name>'
        MMEMory:LOAD:CORRection:TCOefficient '<file name>'[,'<parameter
        name/trace name>']
        
        

   :param operationToBePerformed: This controlselects the type of operation to be performed.
   :param loadParameter: This control specifies the optional string Loadparameter: For imported Touchstone files for more than one port(*.s2p, *.s3p, *.s4p), the parameter denotes the imported S-parameter('S11', 'S12', ...). For ASCII (*.csv) files, the parameter referencesa trace name in the file (case sensitive). If the parameter isomitted, the first trace in the specified file is imported. Theparameter is not used for power meter correction list files (*.pmcl).
   :param fileName: This control specifiesthe file name for the file operation to be performed.

.. method:: SetPowerSensorPosition(self, powerSensorPosition)
           
        This function selects the position of the additional two-port in the
        test setup.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient:CALibration <Boolean>
        
        

   :param powerSensorPosition: This control selectsthe position of the additional two-port in the test setup.

.. method:: GetPowerSensorPosition(self, )
           
        This function returns the position of the additional two-port in the
        test setup.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient:CALibration?
        
        

   :return: powerSensorPosition

.. method:: SetTwoPortTransmissionCoefficientsEnabled(self, twoPortEnabled)
           
        This function enables or disables the use of two-port transmission
        coefficients.
        
        Notes:
        (1) The power loss list must contain at least one point before the
        transmission coefficients can be enabled.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient[:STATe] <Boolean>
        
        

   :param twoPortEnabled: This control enables (ON)or disables (OFF) use of two-port transmission coefficients.

.. method:: GetTwoPortTransmissionCoefficientsEnabled(self, )
           
        This function returns the use of two-port transmission coefficients.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient[:STATe]?
        
        

   :return: twoPortEnabled

.. method:: GetLossListNumberOfValues(self, )
           
        Returns the number of frequency values and transmission coefficients
        in the power loss list.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient:COUNt?
        
        
        

   :return: numberOfValues

.. method:: SetPowerLossListCoefficient(self, operationToBePerformed, point, frequency, transmissionCoefficient)
           
        This function Adds a new frequency and transmission coefficient to the
        power loss list.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient:DEFine <frequency>,
        <transmission>
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient:INSert<List_No>
        <frequency>, <transmission>
        
        

   :param transmissionCoefficient: This control sets the Transmissioncoefficient.
   :param operationToBePerformed: This controlselects the type of operation to be performed.
   :param frequency: This control sets stimulus frequency value.According to frequency range of the analyzer; see list of analyzermodels [Hz]. If several points with identical frequencies are added,the analyzer automatically ensures a frequency spacing of 1 Hz.
   :param point: This control set theposition in the list.

.. method:: GetPowerLossListCoefficient(self, point)
           
        This function returns the frequency and transmission coefficient from
        power loss list.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient:DEFine <List_No>?
        
        

   :param point: This control set the number of point in the list.
   :return: frequency
   :return: transmissionCoefficient

.. method:: DeleteAllPowerLossListPoints(self, )
           
        This function clears the power loss list.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient:DELete<List_No>:ALL
        
        


.. method:: DeletePowerLossListSinglePoint(self, point)
           
        This function deletes a single point no. <List_No> in the power loss
        list.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient:DELete<List_No>[:DUMMy]
        
        

   :param point: This control set the List Number inthe power loss list to delete.

.. method:: SetPowerLossListTrace(self, traceName)
           
        This function Selects a trace which provides the points for the power
        loss list.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection:TCOefficient:FEED '<trace_name>'
        
        

   :param traceName: This control parameter for thetrace name, e.g. 'Trc1'. The trace must exist in the active setup.

.. method:: SetSourcePowerCorrectionState(self, channel=1, portNumber, sourcePowerCorrectionState)
           
        This function enables or disables the source power correction for
        channel <Ch> and for port number <Pt>.
        
        Notes:
        
        (1) The command is disabled unless a source power calibration for the
        analyzer port has been performed
        (rszvb_InitiateSourcePowerCalibration).
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection[:STATe] ON | OFF
        
        

   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.
   :param sourcePowerCorrectionState: This controlenables (ON) or disables (OFF) the source power correction state.

.. method:: GetSourcePowerCorrectionState(self, channel=1, portNumber)
           
        This function returns the state of the source power correction for
        channel <Ch> and for port number <Pt>.
        
        Notes:
        
        (1) The command is disabled unless a source power calibration for the
        analyzer port has been performed
        (rszvb_InitiateSourcePowerCalibration).
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>:CORRection[:STATe]?
        
        

   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.
   :return: sourcePowerCorrectionState

.. method:: SetReceiverPowerCorrectionState(self, channel=1, portNumber, receiverPowerCorrectionState)
           
        This function enables or disables the receiver power calibration for
        channel <Ch> and for the received waves bn.
        
        Notes:
        
        (1) The command is disabled unless the received waves have been power
        calibrated (rszvb_AcquireReceiverPowerCalibration).
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<Pt>:STATe ON | OFF
        
        

   :param receiverPowerCorrectionState: This controlenables (ON) or disables (OFF) the receiver power correction state.
   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.

.. method:: GetReceiverPowerCorrectionState(self, channel=1, portNumber)
           
        This function returns the state of the receiver power calibration for
        channel <Ch> and for the received waves bn.
        
        Notes:
        
        (1) The command is disabled unless the received waves have been power
        calibrated (rszvb_AcquireReceiverPowerCalibration).
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:POWer<Pt>:STATe?
        
        

   :param portNumber: This control sets the calibrated port number.
   :param channel: Channel number.
   :return: receiverPowerCorrectionState

.. method:: CalibrationManager(self, channel=1, operationToBePerformed, fileName)
           
        This function provides operations which allows to store system error
        correction data to the cal pool and to assign stored correction data
        to channels:
        
        Copy
        Apply
        Resolve Pool Link
        Delete
        Merge
        
        Remote-control command(s):
        MMEMory:STORe:CORRection <Ch>,'<file_name>'
        MMEMory:LOAD:CORRection <Ch>,'<file_name>'
        MMEMory:LOAD:CORRection:RESolve <Ch>,'<file_name>'
        MMEMory:DELete:CORRection '<file_name>'
        MMEMory:LOAD:CORRection:MERGe <Channel>, '<file1>.cal', '<file2>.cal',
        ...
        
        

   :param operationToBePerformed: This control selects the type ofoperation to be performed.
   :param channel: Channel number.
   :param fileName: This controlspecifies the file name for the file operation to be performed.

.. method:: CalibrationAuto(self, channel=1, calibrationKitName, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4, calUnitPort1, calUnitPort2, calUnitPort3, calUnitPort4)
           
        This function selects and initiates a one-port, two-port, three-port
        or four-port automatic calibration at arbitrary analyzer and
        calibration unit ports.
        
        Note(s):
        
        (1) Port numbers of the analyzer:
        For an n-port automatic calibration (n = 1 to 4), n arbitrary (not
        necessarily consecutive) port numbers must be specified.
        
        (2) Port numbers of the cal unit:
        For an n-port automatic calibration (n = 1 to 4), n arbitrary (not
        necessarily consecutive) port numbers must be specified. It is
        possible to combine arbitrary (not necessarily matching) pairs of
        analyzer and cal unit ports.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:PORTs '<file_name>',<analyzer_port
        _no>,<cal_unit_port_no>{,<analyzer_port_no>,<cal_unit_port_no>}
        
        

   :param calUnitPort1: Port number of the cal unit.
   :param calUnitPort3: Port number of the cal unit.
   :param calUnitPort2: Port number of the cal unit.
   :param calUnitPort4: Port number of the cal unit.
   :param calibrationKitName: Name and (possibly) directory of the calkit file to be used for the automatic calibration:
   :param analyzerPort1: Port number.
   :param analyzerPort2: Port number.
   :param analyzerPort3: Port number.
   :param analyzerPort4: Port number.
   :param channel: Channel number.

.. method:: CalibrationAutoSimplified(self, channel=1, calibrationKitName, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4)
           
        This function selects and initiates a one-port, two-port, three-port
        or four-port automatic calibration at arbitrary analyzer ports.
        
        Note(s):
        
        (1) If the test setup contains a high attenuation the analyzer may
        fail to detect the cal unit ports connected to each of its ports. In
        this case use the extended function rszvb_CalibrationAuto (command
        [SENSe<Ch>:]CORRection:COLLect:AUTO:PORTs)
        
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO
        '<file_name>',<port_no>{,<port_no>}
        
        

   :param calibrationKitName: Name and (possibly) directory of the calkit file to be used for the automatic calibration:
   :param analyzerPort1: Port number.
   :param analyzerPort2: Port number.
   :param analyzerPort3: Port number.
   :param analyzerPort4: Port number.
   :param channel: Channel number.

.. method:: CalibrationAutoType(self, channel=1, parameters, calibrationKitName, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4, calUnitPort1, calUnitPort2, calUnitPort3, calUnitPort4)
           
        This function selects and initiates a one-port, two-port, three-port
        or four-port automatic calibration at arbitrary analyzer and
        calibration unit ports.
        
        Note(s):
        
        (1) Port numbers of the analyzer:
        For an n-port automatic calibration (n = 1 to 4), n arbitrary (not
        necessarily consecutive) port numbers must be specified.
        
        (2) Port numbers of the cal unit:
        For an n-port automatic calibration (n = 1 to 4), n arbitrary (not
        necessarily consecutive) port numbers must be specified. It is
        possible to combine arbitrary (not necessarily matching) pairs of
        analyzer and cal unit ports.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:PORTs:TYPE <cal_type>,'<file_name>
        ',<analyzer_port_no>,<cal_unit_port_no>{,<analyzer_port_no>,<cal_unit_
        port_no>}
        
        

   :param calUnitPort1: Port number of the cal unit.
   :param calUnitPort3: Port number of the cal unit.
   :param calUnitPort2: Port number of the cal unit.
   :param calUnitPort4: Port number of the cal unit.
   :param parameters: This control selects a calibration type.
   :param calibrationKitName: Name and (possibly) directory of the calkit file to be used for the automatic calibration:
   :param analyzerPort1: Port number.
   :param analyzerPort2: Port number.
   :param analyzerPort3: Port number.
   :param analyzerPort4: Port number.
   :param channel: Channel number.

.. method:: CalibrationAutoTypeSimplified(self, channel=1, parameters, calibrationKitName, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4)
           
        This function Selects and initiates a one-port, two-port, three-port
        or four-port automatic calibration at arbitrary analyzer and cal unit
        ports. This command also selects the calibration type.
        
        Note(s):
        
        (1) If the test setup contains a high attenuation the analyzer may
        fail to detect the cal unit ports connected to each of its ports. In
        this case use the extended function rszvb_CalibrationAutoType (command
        [SENSe<Ch>:]CORRection:COLLect:AUTO:PORTs:TYPE)
        
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:TYPE
        <cal_type>, '<file_name>',<port_no>{,<port_no>}
        
        

   :param parameters: This control selects a calibration type.
   :param calibrationKitName: Name and (possibly) directory of the calkit file to be used for the automatic calibration:
   :param analyzerPort1: Port number.
   :param analyzerPort2: Port number.
   :param analyzerPort3: Port number.
   :param analyzerPort4: Port number.
   :param channel: Channel number.

.. method:: CalibrationRetainPortGroups(self, retainPortGroups)
           
        This function retains port groups during parser calibration with
        calibration Unit.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:RPGRoup
        
        

   :param retainPortGroups: This control retainsport groups during parser calibration with calibration Unit.

.. method:: GetCalibrationConnection(self, channel=1)
           
        This function returns the assignment between the network analyzer
        ports and the ports of the connected automatic calibration unit.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:PORTs:CONNection?
        
        

   :param channel: Channel number.
   :return: analyzerPort1
   :return: analyzerPort2
   :return: analyzerPort3
   :return: analyzerPort4

.. method:: CalibrationAutoEx(self, channel=1, calibrationKitName, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4, calUnitPort1, calUnitPort2, calUnitPort3, calUnitPort4, timeout)
           
        This function selects and initiates a one-port, two-port, three-port
        or four-port automatic calibration at arbitrary analyzer and
        calibration unit ports.
        
        Note(s):
        
        (1) Port numbers of the analyzer:
        For an n-port automatic calibration (n = 1 to 4), n arbitrary (not
        necessarily consecutive) port numbers must be specified.
        
        (2) Port numbers of the cal unit:
        For an n-port automatic calibration (n = 1 to 4), n arbitrary (not
        necessarily consecutive) port numbers must be specified. It is
        possible to combine arbitrary (not necessarily matching) pairs of
        analyzer and cal unit ports.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:PORTs '<file_name>',<analyzer_port
        _no>,<cal_unit_port_no>{,<analyzer_port_no>,<cal_unit_port_no>}
        
        

   :param calUnitPort1: Port number of the cal unit.
   :param calUnitPort3: Port number of the cal unit.
   :param calUnitPort2: Port number of the cal unit.
   :param calUnitPort4: Port number of the cal unit.
   :param calibrationKitName: Name and (possibly) directory of the calkit file to be used for the automatic calibration:
   :param analyzerPort1: Port number.
   :param analyzerPort2: Port number.
   :param analyzerPort3: Port number.
   :param analyzerPort4: Port number.
   :param timeout: This control sets the timeout value in millisecondsfor Auto Calibration feature.
   :param channel: Channel number.

.. method:: CalibrationAutoAssignmentType(self, channel=1, parameters, calibrationKitName)
           
        This function selects a calibration type and a cal unit
        characterization (cal kit file) for an automatic calibration with
        multiple port assignments.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:CONFigure <cal_type>,
        '<file_name>'}
        
        

   :param calibrationKitName: Name and (possibly) directory of the calkit file to be used for the automatic calibration:
   :param parameters: This control selects a calibration type.
   :param channel: Channel number.

.. method:: CalibrationAutoAssignmentDefinition(self, channel=1, assignment, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4, calUnitPort1, calUnitPort2, calUnitPort3, calUnitPort4)
           
        This function defines a port assignment numbered <Assignment>. This
        command is particularly relevant for multiple port
        assignments.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:ASSignment<Asg>:DEFine <analyzer_p
        ort_no>,<cal_unit_port_no>{,<analyzer_port_no>,<cal_unit_port_no>}
        
        

   :param calUnitPort1: Port number of the cal unit.
   :param calUnitPort3: Port number of the cal unit.
   :param calUnitPort2: Port number of the cal unit.
   :param calUnitPort4: Port number of the cal unit.
   :param assignment: Current number of the port assignment.
   :param analyzerPort1: Port number.
   :param analyzerPort2: Port number.
   :param analyzerPort3: Port number.
   :param analyzerPort4: Port number.
   :param channel: Channel number.

.. method:: GetCalibrationAutoAssingnmentDefinition(self, channel=1, assignment)
           
        This function queries a port assignment numbered <Assignment>. This
        command is particularly relevant for multiple port
        assignments.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:ASSignment<Asg>:DEFine?
        
        

   :param assignment: Current number of the port assignment.
   :param channel: Channel number.
   :return: analyzerPort1
   :return: analyzerPort2
   :return: analyzerPort3
   :return: analyzerPort4
   :return: calUnitPort1
   :return: calUnitPort2
   :return: calUnitPort3
   :return: calUnitPort4

.. method:: InitiateCalibrationAutoAssignment(self, channel=1, assignment)
           
        Initiates an automatic calibration for a previously defined port
        assignment numbered <Assignment>.
        
        Note(s):
        
        (1) A complete, valid set of port assignments must be defined before
        you can initiate a calibration
        (rszvb_CalibrationAutoAssignmentDefinition)
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:ASSignment<Asg>:ACQuire
        
        

   :param assignment: Current number of the port assignment.
   :param channel: Channel number.

.. method:: CalibrationAutoAssignmentSave(self, channel=1)
           
        Calculates the error terms, based on the previously acquired
        calibration sweeps for multiple port assignments, saves the data and
        applies the calibration to the active channel <Ch>.
        
        Note(s):
        (1) A complete, valid set of port assignments must have been measured
        (rszvb_InitiateCalibrationAutoAssignment) before the
        analyzer can calculate the error terms.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:SAVE
        
        

   :param channel: Channel number.

.. method:: CalibrationAutoAssingnmentDeleteAll(self, channel=1)
           
        This function deletes all port assignments in specified channel.
        
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:ASSignment<Asg>:DELete:ALL
        
        

   :param channel: Channel number.

.. method:: SetCalibrationDataCurrentState(self, channel=1, keepMeasData)
           
        This function activates or deactivates the calibration mode where the
        raw measurement data of the standards is stored after the calibration
        is completed. The setting is valid for the current calibration, where
        it overwrites the global setting
        ([SENSe<Ch>:]CORRection:COLLect[:ACQuire]:RSAVe:DEFault). A new
        calibration deletes the calibration data acquired in previous
        calibrations.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect[:ACQuire]:RSAVe <Boolean>
        
        
        

   :param keepMeasData: This control keeps measurement data on or off.
   :param channel: Channel number.

.. method:: GetCalibrationDataCurrentState(self, channel=1)
           
        This function returns the state of the calibration mode.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect[:ACQuire]:RSAVe?
        
        

   :param channel: Channel number.
   :return: keepMeasData

.. method:: SetCalibrationDataDefaultState(self, channel=1, keepMeasData)
           
        This function activates or deactivates the calibration mode where the
        raw measurement data of the standards is stored after the calibration
        is completed. The setting remains valid for all subsequent
        calibrations until it is changed explicitly. A new calibration deletes
        the calibration data acquired in previous calibrations.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect[:ACQuire]:RSAVe:DEFault <Boolean>
        
        
        

   :param keepMeasData: This control keeps measurement data on or off.
   :param channel: Channel number.

.. method:: GetCalibrationDataDefaultState(self, channel=1)
           
        This function returns the state of the calibration mode.
        
        Note(s):
        
        (1) For some measurements the default set timeout can be insufficient.
        To set higher timeout use function rszvb_setTimeOut.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect[:ACQuire]:RSAVe:DEFault?
        
        

   :param channel: Channel number.
   :return: keepMeasData

.. method:: ExpCharDataTouchstoneFile(self, fileName)
           
        This function exports the calibration unit's characterization data as
        Touchstone files into the given directory.
        
        Remote-control command(s):
        :MMEMory:AKAL:FACTory:CONVersion <file_name>
        
        

   :param fileName: This control sets the file name

.. method:: ExportUserCharacterizationDataTouchstoneFile(self, directoryName, fileName)
           
        This function converts an arbitrary (e.g. user-defined) set of
        calibration data of the standards in the active calibration
        unit (SYSTem:COMMunicate:RDEVice:AKAL:ADDRess) to Touchstone format
        and copies it to the specified directory.
        
        Remote-control command(s):
        MMEMory:AKAL:USER:CONVersion '<directory_name>'[,'<file_name>']
        
        

   :param directoryName: This control sets thedirectory name
   :param fileName: This control sets the file name

.. method:: SetCalibrationConnector(self, channel=1, connectorName, propagationMode, connectorType, relativePermittivity, impedance)
           
        This function configures the user-defined connector types.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CONNection '<conn_name>', TEM | WGUide, GENDer
        | NGENder, <perm_rel>, <imped>
        
        

   :param propagationMode: This control selects a propagation mode.
   :param relativePermittivity: This control sets the relativepermittivity.
   :param impedance: This control sets the referenceimpedance or cutoff frequency.
   :param connectorType: This control selects a connector type.

   :param connectorName: Name of the user-defined connectors.
   :param channel: Channel number.

.. method:: GetCalibrationConnector(self, channel=1, connectorName)
           
        This function queries the user-defined connector types.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CONNection? '<conn_name>'
        
        
        

   :param connectorName: Name of the user-defined connectors.
   :param channel: Channel number.
   :return: propagationMode
   :return: connectorType
   :return: relativePermittivity
   :return: impedance

.. method:: CalibrationConnectorCatalog(self, catalog, bufferSize)
           
        This function returns a list of the connector types of all calibration
        kits in use.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CONNection:CATalog?
        
        

   :param catalog: Response is a string parameterwith comma-separated list of the connector types of all calibrationkits in use.
   :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.

.. method:: DeleteCalibrationConnector(self, channel=1, connectorName)
           
        This function deletes a user-defined connector type named
        '<conn_name>'.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CONNection:DELete '<conn_name>'
        
        

   :param connectorName: Name of the user-defined connectors.
   :param channel: Channel number.

.. method:: GetCalibrationDate(self, channel=1, bufferSize, calibrationDate)
           
        This function queries date and time of the channel's calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATE?
        
        

   :param bufferSize: This control defines the size of array passed toargument 'Calibration Kit Name'.
   :param channel: Channel number.
   :param calibrationDate: This control returns thename of calibration kit.

.. method:: GetCalibrationState(self, channel=1)
           
        This function queries state of the channel's calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:SSTate?
        
        

   :param channel: Channel number.
   :return: calibrationState

.. method:: GetCalibrationLabel(self, channel=1, bufferSize, label)
           
        This function queries the power calibration label.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:PSTate?
        
        

   :param bufferSize: This control defines the size of array passed toargument 'Label'.
   :param channel: Channel number.
   :param label: This control returns the powercalibration label.

.. method:: GetCalibrationDataParameters(self, channel=1)
           
        This function queries the parameters of the channel's calibration
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter?
        
        

   :param channel: Channel number.
   :return: frequencyStart
   :return: frequencyStop
   :return: numberOfPoints
   :return: internalSignalSourcePower
   :return: sweepType

.. method:: GetCalibrationsNumber(self, channel=1)
           
        This function queries the number of active system error corrections in
        channel no. <Ch>.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter:COUNt?
        
        

   :param channel: Channel number.
   :return: numberOfCalibrations

.. method:: GetCalibrationDataParametersMoreCalibrations(self, channel=1, calibration)
           
        This function queries the parameters of the channel's calibration 
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter<Cal>?
        
        

   :param channel: Channel number.
   :param calibration: Calibration number.
   :return: frequencyStart
   :return: frequencyStop
   :return: numberOfPoints
   :return: internalSignalSourcePower
   :return: sweepType

.. method:: GetCalibrationDataBandwidth(self, channel=1, calibration)
           
        This function queries the bandwidth of the channel's calibration 
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter<Cal>? BAND
        
        

   :param channel: Channel number.
   :param calibration: Calibration number.
   :return: bandwidth

.. method:: GetCalibrationDataPointDelay(self, channel=1, calibration)
           
        This function queries the point delay of the channel's calibration 
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter<Cal>? PDLY
        
        

   :param channel: Channel number.
   :param calibration: Calibration number.
   :return: pointDelay

.. method:: GetCalibrationDataReceiverAttenuation(self, channel=1, calibration, arraySize, calibrationPort, attenuation)
           
        This function queries the point delay of the channel's calibration 
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter<Cal>? RATT
        
        

   :param calibrationPort: This control returns array of calibration ports numbers.
   :param attenuation: This control returns array of calibration portattenuations.
   :param arraySize: Size of array passed to Calibration Port &Attenuation. parameter.
   :param channel: Channel number.
   :param calibration: Calibration number.
   :return: returnedValues

.. method:: GetCalibrationDataType(self, channel=1, calibration)
           
        This function queries the calibration type.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter<Cal>? TYPE
        
        

   :param channel: Channel number.
   :param calibration: Calibration number.
   :return: calibrationType

.. method:: GetCalibrationDataPorts(self, channel=1, calibration, arraySize)
           
        This function queries the calibrated ports.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter<Cal>? PORT
        
        

   :param arraySize: Size of array passed to Calibration Port &Attenuation parameter.
   :param channel: Channel number.
   :param calibration: Calibration number.
   :return: calibrationPorts
   :return: returnedValues

.. method:: GetCalibrationDataThroughs(self, channel=1, calibration, bufferSize, throughs)
           
        This function queries the list of measured Throughs with port
        assignment, if more than two ports are calibrated
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter<Cal>? THR
        
        

   :param throughs: List of measured Throughs withport assignment, if more than two ports are calibrated: <1st Through,1st port no> - <1st Through, 2nd port no>, <2nd Through, 1st port no>- <2nd Through, 2nd port no> ... , e.g. 2-3, 2-4, 3-4 (3 measuredThroughs between ports 2 and 3, 2 and 4, and 3 and 4).
   :param bufferSize: This control defines the size of array passed toargument 'Throughs'.
   :param channel: Channel number.
   :param calibration: Calibration number.

.. method:: GetCalibrationDataTimestamp(self, channel=1, calibration, bufferSize, timestamp)
           
        This function queries the timestamp of the calibration in 24-hour
        clock.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:DATA:PARameter<Cal>? TSTamp
        
        

   :param timestamp: Timestamp of the calibration in24-hour clock, returned as a comma-separated list of integers<Year>,<Month>,<Day>,<Hour>,<Minute>,<Second>
   :param bufferSize: This control defines the size of array passed toargument 'Timestamp'.
   :param channel: Channel number.
   :param calibration: Calibration number.

.. method:: SetActiveCalibrationUnit(self, calibrationUnit)
           
        This function sets the calibration unit with given address as active
        calibration unit.
        
        Remote-control command(s):
        :SYSTem:COMMunicate:RDEVice:AKAL:ADDRess
        
        

   :param calibrationUnit: This control sets theactive calibration unit.

.. method:: GetActiveCalibrationUnit(self, bufferSize, calibrationUnit)
           
        This function returns he type and address of the active calibration
        unit.
        
        Remote-control command(s):
        :SYSTem:COMMunicate:RDEVice:AKAL:ADDRess?
        
        

   :param calibrationUnit: This control returns thetype and address of all calibration units connected to the VNA.
   :param bufferSize: This control defines the sizeof array passed to argument 'Calibration Kit Name'.

.. method:: SetAutomaticPowerReductionState(self, automaticPowerReduction)
           
        This function enables or disables automatic power reduction at all
        test ports while an automatic calibration using the
        calibration unit R&S ZV-Zxx is active.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:AKAL:PREDuction[:STATe] ON | OFF
        
        

   :param automaticPowerReduction: This controlenables or disables automatic power reduction at all test ports whilean automatic calibration using thecalibration unit R&S ZV-Zxx is active.

.. method:: GetAutomaticPowerReductionState(self, )
           
        This function returns automatic power reduction state at all test
        ports while an automatic calibration using the calibration unit R&S
        ZV-Zxx is active.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:AKAL:PREDuction[:STATe]?
        
        

   :return: automaticPowerReduction

.. method:: GetAllCalibrationUnits(self, bufferSize, calibrationUnit)
           
        This function returns the type and address of all calibration units
        connected to the VNA.
        
        Remote-control command(s):
        :SYSTem:COMMunicate:RDEVice:AKAL:ADDRess:ALL?
        
        

   :param calibrationUnit: This control returns thetype and address of all calibration units connected to the VNA.
   :param bufferSize: This control defines the sizeof array passed to argument 'Calibration Kit Name'.

.. method:: ConfigureCalibrationUnitStandard(self, standard, port1, port2)
           
        This function defines calibration unit standard.
        
        Remote-control command(s):
        :SYSTem:COMMunicate:AKAL:CONNection THRough | OPEN | SHORt |
        MATCh,<port_number>{,<port_number>}
        
        

   :param port1: Port number.
   :param port2: Port number.
   :param standard: This control selects acalibration unit standardValid Values:RSZVB_CALUNIT_STD_THR (0) - ThroughRSZVB_CALUNIT_STD_OPEN (1) - OpenRSZVB_CALUNIT_STD_SHOR (2) - ShortRSZVB_CALUNIT_STD_MATC (3) - Match

.. method:: SetFactoryCalibrationState(self, channel=1, factoryCalibration)
           
        This function enables or disables the factory calibration for a
        particular channel.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:FACTory[:STATe] <Boolean>
        
        
        

   :param factoryCalibration: This control enables or disables thefactory calibration.
   :param channel: Channel number.

.. method:: GetFactoryCalibrationState(self, channel=1)
           
        This function returns the factory calibration state for a particular
        channel.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:FACTory[:STATe]?
        
        
        

   :param channel: Channel number.
   :return: factoryCalibration

.. method:: SetEnhancedWaveCorrection(self, channel=1, errorCorrection)
           
        This function activates or deactivates the system error correction of
        all a- and b-waves which are related to the ports
        of the active calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EWAVe[:STATe]
        
        

   :param errorCorrection: This control activates or deactivates thesystem error correction.
   :param channel: Channel number.

.. method:: GetEnhancedWaveCorrection(self, channel=1)
           
        This function queries status of the system error correction of all a-
        and b-waves which are related to the ports of the active calibration.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EWAVe[:STATe]?
        
        
        

   :param channel: Channel number.
   :return: errorCorrection

.. method:: SetLoadMatchingCorrection(self, channel=1, loadMatchingCorrection)
           
        This function enables the load match correction for frequency
        conversion measurements. The load match correction requires an enabled
        Enhanced Wave Correction (rszvb_SetEnhancedWaveCorrection)
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:GAIN:LMCorrection
        
        

   :param channel: Channel number.
   :param loadMatchingCorrection: This control enables the load matchcorrection for frequency conversion measurements.

.. method:: GetLoadMatchingCorrection(self, channel=1)
           
        This function returns the state of the load match correction for
        frequency conversion measurements.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:GAIN:LMCorrection?
        
        

   :param channel: Channel number.
   :return: loadMatchingCorrection

.. method:: SetCalibrationCorrectionBaseFrequencyState(self, channel=1, state)
           
        This function force calibration and system error correction to be
        performed at base frequency for setups with external frequency
        conversion.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CBFReq[:STATe]
        
        

   :param state: This control enables (ON) or disables (OFF) thecalibration and system error correction at base frequency.
   :param channel: Channel number.

.. method:: GetCalibrationCorrectionBaseFrequencyState(self, channel=1)
           
        This function returns the state of calibration and system error
        correction at base frequency for setups with external frequency
        conversion.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CBFReq[:STATe]?
        
        

   :param channel: Channel number.
   :return: state

.. method:: SetCalibrationKit(self, connector, calibrationKitName)
           
        This function selects the calibration kit to be used for a specified
        connector type.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:<conn_type>:SELect '<Ckit_Name>'
        
        

   :param connector: This control selects a connector type.
   :param calibrationKitName: This control defines the name of calibration kit.


.. method:: GetCalibrationKit(self, connector, bufferSize, calibrationKitName)
           
        This function queries the calibration kit to be used for a specified
        connector type.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:<conn_type>:SELect?
        
        

   :param connector: This control selects a connector type.
   :param bufferSize: Thiscontrol defines the size of array passed to argument 'Calibration KitName'.
   :param calibrationKitName: This control returnsthe name of calibration kit.

.. method:: SetCalibrationKitWithLabel(self, connector, calibrationKitName, calibrationKitLabel)
           
        This function selects the calibration kit to be used for a specified
        connector type. The kit is identified by its name and label.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:<conn_type>:LSELect '<ckit_name>',
        '<ckit_label>'
        
        
        

   :param connector: This control selects a connector type.
   :param calibrationKitLabel: String parametercontaining the label of a calibration kit.
   :param calibrationKitName: This control defines the name of calibration kit.


.. method:: SetCalibrationKitUserConnectorType(self, connector, calibrationKitName)
           
        This function selects the calibration kit to be used for a specified
        connector type.
        
        Note(s):
        
        (1) The function is suitable for connector types with arbitrary, user-
        defined names. For standard connector types you can use the command
        [SENSe<Ch>:]CORRection:CKIT:<conn_type>:SELect (function
        rszvb_SetCalibrationKit)
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:SELect '<conn_name>', '<ckit_name>'
        
        

   :param connector: This control sets a user-defined connector type.
   :param calibrationKitName: This control defines thename of calibration kit.

.. method:: GetCalibrationKitUserConnectorType(self, connector, bufferSize, calibrationKitName)
           
        This function returns the calibration kit to be used for a specified
        connector type.
        
        Note(s):
        
        (1) The function is suitable for connector types with arbitrary, user-
        defined names. For standard connector types you can use the command
        [SENSe<Ch>:]CORRection:CKIT:<conn_type>:SELect? (function
        rszvb_GetCalibrationKit)
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:SELect? '<conn_name>'
        
        

   :param connector: This control sets a user-defined connector type.
   :param bufferSize: This control defines the size ofarray passed to argument 'Calibration Kit Name'.
   :param calibrationKitName: This control returnsthe name of calibration kit.

.. method:: SetCalibrationKitUserConnectorTypeWithLabel(self, connectionType, calibrationKitName, calibrationKitLabel)
           
        Selects the calibration kit to be used, specifying its connector type,
        name, and label.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:LSELect '<conn_type>', '<ckit_name>',
        '<ckit_label>'
        
        
        

   :param calibrationKitLabel: String parametercontaining the label of a calibration kit.
   :param calibrationKitName: This control defines thename of calibration kit.
   :param connectionType: Connector type, e.g. auser-defined connector type.

.. method:: GetCalibrationKitUserConnectorTypeWithLabel(self, connectionType, bufferSize, calibrationKitData)
           
        This function returns the name and label of calibration kit.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:LSELect? '<conn_type>'
        
        
        

   :param calibrationKitData: This control returnsthe name and label of calibration kit.
   :param bufferSize: This control defines the size ofarray passed to argument 'Calibration Kit Name'.
   :param connectionType: Connector type, e.g. auser-defined connector type.

.. method:: CalibrationKitCatalog(self, connectorName, catalog, bufferSize)
           
        This function returns a list of all cal kits for a given connector
        type.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:CATalog? '<Conn_Name>'
        
        

   :param catalog: Response is a string parameter withcomma-separated list of all cal kits for a given connector type.
   :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.
   :param connectorName: This control sets the nameof the connector type. Use function rszvb_CalibrationConnectorCatalogto query connector names.

.. method:: CalibrationKitCatalogWithLabel(self, connectorName, bufferSize, catalog)
           
        This function Returns a list of all cal kits and their labels for a
        given connector type.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:LCATalog? '<Conn_Name>'
        
        

   :param catalog: Response is a string parameter with comma-separatedlist of all names of the given connector type.
   :param bufferSize: Pass the number of bytes in the ViChar array you specify for the 'Catalog' parameter.
   :param connectorName: This control sets the nameof the connector type. Use function rszvb_CalibrationConnectorCatalogto query connector names.

.. method:: ImportZVRCalibrationKit(self, calibrationKitName)
           
        This function loads cal kit data from a specified ZVR cal kit file.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:INSTall '<file_name>'
        
        

   :param calibrationKitName: This control definesthe name of calibration kit.

.. method:: ConfigureCalibrationStandard(self, connector, standard, kit, serialNumber, minFreqHz, maxFreqHz, lengthmm, loss, c0L0, c1L1, c2L2, c3L3, approximation)
           
        This function defines the parameters of a calibration standard <std_type> for a specified connector type <conn_type>. A particular
        physical standard can be selected by specifying the name of the
        calibration kit and its serial number.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:<conn_type>:<std_type>
        '<Ckit_Name>','<Std_No>',<Min_Freq>,<Max_Freq>,<El_Length>,<Loss>,<C0>
        | <L0>,<C1> | <L1>,<C2> | <L2>,<C3> | <L3>, OPEN | SHORt
        
        

   :param loss: This control specifies losses in dB/GHz.
   :param c0L0: This control specifies constantparasitic capacitance/inductance.
   :param minFreqHz: This control specifies min. frequency of thestandard.
   :param approximation: This control specifiesapproximate modeling of the standard.
   :param serialNumber: This control specifies serialnumber of the standard.
   :param kit: This control specifiescalibration kit name.
   :param connector: This control selects a connector type.
   :param c3L3: This control specifies polynomialcoefficient 3 for parasitic capacitance/inductance.
   :param lengthmm: This control specifieselectrical length of the standard.
   :param c1L1: This control specifies polynomialcoefficient 1 for parasitic capacitance/inductance.
   :param maxFreqHz: This control specifiesmax. frequency of the standard.
   :param c2L2: This control specifies polynomialcoefficient 2 for parasitic capacitance/inductance.
   :param standard: Thiscontrol selects a standard from the selected calibration kit.(N50,N75, SMA, PC7, PC3.5)

.. method:: ConfigureCalibrationStandardWithLabel(self, standard, connector, calkitName, calkitLabel, standardLabel, minFreqHz, maxFreqHz, electricalLength, loss, z0, capacitances, residualInductances, approximation)
           
        This function defines the parameters of a non-ideal 1 port or 2-port
        calibration standard <std_type>
        
        Attribute(s):
        -
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:<std_type>:WLABel
        
        

   :param loss: This control specifies losses in dB/GHz.
   :param maxFreqHz: This control specifiesmax. frequency of the standard.
   :param capacitances: This controlspecifies constant parasitic capacitance. The array must contain thetotal of 4 values {C0,C1,C2,C3}.
   :param minFreqHz: This control specifies min. frequency of thestandard.
   :param approximation: This control specifies approximatemodeling of the standard.
   :param residualInductances: This control specifiesconstant parasitic inductance. The array must contain the total of 4values {L0,L1,L2,L3}.
   :param standard: This control selects a standard from the selected calibration kit.(N50, N75, SMA, PC7, PC3.5)
   :param connector: This controlselects a connector type.
   :param calkitLabel: This control specifies thelabel (e.g. the serial number) of the calibration kit.
   :param standardLabel: This control specifies the label (e.g. theserial number) of the standard.
   :param electricalLength: This controlspecifies electrical length of the standard.
   :param calkitName: This controlspecifies calibration kit name.
   :param z0: This control specifies referenceimpedance

.. method:: CalibrationStandardsCatalog(self, calibrationKitName, catalog, bufferSize)
           
        This function returns a list of all standards in a given calibration
        kit.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:STANdard:CATalog? '<Ckit_Name>'
        
        

   :param catalog: Response is a string parameter withcomma-separated list of all standards in a given calibration kit.
   :param calibrationKitName: This control sets thename of the cal kit. Use function rszvb_CalibrationKitCatalog to querycal kit names.
   :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.

.. method:: CalibrationStandardsCatalogWithLabel(self, calibrationKitName, calibrationKitLabel, bufferSize, catalog)
           
        This function returns a list of all standards in a given calibration
        kit.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:STANdard:LCATalog? '<ckit_name>',
        '<ckit_label>'
        
        
        

   :param calibrationKitLabel: String parametercontaining the label of a calibration kit.
   :param catalog: Response is a string parameter with comma-separatedlist of all standards in a given calibration kit.
   :param calibrationKitName: This control sets thename of the cal kit. Use function rszvb_CalibrationKitCatalog to querycal kit names.
   :param bufferSize: Pass the number of bytes in the ViChar array you specify for the 'Catalog' parameter.

.. method:: SaveCalibrationKit(self, fileName)
           
        This function characterizes the active calibration unit and saves the
        cal kit file on the calibration unit's internal flash memory (relative
        path) or mass storage (absolute path) as a user cal kit.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:CKIT '<File_Name>'
        
        
        

   :param fileName: This control defines relative orabsolute file name.

.. method:: SaveCalibrationKitPorts(self, fileName, parameters, arraySize, VNAPorts, calUnitPorts)
           
        This function generates a cal kit file with the specified name
        containing the cal kit data of the active calibration unit. The cal
        kit file can be stored in the calibration unit or written to a
        directory on the analyzer.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:AUTO:CKIT:PORTs
        
        
        

   :param calUnitPorts: Port numbers of the calibration unit. For ann-port fixture compensation (n = 1 to 4), n arbitrary (not necessarilyconsecutive) port numbers must be specified.
   :param VNAPorts: Port numbers of the analyzer. Foran n-port fixture compensation (n = 1 to 4), n arbitrary (notnecessarily consecutive) port numbers must be specified.
   :param arraySize: This control sets the array size of the Portscontrol array.
   :param parameters: This control selects acalibration type.
   :param fileName: This control defines relative orabsolute file name.

.. method:: LoadCalibrationKit(self, connectorName, calibrationKitName, standard, calibrationKitLabel, fileName, portNumber1, portNumber2)
           
        This function loads cal kit data for a specific connector type, cal
        kit, and calibration standard from a specified Touchstone file,
        assigning a label for the cal data. A restriction on the port
        assignment may be defined in addition.
        
        Remote-control command(s):
        MMEMory:LOAD:CKIT:SDATa '<conn_name>', '<ckit_name>', MMTHrough |
        MFTHrough | FFTHrough | MMLine | MMLINE1 | MMLINE2 | MMLINE3 | MFLine
        | MFLINE1 | MFLINE2 | MFLINE3 | FFLine | FFLINE1 | FFLINE2 | FFLINE3 |
        MMATten | MFATten | FFATten | MMSNetwork | MFSNetwork | FFSNetwork |
        MOPen | FOPen | MSHort | FSHort | MOSHort | MOSHORT1 | MOSHORT2 |
        MOSHORT3 | FOSHort | FOSHORT1 | FOSHORT2 | FOSHORT3 | MREFlect |
        FREFlect | MMTCh | FMTCh | MSMatch | FSMatch, '<stdlabel_name>',
        '<file_name>' [,<port1_no>][,<port2_no>]
        
        

   :param portNumber1: This control specifies the port assignment: Oneport number for one-port standards, two port number for two-portstandards. If the port numbers are omitted, the cal kit data is validfor all ports.
   :param calibrationKitLabel: This control alabel for the cal kit data. An empty string means that no label isdefined.
   :param portNumber2: This control specifies the portassignment: One port number for one-port standards, two port numberfor two-port standards. If the port numbers are omitted, the cal kitdata is valid for all ports.
   :param calibrationKitName: This control specifiesthe name of a calibration kit available on the analyzer.
   :param fileName: This control specifies the nameand directory of the Touchstone file to be loaded. A *.s1p file mustbe used for one-port standards, a *.s2p file for two-port standards.If no path is specified the analyzer searches the current directory,to be queried with MMEMory:CDIRectory?.
   :param standard: This control selects a calibration standard from aspecified Touchstone file.
   :param connectorName: This control specifies thename of the connector type.

.. method:: SetCalibrationKitLabel(self, calibrationKitName, label)
           
        This function assigns a label to an imported or user-defined
        calibration kit.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:LABel '<ckit_name>', '<label>'
        
        

   :param calibrationKitName: This control definesthe name of the imported or user-defined calibration kit.
   :param label: This control defines the label of thecalibration kit.

.. method:: RenameCalibrationKit(self, calibrationKitName, label, newLabel)
           
        This function renames an existing calibration kit label.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:LLABel
        
        

   :param calibrationKitName: This control definesthe name of the imported or user-defined calibration kit.
   :param newLabel: This control defines new label ofthe calibration kit.
   :param label: This control defines the label of thecalibration kit.

.. method:: GetCalibrationKitLabel(self, calibrationKitName, label)
           
        This function returns a label of an imported or user-defined
        calibration kit.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:LABel? '<ckit_name>'
        
        

   :param calibrationKitName: This control definesthe name of the imported or user-defined calibration kit.
   :param label: This control returns the label of thecalibration kit.

.. method:: DeleteCalibrationKit(self, calibrationKitName)
           
        This function deletes an imported or user-defined cal kit.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:DELete '<ckit_name>'
        
        

   :param calibrationKitName: This control definesthe name of calibration kit.

.. method:: DeleteCalibrationKitWithLabel(self, calibrationKitName, calibrationKitLabel)
           
        This function deletes an imported or user-defined cal kit which is
        identified by its cal kit name and label.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:CKIT:LDELete '<ckit_name>', '<ckit_label>'
        
        
        

   :param calibrationKitLabel: String parametercontaining the label of an imported or user-defined calibration kitavailable on the analyzer.
   :param calibrationKitName: This control definesthe name of calibration kit.

.. method:: ImportKit(self, fileName)
           
        This function loads cal kit data from a specified NWA cal kit file.
        
        Notes:
        (1) The loaded file must be a NWA-specific cal kit file with the
        extension *.calkit. ZVR cal kit files can be imported using the
        [SENSe<Ch>:]CORRection:CKIT:INSTall command. Agilent cal kit files can
        be imported manually and converted into *.calkit files.
        
        Remote-control command(s):
        MMEMory:LOAD:CKIT '<file_name>'
        
        

   :param fileName: This control specifies the nameand directory of the cal kit file to be loaded. If no path isspecified the analyzer searches the current directory, to be queriedwith MMEMory:CDIRectory?.

.. method:: AdditionalDirectoryCalibrationKit(self, directory)
           
        This function specifies the Directory for Additionally Available Cal
        Kits and Conn Types. All cal kit files in the special directory will
        be (re-)loaded automatically every time the NWA application is
        started.
        
        
        Remote-control command(s):
        MMEMory:LOAD:CKIT:UDIRectory '<directory>'
        
        

   :param directory: String parameter to specify thedirectory path. The directory can be created separately(MMEMory:MDIRectory). An empty string means that no cal kit files willbe loaded.

.. method:: ExportKit(self, kitName, fileName)
           
        This function stores the data of a calibration kit to a specified
        file.
        
        Remote-control command(s):
        MMEMory:STORe:CKIT '<kit_name>', '<file_name>'
        
        

   :param kitName: This control specifies the nameof a user-defined calibration kit available on the analyzer. If nopath is specified the analyzer uses the current directory, to bequeried with MMEMory:CDIRectory?.
   :param fileName: This control specifies the nameand directory of the cal kit file to be created. The file is a NWA-specific cal kit file with the extension *.calkit.

.. method:: ExportKitWithLabel(self, kitName, kitLabel, fileName)
           
        Stores the data of a calibration kit to a specified file. The
        calibration kit is identified by its name and label.
        
        Remote-control command(s):
        MMEMory:STORe:CKIT:WLABel
        
        

   :param kitName: This control specifies the nameof a user-defined calibration kit available on the analyzer. If nopath is specified the analyzer uses the current directory, to bequeried with MMEMory:CDIRectory?.
   :param kitLabel: Label of the calibration kit,usually its serial number.
   :param fileName: This control specifies the nameand directory of the cal kit file to be created. The file is a NWA-specific cal kit file with the extension *.calkit.

.. method:: ResetOffsets(self, channel=1)
           
        This function resets the offset parameters for all test ports to zero.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:OFFSet<port_no>:STATe OFF
        
        

   :param channel: Channel number.

.. method:: QueryResetOffsets(self, channel=1)
           
        This function queries whether any of the offset parameters are
        different from zero.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:OFFSet<port_no>:STATe?
        
        

   :param channel: Channel number.
   :return: offsets

.. method:: SetElectricalLength(self, channel=1, port, electricalLength)
           
        This function defines the offset parameter for test port <Port> as an
        electrical length.
        
        Note(s):
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EDELay<port_no>:ELENgth
        
        

   :param electricalLength: This control defines the offset parameterfor test port <Port> as an electrical length.
   :param port: Port number of the analyzer.
   :param channel: Channel number.

.. method:: GetElectricalLength(self, channel=1, port)
           
        This function queries the offset parameter for test port <Port> as an
        electrical length.
        
        Note(s):
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EDELay<port_no>:ELENgth?
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number.
   :return: electricalLength

.. method:: ConfigureMechanicalLength(self, channel=1, port, mechanicalLength, permittivity)
           
        This function configures parameters of mechanical length.
        
        Note(s):
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EDELay<port_no>:DISTance
        [SENSe<Ch>:]CORRection:EDELay<port_no>:DIELectric
        
        

   :param permittivity: This control defines thepermittivity for the offset correction at test port <Port>.
   :param port: Port number of the analyzer.
   :param channel: Channel number.
   :param mechanicalLength: This control defines the offset parameterfor test port <Port> as a mechanical length.

.. method:: SetMechanicalLength(self, channel=1, port, mechanicalLength)
           
        This function defines the offset parameter for test port <Port> as a
        mechanical length.
        
        Note(s):
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EDELay<port_no>:DISTance
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number.
   :param mechanicalLength: This control defines the offset parameterfor test port <Port> as a mechanical length.

.. method:: GetMechanicalLength(self, channel=1, port)
           
        This function queries the offset parameter for test port <Port> as a
        mechanical length.
        
        Note(s):
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EDELay<port_no>:DISTance?
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number.
   :return: mechanicalLength

.. method:: SetPermittivity(self, channel=1, port, permittivity)
           
        This function defines the permittivity for the offset correction at
        test port <Port>.
        
        Note(s):
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EDELay<port_no>:DIELectric
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number.
   :param permittivity: This control defines the permittivity for theoffset correction at test port <Port>.

.. method:: GetPermittivity(self, channel=1, port)
           
        This function returns the permittivity for the offset correction at
        test port <Port>.
        
        Note(s):
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EDELay<port_no>:DIELectric?
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number.
   :return: permittivity

.. method:: ConfigureLoss(self, channel=1, port, lossAtDC, lossAtFrequency, lossReferenceFrequency)
           
        This function configures parameters of One-way Loss.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:LOSS<port_no> <DC_loss>
        [SENSe<Ch>:]CORRection:LOSS<port_no>:OFFSet <ref_loss>
        [SENSe<Ch>:]CORRection:LOSS<port_no>:FREQuency <ref_frequency>
        
        

   :param lossReferenceFrequency: This control defines the reference frequency.
   :param lossAtDC: This control defines the frequency-independent part(DC value) of the offset loss.
   :param lossAtFrequency: Thiscontrol defines the offset loss at the reference frequency.
   :param port: Port number of the analyzer.
   :param channel: Channel number of the offset-corrected channel.

.. method:: SetLossAtDC(self, channel=1, port, lossAtDC)
           
        This function defines the frequency-independent part (DC value) of the
        offset loss.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:LOSS<port_no> <DC_loss>
        
        

   :param lossAtDC: This control defines the frequency-independent part(DC value) of the offset loss.
   :param port: Port number of the analyzer.
   :param channel: Channel number of the offset-corrected channel.

.. method:: GetLossAtDC(self, channel=1, port)
           
        This function returns the frequency-independent part (DC value) of the
        offset loss.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:LOSS<port_no>?
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number of the offset-corrected channel.
   :return: lossAtDC

.. method:: SetLossAtFrequency(self, channel=1, port, lossAtFrequency)
           
        This function defines the offset loss at the reference frequency
        ([SENSe<Ch>:]CORRection:LOSS<port_no>:FREQuency).
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:LOSS<port_no>:OFFSet <ref_loss>
        
        

   :param lossAtFrequency: This control defines the offset loss at thereference frequency.
   :param port: Port number of the analyzer.
   :param channel: Channel number of the offset-corrected channel.

.. method:: GetLossAtFrequency(self, channel=1, port)
           
        This function returns the offset loss at the reference frequency
        ([SENSe<Ch>:]CORRection:LOSS<port_no>:FREQuency).
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:LOSS<port_no>:OFFSet?
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number of the offset-corrected channel.
   :return: lossAtFrequency

.. method:: SetLossReferenceFrequency(self, channel=1, port, lossReferenceFrequency)
           
        This function defines the reference frequency for the frequency-
        dependent part of the offset loss
        ([SENSe<Ch>:]CORRection:LOSS<port_no>:OFFSet).
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:LOSS<port_no>:FREQuency <ref_frequency>
        
        

   :param lossReferenceFrequency: This control defines the referencefrequency.
   :param port: Port number of the analyzer.
   :param channel: Channel number of the offset-corrected channel.

.. method:: GetLossReferenceFrequency(self, channel=1, port)
           
        This function returns the reference frequency for the frequency-
        dependent part of the offset loss
        ([SENSe<Ch>:]CORRection:LOSS<port_no>:OFFSet).
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:LOSS<port_no>:FREQuency?
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number of the offset-corrected channel.
   :return: lossReferenceFrequency

.. method:: SetDelay(self, channel=1, port, delay)
           
        This function defines the offset parameter for test port <Port> as a
        delay time.
        
        Note(s):
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EDELay<port_no>[:TIME]
        
        

   :param delay: This control defines the offset parameter for test port <Port> as a delay time.
   :param port: Port number of the analyzer.
   :param channel: Channel number.

.. method:: GetDelay(self, channel=1, port)
           
        This function queries the offset parameter for test port <Port> as a
        delay time.
        
        Note(s):
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EDELay<port_no>[:TIME]?
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number.
   :return: delay

.. method:: QueryDirectFixtureCompensation(self, channel=1, port)
           
        Returns whether a direct fixture compensation has been carried out at
        port no. <port_no>. A direct fixture compensation resets the offset
        parameters to zero, the analyzer uses calculated transmission factors
        instead.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:OFFSet<port_no>:DFComp[:STATe]?
        
        

   :param port: Port number.
   :param channel: Channel number.
   :return: directFixtureCompensation

.. method:: AutoLength(self, channel=1, port)
           
        This function defines the offset parameter for the active test port such that the residual delay of the active trace is minimized across
        the entire sweep range.
        
        Note(s):
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:EDELay<port_no>:AUTO ONCE
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number.

.. method:: AutoLengthAndLoss(self, channel=1, port)
           
        This function determines all offset parameters such that the residual
        group delay of the active trace (defined as the negative derivative of
        the phase response) is minimized and the measured loss is minimized as
        far as possible across the entire sweep range.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:LOSS<port_no>:AUTO ONCE
        
        

   :param port: Port number of the analyzer.
   :param channel: Channel number of the offset-corrected channel.

.. method:: AcquireFixtureCompensationSweep(self, channel=1, standardType, arraySize, ports)
           
        Starts a fixture compensation sweep in order to acquire measurement
        data for a test fixture that has its inner conductor terminated with
        the selected standards.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:FIXTure[:ACQuire] OPEN | SHORT,
        <port_no>{,<port_no>}
        
        

   :param standardType: This control specifies type of circuit.
   :param arraySize: This control sets the array size of the Portscontrol array.
   :param channel: Channel number.
   :param ports: Port numbers of the analyzer. For ann-port fixture compensation (n = 1 to 4), n arbitrary (not necessarilyconsecutive) port numbers must be specified.

.. method:: StartFixtureCompensationSweep(self, channel=1)
           
        Prepares the analyzer for fixture compensation comprising a single or
        a series of fixture compensation sweeps. Previous compensation data is
        deleted.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:FIXTure:STARt
        
        

   :param channel: Channel number.

.. method:: SaveFixtureCompensationData(self, channel=1)
           
        Completes a fixture compensation, storing and applying the acquired
        data.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:FIXTure:SAVE
        
        

   :param channel: Channel number.

.. method:: SetFixtureCompensationAutoLengthAndLossCalculation(self, autoLengthAndLoss)
           
        This function configures Auto Length and Loss.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:FIXTure:LMParameter:LOSS[:STATe]
        
        

   :param autoLengthAndLoss: This control specifiesan Auto Length or an Auto Length and Loss calculation.

.. method:: GetFixtureCompensationAutoLengthAndLossCalculation(self, )
           
        Gets state of Auto Length or an Auto Length and Loss calculation.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:FIXTure:LMParameter:LOSS[:STATe]?
        
        
        

   :return: autoLengthAndLoss

.. method:: SetFixtureCompensationDirectCompensation(self, directCompensation)
           
        This function configures direct compensation.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:FIXTure:LMParameter[:STATe]
        
        

   :param directCompensation: This controlspecifies an Auto Length (and Loss) calculation or a DirectCompensation.

.. method:: GetFixtureCompensationDirectCompensation(self, )
           
        Returns a Direct Compensation.
        
        Remote-control command(s):
        [SENSe<Ch>:]CORRection:COLLect:FIXTure:LMParameter[:STATe]
        
        

   :return: directCompensation

.. method:: DiagramAreaAdd(self, window)
           
        This function creates a new diagram area, identified by its area
        number <Wnd>.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:STATe ON
        
        

   :param window: Number of the diagram area.

.. method:: DiagramAreaDelete(self, window)
           
        This function deletes a diagram area, identified by its area number
        <Wnd>.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:STATe OFF
        
        

   :param window: Number of the diagram area.

.. method:: DiagramAreaMaximize(self, window, diagramArea)
           
        This function maximizes all diagram areas in the active setup or
        restores the previous display configuration.
        
        Note(s):
        
        Number of the diagram area to become the active diagram area.
        DISPlay:WINDow<Wnd>:MAXimize acts on all diagrams of the current
        setup, however, the digram no. <Wnd> is displayed on top of the
        others.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:MAXimize <Boolean>
        
        

   :param window: Number of the diagram area.
   :param diagramArea: Maximizes all diagram areas in the active setup orrestores the previous display configuration.

.. method:: DiagramAreaTitle(self, window, title, titleString)
           
        This function defines a title for diagram area <Wnd>.
        
        Title provides an input field for the title string. The title may
        comprise a practically unlimited number of characters and is centered
        in a line below the top of the diagram area.
        
        Remote-control command(s):
        DISPlay:WINDow<Wnd>:TITLe[:STATe] <Boolean>
        DISPlay:WINDow<Wnd>:TITLe:DATA '<string>'
        
        

   :param window: Number of the diagram area.
   :param titleString: String variable for the title. The length of thetitle is practically unlimited but should be kept short enough to bedisplayed in the diagrams.
   :param title: Displays or hides the title for area number <Wnd>.

.. method:: DiagramAreaName(self, window, areaName)
           
        This function defines a name for diagram area <Wnd>.
        
        Note:
        
        (1) The name appears in the list of diagram areas, to be queried by
        DISPlay[:WINDow<Wnd>]:CATalog?.
        
        Remote-control command(s):
        DISPlay[:WINDow<Wnd>]:NAME '<string>'
        
        

   :param window: Number of the diagram area.
   :param areaName: String variable for the name.

.. method:: DiagramAreaCatalog(self, window, catalog, bufferSize)
           
        This function returns the numbers and names of all diagram areas in
        the current setup.
        
        Remote-control command(s):
        DISPlay[:WINDow<Wnd>]:CATalog?
        
        

   :param window: Number of the diagram area.
   :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.
   :param catalog: Returns string with comma-separated list of tracenumbers and names. If all traces have been deleted the response is anempty string ("").

.. method:: TraceDiagramAreaCatalog(self, window, catalog, bufferSize)
           
        This function returns the numbers and names of all traces in diagram
        area no. <Wnd>.
        
        Remote-control command(s):
        DISPlay[:WINDow<Wnd>]:TRACe<WndTr>:CATalog?
        
        

   :param window: Number of the diagram area.
   :param bufferSize: Pass the number of bytes in the ViChar array youspecify for the 'Catalog' parameter.
   :param catalog: Returns string with comma-separated list of tracenumbers and names. If all traces have been deleted the response is anempty string ("").

.. method:: SetColorScheme(self, colorScheme)
           
        This function selects the color scheme for all diagram areas in the
        active setup.
        
        Remote-control command(s):
        SYSTem:DISPlay:COLor DBACkground | LBACkground | BWLStyles | BWSolid
        
        

   :param colorScheme: Selects the color scheme forall diagram areas in the active setup.

.. method:: GetColorScheme(self, )
           
        This function returns color scheme used for all diagram areas in the
        active setup.
        
        Remote-control command(s):
        SYSTem:DISPlay:COLor?
        
        

   :return: colorScheme

.. method:: SaveColorScheme(self, fileName)
           
        This function stores a color scheme to a specified NWA color scheme
        file.
        
        Remote-control command(s):
        MMEMory:STORe:CMAP '<file_name>'
        
        

   :param fileName: This control specifies the nameand directory of the cal kit file to be created. If no path isspecified the analyzer uses the current directory, to be queried withMMEMory:CDIRectory?. The default extension (manual control) for colorscheme files is *.ColorScheme, although other extensions are allowed.

.. method:: LoadColorScheme(self, fileName)
           
        This function loads a color scheme from a specified NWA color scheme
        file.
        
        Remote-control command(s):
        MMEMory:LOAD:CMAP '<file_name>'
        
        

   :param fileName: This control specifies the nameand directory of the cal kit file to be loaded. The default extension(manual control) for color scheme files is *.ColorScheme, althoughother extensions are allowed.

.. method:: SetFrequencyInfo(self, frequencyInfo)
           
        This function shows or hides all frequency stimulus values in the
        diagrams.
        
        Remote-control command(s):
        DISPlay:ANNotation:FREQuency[:STATe] <Boolean>
        
        

   :param frequencyInfo: Show or hide stimulusvalues.

.. method:: GetFrequencyInfo(self, )
           
        This function returns whether all frequency stimulus values in the
        diagrams are displayed or not.
        
        Remote-control command(s):
        DISPlay:ANNotation:FREQuency[:STATe]?
        
        

   :return: frequencyInfo

.. method:: SetFontSize(self, fontSize)
           
        This function defines the size of the fonts in the diagram on a
        relative scale.
        
        Remote-control command(s):
        DISPlay:RFSize
        
        

   :param fontSize: Defines the size of the fonts inthe diagram on a relative scale.

.. method:: GetFontSize(self, )
           
        This function returns the size of the fonts in the diagram on a
        relative scale.
        
        Remote-control command(s):
        DISPlay:RFSize?
        
        

   :return: fontSize

.. method:: SetChannelInfo(self, channelInfo)
           
        This function shows or hides the channel list below the diagrams
        
        Remote-control command(s):
        DISPlay:ANNotation:CHANnel[:STATe] <Boolean>
        
        

   :param channelInfo: Shows or hides the channellist below the diagrams.

.. method:: GetChannelInfo(self, )
           
        This function returns whether the channel list below the diagrams
        
        Remote-control command(s):
        DISPlay:ANNotation:CHANnel[:STATe]?
        
        

   :return: channelInfo

.. method:: SetMarkerColorState(self, sameColor)
           
        This function displays all markers with the same color or display each
        marker with the color of the associated trace. The colors of all
        display elements are defined via DISPlay:CMAP<Element>:RGB <red>,
        <green>, <blue>,....
        
        Remote-control command(s):
        DISPlay:CMAP<Element>:MARKer[:STATe] <Boolean>
        
        
        

   :param sameColor: This control sets the markerscolor.

.. method:: GetMarkerColorState(self, )
           
        This function returns the markers color state - whether all displayed
        markers have the same color or each marker has the color of the
        associated trace.
        
        Remote-control command(s):
        DISPlay:CMAP<Element>:MARKer[:STATe]?
        
        
        

   :return: sameColor

.. method:: SetRGBColor(self, element, red, green, blue, traceStyle, traceWidth)
           
        This function defines the color of all display elements based on the
        Red/Green/Blue color model.
        
        Remote-control command(s):
        DISPlay:CMAP<Element>:RGB <red>, <green>, <blue> [,<trace_style>,
        <trace_width>]
        
        
        

   :param blue: Sets the blue color.
   :param traceWidth: Selects the trace width.
   :param element: Selects the display elements.
   :param traceStyle: Selects the trace style.
   :param green: Sets the green color.
   :param red: Sets the red color.

.. method:: GetRGBColor(self, element)
           
        This function returns color of all display elements based on the
        Red/Green/Blue color model.
        
        Remote-control command(s):
        DISPlay:CMAP<Element>:RGB?
        
        
        

   :param element: Selects the display elements.
   :return: red
   :return: green
   :return: blue
   :return: traceStyle
   :return: traceWidth

.. method:: SetTraceColorState(self, traceColor)
           
        This function defines the trace color schemes in different diagram
        areas.
        
        Remote-control command(s):
        DISPlay:CMAP<Element>:TRACe:COLor[:STATe] <Boolean>
        
        
        

   :param traceColor: This control defines thetrace color schemes in different diagram areas.

.. method:: GetTraceColorState(self, )
           
        This function returns the trace color schemes in different diagram
        areas.
        
        Remote-control command(s):
        DISPlay:CMAP<Element>:TRACe:COLor[:STATe]?
        
        

   :return: traceColor

.. method:: TraceSetRGBColor(self, traceName, red, green, blue, traceStyle, traceWidth)
           
        This function defines the color of selected trace based on the
        Red/Green/Blue color model.
        
        Remote-control command(s):
        DISPlay:CMAP<13..28>:RGB <red>, <green>, <blue> ,<trace_style>,
        <trace_width>
        
        
        

   :param blue: Sets the blue color.
   :param traceWidth: Selects the trace width.
   :param traceStyle: Selects the trace style.
   :param green: Sets the green color.
   :param red: Sets the red color.
   :param traceName: Trace name.

.. method:: TraceGetRGBColor(self, traceName)
           
        This function returns the color of selected trace based on the
        Red/Green/Blue color model.
        
        Remote-control command(s):
        DISPlay:CMAP<13..28>:RGB?
        
        

   :param traceName: Trace name.
   :return: red
   :return: green
   :return: blue
   :return: traceStyle
   :return: traceWidth

.. method:: SetPowerPortLimitState(self, channel=1, port, limitState)
           
        Enables or disables the limit for the source power at port no. <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]LLIMit[:STATe]
        
        

   :param limitState: Enables or disables the limit for the sourcepower at port no. <Pt>.
   :param port: Port number.
   :param channel: Channel number.

.. method:: GetPowerPortLimitState(self, channel=1, port)
           
        Queries the state of the limit for the source power at port no. <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]LLIMit[:STATe]?
        
        

   :param port: Port number.
   :param channel: Channel number.
   :return: limitState

.. method:: SetPowerPortLimitValue(self, channel=1, port, limitValue)
           
        Defines a limit for the source power at port no. <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]LLIMit:VALue
        
        

   :param limitValue: Defines a limit for the source power at port no.<Pt>.
   :param port: Port number.
   :param channel: Channel number.

.. method:: GetPowerPortLimitValue(self, channel=1, port)
           
        Queries a limit for the source power at port no. <Pt>.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]LLIMit:VALue?
        
        

   :param port: Port number.
   :param channel: Channel number.
   :return: limitValue

.. method:: SetPowerPortLimitDirectGeneratorAndReceiverState(self, channel=1, port, DRGAccessState)
           
        Optimizes the automatic level control (ALC) for test setups where the
        additional connectors of option R&S ZVA-B16 are used. If the
        optimization is enabled, the ALC is limited to +1 dB so that the
        active port power limits cannot be exceeded by more than 1 dB.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]LLIMit:DGRaccess
        
        

   :param DRGAccessState: Enables or disables ALC optimization.
   :param port: Port number.
   :param channel: Channel number.

.. method:: GetPowerPortLimitDirectGeneratorAndReceiverState(self, channel=1, port)
           
        Queries the state of the ALC optimization.
        
        Remote-control command(s):
        SOURce<Ch>:POWer<Pt>[:LEVel][:IMMediate]LLIMit:DGRaccess?
        
        

   :param port: Port number.
   :param channel: Channel number.
   :return: DRGAccessState

.. method:: SetPresets(self, presetScope)
           
        This function specifies whether a preset (SYSTem:PRESet; *RST) affects
        the active setup only or all open setups.
        
        Remote-control command(s):
        SYSTem:PRESet:SCOPe ALL | SINGle
        
        

   :param presetScope: This control specifies whethera preset (SYSTem:PRESet; *RST) affects the active setup only or allopen setups.

.. method:: GetPresets(self, )
           
        This function queries whether a preset (SYSTem:PRESet; *RST) affects
        the active setup only or all open setups.
        
        Remote-control command(s):
        SYSTem:PRESet:SCOPe?
        
        

   :return: presetScope

.. method:: SetPresetSettingsState(self, state)
           
        This function causes a *RST or SYSTem:PRESet command to restore a set
        of user-defined settings.
        
        Remote-control command(s):
        SYSTem:PRESet:REMote[:STATe]
        
        

   :param state: Preset settings state.

.. method:: GetPresetSettingsState(self, )
           
        This function queries preset settings state.
        
        Remote-control command(s):
        SYSTem:PRESet:REMote[:STATe]
        
        

   :return: state

.. method:: SetUserDefinedPresetState(self, userDefinedPreset)
           
        This function selects a factory preset or a user-defined preset.
        
        Remote-control command(s):
        SYSTem:PRESet:USER[:STATe] ON | OFF
        
        

   :param userDefinedPreset: This control selects afactory preset or a user-defined preset.

.. method:: GetUserDefinedPresetState(self, )
           
        This function returns a state of the user-defined preset.
        
        Remote-control command(s):
        SYSTem:PRESet:USER[:STATe]?
        
        

   :return: userDefinedPreset

.. method:: SetUserDefinedPresetFile(self, userDefinedPresetFile)
           
        This function specifies the name of a setup file (.nwa) to be used for
        a user-defined preset.
        
        Remote-control command(s):
        SYSTem:PRESet:USER:NAME '<Setup_file>'
        
        

   :param userDefinedPresetFile: This controlspecifies the name and directory of the setup file to be loaded. Thedefault extension (manual control) for setup files is *.nwa, althoughother extensions are allowed. If no path is specified the analyzersearches the default directory.

.. method:: GetUserDefinedPresetFile(self, bufferSize, userDefinedPresetFile)
           
        This function returns the name of a setup file (.nwa) used for a user-
        defined preset.
        
        Remote-control command(s):
        SYSTem:PRESet:USER:NAME?
        
        

   :param userDefinedPresetFile: This control returnsthe name of the user defined setup file.
   :param bufferSize: This control sets the buffersize for the control User Defined Preset.

.. method:: SetDisplayUpdate(self, displayUpdate)
           
        This function switches the display on or off while the analyzer is in
        the remote state. This function has no effect while the analyzer is in
        the Local operating state.
        
        Note(s):
        
        Switching off the display speeds up the measurement. This function may
        have an impact on the update of trace and channel settings; see
        SYSTem:SETTings:UPDate.
        
        Remote-control command(s):
        SYSTem:DISPlay:UPDate OFF | ON | ONCE
        
        

   :param displayUpdate: Switches the display updatewhile the analyzer is in the remote state.

.. method:: GetDisplayUpdate(self, )
           
        This function returns if the display update while the analyzer is in
        the remote state is enabled or disabled.
        
        Remote-control command(s):
        SYSTem:DISPlay:UPDate?
        
        

   :return: displayUpdate

.. method:: ImmediateSettingsUpdate(self, )
           
        This function initiates an immediate update of the channel or trace
        settings.
        
        This function has an effect if the analyzer operates in single sweep
        mode (INITiate<Ch>:CONTinuous OFF) and if the display update is
        switched off (SYSTem:DISPlay:UPDate OFF). In this scenario, a change
        of the channel or trace settings is usually not taken into account
        immediately. The analyzer waits until the end of the current sweep
        sequence and changes all settings made during the last sweep period
        when the next single sweep sequence is initiated. Several settings can
        be made en bloc, which generally saves time.
        
        SYSTem:SETtings:UPDate ONCE causes the analyzer to apply the settings
        at once without waiting for the end of the current single sweep
        sequence. This function has no effect in continuous sweep mode or if
        the display update is switched on.
        
        Note(s):
        
        The settings are also updated when the continuous sweep mode is
        activated (INITiate<Ch>:CONTinuous ON).
        
        Remote-control command(s):
        SYSTem:SETTings:UPDate ONCE
        
        


.. method:: QueryFrequencyRange(self, )
           
        Queries the minimum and maximum frequency of the network analyzer.
        
        Remote-control command(s):
        SYSTem:FREQuency? MINimum | MAXimum
        
        

   :return: minimumFrequency
   :return: maximumFrequency

.. method:: SystemKeylock(self, lockout)
           
        This function sets the local lockout.
        
        Remote-control command(s):
        :SYSTem:KLOCk ON | OFF
        
        

   :param lockout: This parameter sets the locallockout.

.. method:: SetRemoteLanguage(self, language)
           
        This function specifies the Remote Language for the analyzer.
        
        Remote-control command(s):
        SYSTem:LANGuage 'SCPI' | 'PNA' | 'HP8510' | 'HP8720' | 'HP8753'
        
        

   :param language: This parameter selects thecommand set.

.. method:: GetRemoteLanguage(self, )
           
        This function returns the Remote Language for the analyzer.
        
        Remote-control command(s):
        SYSTem:LANGuage?
        
        

   :return: language

.. method:: ConfigureExternalGenerator(self, generatorNumber, generatorName, generatorType, interfaceType, interfaceAddress, fastSweepMode, _10MHzReferenceFrequency)
           
        This function configures an external generator and adds it to the list
        of available generators.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:GENerator<gen_no>:DEFine
        '<gen_name>', '<driver>', '<interface>', '<address>'[, <fast_sweep>,
        <10_MHz_Ref>]
        
        

   :param fastSweepMode: This control enables ordisables the fast sweep mode.
   :param generatorNumber: This control sets thenumber of the configured generator. Generators must be numbered inascending order, starting with 1. If a number is re-used, the previousgenerator configuration is overwritten.
   :param interfaceType: This control sets theinterface type: 'GPIB0', 'VXI-11',...
   :param generatorName: This control sets the name of the externalgenerator. An empty string means that no particular name is assignedto the generator.
   :param _10MHzReferenceFrequency: This control sets the analyzer tointernal (OFF) or external (ON) reference frequency.
   :param generatorType: This control sets thegenerator type. The generator type is identical with the name of thegenerator driver file (*.gen) stored in the resources\extdevsubdirectory of the analyzer's program directory.
   :param interfaceAddress: This control sets theinterface address, depending on the interface type

.. method:: QueryExternalGenerator(self, generatorNumber, generatorName, generatorType, interfaceType, interfaceAddress)
           
        This function queries an external generator.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:GENerator<gen_no>:DEFine?
        
        

   :param generatorType: This control returns thegenerator type. The generator type is identical with the name of thegenerator driver file (*.gen) stored in the resources\extdevsubdirectory of the analyzer's program directory.
   :param generatorName: This control returns the name of the externalgenerator. An empty string means that no particular name is assignedto the generator.
   :param interfaceType: This control returns the interface type.
   :param interfaceAddress: This control returns the interface address,depending on the interface type fastSweepMode ViBoolean This controlreturns the fast sweep mode.
   :param generatorNumber: This control sets thenumber of the configured generator. Generators must be numbered inascending order, starting with 1. If a number is re-used, the previousgenerator configuration is overwritten.
   :return: fastSweepMode
   :return: _10MHzReferenceFrequency

.. method:: QueryExternalGeneratorCount(self, )
           
        Queries the number of configured external generators.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:GENerator<gen_no>:COUNt?
        
        

   :return: generatorCount

.. method:: QueryExternalGeneratorNumbers(self, arraySize, generatorNumbers)
           
        Queries the numbers of all configured external generators.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:GENerator<gen_no>:CATalog?
        
        

   :param generatorNumbers: String parameter with acomma-separated list of generator numbers.
   :param arraySize: This control sets the array sizeof the Generator Numbers control array.

.. method:: DeleteExternalGenerator(self, )
           
        This function clears the configuration table for external generators.
        
        Notes:
        
        (1) Generator number is ignored, the command clears all entries in the
        configuration table.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:GENerator<gen_no>:DELete
        
        


.. method:: ConfigureExternalPowerMeter(self, powerMeterNumber, powerMeterName, powerMeterType, interfaceType, interfaceAddress)
           
        This function configures an external power meter and adds it to the
        list of available power meters.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:PMETer<pmeter_no>:DEFine
        '<pmeter_name>', '<driver>', '<interface>', '<address>'
        
        

   :param powerMeterNumber: This control sets thenumber of the configured power meter. Power meters must be numbered inascending order, starting with 1. If a number is re-used, the previousgenerator configuration is overwritten.
   :param interfaceType: This control sets theinterface type: 'USB' (for the supported USB devices)
   :param interfaceAddress: This control sets theinterface address, depending on the interface type
   :param powerMeterType: This control sets the powermeter type. The power meter type is identical with the name of thepower meter driver file (*.pwm) stored in the resources\extdevsubdirectory of the analyzer's program directory.
   :param powerMeterName: This control sets the name of the externalpower meter. An empty string means that no particular name is assignedto the power meter.

.. method:: QueryExternalPowerMeter(self, powerMeterNumber, powerMeterName, powerMeterType, interfaceType, interfaceAddress)
           
        This function queries an external power meter.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:PMETer<pmeter_no>:DEFine?
        
        

   :param powerMeterNumber: This control sets thenumber of the configured power meter. Power meters must be numbered inascending order, starting with 1. If a number is re-used, the previousgenerator configuration is overwritten.
   :param interfaceType: This control returns the interface type.
   :param interfaceAddress: This control returns the interface address,depending on the interface type.
   :param powerMeterType: This control returns thepower meter type. The power meter type is identical with the name ofthe power meter driver file (*.pwm) stored in the resources\extdevsubdirectory of the analyzer's program directory.
   :param powerMeterName: This control returns the name of the externalpower meter. An empty string means that no particular name is assignedto the power meter.

.. method:: QueryExternalPowerMeterCount(self, )
           
        Queries the number of configured external power meters.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:PMETer<pmeter_no>:COUNt?
        
        

   :return: powerMeterCount

.. method:: QueryExternalPowerMeterNumbers(self, bufferSize, powerMeterNumber)
           
        Queries the numbers of all configured external power meters.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:PMETer<pmeter_no>:CATalog?
        
        

   :param powerMeterNumber: String parameter with acomma-separated list of power meter numbers
   :param bufferSize: This control defines size ofbuffer in 'Power Meter Number' argument.

.. method:: AutoZeroingExternalPowerMeter(self, powerMeterNumber)
           
        This function starts auto zeroing of the external power meter.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:PMETer<pmeter_no>:AZERo
        
        

   :param powerMeterNumber: This control sets thenumber of the configured power meter. Power meters must be numbered inascending order, starting with 1. If a number is re-used, the previousgenerator configuration is overwritten.

.. method:: SetAutoConfigNRPZxx(self, powerMeterNumber, autoConfig)
           
        This function enables or disables Auto Config NRP-Zxx.
        
        Note:
        
        (1) If the function is enabled, the analyzer automatically configures
        the first power meter detected at one of the USB ports as Pmtr 1.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:PMETer<pmeter_no>:CONFigure:AUTO[:STATe]
        <Boolean>
        
        

   :param powerMeterNumber: This control sets thenumber of the configured power meter. Power meters must be numbered inascending order, starting with 1. If a number is re-used, the previousgenerator configuration is overwritten.
   :param autoConfig: Enables or disables Auto Config NRP-Zxx.

.. method:: GetAutoConfigNRPZxx(self, powerMeterNumber)
           
        This function returns the Auto Config NRP-Zxx state.
        
        Note:
        
        (1) If the function is enabled, the analyzer automatically configures
        the first power meter detected at one of the USB ports as Pmtr 1.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:PMETer<pmeter_no>:CONFigure:AUTO[:STATe]?
        
        

   :param powerMeterNumber: This control sets thenumber of the configured power meter. Power meters must be numbered inascending order, starting with 1. If a number is re-used, the previousgenerator configuration is overwritten.
   :return: autoConfig

.. method:: DeleteExternalPowerMeter(self, )
           
        This function clears the configuration table for external power
        meters.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:PMETer<pmeter_no>:DELete
        
        


.. method:: SetAlarmSoundsState(self, alarmSounds)
           
        This function switches alarm sounds on or off.
        
        Remote-control command(s):
        SYSTem:SOUNd:ALARm[:STATe] <Boolean>
        
        

   :param alarmSounds: Switches alarm sounds on oroff.

.. method:: GetAlarmSoundsState(self, )
           
        This function returns alarm sounds state.
        
        Remote-control command(s):
        SYSTem:SOUNd:ALARm[:STATe]?
        
        

   :return: alarmSounds

.. method:: SetRestartBehavior(self, restartBehavior)
           
        This function Defines the restart behavior of the instrument.
        
        Remote-control command(s):
        SYSTem:TRESet[:STATe] <Boolean>
        
        

   :param restartBehavior: Defines the restartbehavior of the instrument.

.. method:: GetRestartBehavior(self, )
           
        This function returns the restart behavior of the instrument.
        
        Remote-control command(s):
        SYSTem:TRESet[:STATe]?
        
        

   :return: restartBehavior

.. method:: SetStatusSoundsState(self, statusSounds)
           
        This function switches status sounds on or off.
        
        Remote-control command(s):
        SYSTem:SOUNd:STATus[:STATe] <Boolean>
        
        

   :param statusSounds: Switches status sounds onor off.

.. method:: GetStatusSoundsState(self, )
           
        This function returns status sounds state.
        
        Remote-control command(s):
        SYSTem:SOUNd:STATus[:STATe]?
        
        

   :return: statusSounds

.. method:: SetDataTransfer(self, dataTransfer)
           
        This function controls whether binary data is transferred in normal or
        swapped byte order.
        
        Remote-control command(s):
        FORMat:BORDer NORMal | SWAPped
        
        

   :param dataTransfer: Controls whether binary datais transferred in normal or swapped byte order.

.. method:: GetDataTransfer(self, )
           
        This function returns whether binary data is transferred in normal or
        swapped byte order.
        
        Remote-control command(s):
        FORMat:BORDer?
        
        

   :return: dataTransfer

.. method:: SetErrorDisplayState(self, errorDisplay)
           
        This function switches the display of a tooltip for remote command
        errors on or off. The tooltip appears at the bottom of the remote
        screen and of the manual screen; it is not displayed for SCPI errors
        no. -113, Undefined header.
        
        Remote-control command(s):
        SYSTem:ERRor:DISPlay <Boolean>
        
        

   :param errorDisplay: Switches the display of atooltip for remote command errors on or off.

.. method:: GetErrorDisplayState(self, )
           
        This function returns the display of a tooltip for remote command
        errors.
        
        Remote-control command(s):
        SYSTem:ERRor:DISPlay?
        
        

   :return: errorDisplay

.. method:: SetFrequencyConversionType(self, converterType)
           
        This function selects the frequency converter type for enhanced
        frequency-converting measurements (with option ZVA-K8, Enhanced
        Frequency Conversion).
        
        Note(s):
        
        (1) This function is available only on R&S ZVA and ZVT instrument.
        
        Remote-control command(s):
        SENSe<Ch>:FREQuency:CONVersion:DEVice:NAME '<Converter Type>'
        
        
        

   :param converterType: Selects the frequencyconverter.

.. method:: GetFrequencyConversionType(self, bufferSize, converterType)
           
        This function returns the frequency converter type for enhanced
        frequency-converting measurements (with option ZVA-K8, Enhanced
        Frequency Conversion).
        
        Note(s):
        
        (1) This function is available only on R&S ZVA and ZVT instrument.
        
        Remote-control command(s):
        SENSe<Ch>:FREQuency:CONVersion:DEVice:NAME?
        
        

   :param converterType: Returns the frequencyconverter.
   :param bufferSize: This control defines the sizeof array passed to argument 'Converter Type'.

.. method:: SetFrequencyConversionSource(self, conversionSource)
           
        This function selects the test setup (internal or external sources)
        for the frequency converter measurement (with option ZVA-K8, Enhanced
        Frequency Conversion).
        
        
        Note(s):
        
        (1) This function is available only on R&S ZVA and ZVT instrument.
        
        Remote-control command(s):
        SENSe<Ch>:FREQuency:CONVersion:DEVice:MODE RILI | RILE
        
        

   :param conversionSource: Selects the test setup(internal or external sources) for the frequency convertermeasurement.

.. method:: GetFrequencyConversionSource(self, )
           
        This function returns the test setup (internal or external sources)
        for the frequency converter measurement (with option ZVA-K8, Enhanced
        Frequency Conversion).
        
        
        Note(s):
        
        (1) This function is available only on R&S ZVA and ZVT instrument.
        
        Remote-control command(s):
        SENSe<Ch>:FREQuency:CONVersion:DEVice:MODE?
        
        

   :return: conversionSource

.. method:: SetFastMultiportCorrection(self, fastMultiportCorrection)
           
        This function enables or disables Fast Multiport Correction.
        
        Remote-control command(s):
        SYSTem:CORRection:FMPort[:STATe]
        
        

   :param fastMultiportCorrection: Enables ordisables Fast Multiport Correction.

.. method:: GetFastMultiportCorrection(self, )
           
        This function returns the state of the Fast Multiport Correction.
        
        Remote-control command(s):
        SYSTem:CORRection:FMPort[:STATe]?
        
        

   :return: fastMultiportCorrection

.. method:: SetPowerCoeficients(self, port, coeficient)
           
        Defines power coefficients for frequency converters R&S ZVA-ZxxxE.
        
        Notes:
        
        (1) This command is available for frequency converters with electronic
        attenuators R&S ZVA-ZxxxE.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:DEVice:PCOefficient<Port> <C0>, <C1>,
        <C2>, <C3>
        
        
        

   :param port: Test port number of the analyzer
   :param coeficient: Array of 4 power coefficients.

.. method:: GetPowerCoeficients(self, port, coeficients)
           
        Returns power coefficients for frequency converters R&S ZVA-ZxxxE
        
        Notes:
        
        (1) This command is available for frequency converters with electronic
        attenuators R&S ZVA-ZxxxE.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:DEVice:PCOefficient<Port>?
        
        

   :param port: Test port number of the analyzer
   :param coeficients: Returned array of powercoefficients for frequency converters R&S ZVA-ZxxxE.

.. method:: SetPowerCoeficientsDefault(self, defaultCoeficients)
           
        Enables or disables default power coefficients for frequency
        converters R&S ZVA-ZxxxE.
        
        Notes:
        
        (1) This command is available for frequency converters with electronic
        attenuators R&S ZVA-ZxxxE.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:DEVice:PCOefficient<Port>:DEFault
        
        
        

   :param defaultCoeficients: This control enablesor disables default power coefficients for frequency converters R&SZVA-ZxxxE.

.. method:: GetPowerCoeficientsDefault(self, )
           
        Returns the state of the default power coefficients for frequency
        converters R&S ZVA-ZxxxE.
        
        Notes:
        
        (1) This command is available for frequency converters with electronic
        attenuators R&S ZVA-ZxxxE.
        
        Remote-control command(s):
        [SENSe<Ch>:]FREQuency:CONVersion:DEVice:PCOefficient<Port>:DEFault?>
        
        
        

   :return: defaultCoeficients

.. method:: QueryExtensionUnitDeviceID(self, bufferSize, deviceID)
           
        Queries the device ID of a connected extension unit ZVAXxx.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:EUNit:IDN?
        
        

   :param bufferSize: This control sets the buffersize for the control Device ID.
   :param deviceID: Manufacturer, type of theextension unit, 10-digit order number, serial number, see examplebelow. If no extension unit is connected, an execution error isgenerated.

.. method:: QueryExtensionUnitHardwareOptions(self, bufferSize, options)
           
        Queries the hardware options of a connected extension unit ZVAXxx.
        
        Remote-control command(s):
        SYSTem:COMMunicate:RDEVice:EUNit:OPT?
        
        

   :param bufferSize: This control sets the buffersize for the control Device ID.
   :param options: Comma-separated list of options.

.. method:: SetNWAApplicationPriority(self, priority)
           
        Selects the priority of the running NWA application.
        
        Remote-control command(s):
        SYSTem:PRIority NORMal | ANORmal | HIGH
        
        

   :param priority: Selects the priority of therunning NWA application.

.. method:: GetNWAApplicationPriority(self, )
           
        Queries the priority of the running NWA application.
        
        Remote-control command(s):
        SYSTem:PRIority?
        
        

   :return: priority

.. method:: SystemShutdown(self, )
           
        Switches the analyzer to the standby state.
        
        Remote-control command(s):
        SYSTem:SHUTdown
        
        


.. method:: GenerateSystemReport(self, fileName)
           
        This function generates a System Report and writes it to the specified
        file. See Obtaining Support.
        
        Remote-control command(s):
        DIAGnostic:DEVice:STATe '<file_name>'
        
        

   :param fileName: String parameter containing thefile name. If no path is specified, the file is stored to thedirectory C:\Rohde&Schwarz\Nwa\Report; the extension *.zip isappended automatically.

.. method:: SetCalculationOfBandfilterCenterFrequency(self, channel=1, marker, centerFrequencyCalculation)
           
        This function specifies how the center frequency of a bandfilter
        search is calculated.
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:FUNCtion:BWIDth:GMCenter <Boolean>
        
        

   :param marker: Marker number in the range 1 to 10. This numeric suffixis ignored and may be set to any value because the bandfilter searchfunctions always use markers M 1 to M 4.
   :param centerFrequencyCalculation: Specifies how the center frequencyof a bandfilter search is calculated.
   :param channel: Channel number.

.. method:: GetCalculationOfBandfilterCenterFrequency(self, channel=1, marker)
           
        This function returns how the center frequency of a bandfilter search
        is calculated.
        
        Remote-control command(s):
        CALCulate<Chn>:MARKer<Mk>:FUNCtion:BWIDth:GMCenter?
        
        

   :param marker: Marker number in the range 1 to 10. This numeric suffixis ignored and may be set to any value because the bandfilter searchfunctions always use markers M 1 to M 4.
   :param channel: Channel number.
   :return: centerFrequencyCalculation

.. method:: SetRFOffBehavior(self, RFOffBehavior)
           
        This function configures the behavior of the RF Off switches.
        
        Remote-control command(s):
        OUTPut<1...2>[:STATe]:TYPE
        
        

   :param RFOffBehavior: Configures the behavior ofthe RF Off switches.

.. method:: GetRFOffBehavior(self, )
           
        This function queries the behavior of the RF Off switches.
        
        Remote-control command(s):
        OUTPut<1...2>[:STATe]:TYPE?
        
        

   :return: RFOffBehavior

.. method:: SetRemoteDisplayTitle(self, title)
           
        This function configures a title for the remote display.
        
        Remote-control command(s):
        SYSTem:USER:DISPlay:TITLe 'title'
        
        

   :param title: This control sets the title to bedisplayed in remote control.

.. method:: GetRemoteDisplayTitle(self, bufferSize, title)
           
        This function queries title for the remote display.
        
        Remote-control command(s):
        SYSTem:USER:DISPlay:TITLe?
        
        

   :param bufferSize: This control defines size ofbuffer in 'title' argument.
   :param title: This control returns the title tobe displayed in remote control.

.. method:: SetAnalyzerHostname(self, hostName)
           
        This function sets the analyzer's host name (computer name). The
        domain is not included.
        
        Remote-control command(s):
        SYSTem:COMMunicate:NET:HOSTname '<host_name>'
        
        
        

   :param hostName: This control sets the analyzer'shost name (computer name). The domain is not included.

.. method:: GetAnalyzerHostname(self, bufferSize, hostName)
           
        This function queries the analyzer's host name (computer name). The
        domain is not included.
        
        Remote-control command(s):
        SYSTem:COMMunicate:NET:HOSTname?
        
        

   :param hostName: This control returns theanalyzer's host name (computer name). The domain is not included.
   :param bufferSize: This control defines size ofbuffer in 'hostname' argument.

.. method:: SetSoftKeyLabel(self, keyNumber, label)
           
        This function assigns the label to the soft key 1...8. The label may
        contain the '\n'- character to form multiline labels.
        
        Remote-control command(s):
        :SYSTem:USER:FKEY 0
        :SYSTem:USER:FKEY <1...8>,'<Label>'
        
        

   :param keyNumber: Sets the softkey number.
   :param label: Sets the key label Valid Values:any string

.. method:: GetPressedSoftKey(self, bufferSize, label)
           
        This function returns the number and label of the softkey pressed most
        recently. If no softkey was pressed, the string 0,'' is returned.
        
        Remote-control command(s):
        :SYSTem:USER:FKEY?
        
        

   :param bufferSize: This control defines the size of array passed toargument 'Label'.
   :param label: Returns the key label 
   :return: keyNumber

.. method:: SetOutputPortBits(self, outputPort, portBits)
           
        This function sets a channel-dependent bit pattern to the output ports
        A or B of the Universal Interface (option R&S ZVAB-B14). The channel
        bits are combined with the (static) output bits defined via
        CONTrol:HANDler:A|B[:DATA] using a logical "or" operation. The channel
        bits must be defined while the channel is active (CONTrol:NSELect
        <Ch>); the corresponding signals will be in effect while the channel
        is measured (dynamic output signals).
        
        Remote-control command(s):
        CONTrol:AUXiliary:A[:DATA]
        CONTrol:AUXiliary:B[:DATA]
        
        

   :param outputPort: This Control defines the outputport of the Universal Interface for write a channel-dependent bitpattern.
   :param portBits: This control setsa channel-dependent bit pattern to the output ports A or B of theUniversal Interface. The channel bits must be defined while thechannel is active.

.. method:: GetOutputPortBits(self, outputPort)
           
        This function queries a channel-dependent bit pattern to the output
        ports A or B of the Universal Interface (option R&S ZVAB-B14). The
        channel bits are combined with the (static) output bits defined via
        CONTrol:HANDler:A|B[:DATA] using a logical "or" operation. The channel
        bits must be defined while the channel is active (CONTrol:NSELect
        <Ch>); the corresponding signals will be in effect while the channel
        is measured (dynamic output signals).
        
        Remote-control command(s):
        CONTrol:AUXiliary:<A|B>[:DATA]?
        
        

   :param outputPort: This Control defines the outputport of the Universal Interface for read a channel-dependent bitpattern.
   :return: portBits

.. method:: SetChannelBits(self, channelBits)
           
        This function sets a channel-dependent four-bit decimal value to
        control four independent output signals at the USER CONTROL connector
        (applied to pins 8, 9, 10, 11). The output signals are 3.3 V TTL
        signals which can be used to differentiate between up to 16
        independent analyzer states. This function itself does not change the
        analyzer state.
        
        Remote-control command(s):
        CONTrol:AUXiliary:C[:DATA]
        
        

   :param channelBits: This control sets a channel-dependent four-bit decimal value to control four independent outputsignals at the USER CONTROL connector (applied to pins 8, 9, 10, 11).

.. method:: GetChannelBits(self, )
           
        This function queries a channel-dependent four-bit decimal value to
        control four independent output signals at the USER CONTROL connector
        (applied to pins 8, 9, 10, 11). The output signals are 3.3 V TTL
        signals which can be used to differentiate between up to 16
        independent analyzer states. This function itself does not change the
        analyzer state.
        
        Remote-control command(s):
        CONTrol:AUXiliary:C[:DATA]?
        
        

   :return: channelBits

.. method:: SetUIDirection(self, port, direction)
           
        This function controls the direction of the data flow at ports A, B,
        C, D. The direction at the combined ports E and F is according to the
        configuration at the other ports.
        
        Remote-control command(s):
        CONTrol:HANDler:A:MODE INPut | OUTPut
        CONTrol:HANDler:B:MODE INPut | OUTPut
        CONTrol:HANDler:C:MODE INPut | OUTPut
        CONTrol:HANDler:D:MODE INPut | OUTPut
        
        
        

   :param direction: Sets thedirection of the data flow at ports A, B, C, D
   :param port: This Control defines the port of theUniversal Interface.

.. method:: GetUIDirection(self, port)
           
        This function reads the direction of the data flow at ports A, B, C,
        D. The direction at the combined ports E and F is according to the
        configuration at the other ports.
        
        Remote-control command(s):
        CONTrol:HANDler:A:MODE?
        CONTrol:HANDler:B:MODE?
        CONTrol:HANDler:C:MODE?
        CONTrol:HANDler:D:MODE?
        
        
        

   :param port: This Control defines the port of theUniversal Interface.
   :return: direction

.. method:: SetUIData(self, port, data)
           
        This function write data to ports A, B, C, D, E, F. To write data to a
        port, the port must be configured as an output port. The port lines
        have negative logic: A "0" at a pin corresponds to a high signal, a
        "1" to a low signal.
        
        Remote-control command(s):
        CONTrol:HANDler:A[:DATA] <decimal>
        CONTrol:HANDler:B[:DATA] <decimal>
        CONTrol:HANDler:C[:DATA] <decimal>
        CONTrol:HANDler:D[:DATA] <decimal>
        CONTrol:HANDler:E[:DATA] <decimal>
        CONTrol:HANDler:F[:DATA] <decimal>
        
        
        

   :param data: This control writesdata to ports A, B, C, D, E, F
   :param port: This Control defines the output port of the Universal Interface.

.. method:: GetUIData(self, port)
           
        This function reads data from ports A, B, C, D, E, F. If the port is
        an output port, the queries return the last value that was written to
        the port.
        
        Remote-control command(s):
        CONTrol:HANDler:A[:DATA]?
        CONTrol:HANDler:B[:DATA]?
        CONTrol:HANDler:C[:DATA]?
        CONTrol:HANDler:D[:DATA]?
        CONTrol:HANDler:E[:DATA]?
        CONTrol:HANDler:F[:DATA]?
        
        
        

   :param port: This Control defines the output port of the Universal Interface.
   :return: data

.. method:: SetUISignalPin20(self, pin20)
           
        This function selects the digital signal that is routed to pin 20 of
        the Universal Interface connector.
        
        Remote-control command(s):
        CONTrol:HANDler[:EXTension]:INDex:STATe
        
        

   :param pin20: Selects the digital signal that isrouted to pin 20 of the Universal Interface connector

.. method:: GetUISignalPin20(self, )
           
        This function returns the digital signal that is routed to pin 20 of
        the Universal Interface connector.
        
        Remote-control command(s):
        CONTrol:HANDler[:EXTension]:INDex:STATe
        
        

   :return: pin20

.. method:: SetUISignalPin21(self, pin21)
           
        This function selects the digital signal that is routed to pin 21 of
        the Universal Interface connector.
        
        Remote-control command(s):
        CONTrol:HANDler[:EXTension]:RTRigger:STATe
        
        

   :param pin21: Selects the digital signal that isrouted to pin 21 of the Universal Interface connector

.. method:: GetUISignalPin21(self, )
           
        This function returns the digital signal that is routed to pin 21 of
        the Universal Interface connector.
        
        Remote-control command(s):
        CONTrol:HANDler[:EXTension]:RTRigger:STATe?
        
        
        

   :return: pin21

.. method:: SetUIPortBinaryData(self, port, data)
           
        Writes a 0 or 1 to the output ports (pin 3 or 4) of the Universal
        Interface connector. The port lines have negative logic: A "0"
        corresponds to a high signal, a "1" to a low signal.
        
        Remote-control command(s):
        CONTrol:HANDler:OUTPut<port>[:DATA]
        
        
        

   :param data: Writes a 0 or 1 to the output ports (pin3 or 4) of the Universal Interface connector.
   :param port: Output port number.

.. method:: GetUIPortBinaryData(self, port)
           
        Reads the last value that has been written to the output port.
        
        Remote-control command(s):
        CONTrol:HANDler:OUTPut<port>[:DATA]?
        
        
        

   :param port: Output port number.
   :return: data

.. method:: SetUIPortNextState(self, port, nextState)
           
        Defines the state of the output ports (pin 3 or 4) of the Universal
        Interface connector after the next negative pulse on the Input 1 line
        (pin 2).
        
        Remote-control command(s):
        CONTrol:HANDler:OUTPut<port>:USER
        
        
        

   :param port: Output port number.
   :param nextState: Defines the state of the outputports (pin 3 or 4) of the Universal Interface connector after the nextnegative pulse on the Input 1 line (pin 2).

.. method:: GetUIPortNextState(self, port)
           
        Returns the state of the output ports (pin 3 or 4) of the Universal
        Interface connector after the next negative pulse on the Input 1 line
        (pin 2).
        
        Remote-control command(s):
        CONTrol:HANDler:OUTPut<port>:USER?
        
        
        

   :param port: Output port number.
   :return: nextState

.. method:: RestoreUIDefaultStates(self, )
           
        Restores the default states of the Universal Interface including the
        data port values.
        
        Remote-control command(s):
        CONTrol:HANDler:RESet
        
        
        
        


.. method:: setStatusRegister(self, registerOperation, questionableRegister, enable, PTransition, NTransition)
           
        This function sets the Enable, NTransition, and PTransition bits of
        status questionable and operating registers.
        
        Note:
        
        (1) For detailed description of Status Reporting System see also
        operating manual.
        
        Remote-control command(s):
        STATus:PRESet
        STATus:QUEStionable:ENABle
        STATus:QUEStionable:LIMit<1|2>:ENABle
        STATus:QUEStionable:INTegrity:ENABle
        STATus:QUEStionable:INTegrity:HARDware:ENABle
        STATus:QUEStionable:PTRansition
        STATus:QUEStionable:LIMit<1|2>:PTRansition
        STATus:QUEStionable:INTegrity:PTRansition
        STATus:QUEStionable:INTegrity:HARDware:PTRansition
        STATus:QUEStionable:NTRansition
        STATus:QUEStionable:LIMit<1|2>:NTRansition
        STATus:QUEStionable:INTegrity:NTRansition
        STATus:QUEStionable:INTegrity:HARDware:NTRansition
        
        

   :param NTransition: This control sets the NTransition bits (edgedetectors) of the status register.
   :param enable: This control sets the enable bits of the status register.
   :param questionableRegister: This control selects the registers thatwill be configured.
   :param PTransition: This control sets the PTransition bits (edgedetectors) of the status register.
   :param registerOperation: Specifies the operationto perform.

.. method:: getStatusRegister(self, statusRegistersQuery)
           
        This function contains the commands for the querying status reporting
        system.
        
        Note:
        
        For detailed description of Status Reporting System see also operating
        manual.
        
        Remote-control command(s):
        STATus:OPERation:EVENt?
        STATus:OPERation:CONDition?
        STATus:QUEStionable:EVENt?
        STATus:QUEStionable:CONDition?
        STATus:QUEStionable:LIMit<1|2>:EVENt?
        STATus:QUEStionable:LIMit<1|2>:CONDition?
        STATus:QUEStionable:INTegrity:EVENt?
        STATus:QUEStionable:INTegrity:CONDition?
        STATus:QUEStionable:INTegrity:HARDware:EVENt?
        STATus:QUEStionable:INTegrity:HARDware:CONDition?
        
        

   :param statusRegistersQuery: This control selectsthe registers to be queried.
   :return: registerValue

.. method:: setTimeOut(self, timeout)
           
        Sets a minimum timeout value for driver I/O transactions in
        milliseconds. The timeout period may vary on computer platforms.
        
        

   :param timeout: Sets the I/O timeout for allfunctions in the driver. It is specified in milliseconds.

.. method:: getTimeOut(self, )
           
        Returns the timeout value for driver I/O transactions in milliseconds.
        
        The timeout period may vary on computer platforms.
        
        

   :return: timeout

.. method:: errorCheckState(self, stateChecking)
           
        This function switches state checking of the instrument (reading of
        the Standard Event Register and checking it for error) status
        subsystem. Driver functions are using state checking which is by
        default enabled.
        
        Note:
        
        (1) In debug mode enable state checking.
        
        (2) For better bus throughput and instruments performance disable
        state checking.
        
        (3) When state checking is disabled driver does not check if correct
        instrument model or option is used with each of the functions. This
        might cause unexpected behaviour of the instrument.
        
        
        

   :param stateChecking: This control switchesinstrument state checking On or Off.

.. method:: setCheckOption(self, optionChecking)
           
        This function switches option checking of the instrument.
        
        

   :param optionChecking: This control switchesinstrument and option checking On or Off.

.. method:: setCheckRange(self, rangeChecking)
           
        This function switches range checking of the instrument.
        
        

   :param rangeChecking: This control switchesrange checking On or Off.

.. method:: writeInstrData(self, writeBuffer)
           
        This function writes commands and queries to the instrument to modify
        parameters and query device settings.
        
        
        

   :param writeBuffer: The user can use this controlto send common commands and queries to the instrument. This controlcan also be used to write any valid command to the instrument.

.. method:: readInstrData(self, numberBytesToRead, readBuffer)
           
        This function reads data from the instrument's output buffer and
        returns it to the specified variable in memory.
        
        Notes:
        
        (1) Because the instrument may return both numeric and text data in
        response to queries this function returns the data in string format.
        
        (2) If valid data is not available at the instrument's output buffer
        when this function is called the instrument will hang up and the
        function will not return until it times out. If the time-out is
        disabled this function will hang indefinitely and it may be necessary
        to reboot the computer to break out.
        
        
        

   :param readBuffer: The incoming data from the instrument is placedinto this variable.
   :param numberBytesToRead: The number of bytesspecified by this control should be greater than or equal to thenumber of bytes which are to be read from the instrument. If theactual number of bytes to be read is greater than the number thiscontrol specifies then multiple reads will be required to empty theinstrument's output buffer.
   :return: numBytesRead

.. method:: reset(self, )
           
        This function resets the instrument to a known state and sends
        initialization commands to the instrument that set any necessary
        programmatic variables to the state necessary for the operation of the
        instrument driver.
        
        
        


.. method:: self_test(self, selfTestMessage)
           
        This function runs the instrument's self test routine and returns the
        test result(s).
        
        
        

   :param selfTestMessage: This control contains the string returnedfrom the self test. See the device's operation manual for anexplanation of the string's contents.
   :return: selfTestResult

.. method:: error_query(self, errorMessage)
           
        This function reads an error code from the instrument's error queue.
        
        
        

   :param errorMessage: This control returns the error message stringread from the instrument's error message queue.
   :return: errorCode

.. method:: error_message(self, statusCode, message)
           
        This function takes the Status Code returned by the instrument driver
        functions, interprets it and returns it as a user readable string.
        
        
        

   :param message: This control returns the interpretedStatus Code as a user readable message string.
   :param statusCode: This control accepts theStatus Code returned from the instrument driver functions.

.. method:: revision_query(self, instrumentDriverRevision, firmwareRevision)
           
        This function returns the revision numbers of the instrument driver
        and instrument firmware, and tells the user with which instrument
        firmware this revision of the driver is compatible.
        
        
        

   :param firmwareRevision: This control returns the Instrument FirmwareRevision.
   :param instrumentDriverRevision: This controlreturns the Instrument Driver Software Revision.

.. method:: close(self, )
           
        This function performs the following operations:
        viClose (instrSession) and viClose (rmSession).
        
        Notes:
        
        (1) The instrument must be reinitialized to use it again.
        
        
        


