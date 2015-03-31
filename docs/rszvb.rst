.. function:: init(IDQuery,resetDevice,instrumentHandle)

.. function:: ApplicationExample(channel=1,startFrequency,stopFrequency,power,noOfValues,stimulusData,responseData)

.. function:: WindowNew(setupName)

.. function:: WindowSelect(setupName)

.. function:: WindowClose(setupName)

.. function:: WindowList(catalog,bufferSize)

.. function:: Print(printerName)

.. function:: PrinttoFile(fileName,fileFormat,diagramArea,logo,dateAndTime,markerList)

.. function:: PrintSetup(diagramArea,logo,dateAndTime,markerList,pageOrientation,leftMargin,rightMargin,topMargin,bottomMargin)

.. function:: FileManager(operationToBePerformed,source,destination)

.. function:: GetCurrentDirectory(currentDirectory)

.. function:: SetupSave(fileName)

.. function:: SetupRecall(fileName)

.. function:: readToFile(source,destination)

.. function:: writeFromFile(source,destination)

.. function:: SelectPowerMeter(channel=1,traceName,powerMeter,outPort)

.. function:: SelectSParameters(channel=1,traceName,outPort,inPort)

.. function:: SelectMoreSParameters(channel=1,traceName,outMode,outPort,inMode,inPort)

.. function:: SelectRatios(channel=1,traceName,ratios)

.. function:: SelectMoreRatios(channel=1,traceName,sourcePort,numeratorType,numeratorPortNumber,denominatorType,denominatorPortNumber)

.. function:: SelectMoreRatiosWithDetector(channel=1,traceName,sourcePort,numeratorType,numeratorPortNumber,denominatorType,denominatorPortNumber,detector,observationTime)

.. function:: SelectMoreRatiosGenerator(channel=1,traceName,generatorNumber,numeratorType,numeratorPortNumber,denominatorType,denominatorPortNumber)

.. function:: SelectMoreRatiosGeneratorWithDetector(channel=1,traceName,generatorNumber,numeratorType,numeratorPortNumber,denominatorType,denominatorPortNumber,detector,observationTime)

.. function:: SelectWaveQuantities(channel=1,traceName,waveQuantities)

.. function:: SelectMoreWaveQuantities(channel=1,traceName,waveQuantityType,waveQuantityPortNumber,sourcePort)

.. function:: SelectMoreWaveQuantitiesWithDetector(channel=1,traceName,waveQuantityType,waveQuantityPortNumber,sourcePort,detector,observationTime)

.. function:: SelectImpedances(channel=1,traceName,outPort,inPort)

.. function:: SelectMoreImpedances(channel=1,traceName,outMode,outPort,inMode,inPort)

.. function:: SelectAdmitances(channel=1,traceName,outPort,inPort)

.. function:: SelectMoreAdmitances(channel=1,traceName,outMode,outPort,inMode,inPort)

.. function:: SelectZParameters(channel=1,traceName,outMode,outPort,inMode,inPort)

.. function:: SelectYParameters(channel=1,traceName,outMode,outPort,inMode,inPort)

.. function:: SelectStabilityFactors(channel=1,traceName,DUTOut,DUTIn,stabilityFactor)

.. function:: SelectDCMeasurement(channel=1,traceName,DCMeas)

.. function:: SelectPAEMeasurement(channel=1,traceName,DUTOut,DUTIn)

.. function:: DefinePAEMeasurement(channel_Trace,testModel,constantC,constantK)

.. function:: SelectNoiseFigure(channel=1,traceName,outPort,inPort)

.. function:: CreateTrace(channel=1,traceName,parameter)

.. function:: ConfigureMesurementParameters(channel=1,traceName,parameter)

.. function:: QueryMesurementParameters(channel=1,traceName,bufferSize,parameters)

.. function:: SetTraceFormat(channel_Trace,format)

.. function:: GetTraceFormat(channel_Trace,format)

.. function:: SetTraceUnit(channel_Trace,format)

.. function:: GetTraceUnit(channel_Trace,format)

.. function:: SetApertureGroupDelaySteps(channel_Trace,steps)

.. function:: GetApertureGroupDelaySteps(channel_Trace,steps)

.. function:: TraceAutoscale(window,window_Trace)

.. function:: TraceAutoscaleByName(window,traceName)

.. function:: SetTraceBottom(window,window_Trace,bottom)

.. function:: GetTraceBottom(window,window_Trace,bottom)

.. function:: SetTraceScaleDivisions(window,window_Trace,scaleDivisions)

.. function:: SetTraceScaleDivisionsByName(window,scaleDivisions,traceName)

.. function:: GetTraceScaleDivisions(window,window_Trace,scaleDivisions)

.. function:: SetTraceRefValue(window,window_Trace,referenceLevel)

.. function:: SetTraceRefValueByName(window,referenceLevel,traceName)

.. function:: GetTraceRefValue(window,window_Trace,referenceLevel)

.. function:: SetTraceRefPosition(window,window_Trace,referencePosition)

.. function:: SetTraceRefPositionByName(window,referencePosition,traceName)

.. function:: GetTraceRefPosition(window,window_Trace,referencePosition)

.. function:: SetTraceTop(window,window_Trace,top)

.. function:: GetTraceTop(window,window_Trace,top)

.. function:: TraceAdd(channel=1,traceName)

.. function:: TraceAddMode(channel=1,traceName,outMode,inMode)

.. function:: SetTraceDisplayState(traceType,singleTraceName,showTrace)

.. function:: GetTraceDisplayState(traceType,singleTraceName,showTrace)

.. function:: TraceAddSParameterGroup(channel=1,numberOfLogicalPortNumbers,logicalPortNumber_s)

.. function:: QueryTraceAddSParameterGroup(channel=1,logicalPortNumber_s)

.. function:: TraceAddDiagramArea(window,window_Trace,channel=1,traceName)

.. function:: TraceAssignDiagramArea(window,window_Trace,traceName)

.. function:: TraceAssignWindowDiagramArea(window,traceName)

.. function:: TraceUnassignDiagramArea(window,window_Trace)

.. function:: TraceSelect(channel=1,traceName)

.. function:: TraceDelete(channel=1,traceName)

.. function:: TraceDeleteAll(channel=1)

.. function:: TraceDeleteAllChannels()

.. function:: TraceList(channel=1,catalog,bufferSize)

.. function:: TraceRename(oldTraceName,newTraceName)

.. function:: ChannelTraceRename(channel=1,traceName)

.. function:: TraceListCatalog(catalog,bufferSize)

.. function:: TraceGetTraceName(traceNumber,traceName)

.. function:: TraceGetTraceNumber(traceName,traceNumber)

.. function:: TraceGetChannelName(traceName,channelName)

.. function:: TraceGetChannelNumber(traceName,channelNumber)

.. function:: TraceDataToMemory(channel_Trace)

.. function:: TraceDataToMemoryTrace(memoryTrace,dataTrace)

.. function:: TraceMathToMemoryTrace(memoryTrace,dataTrace)

.. function:: DeleteMemoryTrace(memoryTrace)

.. function:: TraceUserDefinedMath(channel_Trace,mathematicalExpression)

.. function:: SetTraceMathState(channel_Trace,mathState)

.. function:: GetTraceMathState(channel_Trace,mathState)

.. function:: SetTraceMathFunction(channel_Trace,mathematicalFunction)

.. function:: GetTraceMathFunction(channel_Trace,mathematicalFunction)

.. function:: SetTraceMathWaveQuantityState(channel_Trace,mathWaveQuantityState)

.. function:: GetTraceMathWaveQuantityState(channel_Trace,mathWaveQuantityState)

.. function:: SetTraceTransformDomain(channel_Trace,transformDomain)

.. function:: GetTraceTransformDomain(channel_Trace,transformDomain)

.. function:: SetTraceTransformConversion(channel_Trace,conversion)

.. function:: GetTraceTransformConversion(channel_Trace,conversion)

.. function:: SetTimeDomainStartTime(channel_Trace,startTime)

.. function:: GetTimeDomainStartTime(channel_Trace,startTime)

.. function:: SetTimeDomainStopTime(channel_Trace,stopTime)

.. function:: GetTimeDomainStopTime(channel_Trace,stopTime)

.. function:: SetTimeDomainCenterTime(channel_Trace,centerTime)

.. function:: GetTimeDomainCenterTime(channel_Trace,centerTime)

.. function:: SetTimeDomainTimeSpan(channel_Trace,timeSpan)

.. function:: GetTimeDomainTimeSpan(channel_Trace,timeSpan)

.. function:: SetTimeDomainTimeAxisScaling(channel_Trace,timeAxisScaling)

.. function:: GetTimeDomainTimeAxisScaling(channel_Trace,timeAxisScaling)

.. function:: SetTimeDomainTransformationType(channel_Trace,transformationType)

.. function:: GetTimeDomainTransformationType(channel_Trace,transformationType)

.. function:: SetTimeDomainTransformationFilter(channel_Trace,filterType)

.. function:: GetTimeDomainTransformationFilter(channel_Trace,filterType)

.. function:: SetTimeDomainTransformationSidebandSuppression(channel_Trace,sidebandSuppression)

.. function:: GetTimeDomainTransformationSidebandSuppression(channel_Trace,sidebandSuppression)

.. function:: SetTimeDomainTransformationResolutionEfactor(channel_Trace,resolution)

.. function:: GetTimeDomainTransformationResolutionEfactor(channel_Trace,resolution)

.. function:: SetHarmonicGridAndKeep(channel_Trace,calculationMethod)

.. function:: SetDCValue(channel_Trace,DCValue)

.. function:: GetDCValue(channel_Trace,DCValue)

.. function:: ExtrapolateDCValue(channel_Trace)

.. function:: SetContinuousExtrapolation(channel_Trace,continuousExtrapolation)

.. function:: GetContinuousExtrapolation(channel_Trace,continuousExtrapolation)

.. function:: CalculateHarmonicGrid(channel_Trace)

.. function:: SetTimeGateState(channel_Trace,timeGate)

.. function:: GetTimeGateState(channel_Trace,timeGate)

.. function:: SetTimeGateStartTime(channel_Trace,startTime)

.. function:: GetTimeGateStartTime(channel_Trace,startTime)

.. function:: SetTimeGateStopTime(channel_Trace,stopTime)

.. function:: GetTimeGateStopTime(channel_Trace,stopTime)

.. function:: SetTimeGateCenterTime(channel_Trace,centerTime)

.. function:: GetTimeGateCenterTime(channel_Trace,centerTime)

.. function:: SetTimeGateType(channel_Trace,timeGateType)

.. function:: GetTimeGateType(channel_Trace,timeGateType)

.. function:: SetTimeGateFilter(channel_Trace,filterType)

.. function:: GetTimeGateFilter(channel_Trace,filterType)

.. function:: SetTimeGateSidebandSuppression(channel_Trace,sidebandSuppression)

.. function:: GetTimeGateSidebandSuppression(channel_Trace,sidebandSuppression)

.. function:: SetTimeGateShape(channel_Trace,timeGateShape)

.. function:: GetTimeGateShape(channel_Trace,timeGateShape)

.. function:: SetTimeGateSpan(channel_Trace,span)

.. function:: GetTimeGateSpan(channel_Trace,span)

.. function:: SetTimeGateDisplayState(channel_Trace,timeGateDisplay)

.. function:: GetTimeGateDisplayState(channel_Trace,timeGateDisplay)

.. function:: TraceEvaluationRange(channel_Trace,evaluationRange,start,stop)

.. function:: TraceStatisticalEvaluation(channel_Trace,statisticalParameter,infoField,responseValue_s)

.. function:: SetTraceEvaluationRangeShow(channel_Trace,showRange)

.. function:: GetTraceEvaluationRangeShow(channel_Trace,showRange)

.. function:: SetTraceCompressionValue(channel_Trace,compressionValue)

.. function:: GetTraceCompressionValue(channel_Trace,compressionValue)

.. function:: GetTraceCompressionPoint(channel_Trace,compressionPointIn,compressionPointOut)

.. function:: SetDisplayResultsState(channel_Trace,resultType,displayResults)

.. function:: GetDisplayResultsState(channel_Trace,resultType,displayResults)

.. function:: SetTraceSmoothing(channel_Trace,smoothing,aperture)

.. function:: GetTraceSmoothing(channel_Trace,smoothing,aperture)

.. function:: TraceResponseData(channel_Trace,dataFormat,noOfValues,traceData)

.. function:: TraceResponseDataError(channel_Trace,errorTerm,noOfValues,traceData)

.. function:: TraceResponseDataAll(channel_Trace,dataFormat,noOfValues,traceData)

.. function:: TraceComplexResponseData(channel_Trace,dataFormat,noOfValues,traceData)

.. function:: TraceComplexResponseCatalog(channel_Trace,bufferSize,catalog)

