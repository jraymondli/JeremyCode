##############################################################################
# This program takes an input and then aligns it by center and also surrounds 
# it with astericks.
# Author: Jeremy Li
# May 9, 2015
##############################################################################
input_list = []
input_scan_val = 0
max_input_line_length = 0
align_spaces = 0
spacing_side1 = 0
input_print_val = 0
spacing_side_shifter = 0 
# defining majority of variables used in code
##############################################################################
while True:
    try:                                                     
        line_input = raw_input()
	input_list.append(line_input)
    except EOFError:
        break
# taking input from problem
##############################################################################
max_list_items = len(input_list)-1
while input_scan_val <= max_list_items: 
    if max_input_line_length < len(input_list[input_scan_val]):
        max_input_line_length = len(input_list[input_scan_val]) 
        input_scan_val = input_scan_val + 1
    else:
        input_scan_val = input_scan_val + 1
# finds maximum line length
##############################################################################
print '*' * (max_input_line_length+2)
for x in range(len(input_list)):
   input_line_length  = len(input_list[input_print_val]) 
   # length of current line
   align_spaces = max_input_line_length - input_line_length
   # length of total spaces(left and right of line)
   if align_spaces == 0:
      # if there are no spaces 
      print ''.join(str(y) for y in ('*',input_list[input_print_val],'*'))
   elif align_spaces/2 * 2 != align_spaces:
      # if there are odd spaces
      if spacing_side_shifter == 0:
          # first put more spaces on left on line
          spacing_side1 = (align_spaces-1)/2
          spacing_side2 = (align_spaces+1)/2
          print ''.join(str(y) for y in ('*',' ' * spacing_side1,input_list[input_print_val],' ' * spacing_side2,'*'))
          spacing_side_shifter = 1
      else:
          # then put more spaces on right of line
          spacing_side1 = (align_spaces-1)/2
          spacing_side2 = (align_spaces+1)/2
          print ''.join(str(y) for y in ('*',' ' * spacing_side2,input_list[input_print_val],' ' * spacing_side1,'*'))
          spacing_side_shifter = 0
   else:
       # if there are even spaces
       spacing_side1 = align_spaces/2 
       print ''.join(str(y) for y in ('*',' ' * spacing_side1,input_list[input_print_val],' ' * spacing_side1,'*'))  
   input_print_val = input_print_val + 1
print '*' * (max_input_line_length+2)
# block prints rectangle of astericks, spaces, and centered lines
##############################################################################
