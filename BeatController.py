from ControllerInterface import *
from DJView import *

class BeatController:
	def __init__(self, ControllerInterface):
	self.model = BeatModelInterface
	self.view = DJView
   
	def BeatController(model):
		self.model = model
		self.view = DJView(model)
        self.view.createView()
        self.view.createControls()
		self.view.disableStopMenuItem()
		self.view.enableStartMenuItem()
		self.model.initialize()
	
  
	def start():
		model.on();
		self.view.disableStartMenuItem()
		self.view.enableStopMenuItem()

  
	def stop() :
		self.model.off()
		self.view.disableStopMenuItem()
		self.view.enableStartMenuItem()
    
	def increaseBPM():
        int bpm = self.model.getBPM()
        self.model.setBPM(bpm + 1)

    
	def decreaseBPM():
		int bpm
		bpm = self.model.getBPM()
        self.model.setBPM(bpm - 1)
  
 	def setBPM(int bpm):
		self.model.setBPM(bpm)

