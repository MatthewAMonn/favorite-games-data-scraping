from video_games import VideoGame
import pandas as pd


def main():
    link_to_the_past = VideoGame('The Legend of Zelda: A Link To The Past')
    create_data_frame(link_to_the_past)
    # print(vars(link_to_the_past))


def create_data_frame(video_games: VideoGame):
    list_of_video_games = []
    # list_of_video_games.append(video_games.as_dict())
    list_of_video_games.append(video_games)
    print(list_of_video_games)
    print()
    df = pd.DataFrame([p.as_dict() for p in list_of_video_games])
    print(df)
    df.index.name = 'My Game Rankings'
    df.index += 1
    df.to_csv('video_game_table.csv')
    pass


def create_all_video_game_objects():
    return 'asd'


if __name__ == "__main__":
    main()
