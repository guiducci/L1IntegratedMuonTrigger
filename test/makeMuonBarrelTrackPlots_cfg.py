import FWCore.ParameterSet.Config as cms

process = cms.Process('PLOTMAKER')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.TFileService = cms.Service(
    "TFileService",
    fileName=cms.string('L1ITMuonBarrelTrackPlots.root')
    )

process.L1ITMuPlotter = cms.EDAnalyzer(
    'L1ITMuonBarrelTrackPlots',
    MBTracksCollection = cms.InputTag('MBTracksProducer'),
    MBLTCollection = cms.InputTag('MBLTProducer'),
    L1ITDTChambPhContainer = cms.InputTag('L1ITMuonBarrelPrimitiveProducer', '', 'L1ITMU')
)

infile = 'file:L1ITMBLT.root'

process.source = cms.Source(
    'PoolSource',
    fileNames = cms.untracked.vstring(infile)
    )

process.L1ITMUSequence = cms.Sequence(process.L1ITMuPlotter)

process.L1ITMUPath = cms.Path(process.L1ITMUSequence)

process.schedule = cms.Schedule(process.L1ITMUPath)