.. function:: TraceResponseDataAllData(channel_Trace,dataFormat,noOfValues,traceData)

.. function:: TraceResponseSingleSweepData(channel_Trace,sweepNumber,noOfValues,traceData)

.. function:: TraceResponseSingleSweepDataCount(channel_Trace,sweepCount)

.. function:: TraceResponseSingleSweepDataForward(channel_Trace,sweepNumber,noOfValues,traceData)

.. function:: TraceStimulusData(channel_Trace,noOfValues,traceData)

.. function:: WriteMemoryTraceData(channel_Trace,noOfPoints,traceData)

.. function:: WriteMemoryTraceDataExt(channel_Trace,dataFormat,noOfPoints,traceData)

.. function:: SetTraceFormatZVR(dataFormat)

.. function:: GetTraceFormatZVR(dataFormat)

.. function:: TraceResponseDataZVR(dataFormat,valuesToReturn,noOfValues,traceData)

.. function:: TraceStimulusDataZVR(dataFormat,valuesToReturn,noOfValues,traceData)

.. function:: TraceResponseDataSParameterGroup(channel_Trace,dataFormat,valuesToReturn,noOfValues,traceData)

.. function:: TraceImportData(traceName,fileName)

.. function:: TraceExportData(traceName,fileName)

.. function:: TraceExportDataWithOptions(traceName,fileName,exportFormat,exportData)

.. function:: TraceExportDataWithOptionsExt(traceName,fileName,exportFormat,exportData,decimalSeparator,fieldSeparator)

.. function:: ChannelTraceExportData(selectChannel,channel_Trace,fileName)

.. function:: ChannelTraceExportDataWithOptions(selectChannel,channel_Trace,fileName,exportFormat,exportData)

.. function:: ChannelTraceExportDataWithOptionsExt(selectChannel,channel_Trace,fileName,exportFormat,exportData,decimalSeparator,fieldSeparator)

.. function:: TraceExportDataPorts(channel=1,fileName,exportData,port1,port2,port3,port4)

.. function:: TraceExportDataPortsIncomplete(channel=1,fileName,exportData,port1,port2,port3,port4)

.. function:: SetRenormalizationState(state)

.. function:: GetRenormalizationState(state)

.. function:: SetRenormalizationMode(mode)

.. function:: GetRenormalizationMode(mode)

.. function:: SetRenormalizationImpedance(impedance)

.. function:: GetRenormalizationImpedance(impedance)

.. function:: TraceShiftStimulusValue(window,window_Trace,shiftStimulusValue)

.. function:: TraceShiftResponseValue(window,window_Trace,magnitude,phase,real,imaginary)

.. function:: SetHold(channel=1,hold)

.. function:: GetHold(channel=1,hold)

.. function:: LinearityDeviationManual(channel=1,slope,constant,electricalLength)

.. function:: LinearityDeviationAuto(channel=1)

.. function:: SetLinearityDeviationState(channel=1,state)

.. function:: GetLinearityDeviationState(channel=1,state)

.. function:: SetLinearityDeviationSlope(channel=1,slope)

.. function:: GetLinearityDeviationSlope(channel=1,slope)

.. function:: SetLinearityDeviationConstant(channel=1,constant)

.. function:: GetLinearityDeviationConstant(channel=1,constant)

.. function:: SetLinearityDeviationElectricalLength(channel=1,electricalLength)

.. function:: GetLinearityDeviationElectricalLength(channel=1,electricalLength)

.. function:: SetMarkerState(channel_Trace,marker,markerState)

.. function:: GetMarkerState(channel_Trace,marker,markerState)

.. function:: SetMarkerStimulus(channel_Trace,marker,markerStimulus)

.. function:: GetMarkerStimulus(channel_Trace,marker,markerStimulus)

.. function:: GetMarkerResponse(channel_Trace,marker,markerResponse)

.. function:: SetReferenceMarkerState(channel_Trace,marker,referenceMarkerState)

.. function:: GetReferenceMarkerState(channel_Trace,marker,referenceMarkerState)

.. function:: SetReferenceMarkerStimulus(channel_Trace,marker,referenceMarkerStimulus)

.. function:: GetReferenceMarkerStimulus(channel_Trace,marker,referenceMarkerStimulus)

.. function:: GetReferenceMarkerResponse(channel_Trace,marker,referenceMarkerResponse)

.. function:: SetReferenceDiscreteMarker(channel_Trace,marker,mode)

.. function:: GetReferenceDiscreteMarker(channel_Trace,marker,mode)

.. function:: SetReferenceFixedMarker(channel_Trace,marker,type)

.. function:: GetReferenceFixedMarker(channel_Trace,marker,type)

.. function:: SetDeltaMarkerState(channel_Trace,marker,deltaMarkerState)

.. function:: GetDeltaMarkerState(channel_Trace,marker,deltaMarkerState)

.. function:: SetCoupledMarkers(channel_Trace,marker,markerCoupled)

.. function:: GetCoupledMarkers(channel_Trace,marker,markerCoupled)

.. function:: SetDiscreteMarker(channel_Trace,marker,discreteMode)

.. function:: GetDiscreteMarker(channel_Trace,marker,discreteMode)

.. function:: SetFixedMarker(channel_Trace,marker,fixedMarker)

.. function:: GetFixedMarker(channel_Trace,marker,fixedMarker)

.. function:: SetMarkerFormat(channel_Trace,marker,markerFormat)

.. function:: GetMarkerFormat(channel_Trace,marker,markerFormat)

.. function:: SetAllMarkersOff(channel_Trace)

.. function:: SaveAllMarkers(fileName)

.. function:: MarkerSearch(channel_Trace,marker,search)

.. function:: MarkerTargetSearch(channel_Trace,marker,search)

.. function:: SetMarkerTargetValue(channel_Trace,marker,targetValue)

.. function:: GetMarkerTargetValue(channel_Trace,marker,targetValue)

.. function:: MarkerBandpassSearch(channel_Trace,marker)

.. function:: MarkerBandstopSearch(channel_Trace,marker)

.. function:: SetMarkerSearchMode(channel_Trace,marker,searchMode)

.. function:: GetMarkerSearchMode(channel_Trace,marker,searchMode)

.. function:: MarkerBandfilterTracking(channel_Trace,marker,bandfilterTracking)

.. function:: MarkerxdBBandwidth(channel_Trace,marker,xDBBandwidth)

.. function:: MarkerBandfilterResults(channel_Trace,marker,bandwidth,centerStimulus,q,loss,LBE,UBE)

.. function:: MarkerxdBBandwidthZVR(channel_Trace,marker,xDBBandwidth)

.. function:: MarkerBandfilterResultsZVR(channel_Trace,marker,bandwidth)

.. function:: SetMarkerSearchResultState(channel_Trace,marker,searchResults)

.. function:: GetMarkerSearchResultState(channel_Trace,marker,searchResults)

.. function:: SetMarkerTracking(channel_Trace,marker,markerTracking)

.. function:: GetMarkerTracking(channel_Trace,marker,markerTracking)

.. function:: MarkerSearchRange(channel_Trace,marker,searchRange,start,stop)

.. function:: SetMarkerSearchRangeShow(channel_Trace,marker,showRange)

.. function:: GetMarkerSearchRangeShow(channel_Trace,marker,showRange)

.. function:: MarkerSearchResults(channel_Trace,marker,markerStimulus,markerResponse)

.. function:: SetStartToMarker(channel_Trace,marker)

.. function:: SetStopToMarker(channel_Trace,marker)

.. function:: SetCenterToMarker(channel_Trace,marker)

.. function:: ShowLimitLine(channel_Trace,displayLimitLine)

.. function:: SetLimitCheck(channel_Trace,limitLine,limitCheck)

.. function:: GetLimitCheck(channel_Trace,limitLine,limitCheck)

.. function:: SetLimitLineFailBeep(channel_Trace,failBeep)

.. function:: GetLimitLineFailBeep(channel_Trace,failBeep)

.. function:: GetLimitCheckResult(channel_Trace,limitCheckResult)

.. function:: AddLimitLineSegment(channel_Trace,segment,type,startStimulus,stopStimulus,startResponse,stopResponse)

.. function:: EditLimitLineSegment(channel_Trace,segment,type,startStimulus,stopStimulus,startResponse,stopResponse)

.. function:: ReadLimitLineSegmentList(channel_Trace,listSize,segmentsCount,type,startStimulus,stopStimulus,startResponse,stopResponse)

.. function:: WriteLimitLineSegmentList(channel_Trace,listSize,type,startStimulus,stopStimulus,startResponse,stopResponse)

.. function:: ShiftLimitLineSegmentList(channel_Trace,limitLineType,stimulusOffset,responseOffset)

.. function:: DeleteLimitLineSegments(channel_Trace)

.. function:: RecallLimitLine(traceName,fileName)

.. function:: RecallLimitLineWithOptions(traceName,fileName,sParameter,xOffset,yOffset,type)

.. function:: SaveLimitLine(traceName,fileName)

.. function:: ImportTraceasLimitLine(channel_Trace,limitLineType,stimulusOffset,responseOffset,traceName)

.. function:: SetLimitLineTTLOutPass(channel_Trace,outputNo,TTLOutput)

.. function:: GetLimitLineTTLOutPass(channel_Trace,outputNo,TTLOutput)

.. function:: SetDisplayLine(channel_Trace,displayLine,position)

.. function:: GetDisplayLine(channel_Trace,displayLine,position)

.. function:: SetLimitDomainUnits(channel_Trace,domainUnits)

.. function:: SetLimitResponseDomainComplexUnits(channel_Trace,responseUnits)

.. function:: SetLimitResponseDomainFormatUnits(channel_Trace,responseUnits)

.. function:: SetLimitResponseDomainSpacingUnits(channel_Trace,responseUnits)

.. function:: SetRippleCheckOn(channel_Trace,limitCheck)

.. function:: GetRippleCheckOn(channel_Trace,limitCheck)

.. function:: GetRippleLimitGlobalCheckResult(channel_Trace,rippleLimitCheckResult)

.. function:: SetCheckRippleLimitRangeSegment(channel_Trace,segment,limitCheck)

.. function:: GetCheckRippleLimitRangeSegment(channel_Trace,segment,limitCheck)

.. function:: GetRippleLimitCheckSegmentResult(channel_Trace,segment,fail,limitCheckResult)

.. function:: SetRippleLimitsDisplayState(channel_Trace,displayLine)

.. function:: GetRippleLimitsDisplayState(channel_Trace,displayLine)

.. function:: SetRippleFailBeepOn(channel_Trace,failBeep)

.. function:: GetRippleFailBeepOn(channel_Trace,failBeep)

.. function:: AddRippleLimitLineRangesSegment(channel_Trace,noOfValues,type,startStimulus,stopStimulus,limit)

.. function:: EditRippleLimitLineSegment(channel_Trace,segment,startStimulus,stopStimulus)

.. function:: DeleteAllRippleLimitRanges(channel_Trace)

.. function:: SetRippleLimitPhysicalUnits(channel_Trace,physicalUnits)

.. function:: SetRippleLimitResponseDomainFormatUnits(channel_Trace,responseUnits)

.. function:: GetNumberRippleLimitRanges(channel_Trace,segment,number)

.. function:: SetRippleLimitRange(channel_Trace,segment,limit)

.. function:: GetRippleLimitRange(channel_Trace,segment,limit)

.. function:: SaveRecallRippleLimit(operationToBePerformed,traceName,fileName)

.. function:: SetStartFrequency(channel=1,startFrequency)

.. function:: GetStartFrequency(channel=1,startFrequency)

.. function:: SetStopFrequency(channel=1,stopFrequency)

.. function:: GetStopFrequency(channel=1,stopFrequency)

.. function:: SetCenterFrequency(channel=1,centerFrequency)

.. function:: GetCenterFrequency(channel=1,centerFrequency)

.. function:: SetFrequencySpan(channel=1,span)

.. function:: GetFrequencySpan(channel=1,span)

.. function:: SetPower(channel=1,power)

.. function:: GetPower(channel=1,power)

.. function:: SetCWFrequency(channel=1,CWFrequency)

.. function:: GetCWFrequency(channel=1,CWFrequency)

.. function:: SetStartPower(channel=1,startPower)

.. function:: GetStartPower(channel=1,startPower)

.. function:: SetStopPower(channel=1,stopPower)

.. function:: GetStopPower(channel=1,stopPower)

.. function:: SetSourcePort(channel=1,sourcePort)

.. function:: GetSourcePort(channel=1,sourcePort)

.. function:: ConfigurePowerBandwidthAverage(channel=1,RFState,measBandwidth,averageState,averageFactor)

.. function:: SetReceiverStepAttenuators(channel=1,analyzerPort,attenuationFactor)

