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
from demo_flexbe_states.check_door_open import check_door_open
from demo_flexbe_states.example_state import ExampleState
from demo_flexbe_states.passing_door import passing_door
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Mar 02 2023
@author: gqc
'''
class taking_elevatorSM(Behavior):
	'''
	case:in front of the elevator,ask somebody to help taking the elevator.
	'''


	def __init__(self):
		super(taking_elevatorSM, self).__init__()
		self.name = 'taking_elevator'

		# parameters of this behavior
		self.add_parameter('floor', 0)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:222 y:441
		_state_machine = OperatableStateMachine(outcomes=['finished'])
		_state_machine.userdata.input_value = None

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:89 y:92
			OperatableStateMachine.add('ask_to_open_door',
										asking_for_help(),
										transitions={'accepted': 'check_door_open', 'refused': 'wait_for_another_person', 'unclear': 'ask_to_open_door'},
										autonomy={'accepted': Autonomy.Off, 'refused': Autonomy.Off, 'unclear': Autonomy.Off})

			# x:699 y:90
			OperatableStateMachine.add('ask_to_press_button',
										asking_to_press_button(floor=self.floor),
										transitions={'accepted': 'check_floor', 'refused': 'ask_to_press_button', 'unclear': 'ask_to_press_button'},
										autonomy={'accepted': Autonomy.Off, 'refused': Autonomy.Off, 'unclear': Autonomy.Off})

			# x:345 y:215
			OperatableStateMachine.add('check_door_open',
										check_door_open(),
										transitions={'open': 'pass_door', 'close': 'ask_to_open_door'},
										autonomy={'open': Autonomy.Off, 'close': Autonomy.Off})

			# x:415 y:355
			OperatableStateMachine.add('check_door_open_out',
										check_door_open(),
										transitions={'open': 'getout', 'close': 'check_door_open_out'},
										autonomy={'open': Autonomy.Off, 'close': Autonomy.Off})

			# x:730 y:241
			OperatableStateMachine.add('check_floor',
										ExampleState(target_time=5),
										transitions={'continue': 'check_door_open_out', 'failed': 'check_floor'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:235 y:332
			OperatableStateMachine.add('getout',
										passing_door(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:533 y:143
			OperatableStateMachine.add('pass_door',
										passing_door(),
										transitions={'done': 'ask_to_press_button'},
										autonomy={'done': Autonomy.Off})

			# x:288 y:19
			OperatableStateMachine.add('wait_for_another_person',
										ExampleState(target_time=5),
										transitions={'continue': 'ask_to_open_door', 'failed': 'wait_for_another_person'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
