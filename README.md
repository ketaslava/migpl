# MIGPL

Multi instance Godot project loader

# About

MIGPL is a script for automating the launch of a game project on the Godot Engine project in multiple instances. The script allows you to significantly speed up development of multiplayer projects by allowing you to automatically launch the server and multiple clients without having to launch them manually every time you build a project. This script fully automates this task.

# Features

* Automatically run multiple instances of a project
* Output debugging information to the console
* Easy installation and use

# Creators and contacts

The script was developed by Ketoslava Ket and KTVINCCO and is available for use under the MIT license

[Copyright Declaration](http://ktvincco.com/copyrightdeclaration/)
[Contact Ketoslava Ket](http://ktvincco.com/keta/contacts/)

# Instruction

* You can watch the tutorial on YouTube (https://youtu.be/fI239ocDA2E)

1. Download or clone repository

2. Extract migpl.zip and go to the master/migpl/ folder

3. Open terminal as admin or use sudo

4. Use "pip install" to install all requirements from requirements.txt for python3

5. Copy migpl.py to root directory of your project (where there is a project.godot file)

6. Go to the https://godotengine.org/ , click download (once), scroll down and download Export templates

7. Extract Export templates, and copy them to root directory of your project -> GodotProject/templates/[ManyFiles]

8. Open migpl.py and set export_template_path = "templates/YourSystemName.template"

9. Set project instances count (process_instances_count)

10. Set start arguments for instances of project (array_process_arguments), start arguments can be readed from any project script, use OS.get_cmdline_args() to get arguments array

11. If you want the client window to be on top after launching for convenience, set it to launch last in the queue and set a delay of 0.5 seconds before it opens

12. For convenience, you can remove the hotkeys, such as f3, f4 or f1, f2, in the shortcuts settings of the Godot editor and/or change script hotkeys settings

13. Open terminal in the project root folder as admin or use sudo

14. Run "python3 migpl.py"

15. Read instruction, and press hotkey buttons to launch and stop project instances
