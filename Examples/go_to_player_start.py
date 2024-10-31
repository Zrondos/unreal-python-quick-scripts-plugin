import unreal

def main():
    subsystem=unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
    world = subsystem.get_editor_world()
    player_start_actors = unreal.GameplayStatics.get_all_actors_of_class(world, unreal.PlayerStart)
    if len(player_start_actors):
        player_start = player_start_actors[0]
        scene_component = player_start.get_editor_property("root_component")
        relative_location = scene_component.get_editor_property("relative_location")
        relative_rotation = scene_component.get_editor_property("relative_rotation")
        subsystem.set_level_viewport_camera_info(relative_location, relative_rotation)

main()