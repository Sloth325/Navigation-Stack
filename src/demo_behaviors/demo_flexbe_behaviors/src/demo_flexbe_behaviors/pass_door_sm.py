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
from demo_flexbe_states.check_door_open import check_door_open
from demo_flexbe_states.passing_door import passing_door
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Mar 01 2023
@author: gqc
'''
class pass_doorSM(Behavior):
	'''
	behavior of passing doors
	'''


	def __init__(self):
		super(pass_doorSM, self).__init__()
		self.name = 'pass_door'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:125 y:105
			OperatableStateMachine.add('asking_for_help',
										asking_for_help(),
										transitions={'accepted': 'check_door_open', 'refused': 'asking_for_help', 'unclear': 'asking_for_help'},
										autonomy={'accepted': Autonomy.Off, 'refused': Autonomy.Off, 'unclear': Autonomy.Off})

			# x:295 y:241
			OperatableStateMachine.add('check_door_open',
										check_door_open(),
										transitions={'open': 'passing_door', 'close': 'check_door_open'},
										autonomy={'open': Autonomy.Off, 'close': Autonomy.Off})

			# x:236 y:370
			OperatableStateMachine.add('passing_door',
										passing_door(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
