start /MAX cmd /k "title RUN && cd venv/Scripts && activate && cd .. && cd .. && cls && waitress-serve --listen=127.0.0.1:10001 Main.wsgi:application"