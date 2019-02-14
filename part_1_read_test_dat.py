from builtins import print

from cc_dat_utils import make_cc_data_from_dat


input_dat_file = "data/pfgd_test.dat"
data = make_cc_data_from_dat(input_dat_file)
print(data)



#Use cc_dat_utils.make_cc_data_from_dat() to load the file specified by input_dat_file
#print the resulting data
