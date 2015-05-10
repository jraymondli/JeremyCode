##############################################################################
# This program takes an input and then aligns it by center and also surrounds 
# it with astericks.
# Author: Jeremy Li
# May 9, 2015
##############################################################################
 
input_dictionary = []
input_scan_val = 0
max_input_line_length = 0
align_spaces = 0
spacing_side1 = 0
input_print_val = 0
spacing_side_shifter = 0 
while True:
    try:                                                     
        line_input = raw_input()
	input_dictionary.append(line_input)
    except EOFError:
        break
max_dictionary_items = len(input_dictionary)-1
while input_scan_val <= max_dictionary_items: 
    if max_input_line_length < len(input_dictionary[input_scan_val]):
        max_input_line_length = len(input_dictionary[input_scan_val]) 
        input_scan_val = input_scan_val + 1
    else:
        input_scan_val = input_scan_val + 1
print '*' * (max_input_line_length+2)
for x in range(len(input_dictionary)):
   input_line_length  = len(input_dictionary[input_print_val])
   align_spaces = max_input_line_length - input_line_length
   if align_spaces == 0:
      print ''.join(str(y) for y in ('*',input_dictionary[input_print_val],'*'))
   elif align_spaces/2 * 2 != align_spaces:
      if spacing_side_shifter == 0:
          spacing_side1 = (align_spaces-1)/2
          spacing_side2 = (align_spaces+1)/2
          print ''.join(str(y) for y in ('*',' ' * spacing_side1,input_dictionary[input_print_val],' ' * spacing_side2,'*'))
          spacing_side_shifter = 1
      else:
          spacing_side1 = (align_spaces-1)/2
          spacing_side2 = (align_spaces+1)/2
          print ''.join(str(y) for y in ('*',' ' * spacing_side2,input_dictionary[input_print_val],' ' * spacing_side1,'*'))
          spacing_side_shifter = 0
   else:
       spacing_side1 = align_spaces/2 
       print ''.join(str(y) for y in ('*',' ' * spacing_side1,input_dictionary[input_print_val],' ' * spacing_side1,'*'))  
   input_print_val = input_print_val + 1
print '*' * (max_input_line_length+2)
