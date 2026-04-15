from fileLoader import load_audio_files
from pitchHandler import pitchshift


if __name__ == "__main__":
    #names of the voices in elevenlabs 
    names = ["Bella", "Clancy", "Matt", "River"] #Name of the three voices we are using 


    #define the folder that the stimuli that has the stim you want to change 

    storagefolder= 'C:/Users/testarr/Documents/pythoncode/PitchAnalysis/Bella512' 
    audio_files, GibFiles, IEEEFiles = load_audio_files(storagefolder, names) # function creats a list of wav files in the folder 

    newfolder = "BellaShifted"

    pitchshift(GibFiles['Bella'], 0.874079226075685, newfolder, storagefolder)  ##0.874079226075685 to
    pitchshift(GibFiles['River'], 1.129, newfolder, storagefolder)  ##1.129 gets to 192
    pitchshift(GibFiles['Clancy'], 1.071, newfolder, storagefolder)  ##1.071 gets to 90
    pitchshift(GibFiles['Matt'], 0.88899, newfolder, storagefolder) 

    pitchshift(IEEEFiles['Bella'], 0.904761904761905, newfolder, storagefolder)  #0.904761904761905, to get to 192
    pitchshift(IEEEFiles['River'], 1.1228, newfolder, storagefolder)  ## 1.1228 gets to 192
    pitchshift(IEEEFiles['Clancy'], 1.046, newfolder, storagefolder)  ##1.046 gets to 90 
    pitchshift(IEEEFiles['Matt'], 0.88999, newfolder, storagefolder) 

    print ("Files made")
