    .. method:: init(self, IDQuery, resetDevice)
        Returns :  instrumentHandle

    .. method:: ApplicationExample(self, channel=1, startFrequency, stopFrequency, power, stimulusData, responseData)
        Returns :  noOfValues

    .. method:: WindowNew(self, setupName)

    .. method:: WindowSelect(self, setupName)

    .. method:: WindowClose(self, setupName)

    .. method:: WindowList(self, catalog, bufferSize)

    .. method:: Print(self, printerName)

    .. method:: PrinttoFile(self, fileName, fileFormat, diagramArea, logo, dateAndTime, markerList)

    .. method:: PrintSetup(self, diagramArea, logo, dateAndTime, markerList, pageOrientation, leftMargin, rightMargin, topMargin, bottomMargin)

    .. method:: FileManager(self, operationToBePerformed, source, destination)

    .. method:: GetCurrentDirectory(self, currentDirectory)

    .. method:: SetupSave(self, fileName)

    .. method:: SetupRecall(self, fileName)

    .. method:: readToFile(self, source, destination)

    .. method:: writeFromFile(self, source, destination)

    .. method:: SelectPowerMeter(self, channel=1, traceName, powerMeter, outPort)

    .. method:: SelectSParameters(self, channel=1, traceName, outPort, inPort)

    .. method:: SelectMoreSParameters(self, channel=1, traceName, outMode, outPort, inMode, inPort)

    .. method:: SelectRatios(self, channel=1, traceName, ratios)

    .. method:: SelectMoreRatios(self, channel=1, traceName, sourcePort, numeratorType, numeratorPortNumber, denominatorType, denominatorPortNumber)

    .. method:: SelectMoreRatiosWithDetector(self, channel=1, traceName, sourcePort, numeratorType, numeratorPortNumber, denominatorType, denominatorPortNumber, detector, observationTime)

    .. method:: SelectMoreRatiosGenerator(self, channel=1, traceName, generatorNumber, numeratorType, numeratorPortNumber, denominatorType, denominatorPortNumber)

    .. method:: SelectMoreRatiosGeneratorWithDetector(self, channel=1, traceName, generatorNumber, numeratorType, numeratorPortNumber, denominatorType, denominatorPortNumber, detector, observationTime)

    .. method:: SelectWaveQuantities(self, channel=1, traceName, waveQuantities)

    .. method:: SelectMoreWaveQuantities(self, channel=1, traceName, waveQuantityType, waveQuantityPortNumber, sourcePort)

    .. method:: SelectMoreWaveQuantitiesWithDetector(self, channel=1, traceName, waveQuantityType, waveQuantityPortNumber, sourcePort, detector, observationTime)

    .. method:: SelectImpedances(self, channel=1, traceName, outPort, inPort)

    .. method:: SelectMoreImpedances(self, channel=1, traceName, outMode, outPort, inMode, inPort)

    .. method:: SelectAdmitances(self, channel=1, traceName, outPort, inPort)

    .. method:: SelectMoreAdmitances(self, channel=1, traceName, outMode, outPort, inMode, inPort)

    .. method:: SelectZParameters(self, channel=1, traceName, outMode, outPort, inMode, inPort)

    .. method:: SelectYParameters(self, channel=1, traceName, outMode, outPort, inMode, inPort)

    .. method:: SelectStabilityFactors(self, channel=1, traceName, DUTOut, DUTIn, stabilityFactor)

    .. method:: SelectDCMeasurement(self, channel=1, traceName, DCMeas)

    .. method:: SelectPAEMeasurement(self, channel=1, traceName, DUTOut, DUTIn)

    .. method:: DefinePAEMeasurement(self, channel_Trace, testModel, constantC, constantK)

    .. method:: SelectNoiseFigure(self, channel=1, traceName, outPort, inPort)

    .. method:: CreateTrace(self, channel=1, traceName, parameter)

    .. method:: ConfigureMesurementParameters(self, channel=1, traceName, parameter)

    .. method:: QueryMesurementParameters(self, channel=1, traceName, bufferSize, parameters)

    .. method:: SetTraceFormat(self, channel_Trace, format)

    .. method:: GetTraceFormat(self, channel_Trace)
        Returns :  format

    .. method:: SetTraceUnit(self, channel_Trace, format)

    .. method:: GetTraceUnit(self, channel_Trace)
        Returns :  format

    .. method:: SetApertureGroupDelaySteps(self, channel_Trace, steps)

    .. method:: GetApertureGroupDelaySteps(self, channel_Trace)
        Returns :  steps

    .. method:: TraceAutoscale(self, window, window_Trace)

    .. method:: TraceAutoscaleByName(self, window, traceName)

    .. method:: SetTraceBottom(self, window, window_Trace, bottom)

    .. method:: GetTraceBottom(self, window, window_Trace)
        Returns :  bottom

    .. method:: SetTraceScaleDivisions(self, window, window_Trace, scaleDivisions)

    .. method:: SetTraceScaleDivisionsByName(self, window, scaleDivisions, traceName)

    .. method:: GetTraceScaleDivisions(self, window, window_Trace)
        Returns :  scaleDivisions

    .. method:: SetTraceRefValue(self, window, window_Trace, referenceLevel)

    .. method:: SetTraceRefValueByName(self, window, referenceLevel, traceName)

    .. method:: GetTraceRefValue(self, window, window_Trace)
        Returns :  referenceLevel

    .. method:: SetTraceRefPosition(self, window, window_Trace, referencePosition)

    .. method:: SetTraceRefPositionByName(self, window, referencePosition, traceName)

    .. method:: GetTraceRefPosition(self, window, window_Trace)
        Returns :  referencePosition

    .. method:: SetTraceTop(self, window, window_Trace, top)

    .. method:: GetTraceTop(self, window, window_Trace)
        Returns :  top

    .. method:: TraceAdd(self, channel=1, traceName)

    .. method:: TraceAddMode(self, channel=1, traceName, outMode, inMode)

    .. method:: SetTraceDisplayState(self, traceType, singleTraceName, showTrace)

    .. method:: GetTraceDisplayState(self, traceType, singleTraceName)
        Returns :  showTrace

    .. method:: TraceAddSParameterGroup(self, channel=1, numberOfLogicalPortNumbers, logicalPortNumber_s)

    .. method:: QueryTraceAddSParameterGroup(self, channel=1, logicalPortNumber_s)

    .. method:: TraceAddDiagramArea(self, window, window_Trace, channel=1, traceName)

    .. method:: TraceAssignDiagramArea(self, window, window_Trace, traceName)

    .. method:: TraceAssignWindowDiagramArea(self, window, traceName)

    .. method:: TraceUnassignDiagramArea(self, window, window_Trace)

    .. method:: TraceSelect(self, channel=1, traceName)

    .. method:: TraceDelete(self, channel=1, traceName)

    .. method:: TraceDeleteAll(self, channel=1)

    .. method:: TraceDeleteAllChannels(self, )

    .. method:: TraceList(self, channel=1, catalog, bufferSize)

    .. method:: TraceRename(self, oldTraceName, newTraceName)

    .. method:: ChannelTraceRename(self, channel=1, traceName)

    .. method:: TraceListCatalog(self, catalog, bufferSize)

    .. method:: TraceGetTraceName(self, traceNumber, traceName)

    .. method:: TraceGetTraceNumber(self, traceName)
        Returns :  traceNumber

    .. method:: TraceGetChannelName(self, traceName, channelName)

    .. method:: TraceGetChannelNumber(self, traceName)
        Returns :  channelNumber

    .. method:: TraceDataToMemory(self, channel_Trace)

    .. method:: TraceDataToMemoryTrace(self, memoryTrace, dataTrace)

    .. method:: TraceMathToMemoryTrace(self, memoryTrace, dataTrace)

    .. method:: DeleteMemoryTrace(self, memoryTrace)

    .. method:: TraceUserDefinedMath(self, channel_Trace, mathematicalExpression)

    .. method:: SetTraceMathState(self, channel_Trace, mathState)

    .. method:: GetTraceMathState(self, channel_Trace)
        Returns :  mathState

    .. method:: SetTraceMathFunction(self, channel_Trace, mathematicalFunction)

    .. method:: GetTraceMathFunction(self, channel_Trace)
        Returns :  mathematicalFunction

    .. method:: SetTraceMathWaveQuantityState(self, channel_Trace, mathWaveQuantityState)

    .. method:: GetTraceMathWaveQuantityState(self, channel_Trace)
        Returns :  mathWaveQuantityState

    .. method:: SetTraceTransformDomain(self, channel_Trace, transformDomain)

    .. method:: GetTraceTransformDomain(self, channel_Trace)
        Returns :  transformDomain

    .. method:: SetTraceTransformConversion(self, channel_Trace, conversion)

    .. method:: GetTraceTransformConversion(self, channel_Trace)
        Returns :  conversion

    .. method:: SetTimeDomainStartTime(self, channel_Trace, startTime)

    .. method:: GetTimeDomainStartTime(self, channel_Trace)
        Returns :  startTime

    .. method:: SetTimeDomainStopTime(self, channel_Trace, stopTime)

    .. method:: GetTimeDomainStopTime(self, channel_Trace)
        Returns :  stopTime

    .. method:: SetTimeDomainCenterTime(self, channel_Trace, centerTime)

    .. method:: GetTimeDomainCenterTime(self, channel_Trace)
        Returns :  centerTime

    .. method:: SetTimeDomainTimeSpan(self, channel_Trace, timeSpan)

    .. method:: GetTimeDomainTimeSpan(self, channel_Trace)
        Returns :  timeSpan

    .. method:: SetTimeDomainTimeAxisScaling(self, channel_Trace, timeAxisScaling)

    .. method:: GetTimeDomainTimeAxisScaling(self, channel_Trace)
        Returns :  timeAxisScaling

    .. method:: SetTimeDomainTransformationType(self, channel_Trace, transformationType)

    .. method:: GetTimeDomainTransformationType(self, channel_Trace)
        Returns :  transformationType

    .. method:: SetTimeDomainTransformationFilter(self, channel_Trace, filterType)

    .. method:: GetTimeDomainTransformationFilter(self, channel_Trace)
        Returns :  filterType

    .. method:: SetTimeDomainTransformationSidebandSuppression(self, channel_Trace, sidebandSuppression)

    .. method:: GetTimeDomainTransformationSidebandSuppression(self, channel_Trace)
        Returns :  sidebandSuppression

    .. method:: SetTimeDomainTransformationResolutionEfactor(self, channel_Trace, resolution)

    .. method:: GetTimeDomainTransformationResolutionEfactor(self, channel_Trace)
        Returns :  resolution

    .. method:: SetHarmonicGridAndKeep(self, channel_Trace, calculationMethod)

    .. method:: SetDCValue(self, channel_Trace, DCValue)

    .. method:: GetDCValue(self, channel_Trace)
        Returns :  DCValue

    .. method:: ExtrapolateDCValue(self, channel_Trace)

    .. method:: SetContinuousExtrapolation(self, channel_Trace, continuousExtrapolation)

    .. method:: GetContinuousExtrapolation(self, channel_Trace)
        Returns :  continuousExtrapolation

    .. method:: CalculateHarmonicGrid(self, channel_Trace)

    .. method:: SetTimeGateState(self, channel_Trace, timeGate)

    .. method:: GetTimeGateState(self, channel_Trace)
        Returns :  timeGate

    .. method:: SetTimeGateStartTime(self, channel_Trace, startTime)

    .. method:: GetTimeGateStartTime(self, channel_Trace)
        Returns :  startTime

    .. method:: SetTimeGateStopTime(self, channel_Trace, stopTime)

    .. method:: GetTimeGateStopTime(self, channel_Trace)
        Returns :  stopTime

    .. method:: SetTimeGateCenterTime(self, channel_Trace, centerTime)

    .. method:: GetTimeGateCenterTime(self, channel_Trace)
        Returns :  centerTime

    .. method:: SetTimeGateType(self, channel_Trace, timeGateType)

    .. method:: GetTimeGateType(self, channel_Trace)
        Returns :  timeGateType

    .. method:: SetTimeGateFilter(self, channel_Trace, filterType)

    .. method:: GetTimeGateFilter(self, channel_Trace)
        Returns :  filterType

    .. method:: SetTimeGateSidebandSuppression(self, channel_Trace, sidebandSuppression)

    .. method:: GetTimeGateSidebandSuppression(self, channel_Trace)
        Returns :  sidebandSuppression

    .. method:: SetTimeGateShape(self, channel_Trace, timeGateShape)

    .. method:: GetTimeGateShape(self, channel_Trace)
        Returns :  timeGateShape

    .. method:: SetTimeGateSpan(self, channel_Trace, span)

    .. method:: GetTimeGateSpan(self, channel_Trace)
        Returns :  span

    .. method:: SetTimeGateDisplayState(self, channel_Trace, timeGateDisplay)

    .. method:: GetTimeGateDisplayState(self, channel_Trace)
        Returns :  timeGateDisplay

    .. method:: TraceEvaluationRange(self, channel_Trace, evaluationRange, start, stop)

    .. method:: TraceStatisticalEvaluation(self, channel_Trace, statisticalParameter, infoField, responseValue_s)

    .. method:: SetTraceEvaluationRangeShow(self, channel_Trace, showRange)

    .. method:: GetTraceEvaluationRangeShow(self, channel_Trace)
        Returns :  showRange

    .. method:: SetTraceCompressionValue(self, channel_Trace, compressionValue)

    .. method:: GetTraceCompressionValue(self, channel_Trace)
        Returns :  compressionValue

    .. method:: GetTraceCompressionPoint(self, channel_Trace)
        Returns :  compressionPointIn, compressionPointOut

    .. method:: SetDisplayResultsState(self, channel_Trace, resultType, displayResults)

    .. method:: GetDisplayResultsState(self, channel_Trace, resultType)
        Returns :  displayResults

    .. method:: SetTraceSmoothing(self, channel_Trace, smoothing, aperture)

    .. method:: GetTraceSmoothing(self, channel_Trace)
        Returns :  smoothing, aperture

    .. method:: TraceResponseData(self, channel_Trace, dataFormat, traceData)
        Returns :  noOfValues

    .. method:: TraceResponseDataError(self, channel_Trace, errorTerm, traceData)
        Returns :  noOfValues

    .. method:: TraceResponseDataAll(self, channel_Trace, dataFormat, traceData)
        Returns :  noOfValues

    .. method:: TraceComplexResponseData(self, channel_Trace, dataFormat, traceData)
        Returns :  noOfValues

    .. method:: TraceComplexResponseCatalog(self, channel_Trace, bufferSize, catalog)

    .. method:: TraceResponseDataAllData(self, channel_Trace, dataFormat, traceData)
        Returns :  noOfValues

    .. method:: TraceResponseSingleSweepData(self, channel_Trace, sweepNumber, traceData)
        Returns :  noOfValues

    .. method:: TraceResponseSingleSweepDataCount(self, channel_Trace)
        Returns :  sweepCount

    .. method:: TraceResponseSingleSweepDataForward(self, channel_Trace, sweepNumber, traceData)
        Returns :  noOfValues

    .. method:: TraceStimulusData(self, channel_Trace, traceData)
        Returns :  noOfValues

    .. method:: WriteMemoryTraceData(self, channel_Trace, noOfPoints, traceData)

    .. method:: WriteMemoryTraceDataExt(self, channel_Trace, dataFormat, noOfPoints, traceData)

    .. method:: SetTraceFormatZVR(self, dataFormat)

    .. method:: GetTraceFormatZVR(self, )
        Returns :  dataFormat

    .. method:: TraceResponseDataZVR(self, dataFormat, valuesToReturn, traceData)
        Returns :  noOfValues

    .. method:: TraceStimulusDataZVR(self, dataFormat, valuesToReturn, traceData)
        Returns :  noOfValues

    .. method:: TraceResponseDataSParameterGroup(self, channel_Trace, dataFormat, valuesToReturn, traceData)
        Returns :  noOfValues

    .. method:: TraceImportData(self, traceName, fileName)

    .. method:: TraceExportData(self, traceName, fileName)

    .. method:: TraceExportDataWithOptions(self, traceName, fileName, exportFormat, exportData)

    .. method:: TraceExportDataWithOptionsExt(self, traceName, fileName, exportFormat, exportData, decimalSeparator, fieldSeparator)

    .. method:: ChannelTraceExportData(self, selectChannel, channel_Trace, fileName)

    .. method:: ChannelTraceExportDataWithOptions(self, selectChannel, channel_Trace, fileName, exportFormat, exportData)

    .. method:: ChannelTraceExportDataWithOptionsExt(self, selectChannel, channel_Trace, fileName, exportFormat, exportData, decimalSeparator, fieldSeparator)

    .. method:: TraceExportDataPorts(self, channel=1, fileName, exportData, port1, port2, port3, port4)

    .. method:: TraceExportDataPortsIncomplete(self, channel=1, fileName, exportData, port1, port2, port3, port4)

    .. method:: SetRenormalizationState(self, state)

    .. method:: GetRenormalizationState(self, )
        Returns :  state

    .. method:: SetRenormalizationMode(self, mode)

    .. method:: GetRenormalizationMode(self, )
        Returns :  mode

    .. method:: SetRenormalizationImpedance(self, impedance)

    .. method:: GetRenormalizationImpedance(self, )
        Returns :  impedance

    .. method:: TraceShiftStimulusValue(self, window, window_Trace, shiftStimulusValue)

    .. method:: TraceShiftResponseValue(self, window, window_Trace, magnitude, phase, real, imaginary)

    .. method:: SetHold(self, channel=1, hold)

    .. method:: GetHold(self, channel=1)
        Returns :  hold

    .. method:: LinearityDeviationManual(self, channel=1, slope, constant, electricalLength)

    .. method:: LinearityDeviationAuto(self, channel=1)

    .. method:: SetLinearityDeviationState(self, channel=1, state)

    .. method:: GetLinearityDeviationState(self, channel=1)
        Returns :  state

    .. method:: SetLinearityDeviationSlope(self, channel=1, slope)

    .. method:: GetLinearityDeviationSlope(self, channel=1)
        Returns :  slope

    .. method:: SetLinearityDeviationConstant(self, channel=1, constant)

    .. method:: GetLinearityDeviationConstant(self, channel=1)
        Returns :  constant

    .. method:: SetLinearityDeviationElectricalLength(self, channel=1, electricalLength)

    .. method:: GetLinearityDeviationElectricalLength(self, channel=1)
        Returns :  electricalLength

    .. method:: SetMarkerState(self, channel_Trace, marker, markerState)

    .. method:: GetMarkerState(self, channel_Trace, marker)
        Returns :  markerState

    .. method:: SetMarkerStimulus(self, channel_Trace, marker, markerStimulus)

    .. method:: GetMarkerStimulus(self, channel_Trace, marker)
        Returns :  markerStimulus

    .. method:: GetMarkerResponse(self, channel_Trace, marker, markerResponse)

    .. method:: SetReferenceMarkerState(self, channel_Trace, marker, referenceMarkerState)

    .. method:: GetReferenceMarkerState(self, channel_Trace, marker)
        Returns :  referenceMarkerState

    .. method:: SetReferenceMarkerStimulus(self, channel_Trace, marker, referenceMarkerStimulus)

    .. method:: GetReferenceMarkerStimulus(self, channel_Trace, marker)
        Returns :  referenceMarkerStimulus

    .. method:: GetReferenceMarkerResponse(self, channel_Trace, marker)
        Returns :  referenceMarkerResponse

    .. method:: SetReferenceDiscreteMarker(self, channel_Trace, marker, mode)

    .. method:: GetReferenceDiscreteMarker(self, channel_Trace, marker)
        Returns :  mode

    .. method:: SetReferenceFixedMarker(self, channel_Trace, marker, type)

    .. method:: GetReferenceFixedMarker(self, channel_Trace, marker)
        Returns :  type

    .. method:: SetDeltaMarkerState(self, channel_Trace, marker, deltaMarkerState)

    .. method:: GetDeltaMarkerState(self, channel_Trace, marker)
        Returns :  deltaMarkerState

    .. method:: SetCoupledMarkers(self, channel_Trace, marker, markerCoupled)

    .. method:: GetCoupledMarkers(self, channel_Trace, marker)
        Returns :  markerCoupled

    .. method:: SetDiscreteMarker(self, channel_Trace, marker, discreteMode)

    .. method:: GetDiscreteMarker(self, channel_Trace, marker)
        Returns :  discreteMode

    .. method:: SetFixedMarker(self, channel_Trace, marker, fixedMarker)

    .. method:: GetFixedMarker(self, channel_Trace, marker)
        Returns :  fixedMarker

    .. method:: SetMarkerFormat(self, channel_Trace, marker, markerFormat)

    .. method:: GetMarkerFormat(self, channel_Trace, marker)
        Returns :  markerFormat

    .. method:: SetAllMarkersOff(self, channel_Trace)

    .. method:: SaveAllMarkers(self, fileName)

    .. method:: MarkerSearch(self, channel_Trace, marker, search)

    .. method:: MarkerTargetSearch(self, channel_Trace, marker, search)

    .. method:: SetMarkerTargetValue(self, channel_Trace, marker, targetValue)

    .. method:: GetMarkerTargetValue(self, channel_Trace, marker)
        Returns :  targetValue

    .. method:: MarkerBandpassSearch(self, channel_Trace, marker)

    .. method:: MarkerBandstopSearch(self, channel_Trace, marker)

    .. method:: SetMarkerSearchMode(self, channel_Trace, marker, searchMode)

    .. method:: GetMarkerSearchMode(self, channel_Trace, marker)
        Returns :  searchMode

    .. method:: MarkerBandfilterTracking(self, channel_Trace, marker, bandfilterTracking)

    .. method:: MarkerxdBBandwidth(self, channel_Trace, marker, xDBBandwidth)

    .. method:: MarkerBandfilterResults(self, channel_Trace, marker)
        Returns :  bandwidth, centerStimulus, q, loss, LBE, UBE

    .. method:: MarkerxdBBandwidthZVR(self, channel_Trace, marker, xDBBandwidth)

    .. method:: MarkerBandfilterResultsZVR(self, channel_Trace, marker)
        Returns :  bandwidth

    .. method:: SetMarkerSearchResultState(self, channel_Trace, marker, searchResults)

    .. method:: GetMarkerSearchResultState(self, channel_Trace, marker)
        Returns :  searchResults

    .. method:: SetMarkerTracking(self, channel_Trace, marker, markerTracking)

    .. method:: GetMarkerTracking(self, channel_Trace, marker)
        Returns :  markerTracking

    .. method:: MarkerSearchRange(self, channel_Trace, marker, searchRange, start, stop)

    .. method:: SetMarkerSearchRangeShow(self, channel_Trace, marker, showRange)

    .. method:: GetMarkerSearchRangeShow(self, channel_Trace, marker)
        Returns :  showRange

    .. method:: MarkerSearchResults(self, channel_Trace, marker, markerResponse)
        Returns :  markerStimulus

    .. method:: SetStartToMarker(self, channel_Trace, marker)

    .. method:: SetStopToMarker(self, channel_Trace, marker)

    .. method:: SetCenterToMarker(self, channel_Trace, marker)

    .. method:: ShowLimitLine(self, channel_Trace, displayLimitLine)

    .. method:: SetLimitCheck(self, channel_Trace, limitLine, limitCheck)

    .. method:: GetLimitCheck(self, channel_Trace, limitLine)
        Returns :  limitCheck

    .. method:: SetLimitLineFailBeep(self, channel_Trace, failBeep)

    .. method:: GetLimitLineFailBeep(self, channel_Trace)
        Returns :  failBeep

    .. method:: GetLimitCheckResult(self, channel_Trace)
        Returns :  limitCheckResult

    .. method:: AddLimitLineSegment(self, channel_Trace, segment, type, startStimulus, stopStimulus, startResponse, stopResponse)

    .. method:: EditLimitLineSegment(self, channel_Trace, segment, type, startStimulus, stopStimulus, startResponse, stopResponse)

    .. method:: ReadLimitLineSegmentList(self, channel_Trace, listSize, type, startStimulus, stopStimulus, startResponse, stopResponse)
        Returns :  segmentsCount

    .. method:: WriteLimitLineSegmentList(self, channel_Trace, listSize, type, startStimulus, stopStimulus, startResponse, stopResponse)

    .. method:: ShiftLimitLineSegmentList(self, channel_Trace, limitLineType, stimulusOffset, responseOffset)

    .. method:: DeleteLimitLineSegments(self, channel_Trace)

    .. method:: RecallLimitLine(self, traceName, fileName)

    .. method:: RecallLimitLineWithOptions(self, traceName, fileName, sParameter, xOffset, yOffset, type)

    .. method:: SaveLimitLine(self, traceName, fileName)

    .. method:: ImportTraceasLimitLine(self, channel_Trace, limitLineType, stimulusOffset, responseOffset, traceName)

    .. method:: SetLimitLineTTLOutPass(self, channel_Trace, outputNo, TTLOutput)

    .. method:: GetLimitLineTTLOutPass(self, channel_Trace, outputNo)
        Returns :  TTLOutput

    .. method:: SetDisplayLine(self, channel_Trace, displayLine, position)

    .. method:: GetDisplayLine(self, channel_Trace)
        Returns :  displayLine, position

    .. method:: SetLimitDomainUnits(self, channel_Trace, domainUnits)

    .. method:: SetLimitResponseDomainComplexUnits(self, channel_Trace, responseUnits)

    .. method:: SetLimitResponseDomainFormatUnits(self, channel_Trace, responseUnits)

    .. method:: SetLimitResponseDomainSpacingUnits(self, channel_Trace, responseUnits)

    .. method:: SetRippleCheckOn(self, channel_Trace, limitCheck)

    .. method:: GetRippleCheckOn(self, channel_Trace)
        Returns :  limitCheck

    .. method:: GetRippleLimitGlobalCheckResult(self, channel_Trace)
        Returns :  rippleLimitCheckResult

    .. method:: SetCheckRippleLimitRangeSegment(self, channel_Trace, segment, limitCheck)

    .. method:: GetCheckRippleLimitRangeSegment(self, channel_Trace, segment)
        Returns :  limitCheck

    .. method:: GetRippleLimitCheckSegmentResult(self, channel_Trace, segment)
        Returns :  fail, limitCheckResult

    .. method:: SetRippleLimitsDisplayState(self, channel_Trace, displayLine)

    .. method:: GetRippleLimitsDisplayState(self, channel_Trace)
        Returns :  displayLine

    .. method:: SetRippleFailBeepOn(self, channel_Trace, failBeep)

    .. method:: GetRippleFailBeepOn(self, channel_Trace)
        Returns :  failBeep

    .. method:: AddRippleLimitLineRangesSegment(self, channel_Trace, noOfValues, type, startStimulus, stopStimulus, limit)

    .. method:: EditRippleLimitLineSegment(self, channel_Trace, segment, startStimulus, stopStimulus)

    .. method:: DeleteAllRippleLimitRanges(self, channel_Trace)

    .. method:: SetRippleLimitPhysicalUnits(self, channel_Trace, physicalUnits)

    .. method:: SetRippleLimitResponseDomainFormatUnits(self, channel_Trace, responseUnits)

    .. method:: GetNumberRippleLimitRanges(self, channel_Trace, segment)
        Returns :  number

    .. method:: SetRippleLimitRange(self, channel_Trace, segment, limit)

    .. method:: GetRippleLimitRange(self, channel_Trace, segment)
        Returns :  limit

    .. method:: SaveRecallRippleLimit(self, operationToBePerformed, traceName, fileName)

    .. method:: SetStartFrequency(self, channel=1, startFrequency)

    .. method:: GetStartFrequency(self, channel=1)
        Returns :  startFrequency

    .. method:: SetStopFrequency(self, channel=1, stopFrequency)

    .. method:: GetStopFrequency(self, channel=1)
        Returns :  stopFrequency

    .. method:: SetCenterFrequency(self, channel=1, centerFrequency)

    .. method:: GetCenterFrequency(self, channel=1)
        Returns :  centerFrequency

    .. method:: SetFrequencySpan(self, channel=1, span)

    .. method:: GetFrequencySpan(self, channel=1)
        Returns :  span

    .. method:: SetPower(self, channel=1, power)

    .. method:: GetPower(self, channel=1)
        Returns :  power

    .. method:: SetCWFrequency(self, channel=1, CWFrequency)

    .. method:: GetCWFrequency(self, channel=1)
        Returns :  CWFrequency

    .. method:: SetStartPower(self, channel=1, startPower)

    .. method:: GetStartPower(self, channel=1)
        Returns :  startPower

    .. method:: SetStopPower(self, channel=1, stopPower)

    .. method:: GetStopPower(self, channel=1)
        Returns :  stopPower

    .. method:: SetSourcePort(self, channel=1, sourcePort)

    .. method:: GetSourcePort(self, channel=1)
        Returns :  sourcePort

    .. method:: ConfigurePowerBandwidthAverage(self, channel=1, RFState, measBandwidth, averageState, averageFactor)

    .. method:: SetReceiverStepAttenuators(self, channel=1, analyzerPort, attenuationFactor)

    .. method:: GetReceiverStepAttenuators(self, channel=1, analyzerPort)
        Returns :  attenuationFactor

    .. method:: SetGeneratorStepAttenuators(self, channel=1, port, attenuationFactor)

    .. method:: GetGeneratorStepAttenuators(self, channel=1, port)
        Returns :  attenuationFactor

    .. method:: SetAutomaticGeneratorAttenuator(self, channel=1, port, automaticAttenuation)

    .. method:: GetAutomaticGeneratorAttenuator(self, channel=1, port)
        Returns :  automaticAttenuation

    .. method:: GetAutomaticGeneratorAttenuation(self, channel=1, port)
        Returns :  attenuation

    .. method:: SetGeneratorAttenuatorMode(self, channel=1, port, attenuationMode)

    .. method:: GetGeneratorAttenuatorMode(self, channel=1, port)
        Returns :  attenuationMode

    .. method:: SetRFState(self, RFState)

    .. method:: GetRFState(self, )
        Returns :  RFState

    .. method:: SetMeasBandwidth(self, channel=1, measBandwidth)

    .. method:: GetMeasBandwidth(self, channel=1)
        Returns :  measBandwidth

    .. method:: SetMeasBandwidthSelectivity(self, channel=1, measBandwidthSelectivity)

    .. method:: GetMeasBandwidthSelectivity(self, channel=1)
        Returns :  measBandwidthSelectivity

    .. method:: SetMeasBandwidthReduction(self, channel=1, reduction)

    .. method:: GetMeasBandwidthReduction(self, channel=1)
        Returns :  reduction

    .. method:: SetAverageState(self, channel=1, averageState)

    .. method:: GetAverageState(self, channel=1)
        Returns :  averageState

    .. method:: SetAverageFactor(self, channel=1, averageFactor)

    .. method:: GetAverageFactor(self, channel=1)
        Returns :  averageFactor

    .. method:: GetCurrentSweep(self, channel=1)
        Returns :  currentSweep

    .. method:: RestartAverage(self, channel=1)

    .. method:: SetPartialMeasurementResolutionBandwidthMode(self, channel=1, bandwidthMode)

    .. method:: GetPartialMeasurementResolutionBandwidthMode(self, channel=1)
        Returns :  bandwidthMode

    .. method:: SetGeneratorPortResolutionBandwidth(self, channel=1, generatorPort, resolutionBandwidth)

    .. method:: GetGeneratorPortResolutionBandwidth(self, channel=1, generatorPort)
        Returns :  resolutionBandwidth

    .. method:: SetPhysicalPortResolutionBandwidth(self, channel=1, analyzerPort, resolutionBandwidth)

    .. method:: GetPhysicalPortResolutionBandwidth(self, channel=1, analyzerPort)
        Returns :  resolutionBandwidth

    .. method:: SetSweepType(self, channel=1, sweepType)

    .. method:: GetSweepType(self, channel=1)
        Returns :  sweepType

    .. method:: InsertNewSegment(self, channel=1, segment, startFrequency, stopFrequency, numberOfPoints, power, sweepTimeSelect, time, pointDelay, measBandwidth)

    .. method:: RedefineSegment(self, channel=1, segment, startFrequency, stopFrequency, numberOfPoints, power, sweepTimeSelect, time, pointDelay, measBandwidth)

    .. method:: AddNewSegment(self, channel=1, segment)

    .. method:: DeleteSelectedSegment(self, channel=1, segment)

    .. method:: DeleteAllSegments(self, channel=1)

    .. method:: GetSweepSegmentsCount(self, channel=1)
        Returns :  count

    .. method:: SetSweepSegmentState(self, channel=1, segment, state)

    .. method:: GetSweepSegmentState(self, channel=1, segment)
        Returns :  state

    .. method:: SetSweepSegmentStartFrequency(self, channel=1, segment, startFrequency)

    .. method:: GetSweepSegmentStartFrequency(self, channel=1, segment)
        Returns :  startFrequency

    .. method:: SetSweepSegmentStopFrequency(self, channel=1, segment, stopFrequency)

    .. method:: GetSweepSegmentStopFrequency(self, channel=1, segment)
        Returns :  stopFrequency

    .. method:: SetSweepSegmentNumberOfPoints(self, channel=1, segment, numberOfPoints)

    .. method:: GetSweepSegmentNumberOfPoints(self, channel=1, segment)
        Returns :  numberOfPoints

    .. method:: SetSweepSegmentName(self, channel=1, segment, name)

    .. method:: GetSweepSegmentName(self, channel=1, segment, bufferSize, name)

    .. method:: SetSweepSegmentPower(self, channel=1, segment, power)

    .. method:: GetSweepSegmentPower(self, channel=1, segment)
        Returns :  power

    .. method:: SetSweepSegmentIndependentPower(self, channel=1, segment, power)

    .. method:: GetSweepSegmentIndependentPower(self, channel=1, segment)
        Returns :  power

    .. method:: SetSweepSegmentMeasBandwidth(self, channel=1, segment, measBandwidth)

    .. method:: GetSweepSegmentMeasBandwidth(self, channel=1, segment)
        Returns :  measBandwidth

    .. method:: SetSweepSegmentIndependentBandwidth(self, channel=1, segment, measBandwidth)

    .. method:: GetSweepSegmentIndependentBandwidth(self, channel=1, segment)
        Returns :  measBandwidth

    .. method:: SetSweepSegmentSpurAvoid(self, channel=1, segment, spurAvoid)

    .. method:: GetSweepSegmentSpurAvoid(self, channel=1, segment)
        Returns :  spurAvoid

    .. method:: SetSweepSegmentIndependentSpurAvoid(self, channel=1, segment, spurAvoid)

    .. method:: GetSweepSegmentIndependentSpurAvoid(self, channel=1, segment)
        Returns :  spurAvoid

    .. method:: SetSweepSegmentSelectivity(self, channel=1, segment, selectivity)

    .. method:: GetSweepSegmentSelectivity(self, channel=1, segment)
        Returns :  selectivity

    .. method:: SetSweepSegmentIndependentSelectivity(self, channel=1, segment, selectivity)

    .. method:: GetSweepSegmentIndependentSelectivity(self, channel=1, segment)
        Returns :  selectivity

    .. method:: SetSweepSegmentSweepTime(self, channel=1, segment, time)

    .. method:: GetSweepSegmentSweepTime(self, channel=1, segment)
        Returns :  time

    .. method:: SetSweepSegmentIndependentTime(self, channel=1, segment, time)

    .. method:: GetSweepSegmentIndependentTime(self, channel=1, segment)
        Returns :  time

    .. method:: SetSweepSegmentPointDelay(self, channel=1, segment, pointDelay)

    .. method:: GetSweepSegmentPointDelay(self, channel=1, segment)
        Returns :  pointDelay

    .. method:: SetSweepSegmentIndependentPointDelay(self, channel=1, segment, pointDelay)

    .. method:: GetSweepSegmentIndependentPointDelay(self, channel=1, segment)
        Returns :  pointDelay

    .. method:: SetSweepSegmentTriggering(self, channel=1, segment, triggering)

    .. method:: GetSweepSegmentTriggering(self, channel=1, segment)
        Returns :  triggering

    .. method:: SetSweepSelectiveSegmentTriggering(self, channel=1, triggering)

    .. method:: GetSweepSelectiveSegmentTriggering(self, channel=1)
        Returns :  triggering

    .. method:: SetSweepSegmentBitsState(self, channel=1, state)

    .. method:: GetSweepSegmentBitsState(self, channel=1)
        Returns :  state

    .. method:: SetSweepSegmentBitValues(self, channel=1, segment, bit0, bit1, bit2, bit3)

    .. method:: GetSweepSegmentBitValues(self, channel=1, segment)
        Returns :  bit0, bit1, bit2, bit3

    .. method:: GetSweepSegmentCenterFrequency(self, channel=1, segment)
        Returns :  centerFrequency

    .. method:: GetSweepSegmentFrequencySpan(self, channel=1, segment)
        Returns :  frequencySpan

    .. method:: SaveSegment(self, channel=1, fileName)

    .. method:: LoadSegment(self, channel=1, fileName)

    .. method:: QueryOverlappingSweepSegments(self, segment)
        Returns :  overlapping

    .. method:: QuerySumOfSweepSegmentsTime(self, channel=1)
        Returns :  sweepTime

    .. method:: SetPulseTimeStart(self, channel=1, timeStart)

    .. method:: GetPulseTimeStart(self, channel=1)
        Returns :  timeStart

    .. method:: SetPulseTimeStop(self, channel=1, timeStop)

    .. method:: GetPulseTimeStop(self, channel=1)
        Returns :  timeStop

    .. method:: SetPulseTimeBandwidth(self, channel=1, timeBandwidth)

    .. method:: GetPulseTimeBandwidth(self, channel=1)
        Returns :  timeBandwidth

    .. method:: SetPulseCoupledSectionLimitLinesState(self, channel=1, coupleLimits)

    .. method:: GetPulseCoupledSectionLimitLinesState(self, channel=1)
        Returns :  coupleLimits

    .. method:: SetPulseEvaluationMode(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber, evaluationMode)

    .. method:: GetPulseEvaluationMode(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber)
        Returns :  evaluationMode

    .. method:: SetPulseEvaluationSectionStart(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber, evaluationStartTime)

    .. method:: GetPulseEvaluationSectionStart(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber)
        Returns :  evaluationStartTime

    .. method:: SetPulseEvaluationSectionStop(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber, evaluationStopTime)

    .. method:: GetPulseEvaluationSectionStop(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber)
        Returns :  evaluationStopTime

    .. method:: SetPulseSectionLimitLinesState(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber, limitLinesState)

    .. method:: GetPulseSectionLimitLinesState(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber)
        Returns :  limitLinesState

    .. method:: SetPulseShiftStimulus(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber, shiftStimulus)

    .. method:: GetPulseShiftStimulus(self, channel=1, receiverType, recordNumber, interfaceType, generatorPortNumber)
        Returns :  shiftStimulus

    .. method:: ReadTimeSamplesData(self, channel_Trace, traceData)
        Returns :  noOfValues

    .. method:: SetSweepNumberOfPoints(self, channel=1, numberOfPoints)

    .. method:: GetSweepNumberOfPoints(self, channel=1)
        Returns :  numberOfPoints

    .. method:: SetFrequencyStepSize(self, channel=1, stepSize)

    .. method:: GetFrequencyStepSize(self, channel=1)
        Returns :  stepSize

    .. method:: SetSweepCount(self, channel=1, sweepCount)

    .. method:: GetSweepCount(self, channel=1)
        Returns :  sweepCount

    .. method:: ConfigureSweepTime(self, channel=1, autoSweepTime, sweepTime, measDelay)

    .. method:: SetSweepTime(self, channel=1, sweepTime)

    .. method:: GetSweepTime(self, channel=1)
        Returns :  sweepTime

    .. method:: SetSweepMeasDelay(self, channel=1, measDelay)

    .. method:: GetSweepMeasDelay(self, channel=1)
        Returns :  measDelay

    .. method:: SetSweepTimeAuto(self, channel=1, autoSweepTime)

    .. method:: GetSweepTimeAuto(self, channel=1)
        Returns :  autoSweepTime

    .. method:: ConfigureTriggerFreeRun(self, channel=1)

    .. method:: ConfigureTriggerExternal(self, channel=1, triggerOn)

    .. method:: ConfigureTriggerPeriodic(self, channel=1, triggerPeriod)

    .. method:: ConfigureTriggerRFPower(self, channel=1)

    .. method:: ConfigureTriggerManual(self, channel=1)

    .. method:: ConfigureTriggerSettings(self, channel=1, triggerMeasSequence, triggerDelay)

    .. method:: SetTriggerSource(self, channel=1, triggerSource)

    .. method:: GetTriggerSource(self, channel=1)
        Returns :  triggerSource

    .. method:: SetTriggerDelay(self, channel=1, triggerDelay)

    .. method:: GetTriggerDelay(self, channel=1)
        Returns :  triggerDelay

    .. method:: SetPartialMeasurementTriggerMode(self, channel=1, triggerMode)

    .. method:: GetPartialMeasurementTriggerMode(self, channel=1)
        Returns :  triggerMode

    .. method:: SetGeneratorPortTriggerDelay(self, channel=1, generatorPort, triggerDelay)

    .. method:: GetGeneratorPortTriggerDelay(self, channel=1, generatorPort)
        Returns :  triggerDelay

    .. method:: SetPhysicalPortTriggerDelay(self, channel=1, analyzerPort, triggerDelay)

    .. method:: GetPhysicalPortTriggerDelay(self, channel=1, analyzerPort)
        Returns :  triggerDelay

    .. method:: SetTriggeredMeasSequence(self, channel=1, triggerMeasSequence)

    .. method:: GetTriggeredMeasSequence(self, channel=1)
        Returns :  triggerMeasSequence

    .. method:: SetTriggerOn(self, channel=1, triggerOn)

    .. method:: GetTriggerOn(self, channel=1)
        Returns :  triggerOn

    .. method:: SetTriggerPeriod(self, channel=1, triggerPeriod)

    .. method:: GetTriggerPeriod(self, channel=1)
        Returns :  triggerPeriod

    .. method:: SendTrigger(self, )

    .. method:: SendTriggerWaitOPC(self, timeout)

    .. method:: SendChannelTrigger(self, channel=1)

    .. method:: SendChannelTriggerWaitOPC(self, channel=1, timeout)

    .. method:: SetSweepSingleAllChans(self, singleSweep)

    .. method:: GetSweepSingleAllChans(self, )
        Returns :  singleSweep

    .. method:: SweepRestart(self, channel=1)

    .. method:: SetSweepSingle(self, channel=1, singleSweep)

    .. method:: GetSweepSingle(self, channel=1)
        Returns :  singleSweep

    .. method:: DefineGroupOfMeasuredPorts(self, channel=1, group, firstPort, lastPort)

    .. method:: GetGroupOfMeasuredPorts(self, channel=1, group)
        Returns :  firstPort, lastPort

    .. method:: DefineGroupOfAllMeasuredPorts(self, channel=1, group, numberOfPortsInGroup, ports)

    .. method:: GetGroupOfAllMeasuredPorts(self, channel=1, group, ports)
        Returns :  numberOfPortsInGroup

    .. method:: GetPortGroupsCount(self, channel=1)
        Returns :  portGroups

    .. method:: DeleteGroupOfMeasuredPorts(self, channel=1, group)

    .. method:: DeleteAllGroupsOfMeasuredPorts(self, channel=1)

    .. method:: DefineBalancedPort(self, channel=1, logicalPort, physicalPort1, physicalPort2)

    .. method:: GetBalancedPort(self, channel=1, logicalPort)
        Returns :  physicalPort1, physicalPort2

    .. method:: DeleteBalancedPort(self, channel=1, logicalPort)

    .. method:: DeleteAllBalancedPorts(self, channel=1)

    .. method:: SetDifferentialModeImpedance(self, channel=1, logicalPort, impedance)

    .. method:: GetDifferentialModeImpedance(self, channel=1, logicalPort)
        Returns :  impedance

    .. method:: SetCommonModeImpedance(self, channel=1, logicalPort, impedance)

    .. method:: GetCommonModeImpedance(self, channel=1, logicalPort)
        Returns :  impedance

    .. method:: DefinePortPair(self, channel=1, functionType, portPair, port1, port2)

    .. method:: DeletePortPair(self, channel=1, functionType, portPair)

    .. method:: SetDefaultConfigurationState(self, defaultSettings)

    .. method:: GetDefaultConfigurationState(self, )
        Returns :  defaultSettings

    .. method:: SetPortConfigration(self, channel=1, portGroupA, portGroupB, portGroupC, portGroupD)

    .. method:: GetPortConfigration(self, channel=1)
        Returns :  portGroupA, portGroupB, portGroupC, portGroupD

    .. method:: SetConverterPowerOffset(self, channel=1, port, portPowerOffset, offsetParameter)

    .. method:: GetConverterPowerOffset(self, channel=1, port)
        Returns :  portPowerOffset, offsetParameter

    .. method:: SetConverterCalPowerOffset(self, channel=1, converter, calPowerOffset)

    .. method:: GetConverterCalPowerOffset(self, channel=1, converter)
        Returns :  calPowerOffset

    .. method:: SetAdvancedPowerTransferModelFrequencyState(self, channel=1, state)

    .. method:: GetAdvancedPowerTransferModelFrequencyState(self, channel=1)
        Returns :  state

    .. method:: SetSenseTypeOfPortTransferModel(self, channel=1, port, modelType)

    .. method:: GetSenseTypeOfPortTransferModel(self, channel=1, port)
        Returns :  modelType

    .. method:: SetSenseTypeOfAdvancedPowerTransferModel(self, channel=1, modelType)

    .. method:: GetSenseTypeOfAdvancedPowerTransferModel(self, channel=1)
        Returns :  modelType

    .. method:: SetConverterDataSetType(self, port, dataSetType)

    .. method:: GetConverterDataSetType(self, port)
        Returns :  dataSetType

    .. method:: SetConverterUserDataSetDirectory(self, port, directory)

    .. method:: GetConverterUserDataSetDirectory(self, port, bufferSize, directory)

    .. method:: SetConverterPortAssignment(self, port, serialNumber)

    .. method:: GetConverterPortAssignment(self, port, bufferSize, serialNumber)

    .. method:: SetPortTransferModelState(self, channel=1, port, state)

    .. method:: GetPortTransferModelState(self, channel=1, port)
        Returns :  state

    .. method:: SetPortWaveguideAttenuator(self, channel=1, port, waveguideAttenuator, attenuation)

    .. method:: GetPortWaveguideAttenuatorType(self, channel=1, port)
        Returns :  waveguideAttenuator

    .. method:: GetPortWaveguideAttenuator(self, channel=1, port, waveguideAttenuator)
        Returns :  attenuation

    .. method:: SetPortWaveguideAttenuatorSlope(self, channel=1, port, slope)

    .. method:: GetPortWaveguideAttenuatorSlope(self, channel=1, port)
        Returns :  slope

    .. method:: SetPortWaveguideAttenuatorOffset(self, channel=1, port, offset)

    .. method:: GetPortWaveguideAttenuatorOffset(self, channel=1, port)
        Returns :  offset

    .. method:: SetPortElectronicPowerTreshold(self, channel=1, port, threshold)

    .. method:: GetPortElectronicPowerTreshold(self, channel=1, port)
        Returns :  threshold

    .. method:: SetPortElectronicPowerReduction(self, channel=1, port, reduction)

    .. method:: GetPortElectronicPowerReduction(self, channel=1, port)
        Returns :  reduction

    .. method:: SetSimultaneousMeasurementOfPortsGroups(self, channel=1, state)

    .. method:: GetSimultaneousMeasurementOfPortsGroups(self, channel=1)
        Returns :  state

    .. method:: SetSimultaneousMeasurementFrequencyOffsetState(self, channel=1, state)

    .. method:: GetSimultaneousMeasurementFrequencyOffsetState(self, channel=1)
        Returns :  state

    .. method:: SetSimultaneousMeasurementMinimumFrequencyOffsetMode(self, channel=1, minimumFrequencyOffset)

    .. method:: GetSimultaneousMeasurementMinimumFrequencyOffsetMode(self, channel=1)
        Returns :  minimumFrequencyOffset

    .. method:: SetFrequencyConversion(self, measurementType, channel=1, port, numerator, denominator, offset, sweepType)

    .. method:: GetFrequencyConversion(self, measurementType, channel=1, port)
        Returns :  numerator, denominator, offset, sweepType

    .. method:: SetPowerMeterFrequencyConversion(self, channel=1, powerMeterNumber, numerator, denominator, offset, sweepType)

    .. method:: GetPowerMeterFrequencyConversion(self, channel=1, powerMeterNumber)
        Returns :  numerator, denominator, offset, sweepType

    .. method:: SetGeneratorFrequencyConversion(self, channel=1, port, generatorNumber, state, numerator, denominator, offset, sweepType)

    .. method:: GetGeneratorFrequencyConversion(self, channel=1, port, generatorNumber)
        Returns :  state, numerator, denominator, offset, sweepType

    .. method:: SetConverterSourceFrequency(self, channel=1, port, numerator, denominator, offset, sweepType)

    .. method:: GetConverterSourceFrequency(self, channel=1, port)
        Returns :  numerator, denominator, offset, sweepType

    .. method:: SetMeasureAWavesState(self, channel=1, state)

    .. method:: GetMeasureAWavesState(self, channel=1)
        Returns :  state

    .. method:: SetLocalOscilatorAState(self, channel=1, port, state)

    .. method:: GetLocalOscilatorAState(self, channel=1, port)
        Returns :  state

    .. method:: SetLocalOscilatorBState(self, channel=1, port, state)

    .. method:: GetLocalOscilatorBState(self, channel=1, port)
        Returns :  state

    .. method:: SetLogicalPortCommonRefImpedance(self, channel=1, port, real, imaginary)

    .. method:: GetLogicalPortCommonRefImpedance(self, channel=1, port)
        Returns :  real, imaginary

    .. method:: SetLogicalPortDifferentialRefImpedance(self, channel=1, port, real, imaginary)

    .. method:: GetLogicalPortDifferentialRefImpedance(self, channel=1, port)
        Returns :  real, imaginary

    .. method:: SetPortImpedancesRenormalization(self, channel=1, theory)

    .. method:: GetPortImpedancesRenormalization(self, channel=1)
        Returns :  theory

    .. method:: SetPhysicalPortRefImpedance(self, channel=1, port, real, imaginary)

    .. method:: GetPhysicalPortRefImpedance(self, channel=1, port)
        Returns :  real, imaginary

    .. method:: SetIFGain(self, channel=1, port, IFGain)

    .. method:: GetIFGain(self, channel=1, port)
        Returns :  IFGain

    .. method:: SetIFGainReferenceChannel(self, channel=1, port, IFGain)

    .. method:: GetIFGainReferenceChannel(self, channel=1, port)
        Returns :  IFGain

    .. method:: SetRFSignalSourceState(self, channel=1, port, state)

    .. method:: GetRFSignalSourceState(self, channel=1, port)
        Returns :  state

    .. method:: SetPermanentSignalSourceState(self, channel=1, port, state)

    .. method:: GetPermanentSignalSourceState(self, channel=1, port)
        Returns :  state

    .. method:: SetPermanentSignalGeneratorState(self, channel=1, port, generatorNumber, state)

    .. method:: GetPermanentSignalGeneratorState(self, channel=1, port, generatorNumber)
        Returns :  state

    .. method:: SetPortPowerGeneratorOffset(self, channel=1, portNumber, generatorNumber, portPowerOffset, offsetParameter)

    .. method:: GetPortPowerGeneratorOffset(self, channel=1, portNumber, generatorNumber)
        Returns :  portPowerOffset, offsetParameter

    .. method:: SetSlope(self, channel=1, port, slope)

    .. method:: GetSlope(self, channel=1, port)
        Returns :  slope

    .. method:: SetSourceCombinerState(self, channel=1, state)

    .. method:: GetSourceCombinerState(self, channel=1)
        Returns :  state

    .. method:: SetFrequencyStimulus(self, channel=1, frequencyStimulus)

    .. method:: GetFrequencyStimulus(self, channel=1, frequencyStimulus)

    .. method:: SetPowerStimulus(self, channel=1, powerStimulus)

    .. method:: GetPowerStimulus(self, channel=1, powerStimulus)

    .. method:: SetTDIFState(self, channel=1, trueDifferentialModeState)

    .. method:: GetTDIFState(self, channel=1)
        Returns :  trueDifferentialModeState

    .. method:: SetTDIFAmplitudeImbalanceLogicalPort(self, channel=1, port)

    .. method:: GetTDIFAmplitudeImbalanceLogicalPort(self, channel=1)
        Returns :  port

    .. method:: SetTDIFAmplitudeImbalanceStartPower(self, channel=1, startPower)

    .. method:: GetTDIFAmplitudeImbalanceStartPower(self, channel=1)
        Returns :  startPower

    .. method:: SetTDIFAmplitudeImbalanceStopPower(self, channel=1, stopPower)

    .. method:: GetTDIFAmplitudeImbalanceStopPower(self, channel=1)
        Returns :  stopPower

    .. method:: SetTDIFPhaseImbalanceLogicalPort(self, channel=1, port)

    .. method:: GetTDIFPhaseImbalanceLogicalPort(self, channel=1)
        Returns :  port

    .. method:: SetTDIFPhaseImbalanceStartPhase(self, channel=1, startPhase)

    .. method:: GetTDIFPhaseImbalanceStartPhase(self, channel=1)
        Returns :  startPhase

    .. method:: SetTDIFPhaseImbalanceStopPhase(self, channel=1, stopPhase)

    .. method:: GetTDIFPhaseImbalanceStopPhase(self, channel=1)
        Returns :  stopPhase

    .. method:: SetTDIFSourcePowerMode(self, channel=1, sourcePowerMode)

    .. method:: GetTDIFSourcePowerMode(self, channel=1)
        Returns :  sourcePowerMode

    .. method:: SetTDIFCompensationState(self, channel=1, compensationState)

    .. method:: GetTDIFCompensationState(self, channel=1)
        Returns :  compensationState

    .. method:: SetTDIFReceiverFrequency(self, channel=1, receiverFrequency)

    .. method:: GetTDIFReceiverFrequency(self, channel=1)
        Returns :  receiverFrequency

    .. method:: SetPulseGeneratorState(self, channel=1, pulseGeneratorState)

    .. method:: GetPulseGeneratorState(self, channel=1)
        Returns :  pulseGeneratorState

    .. method:: DefinePulseGenerator(self, channel=1, generator, pulseType, pulseWidth, singleTrainPulsePeriod, pulsePolarity, pulseMode)

    .. method:: DefinePulseTrainSegments(self, channel=1, bufferSize, pulseTrainActive, startTime, stopTime)

    .. method:: ConfigureChoppedPulseProfile(self, channel=1, choppedPulseProfileMode, delayIncrement)

    .. method:: SetPulseGeneratorType(self, channel=1, generator, pulseType)

    .. method:: GetPulseGeneratorType(self, channel=1, generator)
        Returns :  pulseType

    .. method:: SetPulseGeneratorWidth(self, channel=1, generator, pulseWidth)

    .. method:: GetPulseGeneratorWidth(self, channel=1, generator)
        Returns :  pulseWidth

    .. method:: SetPulseGeneratorSinglePeriod(self, channel=1, singlePulsePeriod)

    .. method:: GetPulseGeneratorSinglePeriod(self, channel=1)
        Returns :  singlePulsePeriod

    .. method:: SetPulseGeneratorTrainPeriod(self, channel=1, trainPulsePeriod)

    .. method:: GetPulseGeneratorTrainPeriod(self, channel=1)
        Returns :  trainPulsePeriod

    .. method:: SetPulseGeneratorPolarity(self, channel=1, generator, pulsePolarity)

    .. method:: GetPulseGeneratorPolarity(self, channel=1, generator)
        Returns :  pulsePolarity

    .. method:: SetPulseGeneratorMode(self, channel=1, pulseMode)

    .. method:: GetPulseGeneratorMode(self, channel=1)
        Returns :  pulseMode

    .. method:: SetPulseGeneratorMasterChannel(self, masterChannel)

    .. method:: GetPulseGeneratorMasterChannel(self, )
        Returns :  masterChannel

    .. method:: GetPulseTrainSegments(self, channel=1, bufferSize, pulseTrainActive, startTime, stopTime)

    .. method:: SetPulseTrainSegmentState(self, channel=1, segment, segmentState)

    .. method:: GetPulseTrainSegmentState(self, channel=1, segment)
        Returns :  segmentState

    .. method:: SetPulseTrainSegmentStart(self, channel=1, segment, segmentStart)

    .. method:: GetPulseTrainSegmentStart(self, channel=1, segment)
        Returns :  segmentStart

    .. method:: SetPulseTrainSegmentStop(self, channel=1, segment, segmentStop)

    .. method:: GetPulseTrainSegmentStop(self, channel=1, segment)
        Returns :  segmentStop

    .. method:: GetPulseTrainSegmentCount(self, channel=1)
        Returns :  segmentCount

    .. method:: DeleteAllPulseTrainSegments(self, channel=1)

    .. method:: SavePulseTrainFile(self, channel=1, generator, fileName)

    .. method:: LoadPulseTrainFile(self, channel=1, generator, fileName)

    .. method:: SetPulseGeneratorDelay(self, channel=1, delay)

    .. method:: GetPulseGeneratorDelay(self, channel=1)
        Returns :  delay

    .. method:: SetChoppedPulseProfileMode(self, channel=1, choppedPulseProfileMode)

    .. method:: GetChoppedPulseProfileMode(self, channel=1)
        Returns :  choppedPulseProfileMode

    .. method:: SetChoppedPulseProfileDelayIncrement(self, channel=1, delayIncrement)

    .. method:: GetChoppedPulseProfileDelayIncrement(self, channel=1)
        Returns :  delayIncrement

    .. method:: ConfigureZVAXPath(self, channel=1, path, internalCombiner, harmonicFilter, pulseModulator)

    .. method:: ConfigurePulseGenerators(self, channel=1, extSignalGeneratorInput, extSignalGeneratorOutput, assignment)

    .. method:: SetInternalCombiner(self, channel=1, internalCombiner)

    .. method:: GetInternalCombiner(self, channel=1)
        Returns :  internalCombiner

    .. method:: SetHarmonicFilter(self, channel=1, path, harmonicFilter)

    .. method:: GetHarmonicFilter(self, channel=1, path)
        Returns :  harmonicFilter

    .. method:: SetLNPreamplifier(self, channel=1, state)

    .. method:: GetLNPreamplifier(self, channel=1)
        Returns :  state

    .. method:: SetPulseModulator(self, channel=1, path, pulseModulator)

    .. method:: GetPulseModulator(self, channel=1, path)
        Returns :  pulseModulator

    .. method:: SetExternalSignalGeneratorInput(self, channel=1, extSignalGeneratorInput)

    .. method:: GetExternalSignalGeneratorInput(self, channel=1)
        Returns :  extSignalGeneratorInput

    .. method:: SetPulseGeneratorAssignment(self, channel=1, assignment)

    .. method:: GetPulseGeneratorAssignment(self, channel=1)
        Returns :  assignment

    .. method:: SetExternalSignalGeneratorOutput(self, channel=1, extSignalGeneratorOutput)

    .. method:: GetExternalSignalGeneratorOutput(self, channel=1)
        Returns :  extSignalGeneratorOutput

    .. method:: SetTRMMeasureInput(self, channel=1, path, input)

    .. method:: GetTRMMeasureInput(self, channel=1, path)
        Returns :  input

    .. method:: SetTRMCombinerState(self, channel=1, path, combinerState)

    .. method:: GetTRMCombinerState(self, channel=1, path)
        Returns :  combinerState

    .. method:: SetTRMPowerAmplifierState(self, channel=1, path, powerAmplifierState)

    .. method:: GetTRMPowerAmplifierState(self, channel=1, path)
        Returns :  powerAmplifierState

    .. method:: SetTRMPulseModulatorState(self, channel=1, path, pulseModulatorState)

    .. method:: GetTRMPulseModulatorState(self, channel=1, path)
        Returns :  pulseModulatorState

    .. method:: SetTRMUserSourcePathExtensionState(self, channel=1, path, userSourcePathExtension)

    .. method:: GetTRMUserSourcePathExtensionState(self, channel=1, path)
        Returns :  userSourcePathExtension

    .. method:: SetTRMUserMeasurementPathExtensionState(self, channel=1, path, userMeasurementPathExtension)

    .. method:: GetTRMUserMeasurementPathExtensionState(self, channel=1, path)
        Returns :  userMeasurementPathExtension

    .. method:: SetTRMPulseModulatorSource(self, channel=1, path, pulseModulatorSource)

    .. method:: GetTRMPulseModulatorSource(self, channel=1, path)
        Returns :  pulseModulatorSource

    .. method:: SetTRMPulseGeneratorSource(self, channel=1, extOut, pulseGeneratorSource)

    .. method:: GetTRMPulseGeneratorSource(self, channel=1, extOut)
        Returns :  pulseGeneratorSource

    .. method:: SetTRMPulseGeneratorInvertSource(self, channel=1, extOut, invertSource)

    .. method:: GetTRMPulseGeneratorInvertSource(self, channel=1, extOut)
        Returns :  invertSource

    .. method:: GetTRMNumberOfUnits(self, )
        Returns :  numberOfUnits

    .. method:: GetTRMUnitDeviceID(self, bufferSize, deviceID)

    .. method:: GetTRMUnitHardwareOptions(self, bufferSize, optionList)

    .. method:: ConfigureHarmonicMeasurement(self, channel=1, harmonicMeasurement, relativeHarmonicMeasurement, source, harmonicMeasuredAt, harmonicOrder)

    .. method:: SetHarmonicMeasurementState(self, channel=1, harmonicMeasurement)

    .. method:: GetHarmonicMeasurementState(self, channel=1)
        Returns :  harmonicMeasurement

    .. method:: SetHarmonicOrder(self, channel=1, harmonicOrder)

    .. method:: GetHarmonicOrder(self, channel=1)
        Returns :  harmonicOrder

    .. method:: SetHarmonicSourcePort(self, channel=1, port)

    .. method:: GetHarmonicSourcePort(self, channel=1)
        Returns :  port

    .. method:: SetHarmonicReceivePort(self, channel=1, port)

    .. method:: GetHarmonicReceivePort(self, channel=1)
        Returns :  port

    .. method:: SetHarmonicRelativeState(self, channel=1, relativeHarmonicMeasurement)

    .. method:: GetHarmonicRelativeState(self, channel=1)
        Returns :  relativeHarmonicMeasurement

    .. method:: SetMixerMode(self, channel=1, mixerMode)

    .. method:: GetMixerMode(self, channel=1)
        Returns :  mixerMode

    .. method:: SetNumberOfStages(self, channel=1, numberOfStages)

    .. method:: GetNumberOfStages(self, channel=1)
        Returns :  numberOfStages

    .. method:: SetSignalSource(self, channel=1, stage, source, portNumber)

    .. method:: GetSignalSource(self, channel=1, stage)
        Returns :  source, portNumber

    .. method:: SetIFSignalPort(self, channel=1, portNumber)

    .. method:: GetIFSignalPort(self, channel=1)
        Returns :  portNumber

    .. method:: SetRFSignalPort(self, channel=1, portNumber)

    .. method:: GetRFSignalPort(self, channel=1)
        Returns :  portNumber

    .. method:: SetInternalSignalSource(self, channel=1, internalSignalSource)

    .. method:: GetInternalSignalSource(self, channel=1)
        Returns :  internalSignalSource

    .. method:: SetExternalSignalSource(self, channel=1, externalSignalSource)

    .. method:: GetExternalSignalSource(self, channel=1)
        Returns :  externalSignalSource

    .. method:: ConfigurePowerSettings(self, channel=1, fundamentalPower, fixedPower)

    .. method:: SetFundamentalPowerSignal(self, channel=1, fundamentalPower)

    .. method:: GetFundamentalPowerSignal(self, channel=1)
        Returns :  fundamentalPower

    .. method:: SetFixedPower(self, channel=1, fixedPower)

    .. method:: GetFixedPower(self, channel=1)
        Returns :  fixedPower

    .. method:: SetFixedPowerToSignal(self, channel=1, signal, fixedPower)

    .. method:: GetFixedPowerToSignal(self, channel=1, signal)
        Returns :  fixedPower

    .. method:: SetSignalPowerMode(self, channel=1, signal, mode)

    .. method:: GetSignalPowerMode(self, channel=1, signal)
        Returns :  mode

    .. method:: ConfigureFrequencySettings(self, channel=1, fundamentalFrequencySignal, fixedFrequencySignal, fixedFrequency, frequencyConversionMode)

    .. method:: SetFundamentalFrequencySignal(self, channel=1, fundamentalFrequency)

    .. method:: GetFundamentalFrequencySignal(self, channel=1)
        Returns :  fundamentalFrequency

    .. method:: SetFixedFrequencySignal(self, channel=1, fixedFrequency)

    .. method:: GetFixedFrequencySignal(self, channel=1)
        Returns :  fixedFrequency

    .. method:: SetFixedFrequencySignalStage2(self, channel=1, fixedFrequency)

    .. method:: GetFixedFrequencySignalStage2(self, channel=1)
        Returns :  fixedFrequency

    .. method:: SetFixedFrequency(self, channel=1, fixedFrequency)

    .. method:: GetFixedFrequency(self, channel=1)
        Returns :  fixedFrequency

    .. method:: SetFixedFrequencyToSignal(self, channel=1, signal, fixedFrequency)

    .. method:: GetFixedFrequencyToSignal(self, channel=1, signal)
        Returns :  fixedFrequency

    .. method:: SetFrequencyConversionMode(self, channel=1, frequencyConversionMode)

    .. method:: GetFrequencyConversionMode(self, channel=1)
        Returns :  frequencyConversionMode

    .. method:: SetFrequencyConversionModeStage2(self, channel=1, frequencyConversionMode)

    .. method:: GetFrequencyConversionModeStage2(self, channel=1)
        Returns :  frequencyConversionMode

    .. method:: SetFrequencyHighAccuracy(self, channel=1, highAccuracy)

    .. method:: GetFrequencyHighAccuracy(self, channel=1)
        Returns :  highAccuracy

    .. method:: SetFrequencyLOConversionFactor(self, channel=1, stage, numerator, denominator)

    .. method:: GetFrequencyLOConversionFactor(self, channel=1, stage)
        Returns :  numerator, denominator

    .. method:: SetFrequencyRFConversionFactor(self, channel=1, numerator, denominator)

    .. method:: GetFrequencyRFConversionFactor(self, channel=1)
        Returns :  numerator, denominator

    .. method:: SetRFImageFrequency(self, channel=1, RFImageFrequency)

    .. method:: GetRFImageFrequency(self, channel=1)
        Returns :  RFImageFrequency

    .. method:: SetExternalPowerMeter(self, channel=1, numberOfExternalPowerMeter)

    .. method:: GetExternalPowerMeter(self, channel=1)
        Returns :  numberOfExternalPowerMeter

    .. method:: RFSourceCalibration(self, channel=1)

    .. method:: IFReceiverCalibration(self, channel=1)

    .. method:: LOSourceCalibration(self, channel=1)

    .. method:: LOSourceCalibrationStage2(self, channel=1)

    .. method:: SetMixerDelayMeasurementSetup(self, channel=1, measurementSetup)

    .. method:: GetMixerDelayMeasurementSetup(self, channel=1)
        Returns :  measurementSetup

    .. method:: SetMixerDelayLANConnection(self, channel=1, LANConnection)

    .. method:: GetMixerDelayLANConnection(self, channel=1)
        Returns :  LANConnection

    .. method:: DefineMixerDelayReceiver(self, measurementSetup)

    .. method:: ClearMixerDelayReceiverList(self, )

    .. method:: StartMixerDelayCalibrationSweep(self, channel=1)

    .. method:: SetMixerDelayAperture(self, channel=1, aperture)

    .. method:: GetMixerDelayAperture(self, channel=1)
        Returns :  aperture

    .. method:: SetMixerDelayConstant(self, channel=1, constantDelay)

    .. method:: GetMixerDelayConstant(self, channel=1)
        Returns :  constantDelay

    .. method:: SetMixerDelayCombinerState(self, channel=1, internalCombiner)

    .. method:: GetMixerDelayCombinerState(self, channel=1)
        Returns :  internalCombiner

    .. method:: SetMixerDelayDivisionByTwoEnabled(self, channel=1, divisionByTwo)

    .. method:: GetMixerDelayDivisionByTwoEnabled(self, channel=1)
        Returns :  divisionByTwo

    .. method:: SetMixerConstantDelayEnabled(self, channel=1, constantDelay)

    .. method:: GetMixerConstantDelayEnabled(self, channel=1)
        Returns :  constantDelay

    .. method:: SetMixerDelayCorrection(self, channel=1, correction)

    .. method:: GetMixerDelayCorrection(self, channel=1)
        Returns :  correction

    .. method:: SetMixerDelayUpperToneSource(self, channel=1, source, portNumber)

    .. method:: GetMixerDelayUpperToneSource(self, channel=1)
        Returns :  source, portNumber

    .. method:: LoadMixerDelayValues(self, channel=1, type, file)

    .. method:: LoadMixerDelayCalibrationData(self, channel=1, file)

    .. method:: StoreMixerDelayCalibrationData(self, channel=1, file)

    .. method:: SetVectorMixerMode(self, channel=1, mixerMode)

    .. method:: GetVectorMixerMode(self, channel=1)
        Returns :  mixerMode

    .. method:: SetInternalSignalSourceAUX(self, channel=1, internalSignalSource)

    .. method:: GetInternalSignalSourceAUX(self, channel=1)
        Returns :  internalSignalSource

    .. method:: SetExternalSignalSourceAUX(self, channel=1, externalSignalSource)

    .. method:: GetExternalSignalSourceAUX(self, channel=1)
        Returns :  externalSignalSource

    .. method:: SetAUXMixerPort(self, channel=1, portNumber)

    .. method:: GetAUXMixerPort(self, channel=1)
        Returns :  portNumber

    .. method:: SetAUXFixedPower(self, channel=1, fixedPower)

    .. method:: GetAUXFixedPower(self, channel=1)
        Returns :  fixedPower

    .. method:: AutomaticVectorMixerCalibration(self, channel=1, mode, dispersion, mixerParameter, delayPhase)

    .. method:: SetIMODLowerToneSource(self, channel=1, source, sourceNumber)

    .. method:: GetIMODLowerToneSource(self, channel=1)
        Returns :  source, sourceNumber

    .. method:: SetIMODUpperToneSource(self, channel=1, source, sourceNumber)

    .. method:: GetIMODUpperToneSource(self, channel=1)
        Returns :  source, sourceNumber

    .. method:: SetIMODToneDistance(self, channel=1, toneDistance)

    .. method:: GetIMODToneDistance(self, channel=1)
        Returns :  toneDistance

    .. method:: SetIMODReceiverPort(self, channel=1, receiverPort)

    .. method:: GetIMODReceiverPort(self, channel=1)
        Returns :  receiverPort

    .. method:: SetIMODMeasurementOrder(self, channel=1, productOrder, measurementState)

    .. method:: GetIMODMeasurementOrder(self, channel=1, productOrder)
        Returns :  measurementState

    .. method:: SetIMODEnhancedWaveCorrection(self, channel=1, state)

    .. method:: GetIMODEnhancedWaveCorrection(self, channel=1)
        Returns :  state

    .. method:: SetIMODInternalCombiner(self, channel=1, internalCombiner)

    .. method:: GetIMODInternalCombiner(self, channel=1)
        Returns :  internalCombiner

    .. method:: SetIMODSpectrumMeasurement(self, channel=1, spectrumMeasurement)

    .. method:: GetIMODSpectrumMeasurement(self, channel=1)
        Returns :  spectrumMeasurement

    .. method:: SetIMODMaxOrder(self, channel=1, maxOrder)

    .. method:: GetIMODMaxOrder(self, channel=1)
        Returns :  maxOrder

    .. method:: SetIMODTwoToneOutput(self, channel=1, twoToneOutput)

    .. method:: GetIMODTwoToneOutput(self, channel=1)
        Returns :  twoToneOutput

    .. method:: StartIMODLowerToneSourcePowerCalibration(self, channel=1)

    .. method:: StartIMODUpperToneSourcePowerCalibration(self, channel=1)

    .. method:: StartIMODReceivePortSourcePowerCalibration(self, channel=1)

    .. method:: StartIMODLowerUpperTonePortsSourcePowerCalibration(self, channel=1)

    .. method:: StartIMODReceiverPortPowerCalibration(self, channel=1)

    .. method:: StartIMODReceiverPowerCalibration(self, channel=1)

    .. method:: SetIMODDistortionMeasurementCalibrationState(self, channel=1, state)

    .. method:: GetIMODDistortionMeasurementCalibrationState(self, channel=1)
        Returns :  state

    .. method:: DisableIMODMeasurement(self, channel=1)

    .. method:: SetNoiseFigureDetectorMeasurementTime(self, channel=1, detectorTime)

    .. method:: GetNoiseFigureDetectorMeasurementTime(self, channel=1)
        Returns :  detectorTime

    .. method:: SetNoiseFigureMeasurementMode(self, channel=1, measurementMode)

    .. method:: GetNoiseFigureMeasurementMode(self, channel=1)
        Returns :  measurementMode

    .. method:: SetNoiseFigureLOOscillator(self, channel=1, LOOscillator)

    .. method:: GetNoiseFigureLOOscillator(self, channel=1)
        Returns :  LOOscillator

    .. method:: SetNoiseFigureNarowbandDUT(self, channel=1, narowbandDUT)

    .. method:: GetNoiseFigureNarowbandDUT(self, channel=1)
        Returns :  narowbandDUT

    .. method:: SetNoiseFigureRFImageCorrection(self, channel=1, RFImageCorrection)

    .. method:: GetNoiseFigureRFImageCorrection(self, channel=1)
        Returns :  RFImageCorrection

    .. method:: SetNoiseFigureCalibrationState(self, channel=1, calibration)

    .. method:: GetNoiseFigureCalibrationState(self, channel=1)
        Returns :  calibration

    .. method:: GetNoiseFigureCalibrationStateLabel(self, channel=1, bufferSize, label)

    .. method:: DefineNoiseFigureCalibrationSettings(self, channel=1, port1, port2, externalAttenuator, sourceNoiseCalAttenuation, DUTMeasurementAttenuation)

    .. method:: StartNoiseFigureCalibration(self, channel=1, calibrationStep)

    .. method:: TerminateNoiseFigureCalibration(self, channel=1)

    .. method:: CompleteNoiseFigureCalibration(self, channel=1)

    .. method:: OverwriteNoiseFigureChannelSettings(self, channel=1, traceName)

    .. method:: SetVirtualTransformBalancedState(self, channel=1, functionType, logicalPortNumber, state)

    .. method:: GetVirtualTransformBalancedState(self, channel=1, functionType, logicalPortNumber)
        Returns :  state

    .. method:: SetVirtualTransformBalancedPort(self, channel=1, functionType, logicalPortNumber, parameterType, parameterNumber, circuitModel, value)

    .. method:: GetVirtualTransformBalancedPort(self, channel=1, functionType, logicalPortNumber, parameterType, parameterNumber, circuitModel)
        Returns :  value

    .. method:: SetVirtualTransformBalancedCircuitModel(self, channel=1, functionType, logicalPortNumber, circuitModel)

    .. method:: GetVirtualTransformBalancedCircuitModel(self, channel=1, functionType, logicalPortNumber)
        Returns :  circuitModel

    .. method:: LoadBalancedPortCircuitModelData(self, channel=1, functionType, logicalPortNumber, fileName, parameter)

    .. method:: LoadAndInterchangeBalancedPortCircuitModelData(self, channel=1, functionType, logicalPortNumber, fileName, parameter)

    .. method:: SetVirtualTransformSingleEndedState(self, channel=1, functionType, physicalPortNumber, state)

    .. method:: GetVirtualTransformSingleEndedState(self, channel=1, functionType, physicalPortNumber)
        Returns :  state

    .. method:: SetVirtualTransformSingleEndedPort(self, channel=1, functionType, physicalPortNumber, parameterType, parameterNumber, circuitModel, value)

    .. method:: GetVirtualTransformSingleEndedPort(self, channel=1, functionType, physicalPortNumber, parameterType, parameterNumber, circuitModel)
        Returns :  value

    .. method:: SetVirtualTransformSingleEndedCircuitModel(self, channel=1, functionType, physicalPortNumber, circuitModel)

    .. method:: GetVirtualTransformSingleEndedCircuitModel(self, channel=1, functionType, physicalPortNumber)
        Returns :  circuitModel

    .. method:: LoadSingleEndedPortCircuitModelData(self, channel=1, functionType, physicalPortNumber, fileName)

    .. method:: LoadAndInterchangeSingleEndedPortCircuitModelData(self, channel=1, functionType, physicalPortNumber, fileName)

    .. method:: SetVirtualTransformGroundLoopState(self, channel=1, functionType, state)

    .. method:: GetVirtualTransformGroundLoopState(self, channel=1, functionType)
        Returns :  state

    .. method:: SetVirtualTransformGroundLoop(self, channel=1, functionType, parameterType, circuitModel, groundLoopValue)

    .. method:: GetVirtualTransformGroundLoop(self, channel=1, functionType, parameterType, circuitModel)
        Returns :  groundLoopValue

    .. method:: SetVirtualTransformGroundLoopCircuitModel(self, channel=1, functionType, circuitModel)

    .. method:: GetVirtualTransformGroundLoopCircuitModel(self, channel=1, functionType)
        Returns :  circuitModel

    .. method:: LoadGroundLoopCircuitModelData(self, channel=1, functionType, fileName)

    .. method:: SetVirtualTransformPortPairState(self, channel=1, functionType, portPair, state)

    .. method:: GetVirtualTransformPortPairState(self, channel=1, functionType, portPair)
        Returns :  state

    .. method:: SetVirtualTransformPortPair(self, channel=1, functionType, portPair, parameterType, parameterNumber, circuitModel, value)

    .. method:: GetVirtualTransformPortPair(self, channel=1, functionType, portPair, parameterType, parameterNumber, circuitModel)
        Returns :  value

    .. method:: SetVirtualTransformPortPairCircuitModel(self, channel=1, functionType, portPair, circuitModel)

    .. method:: GetVirtualTransformPortPairCircuitModel(self, channel=1, functionType, portPair)
        Returns :  circuitModel

    .. method:: LoadPortPairCircuitModelData(self, channel=1, functionType, portPair, fileName, parameter, interchangePortNumbers)

    .. method:: SetCoherentSignalState(self, channel=1, port, coherentSignal)

    .. method:: GetCoherentSignalState(self, channel=1, port)
        Returns :  coherentSignal

    .. method:: SetCoherentSignalAmplitude(self, channel=1, port, amplitude)

    .. method:: GetCoherentSignalAmplitude(self, channel=1, port)
        Returns :  amplitude

    .. method:: SetCoherentSignalPhase(self, channel=1, port, phase)

    .. method:: GetCoherentSignalPhase(self, channel=1, port)
        Returns :  phase

    .. method:: SetCoherentSignalReferencePort(self, channel=1, referencePort)

    .. method:: GetCoherentSignalReferencePort(self, channel=1)
        Returns :  referencePort

    .. method:: SetAlternateSweepMode(self, channel=1, alternateSweepMode)

    .. method:: GetAlternateSweepMode(self, channel=1)
        Returns :  alternateSweepMode

    .. method:: SetSpuriousAvoidance(self, channel=1, spuriousAvoidance)

    .. method:: GetSpuriousAvoidance(self, channel=1)
        Returns :  spuriousAvoidance

    .. method:: SetAutomaticLevelControlState(self, ALCState)

    .. method:: GetAutomaticLevelControlState(self, )
        Returns :  ALCState

    .. method:: SetIndividualALCPortState(self, channel=1, port, state)

    .. method:: GetIndividualALCPortState(self, channel=1, port)
        Returns :  state

    .. method:: SetALCPortState(self, channel=1, port, state)

    .. method:: GetALCPortState(self, channel=1, port)
        Returns :  state

    .. method:: SetALCPortClamp(self, channel=1, port, clampState)

    .. method:: GetALCPortClamp(self, channel=1, port)
        Returns :  clampState

    .. method:: SetALCPortAUBWState(self, channel=1, port, state)

    .. method:: GetALCPortAUBWState(self, channel=1, port)
        Returns :  state

    .. method:: SetALCPortBandwidth(self, channel=1, port, bandwidth)

    .. method:: GetALCPortBandwidth(self, channel=1, port)
        Returns :  bandwidth

    .. method:: SetALCPortCoupling(self, channel=1, state)

    .. method:: GetALCPortCoupling(self, channel=1)
        Returns :  state

    .. method:: SetALCChannelState(self, channel=1, state)

    .. method:: GetALCChannelState(self, channel=1)
        Returns :  state

    .. method:: SetALCLowPhaseNoiseMode(self, channel=1, state)

    .. method:: GetALCLowPhaseNoiseMode(self, channel=1)
        Returns :  state

    .. method:: SetALCPortOffsetState(self, channel=1, port, state)

    .. method:: GetALCPortOffsetState(self, channel=1, port)
        Returns :  state

    .. method:: SetALCPortControlRange(self, channel=1, port, controlRange)

    .. method:: GetALCPortControlRange(self, channel=1, port)
        Returns :  controlRange

    .. method:: SetALCPortStartOffset(self, channel=1, port, startOffset)

    .. method:: GetALCPortStartOffset(self, channel=1, port)
        Returns :  startOffset

    .. method:: SetALCPortSettingTolerance(self, channel=1, port, settingTolerance)

    .. method:: GetALCPortSettingTolerance(self, channel=1, port)
        Returns :  settingTolerance

    .. method:: SetLowPhaseNoiseState(self, channel=1, lowPhaseNoiseState)

    .. method:: GetLowPhaseNoiseState(self, channel=1)
        Returns :  lowPhaseNoiseState

    .. method:: ConfigurePortPIController(self, channel=1, port, PIControllerMode, gain, integrationTime)

    .. method:: ConfigureSAWMatchingNetwork(self, channel=1, apply, parallelL, serialC, differentialModeImpedance, commonModeImpedance)

    .. method:: SetSAWState(self, channel=1, apply)

    .. method:: GetSAWState(self, channel=1)
        Returns :  apply

    .. method:: SetSAWParallelL(self, channel=1, parallelL)

    .. method:: GetSAWParallelL(self, channel=1)
        Returns :  parallelL

    .. method:: SetSAWSerialC(self, channel=1, serialC)

    .. method:: GetSAWSerialC(self, channel=1)
        Returns :  serialC

    .. method:: SetSAWSimulationType(self, channel=1, type)

    .. method:: GetSAWSimulationType(self, channel=1)
        Returns :  type

    .. method:: SetPIControllerMode(self, channel=1, port, PIControllerMode)

    .. method:: GetPIControllerMode(self, channel=1, port)
        Returns :  PIControllerMode

    .. method:: SetPIControllerGain(self, channel=1, port, gain)

    .. method:: GetPIControllerGain(self, channel=1, port)
        Returns :  gain

    .. method:: SetPIControllerIntegrationTime(self, channel=1, port, integrationTime)

    .. method:: GetPIControllerIntegrationTime(self, channel=1, port)
        Returns :  integrationTime

    .. method:: ChannelAdd(self, channel=1, channelName)

    .. method:: ChannelAddTrace(self, window, window_Trace, channel=1, channelName, traceName)

    .. method:: ChannelAddTraceDiagramArea(self, window, window_Trace, channel=1, channelName, traceName)

    .. method:: ChannelDelete(self, channel=1)

    .. method:: ChannelList(self, catalog, bufferSize)

    .. method:: ChannelGetChannelName(self, channel=1, channelName)

    .. method:: ChannelGetChannelNumber(self, channelName)
        Returns :  channelNumber

    .. method:: ChannelSetActive(self, channel=1)

    .. method:: ChannelGetActive(self, )
        Returns :  channel

    .. method:: ChannelRename(self, channel=1, channelName)

    .. method:: SetConnector(self, channel=1, port, connector)

    .. method:: GetConnector(self, channel=1, port)
        Returns :  connector

    .. method:: SetSameConnectorTypeAtAllPorts(self, channel=1, sameConnectorAtAllPorts)

    .. method:: GetSameConnectorTypeAtAllPorts(self, channel=1)
        Returns :  sameConnectorAtAllPorts

    .. method:: SetSameConnectorGenderAtAllPorts(self, channel=1, sameGenderAtAllPorts)

    .. method:: GetSameConnectorGenderAtAllPorts(self, channel=1)
        Returns :  sameGenderAtAllPorts

    .. method:: SetUserConnector(self, channel=1, port, connector, connectorGender)

    .. method:: GetUserConnector(self, channel=1, port, connector)
        Returns :  connectorGender

    .. method:: SetSameSweepSetup(self, channel=1, sameSweepSetup)

    .. method:: GetSameSweepSetup(self, channel=1)
        Returns :  sameSweepSetup

    .. method:: SetSParameterDetector(self, channel=1, sParameterDetector)

    .. method:: GetSParameterDetector(self, channel=1)
        Returns :  sParameterDetector

    .. method:: SelectCalibrationType(self, channel=1, calibrationName, parameters, port1, port2, port3, port4)

    .. method:: GetCalibrationType(self, channel=1)
        Returns :  calibrationType, port1, port2, port3, port4

    .. method:: StartCalibration(self, channel=1, standard, port1, port2)

    .. method:: StartCalibrationLine(self, channel=1, line, port1, port2)

    .. method:: StartCalibrationWithOptions(self, channel=1, standard, port1, port2, dispersion, delayPhase, delayPhaseValue)

    .. method:: SetCalibrationReferencePlaneShift(self, channel=1, referencePlaneShift)

    .. method:: GetCalibrationReferencePlaneShift(self, channel=1)
        Returns :  referencePlaneShift

    .. method:: SetCalibrationReferencePlaneShiftSpecific(self, channel=1, referencePlaneShift, calibrationName)

    .. method:: GetCalibrationReferencePlaneShiftSpecific(self, channel=1, calibrationName)
        Returns :  referencePlaneShift

    .. method:: QueryCalibrationReferencePlaneShift(self, channel=1, calibrationIndex)
        Returns :  referencePlaneShift

    .. method:: SaveCalibrationData(self, channel=1)

    .. method:: GenerateDefaultCalibrationData(self, channel=1)

    .. method:: DeleteCalibrationData(self, channel=1, calibrationName)

    .. method:: DeleteAllCalibrationData(self, channel=1)

    .. method:: ReadCalibrationData(self, channel=1, errorTermParameters, port1, port2, calibrationData)

    .. method:: WriteCalibrationData(self, channel=1, errorTermParameters, port1, port2, calibrationData)

    .. method:: SetCorrectionState(self, channel=1, correctionState)

    .. method:: GetCorrectionState(self, channel=1)
        Returns :  correctionState

    .. method:: AcquireSourcePowerCalibration(self, channel=1, source, portNumber)

    .. method:: InitiateSourcePowerCalibration(self, channel=1, portNumber, externalPowerMeter)

    .. method:: SetDummySourcePowerCalibrationState(self, dummySourcePowerCalibration)

    .. method:: GetDummySourcePowerCalibrationState(self, )
        Returns :  dummySourcePowerCalibration

    .. method:: SetSourcePowerCalibrationPortState(self, channel=1, portNumber, portState)

    .. method:: GetSourcePowerCalibrationPortState(self, channel=1, portNumber)
        Returns :  portState

    .. method:: SetSourcePowerCalibrationGeneratorState(self, channel=1, portNumber, generatorState)

    .. method:: GetSourcePowerCalibrationGeneratorState(self, channel=1, portNumber)
        Returns :  generatorState

    .. method:: SetVerificationSweepState(self, channel=1, verificationSweep)

    .. method:: GetVerificationSweepState(self, channel=1)
        Returns :  verificationSweep

    .. method:: QueryVerificationSweepResults(self, )
        Returns :  calibrationPassed, maxOffset

    .. method:: GeneratorPowerCalibrationHarmonic(self, channel=1)

    .. method:: SetSourcePowerCalibrationState(self, calibrationState)

    .. method:: GetSourcePowerCalibrationState(self, )
        Returns :  calibrationState

    .. method:: SetReferenceReceiverCalibrationState(self, calibrationState)

    .. method:: GetReferenceReceiverCalibrationState(self, )
        Returns :  calibrationState

    .. method:: ModifySourcePowerCalibrationSettings(self, channel=1, portNumber, numberOfReadings, tolerance, otherSourcesState, portPowerOffset, offsetParameter, calibrationPowerOffset)

    .. method:: SetNumberOfReadings(self, channel=1, numberOfReadings)

    .. method:: GetNumberOfReadings(self, channel=1)
        Returns :  numberOfReadings

    .. method:: SetTolerance(self, channel=1, tolerance)

    .. method:: GetTolerance(self, channel=1)
        Returns :  tolerance

    .. method:: SetOtherSourcesState(self, channel=1, otherSources)

    .. method:: GetOtherSourcesState(self, channel=1)
        Returns :  otherSources

    .. method:: SetPortPowerOffset(self, channel=1, portNumber, portPowerOffset, offsetParameter)

    .. method:: GetPortPowerOffset(self, channel=1, portNumber)
        Returns :  portPowerOffset, offsetParameter

    .. method:: SetCalibrationPowerOffset(self, channel=1, portNumber, calibrationPowerOffset)

    .. method:: GetCalibrationPowerOffset(self, channel=1, portNumber)
        Returns :  calibrationPowerOffset

    .. method:: SetCalibrationPowerGeneratorOffset(self, channel=1, portNumber, generatorNumber, calPowerGeneratorOffset)

    .. method:: GetCalibrationPowerGeneratorOffset(self, channel=1, portNumber, generatorNumber)
        Returns :  calPowerGeneratorOffset

    .. method:: SetReferenceReceiverAfterFirstCalSweep(self, fastSourcePowerCalibration)

    .. method:: GetReferenceReceiverAfterFirstCalSweep(self, )
        Returns :  fastSourcePowerCalibration

    .. method:: SetPowerCalibrationMethodSource(self, methodSource)

    .. method:: GetPowerCalibrationMethodSource(self, )
        Returns :  methodSource

    .. method:: SetCalibrationPowerMeterReadings(self, powerMeterReadings)

    .. method:: GetCalibrationPowerMeterReadings(self, )
        Returns :  powerMeterReadings

    .. method:: ReadSourcePowerCorrectionData(self, channel=1, portNumber, calibratedWave, powerCorrectionValues)
        Returns :  numberOfValues

    .. method:: WriteSourcePowerCorrectionData(self, channel=1, portNumber, calibratedWave, numberOfValues, powerCorrectionValues)

    .. method:: GetSourcePowerCalibrationNumberOfWaves(self, channel=1)
        Returns :  numberOfWaves

    .. method:: GetSourcePowerCalibrationParamaterWave(self, channel=1, calibrationIndex, bufferSize, calibratedWave)

    .. method:: GetSourcePowerCalibrationParamaterStart(self, channel=1, calibrationIndex)
        Returns :  start

    .. method:: GetSourcePowerCalibrationParamaterStop(self, channel=1, calibrationIndex)
        Returns :  stop

    .. method:: GetSourcePowerCalibrationParamaterPoints(self, channel=1, calibrationIndex)
        Returns :  points

    .. method:: GetSourcePowerCalibrationParamaterType(self, channel=1, calibrationIndex)
        Returns :  type

    .. method:: GetSourcePowerCalibrationParamaterAttenuation(self, channel=1, calibrationIndex)
        Returns :  attenuation

    .. method:: GetSourcePowerCalibrationParamaterCWPower(self, channel=1, calibrationIndex)
        Returns :  CWPower

    .. method:: GetSourcePowerCalibrationParamaterCWFrequency(self, channel=1, calibrationIndex)
        Returns :  CWFrequency

    .. method:: GetSourcePowerCalibrationParamaterTimestamp(self, channel=1, calibrationIndex, bufferSize, timestamp)

    .. method:: SetSourcePowerCalibrationConvergenceFactor(self, convergenceFactor)

    .. method:: GetSourcePowerCalibrationConvergenceFactor(self, )
        Returns :  convergenceFactor

    .. method:: SetSourcePowerCalibrationConverterState(self, channel=1, converter, calibrationConverter)

    .. method:: GetSourcePowerCalibrationConverterState(self, channel=1, converter)
        Returns :  calibrationConverter

    .. method:: AcquireReceiverPowerCalibration(self, channel=1, wave, portNumber, source, sourceNumber, referencePower)

    .. method:: SetAWaveReceiverPowerCalibrationState(self, channel=1, portNumber, receiverPowerCalibration)

    .. method:: GetAWaveReceiverPowerCalibrationState(self, channel=1, portNumber)
        Returns :  receiverPowerCalibration

    .. method:: SetAWaveIdealPowerMeterMatchState(self, channel=1, portNumber, state)

    .. method:: GetAWaveIdealPowerMeterMatchState(self, channel=1, portNumber)
        Returns :  state

    .. method:: SetBWaveReceiverPowerCalibrationState(self, channel=1, portNumber, receiverPowerCalibration)

    .. method:: GetBWaveReceiverPowerCalibrationState(self, channel=1, portNumber)
        Returns :  receiverPowerCalibration

    .. method:: ReadReceiverPowerCorrectionData(self, channel=1, portNumber, calibratedWave, powerCorrectionValues)
        Returns :  numberOfValues

    .. method:: WriteReceiverPowerCorrectionData(self, channel=1, portNumber, calibratedWave, numberOfValues, powerCorrectionValues)

    .. method:: ReceiverPowerCalibrationHarmonic(self, channel=1)

    .. method:: CorrectionManager(self, operationToBePerformed, fileName, loadParameter)

    .. method:: SetPowerSensorPosition(self, powerSensorPosition)

    .. method:: GetPowerSensorPosition(self, )
        Returns :  powerSensorPosition

    .. method:: SetTwoPortTransmissionCoefficientsEnabled(self, twoPortEnabled)

    .. method:: GetTwoPortTransmissionCoefficientsEnabled(self, )
        Returns :  twoPortEnabled

    .. method:: GetLossListNumberOfValues(self, )
        Returns :  numberOfValues

    .. method:: SetPowerLossListCoefficient(self, operationToBePerformed, point, frequency, transmissionCoefficient)

    .. method:: GetPowerLossListCoefficient(self, point)
        Returns :  frequency, transmissionCoefficient

    .. method:: DeleteAllPowerLossListPoints(self, )

    .. method:: DeletePowerLossListSinglePoint(self, point)

    .. method:: SetPowerLossListTrace(self, traceName)

    .. method:: SetSourcePowerCorrectionState(self, channel=1, portNumber, sourcePowerCorrectionState)

    .. method:: GetSourcePowerCorrectionState(self, channel=1, portNumber)
        Returns :  sourcePowerCorrectionState

    .. method:: SetReceiverPowerCorrectionState(self, channel=1, portNumber, receiverPowerCorrectionState)

    .. method:: GetReceiverPowerCorrectionState(self, channel=1, portNumber)
        Returns :  receiverPowerCorrectionState

    .. method:: CalibrationManager(self, channel=1, operationToBePerformed, fileName)

    .. method:: CalibrationAuto(self, channel=1, calibrationKitName, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4, calUnitPort1, calUnitPort2, calUnitPort3, calUnitPort4)

    .. method:: CalibrationAutoSimplified(self, channel=1, calibrationKitName, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4)

    .. method:: CalibrationAutoType(self, channel=1, parameters, calibrationKitName, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4, calUnitPort1, calUnitPort2, calUnitPort3, calUnitPort4)

    .. method:: CalibrationAutoTypeSimplified(self, channel=1, parameters, calibrationKitName, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4)

    .. method:: CalibrationRetainPortGroups(self, retainPortGroups)

    .. method:: GetCalibrationConnection(self, channel=1)
        Returns :  analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4

    .. method:: CalibrationAutoEx(self, channel=1, calibrationKitName, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4, calUnitPort1, calUnitPort2, calUnitPort3, calUnitPort4, timeout)

    .. method:: CalibrationAutoAssignmentType(self, channel=1, parameters, calibrationKitName)

    .. method:: CalibrationAutoAssignmentDefinition(self, channel=1, assignment, analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4, calUnitPort1, calUnitPort2, calUnitPort3, calUnitPort4)

    .. method:: GetCalibrationAutoAssingnmentDefinition(self, channel=1, assignment)
        Returns :  analyzerPort1, analyzerPort2, analyzerPort3, analyzerPort4, calUnitPort1, calUnitPort2, calUnitPort3, calUnitPort4

    .. method:: InitiateCalibrationAutoAssignment(self, channel=1, assignment)

    .. method:: CalibrationAutoAssignmentSave(self, channel=1)

    .. method:: CalibrationAutoAssingnmentDeleteAll(self, channel=1)

    .. method:: SetCalibrationDataCurrentState(self, channel=1, keepMeasData)

    .. method:: GetCalibrationDataCurrentState(self, channel=1)
        Returns :  keepMeasData

    .. method:: SetCalibrationDataDefaultState(self, channel=1, keepMeasData)

    .. method:: GetCalibrationDataDefaultState(self, channel=1)
        Returns :  keepMeasData

    .. method:: ExpCharDataTouchstoneFile(self, fileName)

    .. method:: ExportUserCharacterizationDataTouchstoneFile(self, directoryName, fileName)

    .. method:: SetCalibrationConnector(self, channel=1, connectorName, propagationMode, connectorType, relativePermittivity, impedance)

    .. method:: GetCalibrationConnector(self, channel=1, connectorName)
        Returns :  propagationMode, connectorType, relativePermittivity, impedance

    .. method:: CalibrationConnectorCatalog(self, catalog, bufferSize)

    .. method:: DeleteCalibrationConnector(self, channel=1, connectorName)

    .. method:: GetCalibrationDate(self, channel=1, bufferSize, calibrationDate)

    .. method:: GetCalibrationState(self, channel=1)
        Returns :  calibrationState

    .. method:: GetCalibrationLabel(self, channel=1, bufferSize, label)

    .. method:: GetCalibrationDataParameters(self, channel=1)
        Returns :  frequencyStart, frequencyStop, numberOfPoints, internalSignalSourcePower, sweepType

    .. method:: GetCalibrationsNumber(self, channel=1)
        Returns :  numberOfCalibrations

    .. method:: GetCalibrationDataParametersMoreCalibrations(self, channel=1, calibration)
        Returns :  frequencyStart, frequencyStop, numberOfPoints, internalSignalSourcePower, sweepType

    .. method:: GetCalibrationDataBandwidth(self, channel=1, calibration)
        Returns :  bandwidth

    .. method:: GetCalibrationDataPointDelay(self, channel=1, calibration)
        Returns :  pointDelay

    .. method:: GetCalibrationDataReceiverAttenuation(self, channel=1, calibration, arraySize, calibrationPort, attenuation)
        Returns :  returnedValues

    .. method:: GetCalibrationDataType(self, channel=1, calibration)
        Returns :  calibrationType

    .. method:: GetCalibrationDataPorts(self, channel=1, calibration, arraySize)
        Returns :  calibrationPorts, returnedValues

    .. method:: GetCalibrationDataThroughs(self, channel=1, calibration, bufferSize, throughs)

    .. method:: GetCalibrationDataTimestamp(self, channel=1, calibration, bufferSize, timestamp)

    .. method:: SetActiveCalibrationUnit(self, calibrationUnit)

    .. method:: GetActiveCalibrationUnit(self, bufferSize, calibrationUnit)

    .. method:: SetAutomaticPowerReductionState(self, automaticPowerReduction)

    .. method:: GetAutomaticPowerReductionState(self, )
        Returns :  automaticPowerReduction

    .. method:: GetAllCalibrationUnits(self, bufferSize, calibrationUnit)

    .. method:: ConfigureCalibrationUnitStandard(self, standard, port1, port2)

    .. method:: SetFactoryCalibrationState(self, channel=1, factoryCalibration)

    .. method:: GetFactoryCalibrationState(self, channel=1)
        Returns :  factoryCalibration

    .. method:: SetEnhancedWaveCorrection(self, channel=1, errorCorrection)

    .. method:: GetEnhancedWaveCorrection(self, channel=1)
        Returns :  errorCorrection

    .. method:: SetLoadMatchingCorrection(self, channel=1, loadMatchingCorrection)

    .. method:: GetLoadMatchingCorrection(self, channel=1)
        Returns :  loadMatchingCorrection

    .. method:: SetCalibrationCorrectionBaseFrequencyState(self, channel=1, state)

    .. method:: GetCalibrationCorrectionBaseFrequencyState(self, channel=1)
        Returns :  state

    .. method:: SetCalibrationKit(self, connector, calibrationKitName)

    .. method:: GetCalibrationKit(self, connector, bufferSize, calibrationKitName)

    .. method:: SetCalibrationKitWithLabel(self, connector, calibrationKitName, calibrationKitLabel)

    .. method:: SetCalibrationKitUserConnectorType(self, connector, calibrationKitName)

    .. method:: GetCalibrationKitUserConnectorType(self, connector, bufferSize, calibrationKitName)

    .. method:: SetCalibrationKitUserConnectorTypeWithLabel(self, connectionType, calibrationKitName, calibrationKitLabel)

    .. method:: GetCalibrationKitUserConnectorTypeWithLabel(self, connectionType, bufferSize, calibrationKitData)

    .. method:: CalibrationKitCatalog(self, connectorName, catalog, bufferSize)

    .. method:: CalibrationKitCatalogWithLabel(self, connectorName, bufferSize, catalog)

    .. method:: ImportZVRCalibrationKit(self, calibrationKitName)

    .. method:: ConfigureCalibrationStandard(self, connector, standard, kit, serialNumber, minFreqHz, maxFreqHz, lengthmm, loss, c0L0, c1L1, c2L2, c3L3, approximation)

    .. method:: ConfigureCalibrationStandardWithLabel(self, standard, connector, calkitName, calkitLabel, standardLabel, minFreqHz, maxFreqHz, electricalLength, loss, z0, capacitances, residualInductances, approximation)

    .. method:: CalibrationStandardsCatalog(self, calibrationKitName, catalog, bufferSize)

    .. method:: CalibrationStandardsCatalogWithLabel(self, calibrationKitName, calibrationKitLabel, bufferSize, catalog)

    .. method:: SaveCalibrationKit(self, fileName)

    .. method:: SaveCalibrationKitPorts(self, fileName, parameters, arraySize, VNAPorts, calUnitPorts)

    .. method:: LoadCalibrationKit(self, connectorName, calibrationKitName, standard, calibrationKitLabel, fileName, portNumber1, portNumber2)

    .. method:: SetCalibrationKitLabel(self, calibrationKitName, label)

    .. method:: RenameCalibrationKit(self, calibrationKitName, label, newLabel)

    .. method:: GetCalibrationKitLabel(self, calibrationKitName, label)

    .. method:: DeleteCalibrationKit(self, calibrationKitName)

    .. method:: DeleteCalibrationKitWithLabel(self, calibrationKitName, calibrationKitLabel)

    .. method:: ImportKit(self, fileName)

    .. method:: AdditionalDirectoryCalibrationKit(self, directory)

    .. method:: ExportKit(self, kitName, fileName)

    .. method:: ExportKitWithLabel(self, kitName, kitLabel, fileName)

    .. method:: ResetOffsets(self, channel=1)

    .. method:: QueryResetOffsets(self, channel=1)
        Returns :  offsets

    .. method:: SetElectricalLength(self, channel=1, port, electricalLength)

    .. method:: GetElectricalLength(self, channel=1, port)
        Returns :  electricalLength

    .. method:: ConfigureMechanicalLength(self, channel=1, port, mechanicalLength, permittivity)

    .. method:: SetMechanicalLength(self, channel=1, port, mechanicalLength)

    .. method:: GetMechanicalLength(self, channel=1, port)
        Returns :  mechanicalLength

    .. method:: SetPermittivity(self, channel=1, port, permittivity)

    .. method:: GetPermittivity(self, channel=1, port)
        Returns :  permittivity

    .. method:: ConfigureLoss(self, channel=1, port, lossAtDC, lossAtFrequency, lossReferenceFrequency)

    .. method:: SetLossAtDC(self, channel=1, port, lossAtDC)

    .. method:: GetLossAtDC(self, channel=1, port)
        Returns :  lossAtDC

    .. method:: SetLossAtFrequency(self, channel=1, port, lossAtFrequency)

    .. method:: GetLossAtFrequency(self, channel=1, port)
        Returns :  lossAtFrequency

    .. method:: SetLossReferenceFrequency(self, channel=1, port, lossReferenceFrequency)

    .. method:: GetLossReferenceFrequency(self, channel=1, port)
        Returns :  lossReferenceFrequency

    .. method:: SetDelay(self, channel=1, port, delay)

    .. method:: GetDelay(self, channel=1, port)
        Returns :  delay

    .. method:: QueryDirectFixtureCompensation(self, channel=1, port)
        Returns :  directFixtureCompensation

    .. method:: AutoLength(self, channel=1, port)

    .. method:: AutoLengthAndLoss(self, channel=1, port)

    .. method:: AcquireFixtureCompensationSweep(self, channel=1, standardType, arraySize, ports)

    .. method:: StartFixtureCompensationSweep(self, channel=1)

    .. method:: SaveFixtureCompensationData(self, channel=1)

    .. method:: SetFixtureCompensationAutoLengthAndLossCalculation(self, autoLengthAndLoss)

    .. method:: GetFixtureCompensationAutoLengthAndLossCalculation(self, )
        Returns :  autoLengthAndLoss

    .. method:: SetFixtureCompensationDirectCompensation(self, directCompensation)

    .. method:: GetFixtureCompensationDirectCompensation(self, )
        Returns :  directCompensation

    .. method:: DiagramAreaAdd(self, window)

    .. method:: DiagramAreaDelete(self, window)

    .. method:: DiagramAreaMaximize(self, window, diagramArea)

    .. method:: DiagramAreaTitle(self, window, title, titleString)

    .. method:: DiagramAreaName(self, window, areaName)

    .. method:: DiagramAreaCatalog(self, window, catalog, bufferSize)

    .. method:: TraceDiagramAreaCatalog(self, window, catalog, bufferSize)

    .. method:: SetColorScheme(self, colorScheme)

    .. method:: GetColorScheme(self, )
        Returns :  colorScheme

    .. method:: SaveColorScheme(self, fileName)

    .. method:: LoadColorScheme(self, fileName)

    .. method:: SetFrequencyInfo(self, frequencyInfo)

    .. method:: GetFrequencyInfo(self, )
        Returns :  frequencyInfo

    .. method:: SetFontSize(self, fontSize)

    .. method:: GetFontSize(self, )
        Returns :  fontSize

    .. method:: SetChannelInfo(self, channelInfo)

    .. method:: GetChannelInfo(self, )
        Returns :  channelInfo

    .. method:: SetMarkerColorState(self, sameColor)

    .. method:: GetMarkerColorState(self, )
        Returns :  sameColor

    .. method:: SetRGBColor(self, element, red, green, blue, traceStyle, traceWidth)

    .. method:: GetRGBColor(self, element)
        Returns :  red, green, blue, traceStyle, traceWidth

    .. method:: SetTraceColorState(self, traceColor)

    .. method:: GetTraceColorState(self, )
        Returns :  traceColor

    .. method:: TraceSetRGBColor(self, traceName, red, green, blue, traceStyle, traceWidth)

    .. method:: TraceGetRGBColor(self, traceName)
        Returns :  red, green, blue, traceStyle, traceWidth

    .. method:: SetPowerPortLimitState(self, channel=1, port, limitState)

    .. method:: GetPowerPortLimitState(self, channel=1, port)
        Returns :  limitState

    .. method:: SetPowerPortLimitValue(self, channel=1, port, limitValue)

    .. method:: GetPowerPortLimitValue(self, channel=1, port)
        Returns :  limitValue

    .. method:: SetPowerPortLimitDirectGeneratorAndReceiverState(self, channel=1, port, DRGAccessState)

    .. method:: GetPowerPortLimitDirectGeneratorAndReceiverState(self, channel=1, port)
        Returns :  DRGAccessState

    .. method:: SetPresets(self, presetScope)

    .. method:: GetPresets(self, )
        Returns :  presetScope

    .. method:: SetPresetSettingsState(self, state)

    .. method:: GetPresetSettingsState(self, )
        Returns :  state

    .. method:: SetUserDefinedPresetState(self, userDefinedPreset)

    .. method:: GetUserDefinedPresetState(self, )
        Returns :  userDefinedPreset

    .. method:: SetUserDefinedPresetFile(self, userDefinedPresetFile)

    .. method:: GetUserDefinedPresetFile(self, bufferSize, userDefinedPresetFile)

    .. method:: SetDisplayUpdate(self, displayUpdate)

    .. method:: GetDisplayUpdate(self, )
        Returns :  displayUpdate

    .. method:: ImmediateSettingsUpdate(self, )

    .. method:: QueryFrequencyRange(self, )
        Returns :  minimumFrequency, maximumFrequency

    .. method:: SystemKeylock(self, lockout)

    .. method:: SetRemoteLanguage(self, language)

    .. method:: GetRemoteLanguage(self, )
        Returns :  language

    .. method:: ConfigureExternalGenerator(self, generatorNumber, generatorName, generatorType, interfaceType, interfaceAddress, fastSweepMode, _10MHzReferenceFrequency)

    .. method:: QueryExternalGenerator(self, generatorNumber, generatorName, generatorType, interfaceType, interfaceAddress)
        Returns :  fastSweepMode, _10MHzReferenceFrequency

    .. method:: QueryExternalGeneratorCount(self, )
        Returns :  generatorCount

    .. method:: QueryExternalGeneratorNumbers(self, arraySize, generatorNumbers)

    .. method:: DeleteExternalGenerator(self, )

    .. method:: ConfigureExternalPowerMeter(self, powerMeterNumber, powerMeterName, powerMeterType, interfaceType, interfaceAddress)

    .. method:: QueryExternalPowerMeter(self, powerMeterNumber, powerMeterName, powerMeterType, interfaceType, interfaceAddress)

    .. method:: QueryExternalPowerMeterCount(self, )
        Returns :  powerMeterCount

    .. method:: QueryExternalPowerMeterNumbers(self, bufferSize, powerMeterNumber)

    .. method:: AutoZeroingExternalPowerMeter(self, powerMeterNumber)

    .. method:: SetAutoConfigNRPZxx(self, powerMeterNumber, autoConfig)

    .. method:: GetAutoConfigNRPZxx(self, powerMeterNumber)
        Returns :  autoConfig

    .. method:: DeleteExternalPowerMeter(self, )

    .. method:: SetAlarmSoundsState(self, alarmSounds)

    .. method:: GetAlarmSoundsState(self, )
        Returns :  alarmSounds

    .. method:: SetRestartBehavior(self, restartBehavior)

    .. method:: GetRestartBehavior(self, )
        Returns :  restartBehavior

    .. method:: SetStatusSoundsState(self, statusSounds)

    .. method:: GetStatusSoundsState(self, )
        Returns :  statusSounds

    .. method:: SetDataTransfer(self, dataTransfer)

    .. method:: GetDataTransfer(self, )
        Returns :  dataTransfer

    .. method:: SetErrorDisplayState(self, errorDisplay)

    .. method:: GetErrorDisplayState(self, )
        Returns :  errorDisplay

    .. method:: SetFrequencyConversionType(self, converterType)

    .. method:: GetFrequencyConversionType(self, bufferSize, converterType)

    .. method:: SetFrequencyConversionSource(self, conversionSource)

    .. method:: GetFrequencyConversionSource(self, )
        Returns :  conversionSource

    .. method:: SetFastMultiportCorrection(self, fastMultiportCorrection)

    .. method:: GetFastMultiportCorrection(self, )
        Returns :  fastMultiportCorrection

    .. method:: SetPowerCoeficients(self, port, coeficient)

    .. method:: GetPowerCoeficients(self, port, coeficients)

    .. method:: SetPowerCoeficientsDefault(self, defaultCoeficients)

    .. method:: GetPowerCoeficientsDefault(self, )
        Returns :  defaultCoeficients

    .. method:: QueryExtensionUnitDeviceID(self, bufferSize, deviceID)

    .. method:: QueryExtensionUnitHardwareOptions(self, bufferSize, options)

    .. method:: SetNWAApplicationPriority(self, priority)

    .. method:: GetNWAApplicationPriority(self, )
        Returns :  priority

    .. method:: SystemShutdown(self, )

    .. method:: GenerateSystemReport(self, fileName)

    .. method:: SetCalculationOfBandfilterCenterFrequency(self, channel=1, marker, centerFrequencyCalculation)

    .. method:: GetCalculationOfBandfilterCenterFrequency(self, channel=1, marker)
        Returns :  centerFrequencyCalculation

    .. method:: SetRFOffBehavior(self, RFOffBehavior)

    .. method:: GetRFOffBehavior(self, )
        Returns :  RFOffBehavior

    .. method:: SetRemoteDisplayTitle(self, title)

    .. method:: GetRemoteDisplayTitle(self, bufferSize, title)

    .. method:: SetAnalyzerHostname(self, hostName)

    .. method:: GetAnalyzerHostname(self, bufferSize, hostName)

    .. method:: SetSoftKeyLabel(self, keyNumber, label)

    .. method:: GetPressedSoftKey(self, bufferSize, label)
        Returns :  keyNumber

    .. method:: SetOutputPortBits(self, outputPort, portBits)

    .. method:: GetOutputPortBits(self, outputPort)
        Returns :  portBits

    .. method:: SetChannelBits(self, channelBits)

    .. method:: GetChannelBits(self, )
        Returns :  channelBits

    .. method:: SetUIDirection(self, port, direction)

    .. method:: GetUIDirection(self, port)
        Returns :  direction

    .. method:: SetUIData(self, port, data)

    .. method:: GetUIData(self, port)
        Returns :  data

    .. method:: SetUISignalPin20(self, pin20)

    .. method:: GetUISignalPin20(self, )
        Returns :  pin20

    .. method:: SetUISignalPin21(self, pin21)

    .. method:: GetUISignalPin21(self, )
        Returns :  pin21

    .. method:: SetUIPortBinaryData(self, port, data)

    .. method:: GetUIPortBinaryData(self, port)
        Returns :  data

    .. method:: SetUIPortNextState(self, port, nextState)

    .. method:: GetUIPortNextState(self, port)
        Returns :  nextState

    .. method:: RestoreUIDefaultStates(self, )

    .. method:: setStatusRegister(self, registerOperation, questionableRegister, enable, PTransition, NTransition)

    .. method:: getStatusRegister(self, statusRegistersQuery)
        Returns :  registerValue

    .. method:: setTimeOut(self, timeout)

    .. method:: getTimeOut(self, )
        Returns :  timeout

    .. method:: errorCheckState(self, stateChecking)

    .. method:: setCheckOption(self, optionChecking)

    .. method:: setCheckRange(self, rangeChecking)

    .. method:: writeInstrData(self, writeBuffer)

    .. method:: readInstrData(self, numberBytesToRead, readBuffer)
        Returns :  numBytesRead

    .. method:: reset(self, )

    .. method:: self_test(self, selfTestMessage)
        Returns :  selfTestResult

    .. method:: error_query(self, errorMessage)
        Returns :  errorCode

    .. method:: error_message(self, statusCode, message)

    .. method:: revision_query(self, instrumentDriverRevision, firmwareRevision)

    .. method:: close(self, )

