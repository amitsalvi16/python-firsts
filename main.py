from replit import audio
import logging
import subprocess
def main():
    source = None
    try:
      #source = audio.play_file('song.mp3')
      #source.toggle_playing()
      subprocess.check_output(['play', 'song.mp3'])
    except Exception as e: 
      print("error !")
      print(e)
    
    #if source.get_paused() == True:
    #  source.toggle_playing()

    print('press enter to play/pause')

    while True:        
        cmd = input('> ').lower()
        
        if cmd == 'play':
            print("play")
        elif cmd == 'pause':
            print("pause")


main()