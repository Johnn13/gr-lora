#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Rx USRP
# Author: jkadbear
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


class rx_usrp(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Rx USRP")

        ##################################################
        # Variables
        ##################################################
        self.sf = sf = 7
        self.bw = bw = 250000
        self.samp_rate = samp_rate = 500e3
        self.payload_len = payload_len = 8
        self.ldr = ldr = 2**sf/bw > 16e-3
        self.header = header = True
        self.freq = freq = 868000000
        self.crc = crc = True
        self.cr = cr = 3

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
        self.uhd_usrp_source_0.set_gain(20, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_bandwidth(bw, 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        # No synchronization enforced.
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
        self.lora_demod_old_0 = lora.Olddemod(sf, header, payload_len, 1, crc, ldr, 25.0, 10, 0, 4, 2)
        self.lora_decode_0 = lora.decode(sf, header, payload_len, cr, crc, ldr)
        self.blocks_socket_pdu_0 = blocks.socket_pdu('UDP_CLIENT', '127.0.0.1', '52002', 10000, False)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lora_decode_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))
        self.msg_connect((self.lora_decode_0, 'header'), (self.lora_demod_old_0, 'header'))
        self.msg_connect((self.lora_demod_old_0, 'out'), (self.lora_decode_0, 'in'))
        self.connect((self.low_pass_filter_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.lora_demod_old_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))


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
        self.uhd_usrp_source_0.set_bandwidth(self.bw, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.bw/2+10e3, 1e3, firdes.WIN_RECTANGULAR, 6.76))
        self.pfb_arb_resampler_xxx_0.set_rate(2*self.bw/self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

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
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)

    def get_crc(self):
        return self.crc

    def set_crc(self, crc):
        self.crc = crc

    def get_cr(self):
        return self.cr

    def set_cr(self, cr):
        self.cr = cr





def main(top_block_cls=rx_usrp, options=None):
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
