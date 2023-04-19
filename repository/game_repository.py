from pymysql.connections import Connection

from models.game import Game


class GameRepository:
    connection: Connection

    def __init__(self, connection) -> None:
        self.connection = connection

    def insert_game(self, name, description, price):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO games(name, description, price) VALUES (%s, %s, %s)",
                (name, description, price),
            )
        self.connection.commit()
        self.connection.close()

    def get_games(self):
        games = []
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT id, name, description, price FROM games")
            games = [Game(*game_data) for game_data in cursor.fetchall()]
        self.connection.close()
        return games

    def get_game_by_id(self, id):
        game = None
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, description, price FROM games WHERE id = %s",
                id
            )
            game = Game(*cursor.fetchone())
        self.connection.close()
        return game

    def update_game(self, id, name, description, price):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE games SET name = %s, description = %s, price = %s WHERE id = %s",
                (name, description, price, id)
            )
        self.connection.commit()
        self.connection.close()

    def delete_game(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM games WHERE id = %s", id)
        self.connection.commit()
        self.connection.close()
