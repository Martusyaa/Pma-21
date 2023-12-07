import json

def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def get_assets():
    data = load_data()
    return data['assets']

def add_asset(new_asset):
    data = load_data()
    data['assets'].append(new_asset)
    save_data(data)
    return data['assets']

def update_asset(asset_id, update_info):
    data = load_data()
    for asset in data['assets']:
        if asset['id'] == asset_id:
            asset.update(update_info)
            break
    save_data(data)
    return data['assets']

def delete_asset(asset_id):
    data = load_data()
    for asset in data['assets']:
        if asset['id'] == asset_id:
            data['assets'].remove(asset)
            break
    save_data(data)
    return data['assets']
