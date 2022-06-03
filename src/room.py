class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.song_list = []
        self.guest_list = []
    
    def guest_count(self):
        return len(self.guest_list)

    def check_in_guest(self, guest):
        self.guest_list.append(guest)
    
    def check_guest_out(self, guest):
        self.guest_list.pop(guest)

    def return_list(self):
        return self.guest_list
    
    def add_song_to_list(self, song):
        self.song_list.append(song)
    
    
