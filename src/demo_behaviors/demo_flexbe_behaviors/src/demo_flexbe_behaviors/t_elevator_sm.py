#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from demo_flexbe_states.ask_to_press_button import asking_to_press_button
from demo_flexbe_states.asking_for_help import asking_for_help
from demo_flexbe_states.passing_door import passing_door
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Mar 02 2023
@author: gqc
'''
class t_elevatorSM(Behavior):
	'''
	case:in front of the elevator,ask somebody to help taking the elevator.
	'''


	def __init__(self):
		super(taking_elevatorSM, self).__init__()
		self.name = 'taking_elevator'

		# parameters of this behavior
		self.add_parameter('floor', '')

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:448 y:425, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.input_value = None

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:151 y:95
			OperatableStateMachine.add('ask_for_help',
										asking_for_help(),
										transitions={'accepted': 'get_in_elevator', 'refused': 'failed', 'unclear': 'ask_for_help'},
										autonomy={'accepted': Autonomy.Off, 'refused': Autonomy.Off, 'unclear': Autonomy.Off})

			# x:546 y:203
			OperatableStateMachine.add('get_in_elevator',
										passing_door(),
										transitions={'done': 'ask to press button'},
										autonomy={'done': Autonomy.Off})

			# x:717 y:448
			OperatableStateMachine.add('get_out_elevator',
										passing_door(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:776 y:304
			OperatableStateMachine.add('ask to press button',
										asking_to_press_button(floor=self.floor),
										transitions={'accepted': 'get_out_elevator', 'refused': 'finished', 'unclear': 'ask to press button'},
										autonomy={'accepted': Autonomy.Off, 'refused': Autonomy.Off, 'unclear': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
