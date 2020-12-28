# -*- coding: utf-8 -*-
"""
Speech recognition script that adds or removes a txt file 

"""


import speech_recognition as sr
import os 


class Recognize_speech:
    def __init__ (self):
        pass
    
    def listen(self):
        print("I am listening, say something !")
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        
        with self.mic as source:
            audio = self.r.listen(source)
        
            # set up the response object
        response = {
                        "success": True,
                        "error": None,
                        "transcription": None
                    }
                     
            # Recording successful
        try:
            response["transcription"] = self.r.recognize_google(audio)
            self.speech = response["transcription"]
                           
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
                                
        except sr.UnknownValueError:
            # Speech was unintelligible
            response["error"] = "Unable to recognize speech"
           
        return self.speech
        
        
    def add_file(self):
        print("Which file do you want to add ?")
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        
        with self.mic as source:
            audio = self.r.listen(source)
            file_to_add = self.r.recognize_google(audio)
    
        file_extension = file_to_add + ".txt"
        
        
        file = open(file_extension, "w")
        file.write("created from the moon")
        print(f"file {file_extension} added")
       
    def remove_file(self):
        print("Which file do you want to remove ?")
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        
        with self.mic as source:
            audio = self.r.listen(source)
            file_to_remove = self.r.recognize_google(audio)
        
        file_extension = file_to_remove + ".txt"
        os.remove(file_extension)
        
        print(f"file {file_extension} removed. Congratulations !")
     

if __name__ == "__main__":
    obj = Recognize_speech()    
    if (obj.listen()) == "add new file":
        obj.add_file()
    elif (obj.listen()) == "remove file":
        obj.remove_file()
    else:
        pass
    
    
    
    
    
    
    
    
    
    