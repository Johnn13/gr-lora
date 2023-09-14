/* -*- c++ -*- */
/* 
 * Copyright 2016 Bastille Networks.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_LORA_DEMOD_IMPL_H
#define INCLUDED_LORA_DEMOD_IMPL_H

#include <cmath>
#include <cstdlib>
#include <vector>
#include <queue>
#include <complex>
#include <fstream>
#include <numeric>
#include <gnuradio/fft/fft.h>
#include <gnuradio/fft/window.h>
#include <volk/volk.h>
#include "lora/demod.h"
#include "utilities.h"


namespace gr {
  namespace lora {

    class demod_impl : public demod
    {
     private:
      pmt::pmt_t d_header_port;
      pmt::pmt_t d_out_port;

      demod_state_t d_state;
      uint8_t d_sf;
      uint8_t d_cr;
      uint8_t d_dw_size;
      uint8_t d_payload_len;
      bool d_crc;
      bool d_ldr;
      bool d_header;
      bool d_header_received;
      bool d_header_valid;

      uint16_t d_num_symbols;
      uint16_t d_fft_size_factor;
      uint32_t d_fft_size;
      uint16_t d_overlaps;
      uint16_t d_offset;
      uint16_t d_p;
      uint32_t d_num_samples;
      uint32_t d_bin_size;
      uint32_t d_preamble_drift_max;

      uint32_t d_packet_symbol_len;

      float d_cfo;

      uint32_t d_preamble_idx;
      uint16_t d_sfd_idx;
      std::vector<uint32_t> d_argmax_history;
      std::vector<std::vector<uint32_t>> preamble_pk_list;
      std::vector<uint16_t> d_sfd_history;
      uint16_t d_sync_recovery_counter;

      uint16_t d_peak_search_algorithm;
      uint16_t d_peak_search_phase_k;

      std::vector<uint16_t> pattern;

      fft::fft_complex   *d_fft;
      std::vector<float> d_window;
      std::vector<float> d_window_large;
      float              d_beta;

      std::vector<gr_complex> d_upchirp;
      std::vector<gr_complex> d_downchirp;

      // 这两个 base up-/down-chirp 用来进行前导部分的detect
      std::vector<gr_complex> ref_upchirp;
      std::vector<gr_complex> ref_downchirp;

      float ref_upchirp_bin;
      float ref_downchirp_bin;
      std::vector<uint32_t> ref_pattern_bin_list;
      std::vector<uint32_t> pattern_bin_list;

      std::vector<float> d_symbols;

      std::ofstream f_raw, f_up_windowless, f_up, f_down, f_fft;
      std::ofstream f_ref_up,f_ref_down,f_dechirp_up,f_dechirp_down,f_fft_up,f_fft_down,f_fft_iq;

     public:
      demod_impl( uint8_t   spreading_factor,
                  bool      header,
                  uint8_t   payload_len,
                  uint8_t   cr,
                  bool      crc,
                  uint8_t   dw_size,
                  bool      low_data_rate,
                  float     beta,
                  uint16_t  fft_factor,
                  uint8_t   peak_search_algorithm,
                  uint16_t  peak_search_phase_k,
                  float     fs_bw_ratio);
      ~demod_impl();

      uint16_t argmax(gr_complex *fft_result);
      uint32_t argmax_32f(float *fft_result, float *max_val_p);
      uint32_t search_fft_peak(const lv_32fc_t *fft_result,
                                   float *buffer1, float *buffer2,
                                   gr_complex *buffer_c, float *max_val_p);
      uint32_t fft_add(const lv_32fc_t *fft_result, float *buffer, gr_complex *buffer_c,
                           float *max_val_p, float phase_offset);
      void dynamic_compensation(std::vector<uint16_t>& compensated_symbols);
      
      void parse_header(pmt::pmt_t dict);
    
      void dechirp(bool is_up,
                            const gr_complex *in,
                            gr_complex *up_block,
                            uint8_t dw_size,
                            float *fft_mag,
                            float *fft_add);
      
      std::vector<uint32_t> preamble_dechirp(const gr_complex *in);
      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace lora
} // namespace gr

#endif /* INCLUDED_LORA_DEMOD_IMPL_H */