.. function:: GetReceiverStepAttenuators(channel=1,analyzerPort,attenuationFactor)

.. function:: SetGeneratorStepAttenuators(channel=1,port,attenuationFactor)

.. function:: GetGeneratorStepAttenuators(channel=1,port,attenuationFactor)

.. function:: SetAutomaticGeneratorAttenuator(channel=1,port,automaticAttenuation)

.. function:: GetAutomaticGeneratorAttenuator(channel=1,port,automaticAttenuation)

.. function:: GetAutomaticGeneratorAttenuation(channel=1,port,attenuation)

.. function:: SetGeneratorAttenuatorMode(channel=1,port,attenuationMode)

.. function:: GetGeneratorAttenuatorMode(channel=1,port,attenuationMode)

.. function:: SetRFState(RFState)

.. function:: GetRFState(RFState)

.. function:: SetMeasBandwidth(channel=1,measBandwidth)

.. function:: GetMeasBandwidth(channel=1,measBandwidth)

.. function:: SetMeasBandwidthSelectivity(channel=1,measBandwidthSelectivity)

.. function:: GetMeasBandwidthSelectivity(channel=1,measBandwidthSelectivity)

.. function:: SetMeasBandwidthReduction(channel=1,reduction)

.. function:: GetMeasBandwidthReduction(channel=1,reduction)

.. function:: SetAverageState(channel=1,averageState)

.. function:: GetAverageState(channel=1,averageState)

.. function:: SetAverageFactor(channel=1,averageFactor)

.. function:: GetAverageFactor(channel=1,averageFactor)

.. function:: GetCurrentSweep(channel=1,currentSweep)

.. function:: RestartAverage(channel=1)

.. function:: SetPartialMeasurementResolutionBandwidthMode(channel=1,bandwidthMode)

.. function:: GetPartialMeasurementResolutionBandwidthMode(channel=1,bandwidthMode)

.. function:: SetGeneratorPortResolutionBandwidth(channel=1,generatorPort,resolutionBandwidth)

.. function:: GetGeneratorPortResolutionBandwidth(channel=1,generatorPort,resolutionBandwidth)

.. function:: SetPhysicalPortResolutionBandwidth(channel=1,analyzerPort,resolutionBandwidth)

.. function:: GetPhysicalPortResolutionBandwidth(channel=1,analyzerPort,resolutionBandwidth)

.. function:: SetSweepType(channel=1,sweepType)

.. function:: GetSweepType(channel=1,sweepType)

.. function:: InsertNewSegment(channel=1,segment,startFrequency,stopFrequency,numberOfPoints,power,sweepTimeSelect,time,pointDelay,measBandwidth)

.. function:: RedefineSegment(channel=1,segment,startFrequency,stopFrequency,numberOfPoints,power,sweepTimeSelect,time,pointDelay,measBandwidth)

.. function:: AddNewSegment(channel=1,segment)

.. function:: DeleteSelectedSegment(channel=1,segment)

.. function:: DeleteAllSegments(channel=1)

.. function:: GetSweepSegmentsCount(channel=1,count)

.. function:: SetSweepSegmentState(channel=1,segment,state)

.. function:: GetSweepSegmentState(channel=1,segment,state)

.. function:: SetSweepSegmentStartFrequency(channel=1,segment,startFrequency)

.. function:: GetSweepSegmentStartFrequency(channel=1,segment,startFrequency)

.. function:: SetSweepSegmentStopFrequency(channel=1,segment,stopFrequency)

.. function:: GetSweepSegmentStopFrequency(channel=1,segment,stopFrequency)

.. function:: SetSweepSegmentNumberOfPoints(channel=1,segment,numberOfPoints)

.. function:: GetSweepSegmentNumberOfPoints(channel=1,segment,numberOfPoints)

.. function:: SetSweepSegmentName(channel=1,segment,name)

.. function:: GetSweepSegmentName(channel=1,segment,bufferSize,name)

.. function:: SetSweepSegmentPower(channel=1,segment,power)

.. function:: GetSweepSegmentPower(channel=1,segment,power)

.. function:: SetSweepSegmentIndependentPower(channel=1,segment,power)

.. function:: GetSweepSegmentIndependentPower(channel=1,segment,power)

.. function:: SetSweepSegmentMeasBandwidth(channel=1,segment,measBandwidth)

.. function:: GetSweepSegmentMeasBandwidth(channel=1,segment,measBandwidth)

.. function:: SetSweepSegmentIndependentBandwidth(channel=1,segment,measBandwidth)

.. function:: GetSweepSegmentIndependentBandwidth(channel=1,segment,measBandwidth)

.. function:: SetSweepSegmentSpurAvoid(channel=1,segment,spurAvoid)

.. function:: GetSweepSegmentSpurAvoid(channel=1,segment,spurAvoid)

.. function:: SetSweepSegmentIndependentSpurAvoid(channel=1,segment,spurAvoid)

.. function:: GetSweepSegmentIndependentSpurAvoid(channel=1,segment,spurAvoid)

.. function:: SetSweepSegmentSelectivity(channel=1,segment,selectivity)

.. function:: GetSweepSegmentSelectivity(channel=1,segment,selectivity)

.. function:: SetSweepSegmentIndependentSelectivity(channel=1,segment,selectivity)

.. function:: GetSweepSegmentIndependentSelectivity(channel=1,segment,selectivity)

.. function:: SetSweepSegmentSweepTime(channel=1,segment,time)

.. function:: GetSweepSegmentSweepTime(channel=1,segment,time)

.. function:: SetSweepSegmentIndependentTime(channel=1,segment,time)

.. function:: GetSweepSegmentIndependentTime(channel=1,segment,time)

.. function:: SetSweepSegmentPointDelay(channel=1,segment,pointDelay)

.. function:: GetSweepSegmentPointDelay(channel=1,segment,pointDelay)

.. function:: SetSweepSegmentIndependentPointDelay(channel=1,segment,pointDelay)

.. function:: GetSweepSegmentIndependentPointDelay(channel=1,segment,pointDelay)

.. function:: SetSweepSegmentTriggering(channel=1,segment,triggering)

.. function:: GetSweepSegmentTriggering(channel=1,segment,triggering)

.. function:: SetSweepSelectiveSegmentTriggering(channel=1,triggering)

.. function:: GetSweepSelectiveSegmentTriggering(channel=1,triggering)

.. function:: SetSweepSegmentBitsState(channel=1,state)

.. function:: GetSweepSegmentBitsState(channel=1,state)

.. function:: SetSweepSegmentBitValues(channel=1,segment,bit0,bit1,bit2,bit3)

.. function:: GetSweepSegmentBitValues(channel=1,segment,bit0,bit1,bit2,bit3)

.. function:: GetSweepSegmentCenterFrequency(channel=1,segment,centerFrequency)

.. function:: GetSweepSegmentFrequencySpan(channel=1,segment,frequencySpan)

.. function:: SaveSegment(channel=1,fileName)

.. function:: LoadSegment(channel=1,fileName)

.. function:: QueryOverlappingSweepSegments(segment,overlapping)

.. function:: QuerySumOfSweepSegmentsTime(channel=1,sweepTime)

.. function:: SetPulseTimeStart(channel=1,timeStart)

.. function:: GetPulseTimeStart(channel=1,timeStart)

.. function:: SetPulseTimeStop(channel=1,timeStop)

.. function:: GetPulseTimeStop(channel=1,timeStop)

.. function:: SetPulseTimeBandwidth(channel=1,timeBandwidth)

.. function:: GetPulseTimeBandwidth(channel=1,timeBandwidth)

.. function:: SetPulseCoupledSectionLimitLinesState(channel=1,coupleLimits)

.. function:: GetPulseCoupledSectionLimitLinesState(channel=1,coupleLimits)

.. function:: SetPulseEvaluationMode(channel=1,receiverType,recordNumber,interfaceType,generatorPortNumber,evaluationMode)

.. function:: GetPulseEvaluationMode(channel=1,receiverType,recordNumber,interfaceType,generatorPortNumber,evaluationMode)

.. function:: SetPulseEvaluationSectionStart(channel=1,receiverType,recordNumber,interfaceType,generatorPortNumber,evaluationStartTime)

.. function:: GetPulseEvaluationSectionStart(channel=1,receiverType,recordNumber,interfaceType,generatorPortNumber,evaluationStartTime)

.. function:: SetPulseEvaluationSectionStop(channel=1,receiverType,recordNumber,interfaceType,generatorPortNumber,evaluationStopTime)

.. function:: GetPulseEvaluationSectionStop(channel=1,receiverType,recordNumber,interfaceType,generatorPortNumber,evaluationStopTime)

.. function:: SetPulseSectionLimitLinesState(channel=1,receiverType,recordNumber,interfaceType,generatorPortNumber,limitLinesState)

.. function:: GetPulseSectionLimitLinesState(channel=1,receiverType,recordNumber,interfaceType,generatorPortNumber,limitLinesState)

.. function:: SetPulseShiftStimulus(channel=1,receiverType,recordNumber,interfaceType,generatorPortNumber,shiftStimulus)

.. function:: GetPulseShiftStimulus(channel=1,receiverType,recordNumber,interfaceType,generatorPortNumber,shiftStimulus)

.. function:: ReadTimeSamplesData(channel_Trace,noOfValues,traceData)

.. function:: SetSweepNumberOfPoints(channel=1,numberOfPoints)

.. function:: GetSweepNumberOfPoints(channel=1,numberOfPoints)

.. function:: SetFrequencyStepSize(channel=1,stepSize)

.. function:: GetFrequencyStepSize(channel=1,stepSize)

.. function:: SetSweepCount(channel=1,sweepCount)

.. function:: GetSweepCount(channel=1,sweepCount)

.. function:: ConfigureSweepTime(channel=1,autoSweepTime,sweepTime,measDelay)

.. function:: SetSweepTime(channel=1,sweepTime)

.. function:: GetSweepTime(channel=1,sweepTime)

.. function:: SetSweepMeasDelay(channel=1,measDelay)

.. function:: GetSweepMeasDelay(channel=1,measDelay)

.. function:: SetSweepTimeAuto(channel=1,autoSweepTime)

.. function:: GetSweepTimeAuto(channel=1,autoSweepTime)

.. function:: ConfigureTriggerFreeRun(channel=1)

.. function:: ConfigureTriggerExternal(channel=1,triggerOn)

.. function:: ConfigureTriggerPeriodic(channel=1,triggerPeriod)

.. function:: ConfigureTriggerRFPower(channel=1)

.. function:: ConfigureTriggerManual(channel=1)

.. function:: ConfigureTriggerSettings(channel=1,triggerMeasSequence,triggerDelay)

.. function:: SetTriggerSource(channel=1,triggerSource)

.. function:: GetTriggerSource(channel=1,triggerSource)

.. function:: SetTriggerDelay(channel=1,triggerDelay)

.. function:: GetTriggerDelay(channel=1,triggerDelay)

.. function:: SetPartialMeasurementTriggerMode(channel=1,triggerMode)

.. function:: GetPartialMeasurementTriggerMode(channel=1,triggerMode)

.. function:: SetGeneratorPortTriggerDelay(channel=1,generatorPort,triggerDelay)

.. function:: GetGeneratorPortTriggerDelay(channel=1,generatorPort,triggerDelay)

.. function:: SetPhysicalPortTriggerDelay(channel=1,analyzerPort,triggerDelay)

.. function:: GetPhysicalPortTriggerDelay(channel=1,analyzerPort,triggerDelay)

.. function:: SetTriggeredMeasSequence(channel=1,triggerMeasSequence)

.. function:: GetTriggeredMeasSequence(channel=1,triggerMeasSequence)

.. function:: SetTriggerOn(channel=1,triggerOn)

.. function:: GetTriggerOn(channel=1,triggerOn)

.. function:: SetTriggerPeriod(channel=1,triggerPeriod)

.. function:: GetTriggerPeriod(channel=1,triggerPeriod)

.. function:: SendTrigger()

.. function:: SendTriggerWaitOPC(timeout)

.. function:: SendChannelTrigger(channel=1)

.. function:: SendChannelTriggerWaitOPC(channel=1,timeout)

.. function:: SetSweepSingleAllChans(singleSweep)

.. function:: GetSweepSingleAllChans(singleSweep)

.. function:: SweepRestart(channel=1)

.. function:: SetSweepSingle(channel=1,singleSweep)

.. function:: GetSweepSingle(channel=1,singleSweep)

.. function:: DefineGroupOfMeasuredPorts(channel=1,group,firstPort,lastPort)

.. function:: GetGroupOfMeasuredPorts(channel=1,group,firstPort,lastPort)

.. function:: DefineGroupOfAllMeasuredPorts(channel=1,group,numberOfPortsInGroup,ports)

.. function:: GetGroupOfAllMeasuredPorts(channel=1,group,numberOfPortsInGroup,ports)

