README.md

Name: Tanuja Mohan
Class: ITP 125 - Hackers to CEOs
Final Programming Assignment - Old Spice Voicemail

Logic:
I first read in the command line arguments that the user enters and error check that all the correct arguments are present. If all the arguments are present, then I proceed to store the values for each argument into a local variable. I then do error checking on these values to make sure that they are valid and exist. This error checking includes making sure the phone number is one of the 4 valid formats. If all values are properly formatted I then display a summary of the inputs and ask the user to accept of decline the information. If the user declines, I then terminate the program. If the user accepts I then download the files from online and use an array to maintain the order in which I need to stitch the mp3 files together. The final step is putting the mp3 files together into one mp3 file which I do by calling the cat command line argument.

To Run: 
To run the program use the command line ‘python finalProject.py -g f -n “##########” -r # -e # -o output.txt