str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find(':')
new_str = str[atpos+1:]
new_str = float(new_str)
print(new_str)
