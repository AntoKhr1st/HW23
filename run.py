from lesson23_project_source.app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(port=25000)