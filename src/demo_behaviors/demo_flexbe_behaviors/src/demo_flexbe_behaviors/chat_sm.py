#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from demo_flexbe_states.chating import chating
from demo_flexbe_states.check_ques import check_ques
from demo_flexbe_states.get_time import get_time
from demo_flexbe_states.get_weather import get_weather
from demo_flexbe_states.tell_jokes import tell_jokes
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Mar 02 2023
@author: gqc
'''
class chatSM(Behavior):
	'''
	a simple chat behavior containing get weather, time,telling a joke.
	'''


	def __init__(self):
		super(chatSM, self).__init__()
		self.name = 'chat'

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
			# x:116 y:60
			OperatableStateMachine.add('chat',
										chating(),
										transitions={'weather': 'weather', 'joke': 'joke', 'time': 'time', 'finish': 'finished', 'other': 'chat'},
										autonomy={'weather': Autonomy.Off, 'joke': Autonomy.Off, 'time': Autonomy.Off, 'finish': Autonomy.Off, 'other': Autonomy.Off})

			# x:682 y:352
			OperatableStateMachine.add('check_ques',
										check_ques(),
										transitions={'yes': 'chat', 'no': 'finished', 'unclear': 'check_ques'},
										autonomy={'yes': Autonomy.Off, 'no': Autonomy.Off, 'unclear': Autonomy.Off})

			# x:434 y:240
			OperatableStateMachine.add('joke',
										tell_jokes(),
										transitions={'done': 'check_ques'},
										autonomy={'done': Autonomy.Off})

			# x:424 y:43
			OperatableStateMachine.add('time',
										get_time(),
										transitions={'done': 'check_ques'},
										autonomy={'done': Autonomy.Off})

			# x:415 y:148
			OperatableStateMachine.add('weather',
										get_weather(),
										transitions={'done': 'check_ques'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
