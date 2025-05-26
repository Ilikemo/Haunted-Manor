import json
from item import Item
from world import Room, Container
from unit import Unit  # For mobs, if needed

def load_world():
    # Load data
    with open("data/items.json") as f:
        item_data = json.load(f)

    with open("data/containers.json") as f:
        container_data = json.load(f)

    with open("data/rooms.json") as f:
        room_data = json.load(f)

    with open("data/exits.json") as f:
        exits_data = json.load(f)

    items = {}
    containers = {}
    rooms = {}

    # Create item instances
    for key, data in item_data.items():
        items[key] = Item(**data)

    # Create container instances
    for key, data in container_data.items():
        container_items = [items[item_key] for item_key in data.get("items", [])]
        container_key = items[data["key"]] if data.get("key") else None
        containers[key] = Container(
            name=data["name"],
            description=data["description"],
            items=container_items,
            key=container_key,
            is_locked=data.get("is_locked", False)
        )

    # Create room instances
    for key, data in room_data.items():
        interactables = []

        for name in data.get("interactables", []):
            if name in items:
                interactables.append(items[name])
            elif name in containers:
                interactables.append(containers[name])

        mob = None
        if data.get("mob"):
            mob = Unit(data["mob"], 30, 8)  # simple placeholder for now

        room = Room(
            name=data["name"],
            description=data["description"],
            interactables=interactables,
            mob=mob,
            locked=data.get("locked", False),
            key=items[data["key"]] if data.get("key") else None,
            door_description=data.get("door_description", "")
        )
        rooms[key] = room

    # Link exits
    for room_key, exits in exits_data.items():
        for direction, target_room_key in exits.items():
            rooms[room_key].add_exit(direction, rooms[target_room_key])

    return rooms
