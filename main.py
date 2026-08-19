import dolphin_memory_engine as dme
import os
import subprocess

def clear_console():
    command = 'cls' if os.name == "nt" else "clear"
    subprocess.run(command, shell=True)

def main():
    clear_console()
    print("Mario Party 4 Autosplitter\n\n1. Configure and start autosplitter.\n2. Exit.\n")

    selection1 = input("Select an option: ")

    if selection1 == "1":
        clear_console()
        print("Mario Party 4 Autosplitter\n\nSelect Game Region:\n1. NTSC-J\n")
        selection2 = input("Select an option: ")
    elif selection1 == "2":
        print("\nExiting.")
        exit()
    else:
        print("\nInvalid option.\nPress Enter to Retry.\n")
        invalidopt = input()
        main()

    if selection2 == "1":
        clear_console()
        print("Mario Party 4 Autosplitter\n\nSelect Category:\n1. Individual Boards (Not Board Specific)\n")
        selection3 = input("Select an option: ")
    else:
        print("\nInvalid option.\nPress Enter to Retry.\n")
        invalidopt = input()
        main()

    if selection3 == "1":
        print("Hooking Dolphin...")
        dme.hook()
        
        attempts = 0
        while not dme.is_hooked() and attempts < 20:
            import time
            time.sleep(0.1)
            attempts += 1

        if dme.is_hooked():
            print("Dolphin Hooked successfully.\n")
            currentturn = dme.read_byte(0x8018F99C)
            print("You are on turn", currentturn)
        else:
            print("Could not hook to Dolphin. Is the game running?")

    else:
        print("\nInvalid option.\nPress Enter to Retry.\n")
        invalidopt = input()
        main()
 
main()