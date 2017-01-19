#add pause/play/quit/next song
oscillioscope--use grove mic for threshhold triggers

import pygame

pygame.init()
pygame.mixer.init(44100, -16,2,2048)
#pygame.mixer.music.queue('next_song.mp3') que song
#pygame.mixer.music.stop() stop song
#////////////////////////////FX
'''effect = pygame.mixer.Sound('beep.wav')
effect.play()'''
#/////////////////play songs randomly

#_songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3', 'song_4.mp3', 'song_5.mp3']
_songs=['/home/pi/Desktop/MUZAK/%s.mp3']
_currently_playing_song = None

import random

def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()
#/////////////////////////////end of song event



SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('Peter Schilling - Major Tom.mp3')
pygame.mixer.music.play()

while True:
    
    for event in pygame.event.get():
        
        if event.type == SONG_END:
            #pygame.mixer.music.load('FIDLAR - Leave Me Alone.mp3')
            play_a_different_song
            #pygame.mixer.music.play(0)#-1 for infinite loop
            print("the song ended!")
    
