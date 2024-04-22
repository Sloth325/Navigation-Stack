state:
    asking_for_help.py
        '''
        Asking people for help to open the door (of elevator)


        <= accepted   	 accepted
        <= refused   refused
        <= unclear   unclear

        '''

    ask_to_press_button.py
        '''
        Asking people to press the button of xth floor

        para:self._floor

        <= accepted   	 accepted
        <= refused   refused
        <= unclear   unclear

        '''

    chating.py
        '''
        simple chat state

        <= weather  return weather
        <= joke     tell a joke
        <= time     return time
        <=finish    stop chating
        <=other     unclear repeat again

        '''

    check_door_open.py
        '''
        Asking people whether door is open


        <= open   	 door is open
        <= close     door is closed

        '''

    check_ques.py
        '''
        Asking people whether they still have question


        <= open   	 no question
        <= close     more question
        <= unclear

        '''
    
    example_state.py
        '''
        Example for a state to demonstrate which functionality is available for state implementation.
        This example lets the behavior wait until the given target_time has passed since the behavior has been started.

        -- target_time 	float 	Time which needs to have passed since the behavior started.

        <= continue 			Given time has passed.
        <= failed 				Example for a failure outcome.

        '''

    get_time.py
        '''
        get time now

        <= done

        '''

    get_weather.py
        '''
        get weather of shanghai (choose city by code)

        <= done

        '''

    passing_door.py
        '''
        give warning voice when passing door

        <= done

        '''

    tell_jokes.py
        '''
        tell a joke randomly from the list

        <= done

        '''






behaviors:
    chat
        '''
        a simple chat behavior containing get weather, time,telling a joke.

        <= finfished

        '''

    pass_door
        '''
        behaviors of passing the door

        <= finished

        '''

    taking_elevator
        '''
        behaviors of taking the elevator

        behavior para:
            floor text

        <= finished

        '''