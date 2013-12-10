#!/usr/bin/env python

import os
import Queue
import sys
from adapters import console, flowbot
from util.exceptionwithcontext import ExceptionWithContext
from util import logger
import logging

sys.path += ['plugins']  # so 'import hook' works without duplication
sys.path += ['lib']
os.chdir(sys.path[0] or '.')  # do stuff relative to the install directory


class Bot(object):
    pass


bot = Bot()

print 'Loading plugins'

# bootstrap the reloader
eval(compile(open(os.path.join('core', 'reload.py'), 'U').read(),
    os.path.join('core', 'reload.py'), 'exec'))

reload(init=True)

config()
if not hasattr(bot, 'config'):
    logger.log("no config found for bot", logging.ERROR)
    exit()

logger.log("Connecting to IRC")

bot.conns = {}
bot.logins = {}
try:
    for name, conf in bot.config['connections'].iteritems():
        #bot.conns[name] = flowbot.BotOutput(conf)
        bot.conns[name] = console.ConsoleOutput(conf)
    for name, conf in bot.config['logins'].iteritems():
        bot.logins[name] = conf
except Exception, e:
    logger.log("malformed config file %s" % e, logging.ERROR)
    sys.exit()

bot.persist_dir = os.path.abspath('persist')
if not os.path.exists(bot.persist_dir):
    os.mkdir(bot.persist_dir)

logger.log("Running main loop")

while True:
    reload()  # these functions only do things
    config()  # if changes have occured

    for conn in bot.conns.itervalues():
        try:
            conn.run(bot)
            #out = conn.out.get_nowait()
            #main(conn, out)
        except Queue.Empty:
            pass
        except:
            raise ExceptionWithContext("bot died before his time")
