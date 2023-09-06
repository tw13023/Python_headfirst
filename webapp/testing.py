from flask import Flask, render_template, request, escape
with open('vsearch.log') as log:
     
     lines = []
     for raw_line in log:
         line_list = raw_line.split('|')
         print(type(line_list))
         print(line_list)
         lines.append(line_list)
         print('--------')       
       
     print(str(escape(lines)))    