#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from demo_flexbe_states.asking_for_help import asking_for_help
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Mar 01 2023
@author: gqc
'''
class pass_door1SM(Behavior):
	'''
	behavior of passing doors
	'''


	def __init__(self):
		super(pass_door1SM, self).__init__()
		self.name = 'pass_door1'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:334 y:181
			OperatableStateMachine.add('a',
										asking_for_help(),
										transitions={'accepted': 'failed', 'refused': 'a', 'unclear': 'finished'},
										autonomy={'accepted': Autonomy.Off, 'refused': Autonomy.Off, 'unclear': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
