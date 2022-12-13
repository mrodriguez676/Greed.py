class Director:
    
    def __init__(self, keyboard_service, video_service):
          
        self._keyboard_service = keyboard_service
    
        self._video_service = video_service
    
        self._score = 0
    
    def _help_test(self, cast):
        all_cast = cast.get_all_actors()
        print("--------------------")
        print("Objects in game:\n")
        print(f"All Actors: {all_cast}")
        print("--------------------")
        banner = cast.get_first_actor("banners")
        tracker = cast.get_first_actor("tracker")
        notification = cast.get_first_actor("notification")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")
        print(f"Player: {robot}, Banner: {banner}, Tracker: {tracker}, Notify: {notification}")
        print(f"Gems: [{gems}] \n Rocks: [{rocks}]")
        print(f"All Artifacts: [{artifacts}]")
        print("---------------------")
        
        def start_game(self, cast):
            
             self._help_test(cast)
             
             self._video_service.open_window()
             
             while self._video_service.is_window_open():
                 
                 notification.set_text(f'Collision: Gem')
                 
                 self._score += gem._collision_score
                 
                 gem.is_used("")
                 
             for rock in rocks:
                
                if robot.get_position().equals(rock.get_position()):
                    
                    notification.set_text(f'Collision: Rock')
                    
                    self._score += rock._collision_score
                    
                    rock.is_used(" ")
def _do_outputs(self, cast):
     
     self._video_service.clear_buffer()
     actors = cast.get_all_actors()
     self._video_service.draw_actors(actors)
     self._video_service.flush_buffer()
     
     
     
     
     
                         
                    
                   
                 
                 
            
                  
             
        
        
        
        
        
        
        
        
        
        
        
        
      
      
