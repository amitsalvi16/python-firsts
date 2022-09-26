from replit import audio
import logging

def main():
    source = audio.play_file('song.mp3')
    source.toggle_playing()

    if source.get_paused() == True:
      source.toggle_playing()

    volume = 1
    loops = 0
  
    print('press enter to play/pause')

    while True:
        print(
            f'volume is at {source.volume * 100}% with',
            f'{source.loops_remaining} loops remaining.'
        )
        
        cmd = input('> ').lower()
        
        if cmd == 'play':
            print(source.get_remaining())
        elif cmd == 'pause':
            print(source.get_paused())


main()