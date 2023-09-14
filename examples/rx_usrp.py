#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Rx USRP
# Author: jkadbear
# GNU Radio version: v3.8.5.0-6-g57bd109d

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time

from gnuradio import qtgui

class rx_usrp(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Rx USRP")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Rx USRP")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "rx_usrp")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.sf = sf = 7
        self.bw = bw = 250000
        self.samp_rate = samp_rate = 500e3
        self.payload_len = payload_len = 8
        self.ldr = ldr = 2**sf/bw > 16e-3
        self.header = header = True
        self.freq = freq = 470e6
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
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            freq, #fc
            bw, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rx_usrp")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

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
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.freq, self.bw)
        self.uhd_usrp_source_0.set_bandwidth(self.bw, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
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
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.freq, self.bw)
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

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
