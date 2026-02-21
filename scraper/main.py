from video_games import VideoGame
import pandas as pd
import time
import random


def main():
    my_game_list_as_objects = create_all_video_game_objects(
        'docs/my_game_list.txt')
    wifes_game_list_as_objects = create_all_video_game_objects(
        'docs/wifes_game_list.txt')
    # link_to_the_past = VideoGame('The Legend of Zelda: A Link To The Past')
    # create_data_frame(link_to_the_past)
    # print(vars(link_to_the_past))


def create_data_frame(video_games: list[VideoGame]):
    list_of_video_games = []
    # list_of_video_games.append(video_games.as_dict())
    list_of_video_games.append(video_games)
    print(list_of_video_games)
    print()
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
