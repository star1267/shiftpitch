from fileLoader import load_audio_files
from pitchHandler import pitchshift


if __name__ == "__main__":
    #names of the voices in elevenlabs 
    names = ["Bella", "Clancy", "Matt", "River"] #Name of the three voices we are using 


    #define the folder that the stimuli that has the stim you want to change 

    storagefolder= 'C:/Users/testarr/Documents/pythoncode/PitchAnalysis/FinalWav' 
    audio_files, GibFiles, IEEEFiles = load_audio_files(storagefolder, names) # function creats a list of wav files in the folder 

    newfolder = "MatchPitches"

    pitchshift(GibFiles['Bella'], 0.8767, newfolder, storagefolder)  
    #pitchshift(GibFiles['River'], 1.129, newfolder, storagefolder)  ##1.129 gets to 192
    #pitchshift(GibFiles['Clancy'], 1.071, newfolder, storagefolder)  ##1.071 gets to 90
    pitchshift(GibFiles['Matt'], 0.9329, newfolder, storagefolder) 

    pitchshift(IEEEFiles['Bella'], 0.9142, newfolder, storagefolder)  
    #pitchshift(IEEEFiles['River'], 1.1228, newfolder, storagefolder)  ## 1.1228 gets to 192
    #pitchshift(IEEEFiles['Clancy'], 1.046, newfolder, storagefolder)  ##1.046 gets to 90 
    pitchshift(IEEEFiles['Matt'], 0.9427, newfolder, storagefolder) 

    print ("Files made")
