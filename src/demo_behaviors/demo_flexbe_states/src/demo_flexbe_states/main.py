# coding=utf-8
import sys

sys.path.append(r"/home/agilex01/agilex_ws/src/demo_behaviors/demo_flexbe_states/src/demo_flexbe_states/modules")

import simple_voice
import simple_speek
import answerq
import mic

if __name__ == "__main__":
    state = ["standby", "requesting", "checking"]
    curr_state = "standby"
    action = ""
    place = ""
    while True:
        mic.Monitor_MIC(70, "t")
        simple_voice.recogize_voice()
        ans, curr_state, action, place = answerq.getans(action, place, curr_state)
        simple_speek.speek(ans)
