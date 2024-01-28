# Made by Logan -!not ChatGPT!- to learn RegEx and DocX a lil better
# Tested with Cisco Lab handouts

#Import some cool stuff
import re
import docx

#Dolla Dolla Bills Yall She's About To Get Stripping!
def stripper(docx_file, output_file):
    
    #First read the Word doc through DocX so it becomes a big juicy Document class
    doc = docx.Document(docx_file)
    #Now make a place to store our output text string (can only write to docs with strings)
    text = ""
    #Define the RegEx search pattern here
    regex = r"^[RS]\d"

    #Let's start working with the docx -> split each paragraph element into their own lines, this creates a list
    for paragraph in doc.paragraphs:
        lines = paragraph.text.splitlines()
    
        #Now iterate through the list and use RegEx to find matching patterns
        for line in lines:

            #For every matching pattern, add the list element to the text string. We be converting over here
            if re.findall(regex, line):
               text += line + "\n\n"
            
   #We should have a string, separated by newlines, of lines starting with R or S followed by a digit
   #Open an output file, write to it with the 'text' string variable we assembled
    with open(output_file, 'w') as file:
        file.write(text)
        
#Be polite and only run this program if it is the main program being run
if __name__ == "__main__":
    input_docx_file = "Lab 06.docx"  # Replace with your input Word document
    output_txt_file = "output.txt"  # Replace with the desired output text file

    #Call that money makin function and create a text file for speedrunning Cisco labs
    stripper(input_docx_file, output_txt_file)
    print("Commands stripped and saved to", output_txt_file)
    
# If you have any improvements, feel free to share :)
# Good luck with studying!