.. function:: GetPortGroupsCount(channel=1,portGroups)

.. function:: DeleteGroupOfMeasuredPorts(channel=1,group)

.. function:: DeleteAllGroupsOfMeasuredPorts(channel=1)

.. function:: DefineBalancedPort(channel=1,logicalPort,physicalPort1,physicalPort2)

.. function:: GetBalancedPort(channel=1,logicalPort,physicalPort1,physicalPort2)

.. function:: DeleteBalancedPort(channel=1,logicalPort)

.. function:: DeleteAllBalancedPorts(channel=1)

.. function:: SetDifferentialModeImpedance(channel=1,logicalPort,impedance)

.. function:: GetDifferentialModeImpedance(channel=1,logicalPort,impedance)

.. function:: SetCommonModeImpedance(channel=1,logicalPort,impedance)

.. function:: GetCommonModeImpedance(channel=1,logicalPort,impedance)

.. function:: DefinePortPair(channel=1,functionType,portPair,port1,port2)

.. function:: DeletePortPair(channel=1,functionType,portPair)

.. function:: SetDefaultConfigurationState(defaultSettings)

.. function:: GetDefaultConfigurationState(defaultSettings)

.. function:: SetPortConfigration(channel=1,portGroupA,portGroupB,portGroupC,portGroupD)

.. function:: GetPortConfigration(channel=1,portGroupA,portGroupB,portGroupC,portGroupD)

.. function:: SetConverterPowerOffset(channel=1,port,portPowerOffset,offsetParameter)

.. function:: GetConverterPowerOffset(channel=1,port,portPowerOffset,offsetParameter)

.. function:: SetConverterCalPowerOffset(channel=1,converter,calPowerOffset)

.. function:: GetConverterCalPowerOffset(channel=1,converter,calPowerOffset)

.. function:: SetAdvancedPowerTransferModelFrequencyState(channel=1,state)

.. function:: GetAdvancedPowerTransferModelFrequencyState(channel=1,state)

.. function:: SetSenseTypeOfPortTransferModel(channel=1,port,modelType)

.. function:: GetSenseTypeOfPortTransferModel(channel=1,port,modelType)

.. function:: SetSenseTypeOfAdvancedPowerTransferModel(channel=1,modelType)

.. function:: GetSenseTypeOfAdvancedPowerTransferModel(channel=1,modelType)

.. function:: SetConverterDataSetType(port,dataSetType)

.. function:: GetConverterDataSetType(port,dataSetType)

.. function:: SetConverterUserDataSetDirectory(port,directory)

.. function:: GetConverterUserDataSetDirectory(port,bufferSize,directory)

.. function:: SetConverterPortAssignment(port,serialNumber)

.. function:: GetConverterPortAssignment(port,bufferSize,serialNumber)

.. function:: SetPortTransferModelState(channel=1,port,state)

.. function:: GetPortTransferModelState(channel=1,port,state)

.. function:: SetPortWaveguideAttenuator(channel=1,port,waveguideAttenuator,attenuation)

.. function:: GetPortWaveguideAttenuatorType(channel=1,port,waveguideAttenuator)

.. function:: GetPortWaveguideAttenuator(channel=1,port,waveguideAttenuator,attenuation)

.. function:: SetPortWaveguideAttenuatorSlope(channel=1,port,slope)

.. function:: GetPortWaveguideAttenuatorSlope(channel=1,port,slope)

.. function:: SetPortWaveguideAttenuatorOffset(channel=1,port,offset)

.. function:: GetPortWaveguideAttenuatorOffset(channel=1,port,offset)

.. function:: SetPortElectronicPowerTreshold(channel=1,port,threshold)

.. function:: GetPortElectronicPowerTreshold(channel=1,port,threshold)

.. function:: SetPortElectronicPowerReduction(channel=1,port,reduction)

.. function:: GetPortElectronicPowerReduction(channel=1,port,reduction)

.. function:: SetSimultaneousMeasurementOfPortsGroups(channel=1,state)

.. function:: GetSimultaneousMeasurementOfPortsGroups(channel=1,state)

.. function:: SetSimultaneousMeasurementFrequencyOffsetState(channel=1,state)

.. function:: GetSimultaneousMeasurementFrequencyOffsetState(channel=1,state)

.. function:: SetSimultaneousMeasurementMinimumFrequencyOffsetMode(channel=1,minimumFrequencyOffset)

.. function:: GetSimultaneousMeasurementMinimumFrequencyOffsetMode(channel=1,minimumFrequencyOffset)

.. function:: SetFrequencyConversion(measurementType,channel=1,port,numerator,denominator,offset,sweepType)

.. function:: GetFrequencyConversion(measurementType,channel=1,port,numerator,denominator,offset,sweepType)

.. function:: SetPowerMeterFrequencyConversion(channel=1,powerMeterNumber,numerator,denominator,offset,sweepType)

.. function:: GetPowerMeterFrequencyConversion(channel=1,powerMeterNumber,numerator,denominator,offset,sweepType)

.. function:: SetGeneratorFrequencyConversion(channel=1,port,generatorNumber,state,numerator,denominator,offset,sweepType)

.. function:: GetGeneratorFrequencyConversion(channel=1,port,generatorNumber,state,numerator,denominator,offset,sweepType)

.. function:: SetConverterSourceFrequency(channel=1,port,numerator,denominator,offset,sweepType)

.. function:: GetConverterSourceFrequency(channel=1,port,numerator,denominator,offset,sweepType)

.. function:: SetMeasureAWavesState(channel=1,state)

.. function:: GetMeasureAWavesState(channel=1,state)

.. function:: SetLocalOscilatorAState(channel=1,port,state)

.. function:: GetLocalOscilatorAState(channel=1,port,state)

.. function:: SetLocalOscilatorBState(channel=1,port,state)

.. function:: GetLocalOscilatorBState(channel=1,port,state)

.. function:: SetLogicalPortCommonRefImpedance(channel=1,port,real,imaginary)

.. function:: GetLogicalPortCommonRefImpedance(channel=1,port,real,imaginary)

.. function:: SetLogicalPortDifferentialRefImpedance(channel=1,port,real,imaginary)

.. function:: GetLogicalPortDifferentialRefImpedance(channel=1,port,real,imaginary)

.. function:: SetPortImpedancesRenormalization(channel=1,theory)

.. function:: GetPortImpedancesRenormalization(channel=1,theory)

.. function:: SetPhysicalPortRefImpedance(channel=1,port,real,imaginary)

.. function:: GetPhysicalPortRefImpedance(channel=1,port,real,imaginary)

.. function:: SetIFGain(channel=1,port,IFGain)

.. function:: GetIFGain(channel=1,port,IFGain)

.. function:: SetIFGainReferenceChannel(channel=1,port,IFGain)

.. function:: GetIFGainReferenceChannel(channel=1,port,IFGain)

.. function:: SetRFSignalSourceState(channel=1,port,state)

.. function:: GetRFSignalSourceState(channel=1,port,state)

.. function:: SetPermanentSignalSourceState(channel=1,port,state)

.. function:: GetPermanentSignalSourceState(channel=1,port,state)

.. function:: SetPermanentSignalGeneratorState(channel=1,port,generatorNumber,state)

.. function:: GetPermanentSignalGeneratorState(channel=1,port,generatorNumber,state)

.. function:: SetPortPowerGeneratorOffset(channel=1,portNumber,generatorNumber,portPowerOffset,offsetParameter)

.. function:: GetPortPowerGeneratorOffset(channel=1,portNumber,generatorNumber,portPowerOffset,offsetParameter)

.. function:: SetSlope(channel=1,port,slope)

.. function:: GetSlope(channel=1,port,slope)

.. function:: SetSourceCombinerState(channel=1,state)

.. function:: GetSourceCombinerState(channel=1,state)

.. function:: SetFrequencyStimulus(channel=1,frequencyStimulus)

.. function:: GetFrequencyStimulus(channel=1,frequencyStimulus)

.. function:: SetPowerStimulus(channel=1,powerStimulus)

.. function:: GetPowerStimulus(channel=1,powerStimulus)

.. function:: SetTDIFState(channel=1,trueDifferentialModeState)

.. function:: GetTDIFState(channel=1,trueDifferentialModeState)

.. function:: SetTDIFAmplitudeImbalanceLogicalPort(channel=1,port)

.. function:: GetTDIFAmplitudeImbalanceLogicalPort(channel=1,port)

.. function:: SetTDIFAmplitudeImbalanceStartPower(channel=1,startPower)

.. function:: GetTDIFAmplitudeImbalanceStartPower(channel=1,startPower)

.. function:: SetTDIFAmplitudeImbalanceStopPower(channel=1,stopPower)

.. function:: GetTDIFAmplitudeImbalanceStopPower(channel=1,stopPower)

.. function:: SetTDIFPhaseImbalanceLogicalPort(channel=1,port)

.. function:: GetTDIFPhaseImbalanceLogicalPort(channel=1,port)

.. function:: SetTDIFPhaseImbalanceStartPhase(channel=1,startPhase)

.. function:: GetTDIFPhaseImbalanceStartPhase(channel=1,startPhase)

.. function:: SetTDIFPhaseImbalanceStopPhase(channel=1,stopPhase)

.. function:: GetTDIFPhaseImbalanceStopPhase(channel=1,stopPhase)

.. function:: SetTDIFSourcePowerMode(channel=1,sourcePowerMode)

.. function:: GetTDIFSourcePowerMode(channel=1,sourcePowerMode)

.. function:: SetTDIFCompensationState(channel=1,compensationState)

.. function:: GetTDIFCompensationState(channel=1,compensationState)

.. function:: SetTDIFReceiverFrequency(channel=1,receiverFrequency)

.. function:: GetTDIFReceiverFrequency(channel=1,receiverFrequency)

.. function:: SetPulseGeneratorState(channel=1,pulseGeneratorState)

.. function:: GetPulseGeneratorState(channel=1,pulseGeneratorState)

.. function:: DefinePulseGenerator(channel=1,generator,pulseType,pulseWidth,singleTrainPulsePeriod,pulsePolarity,pulseMode)

.. function:: DefinePulseTrainSegments(channel=1,bufferSize,pulseTrainActive,startTime,stopTime)

.. function:: ConfigureChoppedPulseProfile(channel=1,choppedPulseProfileMode,delayIncrement)

.. function:: SetPulseGeneratorType(channel=1,generator,pulseType)

.. function:: GetPulseGeneratorType(channel=1,generator,pulseType)

.. function:: SetPulseGeneratorWidth(channel=1,generator,pulseWidth)

.. function:: GetPulseGeneratorWidth(channel=1,generator,pulseWidth)

.. function:: SetPulseGeneratorSinglePeriod(channel=1,singlePulsePeriod)

.. function:: GetPulseGeneratorSinglePeriod(channel=1,singlePulsePeriod)

.. function:: SetPulseGeneratorTrainPeriod(channel=1,trainPulsePeriod)

.. function:: GetPulseGeneratorTrainPeriod(channel=1,trainPulsePeriod)

.. function:: SetPulseGeneratorPolarity(channel=1,generator,pulsePolarity)

.. function:: GetPulseGeneratorPolarity(channel=1,generator,pulsePolarity)

.. function:: SetPulseGeneratorMode(channel=1,pulseMode)

.. function:: GetPulseGeneratorMode(channel=1,pulseMode)

.. function:: SetPulseGeneratorMasterChannel(masterChannel)

.. function:: GetPulseGeneratorMasterChannel(masterChannel)

.. function:: GetPulseTrainSegments(channel=1,bufferSize,pulseTrainActive,startTime,stopTime)

.. function:: SetPulseTrainSegmentState(channel=1,segment,segmentState)

.. function:: GetPulseTrainSegmentState(channel=1,segment,segmentState)

.. function:: SetPulseTrainSegmentStart(channel=1,segment,segmentStart)

.. function:: GetPulseTrainSegmentStart(channel=1,segment,segmentStart)

.. function:: SetPulseTrainSegmentStop(channel=1,segment,segmentStop)

.. function:: GetPulseTrainSegmentStop(channel=1,segment,segmentStop)

.. function:: GetPulseTrainSegmentCount(channel=1,segmentCount)

.. function:: DeleteAllPulseTrainSegments(channel=1)

.. function:: SavePulseTrainFile(channel=1,generator,fileName)

.. function:: LoadPulseTrainFile(channel=1,generator,fileName)

.. function:: SetPulseGeneratorDelay(channel=1,delay)

.. function:: GetPulseGeneratorDelay(channel=1,delay)

.. function:: SetChoppedPulseProfileMode(channel=1,choppedPulseProfileMode)

.. function:: GetChoppedPulseProfileMode(channel=1,choppedPulseProfileMode)

.. function:: SetChoppedPulseProfileDelayIncrement(channel=1,delayIncrement)

