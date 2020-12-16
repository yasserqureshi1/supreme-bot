import os
from subprocess import *


def create_instance(number_of_instances):
    for i in range(number_of_instances):
        p = Popen([r'SupremeBot.py', "ArcView"], shell=True, stdin=PIPE, stdout=PIPE)
        output = p.communicate()