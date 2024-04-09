from app import create_app


server = create_app()
server.run(port="8050", debug=True)