.. function:: GetChoppedPulseProfileDelayIncrement(channel=1,delayIncrement)

.. function:: ConfigureZVAXPath(channel=1,path,internalCombiner,harmonicFilter,pulseModulator)

.. function:: ConfigurePulseGenerators(channel=1,extSignalGeneratorInput,extSignalGeneratorOutput,assignment)

.. function:: SetInternalCombiner(channel=1,internalCombiner)

.. function:: GetInternalCombiner(channel=1,internalCombiner)

.. function:: SetHarmonicFilter(channel=1,path,harmonicFilter)

.. function:: GetHarmonicFilter(channel=1,path,harmonicFilter)

.. function:: SetLNPreamplifier(channel=1,state)

.. function:: GetLNPreamplifier(channel=1,state)

.. function:: SetPulseModulator(channel=1,path,pulseModulator)

.. function:: GetPulseModulator(channel=1,path,pulseModulator)

.. function:: SetExternalSignalGeneratorInput(channel=1,extSignalGeneratorInput)

.. function:: GetExternalSignalGeneratorInput(channel=1,extSignalGeneratorInput)

.. function:: SetPulseGeneratorAssignment(channel=1,assignment)

.. function:: GetPulseGeneratorAssignment(channel=1,assignment)

.. function:: SetExternalSignalGeneratorOutput(channel=1,extSignalGeneratorOutput)

.. function:: GetExternalSignalGeneratorOutput(channel=1,extSignalGeneratorOutput)

.. function:: SetTRMMeasureInput(channel=1,path,input)

.. function:: GetTRMMeasureInput(channel=1,path,input)

.. function:: SetTRMCombinerState(channel=1,path,combinerState)

.. function:: GetTRMCombinerState(channel=1,path,combinerState)

.. function:: SetTRMPowerAmplifierState(channel=1,path,powerAmplifierState)

.. function:: GetTRMPowerAmplifierState(channel=1,path,powerAmplifierState)

.. function:: SetTRMPulseModulatorState(channel=1,path,pulseModulatorState)

.. function:: GetTRMPulseModulatorState(channel=1,path,pulseModulatorState)

.. function:: SetTRMUserSourcePathExtensionState(channel=1,path,userSourcePathExtension)

.. function:: GetTRMUserSourcePathExtensionState(channel=1,path,userSourcePathExtension)

.. function:: SetTRMUserMeasurementPathExtensionState(channel=1,path,userMeasurementPathExtension)

.. function:: GetTRMUserMeasurementPathExtensionState(channel=1,path,userMeasurementPathExtension)

.. function:: SetTRMPulseModulatorSource(channel=1,path,pulseModulatorSource)

.. function:: GetTRMPulseModulatorSource(channel=1,path,pulseModulatorSource)

.. function:: SetTRMPulseGeneratorSource(channel=1,extOut,pulseGeneratorSource)

.. function:: GetTRMPulseGeneratorSource(channel=1,extOut,pulseGeneratorSource)

.. function:: SetTRMPulseGeneratorInvertSource(channel=1,extOut,invertSource)

.. function:: GetTRMPulseGeneratorInvertSource(channel=1,extOut,invertSource)

.. function:: GetTRMNumberOfUnits(numberOfUnits)

.. function:: GetTRMUnitDeviceID(bufferSize,deviceID)

.. function:: GetTRMUnitHardwareOptions(bufferSize,optionList)

.. function:: ConfigureHarmonicMeasurement(channel=1,harmonicMeasurement,relativeHarmonicMeasurement,source,harmonicMeasuredAt,harmonicOrder)

.. function:: SetHarmonicMeasurementState(channel=1,harmonicMeasurement)

.. function:: GetHarmonicMeasurementState(channel=1,harmonicMeasurement)

.. function:: SetHarmonicOrder(channel=1,harmonicOrder)

.. function:: GetHarmonicOrder(channel=1,harmonicOrder)

.. function:: SetHarmonicSourcePort(channel=1,port)

.. function:: GetHarmonicSourcePort(channel=1,port)

.. function:: SetHarmonicReceivePort(channel=1,port)

.. function:: GetHarmonicReceivePort(channel=1,port)

.. function:: SetHarmonicRelativeState(channel=1,relativeHarmonicMeasurement)

.. function:: GetHarmonicRelativeState(channel=1,relativeHarmonicMeasurement)

.. function:: SetMixerMode(channel=1,mixerMode)

.. function:: GetMixerMode(channel=1,mixerMode)

.. function:: SetNumberOfStages(channel=1,numberOfStages)

.. function:: GetNumberOfStages(channel=1,numberOfStages)

.. function:: SetSignalSource(channel=1,stage,source,portNumber)

.. function:: GetSignalSource(channel=1,stage,source,portNumber)

.. function:: SetIFSignalPort(channel=1,portNumber)

.. function:: GetIFSignalPort(channel=1,portNumber)

.. function:: SetRFSignalPort(channel=1,portNumber)

.. function:: GetRFSignalPort(channel=1,portNumber)

.. function:: SetInternalSignalSource(channel=1,internalSignalSource)

.. function:: GetInternalSignalSource(channel=1,internalSignalSource)

.. function:: SetExternalSignalSource(channel=1,externalSignalSource)

.. function:: GetExternalSignalSource(channel=1,externalSignalSource)

.. function:: ConfigurePowerSettings(channel=1,fundamentalPower,fixedPower)

.. function:: SetFundamentalPowerSignal(channel=1,fundamentalPower)

.. function:: GetFundamentalPowerSignal(channel=1,fundamentalPower)

.. function:: SetFixedPower(channel=1,fixedPower)

.. function:: GetFixedPower(channel=1,fixedPower)

.. function:: SetFixedPowerToSignal(channel=1,signal,fixedPower)

.. function:: GetFixedPowerToSignal(channel=1,signal,fixedPower)

.. function:: SetSignalPowerMode(channel=1,signal,mode)

.. function:: GetSignalPowerMode(channel=1,signal,mode)

.. function:: ConfigureFrequencySettings(channel=1,fundamentalFrequencySignal,fixedFrequencySignal,fixedFrequency,frequencyConversionMode)

.. function:: SetFundamentalFrequencySignal(channel=1,fundamentalFrequency)

.. function:: GetFundamentalFrequencySignal(channel=1,fundamentalFrequency)

.. function:: SetFixedFrequencySignal(channel=1,fixedFrequency)

.. function:: GetFixedFrequencySignal(channel=1,fixedFrequency)

.. function:: SetFixedFrequencySignalStage2(channel=1,fixedFrequency)

.. function:: GetFixedFrequencySignalStage2(channel=1,fixedFrequency)

.. function:: SetFixedFrequency(channel=1,fixedFrequency)

.. function:: GetFixedFrequency(channel=1,fixedFrequency)

.. function:: SetFixedFrequencyToSignal(channel=1,signal,fixedFrequency)

.. function:: GetFixedFrequencyToSignal(channel=1,signal,fixedFrequency)

.. function:: SetFrequencyConversionMode(channel=1,frequencyConversionMode)

.. function:: GetFrequencyConversionMode(channel=1,frequencyConversionMode)

.. function:: SetFrequencyConversionModeStage2(channel=1,frequencyConversionMode)

.. function:: GetFrequencyConversionModeStage2(channel=1,frequencyConversionMode)

.. function:: SetFrequencyHighAccuracy(channel=1,highAccuracy)

.. function:: GetFrequencyHighAccuracy(channel=1,highAccuracy)

.. function:: SetFrequencyLOConversionFactor(channel=1,stage,numerator,denominator)

.. function:: GetFrequencyLOConversionFactor(channel=1,stage,numerator,denominator)

.. function:: SetFrequencyRFConversionFactor(channel=1,numerator,denominator)

.. function:: GetFrequencyRFConversionFactor(channel=1,numerator,denominator)

.. function:: SetRFImageFrequency(channel=1,RFImageFrequency)

.. function:: GetRFImageFrequency(channel=1,RFImageFrequency)

.. function:: SetExternalPowerMeter(channel=1,numberOfExternalPowerMeter)

.. function:: GetExternalPowerMeter(channel=1,numberOfExternalPowerMeter)

.. function:: RFSourceCalibration(channel=1)

.. function:: IFReceiverCalibration(channel=1)

.. function:: LOSourceCalibration(channel=1)

.. function:: LOSourceCalibrationStage2(channel=1)

.. function:: SetMixerDelayMeasurementSetup(channel=1,measurementSetup)

.. function:: GetMixerDelayMeasurementSetup(channel=1,measurementSetup)

.. function:: SetMixerDelayLANConnection(channel=1,LANConnection)

.. function:: GetMixerDelayLANConnection(channel=1,LANConnection)

.. function:: DefineMixerDelayReceiver(measurementSetup)

.. function:: ClearMixerDelayReceiverList()

.. function:: StartMixerDelayCalibrationSweep(channel=1)

.. function:: SetMixerDelayAperture(channel=1,aperture)

.. function:: GetMixerDelayAperture(channel=1,aperture)

.. function:: SetMixerDelayConstant(channel=1,constantDelay)

.. function:: GetMixerDelayConstant(channel=1,constantDelay)

.. function:: SetMixerDelayCombinerState(channel=1,internalCombiner)

.. function:: GetMixerDelayCombinerState(channel=1,internalCombiner)

.. function:: SetMixerDelayDivisionByTwoEnabled(channel=1,divisionByTwo)

.. function:: GetMixerDelayDivisionByTwoEnabled(channel=1,divisionByTwo)

.. function:: SetMixerConstantDelayEnabled(channel=1,constantDelay)

.. function:: GetMixerConstantDelayEnabled(channel=1,constantDelay)

.. function:: SetMixerDelayCorrection(channel=1,correction)

.. function:: GetMixerDelayCorrection(channel=1,correction)

.. function:: SetMixerDelayUpperToneSource(channel=1,source,portNumber)

.. function:: GetMixerDelayUpperToneSource(channel=1,source,portNumber)

.. function:: LoadMixerDelayValues(channel=1,type,file)

.. function:: LoadMixerDelayCalibrationData(channel=1,file)

.. function:: StoreMixerDelayCalibrationData(channel=1,file)

.. function:: SetVectorMixerMode(channel=1,mixerMode)

.. function:: GetVectorMixerMode(channel=1,mixerMode)

.. function:: SetInternalSignalSourceAUX(channel=1,internalSignalSource)

.. function:: GetInternalSignalSourceAUX(channel=1,internalSignalSource)

.. function:: SetExternalSignalSourceAUX(channel=1,externalSignalSource)

.. function:: GetExternalSignalSourceAUX(channel=1,externalSignalSource)

.. function:: SetAUXMixerPort(channel=1,portNumber)

.. function:: GetAUXMixerPort(channel=1,portNumber)

.. function:: SetAUXFixedPower(channel=1,fixedPower)

.. function:: GetAUXFixedPower(channel=1,fixedPower)

.. function:: AutomaticVectorMixerCalibration(channel=1,mode,dispersion,mixerParameter,delayPhase)

.. function:: SetIMODLowerToneSource(channel=1,source,sourceNumber)

.. function:: GetIMODLowerToneSource(channel=1,source,sourceNumber)

.. function:: SetIMODUpperToneSource(channel=1,source,sourceNumber)

.. function:: GetIMODUpperToneSource(channel=1,source,sourceNumber)

.. function:: SetIMODToneDistance(channel=1,toneDistance)

.. function:: GetIMODToneDistance(channel=1,toneDistance)

.. function:: SetIMODReceiverPort(channel=1,receiverPort)

.. function:: GetIMODReceiverPort(channel=1,receiverPort)

.. function:: SetIMODMeasurementOrder(channel=1,productOrder,measurementState)

.. function:: GetIMODMeasurementOrder(channel=1,productOrder,measurementState)

.. function:: SetIMODEnhancedWaveCorrection(channel=1,state)

.. function:: GetIMODEnhancedWaveCorrection(channel=1,state)

.. function:: SetIMODInternalCombiner(channel=1,internalCombiner)

.. function:: GetIMODInternalCombiner(channel=1,internalCombiner)

.. function:: SetIMODSpectrumMeasurement(channel=1,spectrumMeasurement)

.. function:: GetIMODSpectrumMeasurement(channel=1,spectrumMeasurement)

.. function:: SetIMODMaxOrder(channel=1,maxOrder)

.. function:: GetIMODMaxOrder(channel=1,maxOrder)

.. function:: SetIMODTwoToneOutput(channel=1,twoToneOutput)

.. function:: GetIMODTwoToneOutput(channel=1,twoToneOutput)

.. function:: StartIMODLowerToneSourcePowerCalibration(channel=1)

.. function:: StartIMODUpperToneSourcePowerCalibration(channel=1)

.. function:: StartIMODReceivePortSourcePowerCalibration(channel=1)

