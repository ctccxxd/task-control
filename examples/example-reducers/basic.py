from random import random
from time import sleep

import logging
log = logging.getLogger(__name__)

from taskmanager import StepResultCode, step_retry_delay

SUCCESS = StepResultCode.SUCCESS
FAILURE = StepResultCode.FAILURE
RETRY = StepResultCode.RETRY
ABORT = StepResultCode.ABORT

@step_retry_delay(3, 1)
def s1(t_data):
    log.info('s1 running...')
    log.info(t_data)
    sleep(1)
    r = random()
    if r < 0.9:
        return StepResultCode.SUCCESS, {'s1': 1}, 's1 general success'
    else:
        return StepResultCode.ABORT, {'s1': 1}, 's1 fail, abort'


@step_retry_delay()
def s2(t_data): # cleanup step of s1
    log.info('s2 running...')
    log.info(t_data)
    sleep(1)
    r = random()
    if r < 0.9:
        return StepResultCode.SUCCESS, {'s2': 2}, 's2 general success'
    else:
        raise Exception('Woo! s2 raised!')


@step_retry_delay(3, 1)
def s3(t_data):
    log.info('s3 running...')
    log.info(t_data)
    sleep(1)
    r = random()
    if r < 0.3:
        return StepResultCode.SUCCESS, {'s3': 1}, 's3 general success'
    else:
        raise Exception('Woo! s3 raised!')


@step_retry_delay()
def s4(t_data): # cleanup step of s3
    log.info('s4 running...')
    log.info(t_data)
    sleep(1)
    r = random()
    if r < 0.9:
        return StepResultCode.SUCCESS, {'s4': 4}, 's4 general success'
    else:
        raise Exception('Woo! s4 raised!')


@step_retry_delay()
def s5(t_data):
    log.info('s5 running...')
    log.info(t_data)
    sleep(1)
    r = random()
    if r < 0.2:
        return StepResultCode.SUCCESS, {'s5': 5}, 's5 general success'
    else:
        raise Exception('Woo! s5 raised!')

