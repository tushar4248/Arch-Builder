from app import create_app

# Create Flask app instance
app = create_app()

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=8000)
