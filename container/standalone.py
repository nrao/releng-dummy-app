from dummy_app import init_app
import multiprocessing
import os
import gunicorn.app.base

def number_of_workers():
    return  (multiprocessing.cpu_count() * 2) + 1

class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('0.0.0.0', '5000'),
        'workers': number_of_workers(),
        'accesslog': "-",
        'access_log_format': "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sμs"
    }
    path = os.environ.get("CONTEXT_PATH", "/").strip().rstrip("/")
    if path not in ("", "/"):
        os.environ["SCRIPT_NAME"] = path
    app = init_app()
    StandaloneApplication(app, options).run()
