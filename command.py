class Database:
    def __init__(self, id):
        self.id = id
        self.data = {}

    def get_id(self):
        return self.id

    def add(self, key, value):
        if key in self.data:
            return False
        self.data[key] = value
        return True

    def get(self, key):
        return self.data.get(key, None)

    def update(self, key, value):
        if key not in self.data:
            return False
        self.data[key] = value
        return True

    def remove(self, key):
        if key not in self.data:
            return False
        del self.data[key]
        return True

    def display(self):
        for key, value in self.data.items():
            print(f"{key}| {value}")


# Command base class
class Command:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError
    
class AddCommand(Command):
    def __init__(self, database, key, value):
        self.database = database
        self.key = key
        self.value = value

    def execute(self):
        self.database.add(self.key, self.value)

    def undo(self):
        self.database.remove(self.key)
        print("Undid AddCommand")

class UpdateCommand(Command):
    def __init__(self, database, key, value):
        self.database = database
        self.key = key
        self.value = value
        self.old_value = None

    def execute(self):
        if self.key in self.database.data:
            self.old_value = self.database.data[self.key]
        self.database.update(self.key, self.value)

    def undo(self):
        if self.old_value:
            self.database.update(self.key, self.old_value)
            print("Undid UpdateCommand")
            print(f"{self.key}| {self.old_value}")


class RemoveCommand(Command):
    def __init__(self, database, key):
        self.database = database
        self.key = key
        self.old_value = None

    def execute(self):
        if self.key in self.database.data:
            self.old_value = self.database.data[self.key]
        self.database.remove(self.key)

    def undo(self):
        if self.old_value:
            self.database.add(self.key, self.old_value)
            print("Undid RemoveCommand")

            for key, value in sorted(self.database.data.items()):
                print(f"{key}| {value}")

class MacroCommand:
    def __init__(self):
        self.commands = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def execute(self):
        print("Beginning a Macro")
        for command in self.commands:
            command.execute()
        print("Ending a Macro")

    def undo(self):
        print("Begin Undoing Macro")
        for command in reversed(self.commands):
            command.undo()
        print("End Undoing Macro")


def process_commands(commands):
    databases = {}
    command_stack = []
    current_macro = None

    for command in commands:
        parts = command.split(maxsplit=3)

        if len(parts) == 1:
            action = parts[0]
            if action == 'B':
                current_macro = MacroCommand()
                command_stack.append(current_macro)
            elif action == 'E' and current_macro:
                current_macro.execute()
                current_macro = None
            continue

        if len(parts) < 3:
            continue

        action, db_id, key, *value = parts

        if db_id not in databases:
            databases[db_id] = Database(db_id)

        database = databases[db_id]
        value = value[0] if value else ""

        if action == 'A':
            cmd = AddCommand(database, key, value)
        elif action == 'U':
            cmd = UpdateCommand(database, key, value)
        elif action == 'R':
            cmd = RemoveCommand(database, key)
        else:
            continue

        if current_macro:
            current_macro.add_command(cmd)
        else:
            cmd.execute()
            command_stack.append(cmd)

    print("Contents of Databases:")
    for db_id, db in databases.items():
        print(f"Database {db_id}:")
        db.display()
    print()

    for cmd in reversed(command_stack):
        cmd.undo()

    print("\nContents of Databases:")
    for db_id, db in databases.items():
        print(f"Database {db_id}:")
        db.display()


commands = [
    "A one key1 value1",
    "B",
    "A one key2 value two",
    "A one key3 value3",
    "E",
    "A two key4 value four",
    "R one key1",
    "U two key4 value4"
]

def main():
    process_commands(commands)


if __name__ == "__main__":
    main()
