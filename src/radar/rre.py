import math

class RRE:
    """
    Class for Radar Range Equation
    """

    def __init__(self, area=None, height=None, width=None, efficiency=None, a_eff=None, freq=None, gain=None, smin=None, max_detection=None, rcs=None, range=None):
        """
        Initialize RRE Params
        """
        self.wl = None
        self.power = None

        # init height
        self.height = height
        self.width = width
        if area is None:
            if height is not None and width is not None:
                self.area = height*width
        else:
            self.area = area


        self.efficiency = efficiency
        self.a_eff = a_eff
        self.freq = freq
        self.gain = gain
        self.smin = smin
        self.max_detection = max_detection
        self.rcs = rcs
        self.range = range

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
        self.wl = c/freq

        gain = (4 * math.pi * self.a_eff) / self.wl**2
        # Convert to dB
        self.gain = math.log10(gain)

        return self.gain

    def ptp(self):
        """
        Calculate Peak transmit power

        :return: Peak transmit power (kw)
        """

        if self.rcs is None or self.gain is None or self.smin is None or self.wl is None or self.range is None:
            raise AttributeError('Peak transmit power requires radar cross section, gain, smin, wavelength and range.')

        # ((4pi)^3 * Smin * R^4) / (Gain^2 * wl^2 * rcs
        th = ((4*math.pi)**3) * self.smin * (self.range**4)
        bh = (self.gain**2) * (self.wl**2) * self.rcs
        self.power = th/bh

        return self.power

    def hor_beamwidth(self):
        """
        Calculate horizontal beam width

        :return: Horizontal beam width in degrees
        """

        if self.width is None or self.wl is None:
            raise AttributeError('Horizontal beam width requires antenna width and wavelength.')

        # Note 65 constant converts from radians to degrees
        hbw = 65 * (self.wl/self.width)
        return hbw









