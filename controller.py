import subprocess
import sys
import os
import time


def CONTROLLER():
    print("Honeypot Controller started, booting up honeypot instances")
    time.sleep(0.5)

    os.makedirs("Honeypot-Logs", exist_ok=True)


def HONEYPOT_INSTANCE_1():
    print("[CONTROLLER] Starting honeypot_user_1...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_1 successfully started.")
    return subprocess.Popen([sys.executable, '-u', "honeypot_1.py"])


def HONEYPOT_INSTANCE_2():
    print("[CONTROLLER] Starting honeypot_user_2...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_2 successfully started.")
    return subprocess.Popen([sys.executable, '-u', "honeypot_2.py"])


def HONEYPOT_INSTANCE_3():
    print("[CONTROLLER] Starting honeypot_user_3...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_3 successfully started.")
    return subprocess.Popen([sys.executable, '-u', "honeypot_3.py"])


def HONEYPOT_INSTANCE_4():
    print("[CONTROLLER] Starting honeypot_user_4...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_4 successfully started.")
    return subprocess.Popen([sys.executable, '-u', "honeypot_4.py"])


def HONEYPOT_INSTANCE_5():
    print("[CONTROLLER] Starting honeypot_user_5...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_5 successfully started.")
    return subprocess.Popen([sys.executable, '-u', "honeypot_5.py"])


def HONEYPOT_INSTANCE_6():
    print("[CONTROLLER] Starting honeypot_user_6...")
    time.sleep(0.2)
    print("[CONTROLLER] honeypot_user_6 successfully started.")
    return subprocess.Popen([sys.executable, '-u', "honeypot_6.py"])


if __name__ == "__main__":
    CONTROLLER()
    processes = [
        HONEYPOT_INSTANCE_1(),
        HONEYPOT_INSTANCE_2(),
        HONEYPOT_INSTANCE_3(),
        HONEYPOT_INSTANCE_4(),
        HONEYPOT_INSTANCE_5(),
        HONEYPOT_INSTANCE_6(),
    ]
    try:
        for p in processes:
            p.wait()
    except KeyboardInterrupt:
        print("\n[CONTROLLER] Shutdown signal received. Stopping all instances...")
        for p in processes:
            p.terminate()
        for p in processes:
            p.wait()
        print("[CONTROLLER] All instances stopped.")
