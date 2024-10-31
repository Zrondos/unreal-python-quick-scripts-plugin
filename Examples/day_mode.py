import unreal

def main():
    subsystem=unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
    world = subsystem.get_editor_world()
    actors = unreal.GameplayStatics.get_all_actors_of_class(world, unreal.DirectionalLight)
    if len(actors):
        actors[0].get_editor_property("light_component").set_editor_property("intensity",2.5)
        
main()