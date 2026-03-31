from fileLoader import load_audio_files
from pitchHandler import pitchshift


def manipulatevoices(Files, newfolder): 
    pitchshift(Files['Bella'], 0.9, newfolder, storagefolder)  
    #pitchshift(Files['River'], 1.12, newfolder, storagefolder)  
    #pitchshift(Files['Clancy'], 1.09, newfolder, storagefolder)  
    #pitchshift(Files['Matt'], 0.9, newfolder, storagefolder)  


if __name__ == "__main__":
    #names of the voices in elevenlabs 
    names = ["Bella", "Clancy", "Matt", "River"] #Name of the three voices we are using 


    #define the folder that the stimuli that has the stim you want to change 
    #// TODO Make it so it stops saving the new files in the folder with the old files 
    storagefolder= 'C:/Users/testarr/Documents/pythoncode/PitchAnalysis/FinalWav' 
    audio_files, GibFiles, IEEEFiles = load_audio_files(storagefolder, names) # function creats a list of wav files in the folder 

    newfolder = "New"
    manipulatevoices(IEEEFiles, newfolder)
    manipulatevoices(GibFiles, newfolder)
    print ("Files made")