.. function:: StartIMODLowerUpperTonePortsSourcePowerCalibration(channel=1)

.. function:: StartIMODReceiverPortPowerCalibration(channel=1)

.. function:: StartIMODReceiverPowerCalibration(channel=1)

.. function:: SetIMODDistortionMeasurementCalibrationState(channel=1,state)

.. function:: GetIMODDistortionMeasurementCalibrationState(channel=1,state)

.. function:: DisableIMODMeasurement(channel=1)

.. function:: SetNoiseFigureDetectorMeasurementTime(channel=1,detectorTime)

.. function:: GetNoiseFigureDetectorMeasurementTime(channel=1,detectorTime)

.. function:: SetNoiseFigureMeasurementMode(channel=1,measurementMode)

.. function:: GetNoiseFigureMeasurementMode(channel=1,measurementMode)

.. function:: SetNoiseFigureLOOscillator(channel=1,LOOscillator)

.. function:: GetNoiseFigureLOOscillator(channel=1,LOOscillator)

.. function:: SetNoiseFigureNarowbandDUT(channel=1,narowbandDUT)

.. function:: GetNoiseFigureNarowbandDUT(channel=1,narowbandDUT)

.. function:: SetNoiseFigureRFImageCorrection(channel=1,RFImageCorrection)

.. function:: GetNoiseFigureRFImageCorrection(channel=1,RFImageCorrection)

.. function:: SetNoiseFigureCalibrationState(channel=1,calibration)

.. function:: GetNoiseFigureCalibrationState(channel=1,calibration)

.. function:: GetNoiseFigureCalibrationStateLabel(channel=1,bufferSize,label)

.. function:: DefineNoiseFigureCalibrationSettings(channel=1,port1,port2,externalAttenuator,sourceNoiseCalAttenuation,DUTMeasurementAttenuation)

.. function:: StartNoiseFigureCalibration(channel=1,calibrationStep)

.. function:: TerminateNoiseFigureCalibration(channel=1)

.. function:: CompleteNoiseFigureCalibration(channel=1)

.. function:: OverwriteNoiseFigureChannelSettings(channel=1,traceName)

.. function:: SetVirtualTransformBalancedState(channel=1,functionType,logicalPortNumber,state)

.. function:: GetVirtualTransformBalancedState(channel=1,functionType,logicalPortNumber,state)

.. function:: SetVirtualTransformBalancedPort(channel=1,functionType,logicalPortNumber,parameterType,parameterNumber,circuitModel,value)

.. function:: GetVirtualTransformBalancedPort(channel=1,functionType,logicalPortNumber,parameterType,parameterNumber,circuitModel,value)

.. function:: SetVirtualTransformBalancedCircuitModel(channel=1,functionType,logicalPortNumber,circuitModel)

.. function:: GetVirtualTransformBalancedCircuitModel(channel=1,functionType,logicalPortNumber,circuitModel)

.. function:: LoadBalancedPortCircuitModelData(channel=1,functionType,logicalPortNumber,fileName,parameter)

.. function:: LoadAndInterchangeBalancedPortCircuitModelData(channel=1,functionType,logicalPortNumber,fileName,parameter)

.. function:: SetVirtualTransformSingleEndedState(channel=1,functionType,physicalPortNumber,state)

.. function:: GetVirtualTransformSingleEndedState(channel=1,functionType,physicalPortNumber,state)

.. function:: SetVirtualTransformSingleEndedPort(channel=1,functionType,physicalPortNumber,parameterType,parameterNumber,circuitModel,value)

.. function:: GetVirtualTransformSingleEndedPort(channel=1,functionType,physicalPortNumber,parameterType,parameterNumber,circuitModel,value)

.. function:: SetVirtualTransformSingleEndedCircuitModel(channel=1,functionType,physicalPortNumber,circuitModel)

.. function:: GetVirtualTransformSingleEndedCircuitModel(channel=1,functionType,physicalPortNumber,circuitModel)

.. function:: LoadSingleEndedPortCircuitModelData(channel=1,functionType,physicalPortNumber,fileName)

.. function:: LoadAndInterchangeSingleEndedPortCircuitModelData(channel=1,functionType,physicalPortNumber,fileName)

.. function:: SetVirtualTransformGroundLoopState(channel=1,functionType,state)

.. function:: GetVirtualTransformGroundLoopState(channel=1,functionType,state)

.. function:: SetVirtualTransformGroundLoop(channel=1,functionType,parameterType,circuitModel,groundLoopValue)

.. function:: GetVirtualTransformGroundLoop(channel=1,functionType,parameterType,circuitModel,groundLoopValue)

.. function:: SetVirtualTransformGroundLoopCircuitModel(channel=1,functionType,circuitModel)

.. function:: GetVirtualTransformGroundLoopCircuitModel(channel=1,functionType,circuitModel)

.. function:: LoadGroundLoopCircuitModelData(channel=1,functionType,fileName)

.. function:: SetVirtualTransformPortPairState(channel=1,functionType,portPair,state)

.. function:: GetVirtualTransformPortPairState(channel=1,functionType,portPair,state)

.. function:: SetVirtualTransformPortPair(channel=1,functionType,portPair,parameterType,parameterNumber,circuitModel,value)

.. function:: GetVirtualTransformPortPair(channel=1,functionType,portPair,parameterType,parameterNumber,circuitModel,value)

.. function:: SetVirtualTransformPortPairCircuitModel(channel=1,functionType,portPair,circuitModel)

.. function:: GetVirtualTransformPortPairCircuitModel(channel=1,functionType,portPair,circuitModel)

.. function:: LoadPortPairCircuitModelData(channel=1,functionType,portPair,fileName,parameter,interchangePortNumbers)

.. function:: SetCoherentSignalState(channel=1,port,coherentSignal)

.. function:: GetCoherentSignalState(channel=1,port,coherentSignal)

.. function:: SetCoherentSignalAmplitude(channel=1,port,amplitude)

.. function:: GetCoherentSignalAmplitude(channel=1,port,amplitude)

.. function:: SetCoherentSignalPhase(channel=1,port,phase)

.. function:: GetCoherentSignalPhase(channel=1,port,phase)

.. function:: SetCoherentSignalReferencePort(channel=1,referencePort)

.. function:: GetCoherentSignalReferencePort(channel=1,referencePort)

.. function:: SetAlternateSweepMode(channel=1,alternateSweepMode)

.. function:: GetAlternateSweepMode(channel=1,alternateSweepMode)

.. function:: SetSpuriousAvoidance(channel=1,spuriousAvoidance)

.. function:: GetSpuriousAvoidance(channel=1,spuriousAvoidance)

.. function:: SetAutomaticLevelControlState(ALCState)

.. function:: GetAutomaticLevelControlState(ALCState)

.. function:: SetIndividualALCPortState(channel=1,port,state)

.. function:: GetIndividualALCPortState(channel=1,port,state)

.. function:: SetALCPortState(channel=1,port,state)

.. function:: GetALCPortState(channel=1,port,state)

.. function:: SetALCPortClamp(channel=1,port,clampState)

.. function:: GetALCPortClamp(channel=1,port,clampState)

.. function:: SetALCPortAUBWState(channel=1,port,state)

.. function:: GetALCPortAUBWState(channel=1,port,state)

.. function:: SetALCPortBandwidth(channel=1,port,bandwidth)

.. function:: GetALCPortBandwidth(channel=1,port,bandwidth)

.. function:: SetALCPortCoupling(channel=1,state)

.. function:: GetALCPortCoupling(channel=1,state)

.. function:: SetALCChannelState(channel=1,state)

.. function:: GetALCChannelState(channel=1,state)

.. function:: SetALCLowPhaseNoiseMode(channel=1,state)

.. function:: GetALCLowPhaseNoiseMode(channel=1,state)

.. function:: SetALCPortOffsetState(channel=1,port,state)

.. function:: GetALCPortOffsetState(channel=1,port,state)

.. function:: SetALCPortControlRange(channel=1,port,controlRange)

.. function:: GetALCPortControlRange(channel=1,port,controlRange)

.. function:: SetALCPortStartOffset(channel=1,port,startOffset)

.. function:: GetALCPortStartOffset(channel=1,port,startOffset)

.. function:: SetALCPortSettingTolerance(channel=1,port,settingTolerance)

.. function:: GetALCPortSettingTolerance(channel=1,port,settingTolerance)

.. function:: SetLowPhaseNoiseState(channel=1,lowPhaseNoiseState)

.. function:: GetLowPhaseNoiseState(channel=1,lowPhaseNoiseState)

.. function:: ConfigurePortPIController(channel=1,port,PIControllerMode,gain,integrationTime)

.. function:: ConfigureSAWMatchingNetwork(channel=1,apply,parallelL,serialC,differentialModeImpedance,commonModeImpedance)

.. function:: SetSAWState(channel=1,apply)

.. function:: GetSAWState(channel=1,apply)

.. function:: SetSAWParallelL(channel=1,parallelL)

.. function:: GetSAWParallelL(channel=1,parallelL)

.. function:: SetSAWSerialC(channel=1,serialC)

.. function:: GetSAWSerialC(channel=1,serialC)

.. function:: SetSAWSimulationType(channel=1,type)

.. function:: GetSAWSimulationType(channel=1,type)

.. function:: SetPIControllerMode(channel=1,port,PIControllerMode)

.. function:: GetPIControllerMode(channel=1,port,PIControllerMode)

.. function:: SetPIControllerGain(channel=1,port,gain)

.. function:: GetPIControllerGain(channel=1,port,gain)

.. function:: SetPIControllerIntegrationTime(channel=1,port,integrationTime)

.. function:: GetPIControllerIntegrationTime(channel=1,port,integrationTime)

.. function:: ChannelAdd(channel=1,channelName)

.. function:: ChannelAddTrace(window,window_Trace,channel=1,channelName,traceName)

.. function:: ChannelAddTraceDiagramArea(window,window_Trace,channel=1,channelName,traceName)

.. function:: ChannelDelete(channel=1)

.. function:: ChannelList(catalog,bufferSize)

.. function:: ChannelGetChannelName(channel=1,channelName)

.. function:: ChannelGetChannelNumber(channelName,channelNumber)

.. function:: ChannelSetActive(channel=1)

.. function:: ChannelGetActive(channel)

.. function:: ChannelRename(channel=1,channelName)

.. function:: SetConnector(channel=1,port,connector)

.. function:: GetConnector(channel=1,port,connector)

.. function:: SetSameConnectorTypeAtAllPorts(channel=1,sameConnectorAtAllPorts)

.. function:: GetSameConnectorTypeAtAllPorts(channel=1,sameConnectorAtAllPorts)

.. function:: SetSameConnectorGenderAtAllPorts(channel=1,sameGenderAtAllPorts)

.. function:: GetSameConnectorGenderAtAllPorts(channel=1,sameGenderAtAllPorts)

.. function:: SetUserConnector(channel=1,port,connector,connectorGender)

.. function:: GetUserConnector(channel=1,port,connector,connectorGender)

.. function:: SetSameSweepSetup(channel=1,sameSweepSetup)

.. function:: GetSameSweepSetup(channel=1,sameSweepSetup)

.. function:: SetSParameterDetector(channel=1,sParameterDetector)

.. function:: GetSParameterDetector(channel=1,sParameterDetector)

.. function:: SelectCalibrationType(channel=1,calibrationName,parameters,port1,port2,port3,port4)

.. function:: GetCalibrationType(channel=1,calibrationType,port1,port2,port3,port4)

.. function:: StartCalibration(channel=1,standard,port1,port2)

.. function:: StartCalibrationLine(channel=1,line,port1,port2)

.. function:: StartCalibrationWithOptions(channel=1,standard,port1,port2,dispersion,delayPhase,delayPhaseValue)

.. function:: SetCalibrationReferencePlaneShift(channel=1,referencePlaneShift)

.. function:: GetCalibrationReferencePlaneShift(channel=1,referencePlaneShift)

.. function:: SetCalibrationReferencePlaneShiftSpecific(channel=1,referencePlaneShift,calibrationName)

.. function:: GetCalibrationReferencePlaneShiftSpecific(channel=1,calibrationName,referencePlaneShift)

.. function:: QueryCalibrationReferencePlaneShift(channel=1,calibrationIndex,referencePlaneShift)

.. function:: SaveCalibrationData(channel=1)

.. function:: GenerateDefaultCalibrationData(channel=1)

.. function:: DeleteCalibrationData(channel=1,calibrationName)

.. function:: DeleteAllCalibrationData(channel=1)

.. function:: ReadCalibrationData(channel=1,errorTermParameters,port1,port2,calibrationData)

.. function:: WriteCalibrationData(channel=1,errorTermParameters,port1,port2,calibrationData)

.. function:: SetCorrectionState(channel=1,correctionState)

