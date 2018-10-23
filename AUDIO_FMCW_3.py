#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Audio Fmcw 3
# Generated: Tue Oct 23 03:24:03 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from chirp_gen import chirp_gen  # grc-generated hier_block
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class AUDIO_FMCW_3(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Audio Fmcw 3")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.f = f = 0.1
        self.delay = delay = 0

        ##################################################
        # Blocks
        ##################################################
        self._f_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.f,
        	callback=self.set_f,
        	label='f',
        	converter=forms.float_converter(),
        )
        self.Add(self._f_text_box)
        self._delay_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.delay,
        	callback=self.set_delay,
        	label='delay',
        	converter=forms.float_converter(),
        )
        self.Add(self._delay_text_box)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Waterfall Plot',
        	size=(1980,1080),
        )
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.hilbert_fc_0 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.chirp_gen_0 = chirp_gen(
            bf_hz=0,
            chirp_rate_hz=f,
            chirp_width_hz=48e3,
            samp_rate=48e3,
        )
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, delay)
        self.blocks_complex_to_real_1 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self.audio_sink_0_0 = audio.sink(samp_rate, 'hw:1,0', True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_complex_to_real_1, 0), (self.blocks_delay_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.audio_sink_0_0, 0))
        self.connect((self.blocks_delay_0, 1), (self.audio_sink_0_0, 1))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.wxgui_waterfallsink2_0, 0))
        self.connect((self.chirp_gen_0, 1), (self.blocks_complex_to_real_0, 0))
        self.connect((self.chirp_gen_0, 2), (self.blocks_complex_to_real_1, 0))
        self.connect((self.chirp_gen_0, 1), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self._f_text_box.set_value(self.f)
        self.chirp_gen_0.set_chirp_rate_hz(self.f)

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self._delay_text_box.set_value(self.delay)
        self.blocks_delay_0.set_dly(self.delay)


def main(top_block_cls=AUDIO_FMCW_3, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
