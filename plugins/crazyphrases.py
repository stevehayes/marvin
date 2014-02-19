from util import hook, textutils
import random

list_name = "game:crazyphrases:users"
phrases = (
    "I can't wait until Monday",
    "That's very true",
    "I can't believe I just thought that",
    "I'm never going to finish this",
    "This is crazy",
    "Fair enough I assume",
    "I'm hungry and thirsty",
    "I'm so lost",
    "I should have this done by tomorrow",
    "This conversation is over",
    "This is why we can't have nice things",
    "I love Marvin",
    "It smells like a fart over here",
    "Marvin just laughed at me",
    "I have nothing to say",
    "I need to merge"
)
user_phrases = {}
user_points = {}
@hook.regex(r'play crazy phrases', run_always=True)
def crazy_phrases(bot_input, bot_output):
    phrase = random.choice(phrases)
    #storage.set_hash_value(list_name, bot_input.nick, phrase)
    bot_output.say("you're in {0}".format(bot_input.nick))
    user_phrases[bot_input.nick] = textutils.sanitize_message(phrase)
    user = bot_output.get_user_by_name(bot_input.nick)
    bot_output.private_message(str(user["id"]), "Your phrase is: %s" % phrase)


@hook.regex(r'crazy phrases users', run_always=True)
def crazy_phrases_users(bot_input, bot_output):
    users = user_phrases.keys()
    bot_output.say("Current Users Playing: ")
    bot_output.say(", ".join(users))


@hook.regex(r'crazy phrases score', run_always=True)
def crazy_phrases_users(bot_input, bot_output):
    messages = []
    for user, points in user_points:
        messages.append(user + " has " + points)
    bot_output.say("Current Score: ")
    bot_output.say(", ".join(messages))


@hook.regex(r'.*', run_always=True)
def check_phrases(bot_input, bot_output):
    for user, phrase in user_phrases.iteritems():
        if phrase == textutils.sanitize_message(bot_input.message):
            if user == bot_input.nick:
                user_points[user] = (user_points[user] or 0) + 1
                user = bot_output.get_user_by_name(bot_input.nick)
                bot_output.private_message(str(user["id"]), "You got a point.  Current score for you is: " + user_points[user])
            bot_output.say("Woot!  Phrase that pays!")
            bot_output.say(user + " had the phrase: " + phrase)
            bot_output.say("Good job " + bot_input.nick)
