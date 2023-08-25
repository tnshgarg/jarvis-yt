import subprocess

def open_app(app_name):
    try:
        subprocess.run(["open", f"/Applications/{app_name}.app"])
        print(f"{app_name} opened successfully!")
    except Exception as e:
        print(f"An error occurred while opening {app_name}: {e}")
