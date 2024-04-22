#!/usr/bin/env python
import rospy
import sys

sys.path.append(r"/home/agilex01/agilex_ws/src/demo_behaviors/demo_flexbe_states/src/demo_flexbe_states/modules")
import simple_speek, mic, simple_voice
from flexbe_core import EventState, Logger
import random
import re


class chating(EventState):
    '''
    chat state

    <= weather  return weather
    <= joke     tell a joke
    <= time     return time
    <=finish    stop chating
    <=other     unclear repeat again

    '''

    def __init__(self):
        # Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
        super(chating, self).__init__(outcomes=['weather', 'joke', 'time', 'finish', 'other'])
        self.positivelist = ["是的", "对", "嗯", "好的", "yes", "alright"]
        self.negativelist = ["不是", "不对", "错", "不可以", "no", "refused"]

    # Store state parameter for later use.
    # self._target_time = rospy.Duration(target_time)

    # The constructor is called when building the state machine, not when actually starting the behavior.
    # Thus, we cannot save the starting time now and will do so later.
    # self._start_time = None

    def execute(self, userdata):
        joke_list = ['你好，我是chatbot，有什么可以帮你的？', '你可以问问我时间，天气或者让我讲个笑话哦！']
        TEXT = joke_list[random.randint(0, len(joke_list) - 1)]
        simple_speek.speek(TEXT)
        mic.Monitor_MIC(70, "t")
        simple_voice.recogize_voice()
        with open('result.txt', 'rb') as speech_file:
            TEXT = speech_file.read()
            s = TEXT.find('['.encode())
            e = TEXT.find(']'.encode())
            TEXT = TEXT[s + 1:e].decode()  #TEXT is the input words
        print(TEXT)
        if re.match(r'(.*)(天气|weather)\??', TEXT):
            return 'weather'
        if re.match(r'(.*)(时间|日期|今天几号|time)\??', TEXT):
            return 'time'
        if re.match(r'(.*)(笑话|joke)\??', TEXT):
            return 'joke'
        if re.match(r'(.*)(再见|拜拜|停止|stop)\??', TEXT):
            return 'finish'
        else:
            return 'other'

    # This method is called periodically while the state is active.
    # Main purpose is to check state conditions and trigger a corresponding outcome.
    # If no outcome is returned, the state will stay active.

    # if rospy.Time.now() - self._start_time > self._target_time:
    #   return 'continue' # One of the outcomes declared above.

    def on_enter(self, userdata):
        # This method is called when the state becomes active, i.e. a transition from another state to this one is taken.
        # It is primarily used to start actions which are associated with this state.

        # The following code is just for illustrating how the behavior logger works.
        # Text logged by the behavior logger is sent to the operator and displayed in the GUI.

        # time_to_wait = (self._target_time - (rospy.Time.now() - self._start_time)).to_sec()

        # if time_to_wait > 0:
        # Logger.loginfo('Need to wait for %.1f seconds.' % time_to_wait)
        pass

    def on_exit(self, userdata):
        # This method is called when an outcome is returned and another state gets active.
        # It can be used to stop possibly running processes started by on_enter.

        pass  # Nothing to do in this example.

    def on_start(self):
        # This method is called when the behavior is started.
        # If possible, it is generally better to initialize used resources in the constructor
        # because if anything failed, the behavior would not even be started.

        # In this example, we use this event to set the correct start time.
        # self._start_time = rospy.Time.now()
        pass

    def on_stop(self):
        # This method is called whenever the behavior stops execution, also if it is cancelled.
        # Use this event to clean up things like claimed resources.

        pass  # Nothing to do in this example.
