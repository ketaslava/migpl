import subprocess
import keyboard

# ======= SETTINGS ======= #

export_template_path = "templates/linux_debug.x86_64"

key_run = 'f3'
key_stop = 'f4'

process_instances_count = 5
array_process_arguments = [
    ["Arg1", "Arg2"], # First instance arguments
    ["Arg1", "Arg2"], # Second instance arguments
    ["Arg1"], # Third instance arguments
]

# ======= ======== ======= #

processes = []
new_command = []


def processes_run(queue_position):
    global processes, export_template_path, new_command
    args = []
    new_command = []
    if not queue_position >= len(array_process_arguments):
        if isinstance(array_process_arguments[queue_position], list):
            args = array_process_arguments[queue_position]
    new_command.append(export_template_path)
    for arg in args:
        new_command.append(str(arg))
    print(">> Run command array " + str(new_command) + " \n")
    processes.append(subprocess.Popen(new_command))
    pass


def processes_stop():
    global processes
    if len(processes) > 0:
        process = processes[len(processes) - 1]
        process.terminate()
        processes.remove(process)


def run_all():
    print(">> Run all \n")
    i = 0
    while i < process_instances_count:
        processes_run(i)
        i += 1


def stop_all():
    global processes
    i = 0
    start_len = len(processes)
    while i < start_len:
        processes_stop()
        i += 1
    print(">> Stop all \n")


def on_key_press(event):
    if event.name == key_run:
        run_all()
    if event.name == key_stop:
        stop_all()


def main():
    keyboard.on_press(on_key_press)
    print(f"""\n\n
>> Wellcome to MIGPL <<
multi instance godot project launcher
from Ketoslava Ket and KTVINCCO
http://ktvincco.com/keta/contacts/
https://github.com/ketoslavaket/migpl

instrunction:
* Press {key_run} to run processes
* Press {key_stop} to stop all processes
* Change other parameters in the script settings
\n""")
    while True:
        pass


if __name__ == '__main__':
    main()
