#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Rx File
# Author: jkadbear
# GNU Radio version: v3.8.5.0-6-g57bd109d

from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb
import lora


class rx_by_remote(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Rx File")

        ##################################################
        # Variables
        ##################################################
        self.sf = sf = 7
        self.bw = bw = 250e3
        self.samp_rate = samp_rate = 500e3
        self.payload_len = payload_len = 8
        self.ldr = ldr = 2**sf/bw > 16e-3
        self.header = header = True
        self.freq = freq = 868e6
        self.dw_size = dw_size = 2
        self.crc = crc = True
        self.cr = cr = 1

        ##################################################
        # Blocks
        ##################################################
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
            2*bw/samp_rate,
            taps=None,
            flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                bw/2+10e3,
                1e3,
                firdes.WIN_RECTANGULAR,
                6.76))
        self.lora_demod_1 = lora.demod(sf, header, payload_len, 1, crc, dw_size, ldr, 25.0, 8, 0, 4, 2)
        self.lora_decode_0 = lora.decode(sf, header, payload_len, cr, crc, ldr)
        self.blocks_socket_pdu_0 = blocks.socket_pdu('UDP_CLIENT', '127.0.0.1', '52002', 10000, False)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/jm/matlab_sig/ud_pre_packet.cfile', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/jm/matlab_sig/in_iq.cfile', False)
        self.blocks_file_sink_0.set_unbuffered(False)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lora_decode_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))
        self.msg_connect((self.lora_decode_0, 'header'), (self.lora_demod_1, 'header'))
        self.msg_connect((self.lora_demod_1, 'out'), (self.lora_decode_0, 'in'))
        self.connect((self.blocks_file_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.lora_demod_1, 0))


    def get_sf(self):
        return self.sf

    def set_sf(self, sf):
        self.sf = sf
        self.set_ldr(2**self.sf/self.bw > 16e-3)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.set_ldr(2**self.sf/self.bw > 16e-3)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.bw/2+10e3, 1e3, firdes.WIN_RECTANGULAR, 6.76))
        self.pfb_arb_resampler_xxx_0.set_rate(2*self.bw/self.samp_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.bw/2+10e3, 1e3, firdes.WIN_RECTANGULAR, 6.76))
        self.pfb_arb_resampler_xxx_0.set_rate(2*self.bw/self.samp_rate)

    def get_payload_len(self):
        return self.payload_len

    def set_payload_len(self, payload_len):
        self.payload_len = payload_len

    def get_ldr(self):
        return self.ldr

    def set_ldr(self, ldr):
        self.ldr = ldr

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_dw_size(self):
        return self.dw_size

    def set_dw_size(self, dw_size):
        self.dw_size = dw_size

    def get_crc(self):
        return self.crc

    def set_crc(self, crc):
        self.crc = crc

    def get_cr(self):
        return self.cr

    def set_cr(self, cr):
        self.cr = cr





def main(top_block_cls=rx_by_remote, options=None):
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
