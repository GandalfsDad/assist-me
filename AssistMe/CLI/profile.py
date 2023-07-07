import os

HOME = os.path.expanduser('~')
ASSISTME_DIR = os.path.join(HOME, '.assistme')

def load_profile(profile_name: str):
    filename = os.path.join(ASSISTME_DIR, f'{profile_name}.txt')
    if not os.path.exists(filename):
        raise FileNotFoundError(f'Profile {profile_name} not found')
    with open(filename, 'r') as f:
        return f.read()

def save_profile(profile_name: str, profile_prompt: str):
    if not os.path.exists(ASSISTME_DIR):
        os.mkdir(ASSISTME_DIR)
    
    filename = os.path.join(ASSISTME_DIR, f'{profile_name}.txt')
    
    with open(filename, 'w') as f:
        f.write(profile_prompt)
    