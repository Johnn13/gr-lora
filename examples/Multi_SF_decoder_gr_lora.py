#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Multi_SF_decoder_gr_lora
# Author: szu-iot
# GNU Radio version: v3.8.5.0-6-g57bd109d

from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.filter import pfb
import lora


class Multi_SF_decoder_gr_lora(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Multi_SF_decoder_gr_lora")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000e3
        self.payload_len = payload_len = 8
        self.header = header = True
        self.freq = freq = 446000000
        self.crc = crc = True
        self.cr = cr = 3
        self.bw = bw = 250000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(('', "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(100, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_bandwidth(5e6, 0)
        self.uhd_usrp_source_0.set_samp_rate(5e6)
        # No synchronization enforced.
        self.pfb_arb_resampler_xxx_0_0_0_1_0 = pfb.arb_resampler_ccf(
            2*250e3/5e5,
            taps=None,
            flt_size=32)
        self.pfb_arb_resampler_xxx_0_0_0_1_0.declare_sample_delay(0)
        self.pfb_arb_resampler_xxx_0_0_0_1 = pfb.arb_resampler_ccf(
            2*250e3/5e5,
            taps=None,
            flt_size=32)
        self.pfb_arb_resampler_xxx_0_0_0_1.declare_sample_delay(0)
        self.pfb_arb_resampler_xxx_0_0_0_0_0_0 = pfb.arb_resampler_ccf(
            2*250e3/5e5,
            taps=None,
            flt_size=32)
        self.pfb_arb_resampler_xxx_0_0_0_0_0_0.declare_sample_delay(0)
        self.pfb_arb_resampler_xxx_0_0_0_0_0 = pfb.arb_resampler_ccf(
            2*250e3/5e5,
            taps=None,
            flt_size=32)
        self.pfb_arb_resampler_xxx_0_0_0_0_0.declare_sample_delay(0)
        self.pfb_arb_resampler_xxx_0_0_0_0 = pfb.arb_resampler_ccf(
            2*250e3/5e5,
            taps=None,
            flt_size=32)
        self.pfb_arb_resampler_xxx_0_0_0_0.declare_sample_delay(0)
        self.pfb_arb_resampler_xxx_0_0_0 = pfb.arb_resampler_ccf(
            2*250e3/5e5,
            taps=None,
            flt_size=4)
        self.pfb_arb_resampler_xxx_0_0_0.declare_sample_delay(0)
        self.pfb_arb_resampler_xxx_0_0 = pfb.arb_resampler_ccf(
            2*250e3/5e5,
            taps=None,
            flt_size=4)
        self.pfb_arb_resampler_xxx_0_0.declare_sample_delay(0)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
            2*250e3/5e5,
            taps=None,
            flt_size=4)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        self.lora_demod_0_1_1_1_0 = lora.demod(7, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_1_1 = lora.demod(7, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_1_0_0_0 = lora.demod(7, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_1_0_0 = lora.demod(7, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_1_0 = lora.demod(7, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_1 = lora.demod(7, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_1_1_0 = lora.demod(8, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_1_1 = lora.demod(8, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_1_0_0_0 = lora.demod(8, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_1_0_0 = lora.demod(8, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_1_0 = lora.demod(8, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_1 = lora.demod(8, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_2_1_0 = lora.demod(11, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_2_1 = lora.demod(11, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_2_0_0_0 = lora.demod(11, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_2_0_0 = lora.demod(11, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_2_0 = lora.demod(11, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_2 = lora.demod(11, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_1_0_1_0 = lora.demod(12, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_1_0_1 = lora.demod(12, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_1_0_0_0_0 = lora.demod(12, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_1_0_0_0 = lora.demod(12, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_1_0_0 = lora.demod(12, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_1_0 = lora.demod(12, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_1 = lora.demod(12, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_1_1_0 = lora.demod(10, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_1_1 = lora.demod(10, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_1_0_0_0 = lora.demod(10, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_1_0_0 = lora.demod(10, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_1_0 = lora.demod(10, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_1 = lora.demod(10, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_0_0_1_0 = lora.demod(9, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_0_0_1 = lora.demod(9, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_0_0_0_0_0 = lora.demod(9, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_0_0_0_0 = lora.demod(9, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_0_0_0 = lora.demod(9, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_0_0 = lora.demod(9, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0_0 = lora.demod(9, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0_0 = lora.demod(10, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0_0 = lora.demod(11, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1_0 = lora.demod(8, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_1 = lora.demod(7, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_0_0_0_0_0 = lora.demod(12, header, payload_len, cr, crc, 1, True, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_0_0_0_0 = lora.demod(11, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_0_0_0 = lora.demod(10, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_0_0 = lora.demod(9, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0_0 = lora.demod(8, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_demod_0 = lora.demod(7, header, payload_len, cr, crc, 1, False, 25.0, 16, 0, 4, 2)
        self.lora_decode_0_1_1_1_0 = lora.decode(7, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_1_1 = lora.decode(7, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_1_0_0_0 = lora.decode(7, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_1_0_0 = lora.decode(7, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_1_0 = lora.decode(7, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_1 = lora.decode(7, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_1_1_0 = lora.decode(8, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_1_1 = lora.decode(8, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_1_0_0_0 = lora.decode(8, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_1_0_0 = lora.decode(8, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_1_0 = lora.decode(8, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_1 = lora.decode(8, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_1_1_0 = lora.decode(9, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_1_1 = lora.decode(9, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_1_0_0_0 = lora.decode(9, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_1_0_0 = lora.decode(9, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_1_0 = lora.decode(9, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_1 = lora.decode(9, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_1_1_0 = lora.decode(10, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_1_1 = lora.decode(10, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_1_0_0_0 = lora.decode(10, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_1_0_0 = lora.decode(10, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_1_0 = lora.decode(10, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_1 = lora.decode(10, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_1_1_0 = lora.decode(11, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_1_1 = lora.decode(11, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_1_0_0_0 = lora.decode(11, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_1_0_0 = lora.decode(11, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_1_0 = lora.decode(11, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_1 = lora.decode(11, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_0_0_1_0 = lora.decode(12, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_0_0_1 = lora.decode(12, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_0_0_0_0_0 = lora.decode(12, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_0_0_0_0 = lora.decode(12, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_0_0_0 = lora.decode(12, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_0_0 = lora.decode(12, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0_0 = lora.decode(12, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0_0 = lora.decode(11, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0_0 = lora.decode(10, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0_0 = lora.decode(9, header, payload_len, cr, crc, False)
        self.lora_decode_0_1_0 = lora.decode(8, header, payload_len, cr, crc, False)
        self.lora_decode_0_1 = lora.decode(7, header, payload_len, cr, crc, False)
        self.lora_decode_0_0_0_0_0_0 = lora.decode(12, header, payload_len, cr, crc, True)
        self.lora_decode_0_0_0_0_0 = lora.decode(11, header, payload_len, cr, crc, False)
        self.lora_decode_0_0_0_0 = lora.decode(10, header, payload_len, cr, crc, False)
        self.lora_decode_0_0_0 = lora.decode(9, header, payload_len, cr, crc, False)
        self.lora_decode_0_0 = lora.decode(8, header, payload_len, cr, crc, False)
        self.lora_decode_0 = lora.decode(7, header, payload_len, cr, crc, False)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_1 = filter.freq_xlating_fir_filter_ccf(10, firdes.low_pass(1,5e6,5e6/(2*10), 30e3), 2400e3, 5e6)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_1.set_min_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_1.set_max_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0_0 = filter.freq_xlating_fir_filter_ccf(10, firdes.low_pass(1,5e6,5e6/(2*10), 30e3), 2100e3, 5e6)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0_0.set_min_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0_0.set_max_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0 = filter.freq_xlating_fir_filter_ccf(10, firdes.low_pass(1,5e6,5e6/(2*10), 30e3), 1800E3, 5e6)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0.set_min_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0.set_max_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0 = filter.freq_xlating_fir_filter_ccf(10, firdes.low_pass(1,5e6,5e6/(2*10), 30e3), 1500e3, 5e6)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0.set_min_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0.set_max_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0_0 = filter.freq_xlating_fir_filter_ccf(10, firdes.low_pass(1,5e6,5e6/(2*10), 30e3), 1200e3, 5e6)
        self.freq_xlating_fir_filter_xxx_0_0_0_0.set_min_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0_0.set_max_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0 = filter.freq_xlating_fir_filter_ccf(10, firdes.low_pass(1,5e6,5e6/(2*10)*1.2, 30e3), 900e3, 5e6)
        self.freq_xlating_fir_filter_xxx_0_0_0.set_min_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0_0.set_max_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccf(10, firdes.low_pass(1,5e6,5e6/(2*10)*1.2, 30e3), 300e3, 5e6)
        self.freq_xlating_fir_filter_xxx_0_0.set_min_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0_0.set_max_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccf(10, firdes.low_pass(1,5e6,5e6/(2*10)*1.2, 30e3), 0, 5e6)
        self.freq_xlating_fir_filter_xxx_0.set_min_output_buffer(100000)
        self.freq_xlating_fir_filter_xxx_0.set_max_output_buffer(100000)
        self.blocks_message_debug_0_0_0_1_0 = blocks.message_debug()
        self.blocks_message_debug_0_0_0_1 = blocks.message_debug()
        self.blocks_message_debug_0_0_0_0_0_0 = blocks.message_debug()
        self.blocks_message_debug_0_0_0_0_0 = blocks.message_debug()
        self.blocks_message_debug_0_0_0_0 = blocks.message_debug()
        self.blocks_message_debug_0_0_0 = blocks.message_debug()
        self.blocks_message_debug_0_0 = blocks.message_debug()
        self.blocks_message_debug_0 = blocks.message_debug()


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lora_decode_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0, 'header'), (self.lora_demod_0, 'header'))
        self.msg_connect((self.lora_decode_0_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_0, 'header'), (self.lora_demod_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_0_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_0_0, 'header'), (self.lora_demod_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_0_0_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_0_0_0, 'header'), (self.lora_demod_0_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_0_0_0_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_0_0_0_0, 'header'), (self.lora_demod_0_0_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_0_0_0_0_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_0_0_0_0_0, 'header'), (self.lora_demod_0_0_0_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1, 'out'), (self.blocks_message_debug_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1, 'header'), (self.lora_demod_0_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_0, 'out'), (self.blocks_message_debug_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0, 'header'), (self.lora_demod_0_1_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0, 'out'), (self.blocks_message_debug_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0, 'header'), (self.lora_demod_0_1_0_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0, 'out'), (self.blocks_message_debug_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0, 'header'), (self.lora_demod_0_1_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0, 'out'), (self.blocks_message_debug_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0, 'header'), (self.lora_demod_0_1_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0, 'out'), (self.blocks_message_debug_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0, 'header'), (self.lora_demod_0_1_0_0_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0, 'out'), (self.blocks_message_debug_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0, 'header'), (self.lora_demod_0_1_0_0_1_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0_0, 'out'), (self.blocks_message_debug_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0_0, 'header'), (self.lora_demod_0_1_0_0_1_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0_0_0, 'header'), (self.lora_demod_0_1_0_0_1_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0_0_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0_0_0_0, 'header'), (self.lora_demod_0_1_0_0_1_0_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0_1, 'out'), (self.blocks_message_debug_0_0_0_1, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0_1, 'header'), (self.lora_demod_0_1_0_0_1_0_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0_1_0, 'out'), (self.blocks_message_debug_0_0_0_1_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_0_0_1_0, 'header'), (self.lora_demod_0_1_0_0_1_0_1_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1, 'out'), (self.blocks_message_debug_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1, 'header'), (self.lora_demod_0_1_0_0_2, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1_0, 'out'), (self.blocks_message_debug_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1_0, 'header'), (self.lora_demod_0_1_0_0_2_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1_0_0, 'header'), (self.lora_demod_0_1_0_0_2_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1_0_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1_0_0_0, 'header'), (self.lora_demod_0_1_0_0_2_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1_1, 'out'), (self.blocks_message_debug_0_0_0_1, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1_1, 'header'), (self.lora_demod_0_1_0_0_2_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1_1_0, 'out'), (self.blocks_message_debug_0_0_0_1_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_0_1_1_0, 'header'), (self.lora_demod_0_1_0_0_2_1_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1, 'out'), (self.blocks_message_debug_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1, 'header'), (self.lora_demod_0_1_0_0_0_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1_0, 'out'), (self.blocks_message_debug_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1_0, 'header'), (self.lora_demod_0_1_0_0_0_1_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1_0_0, 'header'), (self.lora_demod_0_1_0_0_0_1_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1_0_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1_0_0_0, 'header'), (self.lora_demod_0_1_0_0_0_1_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1_1, 'out'), (self.blocks_message_debug_0_0_0_1, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1_1, 'header'), (self.lora_demod_0_1_0_0_0_1_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1_1_0, 'out'), (self.blocks_message_debug_0_0_0_1_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_0_1_1_0, 'header'), (self.lora_demod_0_1_0_0_0_1_1_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_1, 'out'), (self.blocks_message_debug_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_1, 'header'), (self.lora_demod_0_1_0_0_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_1_0, 'out'), (self.blocks_message_debug_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_1_0, 'header'), (self.lora_demod_0_1_0_0_0_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_1_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_1_0_0, 'header'), (self.lora_demod_0_1_0_0_0_0_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_1_0_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_1_0_0_0, 'header'), (self.lora_demod_0_1_0_0_0_0_0_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_1_1, 'out'), (self.blocks_message_debug_0_0_0_1, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_1_1, 'header'), (self.lora_demod_0_1_0_0_0_0_0_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_0_1_1_0, 'out'), (self.blocks_message_debug_0_0_0_1_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_0_1_1_0, 'header'), (self.lora_demod_0_1_0_0_0_0_0_1_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_1, 'out'), (self.blocks_message_debug_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_1, 'header'), (self.lora_demod_0_1_0_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_1_0, 'out'), (self.blocks_message_debug_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_1_0, 'header'), (self.lora_demod_0_1_0_1_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_1_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_1_0_0, 'header'), (self.lora_demod_0_1_0_1_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_1_0_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_1_0_0_0, 'header'), (self.lora_demod_0_1_0_1_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_1_1, 'out'), (self.blocks_message_debug_0_0_0_1, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_1_1, 'header'), (self.lora_demod_0_1_0_1_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_0_1_1_0, 'out'), (self.blocks_message_debug_0_0_0_1_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_0_1_1_0, 'header'), (self.lora_demod_0_1_0_1_1_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_1, 'out'), (self.blocks_message_debug_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_1, 'header'), (self.lora_demod_0_1_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_1_0, 'out'), (self.blocks_message_debug_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_1_0, 'header'), (self.lora_demod_0_1_1_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_1_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_1_0_0, 'header'), (self.lora_demod_0_1_1_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_1_0_0_0, 'out'), (self.blocks_message_debug_0_0_0_0_0_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_1_0_0_0, 'header'), (self.lora_demod_0_1_1_0_0_0, 'header'))
        self.msg_connect((self.lora_decode_0_1_1_1, 'out'), (self.blocks_message_debug_0_0_0_1, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_1_1, 'header'), (self.lora_demod_0_1_1_1, 'header'))
        self.msg_connect((self.lora_decode_0_1_1_1_0, 'out'), (self.blocks_message_debug_0_0_0_1_0, 'print_pdu'))
        self.msg_connect((self.lora_decode_0_1_1_1_0, 'header'), (self.lora_demod_0_1_1_1_0, 'header'))
        self.msg_connect((self.lora_demod_0, 'out'), (self.lora_decode_0, 'in'))
        self.msg_connect((self.lora_demod_0_0, 'out'), (self.lora_decode_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_0_0, 'out'), (self.lora_decode_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_0_0_0, 'out'), (self.lora_decode_0_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_0_0_0_0, 'out'), (self.lora_decode_0_0_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_0_0_0_0_0, 'out'), (self.lora_decode_0_0_0_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1, 'out'), (self.lora_decode_0_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_0, 'out'), (self.lora_decode_0_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0, 'out'), (self.lora_decode_0_1_0_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0, 'out'), (self.lora_decode_0_1_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_0, 'out'), (self.lora_decode_0_1_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_0_0, 'out'), (self.lora_decode_0_1_0_0_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_0_0_0, 'out'), (self.lora_decode_0_1_0_0_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_0_0_0_0, 'out'), (self.lora_decode_0_1_0_0_1_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_0_0_0_0_0, 'out'), (self.lora_decode_0_1_0_0_1_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_0_0_1, 'out'), (self.lora_decode_0_1_0_0_1_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_0_0_1_0, 'out'), (self.lora_decode_0_1_0_0_1_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_1, 'out'), (self.lora_decode_0_1_0_0_0_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_1_0, 'out'), (self.lora_decode_0_1_0_0_0_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_1_0_0, 'out'), (self.lora_decode_0_1_0_0_0_1_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_1_0_0_0, 'out'), (self.lora_decode_0_1_0_0_0_1_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_1_1, 'out'), (self.lora_decode_0_1_0_0_0_1_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_0_1_1_0, 'out'), (self.lora_decode_0_1_0_0_0_1_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_1, 'out'), (self.lora_decode_0_1_0_0_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_1_0, 'out'), (self.lora_decode_0_1_0_0_0_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_1_0_0, 'out'), (self.lora_decode_0_1_0_0_0_0_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_1_0_0_0, 'out'), (self.lora_decode_0_1_0_0_0_0_0_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_1_0_0_0_0, 'out'), (self.lora_decode_0_1_0_0_0_0_0_0_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_1_0_1, 'out'), (self.lora_decode_0_1_0_0_0_0_0_0_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_1_0_1_0, 'out'), (self.lora_decode_0_1_0_0_0_0_0_0_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_2, 'out'), (self.lora_decode_0_1_0_0_0_0_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_2_0, 'out'), (self.lora_decode_0_1_0_0_0_0_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_2_0_0, 'out'), (self.lora_decode_0_1_0_0_0_0_1_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_2_0_0_0, 'out'), (self.lora_decode_0_1_0_0_0_0_1_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_2_1, 'out'), (self.lora_decode_0_1_0_0_0_0_1_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_0_2_1_0, 'out'), (self.lora_decode_0_1_0_0_0_0_1_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_1, 'out'), (self.lora_decode_0_1_0_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_1_0, 'out'), (self.lora_decode_0_1_0_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_1_0_0, 'out'), (self.lora_decode_0_1_0_1_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_1_0_0_0, 'out'), (self.lora_decode_0_1_0_1_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_1_1, 'out'), (self.lora_decode_0_1_0_1_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_0_1_1_0, 'out'), (self.lora_decode_0_1_0_1_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_1, 'out'), (self.lora_decode_0_1_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_1_0, 'out'), (self.lora_decode_0_1_1_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_1_0_0, 'out'), (self.lora_decode_0_1_1_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_1_0_0_0, 'out'), (self.lora_decode_0_1_1_0_0_0, 'in'))
        self.msg_connect((self.lora_demod_0_1_1_1, 'out'), (self.lora_decode_0_1_1_1, 'in'))
        self.msg_connect((self.lora_demod_0_1_1_1_0, 'out'), (self.lora_decode_0_1_1_1_0, 'in'))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.pfb_arb_resampler_xxx_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0_1, 0), (self.pfb_arb_resampler_xxx_0_0_0_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.lora_demod_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.lora_demod_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.lora_demod_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.lora_demod_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.lora_demod_0_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.lora_demod_0_0_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.lora_demod_0_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.lora_demod_0_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.lora_demod_0_1_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.lora_demod_0_1_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.lora_demod_0_1_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.lora_demod_0_1_0_0_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0, 0), (self.lora_demod_0_1_0_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0, 0), (self.lora_demod_0_1_0_0_0_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0, 0), (self.lora_demod_0_1_0_0_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0, 0), (self.lora_demod_0_1_0_0_2, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0, 0), (self.lora_demod_0_1_0_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0, 0), (self.lora_demod_0_1_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0, 0), (self.lora_demod_0_1_0_0_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0, 0), (self.lora_demod_0_1_0_0_0_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0, 0), (self.lora_demod_0_1_0_0_1_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0, 0), (self.lora_demod_0_1_0_0_2_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0, 0), (self.lora_demod_0_1_0_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0, 0), (self.lora_demod_0_1_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0, 0), (self.lora_demod_0_1_0_0_0_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0, 0), (self.lora_demod_0_1_0_0_0_1_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0, 0), (self.lora_demod_0_1_0_0_1_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0, 0), (self.lora_demod_0_1_0_0_2_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0, 0), (self.lora_demod_0_1_0_1_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0, 0), (self.lora_demod_0_1_1_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0_0, 0), (self.lora_demod_0_1_0_0_0_0_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0_0, 0), (self.lora_demod_0_1_0_0_0_1_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0_0, 0), (self.lora_demod_0_1_0_0_1_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0_0, 0), (self.lora_demod_0_1_0_0_2_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0_0, 0), (self.lora_demod_0_1_0_1_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0_0, 0), (self.lora_demod_0_1_1_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1, 0), (self.lora_demod_0_1_0_0_0_0_0_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1, 0), (self.lora_demod_0_1_0_0_0_1_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1, 0), (self.lora_demod_0_1_0_0_1_0_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1, 0), (self.lora_demod_0_1_0_0_2_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1, 0), (self.lora_demod_0_1_0_1_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1, 0), (self.lora_demod_0_1_1_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1_0, 0), (self.lora_demod_0_1_0_0_0_0_0_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1_0, 0), (self.lora_demod_0_1_0_0_0_1_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1_0, 0), (self.lora_demod_0_1_0_0_1_0_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1_0, 0), (self.lora_demod_0_1_0_0_2_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1_0, 0), (self.lora_demod_0_1_0_1_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_1_0, 0), (self.lora_demod_0_1_1_1_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0_1, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_payload_len(self):
        return self.payload_len

    def set_payload_len(self, payload_len):
        self.payload_len = payload_len

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)

    def get_crc(self):
        return self.crc

    def set_crc(self, crc):
        self.crc = crc

    def get_cr(self):
        return self.cr

    def set_cr(self, cr):
        self.cr = cr

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw





def main(top_block_cls=Multi_SF_decoder_gr_lora, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
