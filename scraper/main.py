from video_games import VideoGame
import pandas as pd
import time
import random


def main():
    my_game_list_as_objects = create_all_video_game_objects(
        'docs/my_game_list.txt')
    create_data_frame(my_game_list_as_objects)
   # wifes_game_list_as_objects = create_all_video_game_objects(
    # 'docs/wifes_game_list.txt')


def create_data_frame(list_of_video_games: list[VideoGame]):
    df = pd.DataFrame([game.as_dict() for game in list_of_video_games])
    print(df)
    df.index.name = 'My Game Rankings'
    df.index += 1
    df.to_csv('video_game_table.csv')
    pass


def create_all_video_game_objects(file_path: str) -> list:
    list_of_video_games = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            video_game_object = VideoGame(line)
            time.sleep(random.randint(0, 3))
            list_of_video_games.append(video_game_object)
    return list_of_video_games


if __name__ == "__main__":
    main()
