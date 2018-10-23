#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Audio Fmcw 2
# Generated: Tue Oct 23 03:24:00 2018
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
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
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
import math
import numpy
import wx


class AUDIO_FMCW_2(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Audio Fmcw 2")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48e3
        self.mul_constant = mul_constant = 50
        self.f = f = 50
        self.delay_ms = delay_ms = 350

        ##################################################
        # Blocks
        ##################################################
        self._mul_constant_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.mul_constant,
        	callback=self.set_mul_constant,
        	label='mul_constant',
        	converter=forms.float_converter(),
        )
        self.Add(self._mul_constant_text_box)
        self._f_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.f,
        	callback=self.set_f,
        	label='f',
        	converter=forms.float_converter(),
        )
        self.Add(self._f_text_box)
        _delay_ms_sizer = wx.BoxSizer(wx.VERTICAL)
        self._delay_ms_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_delay_ms_sizer,
        	value=self.delay_ms,
        	callback=self.set_delay_ms,
        	label='delay_ms',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._delay_ms_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_delay_ms_sizer,
        	value=self.delay_ms,
        	callback=self.set_delay_ms,
        	minimum=0,
        	maximum=1000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_delay_ms_sizer)
        self.wxgui_waterfallsink2_1 = waterfallsink2.waterfall_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	dynamic_range=21,
        	ref_level=10,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=2014,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Waterfall Plot',
        )
        self.Add(self.wxgui_waterfallsink2_1.win)
        self.hilbert_fc_0 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.fft_vxx_0 = fft.fft_vcc(1024, True, (window.blackmanharris(1024)), True, 2)
        self.chirp_gen_0 = chirp_gen(
            bf_hz=0,
            chirp_rate_hz=f,
            chirp_width_hz=48e3,
            samp_rate=48e3,
        )
        self.blocks_vector_to_stream_2 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 1024)
        self.blocks_vector_to_stream_1 = blocks.vector_to_stream(gr.sizeof_float*1, 512)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*1, 512)
        self.blocks_vector_source_x_1 = blocks.vector_source_c((0, 0, 0), True, 1, [])
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 512)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (1024, 1))
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(1, 512, 0)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_ff(mul_constant)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*512, 1)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 512, 1024, 512)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, delay_ms)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(512)
        self.audio_source_0 = audio.source(48000, '', True)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_const_source_x_1 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.audio_source_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_vector_to_stream_1, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_vector_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_vector_to_stream_1, 0), (self.wxgui_waterfallsink2_1, 0))
        self.connect((self.blocks_vector_to_stream_2, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.chirp_gen_0, 1), (self.blocks_delay_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_2, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_waterfallsink2_1.set_sample_rate(self.samp_rate)

    def get_mul_constant(self):
        return self.mul_constant

    def set_mul_constant(self, mul_constant):
        self.mul_constant = mul_constant
        self._mul_constant_text_box.set_value(self.mul_constant)
        self.blocks_multiply_const_xx_0.set_k(self.mul_constant)

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self._f_text_box.set_value(self.f)
        self.chirp_gen_0.set_chirp_rate_hz(self.f)

    def get_delay_ms(self):
        return self.delay_ms

    def set_delay_ms(self, delay_ms):
        self.delay_ms = delay_ms
        self._delay_ms_slider.set_value(self.delay_ms)
        self._delay_ms_text_box.set_value(self.delay_ms)
        self.blocks_delay_0.set_dly(self.delay_ms)


def main(top_block_cls=AUDIO_FMCW_2, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
