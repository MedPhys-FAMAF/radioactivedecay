"""
The radionuclide module defines the ``Radionuclide`` class.

The examples shown assume the ``radioactivedecay`` package has been imported as:

.. highlight:: python
.. code-block:: python

    >>> import radioactivedecay as rd

"""

from typing import List
from radioactivedecay.decaydata import DecayData, DEFAULTDATA
from radioactivedecay.utils import parse_radionuclide, time_unit_conv


class Radionuclide:
    """
    Radionuclide instances are used to fetch decay data on one radionuclide.

    Parameters
    ----------
    radionuclide : str
        Radionuclide string.
    data : DecayData, optional
        Decay dataset (default is the ICRP 107 dataset).

    Attributes
    ----------
    radionuclide : str
        Radionuclide string.
    decay_constant : numpy.float64
        Decay constant of the radionuclide (s\\ :sup:`-1`).
    prog_bf_mode : dict
        Dictionary containing direct progeny as keys, and a list containing the branching fraction
        and the decay mode for that progeny as values.
    data : DecayData
        Decay dataset.

    Examples
    --------
    >>> rd.Radionuclide('H-3')
    Radionuclide: H-3, Decay dataset: icrp107

    """

    def __init__(self, radionuclide: str, data: DecayData = DEFAULTDATA) -> None:
        self.radionuclide = parse_radionuclide(
            radionuclide, data.radionuclides, data.dataset
        )
        self.decay_constant = data.decay_consts[
            data.radionuclide_dict[self.radionuclide]
        ]
        self.prog_bf_mode = data.prog_bfs_modes[
            data.radionuclide_dict[self.radionuclide]
        ]
        self.data = data

    def half_life(self, units: str = "s") -> float:
        """
        Returns half-life of the radionuclide in chosen units.

        Parameters
        ----------
        units : str, optional
            Units for half-life (default is seconds). Options are 'ns', 'us', 'ms', 's', 'm', 'h',
            'd', 'y', 'ky', 'My', 'Gy', 'Ty', 'Py', and some of the common spelling variations of
            these time units.

        Returns
        -------
        float
            Radionuclide half-life.

        Examples
        --------
        >>> Rn222 = rd.Radionuclide('Rn-222')
        >>> Rn222.half_life('d')
        3.8235

        """

        conv = (
            1.0
            if units == "s"
            else time_unit_conv(
                1.0, units_from="s", units_to=units, year_conv=self.data.year_conv
            )
        )
        return conv * self.data.ln2 / self.decay_constant

    def progeny(self) -> List[str]:
        """
        Returns the direct progeny of the radionuclide.

        Returns
        -------
        list
            List of the direct progeny of the radionuclide, ordered by decreasing branching
            fraction.

        Examples
        --------
        >>> K40 = rd.Radionuclide('K-40')
        >>> K40.progeny()
        ['Ca-40', 'Ar-40']

        """

        return list(self.prog_bf_mode.keys())

    def branching_fractions(self) -> List[float]:
        """
        Returns the branching fractions for the direct progeny of the radionuclide.

        Returns
        -------
        list
            List of branching fractions.

        Examples
        --------
        >>> K40 = rd.Radionuclide('K-40')
        >>> K40.branching_fractions()
        [0.8914, 0.1086]

        """

        return [bf_mode[0] for bf_mode in list(self.prog_bf_mode.values())]

    def decay_modes(self) -> List[str]:
        """
        Returns the decay modes for the radionuclide, as defined in the decay dataset. Note: the
        decay mode does not necessarily list all the different radiation particles emitted by the
        decay.

        Returns
        -------
        list
            List of decay modes.

        Examples
        --------
        >>> K40 = rd.Radionuclide('K-40')
        >>> K40.decay_modes()
        ['\u03b2-', '\u03b2+ & EC']

        """

        return [bf_mode[1] for bf_mode in list(self.prog_bf_mode.values())]

    def __repr__(self) -> str:
        return (
            "Radionuclide: "
            + str(self.radionuclide)
            + ", Decay dataset: "
            + self.data.dataset
        )