#!/usr/bin/env python3
import math
import logging

logger = logging.getLogger(__name__)


class ScaleAxis(object):

    def __init__(self):
        pass


def scale_axis(data):
    up = max(data)
    lo = min(data)
    logger.debug("upper: {0}, lower: {1}".format(lo, up))
    r = up - lo
    logger.debug("range: {0}".format(r))
    tick_count = 8

    unrounded_tick_size = r/(tick_count - 1)
    logger.debug("tick_count: {0}, unrounded_tick_size: {1}".format(tick_count, unrounded_tick_size))

    x = math.ceil(math.log10(unrounded_tick_size) - 1)
    pow10x = math.pow(10, x)
    logger.debug("x: {0}, pow10x: {1}".format(x, pow10x))

    rounded_tick_range = math.ceil(unrounded_tick_size / pow10x) * pow10x

    rounded_tick_range = math.ceil(unrounded_tick_size/pow10x) * pow10x
    logger.debug("rounded_tick_range: {0}".format(rounded_tick_range))

    new_lower = rounded_tick_range * round(lo/rounded_tick_range)
    new_upper = rounded_tick_range * round((1+up)/rounded_tick_range)
    logger.debug("new_lower: {0}, new_upper: {1}".format(new_lower, new_upper))
    return (new_lower, new_upper)


def step_size(r, target_steps):
    # calculate an initial guess at step size
    temp_step = r/target_steps
    logger.debug("temp_step: {0}".format(temp_step))

    # get the magnitude of the step size
    mag = float(math.floor(math.log(temp_step)))
    mag_pow = float(math.pow(10, mag))

    # calculate most significant digit of the new step size
    mag_msd = int((temp_step/mag_pow + 0.5))

    # promote the MSD to either 1, 2, or 5
    if mag_msd > 5.0:
        mag_msd = 10.0
    elif mag_msd > 2.0:
        mag_msd = 5.0
    elif mag_msd > 1.0:
        mag_msd = 2.0;

    return mag_msd * mag_pow;

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    data = [15, 234, 140, 65, 90]
    lo, up = scale_axis(data)
    size = step_size(up-lo, 5)
    print("lower: {0}, upper: {1}, size: {2}".format(lo, up, size))

