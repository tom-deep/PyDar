import math

class RRE:
    """
    Class for Radar Range Equation
    """

    def __init__(self, area=None, efficiency=None, a_eff=None, freq=None, gain=None, smin=None, max_detection=None, rcs=None):
        """
        Initialize RRE Params
        """

        self.area = area
        self.efficiency = efficiency
        self.a_eff = a_eff
        self.freq = freq
        self.gain = gain
        self.smin = smin
        self.max_detection = max_detection
        self.rcs = rcs

    def antenna_effective_aperture(self):
        """
        Calculate antenna effective aperture of an antenna. Set the object's antenna effective aperture

        :return: Antenna effective aperture (m squared)
        """

        if self.area is None or self.efficiency is None:
            raise AttributeError('antenna effective aperture requires antenna area and efficiency.')

        self.a_eff = self.area * self.efficiency
        return self.a_eff

    def antenna_gain(self):
        """
        Calculate antenna gain

        :return: Antenna gain (dB)
        """


        if self.a_eff is None or self.freq is None:
            raise AttributeError("antenna gain requires antenna effective aperture and frequency.")

        # Calculate wavelength... speed of light/frequency (Hz)
        c = 3e8
        freq = self.freq * (10**6)
        wl = c/freq

        gain = (4 * math.pi * self.a_eff) / wl**2
        # Convert to dB
        self.gain = math.log10(gain)

        return self.gain

    def ptp(self):
        """
        Calculate Peak transmit power

        :return: Peak transmit power (kw)
        """
        return 0







