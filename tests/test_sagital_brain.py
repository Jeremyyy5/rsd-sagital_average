import numpy as np
import subprocess


def test_average():
    # Creates input file
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    # The expeted result is all zeros, except the last one, it should be 1
    expected = np.zeros(20)
    expected[-1] = 1

    np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

    # run python program
    subprocess.run(["python", "sagital_brain.py"])

    # Check result
    result = np.loadtxt("brain_average.csv",  delimiter=',')
    np.testing.assert_array_equal(result, expected)
