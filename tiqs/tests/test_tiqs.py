"""
Translational Invariant Quantum Solver.
"""
import numpy as np
from numpy.testing import (assert_, run_module_suite, assert_raises,
                           assert_array_equal, assert_array_almost_equal,
                           assert_almost_equal, assert_equal)

import qutip as qt
from tiqs import *

class TestTiqs:
    """
    A test class for the Translational Invariant Quantum Solver.
    """

    def test_traslation(self):
        """
        Test the `traslation` function.
        """
        
        test_basis = traslation("010")
        true_basis = qt.fock(n_cutoff,n_excitation)        
        assert_equal(test_basis, true_basis)

if __name__ == "__main__":
    run_module_suite()