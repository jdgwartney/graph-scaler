#!/usr/bin/env python3
import math
import logging

logger = logging.getLogger(__name__)

class ScaleAxis(object):
    pass


def scale_axis(data):
    upper = max(data)
    lower = min(data)
    print("upper: {0}, lower: {1}".format(lower, upper))
    range = upper - lower
    print("range: {0}".format(range))
    tick_count = 8

    unrounded_tick_size = range/(tick_count - 1)
    print("tick_count: {0}, unrounded_tick_size: {1}".format(tick_count, unrounded_tick_size))

    x = math.ceil(math.log10(unrounded_tick_size) - 1);
    # x1 = math.ceil(math.log(tickRange))
    pow10x = math.pow(10, x);
    print("x: {0}, pow10x: {1}".format(x, pow10x))

    rounded_tick_range = math.ceil(unrounded_tick_size / pow10x) * pow10x

    rounded_tick_range = math.ceil(unrounded_tick_size/pow10x) * pow10x
    print("rounded_tick_range: {0}".format(rounded_tick_range))

    new_lower = rounded_tick_range * round(lower/rounded_tick_range)
    new_upper = rounded_tick_range * round((1+upper)/rounded_tick_range)
    print("new_lower: {0}, new_upper: {1}".format(new_lower, new_upper))
    return (new_lower, new_upper)


def step_size(range, target_steps):
    # calculate an initial guess at step size
    temp_step = range/target_steps
    logger.debug("temp_step: {0}".format(temp_stemp))

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

    return mag_msd*mag_pow;

if __name__ == '__main__':
    data = [15, 234, 140, 65, 90]
    lower, upper = scale_axis(data)
    size = step_size(upper-lower, 5)
    print("lower: {0}, upper: {1}, size: {2}".format(lower, upper, size))

