# 폴더 및 파일 목록 데이터로 변경
import os
from collections import defaultdict

tkc_path = 'G:\T.K.C\음원'

list_by_year = os.listdir(tkc_path)

song_dict = defaultdict(list)

# 파일 형태는 음악 파일이거나 텍스트 파일인 경우가 있음
# 음악 파일인 경우 태그를 잘 가져올 수 있어야 한다
# 파일명에 적혀있는 정보가 들쑥 날쑥 하기 때문
# 디깅 목록 폴더는 확인 제외
for year in list_by_year:
    folder_path = f'{tkc_path}\{year}'
    song_list = os.listdir(folder_path)

    songs = []

    for song in song_list:
        if song == '업로드':
            uploaded_song_list = os.listdir(f'{folder_path}\업로드')
            for uploaded_song in uploaded_song_list:
                songs.append((uploaded_song, 'U'))
        elif song == '디깅 목록':
            continue
        else:
            songs.append((song, 'C'))
        
    song_dict[year] = songs

print(song_dict['2001'])
    

