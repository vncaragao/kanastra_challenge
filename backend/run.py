from app import app

@app.route('/')
def home():   # Remove double bracket
    return 'Healthy'  # The templates folder is already picked

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)