.. function:: GetCorrectionState(channel=1,correctionState)

.. function:: AcquireSourcePowerCalibration(channel=1,source,portNumber)

.. function:: InitiateSourcePowerCalibration(channel=1,portNumber,externalPowerMeter)

.. function:: SetDummySourcePowerCalibrationState(dummySourcePowerCalibration)

.. function:: GetDummySourcePowerCalibrationState(dummySourcePowerCalibration)

.. function:: SetSourcePowerCalibrationPortState(channel=1,portNumber,portState)

.. function:: GetSourcePowerCalibrationPortState(channel=1,portNumber,portState)

.. function:: SetSourcePowerCalibrationGeneratorState(channel=1,portNumber,generatorState)

.. function:: GetSourcePowerCalibrationGeneratorState(channel=1,portNumber,generatorState)

.. function:: SetVerificationSweepState(channel=1,verificationSweep)

.. function:: GetVerificationSweepState(channel=1,verificationSweep)

.. function:: QueryVerificationSweepResults(calibrationPassed,maxOffset)

.. function:: GeneratorPowerCalibrationHarmonic(channel=1)

.. function:: SetSourcePowerCalibrationState(calibrationState)

.. function:: GetSourcePowerCalibrationState(calibrationState)

.. function:: SetReferenceReceiverCalibrationState(calibrationState)

.. function:: GetReferenceReceiverCalibrationState(calibrationState)

.. function:: ModifySourcePowerCalibrationSettings(channel=1,portNumber,numberOfReadings,tolerance,otherSourcesState,portPowerOffset,offsetParameter,calibrationPowerOffset)

.. function:: SetNumberOfReadings(channel=1,numberOfReadings)

.. function:: GetNumberOfReadings(channel=1,numberOfReadings)

.. function:: SetTolerance(channel=1,tolerance)

.. function:: GetTolerance(channel=1,tolerance)

.. function:: SetOtherSourcesState(channel=1,otherSources)

.. function:: GetOtherSourcesState(channel=1,otherSources)

.. function:: SetPortPowerOffset(channel=1,portNumber,portPowerOffset,offsetParameter)

.. function:: GetPortPowerOffset(channel=1,portNumber,portPowerOffset,offsetParameter)

.. function:: SetCalibrationPowerOffset(channel=1,portNumber,calibrationPowerOffset)

.. function:: GetCalibrationPowerOffset(channel=1,portNumber,calibrationPowerOffset)

.. function:: SetCalibrationPowerGeneratorOffset(channel=1,portNumber,generatorNumber,calPowerGeneratorOffset)

.. function:: GetCalibrationPowerGeneratorOffset(channel=1,portNumber,generatorNumber,calPowerGeneratorOffset)

.. function:: SetReferenceReceiverAfterFirstCalSweep(fastSourcePowerCalibration)

.. function:: GetReferenceReceiverAfterFirstCalSweep(fastSourcePowerCalibration)

.. function:: SetPowerCalibrationMethodSource(methodSource)

.. function:: GetPowerCalibrationMethodSource(methodSource)

.. function:: SetCalibrationPowerMeterReadings(powerMeterReadings)

.. function:: GetCalibrationPowerMeterReadings(powerMeterReadings)

.. function:: ReadSourcePowerCorrectionData(channel=1,portNumber,calibratedWave,numberOfValues,powerCorrectionValues)

.. function:: WriteSourcePowerCorrectionData(channel=1,portNumber,calibratedWave,numberOfValues,powerCorrectionValues)

.. function:: GetSourcePowerCalibrationNumberOfWaves(channel=1,numberOfWaves)

.. function:: GetSourcePowerCalibrationParamaterWave(channel=1,calibrationIndex,bufferSize,calibratedWave)

.. function:: GetSourcePowerCalibrationParamaterStart(channel=1,calibrationIndex,start)

.. function:: GetSourcePowerCalibrationParamaterStop(channel=1,calibrationIndex,stop)

.. function:: GetSourcePowerCalibrationParamaterPoints(channel=1,calibrationIndex,points)

.. function:: GetSourcePowerCalibrationParamaterType(channel=1,calibrationIndex,type)

.. function:: GetSourcePowerCalibrationParamaterAttenuation(channel=1,calibrationIndex,attenuation)

.. function:: GetSourcePowerCalibrationParamaterCWPower(channel=1,calibrationIndex,CWPower)

.. function:: GetSourcePowerCalibrationParamaterCWFrequency(channel=1,calibrationIndex,CWFrequency)

.. function:: GetSourcePowerCalibrationParamaterTimestamp(channel=1,calibrationIndex,bufferSize,timestamp)

.. function:: SetSourcePowerCalibrationConvergenceFactor(convergenceFactor)

.. function:: GetSourcePowerCalibrationConvergenceFactor(convergenceFactor)

.. function:: SetSourcePowerCalibrationConverterState(channel=1,converter,calibrationConverter)

.. function:: GetSourcePowerCalibrationConverterState(channel=1,converter,calibrationConverter)

.. function:: AcquireReceiverPowerCalibration(channel=1,wave,portNumber,source,sourceNumber,referencePower)

.. function:: SetAWaveReceiverPowerCalibrationState(channel=1,portNumber,receiverPowerCalibration)

.. function:: GetAWaveReceiverPowerCalibrationState(channel=1,portNumber,receiverPowerCalibration)

.. function:: SetAWaveIdealPowerMeterMatchState(channel=1,portNumber,state)

.. function:: GetAWaveIdealPowerMeterMatchState(channel=1,portNumber,state)

.. function:: SetBWaveReceiverPowerCalibrationState(channel=1,portNumber,receiverPowerCalibration)

.. function:: GetBWaveReceiverPowerCalibrationState(channel=1,portNumber,receiverPowerCalibration)

.. function:: ReadReceiverPowerCorrectionData(channel=1,portNumber,calibratedWave,numberOfValues,powerCorrectionValues)

.. function:: WriteReceiverPowerCorrectionData(channel=1,portNumber,calibratedWave,numberOfValues,powerCorrectionValues)

.. function:: ReceiverPowerCalibrationHarmonic(channel=1)

.. function:: CorrectionManager(operationToBePerformed,fileName,loadParameter)

.. function:: SetPowerSensorPosition(powerSensorPosition)

.. function:: GetPowerSensorPosition(powerSensorPosition)

.. function:: SetTwoPortTransmissionCoefficientsEnabled(twoPortEnabled)

.. function:: GetTwoPortTransmissionCoefficientsEnabled(twoPortEnabled)

.. function:: GetLossListNumberOfValues(numberOfValues)

.. function:: SetPowerLossListCoefficient(operationToBePerformed,point,frequency,transmissionCoefficient)

.. function:: GetPowerLossListCoefficient(point,frequency,transmissionCoefficient)

.. function:: DeleteAllPowerLossListPoints()

.. function:: DeletePowerLossListSinglePoint(point)

.. function:: SetPowerLossListTrace(traceName)

.. function:: SetSourcePowerCorrectionState(channel=1,portNumber,sourcePowerCorrectionState)

.. function:: GetSourcePowerCorrectionState(channel=1,portNumber,sourcePowerCorrectionState)

.. function:: SetReceiverPowerCorrectionState(channel=1,portNumber,receiverPowerCorrectionState)

.. function:: GetReceiverPowerCorrectionState(channel=1,portNumber,receiverPowerCorrectionState)

.. function:: CalibrationManager(channel=1,operationToBePerformed,fileName)

.. function:: CalibrationAuto(channel=1,calibrationKitName,analyzerPort1,analyzerPort2,analyzerPort3,analyzerPort4,calUnitPort1,calUnitPort2,calUnitPort3,calUnitPort4)

.. function:: CalibrationAutoSimplified(channel=1,calibrationKitName,analyzerPort1,analyzerPort2,analyzerPort3,analyzerPort4)

.. function:: CalibrationAutoType(channel=1,parameters,calibrationKitName,analyzerPort1,analyzerPort2,analyzerPort3,analyzerPort4,calUnitPort1,calUnitPort2,calUnitPort3,calUnitPort4)

.. function:: CalibrationAutoTypeSimplified(channel=1,parameters,calibrationKitName,analyzerPort1,analyzerPort2,analyzerPort3,analyzerPort4)

.. function:: CalibrationRetainPortGroups(retainPortGroups)

.. function:: GetCalibrationConnection(channel=1,analyzerPort1,analyzerPort2,analyzerPort3,analyzerPort4)

.. function:: CalibrationAutoEx(channel=1,calibrationKitName,analyzerPort1,analyzerPort2,analyzerPort3,analyzerPort4,calUnitPort1,calUnitPort2,calUnitPort3,calUnitPort4,timeout)

.. function:: CalibrationAutoAssignmentType(channel=1,parameters,calibrationKitName)

.. function:: CalibrationAutoAssignmentDefinition(channel=1,assignment,analyzerPort1,analyzerPort2,analyzerPort3,analyzerPort4,calUnitPort1,calUnitPort2,calUnitPort3,calUnitPort4)

.. function:: GetCalibrationAutoAssingnmentDefinition(channel=1,assignment,analyzerPort1,analyzerPort2,analyzerPort3,analyzerPort4,calUnitPort1,calUnitPort2,calUnitPort3,calUnitPort4)

.. function:: InitiateCalibrationAutoAssignment(channel=1,assignment)

.. function:: CalibrationAutoAssignmentSave(channel=1)

.. function:: CalibrationAutoAssingnmentDeleteAll(channel=1)

.. function:: SetCalibrationDataCurrentState(channel=1,keepMeasData)

.. function:: GetCalibrationDataCurrentState(channel=1,keepMeasData)

.. function:: SetCalibrationDataDefaultState(channel=1,keepMeasData)

.. function:: GetCalibrationDataDefaultState(channel=1,keepMeasData)

.. function:: ExpCharDataTouchstoneFile(fileName)

.. function:: ExportUserCharacterizationDataTouchstoneFile(directoryName,fileName)

.. function:: SetCalibrationConnector(channel=1,connectorName,propagationMode,connectorType,relativePermittivity,impedance)

.. function:: GetCalibrationConnector(channel=1,connectorName,propagationMode,connectorType,relativePermittivity,impedance)

.. function:: CalibrationConnectorCatalog(catalog,bufferSize)

.. function:: DeleteCalibrationConnector(channel=1,connectorName)

.. function:: GetCalibrationDate(channel=1,bufferSize,calibrationDate)

.. function:: GetCalibrationState(channel=1,calibrationState)

.. function:: GetCalibrationLabel(channel=1,bufferSize,label)

.. function:: GetCalibrationDataParameters(channel=1,frequencyStart,frequencyStop,numberOfPoints,internalSignalSourcePower,sweepType)

.. function:: GetCalibrationsNumber(channel=1,numberOfCalibrations)

.. function:: GetCalibrationDataParametersMoreCalibrations(channel=1,calibration,frequencyStart,frequencyStop,numberOfPoints,internalSignalSourcePower,sweepType)

.. function:: GetCalibrationDataBandwidth(channel=1,calibration,bandwidth)

.. function:: GetCalibrationDataPointDelay(channel=1,calibration,pointDelay)

.. function:: GetCalibrationDataReceiverAttenuation(channel=1,calibration,arraySize,calibrationPort,attenuation,returnedValues)

.. function:: GetCalibrationDataType(channel=1,calibration,calibrationType)

.. function:: GetCalibrationDataPorts(channel=1,calibration,arraySize,calibrationPorts,returnedValues)

.. function:: GetCalibrationDataThroughs(channel=1,calibration,bufferSize,throughs)

.. function:: GetCalibrationDataTimestamp(channel=1,calibration,bufferSize,timestamp)

.. function:: SetActiveCalibrationUnit(calibrationUnit)

.. function:: GetActiveCalibrationUnit(bufferSize,calibrationUnit)

.. function:: SetAutomaticPowerReductionState(automaticPowerReduction)

.. function:: GetAutomaticPowerReductionState(automaticPowerReduction)

.. function:: GetAllCalibrationUnits(bufferSize,calibrationUnit)

.. function:: ConfigureCalibrationUnitStandard(standard,port1,port2)

.. function:: SetFactoryCalibrationState(channel=1,factoryCalibration)

.. function:: GetFactoryCalibrationState(channel=1,factoryCalibration)

.. function:: SetEnhancedWaveCorrection(channel=1,errorCorrection)

.. function:: GetEnhancedWaveCorrection(channel=1,errorCorrection)

.. function:: SetLoadMatchingCorrection(channel=1,loadMatchingCorrection)

.. function:: GetLoadMatchingCorrection(channel=1,loadMatchingCorrection)

.. function:: SetCalibrationCorrectionBaseFrequencyState(channel=1,state)

.. function:: GetCalibrationCorrectionBaseFrequencyState(channel=1,state)

