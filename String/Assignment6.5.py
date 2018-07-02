##str = 'X-DSPAM-Confidence:0.8475'
#
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475 '

endPosition = str.find(':')
num_str = str[endPosition+1:-1].strip()
float_num = float(num_str)
print(float_num)
