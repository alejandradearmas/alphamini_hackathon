from src.functions.controller_factory import controllers

# Build in dance, actions and emoticons list: https://docs.ubtrobot.com/alphamini/python-sdk-en/additional.html

async def do_interaction(ip_address_robot: str):
    do_introduction_demo_interaction()

async def do_introduction_demo_interaction():
    await controllers.expression.play_expression("codemao1")
    await controllers.action.play_action("random_short4")
    await controllers.speech.speak("Hi, my name is Mini.")
    await controllers.speech.speak("What is your name?")
    await controllers.speech.speak("What a nice name. You also look nice today.")
    await controllers.speech.speak("Let's get to know each other. I will show you what I can do.")
    await controllers.speech.speak("As you have noticed, I can talk to you. I can also show you how I feel with my eyes.")
    await controllers.speech.speak_with_expression("I can be happy.", expression_name="emo_007")
    await controllers.speech.speak("I can be happy.")
    await controllers.expression.play_expression(expression_name="emo_007")
    await controllers.speech.speak("I can be angry.")
    await controllers.expression.play_expression(expression_name="emo_013")
    await controllers.speech.speak("I can be shy.")
    await controllers.expression.play_expression(expression_name="codemao2")
    await controllers.speech.speak("I also have some moves.")
    await controllers.speech.speak_with_action("Look, I can, for example, wiggle my hips.", action_name="action_015")
    await controllers.speech.speak("And now the question is, how can I help you? That is what this conversation is about.")
    await controllers.action.play_action("random_short3")
