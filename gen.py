import numpy as np
import os
import scipy
from text_parsing import ret_parse
import get_cmd

test_dir = './'
resources_dir = './resources/'

# dx_vst = resources_dir + 'mda_DX10.vst'
dx_vst = resources_dir + 'Dexed.vst'

midi_fl = resources_dir + 'midi_export.mid'
# generator = resources_dir + 'mrswatson64'
generator = resources_dir + 'mrswatson'

fl_name = 'text.wav'

ind_array = ret_parse()
assert len(ind_array) == 147, (len(ind_array), ind_array)

param_set = ""
for x in range(1, len(ind_array) + 1):
    param_set += "--parameter {},{} ".format(str(x), ind_array[x - 1])

cmd = get_cmd.base_command(generator, dx_vst, midi_fl, param_set, fl_name)
os.system.__call__(cmd)

print("Done")
