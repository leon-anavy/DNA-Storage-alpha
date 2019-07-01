#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: experiment1
# Project: DNA-Storage-alpha
# Author: Leon Anavy
# Email: anavy (at) technion (dot) ac (dot) il
# Created: 01/07/2019 03:37

from encoding.repeatition_code import repeatition_code
from encoding.bin2dna.two_bits import two_bits
from simualtors.synthesizers import printer
from simualtors.storage import storage
from simualtors.sequencers import NGS
from encoding.reads2seq import reads2seq

def main():
	print('generate message')
	msg_in = '01010110'
	print('encode message')
	msg_encoded = repeatition_code.encode(msg_in)
	print('convert to dna')
	dna_encoded = two_bits.bin2dna(msg_encoded)
	print('synthesize dna')
	dna_mol_syn = printer.print_dna(dna_encoded)
	print('store dna')
	dna_mol_stor = storage.store(dna_mol_syn)
	print('sequence dna')
	reads = NGS.dna_sequence(dna_mol_stor)
	print('infer dna sequence')
	dna_seq_read = reads2seq.infer(reads)
	print('convert to binary')
	msg_read = two_bits.dna2bin(dna_seq_read)
	print('decode message')
	msg_decoded = repeatition_code.decode(msg_read)
	print('done:')
	print(msg_in,msg_decoded)

if __name__ == '__main__':
	main()
