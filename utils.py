import numpy as np


def SawtoothExact(t, SamplingInterval):
    return t - np.floor(t / SamplingInterval) * SamplingInterval + SamplingInterval


def SawtoothApprox(t, SamplingInterval, Order):
    Value = 1 / 2
    for i in range(Order):
        Value = Value - 1 / (np.pi * (i + 1)) * np.sin(
            2 * (i + 1) * np.pi * t / SamplingInterval
        )
    return Value * SamplingInterval + SamplingInterval
