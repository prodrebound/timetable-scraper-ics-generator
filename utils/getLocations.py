import env


def get_location_from_room_description(room):
    room_without_brackets = room.replace("(", "").replace(")", "")
    return env.ROOM_TO_ADRESS.get(room_without_brackets, room)