.. function:: SetCalibrationKit(connector,calibrationKitName)

.. function:: GetCalibrationKit(connector,bufferSize,calibrationKitName)

.. function:: SetCalibrationKitWithLabel(connector,calibrationKitName,calibrationKitLabel)

.. function:: SetCalibrationKitUserConnectorType(connector,calibrationKitName)

.. function:: GetCalibrationKitUserConnectorType(connector,bufferSize,calibrationKitName)

.. function:: SetCalibrationKitUserConnectorTypeWithLabel(connectionType,calibrationKitName,calibrationKitLabel)

.. function:: GetCalibrationKitUserConnectorTypeWithLabel(connectionType,bufferSize,calibrationKitData)

.. function:: CalibrationKitCatalog(connectorName,catalog,bufferSize)

.. function:: CalibrationKitCatalogWithLabel(connectorName,bufferSize,catalog)

.. function:: ImportZVRCalibrationKit(calibrationKitName)

.. function:: ConfigureCalibrationStandard(connector,standard,kit,serialNumber,minFreqHz,maxFreqHz,lengthmm,loss,c0L0,c1L1,c2L2,c3L3,approximation)

.. function:: ConfigureCalibrationStandardWithLabel(standard,connector,calkitName,calkitLabel,standardLabel,minFreqHz,maxFreqHz,electricalLength,loss,z0,capacitances,residualInductances,approximation)

.. function:: CalibrationStandardsCatalog(calibrationKitName,catalog,bufferSize)

.. function:: CalibrationStandardsCatalogWithLabel(calibrationKitName,calibrationKitLabel,bufferSize,catalog)

.. function:: SaveCalibrationKit(fileName)

.. function:: SaveCalibrationKitPorts(fileName,parameters,arraySize,VNAPorts,calUnitPorts)

.. function:: LoadCalibrationKit(connectorName,calibrationKitName,standard,calibrationKitLabel,fileName,portNumber1,portNumber2)

.. function:: SetCalibrationKitLabel(calibrationKitName,label)

.. function:: RenameCalibrationKit(calibrationKitName,label,newLabel)

.. function:: GetCalibrationKitLabel(calibrationKitName,label)

.. function:: DeleteCalibrationKit(calibrationKitName)

.. function:: DeleteCalibrationKitWithLabel(calibrationKitName,calibrationKitLabel)

.. function:: ImportKit(fileName)

.. function:: AdditionalDirectoryCalibrationKit(directory)

.. function:: ExportKit(kitName,fileName)

.. function:: ExportKitWithLabel(kitName,kitLabel,fileName)

.. function:: ResetOffsets(channel=1)

.. function:: QueryResetOffsets(channel=1,offsets)

.. function:: SetElectricalLength(channel=1,port,electricalLength)

.. function:: GetElectricalLength(channel=1,port,electricalLength)

.. function:: ConfigureMechanicalLength(channel=1,port,mechanicalLength,permittivity)

.. function:: SetMechanicalLength(channel=1,port,mechanicalLength)

.. function:: GetMechanicalLength(channel=1,port,mechanicalLength)

.. function:: SetPermittivity(channel=1,port,permittivity)

.. function:: GetPermittivity(channel=1,port,permittivity)

.. function:: ConfigureLoss(channel=1,port,lossAtDC,lossAtFrequency,lossReferenceFrequency)

.. function:: SetLossAtDC(channel=1,port,lossAtDC)

.. function:: GetLossAtDC(channel=1,port,lossAtDC)

.. function:: SetLossAtFrequency(channel=1,port,lossAtFrequency)

.. function:: GetLossAtFrequency(channel=1,port,lossAtFrequency)

.. function:: SetLossReferenceFrequency(channel=1,port,lossReferenceFrequency)

.. function:: GetLossReferenceFrequency(channel=1,port,lossReferenceFrequency)

.. function:: SetDelay(channel=1,port,delay)

.. function:: GetDelay(channel=1,port,delay)

.. function:: QueryDirectFixtureCompensation(channel=1,port,directFixtureCompensation)

.. function:: AutoLength(channel=1,port)

.. function:: AutoLengthAndLoss(channel=1,port)

.. function:: AcquireFixtureCompensationSweep(channel=1,standardType,arraySize,ports)

.. function:: StartFixtureCompensationSweep(channel=1)

.. function:: SaveFixtureCompensationData(channel=1)

.. function:: SetFixtureCompensationAutoLengthAndLossCalculation(autoLengthAndLoss)

.. function:: GetFixtureCompensationAutoLengthAndLossCalculation(autoLengthAndLoss)

.. function:: SetFixtureCompensationDirectCompensation(directCompensation)

.. function:: GetFixtureCompensationDirectCompensation(directCompensation)

.. function:: DiagramAreaAdd(window)

.. function:: DiagramAreaDelete(window)

.. function:: DiagramAreaMaximize(window,diagramArea)

.. function:: DiagramAreaTitle(window,title,titleString)

.. function:: DiagramAreaName(window,areaName)

.. function:: DiagramAreaCatalog(window,catalog,bufferSize)

.. function:: TraceDiagramAreaCatalog(window,catalog,bufferSize)

.. function:: SetColorScheme(colorScheme)

.. function:: GetColorScheme(colorScheme)

.. function:: SaveColorScheme(fileName)

.. function:: LoadColorScheme(fileName)

.. function:: SetFrequencyInfo(frequencyInfo)

.. function:: GetFrequencyInfo(frequencyInfo)

.. function:: SetFontSize(fontSize)

.. function:: GetFontSize(fontSize)

.. function:: SetChannelInfo(channelInfo)

.. function:: GetChannelInfo(channelInfo)

.. function:: SetMarkerColorState(sameColor)

.. function:: GetMarkerColorState(sameColor)

.. function:: SetRGBColor(element,red,green,blue,traceStyle,traceWidth)

.. function:: GetRGBColor(element,red,green,blue,traceStyle,traceWidth)

.. function:: SetTraceColorState(traceColor)

.. function:: GetTraceColorState(traceColor)

.. function:: TraceSetRGBColor(traceName,red,green,blue,traceStyle,traceWidth)

.. function:: TraceGetRGBColor(traceName,red,green,blue,traceStyle,traceWidth)

.. function:: SetPowerPortLimitState(channel=1,port,limitState)

.. function:: GetPowerPortLimitState(channel=1,port,limitState)

.. function:: SetPowerPortLimitValue(channel=1,port,limitValue)

.. function:: GetPowerPortLimitValue(channel=1,port,limitValue)

.. function:: SetPowerPortLimitDirectGeneratorAndReceiverState(channel=1,port,DRGAccessState)

.. function:: GetPowerPortLimitDirectGeneratorAndReceiverState(channel=1,port,DRGAccessState)

.. function:: SetPresets(presetScope)

.. function:: GetPresets(presetScope)

.. function:: SetPresetSettingsState(state)

.. function:: GetPresetSettingsState(state)

.. function:: SetUserDefinedPresetState(userDefinedPreset)

.. function:: GetUserDefinedPresetState(userDefinedPreset)

.. function:: SetUserDefinedPresetFile(userDefinedPresetFile)

.. function:: GetUserDefinedPresetFile(bufferSize,userDefinedPresetFile)

.. function:: SetDisplayUpdate(displayUpdate)

.. function:: GetDisplayUpdate(displayUpdate)

.. function:: ImmediateSettingsUpdate()

.. function:: QueryFrequencyRange(minimumFrequency,maximumFrequency)

.. function:: SystemKeylock(lockout)

.. function:: SetRemoteLanguage(language)

.. function:: GetRemoteLanguage(language)

.. function:: ConfigureExternalGenerator(generatorNumber,generatorName,generatorType,interfaceType,interfaceAddress,fastSweepMode,_10MHzReferenceFrequency)

.. function:: QueryExternalGenerator(generatorNumber,generatorName,generatorType,interfaceType,interfaceAddress,fastSweepMode,_10MHzReferenceFrequency)

.. function:: QueryExternalGeneratorCount(generatorCount)

.. function:: QueryExternalGeneratorNumbers(arraySize,generatorNumbers)

.. function:: DeleteExternalGenerator()

.. function:: ConfigureExternalPowerMeter(powerMeterNumber,powerMeterName,powerMeterType,interfaceType,interfaceAddress)

.. function:: QueryExternalPowerMeter(powerMeterNumber,powerMeterName,powerMeterType,interfaceType,interfaceAddress)

.. function:: QueryExternalPowerMeterCount(powerMeterCount)

.. function:: QueryExternalPowerMeterNumbers(bufferSize,powerMeterNumber)

.. function:: AutoZeroingExternalPowerMeter(powerMeterNumber)

.. function:: SetAutoConfigNRPZxx(powerMeterNumber,autoConfig)

.. function:: GetAutoConfigNRPZxx(powerMeterNumber,autoConfig)

.. function:: DeleteExternalPowerMeter()

.. function:: SetAlarmSoundsState(alarmSounds)

.. function:: GetAlarmSoundsState(alarmSounds)

.. function:: SetRestartBehavior(restartBehavior)

.. function:: GetRestartBehavior(restartBehavior)

.. function:: SetStatusSoundsState(statusSounds)

.. function:: GetStatusSoundsState(statusSounds)

.. function:: SetDataTransfer(dataTransfer)

.. function:: GetDataTransfer(dataTransfer)

.. function:: SetErrorDisplayState(errorDisplay)

.. function:: GetErrorDisplayState(errorDisplay)

.. function:: SetFrequencyConversionType(converterType)

.. function:: GetFrequencyConversionType(bufferSize,converterType)

.. function:: SetFrequencyConversionSource(conversionSource)

.. function:: GetFrequencyConversionSource(conversionSource)

.. function:: SetFastMultiportCorrection(fastMultiportCorrection)

.. function:: GetFastMultiportCorrection(fastMultiportCorrection)

.. function:: SetPowerCoeficients(port,coeficient)

.. function:: GetPowerCoeficients(port,coeficients)

.. function:: SetPowerCoeficientsDefault(defaultCoeficients)

.. function:: GetPowerCoeficientsDefault(defaultCoeficients)

.. function:: QueryExtensionUnitDeviceID(bufferSize,deviceID)

.. function:: QueryExtensionUnitHardwareOptions(bufferSize,options)

.. function:: SetNWAApplicationPriority(priority)

.. function:: GetNWAApplicationPriority(priority)

.. function:: SystemShutdown()

.. function:: GenerateSystemReport(fileName)

.. function:: SetCalculationOfBandfilterCenterFrequency(channel=1,marker,centerFrequencyCalculation)

.. function:: GetCalculationOfBandfilterCenterFrequency(channel=1,marker,centerFrequencyCalculation)

.. function:: SetRFOffBehavior(RFOffBehavior)

.. function:: GetRFOffBehavior(RFOffBehavior)

.. function:: SetRemoteDisplayTitle(title)

.. function:: GetRemoteDisplayTitle(bufferSize,title)

.. function:: SetAnalyzerHostname(hostName)

.. function:: GetAnalyzerHostname(bufferSize,hostName)

.. function:: SetSoftKeyLabel(keyNumber,label)

.. function:: GetPressedSoftKey(keyNumber,bufferSize,label)

.. function:: SetOutputPortBits(outputPort,portBits)

.. function:: GetOutputPortBits(outputPort,portBits)

.. function:: SetChannelBits(channelBits)

.. function:: GetChannelBits(channelBits)

.. function:: SetUIDirection(port,direction)

.. function:: GetUIDirection(port,direction)

.. function:: SetUIData(port,data)

.. function:: GetUIData(port,data)

.. function:: SetUISignalPin20(pin20)

.. function:: GetUISignalPin20(pin20)

.. function:: SetUISignalPin21(pin21)

.. function:: GetUISignalPin21(pin21)

.. function:: SetUIPortBinaryData(port,data)

.. function:: GetUIPortBinaryData(port,data)

.. function:: SetUIPortNextState(port,nextState)

.. function:: GetUIPortNextState(port,nextState)

.. function:: RestoreUIDefaultStates()

.. function:: setStatusRegister(registerOperation,questionableRegister,enable,PTransition,NTransition)

.. function:: getStatusRegister(statusRegistersQuery,registerValue)

.. function:: setTimeOut(timeout)

.. function:: getTimeOut(timeout)

.. function:: errorCheckState(stateChecking)

.. function:: setCheckOption(optionChecking)

.. function:: setCheckRange(rangeChecking)

.. function:: writeInstrData(writeBuffer)

.. function:: readInstrData(numberBytesToRead,readBuffer,numBytesRead)

.. function:: reset()

.. function:: self_test(selfTestResult,selfTestMessage)

.. function:: error_query(errorCode,errorMessage)

.. function:: error_message(statusCode,message)

.. function:: revision_query(instrumentDriverRevision,firmwareRevision)

.. function:: close()

